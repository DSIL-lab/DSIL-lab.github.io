import os

lab_members_korean = ["권지민", "이용우", "김성주", "정학순", "조영민", "이상현", "구현호", "음성민", "양희수", "김경선", "김형준", "김나현", "신예현", "박민호", "홍수민", "최유림", "이현진", "백승훈", "위동진", "박민지"]

lab_members_english = ["Jimin Kwon", "Haksoon Jung", "Seongju Kim", "Yongwoo Lee", "Sanghyun Lee", "Hyeonho Gu", "Sungmin Eum", "Heesoo Yang", "Kyungsun Kim", "Hyeongjun Kim", "Nahyeon Kim", "Yehyun Shin", "Minho Park", "Sumin Hong", "Yurim Choi", "Hyunjin Lee", "Seunghun Baek", "Dongjin Wi", "Minji Park"]

abbrev_to_full = {
    "J. Kwon": "Jimin Kwon",
    "H. Jung": "Haksoon Jung",
    "S. Kim": "Seongju Kim",
    "Y. Lee": "Yongwoo Lee",
    "H. Lee": "Hyunjin Lee",
    "M. Park": "Minho Park",
    "G. H. Lee": "G. H. Lee",
    "I. Kim": "I. Kim",
    "E. Yang": "Heesoo Yang",
    "Y. Choi": "Yurim Choi",
    "J. Jeong": "J. Jeong",
    "S. Kim": "S. Kim",
    "H. Kim": "Hyeongjun Kim",
    "H. Gu": "Hyeonho Gu",
    "…": "...",
}

def bold_authors(authors, is_korean):
    author_list = [a.strip() for a in authors.split(',')]
    bolded = []
    for a in author_list:
        if is_korean:
            if a in lab_members_korean:
                bolded.append(f"<strong>{a}</strong>")
            else:
                bolded.append(a)
        else:
            full = abbrev_to_full.get(a, a)
            if full in lab_members_english:
                bolded.append(f"<strong>{a}</strong>")
            else:
                bolded.append(a)
    return ', '.join(bolded)

