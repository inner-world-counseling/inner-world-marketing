const fs = require('fs');
const path = require('path');

const directory = '.';
const modifiedFiles = [];

function processFile(filePath) {
    if (filePath.includes('node_modules') || filePath.includes('.git') || filePath.includes('.netlify') || filePath.endsWith('apply_replacements.js')) {
        return;
    }
    
    // Only process text-based files
    const ext = path.extname(filePath).toLowerCase();
    if (!['.html', '.css', '.js', '.py', '.txt', '.xml', '.json', '.toml'].includes(ext) && ext !== '') {
        return;
    }

    let originalContent;
    try {
        originalContent = fs.readFileSync(filePath, 'utf8');
    } catch (e) {
        return; // Ignore binary files or read errors
    }

    let content = originalContent;

    // First replace the longer phrase
    content = content.replace(/specializing in EMDR and CPT/g, 'utilizing evidence-based modalities such as EMDR or CPT');
    
    // Then the shorter phrase
    content = content.replace(/EMDR and CPT/g, 'EMDR or CPT');
    
    // Finally the other phrase
    content = content.replace(/EMDR Specialist/gi, (match) => {
        // preserve case matching if it's exact, else use standard replacement
        if (match === 'EMDR Specialist') return 'Trained in EMDR';
        if (match === 'EMDR specialist') return 'Trained in EMDR'; // "specialist" lowercase
        if (match === 'emdr specialist') return 'trained in emdr';
        return 'Trained in EMDR'; // Fallback
    });

    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        modifiedFiles.push(filePath);
    }
}

function walkDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            walkDir(fullPath);
        } else {
            processFile(fullPath);
        }
    }
}

walkDir(directory);

const resultPath = path.join('.netlify', 'results.md');
const resultContext = `The requested clinical terminology updates have been applied across all project files.

Here is the list of files modified:
${modifiedFiles.map(f => `- ${f}`).join('
')}

The replacements made were:
1. 'specializing in EMDR and CPT' replaced with 'utilizing evidence-based modalities such as EMDR or CPT'.
2. 'EMDR and CPT' replaced with 'EMDR or CPT'.
3. 'EMDR Specialist' replaced with 'Trained in EMDR'.
`;

fs.writeFileSync(resultPath, resultContext, 'utf8');

console.log(modifiedFiles.join('
'));
