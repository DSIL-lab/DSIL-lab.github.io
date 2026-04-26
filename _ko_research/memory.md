---
title: Memory
order: 4
slug: memory
summary: |-
    - Vertical Channel Transistor Development for eDRAM
    - Reliability Analysis from Device to Memory Level
---

### Development of Oxide Semiconductor–Based Vertical Channel Transistor Device 

산화물 반도체 기반 수직채널 트랜지스터(Vertical Channel Transistor, VCT)의 성능을 향상시키기 위한 최적 공정 통합(process integration) 전략을 개발하고 검증합니다. 최근에는, VCT 제작 과정에서 발생하는 문제를 해결하기 위해 새로운 공정 방식을 도입한 연구를 수행하였습니다. ([link](https://ieeexplore.ieee.org/abstract/document/11381590)) 또한 TCAD 기반 소자 모델링을 활용하여 공정 변수들이 소자 특성에 미치는 영향을 정량적으로 파라미터화하고, 이를 통해 공정 조건과 소자 성능 간의 상관관계를 체계적으로 분석합니다. TCAD를 기반으로 다양한 공정 조건과 소자 구조를 체계적으로 탐색하고 검증하며, 이를 바탕으로 새롭고 진보적인 VCT 구조를 제안합니다. 또한 TCAD 시뮬레이션을 통해 실험적으로 직접 관측하기 어려운 전기 퍼텐셜, 전기장, 전류 밀도의 위치 의존적 분포를 분석하여, 소자 내부의 물리적 동작 메커니즘을 정밀하게 규명합니다.

![](/assets/img/research/memory-0.png)

### High performance ALD Film Development

수직채널 트랜지스터의 3차원 구조에서는 채널층의 균일하고 conformal 한 증착을 위해 원자층 증착(Atomic Layer Deposition, ALD)이 필수적입니다. 구성 원소의 조성비, 박막 두께, 도핑 전략을 체계적으로 제어하여 고품질 산화물 ALD 박막을 형성합니다. 이러한 박막은 SS, 드레인 전류(ID), 접촉저항(RC), 오프 전류(IOFF)와 같은 소자 성능 지표뿐만 아니라, XPS, XRD, UPS, ToF-SIMS, UV–Vis 분광, 라만 분광, Hall 측정 등 다양한 재료 분석 기법을 통해 종합적으로 평가합니다.

![](/assets/img/research/memory-1.png)

### Reliability Analysis from Device-level to Memory-level

VCT 공정 및 구조 공학을 통해 최적화된 고성능 ALD 산화물 박막을 기반으로, TDDB, PBS/NBS, PBTI/NBTI과 같은 신뢰성 시험을 수행하여 개별 소자의 신뢰성을 평가합니다. 또한 retention, 동작 속도, endurance와 같은 메모리 레벨 신뢰성 지표를 체계적으로 측정합니다. 나아가 전하 손실과 Vth 이동에 의해 발생하는 성능 변동이 메모리 어레이의 동작 속도, 유지 특성 및 센싱 오류에 미치는 영향을 소자 및 어레이 수준에서 정량적으로 분석합니다.

![](/assets/img/research/memory-2.png)

### Memory array / Peripheral Circuit Design for AI Computing

산화물 반도체 VCT 기반 고집적 eDRAM 어레이에 최적화된 주변회로(peripheral circuitry)를 설계하고, TCAD mixed-mode 시뮬레이션을 이용하여 셀–주변회로–배선 기생성분이 결합된 실제 동작 환경에서의 read/write, sensing, retention을 정밀하게 평가합니다. 더불어 산화물 반도체 트랜지스터의 compact model을 구축하여 SPICE 기반 어레이 레벨 시뮬레이션에 연동합니다. 이러한 모델링 프레임워크를 바탕으로 DRAM 셀을 연산 소자로 활용하는 PIM(Processing-in-Memory) 및 CIM(Compute-in-Memory) 구조로 확장하여, AI 가속을 위한 산화물 반도체 기반 메모리-연산 통합 아키텍처의 가능성을 체계적으로 검증합니다.

![](/assets/img/research/memory-3.png)