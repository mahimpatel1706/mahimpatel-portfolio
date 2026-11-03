/**
 * Design tokens for the portfolio site.
 * Build:  npx tailwindcss@3 -c tailwind.config.js -i assets/css/tailwind.src.css -o assets/css/tailwind.css --minify
 *
 * The standard Tailwind hue families are intentionally re-mapped to a restrained
 * institutional palette (ink navy, cool neutrals, brass accent, muted green / brick),
 * so every existing utility class resolves to the refined brand colours.
 */
module.exports = {
  content: ['./*.html'],
  theme: {
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1200px',
      '2xl': '1440px',
    },
    fontFamily: {
      sans: ['"IBM Plex Sans"', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Helvetica Neue', 'Arial', 'sans-serif'],
      serif: ['"Source Serif 4"', 'Georgia', '"Times New Roman"', 'serif'],
      display: ['"Source Serif 4"', 'Georgia', 'serif'],
      mono: ['"IBM Plex Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
    },
    fontSize: {
      xs: ['0.78rem', { lineHeight: '1.55' }],
      sm: ['0.9rem', { lineHeight: '1.65' }],
      base: ['1rem', { lineHeight: '1.7' }],
      lg: ['1.125rem', { lineHeight: '1.65' }],
      xl: ['1.25rem', { lineHeight: '1.5' }],
      '2xl': ['1.5rem', { lineHeight: '1.35' }],
      '3xl': ['1.875rem', { lineHeight: '1.25' }],
      '4xl': ['2.25rem', { lineHeight: '1.18' }],
      '5xl': ['3rem', { lineHeight: '1.1' }],
      '6xl': ['3.75rem', { lineHeight: '1.05' }],
    },
    borderRadius: {
      none: '0',
      sm: '2px',
      DEFAULT: '3px',
      md: '4px',
      lg: '6px',
      xl: '8px',
      '2xl': '10px',
      full: '9999px',
    },
    boxShadow: {
      xs: '0 1px 0 rgba(11, 36, 71, 0.04)',
      sm: '0 1px 2px rgba(11, 36, 71, 0.05)',
      DEFAULT: '0 1px 3px rgba(11, 36, 71, 0.07)',
      md: '0 4px 14px -4px rgba(11, 36, 71, 0.10)',
      lg: '0 12px 28px -10px rgba(11, 36, 71, 0.16)',
      xl: '0 18px 40px -12px rgba(11, 36, 71, 0.20)',
      '2xl': '0 28px 64px -16px rgba(11, 36, 71, 0.30)',
      none: 'none',
    },
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      white: '#ffffff',
      black: '#000000',
      paper: '#F6F7F9',
      navy: {
        50: '#F3F6FA', 100: '#E6ECF4', 200: '#CBD6E4', 300: '#A6B8CF', 400: '#7B94B3',
        500: '#4E6C93', 600: '#2A5A93', 700: '#1B4577', 800: '#12325E', 900: '#0B2447', 950: '#07142B',
      },
      slate: {
        50: '#F7F8FA', 100: '#EFF1F4', 200: '#E1E5EA', 300: '#CBD1DA', 400: '#98A1AF', 500: '#687282',
        600: '#4B5463', 700: '#363E4C', 800: '#222937', 900: '#141A26', 950: '#0B0F18',
      },
      amber: {
        50: '#FAF7F0', 100: '#F3ECDB', 200: '#E6D9B8', 300: '#D3BE8A', 400: '#BFA161', 500: '#A8864A',
        600: '#8E6F38', 700: '#735A2E', 800: '#5A4625', 900: '#43341C', 950: '#2A2111',
      },
      yellow: {
        50: '#FAF7F0', 100: '#F3ECDB', 200: '#E6D9B8', 300: '#D9C48F', 400: '#BFA161', 500: '#A8864A',
        600: '#8E6F38', 700: '#735A2E', 800: '#5A4625', 900: '#43341C', 950: '#2A2111',
      },
      emerald: {
        50: '#F2F7F4', 100: '#E3EEE8', 200: '#C6DDD0', 300: '#9CC9B1', 400: '#6FAE8E', 500: '#478A6B',
        600: '#2F7155', 700: '#265C45', 800: '#1F4A39', 900: '#193C2F', 950: '#0E2219',
      },
      rose: {
        50: '#FAF3F2', 100: '#F4E4E1', 200: '#E8C9C4', 300: '#DDA8A0', 400: '#C98378', 500: '#A9564B',
        600: '#923F36', 700: '#77322B', 800: '#5E2823', 900: '#4A201C', 950: '#2B110F',
      },
      sky: {
        50: '#F2F5F9', 100: '#E4EAF2', 200: '#CBD6E4', 300: '#A6B8CF', 400: '#8AA3C2', 500: '#5A7699',
        600: '#45607F', 700: '#384E69', 800: '#2E4057', 900: '#263446', 950: '#151D29',
      },
      blue: {
        50: '#F2F5F9', 100: '#E4EAF2', 200: '#CBD6E4', 300: '#A6B8CF', 400: '#8AA3C2', 500: '#5A7699',
        600: '#45607F', 700: '#384E69', 800: '#2E4057', 900: '#263446', 950: '#151D29',
      },
      indigo: {
        50: '#F2F5F9', 100: '#E4EAF2', 200: '#CBD6E4', 300: '#A6B8CF', 400: '#8AA3C2', 500: '#5A7699',
        600: '#45607F', 700: '#384E69', 800: '#2E4057', 900: '#263446', 950: '#151D29',
      },
      cyan: {
        50: '#F2F5F9', 100: '#E4EAF2', 200: '#CBD6E4', 300: '#A6B8CF', 400: '#8AA3C2', 500: '#5A7699',
        600: '#45607F', 700: '#384E69', 800: '#2E4057', 900: '#263446', 950: '#151D29',
      },
      purple: {
        50: '#F2F5F9', 100: '#E4EAF2', 200: '#CBD6E4', 300: '#A6B8CF', 400: '#8AA3C2', 500: '#5A7699',
        600: '#45607F', 700: '#384E69', 800: '#2E4057', 900: '#263446', 950: '#151D29',
      },
    },
    extend: {
      maxWidth: { '8xl': '88rem' },
    },
  },
  plugins: [],
};
