---
layout: page
title: "Molecular aggregates, nanoclusters and nanoalloys"
eyebrow: Research theme · Clusters and aggregation
description: We use PyAR, quantum chemistry and machine-learned potentials to build, rank and interpret molecular aggregates, metallic nanoclusters and multicomponent nanoalloys.
permalink: /research/clusters/
research_theme: clusters
---

When atoms or molecules assemble, the resulting structure is not determined simply by adding together the properties of the individual components. The same collection of building blocks can form many geometrical arrangements, often separated by small energy differences. Adding a single atom or molecule may reorganise the entire assembly.

Our work asks: **how can these structural landscapes be explored systematically, and how do size, composition and collective interactions determine the properties of the resulting clusters?**

We use automated structure generation, quantum-chemical calculations and, increasingly, machine-learned potentials to study systems ranging from noncovalently bound molecular aggregates to metal nanoclusters and multicomponent nanoalloys.

## One search problem, several kinds of assembly

The word *cluster* covers chemically different systems.

In a molecular cluster, otherwise stable molecules are held together mainly by hydrogen bonding, electrostatic interactions and dispersion. Relative molecular orientations and cooperative interactions are central.

In an atomic or metallic cluster, the atoms form a new electronic structure. Bonding, spin state, relativistic effects and structural rearrangement may all depend strongly on the exact number of atoms.

A nanoalloy introduces another level of complexity. In addition to geometry, the search must consider composition and the placement of different elements—whether particular atoms favour the centre, surface or specific bonding environments.

These systems have different bonding physics, but they share a computational difficulty: **the number of possible structures grows rapidly as components are added.** Searching only structures suggested by chemical intuition can therefore miss unexpected low-energy arrangements.

## Building clusters recursively with PyAR

