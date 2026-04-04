const fs = require('fs');
const path = require('path');

// 1. Update sitemap.xml
const sitemapPath = 'sitemap.xml';
if (fs.existsSync(sitemapPath)) {
  let sitemapContent = fs.readFileSync(sitemapPath, 'utf8');
  sitemapContent = sitemapContent.replace(/<loc>([^<]+)<\/loc>/g, (match, url) => {
    if (url === 'https://deirdrekuvaas.com' || url === 'https://deirdrekuvaas.com/') {
      return '<loc>https://deirdrekuvaas.com/</loc>';
    }
    if (!url.endsWith('/')) {
      return `<loc>${url}/</loc>`;
    }
    return match;
  });
  fs.writeFileSync(sitemapPath, sitemapContent);
  console.log('Updated sitemap.xml');
}

// 2. Find all HTML files
function getHtmlFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat && stat.isDirectory()) {
      if (!filePath.includes('.git') && !filePath.includes('node_modules') && !filePath.includes('.netlify')) {
        results = results.concat(getHtmlFiles(filePath));
      }
    } else if (file.endsWith('.html')) {
      results.push(filePath);
    }
  }
  return results;
}

const htmlFiles = getHtmlFiles('.');

// 3. Update canonical tags and internal links
let updatedCount = 0;
for (const file of htmlFiles) {
  let content = fs.readFileSync(file, 'utf8');
  let originalContent = content;

  // Update canonical tags specifically
  // Regex looks for rel="canonical" href="some_url" and we replace if needed
  // Note: we just find the whole tag.
  content = content.replace(/<link\s+rel="canonical"\s+href="([^"]+)"\s*\/?>/gi, (match, url) => {
    if (url === 'https://deirdrekuvaas.com' || url === 'https://deirdrekuvaas.com/') {
      return `<link rel="canonical" href="https://deirdrekuvaas.com/">`;
    }
    if (!url.endsWith('/')) {
      return `<link rel="canonical" href="${url}/">`;
    }
    // ensure exactly match formatting
    return `<link rel="canonical" href="${url}">`;
  });
  
  // Update internal links
  content = content.replace(/href="([^"]+)"/gi, (match, href) => {
    if (href.startsWith('/') || href.startsWith('https://deirdrekuvaas.com/')) {
      if (href === '/' || href === 'https://deirdrekuvaas.com/') {
        return match;
      }
      
      // Ignore if it's pointing to a file extension
      if (/\.(css|js|png|jpg|jpeg|gif|svg|ico|xml|txt|pdf|html|webmanifest|json)$/i.test(href)) {
        return match;
      }

      // Check for # or ?
      let hashOrQueryIdx = href.search(/[#?]/);
      let pathPart = href;
      let rest = '';
      if (hashOrQueryIdx !== -1) {
        pathPart = href.slice(0, hashOrQueryIdx);
        rest = href.slice(hashOrQueryIdx);
      }

      if (pathPart.length > 0 && !pathPart.endsWith('/')) {
        if (pathPart === 'https://deirdrekuvaas.com') {
          return `href="${pathPart}/${rest}"`;
        }
        return `href="${pathPart}/${rest}"`;
      }
    }
    return match;
  });

  if (content !== originalContent) {
    fs.writeFileSync(file, content);
    updatedCount++;
  }
}

console.log(`Updated ${updatedCount} HTML files.`);
