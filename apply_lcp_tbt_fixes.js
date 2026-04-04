const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        if (dirPath.includes('node_modules') || dirPath.includes('.git')) return;
        let isDirectory = fs.statSync(dirPath).isDirectory();
        if (isDirectory) {
            walkDir(dirPath, callback);
        } else if (dirPath.endsWith('.html')) {
            callback(dirPath);
        }
    });
}

walkDir('.', (filePath) => {
    let content = fs.readFileSync(filePath, 'utf8');
    let originalContent = content;

    // GA: Change async to defer
    content = content.replace(/<script\s+async\s+src="https:\/\/www\.googletagmanager\.com\/gtag\/js\?id=G-KR0PGMD050"><\/script>/gi, '<script defer src="https://www.googletagmanager.com/gtag/js?id=G-KR0PGMD050"></script>');

    // Add preload to index.html
    if (filePath === 'index.html' || filePath === './index.html') {
        if (!content.includes('hero-banner-leaves.webp" fetchpriority="high"')) {
            content = content.replace('</head>', '  <link rel="preload" as="image" href="/images/hero-banner-leaves.webp" fetchpriority="high">' + String.fromCharCode(10) + '</head>');
        }
    }

    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
    }
});

console.log('Mobile Performance Optimization Complete');
