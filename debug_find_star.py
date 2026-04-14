import pathlib, re
root = pathlib.Path(r'C:\LabHomepage_Edit\DSIL-lab.github.io\_publications')
pattern = re.compile(r'(<strong>[^<]+)</strong>\*')
for path in sorted(root.glob('*.md')):
    text = path.read_text(encoding='utf-8')
    matches = pattern.findall(text)
    if matches:
        print(path.name)
        for m in matches:
            print('  ', m)
