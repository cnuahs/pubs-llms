```
@article{cloherty2005qualitative,
  title={Qualitative Support for the Gradient Model of Cardiac Pacemaker Heterogeneity},
  author={Shaun L. Cloherty and Socrates Dokos and Nigel H. Lovell},
  journal={27th Annual Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2005},
  pages={133-136},
  doi={10.1109/iembs.2005.1616360},
  url={https://ieeexplore.ieee.org/document/1616360}
}
```

---

# Qualitative Support for the Gradient Model of Cardiac Pacemaker Heterogeneity

Shaun L. Cloherty, Socrates Dokos and Nigel H. Lovell  Graduate School of Biomedical Engineering  University of New South Wales  Sydney, Australia

Abstract—In this study, we investigate the role of sinoatrial node (SAN) cellular heterogeneity in normal cardiac pacemaker function. Using detailed ionic models of electrical activity in SAN and atrial myocytes, we have formulated a number of models of SAN heterogeneity based on discrete- region (in which central and peripheral SAN type cell are separated into discrete regions), gradient and mosaic models of SAN organisation. Simulations of each of the different models were performed in one and two dimensions in the presence of both uniform and linearly increasing conductivity profiles.

Simulation results suggest that the gradient model, in which cells display a smooth variation in membrane properties from the center to the periphery of the SAN, best reproduces action potential waveshapes and a site of earliest activation consistent with experimental observations in the intact SAN. We therefore propose that the gradient model of SAN heterogeneity represents the most plausible model of SAN organisation.

## I. INTRODUCTION

In mammalian hearts, the heartbeat is initiated in the wall of the right atrium, in a region of specialized pacemaker cells known as the sinoatrial node (SAN). The SAN exhibits considerable cellular heterogeneity and is subject to complex electronic interactions with the surrounding atrial tissue. Despite continued attention over the last half century, a number of aspects of normal pacemaker function remain unclear. For example, the functional organisation of the SAN remains a contentious issue, with a number of different models being proposed in the literature. It is also uncertain how the SAN successfully excites the surrounding atrial tissue while remaining protected from its seemingly overwhelming electronic load.

In this paper, we attempt to identify the most plausible model of SAN organisation. We employ a biophysically detailed ionic model of a single SAN myocyte, able to exactly reproduce action potential (AP) recordings from both the center and periphery of the rabbit SAN. With appropriate parameters, this model is also able to produce AP waveshapes characteristic of the intermediate region between the center and the periphery of the SAN [1]. Several models of the SAN are formulated in one and two dimensions, based on three proposed models of SAN heterogeneity: 1) the discrete- region model, in which the SAN consists of a compact central region surrounded by a region of transitional pacemaker cells, 2) the gradient model, in which cells of the SAN exhibit a smooth variation in properties from the center to the periphery of the SAN, and 3) the mosaic model, in which SAN and atrial cells are scattered throughout the SAN region with the proportion of atrial cells increasing towards the periphery.

region with the proportion of atrial cells increasing towards the periphery.

Results are presented from a number of simulations aimed at assessing the relative merits of each of the proposed models. In brief, the gradient model was best able to reproduce AP waveshapes and a site of earliest activation consistent with experimental observations, providing support for the gradient model as the most plausible model of SAN organisation.

## II. METHODS

### A. A 1D Model of the Sinoatrial Node

The SAN and adjoining atrial tissue was approximated as a highly idealized 1D cable, consisting of a region of SAN tissue coupled to a region of atrial tissue as illustrated schematically in Fig. 1(a). The length of the SAN region was set to \(1.5\mathrm{mm}\) , roughly in agreement with the distance from the center to the periphery of the SAN perpendicular to and in the direction of the crista terminalis (CT) in the rabbit [2][3]. The length of the atrial tissue region was also set to \(1.5\mathrm{mm}\) . While considerably shorter than the spatial scale of the right atrium in the rabbit, this length corresponds to roughly 1.5 space constants and was sufficient to approximate the electronic load imposed on the SAN by the atrial tissue.

