const fs = require('fs');
const path = require('path');

const indexHtml = fs.readFileSync('/opt/build/repo/index.html', 'utf8');

const headMatch = indexHtml.match(/(<!DOCTYPE html>[\s\S]*?<\/header>)/);
const footerMatch = indexHtml.match(/(<footer class="site-footer">[\s\S]*?<\/html>)/);

if (!headMatch || !footerMatch) {
  console.error('Could not find header or footer');
  process.exit(1);
}

let topPart = headMatch[1];
let bottomPart = footerMatch[1];

let privacyTop = topPart.replace(/<title>.*?<\/title>/, '<title>Privacy Policy | Inner World Counseling</title>');
privacyTop = privacyTop.replace(/<meta name="description" content=".*?">/, '<meta name="description" content="Privacy Policy for Inner World Counseling Services.">');

const privacyContent = `
  <main>
    <section class="section">
      <div class="container" style="max-width: 800px; margin: 0 auto; padding: 4rem 0;">
        <h1 style="margin-bottom: 1.5rem;">Privacy Policy</h1>
        <p style="margin-bottom: 1rem;"><strong>Effective Date:</strong> March 22, 2026</p>
        <h2 style="margin-top: 2rem; margin-bottom: 1rem;">1. Information We Collect</h2>
        <p style="margin-bottom: 1rem;">We collect information you provide directly to us when you request an appointment, contact us, or otherwise communicate with us. This may include your name, email address, phone number, and any other information you choose to provide.</p>
        <h2 style="margin-top: 2rem; margin-bottom: 1rem;">2. Clinical Records and SimplePractice</h2>
        <p style="margin-bottom: 1rem;"><strong>Please note:</strong> All clinical records, including intake forms, session notes, and sensitive personal health information (PHI), are managed exclusively through a secure, HIPAA-compliant portal called SimplePractice. <strong>No clinical records or sensitive health information are stored on this website.</strong></p>
        <h2 style="margin-top: 2rem; margin-bottom: 1rem;">3. How We Use Your Information</h2>
        <p style="margin-bottom: 1rem;">We use the information we collect to communicate with you, process your requests, and provide you with information about our services. Your information is never sold to third parties.</p>
        <h2 style="margin-top: 2rem; margin-bottom: 1rem;">4. Contact Us</h2>
        <p style="margin-bottom: 1rem;">If you have any questions about this Privacy Policy, please contact us at <a href="mailto:deirdre@innerworldcounselingservices.com">deirdre@innerworldcounselingservices.com</a>.</p>
      </div>
    </section>
  </main>
`;

let termsTop = topPart.replace(/<title>.*?<\/title>/, '<title>Terms of Service | Inner World Counseling</title>');
termsTop = termsTop.replace(/<meta name="description" content=".*?">/, '<meta name="description" content="Terms of Service and Medical Disclaimer for Inner World Counseling Services.">');

const termsContent = `
  <main>
    <section class="section">
      <div class="container" style="max-width: 800px; margin: 0 auto; padding: 4rem 0;">
        <h1 style="margin-bottom: 1.5rem;">Terms of Service</h1>
        <p style="margin-bottom: 1rem;"><strong>Effective Date:</strong> March 22, 2026</p>
        <h2 style="margin-top: 2rem; margin-bottom: 1rem;">1. Acceptance of Terms</h2>
        <p style="margin-bottom: 1rem;">By accessing and using this website, you accept and agree to be bound by the terms and provision of this agreement.</p>
        <h2 style="margin-top: 2rem; margin-bottom: 1rem;">2. Medical Disclaimer</h2>
        <p style="margin-bottom: 1rem;"><strong>The content provided on this website is for educational and informational purposes only.</strong> It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Accessing or using this website does not constitute a therapeutic relationship or establish a therapist-client relationship between you and Inner World Counseling Services or Deirdre Kuvaas, LPCC. Always seek the advice of your physician or other qualified mental health provider with any questions you may have regarding a medical or mental health condition.</p>
        <h2 style="margin-top: 2rem; margin-bottom: 1rem;">3. Use of the Site</h2>
        <p style="margin-bottom: 1rem;">You agree to use the site only for lawful purposes and in a way that does not infringe the rights of, restrict or inhibit anyone else's use and enjoyment of the site.</p>
      </div>
    </section>
  </main>
`;

let updatedBottomPart = bottomPart
  .replace(/<a href="\/privacy\/">Privacy<\/a>/g, '<a href="/privacy.html">Privacy</a>')
  .replace(/<a href="\/terms\/">Terms<\/a>/g, '<a href="/terms.html">Terms</a>');

fs.writeFileSync('/opt/build/repo/privacy.html', privacyTop + privacyContent + updatedBottomPart);
fs.writeFileSync('/opt/build/repo/terms.html', termsTop + termsContent + updatedBottomPart);

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

    content = content.replace(/<a href="\/privacy\/">Privacy<\/a>/g, '<a href="/privacy.html">Privacy</a>');
    content = content.replace(/<a href="\/terms\/">Terms<\/a>/g, '<a href="/terms.html">Terms</a>');

    if (content !== original) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Updated links in: ' + file);
    }
});
console.log('Done.');
