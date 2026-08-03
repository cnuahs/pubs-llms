```
@article{cloherty2001monodomain,
  title={A 2D monodomain model of rabbit sinoatrial node},
  author={Shaun L. Cloherty and Nigel H. Lovell and Socrates Dokos and Branko G. Celler},
  journal={23rd Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2001},
  volume={1},
  pages={44-47},
  doi={10.1109/iembs.2001.1018840},
  url={https://ieeexplore.ieee.org/document/1018840}
}
```

---

# A 2D MONODOMAIN MODEL OF RABBIT SINOATRIAL NODE

S. L. Cloherty<sup>1</sup>, 
N. H. Lovell<sup>1</sup>, 
S. Dokos<sup>1</sup> and 
B. G. Celler<sup>2</sup>

<sup>1</sup>Graduate School of Biomedical Engineering, University of New South Wales, Sydney, Australia. <sup>2</sup>Biomedical Systems Laboratory, School of Electrical Engineering and Telecommunications, University of New South Wales, Sydney, Australia.

Abstract - A biophysically detailed two dimensional monodomain model of the rabbit sinoatrial node and surrounding atrial tissue has been developed. The model incorporates the heterogeneity of action potential characteristics, the anisotropy of tissue conductance properties and the complex geometry of the sinoatrial node. Previously published ionic models of single sinoatrial node and atrial cardiac myocytes have been employed to describe the underlying action potential characteristics. Tissue geometry and conductance properties were derived by interpolation over a coarse finite element mesh. The monodomain equation was solved using a collocation- derived finite difference method. It is anticipated that the model will yield novel insight into the mechanisms underlying action potential propagation from the sinoatrial node into the atrium, migration of the primary pacemaker site in response to vagal stimulation and other complex phenomena. Qualitative simulation results of action potential propagation are in accord with experimental observations.

Keywords - sinoatrial node, monodomain model, collocation method

## I. INTRODUCTION

The pacemaker of the heart, the sinoatrial node, is a highly complex and spatially distributed structure. In the rabbit, the sinoatrial node consists of a large number of heterogeneous cells occupying an area in the wall of the right atrium extending from the superior to the inferior vena cava, roughly bounded by the crista terminalis of the atrial appendage and the left sinoatrial ring bundle on the septal side. The exact dimensions are difficult to quantify given that there is no clear demarcation between nodal and atrial tissue [1, 2]. A number of investigators have reported regional variations in action potential characteristics [3- 5]. Generally speaking, action potentials observed in the periphery of the sinoatrial node tend to exhibit an increase (hyperpolarization) in maximum diastolic potential (MDP), an increase in overshoot potential (OS) and a decrease in cycle length (CL) and action potential duration (APD) compared to action potentials observed nearer the center. Under normal conditions, activation is initiated in a small region ( \(\sim 0.1 \mathrm{mm}^2\) ) at the center of the sinoatrial node and propagates in a preferential direction roughly parallel to the crista terminalis [1]. Propagation of the action potential towards the interatrial septum is blocked [1], with activation of the interatrial septum being subsequent to propagation of the action potential around the top of this block zone. The site of action potential initiation, the primary pacemaker, is known to

migrate in response to a number of external influences including autonomic stimulation [6].

Clearly the sinoatrial node is a complex structure and a number of hypotheses have been proposed to account for its complexity and concomitant phenomena, namely; nonuniform propagation of the cardiac action potential (anisotropy), regional variation in action potential characteristics (heterogeneity), conduction block in the direction of the interatrial septum, and the spatial migration of the primary pacemaker site in response to various perturbations.

Conduction block in the direction of the interatrial septum may be attributed to a region of poor electrical interconnection [7] or alternatively a region of suppressed excitability [8], with the latter hypothesis gaining support in recent times. It has been hypothesized that the block zone plays an important protective role, shielding the sinoatrial node from reentry [8].

Kodama and Boyett [3] observed the regional variation in action potential characteristics in small electrically isolated tissue specimens ( \(\sim 0.3 \mathrm{mm}\) in diameter). They proposed a "gradient model" for the sinoatrial node in which the observed action potential heterogeneity is the result of a genuine transition in cell membrane electrophysiological characteristics. In contrast, Verheijck et al. [9] identified three morphologically different types of central nodal cells in addition to atrial myocytes in the rabbit sinoatrial node. After enzymatic isolation, these three cell types exhibited no significant variation in action potential characteristics. Verheijck et al. therefore hypothesized that the observed transition in action potential characteristics from the center to the periphery of the sinoatrial node is due to a gradual increase in atrial cell density toward the periphery, the so called "mosaic model" of the sinoatrial node.

