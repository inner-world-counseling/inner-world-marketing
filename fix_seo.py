import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Logo Link
content = content.replace(
    '<a href="/" class="site-logo">\n          <img src="/images/inner-world-counseling-logo.png" alt="Inner World Counseling Services, PLLC" width="200" height="193">\n        </a>',
    '<a href="/" class="site-logo" aria-label="Home">\n          <img src="/images/inner-world-counseling-logo.png" alt="Inner World Counseling Services - Deirdre Kuvaas Home" width="200" height="193">\n        </a>'
)

# 2. Top bar phone/email
content = content.replace(
    'Make an Appointment: <a href="tel:+17014047895">(701) 404-7895</a> | <a href="mailto:deirdre@innerworldcounselingservices.com">deirdre@innerworldcounselingservices.com</a>',
    'Make an Appointment: <a href="tel:+17014047895" aria-label="Call (701) 404-7895">(701) 404-7895</a> | <a href="mailto:deirdre@innerworldcounselingservices.com" aria-label="Email Deirdre Kuvaas">deirdre@innerworldcounselingservices.com</a>'
)

# 3. Footer phone/email
content = content.replace(
    '<li><a href="tel:+17014047895">(701) 404-7895</a></li>\n            <li><a href="mailto:deirdre@innerworldcounselingservices.com">deirdre@innerworldcounselingservices.com</a></li>',
    '<li><a href="tel:+17014047895" aria-label="Call (701) 404-7895">(701) 404-7895</a></li>\n            <li><a href="mailto:deirdre@innerworldcounselingservices.com" aria-label="Email Deirdre Kuvaas">deirdre@innerworldcounselingservices.com</a></li>'
)

# 4. Social Icons aria-labels
replacements = {
    'aria-label="Email"': 'aria-label="Email Deirdre Kuvaas"',
    'aria-label="Facebook"': 'aria-label="Visit our Facebook page"',
    'aria-label="Instagram"': 'aria-label="Visit our Instagram page"',
    'aria-label="YouTube"': 'aria-label="Visit our YouTube channel"',
    'aria-label="X (Twitter)"': 'aria-label="Visit our X (Twitter) page"',
    'aria-label="Psychology Today"': 'aria-label="Visit our Psychology Today profile"'
}
for old, new in replacements.items():
    content = content.replace(old, new)

# 5. Buttons
content = content.replace(
    '<a href="/about/" class="btn btn--white">Learn More</a>',
    '<a href="/about/" class="btn btn--white" aria-label="Learn more about my therapy services">Learn More</a>'
)

content = content.replace(
    '<a href="/services/" class="btn btn--outline">See Services</a>',
    '<a href="/services/" class="btn btn--outline" aria-label="See all therapy services">See Services</a>'
)

content = content.replace(
    '<a href="/services/" class="btn btn--primary" style="margin-top: 0.5rem;">See Services</a>',
    '<a href="/services/" class="btn btn--primary" style="margin-top: 0.5rem;" aria-label="See all therapy services">See Services</a>'
)

content = content.replace(
    '<a href="/appointment-request/" class="btn btn--primary" style="margin-top: 0.5rem;">Schedule Your Free Consultation</a>',
    '<a href="/appointment-request/" class="btn btn--primary" style="margin-top: 0.5rem;" aria-label="Schedule your free therapy consultation">Schedule Your Free Consultation</a>'
)

content = content.replace(
    '<a href="/about/" class="btn btn--outline">Learn More About Deirdre</a>',
    '<a href="/about/" class="btn btn--outline" aria-label="Learn more about Deirdre Kuvaas">Learn More About Deirdre</a>'
)

content = content.replace(
    '<a href="https://deirdre-kuvaas.clientsecure.me" class="btn btn--primary" target="_blank" rel="noopener noreferrer">Request Appointment</a>',
    '<a href="https://deirdre-kuvaas.clientsecure.me" class="btn btn--primary" target="_blank" rel="noopener noreferrer" aria-label="Request a therapy appointment">Request Appointment</a>'
)

content = content.replace(
    '<a href="https://deirdre-kuvaas.clientsecure.me" class="btn btn--outline" target="_blank" rel="noopener noreferrer">Current Client Portal</a>',
    '<a href="https://deirdre-kuvaas.clientsecure.me" class="btn btn--outline" target="_blank" rel="noopener noreferrer" aria-label="Access the current client portal">Current Client Portal</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied to index.html")
