/**
 * TERAS React Components v1.0
 * Componentes base siguiendo Brand Manual TERAS v1.0
 * 
 * Requiere: tokens.css importado en el root
 */

import React, { ButtonHTMLAttributes, InputHTMLAttributes, ReactNode } from 'react';

// ================================================
// TIPOS
// ================================================

interface TerasButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: 'primary' | 'secondary' | 'ghost';
    size?: 'sm' | 'md' | 'lg';
    children: ReactNode;
}

interface TerasCardProps {
    title?: string;
    description?: string;
    children?: ReactNode;
    className?: string;
}

interface TerasInputProps extends InputHTMLAttributes<HTMLInputElement> {
    label?: string;
    error?: string;
}

interface TerasHeadingProps {
    level: 1 | 2 | 3 | 4 | 5;
    children: ReactNode;
    className?: string;
}

// ================================================
// ESTILOS BASE (Inline para garantizar cumplimiento)
// ================================================

const baseStyles = {
    heading: {
        fontFamily: "'Matter', 'Verdana', sans-serif",
        fontWeight: 400, // NUNCA cambiar - jerarquía solo por tamaño
        color: '#000000',
        lineHeight: 1.2,
    },
    body: {
        fontFamily: "'Messina Serif', 'Georgia', serif",
        fontWeight: 400,
        color: '#000000',
        lineHeight: 1.5,
    },
    bodySecondary: {
        fontFamily: "'Messina Serif', 'Georgia', serif",
        fontWeight: 400,
        color: '#6F7173',
        lineHeight: 1.5,
    },
};

// ================================================
// TERAS BUTTON
// ================================================

