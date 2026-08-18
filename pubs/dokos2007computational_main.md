```
@article{dokos2007computational,
  title={Computational Model of Atrial Electrical Activation and Propagation},
  author={Socrates Dokos and Shaun L. Cloherty and Nigel H. Lovell},
  journal={29th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2007},
  pages={908-911},
  doi={10.1109/iembs.2007.4352438},
  url={https://ieeexplore.ieee.org/document/4352438/}
}
```

---

# Computational Model of Atrial Electrical Activation and Propagation

Socrates Dokos, Shaun L. Cloherty, Member, IEEE, and Nigel H. Lovell, Senior Member, IEEE

Abstract—We have developed a finite- element surface model of human atria, in order to study normal and abnormal patterns of atrial activation. To characterize electrical activity in both atrial muscle and cardiac pacemaker regions, Fitzhugh- Nagumo- type equations were employed. Model equations were tested using a simplified geometry containing major topological features of both atria. The model is able to generate spontaneous activation of electrical impulses within the sinoatrial node which propagate across the atria. The model can be used as a basis for investigating mechanisms underlying normal and abnormal atrial rhythms, including re- entrant activation by an ectopic focus.

## I. INTRODUCTION

I. nitation of the mammalian heartbeat normally occurs in the specialised pacemaker cells of the sinoatrial node (SAN), located in the right atrial wall of the heart. From there, the electrical impulse spreads across the surface of the atria before reaching the ventricles. Disruptions to atrial excitation and/or propagation represent the most common forms of arrhythmias encountered clinically. In particular, atrial fibrillation represents a significant risk factor for stroke [1].

Beginning in 1968 from the influential work of Moe [2], computer models have proven invaluable in the understanding of ionic mechanisms underlying normal and abnormal atrial rhythms. Despite this, accurate ionic reconstructions of SAN and atrial myocytes which incorporate electrical remodelling and spatial heterogeneity of ion channels are still to be developed [3]. In this study, we describe a preliminary finite-element model of human atria consisting of active SAN and atrial regions, useful for the study of mechanisms of atrial fibrillation.

## II. METHODS

### A. Cellular Excitation

Equations employed for SAN and atrial activation were

Manuscript received April 16, 2009. This work was supported in part by an Australian Research Council Discovery Project Grant DP0667106. S. Dokos is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, 2052, Australia (email: s.dokos@ unsw.edu.au). S. L. Cloherty is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, 2052, Australia (email: s.cloherty@ gsbme.unsw.edu.au). N. H. Lovell is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, 2052, Australia. He is also with, the National Information and Communications Technology Australia (NICTA), Eveleigh NSW 1430, Australia (e- mail: n.lovell@unsw.edu.au).

Fitzugh- Nagumo type, suitably scaled in both time and membrane potential domains. Advantages of such simplified models over more realistic ionic models lie principally in computational efficiency. The equations employed for the SAN region were:

\[\begin{array}{l}\frac{\partial u}{\partial t} = \nabla (\delta \bar{u}) + kc(u - B)\left(\frac{(u - B)}{A} -a\right)\left(1 - \frac{(u - B)}{A}\right) - kc_3v\\ \displaystyle \frac{\partial v}{\partial t} = kc\left(\frac{(u - B)}{A} -dv - b\right) \end{array} \quad (2)\]

where \(u\) denotes the membrane potential and \(v\) governs cellular refractoriness; \(\sigma\) denotes the tissue conductance, nominally set to a value of \(0.001 \mathrm{~S / m}\) , corresponding to activation of both atria within \(250 \mathrm{~ms}\) . Remaining parameters are given in table 1.

In the atrial region, the modified Rogers- McCulloch formulation [4] was used, also suitably scaled:

\[\begin{array}{l}\frac{\partial u}{\partial t} = \nabla (\delta \bar{u}) + kc(u - B)\left(\frac{(u - B)}{A} -a\right)\left(1 - \frac{(u - B)}{A}\right) - kc_3u - B\\ \displaystyle \frac{\partial v}{\partial t} = kc\left(\frac{(u - B)}{A} -dv - b\right) \end{array} \quad (3)\]

with parameter values also given in table I. Initial conditions for (1)- (4) are given in table II, with representative action potential waveforms (ignoring spatial derivatives) shown in figure 1. For a 2D surface, the spatial derivatives in (1) and (3) are given in terms of tangential derivatives of the surface.

