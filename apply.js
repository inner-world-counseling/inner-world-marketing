const fs = require('fs');
const path = require('path');

// 1. Process index.html specifically
let indexPath = path.join('/opt/build/repo', 'index.html');
let indexContent = fs.readFileSync(indexPath, 'utf8');

// Replace H1 -> H2 with styling
indexContent = indexContent.replace(
  /<h1>Stop Surviving\. Start Healing\.<\/h1>/,
  '<h2 style="font-size: 2.5rem;">Stop Surviving. Start Healing.</h2>'
);

// Add new H1 in hero
const heroH1 = `
      <h1 style="font-size: 1.125rem; font-weight: 500; letter-spacing: 0.05em; margin-bottom: 0.5rem; color: #fff; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Online Trauma &amp; Anxiety Therapy | Licensed in ND, MN, OH, &amp; UT</h1>`;
if (!indexContent.includes('Online Trauma &amp; Anxiety Therapy')) {
    indexContent = indexContent.replace(
      /(<div class="hero__content">)/,
      `$1${heroH1}`
    );
}

// Add "Who I Help" section
const whoIHelpSection = `
    <!-- Specialized Telehealth Support For -->
    <section class="section section--sage">
      <div class="container" style="text-align:center; max-width:800px;">
        <h2>Specialized Telehealth Support For:</h2>
        <ul style="text-align: left; margin: 1.5rem auto; max-width: 600px; font-size: 1.125rem; line-height: 1.6;">
          <li>High-functioning anxiety &amp; chronic overthinking</li>
          <li>PTSD &amp; Complex Trauma (C-PTSD) recovery</li>
          <li>Nervous system regulation &amp; burnout prevention</li>
          <li>Attachment wounds &amp; people-pleasing behaviors</li>
        </ul>
      </div>
    </section>
`;
if (!indexContent.includes('Specialized Telehealth Support For:')) {
    indexContent = indexContent.replace(
      /(<!-- ========== MAIN CONTENT ========== -->\s*<main>)/,
      `$1${whoIHelpSection}`
    );
}

// FAQ section at the bottom of index.html
const faqSection = `
    <!-- FAQ Section -->
    <section class="section">
      <div class="container">
        <h2>Frequently Asked Questions</h2>
        <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
          <h3 itemprop="name" style="font-size: 1.25rem;">Do you offer virtual therapy in my state?</h3>
          <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text">I am licensed for telehealth in ND, MN, OH, and UT.</p>
          </div>
        </div>
        <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <h3 itemprop="name" style="font-size: 1.25rem;">What is the focus of your practice?</h3>
          <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text">I specialize in evidence-based trauma recovery and anxiety treatment for high-functioning adults.</p>
          </div>
        </div>
      </div>
    </section>
`;

const faqSchema = `
  <!-- FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "Do you offer virtual therapy in my state?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "I am licensed for telehealth in ND, MN, OH, and UT."
      }
    }, {
      "@type": "Question",
      "name": "What is the focus of your practice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "I specialize in evidence-based trauma recovery and anxiety treatment for high-functioning adults."
      }
    }]
  }
  </script>
`;

if (!indexContent.includes('Do you offer virtual therapy in my state?')) {
    indexContent = indexContent.replace(
      /(<\/main>)/,
      `${faqSection}
  $1`
    );
    indexContent = indexContent.replace(
      /(<\/body>)/,
      `${faqSchema}
$1`
    );
}

fs.writeFileSync(indexPath, indexContent, 'utf8');

// Global changes
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

const geoText = "Licensed to provide professional clinical counseling via telehealth to residents of North Dakota, Minnesota, Ohio, and Utah.";
const footerRegex = /(<div[^>]*>\s*<div\s+id="pt-verified-seal"><\/div>\s*<span>Copyright[^<]+<\/span>\s*<\/div>)/;

walkDir('/opt/build/repo', (filePath) => {
    let content = fs.readFileSync(filePath, 'utf8');
    let originalContent = content;

    // Geographic Anchor in Footer
    if (footerRegex.test(content) && !content.includes(geoText)) {
        content = content.replace(footerRegex, `<div style="display:flex; flex-direction:column; gap:0.5rem;">
          $1
          <p style="font-size: 0.8125rem; color: inherit; margin: 0;">${geoText}</p>
        </div>`);
    }

    // Semantic Definitions
    const hasEMDR = /\bEMDR\b/i.test(content);
    const hasCPT = /\bCPT\b/i.test(content);
    
    const emdrDef = `An evidence-based psychotherapy that enables people to heal from the symptoms and emotional distress that are the result of disturbing life experiences.`;
    const cptDef = `A specific type of cognitive behavioral therapy that helps patients learn how to modify and challenge unhelpful beliefs related to trauma.`;

    if ((hasEMDR || hasCPT) && content.includes('</main>')) {
        let defsHTML = `
    <section class="semantic-definitions" aria-label="Therapy Definitions" style="padding: 2rem 0; background-color: #fafafa; border-top: 1px solid #eaeaea; font-size: 0.875rem; color: #555;">
      <div class="container">
        <dl style="margin: 0; display: flex; flex-direction: column; gap: 1rem;">
`;
        let added = false;
        
        if (hasEMDR && !content.includes('An evidence-based psychotherapy that enables people to heal')) {
            defsHTML += `          <div style="margin: 0;"><dt style="font-weight: 600; display: inline;">EMDR:</dt> <dd style="display: inline; margin-left: 0.25rem;">\${emdrDef}</dd></div>
`;
            added = true;
        }
        if (hasCPT && !content.includes('A specific type of cognitive behavioral therapy that helps')) {
            defsHTML += `          <div style="margin: 0;"><dt style="font-weight: 600; display: inline;">CPT:</dt> <dd style="display: inline; margin-left: 0.25rem;">\${cptDef}</dd></div>
`;
            added = true;
        }
        defsHTML += `        </dl>
      </div>
    </section>
  `;
        
        if (added) {
            content = content.replace('</main>', defsHTML + '</main>');
        }
    }

    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log("Updated: " + filePath);
    }
});