Numerous multicellular models of the sinoatrial node of varying complexity have appeared in the past [10- 12]. Each of these models is based on a resistively coupled cellular network, and is constrained to a highly idealized two dimensional rectangular cartesian geometry. While the contribution these models have made to our understanding of sinoatrial node form and function is useful, novel insights into the phenomena mentioned above have been hampered due to lack of a suitable model encompassing all three key characteristics of the sinoatrial node region, namely; heterogeneity in action potential characteristics, anisotropy of tissue conductance properties and a complex geometry.

In this paper we describe a new monodomain

collocation- derived finite difference model of the sinoatrial node region incorporating these three key characteristics. This represents a significant step forward in modeling of the sinoatrial node and provides a unique tool for the investigation of the phenomena described above.

## II. METHODS

### A. Coordinate Systems

We limit the scope of our discussion to only two spatial dimensions and note that this is a reasonable first approximation given that the atrial wall in the region of the sinoatrial node is relatively thin, and in the rabbit, the sinoatrial node is known to occupy the entire thickness from epicardium to endocardium [1]. If desired, extension of the model to three spatial dimensions is relatively straightforward.

The model formulation is based on techniques described by Sands [13], we begin by defining three coordinate systems. The Reference Coordinate System, a rectangular Cartesian coordinate system defined at any convenient fixed point in physical space. Any point within the problem domain may be described by a set of coordinates \(X_{i}\) in the reference coordinate system. The Element Coordinate System, defined for each element in the finite element mesh (see below). Any point within an element may be described by a set of coordinates \(\xi_{i}\) in the local element coordinate system. The element coordinate system is generally nonorthogonal and curvilinear. The Material Coordinate System, defined at all points within the finite element mesh as an orthogonal coordinate system aligned with the tissue fibre direction. We use the term fibre direction despite the fact that the sinoatrial node does not exhibit a strict fibrous structure in the same manner as working myocardium. Nevertheless, cells of the sinoatrial node tend to be aligned with the crista terminalis [1, 2]. This alignment of cells gives rise to the anisotropic nature of the tissue and hence the need to describe the direction of preferential conduction - the fibre direction.

### B. The Monodomain Model

The basis of the model is the monodomain equation;

\[\nabla (\sigma \nabla E_{m}) = C_{m}\partial E_{m} / \partial t + I_{tot} \quad (1)\]

where \(\sigma\) is an effective conductivity tensor defined at each point relative to the local material coordinate system, \(C_{m}\) is the membrane capacitance, \(E_{m}\) is the transmembrane potential and \(I_{tot}\) is the sum of the transmembrane ionic currents. The underlying membrane equations \((I_{tot})\) are discussed below.

### C. The Collocation-Derived Finite Difference Method

The geometry of the tissue is described by means of a coarse finite element mesh in the reference coordinate system.

In general, the finite element mesh is an unstructured curvilinear quadrilateral mesh, facilitating adequate description of almost any geometry. A computational mesh of collocation points is derived by interpolation of the finite element geometry information and the solution to equation 1 is calculated exactly at those points. Unlike previous network models of the sinoatrial node [10- 12], the spacing between points need not be uniform. Material properties such as fibre direction and the effective conductivity tensor are also derived by interpolation over the finite element mesh. Thus description of anisotropic spatially varying tissue properties is relatively straightforward.

Evaluation of the left hand side of equation 1 at each point in the computational mesh is complicated by their nonuniform spatial relationship and the spatially varying tissue properties. A detailed description of the solution may be found in [13]. Briefly, the effective conductivity tensor \((\sigma)\) , defined in the local material coordinate system, is transformed into the local element coordinate system resulting in a true conductivity tensor. Spatial variation of the conductivity tensor is then taken into account using the geometry information derived from the finite element mesh. In this way, a set of coupling coefficients may be calculated once at each point for a given geometry and all that remains is to calculate the spatial derivative of the membrane potential at each point as the equations of the underlying ionic models are evolved. The left hand side of equation 1 is then given by the product of the coupling coefficients and the spatial derivatives of the membrane potential.

### D. The Underlying Ionic Models

