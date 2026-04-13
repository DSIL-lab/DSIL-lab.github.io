---
title: Logic TEAM
order: 3
slug: logic
summary: |-
    - Two-dimensional transition metal dichalcogenides (TMDs)
    - One-dimensional carbon nanotubes (CNTs)
---

실리콘 기반 전계효과 트랜지스터는 미세화 한계에 근접함에 따라, 기존 스케일링만으로는 성능 향상을 지속하기가 점점 어려워 짐. 이러한 한계를 극복하기 위해, **Gate-All-Around(GAA) FET, Complementary FET(CFET), FlipFET**와 같은 차세대 소자 구조와 함께, 저차원 채널 소재를 활용한 새로운 논리 소자 기술이 활발히 연구되고 있음.
특히 2차원 전이금속 칼코겐화물(TMDs)과 1차원 탄소나노튜브(CNTs)는 스케일 축소 환경에서도 우수한 전기적 특성을 유지할 수 있으며, 저온 공정이 가능해 BEOL 공정과의 높은 호환성을 가짐. 이러한 특성은 순차적 소자 적층과 수직 집적이 가능한 모놀리식 3D 집적 기술을 실현하는 데 중요한 장점으로 작용함.

## Two-dimensional transition metal dichalcogenides (TMDs)

### Single-crystalline 2D channel

본 연구는 2차원 반도체를 트랜지스터 채널 소재로 활용하기 위한 포괄적인 연구 프레임워크를 구축하는 것을 목표로 한다. 먼저 단결정 2D 단일 플레이크(single-flake) 트랜지스터를 제작하여, 플레이크 두께와 재료 균일성이 소자 전기적 특성에 미치는 영향을 체계적·통계적으로 분석함.
이후 단일 플레이크 소자에서 도출된 물리적·전기적 인사이트를 기반으로, 전사된 2D 박막(film) 기반 트랜지스터로 연구 범위를 확장함. 이러한 연속적인 연구 흐름을 통해, 2D 반도체 채널에 대한 기초 물성 이해와 실제 소자 구현 간의 간극을 연결하고자 함.

![](/assets/img/research/logic-0.png)

### High performance TMD FETs

본 연구는 2차원 반도체를 트랜지스터 채널로 상용화하기 위한 성능 및 신뢰성 향상을 목표로 함. 로직 소자 적용이 가능한 탑게이트(top-gated) 2D FET 구조를 중심으로, 초박막 2D 소재에서 발생하는 높은 접촉 저항과 균일하고 고품질의 게이트 스택 형성의 어려움과 같은 핵심 문제를 다룸.
이를 해결하기 위해 접촉 공학(contact engineering)과 시드층/계면 공학을 적용하여 균일한 유전막 증착을 구현하고, 단일 플레이크 수준에서 전기적 특성의 변동성과 신뢰성 지표를 정량적으로 분석함. 나아가, 2D 필름 공정을 도입한 웨이퍼 스케일 대면적 소자 제작으로 연구 범위를 확장함으로써, 실제 집적 환경에서의 2D 채널 적용 가능성을 검증하고 나노스케일 소자 및 스케일링을 향한 기술적 기반을 구축함.

![](/assets/img/research/logic-1.png)

## One-dimensional carbon nanotubes (CNTs)

### High density aligned CNT channel

탄소나노튜브(CNT)를 트랜지스터 채널 소재로 활용하기 위해, 본 연구는 고순도 반도체성 CNT의 분리 및 고밀도·고정렬 CNT 박막 제작을 목표로 한다.
먼저, 용액 공정 기반의 래핑 폴리머(wrapping polymer) 기법을 이용해 금속성 CNT와 반도체성 CNT를 분리하며, 해당 메커니즘 분석을 통해 99.9999% 이상의 반도체성 CNT 순도 달성을 지향한다. 이후, 정렬된 CNT 코팅을 위해 Dimension-limited Self-Alignment(DLSA) 기법을 적용하고, 유체역학 및 물성 분석을 통해 정렬 정밀도를 향상시키고 CNT 적층을 최소화한다. 더 나아가, 튜브 간 간격이 균일한 고질서 CNT 박막을 구현하기 위한 새로운 정렬 공정을 개발한다.
이렇게 확보된 고정렬 CNT 박막을 기반으로 정렬형 CNFET을 제작하고, 이를 CFET 및 GAA FET와 같은 차세대 소자 구조에 적용하는 것을 목표로 한다.

![](/assets/img/research/logic-2.png)

### High performance CNT-FETs

CNT는 높은 캐리어 이동도와 밀도, 그리고 준 1차원 수송 특성으로 인해 강력한 전기적 제어와 높은 구동 전류를 제공함. 그러나 CNT의 상대적으로 작은 밴드갭은 MOSFET 유사 구조의 CNFET에서 오프 상태 누설 전류를 증가시키며, 이는 주로 게이트 언더랩 및 소스/드레인 확장 영역에서의 밴드-투-밴드 터널링에 기인함.
본 연구는 GAA 구조 및 BEOL 호환성을 유지하면서 CNT 채널을 효과적으로 바텀 사이드 도핑할 수 있는 구조적 해법에 초점을 맞춤. 나아가, 해당 소자 개념을 기반으로 수직 적층된 CNFET 기반 CFET 구조와 DTCO(Design-Technology Co-Optimization) 기반 표준 셀 최적화를 수행함. 블록 수준의 PPA(Power–Performance–Area) 벤치마킹을 통해, 저차원 채널 소재 기반 논리 소자의 성능 한계를 규명하고, 미래 모놀리식 3D 집적 시스템을 위한 기술적 확장을 도모함.

![](/assets/img/research/logic-3.png)