### B. A 2D Model of the Sinoatrial Node

In 2D, the SAN was modelled in an idealized sense as a circular region \(3.0\mathrm{mm}\) in diameter, surrounded by atrial tissue to produce an overall mesh diameter of \(5.0\mathrm{mm}\) as illustrated schematically in Fig. 1(b). The SAN is known to be asymmetrical and somewhat more elongated than circular [4]. The symmetrical circular geometry employed here therefore represents a simplification of SAN geometry. Nevertheless, this simplified geometry is sufficient for the purpose of this study, to compare the ability of the discrete- region, gradient and mosaic models to reproduce features of pacemaker activity qualitatively consistent with that observed in the intact SAN.

### C. Governing Equations

Electrical activity in the SAN and atrial tissue was described by the monodomain equation;

\[\nabla \cdot (\sigma \nabla E_m) = A_m\left(C_m\frac{\partial E_m}{\partial t} + i_{tot}\right) \quad (1)\]

> **Image description.** A schematic diagram illustrating two idealized models of cardiac tissue: a one-dimensional (1D) model and a two-dimensional (2D) model, representing the Sinoatrial Node (SAN) and adjoining Atrial Tissue.
>
> The image is divided into two distinct panels, labeled (a) and (b).
>
> **Panel (a): One-Dimensional (1D) Model**
> This panel depicts a linear, one-dimensional representation of the tissue. It is divided into two adjacent sections:
> *   The left section is labeled "Sinoatrial Node" (SAN).
> *   The right section is labeled "Atrial Tissue."
> Below each section, the length is indicated by a dimension label of "1.5 mm." This model represents the tissue along a single axis.
>
> **Panel (b): Two-Dimensional (2D) Model**
> This panel shows a circular, two-dimensional representation of the tissue. It consists of two concentric regions:
> *   The inner, smaller circular region is labeled "SAN."
> *   The outer, larger annular region is labeled "Atrial Tissue."
> The SAN region is depicted with a lighter gray shading, while the surrounding Atrial Tissue region is shaded with a darker gray. A scale bar is provided in the bottom right corner, indicating a length of "0.5 mm."
>
> In summary, the figure visually contrasts the simplified linear representation of the tissue in panel (a) with the more complex, concentric circular representation in panel (b), both modeling the boundary and structure between the SAN and the surrounding atrial tissue.

<center>Fig. 1. Schematic representation of the idealized one dimensional (a) and two dimensional (b) models of the SAN and adjoining atrial tissue. In 2D, the SAN is modelled as a circular region \(3.0\mathrm{mm}\) in diameter, surrounded by atrial tissue resulting in an overall mesh diameter of \(5.0\mathrm{mm}\) . Zero flux boundary conditions were imposed at both ends of the 1D model and at the outer edge of the 2D model. </center>

where \(\sigma\) denotes the tissue conductivity \((\mu \mathrm{S}\cdot \mathrm{mm}^{- 1})\) , \(E_{m}\) denotes the transmembrane potential \((\mathrm{mV})\) , \(A_{m}\) denotes the cell surface- to- volume ratio \((\mathrm{mm}^{- 1})\) , \(C_{m}\) denotes the cell specific membrane capacitance \((\mu \mathrm{F}\cdot \mathrm{mm}^{- 2})\) , \(t\) denotes time (s), and \(i_{tot}\) denotes the sum of the transmembrane ionic currents \((\mathrm{nA}\cdot \mathrm{mm}^{- 2})\) , the kinetics of which are governed by the underlying single cell ionic models.

A Neumann (zero- flux) boundary condition was imposed at both ends of the 1D model and at the outer edge of the 2D model. In both cases, a conservation of flux condition was imposed at the SAN- atrial border where the tissue conductivity \((\sigma)\) was discontinuous (see below).

