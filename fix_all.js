const fs = require('fs');
const path = require('path');

const repoDir = '/opt/build/repo';
const siteUrl = 'https://deirdrekuvaas.com';

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        if (dirPath.includes('node_modules') || dirPath.includes('.git') || dirPath.includes('.netlify')) return;
        let isDirectory = fs.statSync(dirPath).isDirectory();
        if (isDirectory) {
            walkDir(dirPath, callback);
        } else if (dirPath.endsWith('.html')) {
            callback(dirPath);
        }
    });
}

function processHtmlFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;

    // 1. URL Sanitization: Remove trailing slash from img src and og:image content
    content = content.replace(/(<meta\s+property="og:image"\s+content="[^"]+\.(?:jpg|png|webp))\/+(")/gi, '$1$2');
    content = content.replace(/(<img\s+[^>]*src="[^"]+\.(?:jpg|png|webp))\/+(")/gi, '$1$2');

    // 2. Canonical Consistency
    let relativePath = filePath.replace(repoDir, '').replace(/\\/g, '/'); // e.g., /index.html or /faqs/index.html
    let expectedUrl = siteUrl + '/';
    if (relativePath !== '/index.html') {
        let dir = path.dirname(relativePath);
        if (dir !== '/') {
            expectedUrl = siteUrl + dir;
        } else {
            expectedUrl = siteUrl + relativePath.replace('/index.html', ''); // fallback
        }
    }
    
    // Replace <link rel="canonical" href="...">
    content = content.replace(/<link\s+rel="canonical"\s+href="[^"]*"/gi, `<link rel="canonical" href="${expectedUrl}"`);
    // Replace <meta property="og:url" content="...">
    content = content.replace(/<meta\s+property="og:url"\s+content="[^"]*"/gi, `<meta property="og:url" content="${expectedUrl}"`);

    // 3. Security Update: Add rel="noopener noreferrer" to external links
    content = content.replace(/<a\s+([^>]+)>/gi, (match, attrs) => {
        if (attrs.includes('href="http') && !attrs.includes('href="https://deirdrekuvaas.com')) {
            if (!attrs.includes('rel=')) {
                return `<a ${attrs} rel="noopener noreferrer">`;
            } else {
                let relMatch = attrs.match(/rel="([^"]*)"/);
                if (relMatch) {
                    let rels = relMatch[1].split(' ');
                    let hasNoopener = rels.includes('noopener');
                    let hasNoreferrer = rels.includes('noreferrer');
                    if (!hasNoopener || !hasNoreferrer) {
                        let newRels = new Set(rels);
                        newRels.add('noopener');
                        newRels.add('noreferrer');
                        let newAttrs = attrs.replace(/rel="([^"]*)"/, `rel="${Array.from(newRels).join(' ').trim()}"`);
                        return `<a ${newAttrs}>`;
                    }
                }
            }
        }
        return match;
    });

    // 4. Performance Polish: Add explicit width and height to main logo and banner images
    // Based on search results, logo is inner-world-counseling-logo.png and banner might be deirdre-kuvaas.jpg or unsplash image
    // I will regex to add width/height if missing.
    content = content.replace(/<img\s+([^>]+)>/gi, (match, attrs) => {
        let newAttrs = attrs;
        let isMainLogo = newAttrs.includes('inner-world-counseling-logo.png');
        let isSecondaryLogo = newAttrs.includes('inner-world-counseling-logo-secondary.png');
        let isBanner1 = newAttrs.includes('deirdre-kuvaas.jpg');
        let isBanner2 = newAttrs.includes('photo-1506126613408-eca07ce68773');
        
        if (isMainLogo && !newAttrs.includes('width=')) {
            newAttrs += ' width="110" height="110"';
        }
        if (isSecondaryLogo && !newAttrs.includes('width=')) {
            newAttrs += ' width="532" height="513"';
        }
        if (isBanner1 && !newAttrs.includes('width=')) {
            newAttrs += ' width="1920" height="1280"';
        }
        if (isBanner2 && !newAttrs.includes('width=')) {
            newAttrs += ' width="800" height="533"';
        }
        if (newAttrs !== attrs) {
            return `<img ${newAttrs.trim()}>`;
        }
        return match;
    });

    // 5. WebP Readiness: If social share image exists in webp, point to it.
    let webpShareImage = path.join(repoDir, 'images', 'inner-world-counseling-social-share.webp');
    if (fs.existsSync(webpShareImage)) {
        content = content.replace(/inner-world-counseling-social-share\.jpg/g, 'inner-world-counseling-social-share.webp');
    }

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('Fixed:', filePath);
    }
}

walkDir(repoDir, processHtmlFile);
