import os
import re

base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
pubdir = os.path.join(base, '_publications')
entries = [
    {
        'title': '패널패키징을 위한 잉크젯 포토레지스트 Cu Bump 공정 개발\nInkjet-Printed Photoresist Cu Bump Process for Panel-Level-Packaging',
        'venue': 'KFPE 한국 유연인쇄 전자학회',
        'authors': '최유림',
        'year': 2024,
        'date': '2024-10-16 to 2024-10-18',
    },
    {
        'title': '정렬 탄소나노튜브 채널 전계효과트랜지스터를 위한 탄소나노튜브 번들 제거 공정\nRemoval of Polymer and Carbon Nanotube Bundles for Aligned Semiconductor Carbon Nanotubes Field-Effect Transistors',
        'venue': 'KFPE 한국 유연인쇄 전자학회',
        'authors': '신예현',
        'year': 2024,
        'date': '2024-10-16 to 2024-10-18',
    },
    {
        'title': '게이트 절연막 시드층 최적화를 통한 상부 게이트 MoS2 전계효과트랜지스터 제작\nTop-Gate MoS2 Field-Effect Transistors with Optimized Gate Insulator Seed Layer',
        'venue': 'KFPE 한국 유연인쇄 전자학회',
        'authors': '홍수민',
        'year': 2024,
        'date': '2024-10-16 to 2024-10-18',
    },
    {
        'title': '3D-Printed Organic Substrates for Low-Cost, Re-Distribution-Layer-Less Fanout Interposers',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(정학순), 김나현, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Interlayer Dielectric Engineering in Vertical-Channel ITO Field-Effect Transistors for Bias-Reliable Operation',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(구현호), 박민호, 이현진, 이용우, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Top-Gate Oxide Semiconductor FETs for Reliable 2T0C Read/Write Operation with Reduced Capacitive Coupling',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(박민호), 구현호, 이현진, 이용우, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Achieving Low Leakage Current in Carbon Nanotube Field-Effect Transistors Using an Extension Doping Layer',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(백승훈), 음성민, 신예현, 정학순, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Bundle-Free Aligned Semiconductor Carbon Nanotubes for Field-Effect Transistors',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(신예현), 음성민, 정학순, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Top-Gate Carbon Nanotubes Field-Effect Transistors with Buried Extension Gates for Electrostatic Doping',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(음성민), 신예현, 백승훈, 정학순, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Atomic Layer Deposition for High-Mobility and Reliable ITZO Thin Film Transistors',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(이현진), 구현호, 박민호, 이용우, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Inkjet-Printed Photoresist Films for Panel-Level Packaging Using Glass Interposers',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(최유림), 이용우, 정학순, 김나현, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': '3D-Printed Antenna-in-Package Substrates with Quasi-Coaxial Through-Vias for 5G-Advanced Applications',
        'venue': '한국반도체학술대회 (KCS 2025)',
        'authors': '(김나현), 정학순, 최유림, 이용우, 권지민',
        'year': 2025,
        'date': '2025-02-12 to 2025-02-14',
    },
    {
        'title': 'Novel Through-Hole Interconnect Technologies for 3D Printed Fanout Interposer Substrates',
        'venue': '한국유연인쇄전자학회 (KFPE 2025 춘계)',
        'authors': '(정학순), 김나현, 권지민',
        'year': 2025,
        'date': '2025-03-19 to 2025-03-21',
    },
    {
        'title': '3D-Printed Quasi-Coaxial Through-Hole Embedded Substrate for Antenna-in-Package Applications',
        'venue': '한국유연인쇄전자학회 (KFPE 2025 춘계)',
        'authors': '(김나현), 정학순, 권지민',
        'year': 2025,
        'date': '2025-03-19 to 2025-03-21',
    },
    {
        'title': 'Fabrication of RF Transmission Lines and Antenna Using EHD Inkjet Printing',
        'venue': '한국유연인쇄전자학회 (KFPE 2025 춘계)',
        'authors': '(김형준), 이용우, 권지민',
        'year': 2025,
        'date': '2025-03-19 to 2025-03-21',
    },
    {
        'title': 'Curved Through-Holes in 3D-Printed Fanout Organic Interposer Substrate',
        'venue': '한국마이크로전자 및 패키징학회 (KMEPS 2025)',
        'authors': '(정학순), 김나현, 권지민',
        'year': 2025,
        'date': '2025-04-01 to 2025-04-03',
    },
    {
        'title': 'Fabrication of Quasi-Coaxial Through-Hole Embedded Substrate\nfor Antenna-in-Package Using 3D Printing',
        'venue': '한국마이크로전자 및 패키징학회 (KMEPS 2025)',
        'authors': '(김나현), 정학순, 권지민',
        'year': 2025,
        'date': '2025-04-01 to 2025-04-03',
    },
    {
        'title': '첨단 반도체 패키징을 위한 3D 프린팅 유기 팬아웃 기판',
        'venue': '2025 한국전기전자재료학회 하계학술대회',
        'authors': '(정학순), 김나현, 권지민',
        'year': 2025,
        'date': '2025-06-18 to 2025-06-20',
    },
    {
        'title': '고정밀 마이크로 스케일 RF 부품 제작에서 전기 수력학 프린팅 기술의 디자인 룰 개발',
        'venue': '2025 한국전기전자재료학회 하계학술대회',
        'authors': '(김형준), 이용우, 김성주, 권지민',
        'year': 2025,
        'date': '2025-06-18 to 2025-06-20',
    },
    {
        'title': '마이크로스트립 구조를 이용한 유리 기판의 복소 유전율 측정',
        'venue': '2025 한국전기전자재료학회 하계학술대회',
        'authors': '(김경선), 최유림, 정학순, 권지민',
        'year': 2025,
        'date': '2025-06-18 to 2025-06-20',
    },
    {
        'title': '강화학습을 통한 첨단 반도체 패키징에서의 냉각 채널 최적 설계',
        'venue': '2025 한국전기전자재료학회 하계학술대회',
        'authors': '(김성주), 권지민',
        'year': 2025,
        'date': '2025-06-18 to 2025-06-20',
    },
    {
        'title': '균일한 Cu pillar 범프 형성을 위한 잉크젯 프린팅 포토레지스트 도포 공정 개발',
        'venue': '2025 한국전기전자재료학회 하계학술대회',
        'authors': '(최유림), 김성주, 이용우, 정예린, 권지민',
        'year': 2025,
        'date': '2025-06-18 to 2025-06-20',
    },
    {
        'title': 'High-Speed Mixed Ionic-Electronic Active Devices for Bio- and RF Signal Processing',
        'venue': 'KFPE 2025 (추계)',
        'authors': '(이용우), 정성준, 권지민',
        'year': 2025,
        'date': '2025-10-15 to 2025-10-17',
    },
    {
        'title': '3D-Printed AiP Lid Substrates with Coaxial Through-via Feeds for Improved High-Frequency Signal Integrity',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(김경선), 김나현, 정학순, 이용우, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Mixed Ionic-Electronic Conductors-based Radio-Frequency Switches with Interdigitated Channel',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(이용우), 김형준, 김경선, 정학순, 최유림, 음성민, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Fan-Out 3D-Printed Packages  with Embedded Curved Through-Hole Interconnections',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(정학순), 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Scaling Characteristics of Oxide-Based Vertical Channel Transistors for Gain-Cell Memory',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(구현호), 정학순, 박민호, 이현진, 이용우, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Design Rule Development of Electrohydrodynamic Jet Printing for UCIe Based High-Speed Interconnections',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(김형준), 이용우, 김성주, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Understanding the Interfaces in Dimension-Limited Self-Alignment for Highly Ordered Carbon Nanotube Monolayers',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(신예현), 음성민, 정학순, 백승훈, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'T-shaped Gate High Frequency Carbon Nanotube Field-Effect Transistors on Glass Substrates',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(음성민), 신예현, 백승훈, 이용우, 정학순, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Buried Electrostatic Doping Using Nonstoichiometric Silicon Nitride for Scaled N-Type MOSFET-Like CNFETs Enabling High On/Off Ratio',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(백승훈), 정학순, 신예현, 음성민, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': '3D-Printed 28-GHz Antenna-in-Package Lid Substrate Featuring 50-Ohm Quasi-Coaxial Through-Vias',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(김나현), 정학순, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Optimized FlipFET Standard Cell Design for Reduced Gate Delay and Improved Routability',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(위동진), 박민호, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Study of Substrate-Dependent Signal Integrity in Chiplet Systems',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(최유림), 이용우, 정학순, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Effect of Seed-Layer Morphology on Dielectric and Device Performance in MoS2 Field-Effect Transistors',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(홍수민), 정학순, 이상현, 박민호, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Automated Optical Detection and Thickness Estimation of 2D flakes for Large-Scale FET Data Acquisition',
        'venue': '한국반도체학술대회 (KCS 2026)',
        'authors': '(이상현), 정학순, 홍수민, 박민호, 권지민',
        'year': 2026,
        'date': '2026-01-27 to 2026-01-30',
    },
    {
        'title': 'Electrohydrodynamic Jet‑Printed Coplanar Waveguide Transmission Lines for UCIe‑Based High‑Speed Heterogeneous Systems',
        'venue': '한국마이크로전자 및 패키징학회 (KMEPS 2026)',
        'authors': '(김형준), 이용우, 김성주, 권지민',
        'year': 2026,
        'date': '2026-04-01 to 2026-04-03',
    },
    {
        'title': 'Adaptive RF Signal Control Using Mixed Ionic-Electronic Devices for Antenna Tuning and Channel Equalization',
        'venue': '한국마이크로전자 및 패키징학회 (KMEPS 2026)',
        'authors': '(이용우), 김형준, 김경선, 정학순, 음성민, 최유림, 권지민',
        'year': 2026,
        'date': '2026-04-01 to 2026-04-03',
    },
    {
        'title': 'High-Resolution Ceramic 3D Printing Using Multidose Strategies for Liquid Cooled Flip-Chip Power Packaging',
        'venue': '한국마이크로전자 및 패키징학회 (KMEPS 2026)',
        'authors': '(정학순), 김성주, 권지민',
        'year': 2026,
        'date': '2026-04-01 to 2026-04-03',
    },
    {
        'title': 'Robust CPW-Coaxial Transition Structures for 3D-Printed AiP Substrate Embedding RF Components',
        'venue': '한국마이크로전자 및 패키징학회 (KMEPS 2026)',
        'authors': '(김경선), 김나현, 정학순, 권지민',
        'year': 2026,
        'date': '2026-04-01 to 2026-04-03',
    },
]