Cells of the rabbit SAN are reported to be roughly \(8\mu \mathrm{m}\) in diameter [3]. Atrial cells are reported to be somewhat larger, approaching \(20\mu \mathrm{m}\) in diameter [5]. Therefore, assuming that cells of the SAN and atria are roughly cylindrical results in estimated surface- to- volume ratios of \(500\mathrm{mm}^{- 1}\) and \(200\mathrm{mm}^{- 1}\) respectively [6]. The specific membrane capacitance \((C_{m})\) was assigned a uniform value of \(0.01\mu \mathrm{F}\cdot \mathrm{mm}^{- 2}\) throughout both the SAN and atrial regions [7].

### D. Single Cell ionic Models

The membrane ionic models of SAN tissue were based on a generic ionic model of isolated rabbit SAN myocytes [1]. This single cell model includes formulations for 12 membrane currents together with dynamic changes in ionic concentrations. With appropriate parameters, this model is able to accurately reproduce AP waveshapes recorded from the center and periphery of the SAN as well as a smooth variation in AP waveshape characteristics (namely: maximum diastolic potential (MDP), overshoot potential (OS), upstroke velocity (UV), action potential duration (APD) and cycle length (CL)) representative of the intermediate region. For details see [1]. Atrial tissue was simulated using the Earm, Hilgemann and Noble model of a single rabbit atrial myocyte [8][9].

### E. Modelling Sinoatrial Node Heterogeneity

Three models of SAN heterogeneity, namely the discrete- region, gradient and mosaic models, were formulated within the 1D and 2D frameworks described above.

1) The Discrete-Region Model: The SAN region was divided into two discrete areas, \(0 \leq d \leq 0.5\mathrm{mm}\) and \(0.5 < d < 1.5\mathrm{mm}\) , where \(d\) is the distance from the center of the SAN. Computational nodes within these two regions were assigned central and peripheral SAN cell characteristics respectively. The size of the central region \((d \leq 0.5\mathrm{mm})\) was consistent with the data of Kodama et al. [2], who observed central like AP waveshapes in only 1 or 2 balls \((\sim 0.3\mathrm{mm}\) in diameter) prepared from strands of SAN tissue running from the center to the periphery.

2) The Gradient Model: Computational nodes in the SAN were assigned model parameters to produce a linear variation (with respect to \(d\) ) in AP waveshape characteristics from those of a central SAN cell at \(d = 0\mathrm{mm}\) to those of a peripheral SAN cell at \(d = 1.5\mathrm{mm}\) .

3) The Mosaic Model: Computational nodes in the SAN were randomly designated as being of either SAN or atrial type. The probability of a node being designated of atrial type increased linearly with \(d\) , from \(0.0\) at \(d = 0\mathrm{mm}\) to \(1.0\) at \(d = 1.5\mathrm{mm}\) . The average probability of a node being of atrial type was therefore \(0.16\) in the central portion \((d \leq 0.5\mathrm{mm})\) and \(0.66\) in the peripheral portion \((0.5 < d < 1.5\mathrm{mm})\) of the SAN region. These average probabilities compare reasonably well with the proportions of atrial type cells observed by Verheijck et al. in the dominant pacemaker region \((22 \pm 15\%)\) , \(n = 5\) and in the crista terminalis \((63 \pm 18\%)\) , \(n = 6\) of the rabbit [10].

Four variations of the mosaic model were examined, involving central SAN and atrial cells (Mosaic- CA), peripheral SAN and atrial cells (Mosaic- PA), central and peripheral SAN cells (Mosaic- CP), and both central and peripheral SAN and atrial cells (Mosaic- CPA). The Mosaic- CA model, involving central SAN cells interspersed with atrial cells in the SAN region, was found to be untenable in the 1D simulations and was therefore not pursued in 2D.

### F. Sinoatrial Node-Atrial Conductivity Profiles

Two different idealized conductivity profiles were employed within the SAN region of both the 1D and 2D models. The first assumed a uniform conductivity throughout the SAN region and is consistent with electron microscopic studies of gap junction density in the SAN and the adjoining atrial tissue [11]. The second assumed a linear increase in conductivity from the center to the periphery of the SAN region. Such a gradient in coupling was first hypothesized by Joyner and van Capelle [12], and was recently employed in the 1D model formulated by Garny et al. [13]. Both the uniform and linear conductivity profiles employed here included a step change in conductivity at the SAN- atrial boundary, consistent with the experimental observation of Osthoek et al. [14] who reported an abrupt increase in gap junction density at the periphery of the SAN.