export const TerasButton: React.FC<TerasButtonProps> = ({
    variant = 'primary',
    size = 'md',
    children,
    className = '',
    ...props
}) => {
    const variantStyles = {
        primary: {
            backgroundColor: '#EA3348',
            color: '#FFFFFF',
            border: 'none',
        },
        secondary: {
            backgroundColor: 'transparent',
            color: '#000000',
            border: '1px solid #000000',
        },
        ghost: {
            backgroundColor: 'transparent',
            color: '#000000',
            border: 'none',
        },
    };

    const sizeStyles = {
        sm: { padding: '8px 16px', fontSize: '14px' },
        md: { padding: '12px 24px', fontSize: '16px' },
        lg: { padding: '16px 32px', fontSize: '18px' },
    };

    return (
        <button
            className={`teras-btn ${className}`}
            style={{
                fontFamily: "'Matter', 'Verdana', sans-serif",
                fontWeight: 400,
                borderRadius: 0, // Estética técnica
                cursor: 'pointer',
                transition: 'opacity 150ms ease-out',
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '8px',
                ...variantStyles[variant],
                ...sizeStyles[size],
            }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.9')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
            {...props}
        >
            {children}
        </button>
    );
};

// ================================================
// TERAS CARD
// ================================================

export const TerasCard: React.FC<TerasCardProps> = ({
    title,
    description,
    children,
    className = '',
}) => {
    return (
        <article
            className={`teras-card ${className}`}
            style={{
                backgroundColor: '#FFFFFF',
                border: '1px solid #EBEBEB',
                borderRadius: 0,
                padding: '24px',
                transition: 'border-color 150ms ease-out, box-shadow 150ms ease-out',
            }}
        >
            {title && (
                <h3
                    style={{
                        ...baseStyles.heading,
                        fontSize: '20px',
                        marginBottom: '16px',
                    }}
                >
                    {title}
                </h3>
            )}
            {description && (
                <p
                    style={{
                        ...baseStyles.bodySecondary,
                        marginBottom: '16px',
                    }}
                >
                    {description}
                </p>
            )}
            {children}
        </article>
    );
};

// ================================================
// TERAS HEADING
// ================================================

export const TerasHeading: React.FC<TerasHeadingProps> = ({
    level,
    children,
    className = '',
}) => {
    const sizes = {
        1: '40px',
        2: '32px',
        3: '24px',
        4: '20px',
        5: '18px',
    };

    const Tag = `h${level}` as keyof JSX.IntrinsicElements;

    return (
        <Tag
            className={`teras-heading ${className}`}
            style={{
                ...baseStyles.heading,
                fontSize: sizes[level],
            }}
        >
            {children}
        </Tag>
    );
};

// ================================================
// TERAS TEXT (Párrafo)
// ================================================

export const TerasText: React.FC<{
    variant?: 'primary' | 'secondary';
    size?: 'sm' | 'base' | 'lg';
    children: ReactNode;
    className?: string;
}> = ({
    variant = 'primary',
    size = 'base',
    children,
    className = '',
}) => {
        const sizes = { sm: '14px', base: '16px', lg: '18px' };
        const style = variant === 'primary' ? baseStyles.body : baseStyles.bodySecondary;

        return (
            <p
                className={className}
                style={{ ...style, fontSize: sizes[size] }}
            >
                {children}
            </p>
        );
    };

// ================================================
// TERAS INPUT
// ================================================

export const TerasInput: React.FC<TerasInputProps> = ({
    label,
    error,
    className = '',
    ...props
}) => {
    return (
        <div className={className}>
            {label && (
                <label
                    style={{
                        display: 'block',
                        marginBottom: '8px',
                        ...baseStyles.heading,
                        fontSize: '14px',
                    }}
                >
                    {label}
                </label>
            )}
            <input
                style={{
                    width: '100%',
                    padding: '12px 16px',
                    border: error ? '1px solid #EA3348' : '1px solid #EBEBEB',
                    borderRadius: '2px',
                    backgroundColor: '#FFFFFF',
                    color: '#000000',
                    fontFamily: "'Messina Serif', 'Georgia', serif",
                    fontSize: '16px',
                    transition: 'border-color 150ms ease-out',
                    outline: 'none',
                }}
                onFocus={(e) => (e.currentTarget.style.borderColor = '#EA3348')}
                onBlur={(e) => (e.currentTarget.style.borderColor = error ? '#EA3348' : '#EBEBEB')}
                {...props}
            />
            {error && (
                <span
                    style={{
                        display: 'block',
                        marginTop: '4px',
                        color: '#EA3348',
                        fontSize: '12px',
                        ...baseStyles.body,
                    }}
                >
                    {error}
                </span>
            )}
        </div>
    );
};

// ================================================
// TERAS HEADER
// ================================================

export const TerasHeader: React.FC<{
    logo: string;
    navItems: { label: string; href: string }[];
}> = ({ logo, navItems }) => {
    return (
        <header
            style={{
                backgroundColor: '#FFFFFF',
                padding: '24px 32px',
                borderBottom: '1px solid #EBEBEB',
            }}
        >
            <nav
                style={{
                    maxWidth: '1200px',
                    margin: '0 auto',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                }}
            >
                <img
                    src={logo}
                    alt="TERAS"
                    style={{ minWidth: '150px', height: 'auto' }}
                />
                <div style={{ display: 'flex', gap: '32px' }}>
                    {navItems.map((item) => (
                        <a
                            key={item.href}
                            href={item.href}
                            style={{
                                ...baseStyles.heading,
                                fontSize: '14px',
                                textDecoration: 'none',
                                transition: 'color 150ms ease-out',
                            }}
                            onMouseEnter={(e) => (e.currentTarget.style.color = '#EA3348')}
                            onMouseLeave={(e) => (e.currentTarget.style.color = '#000000')}
                        >
                            {item.label}
                        </a>
                    ))}
                </div>
            </nav>
        </header>
    );
};

// ================================================
// TERAS FOOTER
// ================================================

export const TerasFooter: React.FC<{
    logoNegative: string;
    children?: ReactNode;
}> = ({ logoNegative, children }) => {
    return (
        <footer
            style={{
                backgroundColor: '#EA3348',
                color: '#FFFFFF',
                padding: '48px 32px',
                position: 'relative',
                overflow: 'hidden',
            }}
        >
            <div
                style={{
                    maxWidth: '1200px',
                    margin: '0 auto',
                    position: 'relative',
                    zIndex: 10,
                }}
            >
                <img
                    src={logoNegative}
                    alt="TERAS"
                    style={{ minWidth: '150px', marginBottom: '32px' }}
                />
                {children}
            </div>
        </footer>
    );
};

// ================================================
// TERAS SECTION
// ================================================

export const TerasSection: React.FC<{
    variant?: 'default' | 'alt' | 'red';
    children: ReactNode;
    className?: string;
}> = ({ variant = 'default', children, className = '' }) => {
    const backgrounds = {
        default: '#FFFFFF',
        alt: '#F7F7F7',
        red: '#EA3348',
    };

    const textColors = {
        default: '#000000',
        alt: '#000000',
        red: '#FFFFFF',
    };

    return (
        <section
            className={className}
            style={{
                backgroundColor: backgrounds[variant],
                color: textColors[variant],
                padding: '64px 32px',
            }}
        >
            <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
                {children}
            </div>
        </section>
    );
};

// ================================================
// TERAS BADGE
// ================================================

export const TerasBadge: React.FC<{
    children: ReactNode;
    variant?: 'default' | 'red' | 'grey';
}> = ({ children, variant = 'default' }) => {
    const styles = {
        default: { backgroundColor: '#EBEBEB', color: '#000000' },
        red: { backgroundColor: '#FBD6DA', color: '#EA3348' },
        grey: { backgroundColor: '#C6C9CC', color: '#000000' },
    };

    return (
        <span
            style={{
                display: 'inline-flex',
                alignItems: 'center',
                padding: '4px 12px',
                fontSize: '12px',
                fontFamily: "'Matter', 'Verdana', sans-serif",
                fontWeight: 400,
                borderRadius: 0,
                ...styles[variant],
            }}
        >
            {children}
        </span>
    );
};
