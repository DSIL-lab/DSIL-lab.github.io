import re
text='authors: "<strong>Nahyeon Kim</strong> (Presenter), <strong>Haksoon Jung*</strong>, <strong>Yurim Choi</strong>, <strong>Hyeongjun Kim</strong>, <strong>Seongju Kim</strong>, <strong>Yongwoo Lee</strong>, Yunsik Park, Seungyeon Koh, Hyeok Kim, <strong>Jimin Kwon</strong>*"'
pattern=re.compile(r'(<strong>[^<]+)</strong>\*')
print(pattern.search(text) is not None)
print(pattern.sub(r'\1*</strong>', text))