## III. RESULTS

### A. Simulated Activity in the 1D SAN Models

Fig. 2 shows the simulated AP waveshapes for the 1D Gradient model with the uniform conductivity profile. As can be seen, there is a smooth variation in AP waveshape from the center (top trace) to the periphery of the SAN and into the atrial tissue. Comparable simulations of the the Discrete- Region, Mosaic- CP and Mosaic- CPA models also produced AP waveshapes characteristic of both the center and periphery of the SAN (not shown). However, the Mosaic- PA variation of the mosaic model contained no central SAN cells and was therefore unable to produce AP waveshapes characteristic of the central region of the SAN. The Mosaic- CA model was largely unable to maintain spontaneous activity and was unable to successfully drive the adjoining atrial tissue.

Kirchhof et al. [15] reported that dissecting the atrial tissue away from the SAN resulted in a decrease in CL and a shift of the dominant pacemaking site away from the center and towards the periphery of the SAN. In both the Gradient and Mosaic- CP models, with both the uniform and linear conductivity profiles, the site of earliest activation was located in the periphery of the SAN in the absence of the atrial load. In the presence of the atrial load, the site of earliest activation was shifted away from the periphery and towards the center of the SAN. In contrast, the site of earliest activation in the Discrete- Region, Mosaic- PA and Mosaic- CPA models was located towards the center of the SAN for both the uniform and linear conductivity profiles and was largely unaffected by the atrial load.

### B. Simulated Activity in the 2D Sinoatrial Node Models

In the 2D models, the Discrete- Region, Gradient and Mosaic- CP models all displayed spontaneous pacemaker activity and successful activation of the atrial tissue under both the uniform and linear conductivity profiles. In contrast, the Mosaic- PA and Mosaic- CPA models were quiescent under the uniform conductivity profile, displaying no spontaneous pacemaker activity within the SAN either in the absence or in the presence of the surrounding atrial tissue.

> **Image description.** A line graph titled "Fig. 2 Simulated AP waveshapes for the 1D Gradient model of SAN" displays multiple simulated action potential (AP) waves over a period of time.
>
> The graph features a horizontal X-axis labeled "Time (s)," which spans from 0.0 to 0.25 seconds. The vertical Y-axis, which represents the amplitude of the AP waveshape, is unlabeled.
>
> The primary visual content consists of numerous overlapping curves, or traces, which represent the simulated electrical activity. All traces exhibit a similar pattern: they begin near zero, rise sharply to a peak, and then decay back toward the baseline. The curves are stacked vertically, illustrating a gradient in the waveshape. The traces positioned higher on the graph generally show a different profile or amplitude compared to those at the bottom, visually representing the variation from the center to the periphery of the SAN (Sinoatrial Node) as described in the accompanying text.
>
> The visible text elements are:
> *   Figure Caption: "Fig. 2 Simulated AP waveshapes for the 1D Gradient model of SAN"
> *   X-axis Label: "Time (s)"

<center>Fig. 2. Simulated AP waveshapes for the 1D Gradient model of SAN heterogeneity, with the uniform conductivity profile. The upper most trace corresponds to the center of the SAN ( \(d = 0 \mathrm{mm}\) ) and the moment of earliest activation has been aligned at \(t = 0.05 \mathrm{s}\) . The atrial conductivity was set to \(250 \mu \mathrm{S} \cdot \mathrm{mm}^{-1}\) , resulting in a space constant in atrial tissue of approximately \(1.0 \mathrm{mm}\) and an intrinsic conduction velocity of approximately \(0.5 \mathrm{m} \cdot \mathrm{s}^{-1}\) . SAN conductivity was set to \(25 \mu \mathrm{S} \cdot \mathrm{mm}^{-1}\) resulting in a SAN:atrial conductivity ratio of 1:10, consistent with observations of gap junction density [11]. </center>