lab_members = {
    '권지민', '정학순', '이용우', '구현호', '이현진', '신예현', '홍수민', '백승훈', '이상현', '박민호',
    '최유림', '김나현', '김형준', '김경선', '김성주', '음성민', '위동진'
}


def format_author(token):
    raw = token.strip()
    if not raw:
        return ''
    if raw.startswith('(') and raw.endswith(')'):
        inner = raw[1:-1].strip()
        if inner in lab_members:
            return f'(<strong>{inner}</strong>)'
        return raw
    if raw in lab_members:
        return f'<strong>{raw}</strong>'
    return raw

for idx, entry in enumerate(entries, start=27):
    filename = os.path.join(pubdir, f'conf-{idx:03d}.md')
    if os.path.exists(filename):
        raise SystemExit(f'File already exists: {filename}')
    authors_raw = entry['authors'].replace('\n', ', ')
    authors_tokens = [t.strip() for t in authors_raw.split(',') if t.strip()]
    authors = ', '.join(format_author(t) for t in authors_tokens)
    title = entry['title']
    if '\n' in title:
        title_block = 'title: |\n' + '\n'.join('  ' + line for line in title.split('\n'))
    else:
        title_block = f'title: "{title}"'
    content = f'''---
pub-id: {idx}
type:
    - conference-proceeding
    - domestic-conf
year: {entry['year']}

{title_block}
title_url: ""

authors: "{authors}"

status: presented
venue: "<em>{entry['venue']}</em>"
presentation_date: "{entry['date']}"
---
'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created {filename}')
