import pathlib
root = pathlib.Path(r'C:\LabHomepage_Edit\DSIL-lab.github.io\_publications')
names=['Jimin Kwon','Yongwoo Lee','Seongju Kim','Haksoon Jung','Youngmin Jo','Sanghyun Lee','Hyeonho Gu','Sungmin Eum','Heesoo Yang','Kyungsun Kim','Hyeongjun Kim','Nahyeon Kim','Yehyun Shin','Minho Park','Sumin Hong','Yurim Choi','Hyeonjin Lee','Seunghun Baek','Dongjin Wi','Min Ji Park']
for path in sorted(root.glob('*.md')):
    text = path.read_text(encoding='utf-8')
    missing = [n for n in names if n in text and f'<strong>{n}</strong>' not in text]
    if missing:
        print(path.name, missing)
