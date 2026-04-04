const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        if (file.startsWith('.git') || file.startsWith('node_modules')) return;
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        if (stat && stat.isDirectory()) {
            results = results.concat(walk(filePath));
        } else {
            if (filePath.endsWith('.html')) results.push(filePath);
        }
    });
    return results;
}

const files = walk('/opt/build/repo');
files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let original = content;

    content = content.replace(/<li><a href="\/">Inner World Counseling Home<\/a><\/li>/g, '<li><a href="/">Home</a></li>');

    if (content !== original) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Updated footer in: ' + file);
    }
});
