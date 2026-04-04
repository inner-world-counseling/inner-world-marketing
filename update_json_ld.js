const fs = require('fs');

const filePath = '/opt/build/repo/people-pleasing/index.html';
let content = fs.readFileSync(filePath, 'utf-8');

const scriptRegex = /<script type="application\/ld\+json">([\s\S]*?)<\/script>/g;

content = content.replace(scriptRegex, (match, jsonString) => {
  try {
    const data = JSON.parse(jsonString);
    if (data['@graph']) {
      // Add Service Schema
      data['@graph'].push({
        "@type": "Service",
        "serviceType": "Counseling for People Pleasing & Boundaries",
        "audience": {
          "@type": "Audience",
          "audienceType": "High-achievers, over-functioners, professionals."
        },
        "provider": {
          "@id": "https://deirdrekuvaas.com/#person"
        },
        "url": "https://deirdrekuvaas.com/people-pleasing/"
      });

      // Add FAQ Schema
      data['@graph'].push({
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why do I feel so guilty saying no?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Guilt when saying no often stems from childhood conditioning where your safety or worth was tied to accommodating others. Your nervous system interprets setting a boundary as a threat to your relationships, triggering a disproportionate guilt response."
            }
          },
          {
            "@type": "Question",
            "name": "Is people-pleasing actually a trauma response?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, in many cases, chronic people-pleasing is a trauma response known as \"fawning.\" It is an unconscious survival strategy designed to pacify threats and avoid conflict by abandoning one's own needs to appease others."
            }
          },
          {
            "@type": "Question",
            "name": "How can EMDR help me set better boundaries?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "EMDR helps you set better boundaries by targeting and reprocessing the root memories and negative core beliefs that make boundary-setting feel dangerous. By resolving this underlying trauma, EMDR reduces the intense emotional activation and guilt, allowing you to establish and maintain healthy boundaries with confidence."
            }
          }
        ]
      });
      return `<script type="application/ld+json">\n${JSON.stringify(data, null, 2)}\n</script>`;
    }
  } catch (e) {
    console.error("Error parsing JSON:", e);
  }
  return match;
});

fs.writeFileSync(filePath, content, 'utf-8');
console.log("JSON-LD updated.");
