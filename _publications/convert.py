import os
import re

# 현재 폴더에서 실행 (반드시 논문 파일들이 있는 폴더 안에서 실행하세요!)
directory = '.' 

for filename in os.listdir(directory):
    # .md 파일이면서 파일명이 'jour'로 시작하는 경우에만 실행
    if filename.endswith(".md") and filename.startswith("jour"):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 정규표현식: "저자들, 제목. 저널정보"
        pattern = r'title: "(.*?), (.*?\.) (<em>.*)"'
        match = re.search(pattern, content)

        if match:
            authors_val = match.group(1).strip()
            title_val = match.group(2).strip().rstrip('.') # 제목 끝 마침표 제거
            venue_val = match.group(3).strip()

            # 데이터 치환
            # 1. title 필드 업데이트
            new_content = content.replace(match.group(0), f'title: "{title_val}"')
            # 2. authors 필드 업데이트
            new_content = new_content.replace('authors: ""', f'authors: "{authors_val}"')
            # 3. venue 필드 업데이트
            new_content = new_content.replace('venue: ""', f'venue: "{venue_val}"')

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ [Target] {filename} 처리 완료!")
        else:
            print(f"❓ {filename}은 형식이 일치하지 않아 건너뜁니다.")
    else:
        # 조건에 맞지 않는 파일은 그냥 무시함
        continue