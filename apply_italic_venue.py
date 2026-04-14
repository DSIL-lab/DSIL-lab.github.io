import re
from pathlib import Path

root = Path(r'C:\LabHomepage_Edit\DSIL-lab.github.io\_publications')
pattern = re.compile(r'^(venue:\s*")(.*?)(")$', re.MULTILINE)
modified_files = []
for path in sorted(root.glob('*.md')):
    text = path.read_text(encoding='utf-8')
    def repl(match):
        prefix, venue, suffix = match.groups()
        if venue.strip() == '':
            return match.group(0)
        if venue.startswith('<em>') and venue.endswith('</em>'):
            return match.group(0)
        return f'{prefix}<em>{venue}</em>{suffix}'
    new_text = pattern.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        modified_files.append(path.name)

print('Modified files:', len(modified_files))
for name in modified_files:
    print(name)
