---
name: aplicar-react-best-practices
description: Aplica las mejores prácticas de rendimiento React/Next.js de Vercel Engineering. Úsese al escribir, revisar o refactorizar código React/Next.js para asegurar patrones de rendimiento óptimos. Activar en tareas de componentes React, páginas Next.js, data fetching, optimización de bundle o mejoras de rendimiento.
---

# React Best Practices (Vercel Engineering)

Guía de optimización de rendimiento para aplicaciones React y Next.js.
57 reglas en 8 categorías, priorizadas por impacto.

## Cuándo Aplicar

- Escribir nuevos componentes React o páginas Next.js
- Implementar data fetching (cliente o servidor)
- Revisar código por problemas de rendimiento
- Refactorizar código React/Next.js existente
- Optimizar bundle size o tiempos de carga

---

## Categorías por Prioridad

| Prioridad | Categoría | Impacto | Prefijo |
|-----------|-----------|---------|---------|
| 1 | Eliminar Waterfalls | **CRÍTICO** | `async-` |
| 2 | Bundle Size | **CRÍTICO** | `bundle-` |
| 3 | Rendimiento Servidor | ALTO | `server-` |
| 4 | Data Fetching Cliente | MEDIO-ALTO | `client-` |
| 5 | Re-renders | MEDIO | `rerender-` |
| 6 | Rendimiento Rendering | MEDIO | `rendering-` |
| 7 | Performance JavaScript | BAJO-MEDIO | `js-` |
| 8 | Patrones Avanzados | BAJO | `advanced-` |

---

## 1. Eliminar Waterfalls (CRÍTICO)

### `async-defer-await`
Mueve el `await` a la rama donde realmente se usa.

```typescript
// ❌ Incorrecto
async function getData() {
  const data = await fetchData();
  if (condition) {
    return data;
  }
  return null;
}

// ✅ Correcto
async function getData() {
  if (condition) {
    const data = await fetchData();
    return data;
  }
  return null;
}
```

### `async-parallel`
Usa `Promise.all()` para operaciones independientes.

```typescript
// ❌ Incorrecto - waterfall secuencial
const users = await getUsers();
const posts = await getPosts();
const comments = await getComments();

// ✅ Correcto - paralelo
const [users, posts, comments] = await Promise.all([
  getUsers(),
  getPosts(),
  getComments()
]);
```

### `async-suspense-boundaries`
Usa Suspense para streaming de contenido.

```tsx
// ✅ Correcto
<Suspense fallback={<Loading />}>
  <SlowComponent />
</Suspense>
```

---

## 2. Bundle Size (CRÍTICO)

### `bundle-barrel-imports`
Importa directamente, evita barrel files.

```typescript
// ❌ Incorrecto - importa todo el barrel
import { Button } from '@/components';

// ✅ Correcto - importación directa
import { Button } from '@/components/Button';
```

### `bundle-dynamic-imports`
Usa `next/dynamic` para componentes pesados.

```typescript
// ✅ Correcto
import dynamic from 'next/dynamic';

const HeavyChart = dynamic(() => import('./Chart'), {
  loading: () => <ChartSkeleton />,
  ssr: false
});
```

### `bundle-defer-third-party`
Carga analytics/logging después de hydration.

```typescript
// ✅ Correcto
useEffect(() => {
  import('analytics').then(({ init }) => init());
}, []);
```

### `bundle-preload`
Precarga en hover/focus para velocidad percibida.

```tsx
// ✅ Correcto
<Link 
  href="/dashboard"
  onMouseEnter={() => router.prefetch('/dashboard')}
>
  Dashboard
</Link>
```

---

## 3. Rendimiento Servidor (ALTO)

### `server-cache-react`
Usa `React.cache()` para deduplicación por request.

```typescript
// ✅ Correcto
import { cache } from 'react';

const getUser = cache(async (id: string) => {
  return await db.user.findUnique({ where: { id } });
});
```

### `server-parallel-fetching`
Reestructura componentes para paralelizar fetches.

```tsx
// ✅ Correcto - fetches en paralelo
async function Page() {
  const userPromise = getUser();
  const postsPromise = getPosts();
  
  const [user, posts] = await Promise.all([userPromise, postsPromise]);
  
  return <Dashboard user={user} posts={posts} />;
}
```

### `server-serialization`
Minimiza datos pasados a client components.

```tsx
// ❌ Incorrecto - pasa todo el objeto
<ClientComponent user={fullUserObject} />

// ✅ Correcto - solo lo necesario
<ClientComponent userName={user.name} avatarUrl={user.avatar} />
```

---

## 4. Data Fetching Cliente (MEDIO-ALTO)

### `client-swr-dedup`
Usa SWR para deduplicación automática.

```typescript
// ✅ Correcto
import useSWR from 'swr';

function Profile() {
  const { data, error, isLoading } = useSWR('/api/user', fetcher);
  // SWR deduplica automáticamente peticiones idénticas
}
```

### `client-passive-event-listeners`
Usa listeners pasivos para scroll.

