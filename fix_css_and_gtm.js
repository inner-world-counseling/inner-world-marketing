const fs = require('fs');
const glob = require('glob');

// 1. Fix CSS
let css = fs.readFileSync('css/style.css', 'utf8');

// Contrast fixes
css = css.replace(
  /(\.main-nav__link\s*\{\s*[^}]*?color:\s*)var\(--color-olive-dark\)(;)/,
  '$1#2D3436$2'
);

css = css.replace(
  /(\.main-nav__link:hover,\s*\.main-nav__link--active\s*\{\s*color:\s*)var\(--color-sage-dark\)(;)/,
  '$1#2D3436$2'
);

css = css.replace(
  /\.section--sage h2,\s*\.section--sage h3\s*\{\s*color:\s*var\(--color-olive-dark\);\s*\}/,
  `.section--sage h2 {
  color: var(--color-olive-dark);
}

.section--sage h3 {
  color: #2D3436;
}`
);

// Underline fix
if (!css.includes('.footer a { text-decoration: underline !important; }')) {
  css += "\n.footer a { text-decoration: underline !important; }\n";
}

fs.writeFileSync('css/style.css', css);

// 2. Fix GTM script across HTML files
const htmlFiles = glob.sync('**/*.html', { ignore: ['node_modules/**'] });

const oldGTM = /<!-- Google Analytics -->\s*<script>\s*window\.addEventListener\('scroll', \(\) => \{\s*const s = document\.createElement\('script'\);\s*s\.src = "https:\/\/www\.googletagmanager\.com\/gtag\/js\?id=G-KR0PGMD050";\s*s\.defer = true;\s*document\.head\.appendChild\(s\);\s*window\.dataLayer=window\.dataLayer\|\|\[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\('js',new Date\(\)\);\s*gtag\('config','G-KR0PGMD050'\);\s*\}, \{ once: true \}\);\s*<\/script>/;

const newGTM = `<!-- Google Analytics -->
  <script src="https://www.googletagmanager.com/gtag/js?id=G-KR0PGMD050" defer></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-KR0PGMD050');
  </script>`;

htmlFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  
  // Replace complex delayed GTM with standard deferred GTM at bottom
  if (oldGTM.test(content)) {
    content = content.replace(oldGTM, newGTM);
  }
  
  // Check header logo descriptive text (just to be safe)
  // Ensure the <a> tag has aria-label="Inner World Counseling Home" and the <img> has alt="Inner World Counseling Logo"
  const logoRegex = /<a[^>]*href="\/"[^>]*class="site-logo"[^>]*>[\s\S]*?<img[^>]*src="\/images\/inner-world-counseling-logo\.png"[^>]*>[\s\S]*?<\/a>/;
  if (logoRegex.test(content)) {
    let match = content.match(logoRegex)[0];
    if (!match.includes('aria-label="Inner World Counseling Home"')) {
      match = match.replace('<a ', '<a aria-label="Inner World Counseling Home" ');
    }
    if (!match.includes('alt="Inner World Counseling Logo"')) {
      // replace alt if exists, else add
      if (match.includes('alt=')) {
        match = match.replace(/alt="[^"]*"/, 'alt="Inner World Counseling Logo"');
      } else {
        match = match.replace('<img ', '<img alt="Inner World Counseling Logo" ');
      }
    }
    content = content.replace(logoRegex, match);
  }

  // Same check for Roots of healing image, make sure it has an alt
  const rootsRegex = /<img[^>]*roots-of-healing\.webp[^>]*>/;
  if (rootsRegex.test(content)) {
    let match = content.match(rootsRegex)[0];
    if (!match.includes('alt=')) {
      match = match.replace('<img ', '<img alt="Roots of Healing" ');
      content = content.replace(rootsRegex, match);
    }
  }

  fs.writeFileSync(file, content);
});

console.log('Fixes applied successfully.');
