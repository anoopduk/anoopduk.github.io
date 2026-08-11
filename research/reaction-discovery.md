---
layout: page
title: "Automated reaction discovery and astrochemical space"
eyebrow: Research theme · Astrochemistry and reaction discovery
description: We explore molecular chemical space and reaction pathways to develop testable hypotheses in astrochemistry and prebiotic chemistry.
permalink: /research/reaction-discovery/
research_theme: reaction-discovery
---

Astrochemical exploration begins with two related questions: which molecules may be possible within a chosen composition, and how might those molecules form under a particular environment?

Reaction mechanisms are often investigated by proposing a likely product or intermediate and then calculating a pathway to it. This is useful, but the search remains limited by what the researcher thought to draw. A molecular inventory assembled only from known compounds creates a similar limitation.

Our work therefore asks a broader question: **given a collection of atoms or starting molecules, what structures, products and pathways become visible when the corresponding chemical space is explored systematically?**

We use stochastic molecular generation, automated reaction search, electronic-structure calculations and molecular representations to identify candidate structures and examine the pathways connecting them. Astrochemistry and prebiotic chemistry are demanding applications: chemically simple species can generate unexpectedly large spaces, while the environments in which the chemistry occurs remain difficult to reproduce and constrain.

## Chemical space and reaction space

Chemical space is the set of molecular structures that can be constructed from a chosen collection of atoms. It includes constitutional isomers, stereoisomers, conformers, radicals, ionic species and molecular complexes.

Reaction space adds the transformations connecting those structures. It includes:

- different orientations through which reactants may encounter one another;
- bond formation, bond breaking and atom-transfer events;
- intermediates, products and competing reaction channels;
- transition states and minimum-energy paths;
- oligomerisation, isomerisation and fragmentation;
- the effects of charge, spin, temperature, radiation and environment.

In short, **chemical space asks what molecules are possible; reaction space asks how they may be connected and at what energetic cost.**

No finite calculation can enumerate all possible chemistry. Our purpose is to sample chemical and reaction spaces more broadly and reproducibly, reducing dependence on a molecular inventory or mechanism chosen in advance.

## HydroMol: mapping small hydrocarbon space

Small hydrocarbons are abundant and reactive in interstellar, circumstellar and planetary environments. Even when the numbers of carbon and hydrogen atoms are restricted, changes in connectivity, unsaturation, ring formation and molecular topology produce many possible structures.

