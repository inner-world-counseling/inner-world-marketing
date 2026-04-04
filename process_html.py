import re

with open('/opt/build/repo/index.html', 'r') as f:
    content = f.read()

# Add 'for' attribute to labels
def replace_label(match):
    id_val = match.group(1)
    # the whole match is the inner content from <label to <span
    return f'<label class="checklist__label" for="{id_val}"><input type="checkbox" class="checklist__input" id="{id_val}" name="{id_val}">'

content = re.sub(r'<label class="checklist__label"><input type="checkbox" class="checklist__input" id="(vibe-check-\d+)" name="\1">', replace_label, content)

# Check for any static strike-through
content = re.sub(r'<s>(.*?)</s>', r'\1', content)
content = re.sub(r'<strike>(.*?)</strike>', r'\1', content)
content = re.sub(r'style="text-decoration:\s*line-through;?"', '', content)

# JS Block update
# First, remove existing vibe check script
content = re.sub(r'<script>\s*// Vibe Check Interactivity.*?</script>', '', content, flags=re.DOTALL)

# Add the new JS block and style block
new_script = """<style>
  .checklist__label.is-checked .checklist__text,
  .checklist__input:checked ~ .checklist__text {
    text-decoration: line-through;
    opacity: 0.6;
  }
</style>
<script>
  // Vibe Check Interactivity
  document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.checklist__input');
    checkboxes.forEach(cb => {
      // Load state
      const saved = localStorage.getItem(cb.id);
      if (saved === 'true') {
        cb.checked = true;
        cb.parentElement.classList.add('is-checked');
      }

      // Save state and toggle class on change
      cb.addEventListener('change', () => {
        localStorage.setItem(cb.id, cb.checked);
        if (cb.checked) {
          cb.parentElement.classList.add('is-checked');
        } else {
          cb.parentElement.classList.remove('is-checked');
        }
      });
    });
  });
</script>"""

content = content.replace('</body>', new_script + '\n</body>')

with open('/opt/build/repo/index.html', 'w') as f:
    f.write(content)