We have employed the ionic model of a single rabbit sinoatrial node cell previously developed by Dokos et al. [14] with two modifications. Briefly, the delayed rectifier potassium current \(i_{K}\) was replaced by a new formulation consisting of separate rapid and slow components, \(i_{K,e}\) and \(i_{K,s}\) respectively. The reversal potential of both the L and T type calcium currents, \(i_{CaL}\) and \(i_{CaT}\) , was set to a constant value of \(- 40 \mathrm{mV}\) . A set of 38 model parameters was identified which determined the action potential characteristics of the model and appropriate values were chosen to accurately reproduce the central- peripheral variation in action potential characteristics observed by Kodama et al. [15]. A detailed description of the changes to the published model appears in [16]. Atrial tissue was modeled using the ionic model of a single rabbit atrial cell developed by Earm and Noble [17].

### E. Computational Methods

Definition of the finite element mesh, interpolation at the collocation points and calculation of the finite- difference coupling coefficients was performed by a Python [18] front- end to the simulation code. The equations of the underlying ionic models were implemented in GNU C and evolved using the CVODE [19] solver for stiff systems of ordinary

differential equations, with an error tolerance of \(1.0 \times 10^{3}\) . Simulations were performed in double precision and results saved to disk in IEEE double precision binary floating point format. Subsequent analysis was performed using Matlab (The Mathworks Inc., MA, USA). In order to reduce computation time and resource requirements for large scale simulations, we have developed a distributed message passing implementation based on the MPICH [20] implementation of the Message Passing Interface Standard.

## III. RESULTS AND DISCUSSION

To demonstrate some of the features of the model, we have performed initial simulations on a representative, highly idealized geometry. Further work is currently in progress to accurately model the geometry of the sinoatrial node region and select realistic values of the effective conductivities.

> **Image description.** This image is a scientific visualization, Figure 1, consisting of two panels, (a) and (b), which illustrate the results of a simulation of cardiac tissue activity.
>
> Panel (a) is a contour plot, or isochrone map, showing activation times across a two-dimensional region.
> *   **Axes:** Both the horizontal (x) and vertical (y) axes are labeled "mm" and range from 0.0 to 1.4.
> *   **Content:** The plot features a series of concentric, curved lines (isochrones) that represent the time it takes for the tissue to activate. The contours are denser near the center, indicating faster activation in that region.
> *   **Markers:** Two specific locations are marked with crosses: a central cross labeled "Central" is located near the center of the plot (approximately 0.7 mm, 0.7 mm), and a peripheral cross labeled "Peripheral" is located near the upper right corner (approximately 1.2 mm, 1.2 mm).
>
> Panel (b) is a line graph showing the action potentials (voltage over time) at the locations indicated in Panel (a).
> *   **Axes:** The horizontal axis is labeled "ms" (milliseconds) and ranges from 0 to 500. The vertical axis is labeled "mV" (millivolts) and ranges from -100 to 50.
> *   **Traces:** Three distinct voltage traces are plotted:
>     *   **Peripheral:** This trace shows the highest peak voltage, rising sharply to approximately 35 mV before decaying.
>     *   **Central:** This trace shows a slightly lower peak voltage than the peripheral trace, reaching approximately 25 mV, and exhibits a similar shape.
>     *   **Atrial:** This trace is the lowest and broadest, peaking at a voltage around 10-15 mV.
>
> The overall figure demonstrates the difference in activation times and resulting action potential characteristics between the central and peripheral regions of the simulated cardiac tissue.

<center>Fig. 1. (a) Activation times after 5 s of simulated activity on a representative, highly idealized geometry with a uniform fibre angle of \(30^{\circ}\) . Isochrones are spaced at intervals of approximately 5 ms. (b) Action potentials from central and peripheral cell models at the locations indicated by crosses in (a). The atrial cell action potential is from the upper right hand corner of the collocation mesh (not shown in (a)). Action potentials are aligned at the time of maximum upstroke velocity. </center>

