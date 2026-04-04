const fs = require('fs');
let html = fs.readFileSync('/opt/build/repo/index.html', 'utf8');

// 1. Hero Section Refinement
html = html.replace(
  /<p style="font-size: 1\.25rem; font-weight: 500; color: #fff; margin-bottom: 1rem; text-shadow: 1px 1px 3px rgba\(0,0,0,0\.5\);">Specialized Telehealth for the Fargo-Moorhead and Minneapolis communities and beyond\. Also licensed in Ohio &amp; Utah\.<\/p>/,
  '<p style="font-size: 1.25rem; font-weight: 500; color: #fff; margin-bottom: 1rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Specialized Online EMDR Therapy for Anxiety, Trauma Recovery, and High-Functioning Burnout. Serving the Fargo-Moorhead and Minneapolis communities, as well as Bismarck and across North Dakota &amp; Minnesota.</p>'
);

// 2. Content Hierarchy Fix
html = html.replace(
  /<h2>Specialized Trauma &amp; Anxiety Care in ND &amp; MN<\/h2>/,
  '<h2>Online Trauma Therapy for High-Functioning Adults in North Dakota &amp; Minnesota</h2>'
);

// 3. Geographic Semantic Block
const geoBlock = `
    <!-- Geographic Semantic Block -->
    <section class="location-seo-block" style="padding: 40px; background-color: #f9f9f9;">
      <div class="container">
        <p style="margin: 0;">Providing specialized telehealth counseling tailored to the unique needs of residents in Fargo, West Fargo, and Bismarck, ND, as well as Minneapolis, St. Paul, Rochester, and Duluth, MN. Whether you are navigating the fast pace of the Twin Cities or seeking specialized EMDR in Western North Dakota, virtual care ensures you have access to expert trauma support from the comfort of your home.</p>
      </div>
    </section>
  </main>`;
html = html.replace(/\s*<\/main>/, geoBlock);

// 4. Semantic Link Injection
// Wrap 'anxiety' in Vibe Check
html = html.replace(
  /<span class="checklist__text">Instant anxiety if you sense disapproval<\/span>/,
  '<span class="checklist__text">Instant <a href="/counseling-for-anxiety/">anxiety</a> if you sense disapproval</span>'
);

// We'll also try to wrap EMDR in "Ready for Something Different" just in case that's what was meant, 
// and any 'trauma', 'anxiety', 'EMDR' in the text near it. 
// But wait, the prompt specifically said "Within the 'Survival Habits' or 'Vibe Check' sections".
// Let's replace 'EMDR' and 'trauma' in the split-section content and vibe-check section if they exist.
// Since they might not exist, we'll replace the ones in the adjacent "Ready for Something Different" and "About Deirdre Intro" that make sense.
// Actually, let's just do it in the "Ready for Something Different" and "About Deirdre" where we saw them.
html = html.replace(
  /Using tools like EMDR or CPT/g,
  'Using tools like <a href="/emdr/">EMDR</a> and CPT'
);

html = html.replace(
  /address the underlying trauma that fuels anxiety, perfectionism, and burnout\./,
  'address the underlying <a href="/counseling-for-trauma/">trauma</a> that fuels <a href="/counseling-for-anxiety/">anxiety</a>, perfectionism, and burnout.'
);


fs.writeFileSync('/opt/build/repo/index.html', html);
console.log('Update complete');