```typescript
// ✅ Correcto
useEffect(() => {
  window.addEventListener('scroll', handler, { passive: true });
  return () => window.removeEventListener('scroll', handler);
}, []);
```

---

## 5. Re-render Optimization (MEDIO)

### `rerender-memo`
Extrae trabajo caro a componentes memoizados.

```tsx
// ✅ Correcto
const ExpensiveList = memo(function ExpensiveList({ items }) {
  return items.map(item => <ExpensiveItem key={item.id} {...item} />);
});
```

### `rerender-derived-state`
Suscríbete a booleanos derivados, no valores raw.

```typescript
// ❌ Incorrecto
const items = useStore(state => state.items);
const hasItems = items.length > 0;

// ✅ Correcto - componente no re-renderiza si el booleano no cambia
const hasItems = useStore(state => state.items.length > 0);
```

### `rerender-functional-setstate`
Usa setState funcional para callbacks estables.

```typescript
// ✅ Correcto
const increment = useCallback(() => {
  setCount(prev => prev + 1);
}, []); // No necesita count como dependencia
```

### `rerender-lazy-state-init`
Pasa función a useState para valores costosos.

```typescript
// ❌ Incorrecto - se ejecuta en cada render
const [data] = useState(expensiveComputation());

// ✅ Correcto - solo se ejecuta una vez
const [data] = useState(() => expensiveComputation());
```

### `rerender-transitions`
Usa `startTransition` para updates no urgentes.

```typescript
// ✅ Correcto
import { startTransition } from 'react';

function handleSearch(query) {
  // Urgente: actualizar input
  setInputValue(query);
  
  // No urgente: filtrar lista
  startTransition(() => {
    setFilteredItems(filterItems(query));
  });
}
```

---

## 6. Rendering Performance (MEDIO)

### `rendering-content-visibility`
Usa `content-visibility` para listas largas.

```css
/* ✅ Correcto */
.list-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 80px;
}
```

### `rendering-hoist-jsx`
Extrae JSX estático fuera de componentes.

```tsx
// ✅ Correcto - definido fuera, no se recrea
const STATIC_HEADER = <header>App Title</header>;

function App() {
  return (
    <>
      {STATIC_HEADER}
      <DynamicContent />
    </>
  );
}
```

### `rendering-conditional-render`
Usa ternario, no `&&` para condicionales.

```tsx
// ❌ Puede renderizar 0
{count && <Message />}

// ✅ Correcto
{count > 0 ? <Message /> : null}
```

---

## 7. JavaScript Performance (BAJO-MEDIO)

### `js-set-map-lookups`
Usa Set/Map para lookups O(1).

```typescript
// ❌ Incorrecto - O(n) cada lookup
const isSelected = selectedIds.includes(id);

// ✅ Correcto - O(1)
const selectedSet = new Set(selectedIds);
const isSelected = selectedSet.has(id);
```

### `js-early-exit`
Retorna temprano de funciones.

```typescript
// ✅ Correcto
function processUser(user) {
  if (!user) return null;
  if (!user.isActive) return null;
  
  // Lógica principal aquí
}
```

### `js-combine-iterations`
Combina múltiples filter/map en un loop.

```typescript
// ❌ Incorrecto - 3 iteraciones
const result = items
  .filter(x => x.active)
  .map(x => x.name)
  .filter(x => x.length > 0);

// ✅ Correcto - 1 iteración
const result = [];
for (const item of items) {
  if (item.active && item.name.length > 0) {
    result.push(item.name);
  }
}
```

---

## 8. Patrones Avanzados (BAJO)

### `advanced-init-once`
Inicializa app una sola vez.

```typescript
// ✅ Correcto
let initialized = false;

function initApp() {
  if (initialized) return;
  initialized = true;
  
  // Setup code
}
```

### `advanced-use-latest`
useLatest para refs de callback estables.

```typescript
// ✅ Correcto
function useLatest<T>(value: T) {
  const ref = useRef(value);
  ref.current = value;
  return ref;
}
```

---

## Checklist de Revisión

### Crítico (siempre verificar)
- [ ] ¿Hay awaits secuenciales que podrían ser paralelos?
- [ ] ¿Hay barrel imports que podrían ser directos?
- [ ] ¿Los componentes pesados usan dynamic import?

### Alto (verificar en PR)
- [ ] ¿Los datos del servidor están minimizados para el cliente?
- [ ] ¿Se usa React.cache() para deduplicación?
- [ ] ¿Los fetches están paralelizados?

### Medio (verificar si hay problemas)
- [ ] ¿Los componentes caros están memoizados?
- [ ] ¿Se usa startTransition para updates no urgentes?
- [ ] ¿Hay estado derivado calculado en render?

---

## Recursos

- [Rules Detalladas](resources/rules/)
- [Vercel Engineering Blog](https://vercel.com/blog)
- [Next.js Performance Docs](https://nextjs.org/docs/app/building-your-application/optimizing)

---

## Regla Final

> **Prioriza: 1) Eliminar waterfalls 2) Reducir bundle 3) Paralelizar servidor. El resto es optimización secundaria.**
