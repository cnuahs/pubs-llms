```
@article{cloherty2002action,
  title={Action potential heterogeneity assists frequency entrainment in the intact cardiac pacemaker},
  author={Shaun L. Cloherty and Nigel H. Lovell and Socrates Dokos and Branko G. Celler},
  journal={24th Annual Conference of the IEEE Engineering in Medicine and Biology Society and the Annual Fall Meeting of the Biomedical Engineering Society},
  year={2002},
  volume={1},
  pages={248-249},
   doi={10.1109/iembs.2002.1134476},
  url={https://ieeexplore.ieee.org/document/1134476}
}
```

---

# ACTION POTENTIAL HETEROGENEITY ASSISTS FREQUENCY ENTRAINMENT IN THE INTACT CARDIAC PACEMAKER

S. L. Cloherty \(^{1}\) , 
N. H. Lovell \(^{1}\) , 
S. Dokos \(^{1}\) and 
B. G. Celler \(^{2}\)

\(^{1}\) Graduate School of Biomedical Engineering, University of New South Wales, Sydney, Australia. \(^{2}\) Biomedical Systems Laboratory, School of Electrical Engineering and Telecommunications, University of New South Wales, Sydney, Australia.

Abstract—The role of cellular heterogeneity in frequency entrainment of the primary cardiac pacemaker has been investigated using an idealized two dimensional model of the rabbit sinoatrial node and surrounding atrial tissue. Simulation results are presented which support the hypothesis, that regional variation in action potential waveshape contributes to pacemaker synchronization in- vivo.

Keywords—action potential, frequency entrainment, mathematical model, sinoatrial node.

## I. INTRODUCTION

UNDER normal conditions, electrical activation of the mammalian heart is initiated in a small region of specialized pacemaker cells known as the sinoatrial node (SAN). Regional variation in cellular electrical properties is a widely accepted characteristic of the SAN [1], yet little attention has been given to its contribution to both normal and abnormal pacemaker function.

In a recent simulation study, we reported that heterogeneity in action potential (AP) waveshape assisted frequency entrainment of electrically coupled pacemaker cell pairs [2]. It was proposed that regional variation in AP characteristics within the intact SAN provides an important mechanism underlying pacemaker synchronization [2]. In this study we test this hypothesis using an idealized two dimensional model of the intact SAN and surrounding atrial tissue.

## II. METHODS

### A. The Membrane Ionic Models

The membrane ionic models employed for the SAN tissue were based on a generic model of a single rabbit SAN cell including formulations for 12 membrane currents [3]. To reproduce the heterogeneity in AP characteristics, the generic single cell ionic model parameters were fine- tuned via a customised non- linear optimisation routine [3], to fit AP recordings from known spatial locations within the SAN. Atrial tissue was simulated using the Earm and Noble model of a single rabbit atrial cell [4].

To facilitate the investigation of entrainment of both similar and dissimilar cell types while maintaining a constant cycle length (CL) disparity, the free running CL of the Central

and Peripheral cell models was perturbed as in our previous study [2].

### B. An Idealized SAN Model

The idealized two dimensional model of the intact cardiac pacemaker used in this study was formulated within the framework of the monodomain model described previously [5]. Briefly, an idealized two dimensional representation of the SAN was formulated on a rectilinear finite element mesh containing 16 elements \((4 \times 4)\) , each measuring \(0.5mm \times 0.5mm\) as shown in Fig. 1. The fibre angle was uniformly set to \(0^\circ\) , and the anisotropy ratio \((\sigma_f / \sigma_t)\) was uniformly set to 1.0 (isotropic tissue).

The problem domain was partitioned into three regions, denoted as Type1, Type2 and Atrial tissue according to the template superimposed on Fig. 1.

