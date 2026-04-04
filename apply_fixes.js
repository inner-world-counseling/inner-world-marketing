const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        if (f.startsWith('.') || f === 'node_modules') return;
        let isDirectory = fs.statSync(dirPath).isDirectory();
        if (isDirectory) {
            walkDir(dirPath, callback);
        } else if (f.endsWith('.html')) {
            callback(dirPath);
        }
    });
}

const fontRegex1 = /<link href="https:\/\/fonts\.googleapis\.com\/css2\?family=PT\+Serif[^>]+&family=Raleway[^>]+&family=Satisfy&family=Work\+Sans[^>]+&display=swap" rel="stylesheet">/g;
const fontRegex2 = /<link href="https:\/\/fonts\.googleapis\.com\/css2\?family=PT\+Serif[^>]+&family=Raleway[^>]+&family=Satisfy&family=Work\+Sans[^"]+" rel="stylesheet">/g;

const newFontLink = '<link href="https://fonts.googleapis.com/css2?family=Satisfy&family=Work+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">';

walkDir(__dirname, (filePath) => {
    let content = fs.readFileSync(filePath, 'utf-8');
    let changed = false;

    // 1. Update Fonts
    if (fontRegex1.test(content) || fontRegex2.test(content) || content.includes('family=PT+Serif') || content.includes('family=Raleway')) {
        content = content.replace(/<link href="https:\/\/fonts\.googleapis\.com\/css2[^"]+" rel="stylesheet">/g, newFontLink);
        changed = true;
    }

    // 2. Update deirdre-kuvaas-headshot.webp dimensions
    if (content.includes('deirdre-kuvaas-headshot.webp')) {
        const oldContent = content;
        content = content.replace(/(<img[^>]+src="[^"]*deirdre-kuvaas-headshot\.webp"[^>]+)width="\d+"(.*?>)/g, '$1width="600"$2');
        content = content.replace(/(<img[^>]+src="[^"]*deirdre-kuvaas-headshot\.webp"[^>]+)height="\d+"(.*?>)/g, '$1height="400"$2');
        if (oldContent !== content) changed = true;
    }

    // 3. Update inner-world-counseling-logo.png dimensions
    if (content.includes('inner-world-counseling-logo.png')) {
        const oldContent = content;
        content = content.replace(/(<img[^>]+src="[^"]*inner-world-counseling-logo\.png"[^>]+)width="\d+"(.*?>)/g, '$1width="200"$2');
        content = content.replace(/(<img[^>]+src="[^"]*inner-world-counseling-logo\.png"[^>]+)height="\d+"(.*?>)/g, '$1height="193"$2');
        if (oldContent !== content) changed = true;
    }

    // 4. Update roots-of-healing.webp dimensions and loading
    if (content.includes('roots-of-healing.webp')) {
        const oldContent = content;
        content = content.replace(/(<img[^>]+src="[^"]*roots-of-healing\.webp"[^>]+)width="\d+"(.*?>)/g, '$1width="800"$2');
        content = content.replace(/(<img[^>]+src="[^"]*roots-of-healing\.webp"[^>]+)height="\d+"(.*?>)/g, '$1height="533"$2');
        
        // ensure loading="lazy" is present if it's an img tag
        if (content.includes('roots-of-healing.webp')) {
           // We do a manual check for lazy
           const imgMatch = content.match(/<img[^>]+src="[^"]*roots-of-healing\.webp"[^>]+>/);
           if (imgMatch && !imgMatch[0].includes('loading=')) {
               content = content.replace(/(<img[^>]+src="[^"]*roots-of-healing\.webp"[^>]+)>/, '$1 loading="lazy">');
           }
        }
        if (oldContent !== content) changed = true;
    }

    if (changed) {
        fs.writeFileSync(filePath, content, 'utf-8');
        console.log('Updated:', filePath);
    }
});