Fig. 3 shows simulated activity in the 2D Gradient model with the uniform conductivity profile. The activation sequence is illustrated in Fig. 3(a) where the site of earliest activation is rendered in yellow and the smooth transition to red indicates regions activated increasingly later in the activation sequence. The SAN- atrial border ( \(d = 1.5 \mathrm{mm}\) ) is indicated by the dashed circle passing through point D. Fig. 3(b) shows representative AP waveshapes observed along a single radius as indicated on the activation map.

As for the 1D simulations, with the uniform conductivity profile, both the Gradient and Mosaic- CP models exhibited a shift in the site of earliest activation away from the center and towards the periphery of the SAN following removal of the atrial tissue (not shown). However, with the linear conductivity profile, the site of earliest activation in the Mosaic- CP model was located close to the center of the SAN and was largely unaffected by the atrial tissue load.

## IV. DISCUSSION

In addition to the qualitative observations described above, we have also undertaken a quantitative comparison of the different 1D models of SAN heterogeneity [16]. Each of the different models was assessed on their ability to achieve frequency entrainment within the SAN and to successfully activate the adjoining atrial tissue. These simulation results indicated that the gradient model achieved frequency entrainment of the SAN most easily, i.e., at the lowest conductivity. This observation, together with the simulation results described above, suggest that the gradient model represents the most plausible model of SAN heterogeneity.

> **Image description.** A composite technical figure consisting of two panels, (a) and (b), illustrating the results of a 2D Gradient model simulation of cardiac tissue.
>
> Panel (a) is an activation map, presented as a circular heat map.
> *   **Spatial Domain:** The map is defined within a circular area, with axes ranging from -2.5 to 2.5 mm on both the X and Y dimensions.
> *   **Data Representation:** The color gradient represents "Activation Time (ms)," as indicated by the color bar at the bottom. The colors transition from bright yellow (representing the earliest activation, 0 ms) in the center to deep red (representing the latest activation, 40 ms) at the periphery.
> *   **Pattern:** The activation spreads outward from the center in concentric rings, showing a wave-like progression of activation time.
> *   **Labels and Markers:** Six points (A, B, C, D, E, F) are marked along a horizontal line near the top edge of the circle. A dashed circle is drawn passing through point D.
>
> Panel (b) is a line graph showing representative Action Potential (AP) waves over time.
> *   **Axes:** The X-axis is labeled "Time (s)" and ranges from 0.0 to 0.25. The Y-axis is labeled with the corresponding spatial points A, B, C, D, E, and F from panel (a).
> *   **Data Curves:** Multiple curves are plotted, each representing the electrical activity (Action Potential) at a specific location.
> *   **Visual Pattern:** All curves exhibit a characteristic sharp rise (upstroke) followed by a peak and subsequent decay. The timing of the sharp rise (the onset of activation) progresses sequentially from point A, which shows the earliest activation, to point F, which shows the latest activation, directly correlating the temporal data in panel (b) with the spatial progression shown in panel (a).
>
> The figure collectively demonstrates how the activation wave spreads spatially (Panel a) and how this spatial progression translates into a sequence of temporally delayed electrical signals (Panel b).

<center>Fig. 3. Activation map (a) and representative AP waveshapes (b) for the 2D Gradient model with the uniform conductivity profile. As in Fig. 2, the SAN and atrial conductivities were set to \(25\) and \(250\mu \mathrm{S}\cdot \mathrm{mm}^{-1}\) respectively. The dashed circle passing through point D in (a) indicates the location of the SAN-atrial boundary. </center>

## V. CONCLUSION

Simulation results suggest that the gradient model, unlike the discrete- region or mosaic models, reproduces action potential waveshapes and a site of earliest activation consistent with experimental observations in the intact SAN. It is therefore proposed that the gradient model represents the most plausible model of SAN organisation.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
