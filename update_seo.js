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

    // 1. Refine Schema areaServed in MedicalBusiness
    // Regex matches the areaServed array that contains objects with "@type": "State"
    const schemaRegex = /"areaServed": \[\s*\{\s*"@type":\s*"State"[^\]]+\]/g;
    const newAreaServed = `"areaServed": [
          { "@type": "State", "name": "North Dakota" },
          { "@type": "State", "name": "Minnesota" },
          { "@type": "State", "name": "Ohio" },
          { "@type": "State", "name": "Utah" },
          { "@type": "City", "name": "Fargo", "sameAs": "https://www.wikidata.org/wiki/Q34140" },
          { "@type": "City", "name": "Moorhead", "sameAs": "https://www.wikidata.org/wiki/Q1922445" },
          { "@type": "City", "name": "Minneapolis", "sameAs": "https://www.wikidata.org/wiki/Q36091" }
        ]`;
    content = content.replace(schemaRegex, newAreaServed);

    // 2. Footer Update
    if (!content.includes('Physical Location: Horace, ND')) {
        content = content.replace(
            /<span>Copyright &copy; 2026 Inner World Counseling Services, PLLC<\/span>/g,
            `<span>Copyright &copy; 2026 Inner World Counseling Services, PLLC</span>
          <span style="font-size: 0.8125rem; opacity: 0.8; margin-left: auto;">Physical Location: Horace, ND</span>`
        );
    }

    if (filePath === 'index.html' || filePath === 'index.html') {
        // 3. Update Hero & Intro
        content = content.replace(
            /Specialized Telehealth for the Fargo-Moorhead Community and beyond\. Also licensed in Ohio &amp; Utah\./g,
            `Specialized Telehealth for the Fargo-Moorhead and Minneapolis communities and beyond. Also licensed in Ohio &amp; Utah.`
        );

        content = content.replace(
            /Rooted in the Fargo-Moorhead community and serving all of North Dakota and Minnesota/g,
            `Rooted in the Fargo-Moorhead and Minneapolis communities and serving all of North Dakota and Minnesota`
        );

        // 4. Image Alt-Text
        content = content.replace(
            /alt="Virtual trauma therapy session with Trained in EMDR"/g,
            `alt="Virtual trauma therapy for high-achieving professionals in Fargo, ND and Minneapolis, MN."`
        );
    }

    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated ${filePath}`);
    }
});
console.log("Global HTML updates completed.");
