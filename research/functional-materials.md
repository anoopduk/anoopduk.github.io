---
layout: page
title: "Molecular discovery and functional materials"
eyebrow: Research theme · Molecular design and function
description: We combine molecular generation, quantum chemistry and machine learning to discover fuel candidates, TADF emitters and other light-responsive functional molecules and materials.
permalink: /research/functional-materials/
research_theme: functional-materials
---

Molecular discovery is sometimes presented as a search for one exceptional compound. In practice, a useful candidate emerges from a sequence of decisions: which chemical space to construct, which properties to calculate, which compromises to accept and which predictions remain credible after synthesis and experiment.

Our work asks: **how can computational exploration move from molecules that are merely possible to candidates worth investigating for a particular function?**

We combine molecular generation, electronic-structure calculations, machine learning and chemical representations to explore molecular spaces and connect structure with measurable properties. Applications range from high-energy-density hydrocarbon candidates to light-emitting, photoswitchable and photosensitising molecular systems.

## What we mean by molecular discovery and functional materials

*Molecular discovery* includes generating or identifying candidate structures, calculating their properties and selecting chemically plausible candidates for further study.

A *functional molecule* is selected or designed for a measurable task: it may store and release energy, emit or switch light, produce a reactive excited state or respond to an external stimulus. When molecular behaviour is expressed in a crystal, film, device or other condensed environment, it becomes part of a functional material.

The distinction matters. A calculated molecule with an attractive property is a candidate, not automatically a material. Function may depend on several interacting factors:

- molecular constitution and three-dimensional structure;
- conformational flexibility and molecular packing;
- thermodynamic and kinetic stability;
- ground- and excited-state electronic structure;
- absorption, emission and non-radiative processes;
- synthetic accessibility;
- the surrounding solvent, solid state or device environment.

The challenge is therefore not simply to generate more molecules. It is to identify candidates that balance several requirements at once.

## A computational discovery workflow

Our studies use different computational methods depending on the chemical problem, but they share a general progression.

First, a molecular space is constructed through stochastic generation, fragment assembly, substitution around known scaffolds or chemically constrained enumeration. Duplicate and implausible structures are removed, and the remaining candidates are geometrically refined.

Electronic-structure calculations or validated machine-learned models are then used to estimate relevant properties. These may include molecular energies, heats of combustion, density, melting point, excitation energies, singlet–triplet gaps, oscillator strengths, spin–orbit coupling and charge-transfer character.

Candidates are filtered against several criteria rather than ranked by a single number. Synthetic accessibility, structural diversity and uncertainty in the calculations must also be considered.

Machine learning can accelerate this process, particularly when thousands of molecules must be evaluated. It does not replace chemical validation. Predictions remain dependent on the quality and domain of the training data, the molecular representation and the accuracy of the reference calculations.

## From generated molecules to fuel candidates

Strained and cage-like hydrocarbons can store substantial energy in their molecular structures. High energy content alone, however, does not make a useful fuel. Candidate molecules must balance heat of combustion with properties such as liquid density, melting point and chemical plausibility.

