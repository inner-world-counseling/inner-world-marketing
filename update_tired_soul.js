const fs = require('fs');
const path = require('path');

function replaceInDir(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      if (fullPath.includes('.git') || fullPath.includes('node_modules')) continue;
      replaceInDir(fullPath);
    } else if (fullPath.endsWith('.html')) {
      let content = fs.readFileSync(fullPath, 'utf8');
      let newContent = content
        .replace(/&ldquo;The Tired Soul&rdquo; \(Substance Use\)/g, 'Substance Use')
        .replace(/"The Tired Soul" \(Substance Use\)/g, 'Substance Use')
        .replace(/"The Tired Soul \(Substance Use\)"/g, 'Substance Use')
        .replace(/The Tired Soul \(Addiction &amp; Numbing\)/g, 'Substance Use (Addiction &amp; Numbing)');
      
      if (content !== newContent) {
        fs.writeFileSync(fullPath, newContent, 'utf8');
        console.log(`Updated ${fullPath}`);
      }
    }
  }
}

replaceInDir('/opt/build/repo');