In our [HydroMol study](https://doi.org/10.1002/jcc.70236), more than 2,700 neutral hydrocarbons with compositions CₙHₘ, where *n* and *m* range from 1 to 10, were generated stochastically and refined using density-functional theory. Approximately 2,000 of the resulting structures were absent from the major chemical repositories examined in the study.

The structures, geometries, thermodynamic parameters and electronic properties are available through the open-access [HydroMol chemical-space explorer](https://hydromol.github.io/). The resource provides a searchable molecular inventory for computational astrochemistry and a starting point for identifying possible observational or spectroscopic targets.

HydroMol establishes which structures appear in a defined computational chemical space; it does not establish that those molecules exist in an astronomical environment. Formation pathways, destruction processes, abundance, stability under the relevant conditions and sufficiently distinctive spectra must still be investigated. This is where chemical-space exploration connects to reaction discovery.

## From an automated search to a reaction mechanism

We begin by generating multiple relative orientations of the reactants. Artificial-force or AFIR-style biased optimisations encourage different bond rearrangements and produce candidate products and intermediates.

Chemically equivalent results are identified and removed. Distinct candidates are then relaxed and classified. Promising transformations are examined using minimum-energy-path calculations, transition-state optimisation, frequency analysis and intrinsic reaction-coordinate calculations.

Reaction energies tell us whether a transformation is energetically favourable. Activation barriers address whether it may be kinetically accessible. When astronomical or laboratory detection is relevant, calculated rotational and vibrational parameters can provide signatures for searching for the predicted molecules.

[PyAR](https://anoopduk.github.io/research/pyar/) provides the structure-generation and reaction-search framework. The subsequent mechanistic calculations determine which search results deserve to be treated as chemically meaningful pathways.

## Why prebiotic chemistry?

Here, *prebiotic chemistry* means abiotic chemistry that may precede biology and generate molecular precursors relevant to later chemical evolution. It does not mean that every computed molecule participated in the origin of life.

Hydrogen cyanide is a useful starting point. It is a small carbon–nitrogen molecule found in terrestrial and extraterrestrial chemical environments, yet its oligomerisation can produce a surprisingly diverse family of structures. Some of these structures are chemically connected to intermediates used in proposed syntheses of nucleobases and other biomolecular precursors.

This combination—simple reactants, large reaction space and uncertain environmental conditions—makes HCN chemistry a stringent test for automated discovery.

## A progression through our studies

### Photochemistry changes the accessible pathways

Our earlier [study of the photochemical conversion of an HCN tetramer](https://doi.org/10.1002/anie.201303246) examined a step leading towards a purine precursor. The absorbed energy dissipates on a picosecond timescale, making a hot ground-state mechanism unlikely. Instead, successive photoexcitation and internal conversion drive the transformation through an excited azetene structure.

This result illustrates an important limitation of a purely thermal reaction map: the available pathways depend on the source and form of energy.

### Automated exploration of HCN oligomerisation

In our [automated study of HCN tetramerisation](https://doi.org/10.1002/chem.201705492), we explored the HCN dimer space in detail and followed selected structures towards larger oligomers. Molecular fingerprints were used to recognise similar products and reduce repeated exploration.

The search produced four thermal routes towards cis/trans-DAMN-related tetramers and 4-amino-1H-imidazole-5-carbonitrile, intermediates associated with proposed prebiotic syntheses. The broader result was methodological: automated sampling revealed alternative pathways without requiring every product to be specified beforehand.

### From selected molecules to an isomeric landscape

The [C₂H₃NO study](https://doi.org/10.1021/acsearthspacechem.3c00113) widened the question from one oligomerisation sequence to an entire molecular formula. Density-functional calculations identified 33 isomers, including eleven lying within 50 kcal mol⁻¹ of the lowest-energy structure.

We then explored bimolecular reactions involving HCN and formaldehyde using an artificial-force-induced search, followed by minimum-energy-path and transition-state calculations. Oxiran-2-ylazanide and isocyanomethanol emerged as kinetically favoured products in the investigated pathways.

This study connects two levels of exploration: identifying which structures exist in a chemical space and determining how selected structures may be formed.

### From individual reactions to a network

Our [study of HCN, HNC and ammonia reactions](https://doi.org/10.1021/acsearthspacechem.3c00321) examined a Titan-motivated extraterrestrial environment. The initial search identified formamidine, formaldehyde hydrazone and methanediimine. Secondary searches generated a wider set of products containing imine, amine, nitrile and nitrogen-heterocyclic motifs.

Calculated reaction paths revealed both favourable transformations and significant kinetic bottlenecks. Some gas-phase barriers may be too high for direct thermal access under Titan-like temperatures. Solvation, surfaces, radiation and quantum tunnelling could alter those barriers, but they must be investigated rather than assumed.

Theoretical rotational and vibrational parameters were also calculated so that some predicted products could, in principle, be sought experimentally or observationally.

## What the calculations do—and do not—establish

Finding a stable structure in a generated chemical space establishes that a minimum has been located under a specified computational model. It does not establish that the molecule is synthesised in nature, survives in an astronomical environment or reaches an observable abundance.

Similarly, finding a product in an automated reaction search establishes that a computational pathway has been located. It does not establish that the molecule formed in a planetary atmosphere, an interstellar cloud or the early Earth.

Thermodynamic stability does not guarantee kinetic accessibility. A low barrier does not guarantee appreciable abundance. Concentration, temperature, pressure, radiation, solvent, ice or mineral surfaces, competing reactions and destruction pathways all influence the resulting chemistry.

Conversely, failure to find a pathway is not proof that it is impossible. Every search is limited by its sampling, electronic-structure method, charge and spin states, and representation of the environment.

We therefore treat chemical-space and reaction-space exploration as means of generating and ranking testable chemical hypotheses. Experiment, astronomical observation and further computation remain necessary.

## Where this programme is going

The next challenge is to move from collections of reaction candidates towards chemically interpretable networks. We are interested in combining:

- broader and more systematic molecular- and reaction-space sampling;
- validated electronic-structure calculations;
- reaction kinetics and competing pathways;
- gas-phase, solvent, ice and surface environments;
- thermal and photochemical processes;
- calculated spectroscopic observables;
- machine-learned potentials with explicit validation and uncertainty.

The objective is not simply to generate more molecules. It is to determine which parts of large chemical and reaction spaces remain plausible after energetic, kinetic, spectroscopic and environmental constraints are applied.

## Selected papers

- S. Giri, S. Satpati, T. Roy, S. Ghosal and A. Anoop, “[Computational Exploration of Small Hydrocarbon Networks: A Stochastic Generation and DFT Refinement Framework](https://doi.org/10.1002/jcc.70236),” *Journal of Computational Chemistry* **46**, e70236 (2025).
- E. Boulanger, A. Anoop, D. Nachtigallová, W. Thiel and M. Barbatti, “[Photochemical Steps in the Prebiotic Synthesis of Purine Precursors from HCN](https://doi.org/10.1002/anie.201303246),” *Angewandte Chemie International Edition* **52**, 8000–8003 (2013).
- S. Nandi, D. Bhattacharyya and A. Anoop, “[Prebiotic Chemistry of HCN Tetramerization by Automated Reaction Search](https://doi.org/10.1002/chem.201705492),” *Chemistry – A European Journal* **24**, 4885–4894 (2018).
- S. Panda, A. Chiranjibi, D. Awasthi, S. Ghosal and A. Anoop, “[Exploring the Chemical Space of C₂H₃NO Isomers and Bimolecular Reactions with Hydrogen Cyanide and Formaldehyde](https://doi.org/10.1021/acsearthspacechem.3c00113),” *ACS Earth and Space Chemistry* **7**, 1739–1752 (2023).
- S. Panda and A. Anoop, “[Potential Prebiotic Pathways in Extraterrestrial Atmosphere](https://doi.org/10.1021/acsearthspacechem.3c00321),” *ACS Earth and Space Chemistry* **8**, 348–360 (2024).

### Related preprint

- S. Panda, S. Roy, M. Khatun and A. Anoop, “[HCN Dimers to HCN Tetramers: Computational Exploration of Binary Reactions](https://doi.org/10.26434/chemrxiv-2024-c5mzp),” *ChemRxiv* (2024), preprint.

## Connected research

[Explore HydroMol](https://hydromol.github.io/) · [Explore PyAR]({{ '/research/pyar/' | relative_url }}) · [Explore molecular aggregates and nanoclusters]({{ '/research/clusters/' | relative_url }}) · [Explore functional molecular discovery]({{ '/research/functional-materials/' | relative_url }}) · [Read the PyAR documentation](https://pyar.readthedocs.io/en/latest/) · [Browse the PyAR source code](https://github.com/anooplab/pyar) · [Return to the research overview]({{ '/research/' | relative_url }}) · [Visit AnoopLab](https://anooplab.github.io/)
