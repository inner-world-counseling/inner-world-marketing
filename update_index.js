const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf-8');

// 1. SEO & META UPDATES
const newDesc = "Telehealth therapy for anxiety, trauma, and addiction. Stop surviving and start healing with evidence-based tools like EMDR or CPT. Serving adults in ND, MN, OH, and UT. Book a free 15-min consultation with Deirdre Kuvaas, LPCC.";

// Meta description
content = content.replace(
  /<meta name="description" content="[^"]+">/,
  `<meta name="description" content="${newDesc}">`
);
// Schema.org descriptions
content = content.replace(
  /"description": "Telehealth therapy for anxiety, trauma, and addiction — North Dakota, Minnesota, Ohio, Utah"/,
  `"description": "${newDesc}"`
);
content = content.replace(
  /"description": "Telehealth therapy for anxiety, trauma, PTSD, and substance use disorder. Serving adults in North Dakota, Minnesota, Ohio, and Utah via secure video sessions."/,
  `"description": "${newDesc}"`
);
content = content.replace(
  /"description": "Deirdre Kuvaas is a licensed telehealth therapist specializing in trauma \(EMDR, CPT\), anxiety, and substance use disorder for adults in North Dakota, Minnesota, Ohio, and Utah."/,
  `"description": "${newDesc}"`
);

// 2. INTRO SECTION
content = content.replace(
  /(Let us move past the surface and get to the roots of your well-being\.<\/p>)\s*(<a href="\/services" class="btn btn--outline">See Services<\/a>)/,
  `$1\n            <p style="margin-bottom: 1.5rem;"><strong>Get back to the real you. Evidence-Based Virtual Therapy with Deirdre Kuvaas, LPCC.</strong></p>\n            $2`
);

// 3. VIBE CHECK LIST (remove periods at the end of each <li> string)
// Looking at the list, there are no periods, but just in case, let's regex replace ".\s*</span>" with "</span>" inside checklist
content = content.replace(/(<span class="checklist__text">[^<]+?)\.\s*(<\/span>)/g, '$1$2');

// 4. ABOUT SECTION
content = content.replace(
  /<h3>Hi there!<\/h3>/,
  `<h3>Hi there! I am Deirdre! (Deer-dra)</h3>`
);

// About section bullet points update
const oldBullets = `<li><strong>Rooted in Science:</strong> I use evidence based tools like EMDR or CPT to address the underlying trauma that fuels anxiety, perfectionism, and burnout.</li>
              <li><strong>Beyond Symptom Management:</strong> We will move past the surface to heal the origins of your struggle, ensuring that the relief you find is sustainable.</li>
              <li><strong>A Real Connection:</strong> Therapy is a collaborative, human process. You will find a straightforward and compassionate space where you are finally free to be your authentic self.</li>
              <li><strong>Specialized Expertise:</strong> I focus on the unique needs of high functioning "fixers," "empaths," and "peacekeepers" who are ready to reclaim their lives.</li>`;

const newBullets = `<li><strong>Rooted in Science:</strong> I use evidence-based tools like EMDR or CPT to address the underlying trauma that fuels anxiety, perfectionism, and burnout.</li>
              <li><strong>Beyond Symptom Management:</strong> We will move past the surface to heal the origins of your struggle, ensuring that the relief you find is sustainable.</li>
              <li><strong>A Real Connection:</strong> Therapy is a collaborative, human process. You will find a straightforward and compassionate space where you are finally free to be your authentic self.</li>
              <li><strong>Specialized Expertise:</strong> I focus on the unique needs of high-functioning "fixers," "empaths," and "peacekeepers" who are ready to reclaim their lives.</li>`;

content = content.replace(oldBullets, newBullets);

// 5. TYPOGRAPHY (Survival Habits section)
// Survival Habits Aren't Personality Traits -> Aren’t
content = content.replace(/<h2>Survival Habits Aren't Personality Traits<\/h2>/, `<h2>Survival Habits Aren’t Personality Traits</h2>`);
// aren't just "who you are." -> aren’t
content = content.replace(/— aren't just "who you are."/, `— aren’t just "who you are."`);
// telling you that you haven't done enough. -> haven’t
content = content.replace(/telling you that you haven't done enough\./, `telling you that you haven’t done enough.`);
// It's the voice -> It’s
content = content.replace(/It's the voice that keeps you on edge/, `It’s the voice that keeps you on edge`);

fs.writeFileSync('index.html', content, 'utf-8');
console.log('Update complete.');
