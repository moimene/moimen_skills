const DEFAULT_TIMEOUT = 10_000;
export class DigitalTrustClient {
    baseUrl;
    token;
    timeoutMs;
    constructor(config) {
        this.baseUrl = config.baseUrl.replace(/\/$/, '');
        this.token = config.token;
        this.timeoutMs = config.timeoutMs ?? DEFAULT_TIMEOUT;
    }
    setToken(token) {
        this.token = token;
    }
    async login(params) {
        const scope = params.scope ?? 'token';
        const url = new URL(params.loginUrl);
        url.searchParams.set('grant_type', 'client_credentials');
        url.searchParams.set('client_id', params.clientId);
        url.searchParams.set('client_secret', params.clientSecret);
        url.searchParams.set('scope', scope);
        const res = await fetch(url.toString(), {
            method: 'POST',
            headers: { Accept: 'application/json' },
            signal: AbortSignal.timeout(this.timeoutMs),
        });
        if (!res.ok) {
            const text = await res.text();
            throw new Error(`Login failed (${res.status}): ${text}`);
        }
        const data = (await res.json());
        this.token = data.access_token;
        return data;
    }
    async get(path, query) {
        const url = new URL(this.baseUrl + path);
        if (query) {
            Object.entries(query).forEach(([k, v]) => {
                if (v !== undefined)
                    url.searchParams.set(k, String(v));
            });
        }
        return this.request('GET', url.toString());
    }
    async post(path, body) {
        const url = this.baseUrl + path;
        return this.request('POST', url, body);
    }
    async patch(path, body) {
        const url = this.baseUrl + path;
        return this.request('PATCH', url, body);
    }
    async delete(path) {
        const url = this.baseUrl + path;
        return this.request('DELETE', url);
    }
    async getBinary(path) {
        if (!this.token)
            throw new Error('Missing bearer token. Call login() first or set token.');
        const url = this.baseUrl + path;
        const res = await fetch(url, {
            method: 'GET',
            headers: {
                Accept: 'application/octet-stream',
                Authorization: `Bearer ${this.token}`,
            },
            signal: AbortSignal.timeout(this.timeoutMs),
        });
        const arrayBuf = await res.arrayBuffer();
        const contentType = res.headers.get('content-type') || 'application/octet-stream';
        if (!res.ok) {
            throw new Error(`HTTP ${res.status} ${res.statusText}`);
        }
        const base64 = Buffer.from(arrayBuf).toString('base64');
        return { contentType, base64 };
    }
    async request(method, url, body) {
        if (!this.token)
            throw new Error('Missing bearer token. Call login() first or set token.');
        const headers = {
            Accept: 'application/json',
            Authorization: `Bearer ${this.token}`,
        };
        let payload;
        if (body !== undefined) {
            headers['Content-Type'] = 'application/json';
            payload = JSON.stringify(body);
        }
        const res = await fetch(url, {
            method,
            headers,
            body: payload,
            signal: AbortSignal.timeout(this.timeoutMs),
        });
        const contentType = res.headers.get('content-type') || '';
        const isJson = contentType.includes('application/json');
        const text = await res.text();
        const parsed = isJson && text ? safeJson(text) : text;
        if (!res.ok) {
            throw new Error(`HTTP ${res.status} ${res.statusText}: ${text}`);
        }
        return parsed;
    }
}
function safeJson(text) {
    try {
        return JSON.parse(text);
    }
    catch {
        return text;
    }
}
