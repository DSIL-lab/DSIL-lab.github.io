---
order: 26
date: "Apr 06, 2026"
slug: vlsi-2026-paper-acceptance
title: "양희수 (석박통합 2년차)·김형준 (석박통합 2년차) 학생, IEEE VLSI Symposium 2026 논문 채택"
image: ""
summary: |-
    - 제목: Vertical-Die (V-die) 3.5D Integration for Cool Ultrahigh-Bandwidth Memory Systems ([link](https://ieeexplore.ieee.org/document/11577552))

    양희수 (석박통합 2년차), 김형준 (석박통합 2년차) 학생이 <strong>세계 최고 권위 소자·회로 통합 학회인 IEEE Symposium on VLSI Technology and Circuits (VLSI) 2026</strong>에 제출한 논문이 채택되었습니다. 한밭대학교 (Prof. 김성주), UNIST (Prof. 감동윤) 기관들과 공동연구를 통해 연구 성과를 창출하였습니다.

    본 연구에서는 DRAM 다이를 인터포저 위에 수직으로 세워 배치하는 3.5D V-die 메모리 구조를 제안하여, TSV 개수에 의해 제한되던 기존 HBM의 I/O 확장성과 발열 문제를 동시에 해결하는 방안을 제시하였습니다.

    관련 기사: [전자신문] 누운 HBM 세웠더니 대역폭 4배…'수직 다이' 개발 박차 ([link](https://www.etnews.com/20260408000313))

    해외 보도: [IEEE Spectrum] Stacking Chips Sideways Gives AI More Memory ([link](https://spectrum.ieee.org/stacking-chips-sideways))

    
---

- 제목: Vertical-Die (V-die) 3.5D Integration for Cool Ultrahigh-Bandwidth Memory Systems ([link](https://ieeexplore.ieee.org/document/11577552))

양희수 (석박통합 2년차), 김형준 (석박통합 2년차) 학생이 세계 최고 권위 소자·회로 통합 학회인 IEEE Symposium on VLSI Technology and Circuits (VLSI) 2026에 제출한 논문이 채택되었습니다.

본 연구에서는 기존 방식으로 제작된 DRAM 다이를 90도 회전시켜 인터포저 위에 수직으로 세워 배치하는 3.5D V-die 메모리 구조를 제안하였습니다. 현재 HBM은 TSV가 차지하는 면적 때문에 I/O 핀 수를 늘리는 데 한계가 있으며, 다이를 높이 적층할수록 수직 방향으로 열이 축적되어 용량 확장이 제약을 받습니다.

제안한 구조는 다이의 인터포저 대면 측면 전체를 I/O 라우팅에 활용하고, Cu 필러 범프 대신 20 µm 피치의 인듐 범프를 적용하여 I/O 핀 수를 HBM4 대비 최대 4배까지 확보하였습니다. 유리 기판 위에 제작한 CPW 구조로 추출한 물성을 바탕으로 EM 시뮬레이션을 수행한 결과, 최악 조건인 11 mm RDL 길이에서도 삽입 손실과 크로스토크가 HBM 채널과 동등한 수준을 유지하였으며, 아이 개구부는 JEDEC HBM4 수신단 요구사항(0.3 UI / 100 mV)을 상회하였습니다.

시스템 수준의 평가에서는 gem5 기반 벤치마크를 통해 HBM4 대비 4.01배의 최대 대역폭과 37.2% 낮은 읽기 지연시간을 확인하였습니다. 또한 LLMCompass를 활용하여 GPT-3급 175B 파라미터 LLM 워크로드를 평가한 결과, 디코드 처리량이 1.82배 향상되었고 컨텍스트 길이 증가에 따른 성능 저하도 크게 완화되었습니다. 다이 사이에 냉각수를 직접 흘리는 inter-die 직접 액체 냉각(DLC)을 적용하여, HBM4의 최대 온도 90 °C 대비 45 °C 수준의 온도를 유지할 수 있음을 열 해석으로 확인하였습니다.

한밭대학교 (Prof. 김성주), UNIST (Prof. 감동윤) 기관들과 공동연구를 통해 연구 성과를 창출하였습니다.

본 연구는 삼성전자 미래기술육성사업의 지원을 받아 수행되었습니다.

관련 기사: [전자신문] 누운 HBM 세웠더니 대역폭 4배…'수직 다이' 개발 박차 ([link](https://www.etnews.com/20260408000313))

해외 보도: [IEEE Spectrum] Stacking Chips Sideways Gives AI More Memory ([link](https://spectrum.ieee.org/stacking-chips-sideways))