> **Image description.** A line graph titled "AP Waves" displays the action potential (AP) waveforms for two different regions: the Sinoatrial Node (SAN) and the Atrial tissue. The graph plots electrical potential in millivolts (mV) against time in milliseconds (ms).
>
> The vertical Y-axis is labeled "mV" and ranges from -100 to 40, with major tick marks every 20 units. The horizontal X-axis is labeled "time (ms)" and ranges from 0 to 1500, with major tick marks every 500 units.
>
> Two distinct data series are plotted:
> 1.  **SAN (Sinoatrial Node):** Represented by a solid line, the SAN waveform shows a rapid and high-amplitude depolarization. The peaks consistently reach approximately 20 to 30 mV. The pattern of electrical activity repeats at approximately 500 ms and 1000 ms.
> 2.  **Atrial:** Represented by a dashed line, the Atrial waveform shows a slower and lower-amplitude depolarization compared to the SAN. The peaks consistently reach approximately 10 to 15 mV. This pattern also repeats at approximately 500 ms and 1000 ms.
>
> The legend, located in the upper right corner, clearly identifies the solid line as "SAN" and the dashed line as "Atrial."
>
> Below the graph, the figure caption reads: "Fig. 1. Action Potential waves for both SAN pacemaker and atrial". The text "surface." is visible at the top left, appearing to be the end of a sentence from the surrounding document. The overall visual pattern demonstrates that the SAN generates significantly higher voltage action potentials than the surrounding atrial tissue.

<center>Fig. 1. Action Potential waveshapes for both SAN pacemaker and atrial models, obtained from solving the ODE systems (1)-(4), setting all spatial derivatives to zero. An additional stimulus was applied to the right hand side of (3) to elicit the atrial action potential. </center>

### B. Simplified Geometry

In order to solve the cellular excitation equations, we tested the model using a highly simplified geometry of the atria consisting of two joined spherical surfaces, each of diameter \(40\mathrm{mm}\) , as shown in figure 2. The geometry included openings in both atria representing the major blood vessels and valves. The SAN region was modeled as a small circular disk embedded in the right atrium near the opening representing the superior vena cava. The entire system of PDEs (1) - (4) was solved using COMSOL Multiphysics finite- element software'.

> **Image description.** A technical diagram illustrating the simplified geometry of the atria, consisting of two joined spherical surfaces, as used in a computational model. The image is presented in two stacked panels, showing different views of the same anatomical structure.
>
> The overall geometry is rendered in a light blue or lavender color, representing the atrial tissue. The structure features several dark blue or black circular openings on its surface, which represent major blood vessels and valves.
>
> **Top Panel (Posterior View):**
> This panel shows the two interconnected spheres. On the right sphere, a small, bright magenta circular disk is visible, representing the SAN (Sinoatrial Node) region. Two labels are present:
> *   "SVC" points to an opening near the magenta disk, representing the superior vena cava.
> *   "SAN" points directly to the small magenta disk.
>
> **Bottom Panel:**
> This panel shows the same two interconnected spheres from a different perspective. On the left sphere, a small, bright magenta circular disk is visible. A single label is present:
> *   "SVC" points to an opening near this magenta disk, indicating the location of the superior vena cava opening relative to the SAN region in this view.
>
> The visual style is a 3D rendering, typical of scientific or engineering simulations, designed to represent the complex, simplified geometry used for solving cellular excitation equations in cardiac modeling. The magenta disk serves as a focal point, highlighting the specific location of the SAN region within the atrial structure.

<center>Fig. 2. Simplified atrial geometry employed. The SAN region is depicted as a small disk near the opening of the superior vena cava (SVC) on the right atrial surface. Top panel represents a posterior view. </center>

## III. RESULTS

Simulations were undertaken on the simplified atrial geometry over an interval of 2 seconds, corresponding to around 3 SAN depolarizations. Results are illustrated in figure 3, where it can be seen that a wave of depolarization spreads from the SAN disk to cover both atrial surfaces in an interval within \(250\mathrm{ms}\) . This pattern of activation remained stable, with periodic excitation of the atria by the SAN.

Openings in the atrial surface may provide a possible anchor for re- entrant activity. To investigate such a mode of propagation, an ectopic stimulus was introduced onto the left atrial surface at \(t = 550\mathrm{ms}\) , located midway between the lower pulmonary veins. The resulting pattern of activation, illustrated in figure 4, reveals a re- entrant pattern of excitation around one of the openings corresponding to the lower left pulmonary vein, as well as around the SVC in the

TABLEI MODEL PARAMETERS

| Parameter | Atrial Value | SAN Value |
| :--- | :--- | :--- |
| a | 0.13 | -1 |
| b | 0 mV | -0.29 mV |
| c1 | 0.26 | 1.9 |
| c2 | 0.1 | 1 mV |
| d | 1 | 0 |
| e | 0.013 | 0.06 |
| A | 140 mV | 35 mV |
| B | -85 mV | -30 mV |
| k | 3 ms⁻¹ | 3 ms⁻¹ |
| $\sigma$ | 0.001 S/m | 0.001 S/m |

TABLE II INITIAL VALUES