Our initial [tabu-search strategy for molecular aggregation](https://doi.org/10.1016/j.comptc.2017.03.040) reduced cluster construction to a sequence of relative-orientation problems. Multiple trial orientations are generated, while a Tabu list discourages repeated sampling of regions already explored. The candidates are locally optimised, similar results are removed and distinct low-energy structures are retained.

The same idea was developed into the [PyAR global optimiser for nanoclusters](https://doi.org/10.3389/fchem.2019.00644). An *n*-atom cluster is constructed from selected structures of the corresponding (*n*−1)-atom cluster by adding one atom in multiple orientations. The resulting structures are optimised and grouped using molecular representations, and a diverse set of minima is carried forward to the next growth step.

This bottom-up construction is particularly useful when we want to follow how structure and properties evolve with cluster size. It also extends naturally from pure clusters to binary and ternary nanoalloys.

The method does not mathematically prove that the absolute global minimum has been found. Its purpose is to explore the landscape efficiently, reproduce known structures where possible and discover chemically plausible alternatives for more accurate investigation.

## From molecular aggregation to metal clusters

The first implementation was tested on molecular aggregates of water, carbon dioxide and acetic acid. These examples covered strongly hydrogen-bonded, weakly bound and structurally less-explored systems. The search located established global minima as well as important low-lying structures.

The nanocluster implementation expanded this approach to pure Pd, Pt, Au and Al clusters; binary Ru–Pt and Au–Pt nanoalloys; and ternary Ag–Au–Pt clusters. The calculations reproduced major structural trends reported in earlier studies while following their evolution atom by atom.

They also exposed an important limitation: the predicted ordering of cluster structures can depend strongly on the electronic-structure method and spin state. A fast method may be useful for broad exploration without being sufficiently reliable for final energetic ranking.

## Why the lowest-energy structure is not always enough

A global minimum is a useful reference, but real cluster behaviour may involve several low-energy structures. Small clusters can be fluxional, and adsorption or changes in temperature, charge and environment may alter the relative populations of their isomers.

This became particularly clear in our work on platinum clusters.

The [study of subnanometre Pt clusters in the oxygen reduction reaction](https://doi.org/10.1002/jcc.26725) found a strong dependence of catalytic behaviour on atomicity. The exact number of Pt atoms affected the cluster geometry, its response to adsorbed intermediates and the calculated reaction energetics. An inverse size–activity relationship emerged within the investigated range, contrasting with simple trends expected from larger particles.

A subsequent [study of Pt₇](https://doi.org/10.1021/acs.jpca.1c09981) examined spin–orbit coupling and the statistical contribution of low-energy isomers. Relativistic effects changed the ordering of structural candidates, adsorption-induced rearrangements and details of the rate-determining pathway. Low-energy local minima made substantial contributions to the ensemble catalytic activity.

Together, these studies show that a subnanometre catalyst cannot be described only by its elemental composition and a single optimised geometry. Atomicity, spin, relativistic effects and the accessible structural ensemble may all affect its predicted activity.

## Composition and bonding in group 13 clusters

Boron, aluminium and gallium provide a useful series for examining how composition changes cluster structure and bonding. Although they belong to the same group of the periodic table, their cohesive tendencies, atomic sizes and orbital interactions differ substantially.

In the [BAl₄Mg cluster study](https://doi.org/10.3390/atoms9040089), PyAR searches were combined with chemically constructed candidates. The resulting low-energy structures included planar tetracoordinate and pentacoordinate boron atoms. This study also illustrated why automated exploration and chemical intuition should complement one another: neither provides a guarantee of complete structural coverage.

Our broader [study of B–Al–Ga nanoclusters and nanoalloys](https://doi.org/10.1039/D2CP05833B) considered pure, binary and ternary clusters containing up to twelve atoms. Before performing the structural exploration, we benchmarked electronic-structure methods against a dataset of small B–Al–Ga clusters.

The resulting structural map showed systematic differences across the elements. Boron and aluminium clusters favoured predominantly trigonal motifs, whereas gallium produced more rectangular faces. In mixed clusters, boron tended to occupy central positions and gallium was more frequently found towards the periphery, consistent with their different cohesive strengths. Mixing energies identified composition ranges in which alloy formation was energetically favourable relative to the chosen references.

We then examined the [bonding in representative six-atom B–Al–Ga clusters](https://doi.org/10.1016/j.poly.2025.117703). Topological, orbital and multicentre-bonding analyses revealed a progression from the stronger covalency and electron delocalisation of boron-rich clusters towards weaker orbital overlap in gallium-rich systems. The calculations identified multicentre σ and π bonding, aromatic characteristics and, in some structures, charge-concentration regions not centred on a nucleus.

This progression—from structural search to bonding analysis—helps explain why particular geometries and elemental arrangements are favoured rather than merely reporting their energies.

## From structural landscapes to catalyst candidates

The B–Al–Ga landscape was subsequently used to search for [platinum-free oxygen-reduction catalysts](https://doi.org/10.1039/D5CP03587B). Global structure searches and conceptual-DFT descriptors were used for initial screening. Shortlisted clusters were then examined through adsorption calculations, solvation corrections and ab initio molecular dynamics.

B₄Al₂ and B₂Al emerged as promising candidates within the computational model. The analysis suggested complementary roles for the constituent elements: boron promoted stability and electron uptake, aluminium increased reactivity, and gallium could tune electron donation.

This study represents a change in emphasis. Instead of asking only which clusters are stable, we begin with a broad structural landscape and progressively apply energetic, electronic, environmental and dynamical criteria to identify candidates for a specific function.

## The energy model is part of the search

A structure search is only as reliable as the energy model used to optimise and rank its candidates.

Our [benchmark study of small gold–thiolate clusters](https://doi.org/10.1021/acs.jpca.2c07561) compared density functionals and semiempirical composite methods for geometries, relative energies, ligand–core interactions and computational cost. Some methods failed to retain minima found by others, while the methods giving good geometries were not necessarily the best for relative energies.

This has a direct consequence for automated discovery. A rapid method may efficiently explore thousands of structures, but systematic errors in its potential-energy surface can remove important candidates before higher-level calculations begin. We therefore favour multilevel strategies: broad exploration with an affordable method, preservation of structural diversity and accurate refinement of a smaller candidate set.

## Machine-learned exploration of molecular clusters

The cost of quantum-chemical optimisation becomes increasingly restrictive as molecular aggregates grow. In our [recent work on noncovalent molecular clusters](https://doi.org/10.1002/jcc.70287), a pretrained neural-network potential, AIMNet2, was integrated with the Tabu-based PyAR search.

The approach was applied to clusters of water, ammonia, hydrogen peroxide, methanol and acetic acid with aggregation numbers up to ten. It enabled much broader exploration than would normally be practical if every trial structure required a conventional electronic-structure calculation.

AIMNet2 was trained mainly on organic molecules rather than explicitly on molecular clusters. Its use in this neighbouring domain is therefore both an opportunity and a test of transferability. Machine-learned potentials can accelerate sampling substantially, but their predictions must be checked against suitable quantum-chemical calculations, especially for unfamiliar bonding environments or unusual structures.

## Cooperativity in HCN and HNC clusters

Finding low-energy geometries is only the beginning. Molecular aggregates can display collective behaviour that is not captured by treating their interactions as independent molecular pairs.

Our [study of HCN and HNC clusters up to fifteen monomers](https://doi.org/10.1039/D5CP03273C) used the PyAR build-up procedure to locate spiral and dual-ring hydrogen-bonded networks. Energy decomposition separated electrostatic, dispersion and induction contributions, while many-body analysis quantified the non-additive interactions that emerge as the clusters grow.

Pairwise interactions remained dominant, but three- and four-body contributions accounted for as much as approximately 20% of the total interaction energy in the investigated clusters. HNC clusters exhibited stronger non-additive enhancement than their HCN counterparts.

The cooperative strengthening of the hydrogen-bond networks was also reflected in calculated vibrational spectra: the characteristic X–H stretching frequencies shifted progressively to lower wavenumbers with cluster size. These spectroscopic signatures connect structural models to quantities that may be relevant to laboratory and astrochemical observation.

This work demonstrates why aggregation is not simply the repeated addition of one identical interaction. The cluster develops collective properties that are absent from the isolated monomer and cannot always be reconstructed from the dimer alone.

## What the calculations do—and do not—establish

A low-energy structure found by an automated search is a candidate under a specified computational model. It is not proof that the same isolated structure is experimentally dominant.

Electronic energies do not by themselves determine finite-temperature populations. Entropy, kinetic trapping, charge, spin, ligands, solvent, surfaces and supporting materials may change the accessible structures.

A negative mixing energy indicates energetic preference relative to the selected reference clusters; it does not establish that a nanoalloy can be synthesised or retained under operating conditions.

Similarly, promising calculated catalytic activity is a basis for further investigation, not a substitute for experimental synthesis, structural characterisation and activity measurements.

Failure to locate a structure does not prove that it is absent from the potential-energy surface. Every search is constrained by its sampling strategy, energy model and computational budget. Automated algorithms, chemical intuition and independent searches remain complementary.

## Where this programme is going

We are interested in developing cluster exploration as a layered procedure:

- broad and diverse generation of candidate structures;
- inexpensive initial optimisation without premature loss of structural diversity;
- uncertainty-aware use of machine-learned potentials;
- refinement with validated electronic-structure methods;
- treatment of low-energy structural ensembles rather than only one minimum;
- explicit consideration of temperature, solvent, ligands and supports;
- analysis of bonding, cooperativity and spectroscopic observables;
- composition–structure–property relationships for nanoalloy design.

The objective is not merely to produce larger collections of cluster geometries. It is to determine how reliable structures and collective properties emerge as atoms or molecules assemble—and how that understanding can guide chemically testable predictions.

## Selected papers

### Foundations and search methodology

- S. Nandi, S. R. McAnanama-Brereton, M. P. Waller and A. Anoop, “[A tabu-search based strategy for modeling molecular aggregates and binary reactions](https://doi.org/10.1016/j.comptc.2017.03.040),” *Computational and Theoretical Chemistry* **1111**, 69–81 (2017).
- M. Khatun, R. S. Majumdar and A. Anoop, “[A Global Optimizer for Nanoclusters](https://doi.org/10.3389/fchem.2019.00644),” *Frontiers in Chemistry* **7**, 644 (2019).
- V. S. Thimmakondu *et al.*, “[Why an integrated approach between search algorithms and chemical intuition is necessary?](https://doi.org/10.1039/D2CP00315E),” *Physical Chemistry Chemical Physics* **24**, 11680–11686 (2022).

### Metallic clusters and nanoalloys

- M. Khatun *et al.*, “[BAl₄Mg−/0/+: Global Minima with a Planar Tetracoordinate or Hypercoordinate Boron Atom](https://doi.org/10.3390/atoms9040089),” *Atoms* **9**, 89 (2021).
- A. S. Nair, A. Anoop, R. Ahuja and B. Pathak, “[Role of atomicity in the oxygen reduction reaction activity of platinum sub nanometer clusters](https://doi.org/10.1002/jcc.26725),” *Journal of Computational Chemistry* **42**, 1944–1958 (2021).
- A. S. Nair, A. Anoop, R. Ahuja and B. Pathak, “[Relativistic Effects in Platinum Nanocluster Catalysis: A Statistical Ensemble-Based Analysis](https://doi.org/10.1021/acs.jpca.1c09981),” *The Journal of Physical Chemistry A* **126**, 1345–1359 (2022).
- M. Khatun, P. Sarkar, S. Panda, L. T. Sherpa and A. Anoop, “[Nanoclusters and nanoalloys of group 13 elements: benchmarking of methods and analysis of their structures and energies](https://doi.org/10.1039/D2CP05833B),” *Physical Chemistry Chemical Physics* **25**, 19986–20000 (2023).
- M. Khatun, S. Paul, S. Roy, S. Dey and A. Anoop, “[Performance of Density Functionals and Semiempirical 3c Methods for Small Gold–Thiolate Clusters](https://doi.org/10.1021/acs.jpca.2c07561),” *The Journal of Physical Chemistry A* **127**, 2242–2257 (2023).
- M. Khatun, P. Sarkar, S. Panda and A. Anoop, “[Bonding and stability in six-atom nanoclusters of boron, aluminum, and gallium](https://doi.org/10.1016/j.poly.2025.117703),” *Polyhedron* **281**, 117703 (2025).
- P. Sarkar, M. Khatun and A. Anoop, “[Computational discovery of high-performance B–Al–Ga nanoclusters for oxygen reduction reaction catalysis](https://doi.org/10.1039/D5CP03587B),” *Physical Chemistry Chemical Physics* **27**, 25014–25026 (2025).

### Molecular clusters

- S. Giri and A. Anoop, “[Exploring the Chemical Space of Noncovalent Molecular Clusters Using Automated Cluster Building Algorithm and Neural Network Potential](https://doi.org/10.1002/jcc.70287),” *Journal of Computational Chemistry* **46**, e70287 (2025).
- L. T. Sherpa, M. Khatun, S. Panda and A. Anoop, “[Cooperative many-body interactions and spectroscopic signatures in (HCN)n and (HNC)n clusters up to n = 15](https://doi.org/10.1039/D5CP03273C),” *Physical Chemistry Chemical Physics* **28**, 2227–2238 (2026).

## Connected research

[Explore PyAR]({{ '/research/pyar/' | relative_url }}) · [Automated reaction discovery]({{ '/research/reaction-discovery/' | relative_url }}) · [Explore functional molecular discovery]({{ '/research/functional-materials/' | relative_url }}) · [How collaborations shaped the programme](https://anooplab.github.io/research/collaborations/) · [Read the PyAR documentation](https://pyar.readthedocs.io/en/latest/) · [Browse the source code](https://github.com/anooplab/pyar) · [Return to the research overview]({{ '/research/' | relative_url }}) · [Visit AnoopLab](https://anooplab.github.io/)
