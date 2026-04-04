const fs = require('fs');
const path = require('path');

const filePath = path.join('/opt/build/repo', 'index.html');
let html = fs.readFileSync(filePath, 'utf8');

// 1. Meta Description
const oldMetaDesc = '<meta name="description" content="Specialized online trauma and anxiety therapy for adults in the Fargo-Moorhead area, North Dakota, and Minnesota. Also licensed to serve OH and UT. Evidence-based care with EMDR &amp; CPT.">';
const newMetaDesc = '<meta name="description" content="Evidence-based telehealth therapy for high-functioning anxiety, PTSD, and people-pleasing. EMDR & CPT with Deirdre Kuvaas, LPCC. Free consultation for ND, MN, OH & UT residents.">';

if (html.includes(oldMetaDesc)) {
  html = html.replace(oldMetaDesc, newMetaDesc);
  console.log('Updated meta description.');
} else {
  console.log('Failed to find old meta description.');
}

// 2. Image Alt Text
const oldImg = '<img src="/images/deirdre-kuvaas.jpg" alt="Deirdre Kuvaas, LPCC – Licensed Professional Clinical Counselor specializing in trauma and anxiety therapy" title="Deirdre Kuvaas, LPCC" loading="lazy" style="border-radius: 6px;" width="1920" height="1280">';
const newImg = '<img src="/images/deirdre-kuvaas.jpg" alt="Deirdre Kuvaas, LPCC - Trauma and Anxiety Therapist providing EMDR or CPT telehealth in ND, MN, OH, and UT." title="Deirdre Kuvaas, LPCC" loading="lazy" style="border-radius: 6px;" width="1920" height="1280">';

if (html.includes(oldImg)) {
  html = html.replace(oldImg, newImg);
  console.log('Updated image alt text.');
} else {
  console.log('Failed to find old image alt text.');
}

// 3. Header Hierarchy Correction
const ulSection = `        <ul style="text-align: left; margin: 1.5rem auto; max-width: 600px; font-size: 1.125rem; line-height: 1.6; list-style: none; padding-left: 0;">
          <li style="margin-bottom: 0.5rem;"><h2 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">High-functioning anxiety &amp; chronic overthinking</h2></li>
          <li style="margin-bottom: 0.5rem;"><h2 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">PTSD &amp; Complex Trauma (C-PTSD) recovery</h2></li>
          <li style="margin-bottom: 0.5rem;"><h2 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">Nervous system regulation &amp; burnout prevention</h2></li>
          <li style="margin-bottom: 0.5rem;"><h2 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">Attachment wounds &amp; people-pleasing behaviors</h2></li>
        </ul>`;

const newUlSection = `        <ul style="text-align: left; margin: 1.5rem auto; max-width: 600px; font-size: 1.125rem; line-height: 1.6; list-style: none; padding-left: 0;">
          <li style="margin-bottom: 0.5rem;"><h3 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">High-functioning anxiety &amp; chronic overthinking</h3></li>
          <li style="margin-bottom: 0.5rem;"><h3 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">PTSD &amp; Complex Trauma (C-PTSD) recovery</h3></li>
          <li style="margin-bottom: 0.5rem;"><h3 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">Nervous system regulation &amp; burnout prevention</h3></li>
          <li style="margin-bottom: 0.5rem;"><h3 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">Attachment wounds &amp; people-pleasing behaviors</h3></li>
        </ul>`;

if (html.includes(ulSection)) {
  html = html.replace(ulSection, newUlSection);
  console.log('Updated headers from h2 to h3.');
} else {
  console.log('Failed to find header section. Let me try matching loosely.');
  html = html.replace(/<h2 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">/g, '<h3 style="font-size: 1.125rem; font-weight: 400; margin: 0; display: list-item; list-style-type: disc; margin-left: 1.5rem;">');
  html = html.replace(/<\/h2><\/li>/g, '</h3></li>');
  console.log('Did a global replace for the h2 -> h3 nested lists.');
}

// 4. Schema Consolidation & Local SEO
const scriptRegex = /<script type="application\/ld\+json">([\s\S]*?)<\/script>/g;
let match;
let scripts = [];
while ((match = scriptRegex.exec(html)) !== null) {
  try {
    const data = JSON.parse(match[1]);
    scripts.push({
      fullMatch: match[0],
      data: data
    });
  } catch (e) {
    console.error('Failed to parse JSON-LD block');
  }
}

// Find the block that has MedicalBusiness + Person
let targetScriptIndex = -1;
for (let i = 0; i < scripts.length; i++) {
  if (scripts[i].data['@graph']) {
    const hasMedical = scripts[i].data['@graph'].some(item => item['@type'] === 'MedicalBusiness');
    if (hasMedical) {
      targetScriptIndex = i;
      break;
    }
  }
}

if (targetScriptIndex !== -1) {
  const targetScript = scripts[targetScriptIndex];
  const graph = targetScript.data['@graph'];
  
  // Update MedicalBusiness
  const medicalBusiness = graph.find(item => item['@type'] === 'MedicalBusiness');
  if (medicalBusiness && medicalBusiness.areaServed) {
    // Add missing cities: "Bismarck", "Fargo", "Moorhead", "Minneapolis", and "Duluth"
    const requiredCities = ["Bismarck", "Fargo", "Moorhead", "Minneapolis", "Duluth"];
    const existingCities = medicalBusiness.areaServed.filter(item => item['@type'] === 'City').map(item => item.name);
    
    for (const city of requiredCities) {
      if (!existingCities.includes(city)) {
        medicalBusiness.areaServed.push({ "@type": "City", "name": city });
      }
    }
    console.log('Updated areaServed with required cities.');
  }

  const newScriptContent = `<script type="application/ld+json">\n  ${JSON.stringify(targetScript.data, null, 2)}\n  </script>`;
  html = html.replace(targetScript.fullMatch, newScriptContent);
}

fs.writeFileSync(filePath, html, 'utf8');
console.log('File successfully updated.');