Fig. 1 illustrates the ability of the model to simulate the heterogeneity and anisotropy characteristics required of a two dimensional sinoatrial node model. A cartesian finite element mesh containing 9 square elements spanning a region \(2.1 \mathrm{mm} \times 2.1 \mathrm{mm}\) was constructed, with a uniform fibre direction of \(30^{\circ}\) (clockwise from the vertical axis), and a ratio of effective conductances (longitudinal:transverse) of 3:1. A single central sinoatrial node cell was placed at the center of the mesh, the edges of the mesh were modeled as atrial tissue and all other points were modeled as peripheral sinoatrial node cells. Fig. 1(a) shows the activation times in the central portion of the mesh (1.4 mm x 1.4 mm) after five seconds of simulated activity. Isochrones are spaced at intervals of approximately five milliseconds. Note the elliptic activation pattern aligned with the fibre direction, qualitatively similar to that observed experimentally. Fig. 1(b) shows representative action potentials from central, peripheral and atrial cell models from the same simulation shown in Fig 1(a).

A second simulation, again on a cartesian finite element mesh containing 9 square elements spanning a region \(2.1 \mathrm{mm} \times 2.1 \mathrm{mm}\) was performed. This time, a region of conduction block was placed 1/3 of the way in from the right hand edge, extending 2/3 of the way up from the lower edge. This block zone was modelled as a complete block zone of zero width with an imposed Neumann (zero- flux) boundary condition. A single central sinoatrial node cell was placed half way between the block zone and the left hand edge representing the crista terminalis. The effective conductance increased linearly in all directions from this point while maintaining a constant ratio of effective conductances of 3:1 (longitudinal:transverse). Again, the edges of the mesh were modeled as atrial tissue and all other nodes were modeled as peripheral sinoatrial node cells. Fig. 2 shows the activation

> **Image description.** A technical contour plot, specifically an isochrone map, illustrating activation times on a two-dimensional, highly idealized geometry. The image is presented on a white background and uses dark, curved lines to represent the progression of activation.
>
> The plot utilizes a Cartesian coordinate system with both the horizontal (x) and vertical (y) axes labeled "mm." Both axes range from 0.0 to 1.4 mm.
>
> The primary visual element is a series of concentric, curved contour lines (isochrones) that radiate outward from a central point. These lines represent the time taken for electrical activation to reach various points in the tissue. The pattern shows a wave of activation originating from the center and spreading toward the edges.
>
> Key annotations and features include:
> *   **Central Point:** A small star or cross symbol is located near the center of the plot, and the text "Central" is placed immediately below it, indicating the origin of the activation wave.
> *   **Block Zone:** A large, irregularly shaped region is labeled "Block Zone" in the upper right quadrant of the plot. This area is characterized by the contour lines being pushed away or forming a boundary, suggesting a region where activation is significantly delayed or prevented.
> *   **Caption:** A partial caption is visible at the bottom left, reading: "Fig. 2. Activation times on a representative, highly idealized".
>
> The overall visual representation is a simulation result demonstrating how activation propagates through a heterogeneous tissue model, showing a clear difference between the central activation point and the peripheral "Block Zone."

<center>Fig. 2. Activation times on a representative, highly idealized geometry with a uniform fibre angle of \(0^{\circ}\) and region of conduction block (Block Zone). Isochrones are spaced at intervals of approximately 5 ms. Note the elliptical activation pattern roughly aligned with the left hand edge representing the crista terminalis and the propagation of the activation around the top of the block zone towards the interatrial septum (right hand side). Note also the increased conduction velocity to the right of the block zone, corresponding to the area of highest effective conductance. The cross marks the arbitrary location of a "central" sinoatrial node cell model (see text). </center>

times in the central portion of the mesh after five seconds of simulated activity. Isochrones are spaced at intervals of roughly five milliseconds. From Fig. 2, it can be seen that even this simple configuration exhibits a number of characteristics observed experimentally; notably the elliptical activation pattern roughly aligned with the left hand edge representing the crista terminalis and propagation of the activation front around the top of the block zone. It is also interesting to note the increase in conduction velocity, indicated by an increase in isochrone spacing, to the right of the block zone, corresponding to the region of highest effective conductivity.

## IV. CONCLUSION

We have described a new two dimensional monodomain model of the rabbit sinoatrial node region, incorporating heterogeneity of electrical activity, anisotropy of tissue properties and the complex geometry of the sinoatrial node region. It is anticipated that this new model will provide insight into the relative merits of the "gradient" and "mosaic" models of sinoatrial node proposed to explain the observed heterogeneity in action potential characteristics. The model is also well equipped to improve our understanding of the mechanisms underlying action potential propagation into the atrium, and migration of the primary pacemaker site in response to vagal stimulation.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
