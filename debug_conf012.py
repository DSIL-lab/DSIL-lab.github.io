from pathlib import Path
path = Path(r'C:\LabHomepage_Edit\DSIL-lab.github.io\_publications\conf-012.md')
text = path.read_text(encoding='utf-8')
print(text)
print('contains', '</strong>*' in text)
print([line for line in text.splitlines() if 'authors:' in line])
print(repr(text[text.index('authors:'):text.index('authors:')+200]))