domestic_patents = [
    {"title": "반도체소자 및 반도체소자의 패터닝방법", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2026-0058388", "year": "2026"},
    {"title": "반도체소자 및 반도체소자의 패터닝방법", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2026-0058387", "year": "2026"},
    {"title": "나노 물질 광학 특성 분석을 이용한 반도체 소자 레이아웃 자동 생성 방법 및 장치", "authors": "권지민, 이상현, 이용우, 정학순", "status": "filed", "venue": "출원; 10-2026-0052953", "year": "2026"},
    {"title": "클록 분배망의 독립적 배선 구조를 이용한 클록 신호 및 로직 신호의 완전 분리형 반도체 장치 및 시스템", "authors": "권지민, 박희천, 박민호, 신예현, 김익겸", "status": "filed", "venue": "출원; 10-2025-0194458", "year": "2025"},
    {"title": "기상 증착 장치 및 이를 이용한 칼코젠 결함 회복 방법", "authors": "권지민, 정학순, 이철호", "status": "filed", "venue": "출원; 10-2025-0181247", "year": "2025"},
    {"title": "칼코젠 결함 회복을 위한 처리제 및 이를 이용한 칼코젠 결함 회복 방법", "authors": "권지민, 정학순, 이철호", "status": "filed", "venue": "출원; 10-2025-0181227", "year": "2025"},
    {"title": "인공 지능 모델에 기반한 반도체 구조물의 방열 구조를 최적화하기 위한 전자 장치, 및 그 동작 방법", "authors": "권지민, 정학순, 김성주", "status": "filed", "venue": "출원; 10-2025-0162475", "year": "2025"},
    {"title": "도면 파일에 기반하여 반도체 패키징 용 구조물을 생성하기 위한 인쇄 파일을 생성하기 위한 서버, 및 그 동작 방법", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2025-0071086", "year": "2025"},
    {"title": "3D 프린팅 기반 반도체 패키징을 위한 설계 기능을 제공하는 서버, 및 그 동작 방법", "authors": "권지민, 정학순", "status": "registered", "venue": "출원; 10-2025-0071085, 등록; 10-2942713", "year": "2025"},
    {"title": "3D 프린팅에 기반하여 형성된 반도체 패키징을 위한 기판을 포함하는 안테나 패키지, 및 이를 포함하는 전자 장치", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2025-0071081", "year": "2025"},
    {"title": "3D 프린팅에 기반하여 형성된 반도체 패키징을 위한 기판을 포함하는 칩-렌 패키지, 및 이를 포함하는 전자 장치", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2025-0071080", "year": "2025"},
    {"title": "3D 프린팅에 기반하여 형성된 반도체 패키징을 위한 기판과 결합된 구조물, 및 이를 포함하는 전자 장치", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2025-0071074", "year": "2025"},
    {"title": "3D 프린팅에 기반하여 생성된 기판 내부에 인터커넥트 구조를 형성하기 위한 장치, 및 그 제조 방법", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2025-0071073", "year": "2025"},
    {"title": "3D 프린팅에 기반하여 패턴 형성을 위한 전자 장치, 및 그 동작 방법", "authors": "권지민, 정학순", "status": "registered", "venue": "출원; 10-2025-0071068, 등록; 10-2872881", "year": "2025"},
    {"title": "3D 프린팅에 기반하여 고객 맞춤형 반도체 패키징 용 구조물을 제공하는 서버, 및 그 동작 방법", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2025-0071066", "year": "2025"},
    {"title": "3D 프린팅에 기반하여 반도체 패키징 구조물을 제조하기 위한 소재", "authors": "권지민, 정학순", "status": "filed", "venue": "출원; 10-2025-0071064", "year": "2025"},
    {"title": "이온 박막 트랜지스터에 기반한 RF 신호의 반사 조절을 위한 전자 장치 및 그 동작 방법", "authors": "권지민, 이용우, 정학순", "status": "filed", "venue": "출원; 10-2025-0005702", "year": "2025"},
    {"title": "이온 게이트 박막 트랜지스터를 포함하는 반사 부재 전자 장치 및 그 동작 방법", "authors": "권지민, 이용우, 정학순", "status": "filed", "venue": "출원; 10-2025-0005699", "year": "2025"},
    {"title": "게이트 절연층을 포함하는 수직 구조의 트랜지스터 및 그 제조 방법", "authors": "권지민, 이현진, 정학순, 박민호, 이용우", "status": "registered", "venue": "출원; 10-2025-0002764, 등록; 10-2925208", "year": "2025"},
    {"title": "수직채널 반도체 소자 및 그 제조 방법", "authors": "권지민, 구현호, 박민호, 이용우", "status": "filed", "venue": "출원; 10-2025-0002761", "year": "2025"},
    {"title": "고해상도 유기 발광 소자 픽셀 패턴의 제조방법 및 그에 의해 제조된 고해상도 유기 발광 소자 픽셀 패턴", "authors": "권지민, 정학순", "status": "registered", "venue": "출원; 10-2024-0202220, 등록; 10-2907244", "year": "2024"},
    {"title": "연신 박막 트랜지스터, 연신 패널 및 전자 장치", "authors": "이계황, 권지민, 노용영, 강현범, 김형준, 김민규, 정학순", "status": "filed", "venue": "출원; 10-2024-0080521", "year": "2024"},
    {"title": "3D 프린팅 기반 소비자 맞춤형 반도체 패키징을 위한 장치, 서버, 시스템, 및 그 동작 방법", "authors": "권지민, 정학순", "status": "registered", "venue": "출원; 10-2023-0170852, 등록; 10-2834356", "year": "2023"},
]

us_patents = [
    {"title": "ELECTRONIC DEVICE FOR OPTIMIZING HEAT DISSIPATION STRUCTURE OF SEMICONDUCTOR STRUCTURE BASED ON ARTIFICIAL INTELLIGENCE MODEL, AND OPERATING METHOD THEREOF", "authors": "J. Kwon, H. Jung, S. Kim", "status": "filed", "venue": "Filed; 19/379,913(US)", "year": "2025"},
    {"title": "VERTICAL TRANSISTOR INCLUDING GATE INSULATING LAYER AND MANUFACTURING METHOD THEREOF", "authors": "J. Kwon, H. Lee, H. Jung, M. Park, Y. Lee", "status": "filed", "venue": "Filed; 19/375,205(US)", "year": "2025"},
    {"title": "STRETCHABLE THIN FILM TRANSISTOR, STRETCHABLE PANEL, AND ELECTRONIC DEVICE", "authors": "G. H. Lee, …, H. Jung", "status": "filed", "venue": "Filed; 19/237,774(US)", "year": "2025"},
    {"title": "ANTENNA PACKAGE INCLUDING A SUBSTRATE FOR SEMICONDUCTOR PACKAGING FORMED BASED ON 3DP, AND AN ELECTRONIC DEVICE INCLUDING THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 18/976381(US)", "year": "2025"},
    {"title": "CHIP-LET PACKAGE INCLUDING A SUBSTRATE FOR SEMICONDUCTOR PACKAGING FORMED BASED ON 3DP, AND AN ELECTRONIC DEVICE INCLUDING THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 18/976379(US)", "year": "2025"},
    {"title": "STRUCTURE COMBINED WITH A SUBSTRATE FOR SEMICONDUCTOR PACKAGING FORMED BASED ON 3DP, AND AN ELECTRONIC DEVICE INCLUDING THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 18/976377(US)", "year": "2025"},
    {"title": "APPARATUS FOR FORMING INTERCONNECT STRUCTURES INSIDE A SUBSTRATE FORMED BASED ON 3D PRINTING, AND PROCESS METHOD OF THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 18/976376(US)", "year": "2025"},
    {"title": "MATERIAL FOR PRODUCING A SEMICONDUCTOR PACKAGING STRUCTURE BASED ON 3D PRINTING", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 18/976375(US)", "year": "2025"},
    {"title": "APPARATUS FOR CUSTOMIZED SEMICONDUCTOR PACKAGING, SERVER, SYSTEM AND OPERATION METHOD OF THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 18/964696(US)", "year": "2025"},
]

eu_patents = [
    {"title": "ELECTRONIC DEVICE FOR OPTIMIZING HEAT DISSIPATION STRUCTURE OF SEMICONDUCTOR STRUCTURE BASED ON ARTIFICIAL INTELLIGENCE MODEL, AND OPERATING METHOD THEREOF", "authors": "J. Kwon, H. Jung, S. Kim", "status": "filed", "venue": "Filed; 25213729.4(EU)", "year": "2025"},
    {"title": "VERTICAL TRANSISTOR INCLUDING GATE INSULATING LAYER AND MANUFACTURING METHOD THEREOF", "authors": "J. Kwon, H. Lee, H. Jung, M. Park, Y. Lee", "status": "filed", "venue": "Filed; 25212389.8(EU)", "year": "2025"},
    {"title": "ANTENNA PACKAGE INCLUDING A SUBSTRATE FOR SEMICONDUCTOR PACKAGING FORMED BASED ON 3DP, AND AN ELECTRONIC DEVICE INCLUDING THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 24218387.9(EU)", "year": "2025"},
    {"title": "CHIP-LET PACKAGE INCLUDING A SUBSTRATE FOR SEMICONDUCTOR PACKAGING FORMED BASED ON 3DP, AND AN ELECTRONIC DEVICE INCLUDING THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 24218385.3(EU)", "year": "2025"},
    {"title": "STRUCTURE COMBINED WITH A SUBSTRATE FOR SEMICONDUCTOR PACKAGING FORMED BASED ON 3DP, AND AN ELECTRONIC DEVICE INCLUDING THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 24218382.0(EU)", "year": "2025"},
    {"title": "APPARATUS FOR FORMING INTERCONNECT STRUCTURES INSIDE A SUBSTRATE FORMED BASED ON 3D PRINTING, AND PROCESS METHOD OF THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 24218381.2(EU)", "year": "2025"},
    {"title": "MATERIAL FOR A SUBSTRATE FOR ELECTRICAL CONNECTION AND SUBSTRATE FOR ELECTRICAL CONNECTION BETWEEN ELECTRONIC COMPONENTS", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 24218377.0(EU)", "year": "2025"},
    {"title": "APPARATUS FOR CUSTOMIZED SEMICONDUCTOR PACKAGING, SERVER, SYSTEM AND OPERATION METHOD OF THE SAME", "authors": "J. Kwon, H. Jung", "status": "filed", "venue": "Filed; 24216097.6(EU)", "year": "2025"},
]

jp_patents = [
    {"title": "인공 지능 모델에 기반한 반도체 구조물의 방열 구조를 최적화하기 위한 전자 장치, 및 그 동작 방법", "authors": "권지민, 정학순, 김성주", "status": "filed", "venue": "Filed; 2025-187821(JP)", "year": "2025"},
    {"title": "게이트 절연층을 포함하는 수직 구조의 트랜지스터 및 그 제조 방법", "authors": "권지민, 이현진, 정학순, 박민호, 이용우", "status": "filed", "venue": "Filed; 2025-183947(JP)", "year": "2025"},
    {"title": "3DP에 기반하여 형성된 반도체 패키징 용 기판을 포함하는 안테나 패키지, 및 이를 포함하는 전자 장치", "authors": "권지민, 정학순", "status": "filed", "venue": "Filed; 2024-221495(JP)", "year": "2024"},
    {"title": "3DP에 기반하여 형성된 반도체 패키징 용 기판과 결합되는 구조물, 및 이를 포함하는 전자 장치", "authors": "권지민, 정학순", "status": "filed", "venue": "Filed; 2024-221492(JP)", "year": "2024"},
    {"title": "3DP에 기반하여 형성된 반도체 패키징 용 기판을 포함하는 칩-렛 패키지, 및 이를 포함하는 전자 장치", "authors": "권지민, 정학순", "status": "filed", "venue": "Filed; 2024-221477(JP)", "year": "2024"},
    {"title": "3D 프린팅에 기반하여 형성된 기판 내부의 인터커넥트 구조를 형성하기 위한 장치, 및 공정 방법", "authors": "권지민, 정학순", "status": "filed", "venue": "Filed; 2024-221476(JP)", "year": "2024"},
    {"title": "3D 프린팅에 기반하여 반도체 패키징 구조물을 생성하기 위한 소재", "authors": "권지민, 정학순", "status": "filed", "venue": "Filed; 2024-221471(JP)", "year": "2024"},
    {"title": "3D 프린팅 기반 소비자 맞춤형 반도체 패키징을 위한 장치, 서버, 시스템, 및 그 동작 방법", "authors": "권지민, 정학순", "status": "filed", "venue": "Filed; 2024-207709(JP)", "year": "2024"},
]

cn_patents = [
    {"title": "STRETCHABLE THIN FILM TRANSISTOR, STRETCHABLE PANEL, AND ELECTRONIC DEVICE", "authors": "G. H. Lee, …, H. Jung", "status": "filed", "venue": "Filed; 202510819824.X(CN)", "year": "2025"},
]

all_patents = domestic_patents + us_patents + eu_patents + jp_patents + cn_patents

for i, p in enumerate(all_patents, 1):
    pub_id = f"{i:03d}"
    is_korean = p in domestic_patents or p in jp_patents
    authors_bolded = bold_authors(p['authors'], is_korean)
    content = f"""---
pub-id: {pub_id}
type:
    - patent
year: {p['year']}
title: "{p['title']}"
title_url: ""
authors: "{authors_bolded}"
status: {p['status']}
venue: "<em>{p['venue']}</em>"
---"""
    filename = f"pat-{pub_id}.md"
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Created {filename}")
    except Exception as e:
        print(f"Error creating {filename}: {e}")

print("Patent files generation completed.")