| Variable | Atrial Value | SAN Value |
| :--- | :--- | :--- |
| u | -85 mV | -60 mV |
| v | 0 | 0 |

right atrium. These reentrant patterns are maintained, even in the presence of the periodic SAN stimulus. The period of reentry was half that of the SAN cycle. At each SAN subsequent SAN activation, the wavefront from the SAN merges with the right atrial wavefront, sustaining the reentrant pathway.

> **Image description.** A technical visualization consisting of three stacked panels (A, B, and C) illustrating the simulation of Sinoatrial Node (SAN) atrial activation and propagation within a simplified two-chamber geometry. The image uses color gradients to represent the state of activation across the two joined spherical surfaces, which represent the atria.
>
> The overall structure consists of two large, interconnected, roughly spherical shapes. The color scheme indicates a progression of activation: deep blue represents a low or resting state, while orange and red represent areas of depolarization or high activation.
>
> The progression across the three panels shows the spread of the activation wave over time:
>
> *   **Panel A:** Both spherical atria are predominantly colored deep blue, indicating minimal activation. A small, localized area of orange/red activation is visible near the junction or opening on the right-hand sphere, representing the initial stimulus from the SAN region.
> *   **Panel B:** The activation has begun to spread. The right sphere shows a significantly larger area of orange and red activation, particularly concentrated near the opening. The left sphere, while still mostly blue, shows the initial encroachment of orange/red activation towards the central junction.
> *   **Panel C:** The activation wave has spread widely across both atria. Both the left and right spheres display extensive areas of red and orange, indicating that the depolarization has successfully propagated and covered both atrial surfaces.
>
> The figure is labeled "Fig. 3." and includes the caption: "Fig. 3. Simulations of SAN atrial activation and propagation." The visual evidence demonstrates the rapid spread of the activation wave from the initial point of stimulus (the SAN) to cover the entire simplified atrial geometry.

<center>Fig. 3. Simulations of SAN atrial activation and propagation at \(t = 280\mathrm{ms}\) (A), \(380\mathrm{ms}\) (B) and \(480\mathrm{ms}\) (C). </center>

To examine whether the re-entrant pattern can in fact be elicited and sustained in the absence of an anatomical substrate (in this case, the opening to the pulmonary vein), the above simulation was repeated using a modified atrial geometry in which in the four pulmonary openings were absent. Results are shown in figure 5, where it is evident that re-entrant activation cannot be sustained in the left atrium, whereas re-entry is maintained in the right atrium around the opening to the SVC. This suggests that re-entrant activity is in fact facilitated by specific anatomical structures within the atria.

> **Image description.** A scientific figure consisting of two main sections, Figure 4 and Figure 5, which display simulated cardiac activation patterns (re-entry) within a complex, multi-lobed anatomical geometry, likely representing the human atria. Both figures are composed of four vertically stacked panels (A, B, C, D) each showing a progression of activation over time, represented by a gradient of colors (red, orange, yellow, green, and blue).
>
> **Figure 4 (Left Panel):**
> This figure illustrates the stable re-entrant patterns of atrial activation around the openings of the lower left pulmonary vein and the Superior Vena Cava (SVC).
> *   **Caption:** "Fig. 4. Stable re-entrant patterns of atrial activation around the openings of the lower left pulmonary vein and SVC, as elicited by a single one-off ectopic stimulus delivered at $t = 550$ ms at the location depicted by the arrow in panel A, midway between the lower pulmonary veins. The pattern of re-entrant activation is shown at $t = 1400$ ms (A), $1600$ ms (B), $1800$ ms (C) and $2000$ ms (D). The period of the re-entrant loop was twice the SAN rate, and was able to be maintained throughout the presence of periodic SAN excitation."
> *   **Visual Progression:**
>     *   **Panel A:** Shows the initial activation pattern, with a distinct arrow pointing to the "Ectopic stimulus site" located midway between the lower pulmonary veins.
>     *   **Panel B, C, and D:** Show the subsequent evolution of the activation pattern, with the colors spreading and forming a complex, looping structure, indicating the re-entrant activity.
> *   **Labels:** The label "Ectopic stimulus site" is present in Panel A. The label "SAN" (Sinoatrial Node) is visible in Panel D.
>
> **Figure 5 (Right Panel):**
> This figure illustrates the re-entrant pattern of atrial activation in a modified geometry where the pulmonary vein openings are absent.
> *   **Caption:** "Fig. 5. Stable re-entrant pattern of atrial activation in the absence of pulmonary vein openings, elicited by a single ectopic stimulus at $t = 550$ ms (A), $1600$ ms (B), $1700$ ms (C) and $1900$ ms (D). The pattern of re-entrant activation is shown at $t = 1400$ ms (A), $1600$ ms (B), $1800$ ms (C) and $1900$ ms (D). Re-entry was abolished in the left atrium, while re-entry was maintained in the right atrium around the SVC and SAN regions."
> *   **Visual Progression:** Similar to Figure 4, the panels (A-D) show the temporal progression of the activation pattern. However, the overall shape and distribution of the colored activation wavefront appear different from Figure 4, reflecting the change in anatomical structure (absence of pulmonary vein openings).
> *   **Labels:** No specific labels are present within the panels, but the caption references the "SVC" and "SAN" regions.
>
> Both figures use a color map to represent the state of electrical activation, with warmer colors (red/orange) likely indicating the peak or most recent activation, and cooler colors (blue) indicating less recent or inactive areas. The overall visual style is that of a computational fluid dynamics or electrophysiology simulation.