> **Image description.** A technical diagram illustrating a rectilinear finite element mesh used to model the idealized sinoatrial node (SAN) and surrounding atrial tissue. The image is presented within a square frame and features a central, solid black circular region surrounded by a ring of interconnected geometric elements.
>
> The central region, representing the SAN, is a solid black circle. Surrounding this core is an annular ring composed of numerous small, rectangular (rectilinear) elements. These elements are colored in various shades of gray and white, indicating different tissue types or properties within the model.
>
> Key visual elements and labels include:
>
> *   **Tissue Regions:** The central black area is the SAN. The surrounding ring is labeled "Atrial" and is composed of elements categorized as "Type1" and "Type2."
> *   **Mesh Structure:** The entire structure is a 2D discretization, where the continuous tissue is broken down into discrete, small, interconnected elements for computational simulation.
> *   **Annotations:**
>     *   A scale bar is located at the bottom left, indicating a length of "0.5mm."
>     *   A point label "B" is placed near the upper right edge of the atrial ring.
>     *   Partial text from the figure caption is visible at the top, beginning with "Fig. 1 The rectilinear finite element mesh defining the idealized SAN..."
>
> The overall composition is a highly structured, scientific visualization designed to represent a complex biological system (the heart's pacemaker) through a mathematical model.

<center>Fig. 1. The rectilinear finite element mesh defining the idealized SAN geometry. Superimposed on the finite element mesh is a template indicating the spatial relationship of areas designated as Type1 (dark gray), Type2 (light gray) and Atrial (unshaded) tissue. </center>

The region designated as Type1 tissue was simulated by either the unperturbed Central or perturbed Peripheral cell models while points in the surrounding Type2 region were simulated by either the unperturbed Peripheral or perturbed Central

cell models. In agreement with experimental observations, the CL disparity between Type1 and Type2 regions in all simulation was approximately \(18\%\) .

## III. RESULTS AND DISCUSSION

For each Type1:Type2 configuration, the components of the tissue conductivity tensor, \(\sigma_{f} = \sigma_{t} = G_{c} n S / m m\) were systematically varied and hence the critical tissue conductivity \((G_{c, \text{crit}})\) , defined as the minimum tissue conductivity required for \(1:1\) frequency entrainment, was determined. Fig. 2 shows the CL and membrane potential \((E_{m})\) observed at points \(A\) and \(B\) (see Fig. 1) in the Central:Peripheral configuration, for values of the tissue conductivity \((G_{c})\) both above (Fig. 2(a)) and below (Fig. 2(b)) the critical point. Note the beating behavior of the CL at \(A\) in (b), characteristic of unentrained states.

Table I summarizes the critical tissue conductivities for each Type1:Type2 configuration. The columns of Table I represent each of three possible methods of perturbing the intrinsic CL, denoted by symbolic suffixes \((\Delta = \bullet , \Delta\) or \(\bullet\) ). The rows denote the various Type1:Type2 configurations.

TABLE1 CRITICAL CONDUCTIVITY

| Configuration | $G_{c, \text{crit}}$ nS/mm | $\Delta = \bullet$ | $\Delta = \triangle$ | $\Delta = \bullet$ |
| :--- | :--- | :--- | :--- | :--- |
| Central:Peripheral | 6.35 | 6.35 | 6.35 | 6.35 |
| Central:Central$\Delta$ | 12.68 | 11.52 | 12.81 | 12.81 |
| Peripheral$\Delta$:Peripheral | 87.18 | 52.38 | 52.15 | 52.15 |

It is readily apparent, that the critical tissue conductivity for dissimilar cell types, such as in the Central:Peripheral configuration, is significantly less than that for cells with similar AP characteristics. This is in accordance with the hypothesis that heterogeneity in AP waveshape assists frequency entrainment in the intact SAN.

## IV. CONCLUSION

The idealized SAN model used in this study represents a biophysically detailed monodomain model of the intact cardiac pacemaker. The entrainment results presented support the hypothesis that heterogeneity in AP waveshape provides an important mechanism underlying pacemaker synchronization. As well as providing a basis for understanding entrainment of the SAN, we plan to use this model to investigate the efficient propagation of the AP from the SAN into the surrounding atria.

> **Image description.** A scientific figure consisting of two stacked line graphs, labeled (a) and (b), illustrating the relationship between Cycle Length (CL) and Membrane Potential ($E_m$) over time for two points, A and B. Both panels share identical axis scales and labels.
>
> **General Structure and Axes:**
> Both graphs plot time on the horizontal x-axis, ranging from 0 to 5 seconds. Each panel contains two y-axes:
> 1.  The upper y-axis measures CL (ms), ranging from 0 to 600 ms.
> 2.  The lower y-axis measures $E_m$ (mV), ranging from -80 to 40 mV.
> A legend in the upper right corner of each panel identifies the two data series as 'A' and 'B'.
>
> **Panel (a) Description:**
> Panel (a) displays data where the CL and $E_m$ are highly regular.
> *   **CL (Upper Graph):** Both lines A and B maintain a stable, high cycle length, consistently hovering near the 500-600 ms mark throughout the 5-second duration.
> *   **$E_m$ (Lower Graph):** Both lines A and B exhibit consistent, periodic action potential waveforms. Each waveform rises sharply from a baseline, peaks near 40 mV, and then decays back down, indicating a synchronized or entrained state.
>
> **Panel (b) Description:**
> Panel (b) displays data characterized by instability in the cycle length.
> *   **CL (Upper Graph):** The cycle length for line B remains relatively stable, similar to panel (a), around 500 ms. In contrast, the cycle length for line A shows significant variability, exhibiting rapid fluctuations (beating behavior) between approximately 300 ms and 500 ms over the 5-second period.
> *   **$E_m$ (Lower Graph):** Both lines A and B show action potential waveforms. While the general shape of the action potential is maintained, the timing and regularity of the peaks are less uniform compared to panel (a), reflecting the unentrained state of point A.

<center>Fig. 2. Observed cycle length (CL) and membrane potential \((E_{m})\) at points \(A\) and \(B\) in the Central:Peripheral configuration, for values of \(G_{c}\) above (a) and below (b) the critical point. Note the characteristic beating of the CL at \(A\) in (b), indicative of unentrained states. </center>

## REFERENCES

[1] I. Kodama and M. R. Boyett, "Regional differences in the electrical activity of the rabbit sinus node," "Pflugers Arch., vol. 404, pp. 214- 226, 1985.  
[2] S. L. Cloherty, N. H. Lovell, B. G. Celler, and S. Dokos, "Inhomogeneity of action potential waveshape assists frequency entrainment of cardiac pacemaker cells," IEEE Trans. Biomed. Eng., vol. 48, no. 10, pp. 1108- 1115, 2001.  
[3] S. Dokos, S. L. Cloherty, N. H. Lovell, and A. Zaza, "Cell-specific ionic models of cardiac pacemaker activity," in 23rd Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Istanbul, Turkey, 2001.  
[4] Y. E. Earm and D. Noble, "A model of the single atrial cell: relation between calcium current and calcium release," Proc. R. Soc. Lond., vol. 240, pp. 83- 96, 1990.  
[5] S. L. Cloherty, N. H. Lovell, S. Dokos, and B. G. Celler, "A 2D monodomain model of rabbit sinoatrial node," in 23rd Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Istanbul, Turkey, 2001.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
