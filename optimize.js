const fs = require('fs');
const glob = require('glob');

const htmlFiles = glob.sync('**/*.html', { ignore: ['node_modules/**'] });

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let original = content;

    // 1. Render-Blocking Scripts -> defer
    // SimplePractice
    content = content.replace(/<script src="https:\/\/widget-cdn\.simplepractice\.com\/assets\/integration-1\.0\.js"><\/script>/g, '<script src="https://widget-cdn.simplepractice.com/assets/integration-1.0.js" defer></script>');
    
    // js/main.js
    content = content.replace(/<script src="\/js\/main\.js"><\/script>/g, '<script src="/js/main.js" defer></script>');
    
    // 2. Add font-display: swap to CSS
    content = content.replace(/@font-face\s*{([^}]+)}/g, (match, p1) => {
        if (!p1.includes('font-display')) {
            return `@font-face {${p1} font-display: swap; }`;
        }
        return match;
    });

    // 3. Fix Hero image for LCP
    const heroRegex = /<section\s+aria-label="Lush green leaves macro shot representing growth and mental wellness."\s+class="hero\s+hero-section-wrapper\s+extracted-style-1"\s+fetchpriority="high"\s+loading="eager"\s+role="img">\s*<div\s+class="hero__content">/;
    if (heroRegex.test(content)) {
        const replacement = `<section class="hero hero-section-wrapper" style="position: relative;">
<picture style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
  <source media="(max-width: 600px)" srcset="/.netlify/images?url=/images/hero-banner-leaves.webp&w=600">
  <img src="/images/hero-banner-leaves.webp" alt="Lush green leaves macro shot representing growth and mental wellness." loading="eager" fetchpriority="high" style="width: 100%; height: 100%; object-fit: cover;">
</picture>
<div class="hero__content" style="position: relative; z-index: 1;">`;
        content = content.replace(heroRegex, replacement);
    }

    if (original !== content) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Updated HTML:', file);
    }
});

// Update style.css
let css = fs.readFileSync('css/style.css', 'utf8');
let originalCss = css;

// Add touch-action for INP
if (!css.includes('touch-action: manipulation')) {
    css += `
/* Improve INP */
a, button, input[type="submit"], input[type="button"], .nav-toggle, .btn { touch-action: manipulation; }
`;
}

// Add font-display swap if any @font-face exists
css = css.replace(/@font-face\s*{([^}]+)}/g, (match, p1) => {
    if (!p1.includes('font-display')) {
        return `@font-face {${p1} font-display: swap; }`;
    }
    return match;
});

if (css !== originalCss) {
    fs.writeFileSync('css/style.css', css, 'utf8');
    console.log('Updated CSS: css/style.css');
}
