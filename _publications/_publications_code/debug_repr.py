import pathlib
root = pathlib.Path(r'C:\LabHomepage_Edit\DSIL-lab.github.io\_publications')
for path in sorted(root.glob('*.md')):
    text = path.read_text(encoding='utf-8')
    if '</strong>*' in text:
        print(path.name)
        idx = text.index('</strong>*')
        print(repr(text[idx-30:idx+30]))
