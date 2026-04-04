const fs = require('fs');
const path = require('path');

const baseDomain = 'https://deirdrekuvaas.com';
const repoDir = '/opt/build/repo';

function getAllHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      if (!['.git', 'node_modules', '.netlify'].includes(file)) {
        getAllHtmlFiles(filePath, fileList);
      }
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const htmlFiles = getAllHtmlFiles(repoDir);
const canonicalUrls = new Set();

htmlFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');

  // Determine canonical URL
  let relativePath = path.relative(repoDir, file);
  let urlPath = '/' + relativePath.split(path.sep).join('/');
  
  if (urlPath === '/index.html') {
    urlPath = '/';
  } else if (urlPath.endsWith('/index.html')) {
    urlPath = urlPath.slice(0, -10); // keep trailing slash
  } else if (urlPath.endsWith('.html')) {
    urlPath = urlPath.slice(0, -5) + '/'; // e.g. /privacy.html -> /privacy/
  }
  
  const canonicalUrl = baseDomain + urlPath;
  canonicalUrls.add(canonicalUrl);

  // 3. Normalize internal links FIRST
  content = content.replace(/href=["']([^"']+)["']/g, (match, url) => {
    if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('mailto:') || url.startsWith('tel:') || url.startsWith('#')) {
      if (url.startsWith(baseDomain)) {
        let internalPath = url.substring(baseDomain.length);
        if (!internalPath.startsWith('/')) internalPath = '/' + internalPath;
        url = internalPath;
      } else {
        return match;
      }
    }
    
    if (url.startsWith('//') && url.includes('.')) {
      const domainPart = url.substring(2).split('/')[0];
      if (domainPart.includes('.')) {
        return match;
      }
    }

    let urlObj;
    try {
      urlObj = new URL(url, 'http://localhost');
    } catch (e) {
      return match;
    }

    let pathname = urlObj.pathname;
    
    pathname = pathname.replace(/\/{2,}/g, '/');
    if (pathname.endsWith('/index.html') && pathname !== '/index.html') {
        pathname = pathname.slice(0, -10);
    } else if (pathname === '/index.html') {
        pathname = '/';
    } else if (pathname.endsWith('.html')) {
        pathname = pathname.slice(0, -5) + '/';
    }
    
    if (!pathname.includes('.') && !pathname.endsWith('/')) {
        pathname += '/';
    }

    let newUrl = pathname + urlObj.search + urlObj.hash;
    return `href="${newUrl}"`;
  });

  // 1. Standardize Canonical
  const canonicalRegex = /<link\s+rel=["']canonical["']\s+href=["']([^"']*)["']\s*\/?>/i;
  if (canonicalRegex.test(content)) {
    content = content.replace(canonicalRegex, `<link rel="canonical" href="${canonicalUrl}">`);
  } else {
    content = content.replace('</head>', `  <link rel="canonical" href="${canonicalUrl}">\n</head>`);
  }

  // 2. Standardize og:url
  const ogUrlRegex = /<meta\s+property=["']og:url["']\s+content=["']([^"']*)["']\s*\/?>/i;
  if (ogUrlRegex.test(content)) {
    content = content.replace(ogUrlRegex, `<meta property="og:url" content="${canonicalUrl}">`);
  } else {
    content = content.replace('</head>', `  <meta property="og:url" content="${canonicalUrl}">\n</head>`);
  }

  fs.writeFileSync(file, content, 'utf8');
});

console.log('Processed HTML files.');

// Now fix sitemap.xml
const sitemapPath = path.join(repoDir, 'sitemap.xml');
if (fs.existsSync(sitemapPath)) {
  let sitemapContent = fs.readFileSync(sitemapPath, 'utf8');
  sitemapContent = sitemapContent.replace(/<loc>([^<]+)<\/loc>/g, (match, url) => {
    let urlObj;
    try {
      urlObj = new URL(url);
    } catch (e) {
      return match;
    }

    let pathname = urlObj.pathname;
    pathname = pathname.replace(/\/{2,}/g, '/');
    if (pathname.endsWith('/index.html') && pathname !== '/index.html') {
        pathname = pathname.slice(0, -10);
    } else if (pathname === '/index.html') {
        pathname = '/';
    } else if (pathname.endsWith('.html')) {
        pathname = pathname.slice(0, -5) + '/';
    }
    if (!pathname.includes('.') && !pathname.endsWith('/')) {
        pathname += '/';
    }
    const newUrl = baseDomain + pathname;
    
    if (!canonicalUrls.has(newUrl)) {
      console.log(`Warning: Sitemap URL \${newUrl} is not found in generated canonical URLs.`);
    }

    return `<loc>\${newUrl}</loc>`;
  });
  fs.writeFileSync(sitemapPath, sitemapContent, 'utf8');
  console.log('Processed sitemap.xml');
}

// Now process netlify.toml to remove the redirect loop
const netlifyTomlPath = path.join(repoDir, 'netlify.toml');
if (fs.existsSync(netlifyTomlPath)) {
  let tomlContent = fs.readFileSync(netlifyTomlPath, 'utf8');
  // the problematic block is:
  // [[redirects]]
  //   from = "/*"
  //   to = "/:splat/"
  //   status = 301
  //   force = false
  const loopRegex = /\[\[redirects\]\]\s*from\s*=\s*"\/\*"\s*to\s*=\s*"\/:splat\/"\s*status\s*=\s*301\s*force\s*=\s*false/s;
  if (loopRegex.test(tomlContent)) {
    tomlContent = tomlContent.replace(loopRegex, '');
    fs.writeFileSync(netlifyTomlPath, tomlContent.trim() + '\\n', 'utf8');
    console.log('Removed redirect loop from netlify.toml');
  } else {
    console.log('No redirect loop found in netlify.toml');
  }
}
