const fs = require('fs');
const path = require('path');

const repoDir = '/opt/build/repo';

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

    // 2. Fix Broken Social Metadata
    content = content.replace(/inner-world-counseling-social-share\.jpg/g, 'deirdre-kuvaas.jpg');

    // 3. Sanitize URLs (metadata)
    // Remove trailing slashes like .jpg/ or .png/ before the quote
    content = content.replace(/(content="[^"]+\.(?:jpg|png))\/+(")/gi, '$1$2');

    // 4. Global Security Fix
    // Add rel="noopener noreferrer" to all external links
    content = content.replace(/<a\s+([^>]+)>/gi, (match, attrs) => {
        if (attrs.includes('href="http') && !attrs.includes('href="https://deirdrekuvaas.com')) {
            if (!attrs.includes('rel=')) {
                return `<a ${attrs} rel="noopener noreferrer">`;
            } else {
                let relMatch = attrs.match(/rel="([^"]*)"/);
                if (relMatch) {
                    let rels = relMatch[1].split(/\s+/);
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

    // 5. Performance Optimization (CLS)
    content = content.replace(/<img\s+([^>]+)>/gi, (match, attrs) => {
        let newAttrs = attrs;
        if (newAttrs.includes('inner-world-counseling-logo.png') && !newAttrs.includes('width=')) {
            newAttrs += ' width="110" height="110"';
        }
        if (newAttrs.includes('deirdre-kuvaas.jpg') && !newAttrs.includes('width=')) {
            newAttrs += ' width="1920" height="1280"';
        }
        if (newAttrs !== attrs) {
            return `<img ${newAttrs.trim()}>`;
        }
        return match;
    });

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('Fixed:', filePath);
    }
}

walkDir(repoDir, processHtmlFile);