In our [study of strained hydrocarbons as potential high-energy-density fuels](https://doi.org/10.1039/D6SE00364H), we used PyAR-based molecular generation, multilevel geometry optimisation and AIQM2 thermochemical calculations to construct and evaluate candidate structures. A transfer-learned directed message-passing neural network was used to predict relevant properties across the resulting molecular space.

The filtering process identified twenty previously unreported hydrocarbons, containing no more than ten carbon atoms, that satisfied the study's first-pass criteria for net heat of combustion, density, melting point and synthetic plausibility. A topology-focused analysis also identified sixteen novel cage-like candidates.

These are computational leads, not certified aviation fuels. Practical qualification would require synthesis, measurement, safety assessment and evaluation of stability, ignition behaviour, blending and mixture-level operability. The study instead demonstrates how molecular generation and property prediction can reduce a large chemical space to a smaller and experimentally addressable set of hypotheses.

[PyAR]({{ '/research/pyar/' | relative_url }}) provides the molecular-generation framework underlying this search. Our next question is not only which candidates score well, but which structural and topological features produce the favourable combination of properties—and what a graph neural network learns about those relationships.

## Establishing design principles for TADF molecules

Thermally activated delayed fluorescence, or TADF, provides a different molecular-design problem. TADF molecules can convert triplet excitations into emissive singlet excitations through reverse intersystem crossing. This can improve the utilisation of electrically generated excitations in organic light-emitting diodes.

A small singlet–triplet energy gap is important, but it is not sufficient. Excessive separation of the donor and acceptor orbitals may reduce the oscillator strength and weaken emission. Spin–orbit coupling, molecular conformation, charge-transfer character, structural relaxation and the surrounding medium also affect performance.

Our [TD-DFT study of phenothiazine-based TADF systems](https://doi.org/10.1002/chem.202304206) examined ten experimentally studied molecular configurations. We investigated how sulfur oxidation, substitution position and donor–acceptor geometry influence excitation, charge transfer, the singlet–triplet gap, spin–orbit coupling and reverse intersystem crossing.

This work established a molecular-level account of the competing factors governing TADF and provided the foundation for moving from the analysis of selected molecules towards systematic chemical-space exploration.

## Scaling TADF discovery

In our subsequent [chemical-space study of donor–acceptor TADF emitters](https://doi.org/10.1039/D6TC00707D), fragment-based three-dimensional assembly generated 30,987 chemically realistic molecules around established donor and acceptor scaffolds.

Machine-learned geometry relaxation and successive levels of excited-state calculation were used to evaluate the candidates. The screening considered singlet–triplet gaps, oscillator strengths, spin–orbit coupling and charge-transfer character. Initial filtering produced 501 promising molecules, from which eight final candidates were selected after higher-level calculations and an assessment of synthetic accessibility through retrosynthetic analysis.

The numerical reduction—from tens of thousands of structures to a few candidates—is not the main result by itself. The study shows why molecular discovery must be multi-objective. Optimising only the singlet–triplet gap can produce molecules that are poor emitters. Photophysical promise must be considered alongside molecular stability, structural diversity and the possibility of synthesis.

## From calculations to molecules and devices

Computational screening becomes substantially more informative when it is connected to synthesis, structural characterisation, spectroscopy and device measurements.

In our collaborative [study of phenothiazine-based TADF emitters](https://doi.org/10.1039/D5SC04370K), two donor–π–acceptor molecules, NTPH and NTPCF, were investigated experimentally and computationally. Their phenothiazine units can adopt quasi-axial and quasi-equatorial conformations with different electronic structures and emission behaviour.

The relationship between conformation, charge transfer and the singlet–triplet gap helped explain their multiple emission characteristics. NTPCF also showed reversible cyan-to-orange mechanochromic emission, which was applied in an anticounterfeiting demonstration.

The emitters were incorporated into solution-processed devices, including an orange OLED and warm- and cool-white OLEDs. This study provides an important bridge between molecular calculations and functional performance: the relevant object is no longer an isolated optimised structure, but a molecule whose conformation, packing and environment influence an experimentally observable device.

## A broader family of light-responsive molecules

Our interest in functional molecular design extends beyond TADF emitters. Collaborative studies of photocages, photoswitches and photosensitisers examine how small structural changes redirect excited-state behaviour.

In a [study of phenothiazine photocages](https://doi.org/10.1039/D1CC06950K), oxygen functionalisation of the sulfur centre changed the dominant photochemical function. The parent system supported photorelease, whereas oxidation shifted the behaviour towards singlet-oxygen generation. Electronic-structure calculations helped explain how modification of one atomic centre reorganised the relevant excited states.

Our [computational investigation of donor–acceptor Stenhouse adducts](https://doi.org/10.1016/j.jphotochem.2023.115408) explored photoswitch candidates derived from Bial's reaction. Absorption, bond-length alternation, excited-state isomerisation, conical intersections, thermal cyclisation and solvent effects were examined to understand how the proposed molecules might switch between different forms. These calculations identify prospective scaffolds; experimental synthesis and switching measurements remain necessary.

We have also investigated [heavy-atom-free BODIPY derivatives as photosensitisers](https://doi.org/10.1002/asia.202401325). Static electronic-structure calculations and excited-state dynamics were combined to examine singlet-to-triplet population and the molecular features associated with singlet-oxygen generation.

Together, these studies show that function is not an intrinsic label attached to a molecular scaffold. It arises from the pathways available after the molecule absorbs energy, and these pathways can be redirected by substitution, oxidation state, conformation and environment.

## What the calculations do—and do not—establish

The presence of a molecule in a generated database does not establish that it can be synthesised. A favourable predicted property does not guarantee stability, safety or practical performance.

Machine-learned predictions can support large-scale screening, but their reliability depends on whether the proposed molecules resemble the data used to train and validate the model. Unusual bonding, extreme strain or unfamiliar electronic structures may place a candidate outside that reliable domain.

For excited-state materials, calculated descriptors are sensitive to molecular geometry and computational method. Properties measured in solution, crystals, thin films and devices may differ because of aggregation, packing, polarity and conformational restriction.

Retrosynthetic analysis can indicate that plausible synthetic routes exist, but it is not experimental synthesis. Likewise, a computationally promising fuel molecule, photoswitch or emitter should be regarded as a testable candidate rather than a completed material.

We therefore use computational discovery to formulate, compare and prioritise chemical hypotheses. Experimental collaboration determines which of those hypotheses become molecules and materials.

## Where this programme is going

The next stage is to connect molecular generation, property prediction and experimental feedback more closely. We are interested in:

- expanding chemically constrained molecular generation beyond familiar scaffolds;
- developing interpretable relationships between molecular topology and function;
- treating molecular design explicitly as a multi-objective problem;
- quantifying uncertainty and the applicability domains of machine-learned models;
- incorporating conformational, solid-state and environmental effects;
- using experimental results to refine subsequent rounds of generation and screening;
- connecting molecular candidates with realistic synthesis and device constraints.

The objective is not autonomous generation for its own sake. It is a chemically accountable discovery process in which computation narrows the search, explains the governing relationships and helps experiments ask better questions.

## Selected papers

### Property-directed molecular discovery

- S. Giri, S. Ghosal and A. Anoop, “[Data-driven exploration of synthesizable strained hydrocarbons as high-energy-density candidates for sustainable aviation fuels](https://doi.org/10.1039/D6SE00364H),” *Sustainable Energy & Fuels* (2026).

### TADF molecules and devices

- M. Banerjee and A. Anoop, “[Exploring the Theoretical Foundations of Thermally Activated Delayed Fluorescence (TADF) Emission: A Comprehensive TD-DFT Study on Phenothiazine Systems](https://doi.org/10.1002/chem.202304206),” *Chemistry – A European Journal* **30**, e202304206 (2024).
- S. Giri, M. Banerjee, A. Subhash, S. Rajesh, S. E. Padinjarethil and A. Anoop, “[Chemical Space Exploration and Molecular Design of Organic Donor–Acceptor TADF Emitters](https://doi.org/10.1039/D6TC00707D),” *Journal of Materials Chemistry C* (2026).
- P. V. Prabhu, V. Darshan, I. S. Divya, M. Banerjee, S. Varughese, A. Anoop, K. N. N. Unni and J. Joseph, “[Phenothiazine-based TADF emitters with dual conformations for single-molecule white OLEDs](https://doi.org/10.1039/D5SC04370K),” *Chemical Science* **17**, 1002–1015 (2026).

### Related light-responsive molecules

- M. Ojha, M. Banerjee, S. Ray, A. K. Singh, A. Anoop and N. D. P. Singh, “[Switching photorelease to singlet oxygen generation by oxygen functionalization of phenothiazine photocages](https://doi.org/10.1039/D1CC06950K),” *Chemical Communications* **58**, 2754–2757 (2022).
- M. Banerjee, P. R. Chandran, S. V. Nair and A. Anoop, “[Repurposing Bial's Reaction to Engender Donor–Acceptor Stenhouse Adducts: A Computational Investigation](https://doi.org/10.1016/j.jphotochem.2023.115408),” *Journal of Photochemistry and Photobiology A: Chemistry* **449**, 115408 (2024).
- M. Banerjee, S. Giri and A. Anoop, “[Computational Investigation of Meso-Substituted, Heavy Atom-Free BODIPY Derivatives as Photosensitizers: Insights From TDDFT and Dynamics Studies](https://doi.org/10.1002/asia.202401325),” *Chemistry – An Asian Journal* **20**, e202401325 (2025).

## Connected research

[Explore PyAR]({{ '/research/pyar/' | relative_url }}) · [Explore astrochemical and reaction space]({{ '/research/reaction-discovery/' | relative_url }}) · [Explore molecular aggregates, nanoclusters and nanoalloys]({{ '/research/clusters/' | relative_url }}) · [How collaborations shaped the programme](https://anooplab.github.io/research/collaborations/) · [Return to the research overview]({{ '/research/' | relative_url }}) · [Visit AnoopLab](https://anooplab.github.io/)
