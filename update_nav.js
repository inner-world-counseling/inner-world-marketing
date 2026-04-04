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

    // Change "The Reliable One"
    content = content.replace(/&ldquo;The Reliable One&rdquo;\s*\(Anxiety\)/g, 'Anxiety &amp; Worry');
    content = content.replace(/"The Reliable One"\s*\(Anxiety\)/g, 'Anxiety & Worry');
    content = content.replace(/1\.\s*The Reliable One\s*\(<a href="\/counseling-for-anxiety">Anxiety<\/a>\s*&amp;\s*Over-functioning\)/g, '1. Anxiety & Worry');
    content = content.replace(/&ldquo;The Reliable One:&rdquo;\s*Anxiety/g, 'Anxiety &amp; Worry');
    content = content.replace(/"The Reliable One\s*\(<a href="\/counseling-for-anxiety">Anxiety<\/a>\)"/g, '"Anxiety & Worry"');

    // Insert Cognitive Processing Therapy in nav if not present
    if (content.includes('<li><a href="/emdr">EMDR</a></li>') && !content.includes('<li><a href="/cognitive-processing-therapy">Cognitive Processing Therapy</a></li>')) {
        content = content.replace('<li><a href="/emdr">EMDR</a></li>', '<li><a href="/cognitive-processing-therapy">Cognitive Processing Therapy</a></li>\n              <li><a href="/emdr">EMDR</a></li>');
    }

    if (content !== original) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Updated nav/titles in: ' + file);
    }
});
