import pathlib
root = pathlib.Path(r'C:\LabHomepage_Edit\DSIL-lab.github.io\_publications')
print(root)
print(root.exists())
print(len(list(root.glob('*.md'))))
for path in list(root.glob('*.md'))[:3]:
    print(path)