<center>Fig. 4. Stable re-entrant patterns of atrial activation around the openings of the lower left pulmonary vein and SVC, as elicited by a single one-off ectopic stimulus delivered at \(t = 550\) ms at the location depicted by the arrow in panel A, midway between the lower pulmonary veins. The pattern of re-entrant activation is shown at \(t = 1400\) ms (A), \(1600\) ms (B), \(1800\) ms (C) and \(2000\) ms (D). The period of the re-entrant loop was twice the SAN rate, and was able to be maintained throughout the presence of periodic SAN excitation. </center>

## IV. DISCUSSION

Development of realistic anatomical models of human atria is important in computer simulations of normal and abnormal atrial rhythms [5]. As the results of this study show, atrial morphology can be important in the maintenance of re-entrant arrhythmias. The simplified geometrical model incorporated is this study is similar in

structure to previous published models of atrial activation [6, 7]. Unlike these models however, the model of this study incorporates an active SAN region electrotonically coupled to the surrounding atrial myocardium. Results of this study suggest that the SAN and atrial models employed are able to elicit stable patterns of re- entrant activity, at rates higher than the basal SAN rhythm, with openings in the atrial surface acting as anchors for re- entry.

It is known that re- entrant activation can only be elicited and sustained if the cellular refractory period is sufficiently low. In this study, the width of the atrial action potential (and therefore refractory period), is of the order of \(100\mathrm{ms}\) . This period could easily be adjusted via the atrial \(k\) parameter (table I). We found that we could not elicit sustained re- entry on our simplified geometry if the refractory period was much higher than this (i.e. \(k < 3\mathrm{ms}\) ). In reality, refractory period is known to decrease with increased re- entrant pacing, helping to sustain the re- entrant waveform [8]. Therefore, realistic models of atrial fibrillation would need to incorporate some degree of electrical remodeling. This study represents the first stage toward the development of an accurate computer model of atrial fibrillation, incorporating realistic anatomical structure as well as electrical models of both SAN and atrial myocytes.

> **Image description.** A technical 3D visualization of a complex biological model, specifically a finite element mesh representing the geometric surface of human atria.
>
> The central element is a dark gray, three-dimensional structure that accurately depicts the anatomical shape of the upper chambers of the heart (the atria). This structure is rendered as a triangulated mesh, meaning its surface is composed of numerous interconnected triangles, which is a common method in computational modeling (finite element analysis). The mesh lines are clearly visible as thin white lines against the dark gray surface, highlighting the complexity and detail of the model.
>
> The model is presented within a defined three-dimensional coordinate system, indicating its dimensions in millimeters. The axes are labeled with numerical values, providing a scale for the structure:
> *   The horizontal axes (X and Y) show markings ranging from approximately -200 to 250.
> *   The vertical axis (Z) also shows markings ranging from approximately -200 to 250.
>
> Below the image, the figure caption is visible and reads: "Fig. 6. Proposed geometric surface model of human atria, with triangulated mesh consisting of 90,000 elements. Dimensions shown are in millimeters."
>
> The overall visual impression is that of a highly detailed, scientific computer model used for simulating biological processes, such as electrical activity in the heart.

<center>Fig. 6. Proposed geometric surface model of human atria, with triangulated mesh consisting of 90,000 elements. Dimensions shown are in millimeters. </center>

## V. FUTURE WORK

Thorax slice images from the male Visible Human \(^2\) data set have already been used to digitize atrial anatomy, including major blood vessels as well as Bachmann's Bundle connecting the two atria. Custom software has also been written to triangulate the data points, with the resulting finite- element mesh illustrated in figure 6. The model is a 2D surface embedded in 3D space. Owing to the complex nature of this geometry, the surface needs to be smoothed via a piecewise Bezier patch representation for efficient solving of the activation equations by our finite element software. In this study, preliminary simulations were carried out instead using a simplified surface model of the atria, as described in the text. In future however, we intend to incorporate the anatomically realistic model of human atria described above.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
