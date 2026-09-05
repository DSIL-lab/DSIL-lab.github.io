---
order: 26
date: "Apr 06, 2026"
slug: vlsi-2026-paper-acceptance
title: "Paper Co-First-Authored by Heesoo Yang and Hyeongjun Kim (Integrated M.S./Ph.D., 2nd year) Accepted to IEEE VLSI Symposium 2026"
image: ""
summary: |-
    - Title : Vertical-Die (V-die) 3.5D Integration for Cool Ultrahigh-Bandwidth Memory Systems ([link](https://ieeexplore.ieee.org/document/11577552))

    A paper by Heesoo Yang and Hyeongjun Kim (both 2nd-year integrated MS/PhD students) has been accepted at the <strong>IEEE Symposium on VLSI Technology and Circuits (VLSI) 2026</strong>, one of the most prestigious international conferences on integrated device and circuit technology. The work was carried out in collaboration with Hanbat National University (Prof. Seongju Kim) and UNIST (Prof. Dongyun Kam).

    This work proposes a 3.5D V-die memory architecture in which DRAM dies are oriented upright on an interposer, addressing both the TSV-limited I/O scalability and the thermal constraints of conventional HBM.

    Related coverage: [ETNews] Standing HBM upright quadruples bandwidth — accelerating "vertical die" development ([link](https://www.etnews.com/20260408000313))

    International coverage: [IEEE Spectrum] Stacking Chips Sideways Gives AI More Memory ([link](https://spectrum.ieee.org/stacking-chips-sideways))
---

- Title: Vertical-Die (V-die) 3.5D Integration for Cool Ultrahigh-Bandwidth Memory Systems ([link](https://ieeexplore.ieee.org/document/11577552))

A paper by Heesoo Yang and Hyeongjun Kim (both 2nd-year integrated MS/PhD students) has been accepted at the IEEE Symposium on VLSI Technology and Circuits (VLSI) 2026, one of the most prestigious international conferences on integrated device and circuit technology.

This work proposes a 3.5D V-die memory architecture in which conventionally fabricated DRAM dies are rotated upright and arranged horizontally on an interposer. In current HBM, the footprint occupied by TSVs limits how far the I/O pin count can scale, while heat accumulating vertically through densely stacked dies constrains capacity scaling.

The proposed architecture uses the entire interposer-facing sidewall of each die for I/O routing and replaces Cu pillar bumps with 20 µm pitch indium bumps, increasing the total I/O count by up to 4× over HBM4. EM simulations calibrated against CPW structures fabricated on a glass substrate show that, even at a worst-case RDL length of 11 mm, insertion loss and crosstalk remain comparable to conventional HBM channels, with eye openings exceeding the JEDEC HBM4 receiver mask requirements (0.3 UI / 100 mV).

At the system level, gem5-based benchmarks show 4.01× higher peak bandwidth and 37.2% lower read latency than HBM4. Evaluation with LLMCompass on a GPT-3-class 175B-parameter LLM workload yielded 1.82× higher decode throughput, with substantially less degradation as context length scales. Thermal analysis confirms that inter-die direct liquid cooling keeps the V-die at 45 °C, compared with a 90 °C maximum for HBM4.

The work was carried out in collaboration with Hanbat National University (Prof. Seongju Kim) and UNIST (Prof. Dongyun Kam).

This research was supported by the Samsung Research Funding & Incubation Center for Future Technology.

Related coverage: [ETNews] Standing HBM upright quadruples bandwidth — accelerating "vertical die" development ([link](https://www.etnews.com/20260408000313))

International coverage: [IEEE Spectrum] Stacking Chips Sideways Gives AI More Memory ([link](https://spectrum.ieee.org/stacking-chips-sideways))


