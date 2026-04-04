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

const SITE_DOMAIN = "deirdrekuvaas.com"; 

walkDir('.', (filePath) => {
    let content = fs.readFileSync(filePath, 'utf8');
    let originalContent = content;

    // 1. Performance: Defer Metricool
    // Original: c=document.createElement("script");c.type="text/javascript";c.src="https://tracker.metricool.com/resources/be.js";
    content = content.replace(/c=document\.createElement\("script"\);c\.type="text\/javascript";c\.src="https:\/\/tracker\.metricool\.com\/resources\/be\.js";/g, 'c=document.createElement("script");c.type="text/javascript";c.defer=true;c.src="https://tracker.metricool.com/resources/be.js";');

    // 1b. Performance: Defer Psychology Today
    content = content.replace(/<script\s+src="https:\/\/member\.psychologytoday\.com\/verified-seal\.js"\s+type="text\/javascript"/g, '<script src="https://member.psychologytoday.com/verified-seal.js" type="text/javascript" defer');

    // 2. Accessibility: Ensure all <img> tags have descriptive alt attributes.
    content = content.replace(/<img\s+([^>]+)>/gi, (match, attrs) => {
        let newAttrs = attrs;
        // If alt is missing entirely or empty, infer from filename
        if (!/alt\s*=/i.test(attrs) || /alt=""/i.test(attrs)) {
            let srcMatch = attrs.match(/src="([^"]+)"/i);
            let altText = "Image";
            if (srcMatch) {
                let filename = srcMatch[1].split('/').pop().split('.')[0];
                altText = filename.replace(/-/g, ' ');
                // Capitalize first letter of each word
                altText = altText.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
            }
            if (/alt=""/i.test(attrs)) {
                newAttrs = newAttrs.replace(/alt=""/i, `alt="${altText}"`);
            } else {
                newAttrs += ` alt="${altText}"`;
            }
        }
        return `<img ${newAttrs}>`;
    });

    // 3. Best Practices: Ensure all external links include rel="noopener" or rel="noreferrer"
    content = content.replace(/<a\s+([^>]+)>/gi, (match, attrs) => {
        let hrefMatch = attrs.match(/href="([^"]+)"/i);
        if (hrefMatch) {
            let href = hrefMatch[1];
            if (href.startsWith('http') && !href.includes(SITE_DOMAIN)) {
                if (!/rel\s*=/i.test(attrs)) {
                    return `<a ${attrs} rel="noopener noreferrer">`;
                } else if (!/(noopener|noreferrer)/i.test(attrs)) {
                    return `<a ${attrs.replace(/rel="([^"]*)"/i, 'rel="$1 noopener noreferrer"')}>`;
                }
            }
        }
        return match;
    });

    // 4. Images: explicit width and height to logos and banners
    // Logo 1
    content = content.replace(/(<img\s+[^>]*src="\/images\/inner-world-counseling-logo\.png"[^>]*)>/gi, (match, p1) => {
        let newImg = p1;
        if (!/width\s*=/i.test(newImg)) newImg += ' width="431"';
        if (!/height\s*=/i.test(newImg)) newImg += ' height="389"';
        return newImg + '>';
    });
    
    // Logo 2
    content = content.replace(/(<img\s+[^>]*src="\/images\/inner-world-counseling-logo-secondary\.png"[^>]*)>/gi, (match, p1) => {
        let newImg = p1;
        if (!/width\s*=/i.test(newImg)) newImg += ' width="532"';
        if (!/height\s*=/i.test(newImg)) newImg += ' height="513"';
        return newImg + '>';
    });

    // Banner deirdre-kuvaas.jpg
    content = content.replace(/(<img\s+[^>]*src="\/images\/deirdre-kuvaas\.jpg"[^>]*)>/gi, (match, p1) => {
        let newImg = p1;
        if (!/width\s*=/i.test(newImg)) newImg += ' width="1920"';
        if (!/height\s*=/i.test(newImg)) newImg += ' height="1280"';
        return newImg + '>';
    });

    // Banner Unsplash image in index.html
    content = content.replace(/(<img\s+[^>]*src="https:\/\/images\.unsplash\.com\/photo-1506126613408-eca07ce68773\?w=800&q=80"[^>]*)>/gi, (match, p1) => {
        let newImg = p1;
        if (!/width\s*=/i.test(newImg)) newImg += ' width="800"';
        if (!/height\s*=/i.test(newImg)) newImg += ' height="533"'; // Standard ratio
        return newImg + '>';
    });

    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
    }
});
console.log("HTML updates completed.");
