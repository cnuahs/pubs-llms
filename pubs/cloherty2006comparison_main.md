```
@article{cloherty2006comparison,
  title={A comparison of 1-D models of cardiac pacemaker heterogeneity},
  author={Shaun L. Cloherty and Socrates Dokos and Nigel H. Lovell},
  journal={IEEE Transactions on Biomedical Engineering},
  year={2006},
  volume={53},
  number={2},
  pages={164-177},
  doi={10.1109/tbme.2005.862538},
  url={https://ieeexplore.ieee.org/document/1580822}
}
```

---

# A Comparison of 1-D Models of Cardiac Pacemaker Heterogeneity

Shaun L. Cloherty\*, Member, IEEE, Socrates Dokos, and Nigel H. Lovell, Senior Member, IEEE

Abstract—In this paper, we investigate the role of sinoatrial node (SAN) cellular heterogeneity in two key aspects of normal cardiac pacemaker function: frequency entrainment of the SAN, and propagation of excitation into the atrial tissue. Using detailed ionic models of electrical activity in SAN and atrial myocytes, we have formulated a number of one- dimensional models of SAN heterogeneity based on discrete- region (in which central and peripheral SAN type cell are separated into discrete regions), gradient and mosaic models of SAN organization. Each of the different models were assessed on their ability to achieve frequency entrainment of the SAN and activation of the adjoining atrial tissue in the presence of both uniform and linearly increasing conductivity profiles. Simulation results suggest that the gradient model of SAN heterogeneity, in which cells display a smooth variation in membrane properties from the center to the periphery of the SAN, produces action potential waveshapes and a site of earliest activation consistent with experimental observations in the intact SAN. The gradient model also achieves frequency entrainment of the SAN more easily than other models of SAN heterogeneity. Based on these results, we conclude that the gradient model of SAN heterogeneity, in the presence of a uniform conductivity profile, is the most likely model of SAN organization.

Index Terms—Action potential heterogeneity, frequency entrainment, mathematical modeling, monodomain model, sinoatrial node.

## I. INTRODUCTION

UNDER normal conditions, electrical activation of the mammalian heart is initiated in a small region of specialized pacemaker cells known as the sinoatrial node (SAN). Regional variation in cellular electrical properties (both ionic and structural) is a widely accepted characteristic of the intact SAN, which has been well studied in the rabbit [1]. However, little attention has been given to its contribution to both normal and abnormal pacemaker function.  

In a recent simulation study, we reported that heterogeneity in action potential (AP) waveshape assisted frequency entrainment of electrically coupled pacemaker cell pairs [2]. It was proposed that regional variation in AP characteristics within the intact SAN provides an important mechanism underlying pacemaker synchronization [2]. In this paper we formulate a number of computational models of heterogeneity in the rabbit SAN and investigate the relative merits of each model in facilitating the two main functions of the SAN: maintaining a robust synchronous rhythm, and electrical activation of the adjoining atrial tissue.

Early studies of the SAN based on histological, ultrastructural and electrophysical observations describe a discrete- region model of SAN organization (for a review see [3]). According to this discrete- region model, the SAN is composed of a compact central region of primary pacemaker cells surrounded by a region of transitional cells forming a buffer zone between the primary pacemaker cells and the working myocardium. The cardiac AP is initiated in the compact central region of the SAN and propagates outwards through the peripheral region and into the atrial tissue.

In a later study, Kodama and Boyett [1] observed a variation in AP characteristics in small isopotential balls of tissue \((\sim 0.3\mathrm{mm}\) in diameter) isolated from known spatial locations within the SAN. They concluded that the variation in AP waveshape was due to a genuine transition in ion channel expression, and proposed the gradient model of SAN heterogeneity.

More recently, Verheijck et al. [4] identified three morphologically different types of SAN cells in addition to atrial myocytes in rabbit SAN tissue. After enzymatic isolation, these three cell types appeared to exhibit no significant variation in AP characteristics. They hypothesized that the observed variation in AP waveshape from the center to the periphery of the SAN was due to a gradual increase in atrial cell numbers toward the periphery. This interpretation forms the basis of the mosaic model of SAN heterogeneity.

In this paper, we attempt to identify the most plausible model of SAN heterogeneity. We employ a biophysically detailed ionic model of a single SAN myocyte, able to exactly reproduce AP recordings from both the center and periphery of the rabbit SAN. With appropriate parameters, this model is also able to produce AP waveshapes characteristic of the intermediate region between the center and the periphery of the SAN. Several one- dimensional (1- D) models of the SAN are formulated, based on the three conceptual models of SAN heterogeneity described above, namely the discrete- region model, the gradient model and the mosaic model. We present results from a number of simulations aimed at assessing the relative merits of each conceptual model of SAN heterogeneity and attempt to identify a number of mechanisms which likely underly normal SAN pacemaker function.

Manuscript received November 29, 2004; revised May 22, 2005. Asterisk indicates corresponding author. \*S. L. Cloherty is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, NSW 2052, Australia (e- mail: s.cloherty@gsbme.unsw.edu.au). S. Dokos and N. H. Lovell are with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, NSW 2052, Australia. Digital Object Identifier 10.1109/TBME.2005.862538

## II. METHODS

### A. The Single Cell Models

The membrane ionic models of SAN tissue were based on a generic ionic model of isolated rabbit SAN myocytes [5]. This

single cell model includes formulations for 12 membrane currents together with dynamic changes in ionic concentrations. The default parameters of the generic model were selected to faithfully reproduce published voltage clamp data applicable to the rabbit SAN.

In order to reproduce the observed heterogeneity in AP waveshapes from rabbit SAN, a subset comprising 173 of the generic model parameters were then fine- tuned using a nonlinear optimization routine [5], [6], to fit AP recordings from central and peripheral regions. Throughout the optimization process, the model parameters were subject to tight constraints designed to ensure reasonable correlation with the default values and that the peak ion current amplitudes remain in close agreement with experimental observations.

The resulting central and peripheral SAN cell models provided a basis for formulating a smooth transition in cell model parameters in the intermediate region. Model parameters which produced AP waveshape characteristics [namely: maximum diastolic potential (MDP), overshoot potential (OS), upstroke velocity (UV), action potential duration (APD), and cycle length (CL)] representative of the intermediate region were identified in a separate optimization procedure as described previously [5].

Atrial tissue was simulated using the Earm, Hilgemann, and Noble (EHN) model of a single rabbit atrial cell [7], [8].

### B. One-Dimensional Model of the Intact Cardiac Pacemaker

The SAN and adjoining atrial tissue was approximated as a highly idealized 1- D cable, consisting of a region of SAN tissue coupled to a region of atrial tissue as illustrated schematically in Fig. 1.

Electrical activity in the SAN and atrial tissue was determined by the monodomain equation

\[\nabla \cdot (\sigma \nabla E_{m}) = A_{m}\left(C_{m}\frac{\partial E_{m}}{\partial t} +\dot{\imath}_{tot}\right) \quad (1)\]

where \(\sigma\) denotes the tissue conductivity \((\mu \mathrm{S}\cdot \mathrm{mm}^{- 1})\) , \(E_{m}\) denotes the transmembrane potential (mV), \(A_{m}\) denotes the cell surface- to- volume ratio \((\mathrm{mm}^{- 1})\) , \(C_{m}\) denotes the cell specific membrane capacitance \((\mu \mathrm{F}\cdot \mathrm{mm}^{- 2})\) , \(t\) denotes time (s), and \(\dot{\imath}_{tot}\) denotes the sum of the transmembrane ionic currents \((\mathrm{mA}\cdot \mathrm{mm}^{- 2})\) , the kinetics of which are governed by the underlying single cell ionic models.

Neumann (zero- flux) boundary conditions were imposed at both ends of the 1- D model, i.e.,

\[\nabla E_{m}|_{(t = 0)} = \nabla E_{m}|_{(t = l_{s} + l_{a})} = 0. \quad (2)\]

A conservation of flux condition given by (3) was imposed at the SAN- atrial border since the tissue conductivity \((\sigma)\) was discontinuous at \(l = l_{s}\)

\[\sigma_{s}\nabla E_{m}|_{(t - l_{s}) - 0 - } = \sigma_{a}\nabla E_{m}|_{(t - l_{s}) - 0 + }. \quad (3)\]  

The length of the SAN region \((l_{s})\) was set to \(1.5\mathrm{mm}\) , roughly in agreement with the distance from the center to the periphery of the SAN perpendicular to and in the direction of the crista terminalis (CT) in the rabbit [1], [9]. The length of the atrial tissue region \((l_{a})\) was also set to \(1.5\mathrm{mm}\) . While considerably shorter than the spatial scale of the right atrium in the rabbit, this length corresponds to roughly 1.5 space constants and was sufficient to approximate the electronic load imposed on the SAN by the atrial tissue without any adverse effect on the SAN from the zero flux boundary condition imposed at the end of the preparation.

> **Image description.** A schematic diagram illustrating a highly idealized one-dimensional (1D) model of cardiac tissue, consisting of two adjacent, elongated regions. The diagram is presented on a plain white background and uses simple black outlines to define the shapes.
>
> The visual content is divided into two distinct, horizontal sections:
>
> 1.  **Sinoatrial Node (SAN) Region:** Located on the left side of the image, this region is represented by a uniform, elongated, cylindrical shape. Below this shape, the label "Sinoatrial Node" is centered, and the length of this region is indicated by the variable $l_s$ positioned beneath the shape.
> 2.  **Atrial Tissue Region:** Located immediately to the right of the SAN region, this section is also represented by a uniform, elongated, cylindrical shape, suggesting a continuous cable structure. Below this shape, the label "Atrial Tissue" is centered, and the length of this region is indicated by the variable $l_a$ positioned beneath the shape.
>
> The two regions are depicted as being coupled or adjacent, with the SAN region transitioning directly into the Atrial Tissue region. The diagram visually represents the approximation of the SAN and adjoining atrial tissue as a single, continuous 1D cable model, where $l_s$ and $l_a$ denote the respective lengths of the two tissue types.

<center>Fig. 1. The idealized 1-D model of the SAN and adjoining atrial tissue. The total length of the preparation was \(3\mathrm{mm}\) , with \(l_{s} = l_{a} = 1.5\mathrm{mm}\) . Zero flux boundary conditions were imposed at both ends of the model. </center>

There is considerable experimental evidence to suggest that the specific membrane capacitance in cardiac tissue is largely independent of cell type and may reasonably be assumed to be approximately \(0.01\mu \mathrm{F}\cdot \mathrm{mm}^{- 2}\) [10]. Therefore, \(C_{m}\) was assigned a uniform value of \(0.01\mu \mathrm{F}\cdot \mathrm{mm}^{- 2}\) throughout both the SAN and atrial regions of the 1- D models formulated in this paper.

Cells of the rabbit SAN are reported to be roughly \(8\mu \mathrm{m}\) in diameter and \(25 - 30\mu \mathrm{m}\) in length [9]. Atrial cells are reported to be somewhat larger, approaching \(20\mu \mathrm{m}\) in diameter and 100 \(\mu \mathrm{m}\) in length [11]. Therefore, assuming that cells of the SAN and atria are roughly cylindrical results in estimated surface- to- volume ratios of \(500\mathrm{mm}^{- 1}\) and \(200\mathrm{mm}^{- 1}\) respectively.

### C. Modeling Sinotrial Node Heterogeneity

Three models of SAN heterogeneity, namely the discrete- region, gradient and mosaic models, were formulated within the framework of the 1- D model of the SAN described above.

The Discrete- Region Model: In the Discrete- Region model, the SAN region of the 1- D model was divided into two discrete areas, \(0\leq l\leq (1 / 3)l_{s}\) and \((1 / 3)l_{s}< l< l_{s}\) . Computational nodes within these two regions were assigned central and peripheral SAN cell characteristics respectively. The size of the central region \(((1 / 3)l_{s} = 0.5\mathrm{mm})\) was consistent with the data of Kodama et al. [1], who observed central like AP waveshapes in only 1 or 2 balls \((\sim 0.3\mathrm{mm}\) in diameter) prepared from strands of tissue running from the center to the periphery of the SAN.

The Gradient Model: In the Gradient model, a smooth transition in AP waveshape characteristics was imposed in the SAN region of the 1- D model. Computational nodes in the SAN region were assigned SAN model parameters to produce a linear variation (with respect to \(l\) ) in AP waveshape characteristics from those of a central SAN cell at \(l = 0\) to those of a peripheral SAN cell at \(l = l_{s}\) .

The Mosaic Model: In the mosaic model, nodes in the SAN region of the 1- D model were randomly designated as being of either SAN or atrial type. The probability of a node being designated of atrial type increased linearly with \(l\) , from \(0.0\) at \(l = 0\) to \(1.0\) at \(l = l_{s}\) . The average probability of a node being of atrial type was, therefore, \(0.16\) in the central portion \((l\leq (1 / 3)l_{s})\) and \(0.66\) in the peripheral portion \(((1 / 3)l_{s}< l< l_{s})\) of the SAN region. These average probabilities compare reasonably well with the proportions of atrial type cells observed by Verheijck et al. in the dominant pacemaker region \((22\pm 15\% ,n = 5)\) and in the CT \((63\pm 18\% ,n = 6)\) of the rabbit [4].

The following four variations of the mosaic model were examined in this paper.

1) The Mosaic-CA model, in which nodes designated as being of SAN type were simulated using model parameters corresponding to the central type SAN cell. Those designated as being of atrial type were simulated using the single rabbit atrial cell model employed in the atrial region of the 1-D model. 
2) The Mosaic-PA model, which was formulated in the same manner as above, substituting the peripheral SAN cell model in place of the central SAN cell model. 
3) The Mosaic-CP model, which employed the central SAN cell model at nodes designated as being of SAN type, and the peripheral SAN cell model at nodes designated as being of atrial type. 
4) The Mosaic-CPA model, which employed all three cell types. Nodes designated as being of SAN type were randomly assigned model parameters corresponding to either central or peripheral SAN type cells. Nodes designated as being of atrial type were simulated using the atrial cell model.

In the Mosaic- CP variation of the mosaic model, nodes designated as being of atrial type and assigned parameters corresponding to the peripheral SAN cell model may be thought of as representing small regions of tissue containing both SAN and atrial cells with a predominance of atrial type cells. Similarly, nodes designated as being of SAN type and assigned parameters corresponding to the central SAN cell model may be thought of as representing small regions of tissue containing a predominance of SAN type cells.

In the Mosaic- CPA model, the probability of a node being designated as central SAN type \((p_{\mathrm{central}})\) decreased monotonically with \(l\) from 1.0 at \(l = 0\) to 0.0 at \(l = l_{s}\) according to

\[p_{\mathrm{central}} = (1 - \mu)^{\eta} \quad (4)\]

where \(\mu\) is the normalized distance from the center of the SAN, i.e., \(\mu = l / 1.5\) , and \(\eta\) determines the spatial rate of decay of \(p_{\mathrm{central}}\) with distance from the center of the SAN. The parameter \(\eta\) was set to 6.3884 such that the overall probability of a node being designated as central SAN type was reduced to \(\sim 0.05\) at \(l = (1 / 3)l_{s}\) . Fig. 2 shows the probability distribution for each cell type in the SAN region of the Mosaic- CPA model as a function of distance from the center of the SAN.

### D. SAN-Atrial Conductivity Profiles

While there is little experimental information regarding the distribution of gap junctions within the SAN, histological studies suggest the density of gap junctions in atrial tissue may be as much as 10 times higher than in the SAN [12]. Although the exact mechanism remains unclear, there exists some evidence to suggest a spatial gradient in conductivity from the center to the periphery of the SAN [11]. The 1- D models formulated in this paper, therefore, employ two idealized conductivity profiles throughout the SAN region. The first imposes a uniform conductivity throughout the SAN (Fig. 3, top panel), whilst the second establishes a linear increase in conductivity from the center to the periphery of the SAN (Fig. 3, bottom panel).

The atrial conductivity \((\sigma_{a})\) was set to \(250\mu \mathrm{S}\cdot \mathrm{mm}^{- 1}\) . In simulations of a 1- D strand of atrial tissue, this conductivity yielded

> **Image description.** A line graph titled "Fig. 2. Probability distributions for central SAN, peripheral SAN and atrial" illustrates the probability of different cell types (Central SAN, Peripheral SAN, and Atrial) occurring at various distances from the center of the SAN.
>
> The graph features two primary axes:
> *   The Y-axis, labeled "Probability," ranges from 0 to 1.
> *   The X-axis, labeled "Distance from the center of the SAN (mm)," ranges from 0 to 1.5, marked with increments at 0, 0.5, 1, and 1.5.
>
> Three distinct data series are plotted, each representing a different cell type distribution:
>
> 1.  **Central SAN:** Represented by a solid black line. This distribution starts at a probability of 1.0 at a distance of 0 mm. It exhibits a rapid, steep decay, dropping to approximately 0.6 at 0.5 mm and continuing to decrease toward 0 as the distance increases.
> 2.  **Peripheral SAN:** Represented by a dashed black line. This distribution begins at a probability of 0 at 0 mm. It rises sharply, reaching a peak probability of approximately 0.7 at a distance of 0.5 mm. After this peak, the probability gradually decreases, approaching 0 by 1.5 mm.
> 3.  **Atrial:** Represented by a dotted black line. This distribution starts at a probability of 0 at 0 mm. It shows a steady, monotonic increase across the entire range, reaching a probability of approximately 1.0 at 1.5 mm.
>
> The three curves intersect and overlap, demonstrating how the probability of each cell type changes spatially as the distance from the SAN center increases. For example, at a distance of 0.5 mm, the Central SAN probability is around 0.6, the Peripheral SAN probability is at its peak of 0.7, and the Atrial probability is approximately 0.3. At the maximum distance of 1.5 mm, the Atrial probability is 1.0, while the Central and Peripheral SAN probabilities are both near 0.

<center>Fig. 2. Probability distributions for central SAN, peripheral SAN and atrial type cells in the SAN region of the Mosaic-CPA model. </center>

a space constant of approximately \(1.0\mathrm{mm}\) and an intrinsic conduction velocity (CV) of approximately \(0.5\mathrm{m}\cdot \mathrm{s}^{- 1}\) . Removal of the atrial tissue from the intact SAN is known to cause a shift in the site of earliest activation away from the center and toward the periphery of the SAN [13]. In order to assess the ability of each model to reproduce this shift and also to determine the effect of the atrial load on entrainment of the SAN, a number of simulations were performed in which the SAN region was isolated from the atrial tissue region by setting the atrial conductivity \((\sigma_{a})\) to zero. In this configuration, the conservation of flux condition [see (3)] reduced to the familiar Neumann or zero- flux boundary condition imposed at the ends of the 1- D model.

### E. Frequency Entrainment of the Sinotrial Node

In each model of SAN heterogeneity described above, cells within the SAN region exhibit different intrinsic CLs. At low values of SAN conductivity these cells remain essentially independent. At sufficiently large SAN conductivities, cells achieve frequency entrainment at a common CL. A number of simulations were performed to determine the minimum conductivity required for frequency entrainment of each model of SAN heterogeneity described above. The criterion for assessing the entrainment state of the SAN is described below. The critical conductivity, denoted as \(\sigma_{s,ent}\) , was determined for each model with the uniform conductivity profile both in the absence and in the presence of the atrial tissue load.

The process was repeated using the linear conductivity profile with the conductivity at the center of the SAN region \((\sigma_{s - c})\) set to \(0.01\mu \mathrm{S}\cdot \mathrm{mm}^{- 1}\) . This value was approximately \(25\%\) of the minimum critical conductivity for entrainment of the SAN with the uniform conductivity profile (see Section III- B). In the case of the linear conductivity profile, the critical conductivity for entrainment was defined as the minimum conductivity required at the periphery of the SAN region \((l = l_{s})\) and was denoted as \(\sigma_{s - p,ent}\) .

In each configuration, the model was simulated for \(5\mathrm{s}\) to stabilise any initial transients. The model was then simulated for a further \(10\mathrm{s}\) during which the entrainment state of the SAN region was assessed. With the uniform conductivity profile, both the gradient and mosaic models took considerably longer to approach steady state. In these configurations, the model was simulated for an initial period of \(20\mathrm{s}\) before commencing the \(10\mathrm{s}\) observation period.

> **Image description.** A technical figure consisting of two stacked line graphs, labeled Figure 3, which illustrate the conductivity profiles of the SAN (Sinoatrial Node) and adjoining atrial tissue in 1-D models. Both graphs share the same general coordinate system, with the vertical axis representing conductivity ($\sigma_a$) and the horizontal axis representing position or length ($l_s$).
>
> The figure is divided into two distinct panels:
>
> 1.  **Top Panel (Uniform Profile):** This panel depicts the "uniform" conductivity profile. The graph shows two horizontal line segments. The conductivity ($\sigma_a$) is constant from the starting point ($l=0$) up to the boundary at $l=l_s$. At $l=l_s$, the conductivity remains constant but appears to jump to a higher value for the remainder of the domain, extending to $l+l_a$. This represents a step-function where the conductivity is uniform within the SAN region and then constant in the adjoining atrial tissue.
>
> 2.  **Bottom Panel (Linear Profile):** This panel depicts the "linear" conductivity profile. The graph shows a non-uniform distribution. The conductivity starts at a lower value, labeled $\sigma_{s-c}$ (representing the conductivity at the center of the SAN region, $l=0$). The conductivity then increases linearly (or near-linearly) as the position $l$ increases, reaching a value labeled $\sigma_{s-p}$ at the boundary $l=l_s$. At this boundary, the conductivity abruptly jumps to a higher, constant value for the rest of the domain, extending to $l+l_a$.
>
> The figure caption, "Fig. 3. The uniform (top) and linear (bottom) SAN–Atrial conductivity profiles employed in the 1-D models of the SAN and adjoining atrial tissue. A conservation of flux condition was imposed at the boundary between the SAN and atrial tissue regions where the conductivity is discontinuous," provides the technical context for the visual data. The variables $\sigma_a$ and $l_s$ represent conductivity and position, respectively, while the profiles model how electrical conductivity varies across the boundary between the SAN and the surrounding atrial tissue.

<center>Fig. 3. The uniform (top) and linear (bottom) SAN–Atrial conductivity profiles employed in the 1-D models of the SAN and adjoining atrial tissue. A conservation of flux condition was imposed at the boundary between the SAN and atrial tissue regions where the conductivity is discontinuous. </center>

For the purposes of this paper, a given configuration was deemed to be entrained if, for each cycle in the 10 s observation period, the range of CLs observed within the SAN region was less than \(5\%\) of the mean CL in each cycle. The CL at a given node was defined to be the interval between moments of maximal UV. The critical conductivities \((\sigma_{s,ent}\) and \(\sigma_{s = p,ent})\) were then compared in order to assess the relative ease with which each of the models of SAN heterogeneity achieved frequency entrainment.

### F. Activation of the Adjoining Atrial Tissue

A series of simulations were performed for each model of SAN heterogeneity to determine the minimum SAN conductivity required for propagation of the AP from the SAN into the adjoining atrial tissue. The criterion for determining successful activation of the atrial tissue by the SAN is described below.

Simulations were performed first with the uniform conductivity profile described above. The minimum SAN conductivity required for activation of the atrial tissue, referred to as the critical conductivity for activation, was denoted as \(\sigma_{s,act}\) .

The procedure was then repeated with the linear conductivity profile, with the conductivity at the center of the SAN region \((\sigma_{s = c})\) set to \(0.01 \mu \mathrm{S} \cdot \mathrm{mm}^{- 1}\) . As for the entrainment simulations described above, the critical conductivity for activation with the linear conductivity profile was defined as the minimum conductivity required at the periphery of the SAN region \((l = l_{s})\) and was denoted as \(\sigma_{s = p,act}\) .

In determining the critical conductivity, each configuration of the model was simulated for a short duration to stabilise any initial transients. At the conductivities required for successful activation of the atrial tissue, all model configurations approached steady- state within 5 s. Each configuration was then simulated for a further 10 s during which the activation state of the atrial tissue region was assessed. A given configuration was deemed to successfully activate the atrial tissue if a 1:1 correspondence was observed between APs in the SAN and atrial regions throughout the entire 10 s observation period. The critical conductivities \((\sigma_{s,act}\) and \(\sigma_{s = p,act})\) were then compared to assess the relative ease with which each model of SAN heterogeneity could drive the atrial tissue.

> **Image description.** A technical figure consisting of two line graphs, labeled (a) and (b), which display simulated action potential (AP) waves for the central and peripheral parts of the Sinoatrial (SAN) tissue.
>
> **General Graph Features:**
> Both panels are line graphs plotting "Membrane Potential (mV)" on the vertical Y-axis against "Time (s)" on the horizontal X-axis. The Y-axis ranges from -80 mV to 40 mV, with major tick marks every 20 mV. The X-axis ranges from 0 to 1 second, with major tick marks every 0.2 seconds. In both graphs, two data sets are compared: "Model" (represented by a solid dark line) and "Experimental" (represented by a solid red line). Both lines depict the characteristic shape of an action potential, including a rapid depolarization (upward spike), a plateau, and a repolarization (downward return).
>
> **Panel (a): Central SAN**
> The top graph is labeled "Central SAN." It shows the membrane potential over time for the central region of the SAN. The "Model" and "Experimental" lines are closely aligned throughout the cycle, indicating a high degree of agreement between the simulated and observed data. A small inset graph is located in the upper right corner of this panel, providing a zoomed-in view of the action potential waveform.
>
> **Panel (b): Peripheral SAN**
> The bottom graph is labeled "Peripheral SAN." It displays the membrane potential over time for the peripheral region of the SAN. Similar to Panel (a), the "Model" and "Experimental" lines are plotted and show a characteristic action potential shape. While the overall morphology is similar to the central SAN, the specific timing and peak of the AP wave appear slightly different. This panel also includes a small inset graph in the upper right corner, showing a zoomed-in view of the action potential waveform.
>
> **Caption:**
> Below the two graphs, the figure is captioned: "Fig. 4. Simulated AP waves for the (a) central and (b) peripheral SAN."

<center>Fig. 4. Simulated AP waveshapes for the (a) central and (b) peripheral SAN cell models. Experimental recordings from central and peripheral regions of the SAN to which the model parameters were fitted are also shown (Experimental data from Kodama et al. [15]). In each case, the AP waveshapes are shown aligned at the moment of maximum UV and an enlarged view of a portion of the waveshape (indicated by a dotted rectangle) is shown inset in the upper right corner. </center>

### G. Computational Methods

The simulation code, including the underlying ionic models was implemented in ANSI C. The ordinary differential equations of the underlying ionic models were evolved using the CVODE solver for stiff systems [14] with a relative error tolerance of \(10^{- 4}\) and a maximum time step of 0.1 ms. The 1- D monodomain equation was solved using a finite- difference approximation of the partial spatial derivatives with a maximum spatial step of 0.0625 mm.

## III. RESULTS

### A. Central and Peripheral SAN Cell Models

Fig. 4 illustrates the AP waveshapes for the central and peripheral cell models together with the AP data from central and

TABLE I CRITICAL CONDUCTIVITY \((\mu \mathrm{S}\cdot \mathrm{mm}^{-1})\) FOR ENTRAMINENT

| Model | $\sigma_{s,ent}$ Uniform (No Load) | $\sigma_{s,ent}$ Uniform (Load) | $\sigma_{s-p,ent}$ Linear (No Load) | $\sigma_{s-p,ent}$ Linear (Load) |
| :--- | :---: | :---: | :---: | :---: |
| Discrete-Region | 0.063 | 0.063 | 1.846 | 1.848 |
| Gradient | 0.048 | 0.044 | 0.777 | 0.601 |
| Mosaic-CA | $1.473 \pm 0.618^\ddagger$ | $1.121 \pm 0.111^\ddagger$ | $2.367 \pm 0.888^\ddagger$ | $2.555 \pm 1.087^\ddagger$ |
| Mosaic-PA | $0.875 \pm 0.438$ | $1.182 \pm 0.629$ | $1.903 \pm 1.548$ | $2.025 \pm 1.579$ |
| Mosaic-CP | $0.066 \pm 0.013$ | $0.066 \pm 0.013$ | $4.918 \pm 3.025$ | $13.355 \pm 4.160$ |
| Mosaic-CPA | $1.080 \pm 0.743$ | $1.291 \pm 0.786$ | $2.154 \pm 1.470$ | $2.263 \pm 1.505$ |

† SAN region isolated from the atrial load. \(\begin{array}{rl}{\mathrm{~\#~}n=3}&{\mathrm{~\#~}n=2}\end{array}\) \(\begin{array}{r}\mathrm{~\#~}n=8 \end{array}\)

peripheral regions of the SAN to which the default model parameters were fitted [15]. In each case the simulated APs and the experimental recordings are shown aligned at the time of maximum UV. As can be seen, the correlation between the experimental recordings and the simulated AP waveshapes of the central and peripheral cell models is very high.

### B. Critical Conductivity for Entrainment

Table I summarizes the critical SAN conductivity for entrainment for each of the SAN models under both the uniform \((\sigma_{s,ent})\) and the linear \((\sigma_{s - p,ent})\) conductivity profiles. For each profile, values are given both in the absence and in the presence of the atrial load.

In the case of the mosaic models, the critical conductivity is reported as the mean \(\pm \mathrm{SD}\) \((n = 10)\) . A number of trials of the Mosaic- CA model were unable to maintain spontaneous pacemaker activity. These trials have been omitted in the results summarized in Table I. The number of trials included in the affected results are indicated in the table notes.

From Table I it is apparent that the Gradient model achieves frequency entrainment more easily, i.e., at a lower critical conductivity, than the Discrete- Region model. This is true under both the uniform and linear conductivity profiles in the absence and in the presence of the atrial load.

Under the uniform conductivity profile, the Gradient model required significantly lower conductivity to achieve entrainment than the Mosaic- PA, Mosaic- CP or Mosaic- CPA models \((p< 0.001)\) . This was true both in the presence and in the absence of the atrial load. Under the linear conductivity profile, the Gradient model also required a significantly lower conductivity to achieve entrainment in the presence of the atrial load than either the Mosaic- PA, Mosaic- CP or Mosaic- CPA models \((p< 0.01)\) . This was also true in the absence of the atrial load although in the case of the Mosaic- PA model, the difference was marginally less significant \((p< 0.05)\) .

Under the uniform conductivity profile, the critical conductivity required for entrainment of the Discrete- Region and Mosaic- CP models was unaffected by the addition of the atrial load. The presence of the atrial load also had no significant effect on the critical conductivity required for either the Mosaic- PA or the Mosaic- CPA models. In contrast, the critical conductivity for the Gradient model under the uniform conductivity profile was reduced by approximately \(10\%\) on addition of the atrial load. It should be noted that in the case of the Mosaic- CA model, most of the random cell type distributions were unable to maintain

TABLE II CRITICAL CONDUCTIVITY \((\mu \mathrm{S}\cdot \mathrm{mm}^{-1})\) FOR ACTIVATION

| Model | $\sigma_{s,act} (\pm SD)$ | $\sigma_{s-p,act} (\pm SD)$ |
| :--- | :--- | :--- |
| | Uniform | Linear |
| Discrete-Region | 16.279 | 14.244 |
| Gradient | 16.310 | 14.325 |
| Mosaic-CA | 16.133 $\pm$ 2.960 | |
| Mosaic-PA | 16.022 $\pm$ 4.278 | 16.615 $\pm$ 6.945 |
| Mosaic-CP | 16.563 $\pm$ 0.648 | 14.563 $\pm$ 0.385 |
| Mosaic-CPA | 15.720 $\pm$ 3.275 | 15.375 $\pm$ 3.003 |

\(\begin{array}{r}\mathrm{~\#~}n=7 \end{array}\)

spontaneous pacemaker activity under the uniform conductivity profile (see Table I).

Under the linear conductivity profile, addition of the atrial load again had no significant effect on the critical conductivity of either the Discrete- Region, Mosaic- PA or Mosaic- CPA models. However, the critical conductivity for the Mosaic- CP model was significantly increased on addition of the atrial load \((p< 0.001)\) . As for the uniform conductivity profile, the critical conductivity for the Gradient model under the linear conductivity profile was reduced by approximately \(20\%\) on addition of the atrial load. Again, it should be noted that in the case of the Mosaic- CA model, not all of the random cell type distributions were able to maintain spontaneous pacemaker activity (see Table I).

### C. Critical Conductivity for Activation

Table II summarizes the critical conductivity required for activation of the atrial tissue for the different models of SAN heterogeneity, under both the uniform and the linear conductivity profiles. As described above, for the linear conductivity profile, values are given for the critical conductivity at the periphery of the SAN region \((\sigma_{s - p,act})\) corresponding to a value for the conductivity at the center of the SAN region \((\sigma_{s - c})\) of 0.01 \(\mu \mathrm{S}\cdot \mathrm{mm}^{- 1}\) . Again, in the case of the mosaic models, the critical conductivity is reported as the mean \(\pm \mathrm{SD}\) \((n = 10)\) .

The critical conductivity for activation in the case of the Mosaic- CP model under the linear conductivity profile was significantly lower \((p< 0.001)\) than that required under the uniform conductivity profile. However, it was significantly larger \((p< 0.05)\) than that required by either the Discrete- Region or Gradient models. The critical conductivities for activation for the Discrete- Region and Gradient models, under the linear conductivity profile were also \(\sim 10\%\) lower than those required under the uniform conductivity profile. There was no significant difference in the critical conductivity required for activation of

> **Image description.** This image is a scientific figure consisting of a 2x2 grid of line graphs, illustrating simulated Action Potential (AP) waves for a Discrete-Region model of SAN (Sinoatrial Node) heterogeneity under various conditions.
>
> The figure is organized into four distinct panels, each representing a specific combination of conductivity profile (Uniform or Linear) and the presence of an Atrial Load (No Atrial Load or Atrial Load).
>
> **General Visual Characteristics:**
> All four panels are time-series plots. The horizontal axis (x-axis) in every panel is labeled "Time (s)" and ranges from 0.0 to 0.25 seconds. The vertical axis (y-axis) is unlabeled but represents the amplitude or voltage of the AP waves. Each panel displays multiple overlapping, smooth, and complex traces, representing the simulated wave propagation across the tissue.
>
> **Panel Breakdown:**
>
> 1.  **Panel (a) - Top Left:**
>     *   **Conditions:** Uniform Conductivity Profile, No Atrial Load.
>     *   **Visual Content:** Shows multiple AP wave traces under uniform conductivity without the influence of the atrial load. The waves exhibit a consistent, smooth pattern across the time domain.
>
> 2.  **Panel (b) - Top Right:**
>     *   **Conditions:** Uniform Conductivity Profile, Atrial Load.
>     *   **Visual Content:** Shows multiple AP wave traces under uniform conductivity, but in the presence of the Atrial Load. The traces appear slightly altered compared to Panel (a), reflecting the impact of the added load.
>
> 3.  **Panel (c) - Bottom Left:**
>     *   **Conditions:** Linear Conductivity Profile, No Atrial Load.
>     *   **Visual Content:** Shows multiple AP wave traces under a linear conductivity profile without the Atrial Load. The wave shapes and patterns differ from those in Panel (a), consistent with the varying conductivity across the tissue.
>
> 4.  **Panel (d) - Bottom Right:**
>     *   **Conditions:** Linear Conductivity Profile, Atrial Load.
>     *   **Visual Content:** Shows multiple AP wave traces under a linear conductivity profile in the presence of the Atrial Load. This panel combines the effects of both the linear conductivity and the atrial load.
>
> **Text and Labels:**
> The figure includes several labels and titles:
> *   The overall figure caption at the top reads: "Fig. 5. Simulated AP waveshapes for the Discrete-Region model of SAN heterogeneity, (a) and (c) in the absence and (b) and (d) in the presence of the atrial tissue load with the uniform [(a) and (b)] and linear [(c) and (d)] conductivity profiles. In each panel, the upper most trace corresponds to the center of the SAN and the moment of earliest activation has been aligned with t = 0.05 s."
> *   The top row of panels is labeled "Uniform Conductivity Profile."
> *   The bottom row of panels is labeled "Linear Conductivity Profile."
> *   The left column of panels is labeled "No Atrial Load."
> *   The right column of panels is labeled "Atrial Load."
> *   The x-axis label for all panels is "Time (s)."

<center>Fig. 5. Simulated AP waveshapes for the Discrete-Region model of SAN heterogeneity, (a) and (c) in the absence and (b) and (d) in the presence of the atrial tissue load with the uniform [(a) and (b)] and linear [(c) and (d)] conductivity profiles. In each panel, the upper most trace corresponds to the center of the SAN and the moment of earliest activation has been aligned with \(t = 0.05 \mathrm{~s}\) . </center>

the atrial tissue under the uniform and linear conductivity profiles for either the Mosaic- PA or Mosaic- CPA models.

### D. Pacemaker Activity in the 1-D SAN Models

Figs. 5- 9 illustrate the AP waveshapes for each of the models of SAN heterogeneity in the absence (left) and in the presence (right) of the atrial load, for both the uniform (top) and linear (bottom)

conductivity profiles. In the case of the uniform conductivity profile, the SAN conductivity \((\sigma_{s})\) was set to \(25 \mu \mathrm{S} \cdot \mathrm{mm}^{- 1}\) . Under the linear conductivity profile, the conductivity was set to \(0.01 \mu \mathrm{S} \cdot \mathrm{mm}^{- 1}\) at the center of the SAN \((\sigma_{s - c})\) and \(25 \mu \mathrm{S} \cdot \mathrm{mm}^{- 1}\) at the periphery \((\sigma_{s - p})\) . These values for the conductivity were sufficient to achieve entrainment of the SAN region. In the presence of the atrial load, these values were also sufficient to drive the atrial tissue in all cases except the Mosaic- CA model. In the later

> **Image description.** A scientific figure consisting of a 2x2 grid of line graphs, labeled (a), (b), (c), and (d), illustrating simulated Action Potential (AP) waves for a "Gradient model of SAN heterogeneity." The graphs compare different conductivity profiles (Uniform vs. Linear) and conditions (No Atrial Load vs. Atrial Load).
>
> **Layout and Axes:**
> The figure is organized into four panels. All panels share a common horizontal X-axis labeled "Time (s)," which ranges from 0.0 to 0.25. The vertical Y-axis is unlabeled but represents the AP wave shape or potential.
>
> **Panel Descriptions:**
> *   **Top Row (Uniform Conductivity Profile):**
>     *   **Panel (a) - No Atrial Load:** Displays multiple smooth, overlapping traces representing AP waves. The waves begin around $t=0.05$ s and spread across the time axis, showing a typical, gradual depolarization and repolarization pattern.
>     *   **Panel (b) - Atrial Load:** Also displays multiple traces, similar in general shape to Panel (a), but the wave propagation appears slightly more constrained or rapid compared to the "No Atrial Load" condition.
>
> *   **Bottom Row (Linear Conductivity Profile):**
>     *   **Panel (c) - No Atrial Load:** Shows traces that are visually similar to those in Panel (a), maintaining a smooth, spreading wave pattern.
>     *   **Panel (d) - Atrial Load:** This panel exhibits a distinct visual difference from the others. The traces are tightly clustered and show a significantly steeper and more rapid initial depolarization (a sharper rise) compared to the other three panels, suggesting a more constrained or accelerated wave front under the linear profile and atrial load.
>
> **Text and Caption:**
> The figure is titled "Gradient Model" at the top center. Below the four panels, the figure caption reads: "Fig. 6. Simulated AP waveshapes for the Gradient model of SAN heterogeneity, in the absence (a) and (c) and in the presence (b) and (d) of the atrial tissue load with the uniform [(a) and (b)] and linear [(c) and (d)] conductivity profiles. In each panel, the upper most trace corresponds to the center of the SAN and the moment of earliest activation has been aligned with $t = 0.05$ s."
>
> The overall visual presentation is a comparative study using line graphs to demonstrate how changes in conductivity profiles and the presence of atrial load affect the simulated propagation of action potentials.

<center>Fig. 6. Simulated AP waveshapes for the Gradient model of SAN heterogeneity, in the absence (a) and (c) and in the presence (b) and (d) of the atrial tissue load with the uniform [(a) and (b)] and linear [(c) and (d)] conductivity profiles. In each panel, the upper most trace corresponds to the center of the SAN and the moment of earliest activation has been aligned with \(t = 0.05\) s. </center>

case, activation of the atrial tissue was not observed at any value of the SAN conductivity with the uniform conductivity profile. Furthermore, these values for the conductivity yield a CV in the SAN region on the order of \(0.1\mathrm{m}\cdot \mathrm{s}^{- 1}\) , comparable to that observed in the intact SAN of the rabbit [1].  

Curiously, we see in Fig. 5 that even in the absence of the atrial load, the Discrete- Region model exhibits a point of earliest activation not at the periphery of the SAN but partway between the center and the periphery. This is despite the longer intrinsic CL of the central type cell model (0.477 s) compared to that of the peripheral type cell model (0.404 s). This behavior is due to the lower MDP of the central type cell model, which imposes a depolarizing influence on the peripheral type cells, accelerating diastolic depolarization of these peripheral cells and shortening the CL.

The entrained CL of the Discrete- Region model with the uniform conductivity profile ( \(\sigma_{s} = 25\mu \mathrm{S}\cdot \mathrm{mm}^{- 1}\) ) in the absence of

> **Image description.** A technical figure, Figure 7, consisting of four panels arranged in a 2x2 grid, illustrating simulated Action Potential (AP) waves for the Mosaic-PA model of SAN heterogeneity. The figure is titled "Mosaic-PA Model" and compares the effects of uniform versus linear conductivity profiles and the presence or absence of atrial tissue load.
>
> The overall structure is organized as follows:
> *   **Top Row:** Uniform Conductivity Profile (Panels a and b)
> *   **Bottom Row:** Linear Conductivity Profile (Panels c and d)
> *   **Left Column:** No Atrial Load (Panels a and c)
> *   **Right Column:** Atrial Load (Panels b and d)
>
> Each panel displays a set of overlapping line graphs representing the AP wave shape over time. The horizontal axis (X-axis) in all four panels is labeled "Time (s)" and ranges from 0.0 to 0.25 seconds. The vertical axis (Y-axis) is unlabeled but represents the magnitude of the AP wave.
>
> **Detailed Panel Descriptions:**
>
> 1.  **Panel (a) - Uniform Conductivity Profile, No Atrial Load:** This panel shows a cluster of AP wave traces. The waves exhibit a rapid initial rise followed by a decay. A small square inset in the upper right corner displays a grid of letters 'P' and 'A', representing the random cell type assignment (P = Peripheral SAN, A = Atrial type cells) within the simulated SAN region.
> 2.  **Panel (b) - Uniform Conductivity Profile, Atrial Load:** This panel also shows a cluster of AP wave traces. The overall shape is similar to Panel (a), but the traces appear slightly more dispersed. The corresponding inset in the upper right corner shows the same grid of 'P' and 'A' cell type assignments.
> 3.  **Panel (c) - Linear Conductivity Profile, No Atrial Load:** This panel displays AP wave traces that show a very sharp, distinct initial activation (a steep rise occurring around t = 0.05 s), followed by a more gradual decay. The traces are tightly clustered. The inset in the upper right corner shows the 'P' and 'A' cell type grid.
> 4.  **Panel (d) - Linear Conductivity Profile, Atrial Load:** This panel shows AP wave traces similar to Panel (c), characterized by a sharp initial activation. The overall pattern and spread of the traces are slightly different from Panel (c). The inset in the upper right corner shows the 'P' and 'A' cell type grid.
>
> In summary, the figure visually compares how the conductivity profile (uniform vs. linear) and the presence of atrial tissue load affect the simulated AP wave propagation in the Mosaic-PA model, with the cell type distribution shown in the insets of each panel.

<center>Fig. 7. Simulated AP waveshapes for the Mosaic-PA model of SAN heterogeneity, (a) and (c) in the absence and (b) and (d) in the presence of the atrial tissue load with the uniform [(a) and (b)] and linear [(c) and (d)] conductivity profiles. In each panel, the upper most trace corresponds to the center of the SAN and the moment of earliest activation has been aligned with \(t = 0.05\) s. The corresponding random cell type assignment for the computational nodes within the SAN region is shown inset, \(\mathrm{P} = \mathrm{Peripheral~SAN}\) and \(\mathrm{A} = \mathrm{Atrial~type~cell~models}\) . </center>

the atrial load was 0.381 s, shorter than the intrinsic CL of both the central and peripheral type cell models. This shortening of the entrained CL was also observed in the Mosaic- CP (0.362 s) and Mosaic- CPA (0.396 s) models (Figs. 8 and 9). The entrained CL for the Gradient and Mosaic- PA models shown in Figs. 6 and 7 were 0.412 s and 0.432 s respectively.  

Fig. 10 shows the CV as a function of position for each of the SAN models under both the uniform and linear conductivity profiles. In all models of SAN heterogeneity, under both the uniform and linear conductivity profiles, the CV in the SAN region was on the order of \(0.1 \mathrm{m} \cdot \mathrm{s}^{- 1}\) . Under the uniform conductivity profile, both the Gradient and Mosaic- CPA models exhibit a peak in the CV near \(l = 0.6 \mathrm{mm}\) , indicating that the AP is initiated almost simultaneously in a small region of tissue rather than at a single point. This peak in the CV was not observed with the linear conductivity profile. Both the Mosaic- PA and

> **Image description.** This image is a technical figure consisting of four line graphs arranged in a 2x2 grid, illustrating simulated Action Potential (AP) waves for the Mosaic-CP model of Sinoatrial Node (SAN) heterogeneity. The figure is titled "Fig. 8. Simulated AP waveshapes for the Mosaic-CP model of SAN heterogeneity..."
>
> The four panels are labeled (a), (b), (c), and (d) and are organized by conductivity profile (Uniform vs. Linear) and the presence of Atrial Load (No Atrial Load vs. Atrial Load).
>
> **Panel Arrangement and Labels:**
> *   **Top Row (Uniform Conductivity Profile):**
>     *   Panel (a): Labeled "Uniform" and "No Atrial Load."
>     *   Panel (b): Labeled "Uniform" and "Atrial Load."
> *   **Bottom Row (Linear Conductivity Profile):**
>     *   Panel (c): Labeled "Linear" and "No Atrial Load."
>     *   Panel (d): Labeled "Linear" and "Atrial Load."
>
> **Graph Details:**
> Each panel is a time-series plot.
> *   **X-axis:** Labeled "Time (s)," ranging from 0.0 to 0.25 seconds.
> *   **Y-axis:** Represents the AP wave shape (potential), though no specific units are provided.
> *   **Data Traces:** Each panel displays multiple overlapping traces, representing the AP waves of various computational nodes within the SAN region. The traces exhibit a characteristic wave pattern of depolarization, plateau, and repolarization. The context notes that the earliest activation is aligned with $t = 0.05$ s.
>
> **Visual Patterns and Differences:**
> *   **Uniform vs. Linear Profiles:** In the "No Atrial Load" panels (a and c), the traces in the Linear profile (c) show a more pronounced gradient or increase in the wave characteristics (CV) from the center to the periphery compared to the Uniform profile (a).
> *   **Atrial Load Effect:** Comparing the "No Atrial Load" panels (a and c) to their counterparts with "Atrial Load" (b and d), the presence of atrial load appears to alter the shape and timing of the AP waves, particularly near the SAN-Atrial border.
>
> **Inset Diagrams:**
> Each of the four panels contains a small inset diagram in the upper right corner, illustrating the cell type assignment for the computational nodes. This diagram uses two labels:
> *   $C = \text{Central SAN}$
> *   $P = \text{Peripheral SAN}$
> The arrangement of these labels visually represents the spatial distribution of cell types within the simulated SAN region.

<center>Fig. 8. Simulated AP waveshapes for the Mosaic-CP model of SAN heterogeneity, in the absence (a) and (c) and in the presence (b) and (d) of the atrial tissue load with the uniform (a) and (b) and linear (c) and (d) conductivity profiles. In each panel, the upper most trace corresponds to the center of the SAN and the moment of earliest activation has been aligned with \(t = 0.05\mathrm{~s~}\) . The corresponding random cell type assignment for the computational nodes within the SAN region is shown inset, \(C = \mathrm{Central~SAN}\) and \(\mathrm{P} = \mathrm{Peripheral~SAN}\) type cell models. </center>

Mosaic- CPA models displayed a gradual increase in CV from the center to the periphery of the SAN under the linear conductivity profile.  

It is interesting to note the marginally higher atrial CV, near the SAN- Atrial border, observed for the Discrete- Region, Gradient and Mosaic- CP models of SAN heterogeneity. In each of these configurations, the atrial tissue is driven by peripheral SAN type cells in the periphery of the SAN region. The peripheral SAN cells possess a longer APD than the adjacent atrial tissue and, therefore, supply additional depolarizing current to the atrial tissue region, resulting in a marginally higher CV. The increase in CV occurs only in the proximity of the SAN. In simulations involving an extended atrial tissue region (not shown), the CV in the atrial tissue decreased with distance from the SAN- Atrial interface, stabilizing at the intrinsic atrial value of \(\sim 0.5\mathrm{~m~}\cdot \mathrm{s}^{- 1}\) within approximately \(3\mathrm{~mm}\) .

> **Image description.** A composite figure consisting of four line graphs arranged in a 2x2 grid, titled "Mosaic-CPA Model," which illustrates simulated Action Potential (AP) waves under various conditions of conductivity profiles and atrial tissue load.
>
> The overall structure features four panels labeled (a), (b), (c), and (d). All panels share a common horizontal x-axis labeled "Time (s)," ranging from 0.0 to 0.25 seconds. The vertical axis represents the AP wave amplitude, though it is not explicitly labeled. Each panel displays multiple overlapping, fluctuating traces, representing the simulated AP waves across different computational nodes.
>
> The panels are organized as follows:
>
> *   **Top Row (No Atrial Load):**
>     *   **Panel (a):** Labeled "No Atrial Load" and associated with the "Uniform Conductivity Profile." It shows multiple AP wave traces propagating through the model. The traces appear relatively synchronized, with the earliest activation aligned near $t = 0.05$ s.
>     *   **Panel (b):** Labeled "Atrial Load" and associated with the "No Atrial Load" condition (top row). It displays AP wave traces, showing the effect of the added atrial tissue load on the wave propagation compared to panel (a).
>
> *   **Bottom Row (Linear Conductivity Profile):**
>     *   **Panel (c):** Labeled "Uniform Conductivity Profile" (bottom row) and associated with the "Linear Conductivity Profile." This panel shows AP wave traces where the propagation dynamics appear more varied or spread out compared to panel (a).
>     *   **Panel (d):** Labeled "Atrial Load" (bottom row) and associated with the "Linear Conductivity Profile." It displays AP wave traces under the combined influence of a linear conductivity profile and atrial tissue load.
>
> A consistent visual element across all four panels is a small inset grid located in the upper right corner of each graph. This inset represents the random cell type assignment for the computational nodes within the SAN region, using three distinct labels:
> *   **C:** Central SAN
> *   **P:** Peripheral SAN
> *   **A:** Atrial type cell models
>
> The figure provides a detailed visual comparison of how the AP wave propagation changes based on whether the conductivity profile is uniform or linear, and whether the model includes an atrial tissue load.

<center>Fig. 9. Simulated AP waveshapes for the Mosaic-CPA model of SAN heterogeneity, in the absence (a) and (c) and in the presence (b) and (d) of the atrial tissue load with the uniform [(a) and (b)] and linear [(c) and (d)] conductivity profiles. In each panel, the upper most trace corresponds to the center of the SAN and the moment of earliest activation has been aligned with \(t = 0.05\) s. The corresponding random cell type assignment for the computational nodes within the SAN region is shown inset, \(C = \text{Central SAN}\) , \(P = \text{Peripheral SAN}\) and \(A = \text{Atrial type cell models}\) . </center>

## IV. DISCUSSION  

As noted in the Section I, the primary aim of this paper is to identify which of the discrete- region, gradient or mosaic models best accounts for the heterogeneity observed in the SAN. In brief, all of the models except the Mosaic- CA model were able to achieve entrainment of the SAN and successfully excite the adjoining atrial tissue. However, the Mosaic- PA model was unable to reproduce the heterogeneity in AP waveshapes characteristic of the SAN. While both the Gradient and Mosaic- CP models produced a site of earliest activation consistent with observations in the SAN, the Gradient model was found to achieve frequency entrainment most easily. Furthermore, the uniform conductivity profile was found to promote entrainment within the SAN while the linear conductivity profile tended to assist propagation of the AP into the atrial tissue. These key points

> **Image description.** A multi-panel line graph consisting of two stacked plots, labeled (a) and (b), illustrating the relationship between conduction velocity and position for different models of SAN heterogeneity.
>
> **General Graph Features:**
> Both panels share identical axes and a legend.
> *   **Y-axis:** Labeled "Conduction Velocity (m/s)," with a scale ranging from 0.0 to 1.4.
> *   **X-axis:** Labeled "Position (mm)," with a scale ranging from 0 to 3.
> *   **Legend:** Located in the upper left of each panel, identifying four models: "Discrete-Region," "Gradient," "Mosaic-PA," and "Mosaic-CP." The models are represented by distinct line styles:
>     *   Discrete-Region: Solid line
>     *   Gradient: Dashed line
>     *   Mosaic-PA: Dotted line
>     *   Mosaic-CP: Dash-dot line
>
> **Panel (a): Uniform Conductivity Profile**
> This upper panel is titled "Uniform Conductivity Profile." It displays the conduction velocity across the position for the four models under a uniform conductivity condition. All four lines start at a similar velocity near 0.2 m/s at Position 0. As the position increases, the velocity generally decreases, but the decline is gradual. By Position 3, the velocities for all models have stabilized, ranging between approximately 0.6 m/s and 0.8 m/s. The lines are relatively close together throughout the plot.
>
> **Panel (b): Linear Conductivity Profile**
> This lower panel is titled "Linear Conductivity Profile." It shows the conduction velocity across the position for the same four models under a linear conductivity condition. Compared to Panel (a), the lines in this panel exhibit a much steeper decline. All models start near 0.2 m/s at Position 0, but the velocity drops significantly as the position increases. By Position 3, the velocities are much lower than in Panel (a), ranging between approximately 0.4 m/s and 0.6 m/s. The lines are more spread out, particularly at the beginning of the graph.
>
> **Figure Caption:**
> The caption below the graphs reads: "Fig. 10. Conduction velocity as a function of position for the different models of SAN heterogeneity. (a) under the uniform conductivity profile ($\sigma_{s} = 25.0 \mu \mathrm{S} \cdot \mathrm{mm}^{-1}$), and (b) under the linear conductivity profile ($\sigma_{s - c} = 0.01 \mu \mathrm{S} \cdot \mathrm{mm}^{-1}$ and $\sigma_{s - p} = 25.0 \mu \mathrm{S} \cdot \mathrm{mm}^{-1}$). Note the marginally higher atrial CV observed for the Discrete-Region, Gradient and Mosaic-CP models of SAN heterogeneity. The data shown here correspond to the last AP in the observation period. In the case of the mosaic models, the mean conduction velocity as a function of position is shown ($n = 10$)."

<center>Fig. 10. Conduction velocity as a function of position for the different models of SAN heterogeneity. (a) under the uniform conductivity profile \((\sigma_{s} = 25.0 \mu \mathrm{S} \cdot \mathrm{mm}^{-1})\) , and (b) under the linear conductivity profile \((\sigma_{s - c} = 0.01 \mu \mathrm{S} \cdot \mathrm{mm}^{-1}\) and \(\sigma_{s - p} = 25.0 \mu \mathrm{S} \cdot \mathrm{mm}^{-1})\) . Note the marginally higher atrial CV observed for the Discrete-Region, Gradient and Mosaic-CP models of SAN heterogeneity. The data shown here correspond to the last AP in the observation period. In the case of the mosaic models, the mean conduction velocity as a function of position is shown \((n = 10)\) . </center>

are developed in more detail below, followed by a brief discussion of the limitations of this paper.

### A. SAN-Atrial Conductivity Profiles  

In perhaps the earliest modeling study aimed at investigating the relationship between the structure and function of the SAN, Joyner and van Capelle [16] constructed a radially symmetric two- dimensional (2- D) model of the SAN and adjoining atrial tissue, somewhat analogous to the discrete- region model of SAN organization described above. They employed a single SAN cell type in the SAN region of their model, coupled to a region of atrial type tissue. In this simple approximation of the discrete- region model they investigated the effect of SAN size and SAN- Atrial coupling on the ability of the SAN to exhibit spontaneous pacemaker activity and also to drive the atrial tissue. Joyner and van Capelle reported that successful excitation of the atrial tissue required partial uncoupling of the SAN from the atrial tissue, either through a discrete "barrier" resistance or through a region of gradually increasing conductivity.

Winslow et al. [17] adjusted the parameters of the Noble- DiFrancesco- Denyer [18] model of a single SAN myocyte to produce AP waveshapes similar to those observed in the center and periphery of the SAN by Kodama and Boyett [1]. They employed these modified cell models in a large scale 2- D network model of the SAN with a smooth variation in intrinsic CL from the center to the periphery. In this simple gradient model, the AP was initiated in the periphery of the SAN and propagated inwards to the center. When embedded in a larger atrial network, the site of initial activation shifted from the periphery toward the center of the SAN as observed experimentally by Kirchhof et al. [13]. The Winslow et al. model assumed a common uniform conductivity throughout both SAN and atrial tissue regions and although the SAN was able to successfully excite the atrial tissue, the model was unable to reproduce the higher conduction velocity observed experimentally in atrial tissue compared to that in the SAN.

Zhang et al. [19] developed new mathematical models of central and peripheral SAN myocytes and formulated a 1- D gradient model of the SAN. Garny et al. [20] recently published a number of changes to Zhang's original 1- D gradient model. In this corrected 1- D model of the SAN, APs were initiated in the periphery of the SAN region in the absence of the atrial tissue load. However, with its default parameters, the model was unable to reproduce the shift in the site of earliest activation from the periphery to the center of the SAN region in the presence of an atrial load. It should be noted, however, that Garny et al. used conductivity values based on gap- junction experiments in rabbit SAN and atrial cell pairs [21], [22]. This may underestimate the conductivity in- vivo, since cells communicate with more than one neighbor.

In this paper, we have employed two different conductivity profiles within the SAN region of our 1- D models. The first assumes a uniform conductivity throughout the SAN region and is consistent with electron microscopic studies of gap junction density in the SAN and the adjoining atrial tissue. Masson- Pevet et al. [12] estimated the density of gap junctions in the SAN to be roughly 10 times lower than that in the adjacent atrial tissue. The second conductivity profile assumes a linear increase in conductivity from the center to the periphery of the SAN region. A gradient in coupling was first hypothesized by Joyner and van Capelle, and a gradient similar to that employed in this paper was recently employed in the 1- D model formulated by Garny et al. [20]. Though the underlying mechanism is not yet clear, there exists sufficient experimental evidence to surmise such a gradient in conductivity [11]. Both the uniform and linear conductivity profiles employed in this paper include a step change in conductivity at the SAN- Atrial boundary, consistent with the experimental observation of Oosthoek et al. [23] who reported an abrupt increase in gap junction density at the periphery of the SAN.

We found that for each of the different models of SAN heterogeneity, the linear conductivity profile resulted in greater dispersion of activation time and marginally lower CV in the SAN. Based on our results in Tables 1 and II, we note that the

uniform conductivity profile favors frequency entrainment of SAN myocytes while the linear conductivity profile marginally favors propagation of the AP from the SAN into the atrial tissue. This is broadly consistent with the results of the modeling study by Joyner and van Capelle [16] who reported that partial uncoupling of the SAN from the atrial tissue, either through a discrete "barrier" resistance or through a region of gradually increasing conductivity, was required for successful excitation of the atrial tissue. Joyner and van Capelle also noted that a gradual transition in conductivity between the SAN and atrial regions allowed a smaller SAN region to successfully drive the atria than was the case for a discrete barrier resistance. Although we report qualitatively similar results, we note that in this paper, the atria could be successfully driven even with the uniform conductivity profile.

### B. Pacemaker Activity

Similar to the modeling study by Joyner and van Capelle [16], we observed three states of activity in which the SAN was either: completely quiescent, spontaneously active but unable to excite the atria, or spontaneously active and able to successfully excite the atrial tissue.

The Mosaic- CA model involving central SAN and atrial type cell models was found to be untenable, largely failing to maintain spontaneous activity and drive the atrial tissue. Under the uniform conductivity profile, at low vales of \(\sigma_{s}\) , the central SAN cells fired spontaneously, but were unable to activate the interspersed atrial cells. As \(\sigma_{s}\) was increased, atrial cells in the central portion of the SAN, where the proportion of such cells was relatively low, were stimulated to threshold, eliciting APs. However, automaticity of the cells in the periphery of the SAN, where the proportion of atrial cells was considerably higher, was increasingly suppressed as \(\sigma_{s}\) was increased. With the uniform conductivity profile, only 2 of the 10 random cell type distributions of the Mosaic- CA model were capable of entrained pacemaker activity.

We found that the Discrete- Region, Gradient, Mosaic- PA, Mosaic- CP and Mosaic- CPA models were all able to achieve coordinated activation of the entire SAN region and initiate APs in the adjoining atrial tissue region as shown in Figs. 5- 9. In the mosaic models, peripheral SAN myocytes were found to be better suited to driving the interspersed atrial cells than the central SAN myocytes. A similar result was reported by Zhang et al. when using their central and peripheral SAN cell models together with an atrial cell model to formulate mosaic models of the SAN [24].

### C. Site of Earliest Activation

In both the Gradient and Mosaic- CP models, under both the uniform and linear conductivity profiles, the site of earliest activation was located at the SAN- Atrial boundary in the absence of the atrial load. In the presence of the atrial load, the site of earliest activation was shifted away from the periphery and toward the center of the SAN. This is consistent with the experimental observations by Kirchoff et al. [13]. In contrast, the site of earliest activation in the Mosaic- PA model was located at the center of the SAN under both the uniform and linear conductivity profiles and was unaffected by the atrial load.

As noted in the results, for the Discrete- Region and Mosaic- CPA models, the more positive MDP of the central SAN cells has a depolarizing effect on adjacent peripheral SAN cells. This accelerates the diastolic depolarization of the peripheral cells and shortens the entrained CL. As a result, the site of initial activation lies at an intermediate point between the center and periphery of the SAN region. The shortening of the entrained CL in the 1- D model is in contrast to the entrained CL observed when a single central SAN cell model is coupled to a single peripheral SAN cell model, where the entrained CL lies somewhere between the two intrinsic CLs [2].

Activation maps from the intact SAN suggest that the site of earliest activation lies in a region of SAN tissue with intermediate AP waveshape characteristics [25]. This is consistent with the behavior observed in the Discrete- Region, Gradient, Mosaic- CP and Mosaic- CPA models of this paper. We also observed slow conduction from the primary pacemaker site back toward the center ( \(l = 0\) ) of the SAN (Fig. 10). This is comparable to the slow conduction observed experimentally in the intact SAN in the direction of the interatrial septum [25]. It, therefore, seems plausible that the characteristic spread of excitation from the SAN may at least in part be due to the regional distribution of cell types in and around the SAN. This is consistent with the view that the block zone on the septal side of the SAN is due to a region of cells exhibiting low excitability [9], [25]. It also suggests that central SAN cells in or adjacent to the block zone may play an important role in normal pacemaker function by acting as a current source supplying current to the primary pacemaker site.

### D. Preservation of Action Potential Heterogeneity

Kirchhof et al. [13] reported that dissecting away the atrial tissue from the SAN resulted in a decrease in CL and a shift of the dominant pacemaking site away from the center and toward the periphery of the SAN. This appeared to be at odds with observations made in the intact SAN and provided evidence that the observed AP waveshape of a cell is determined not only by the intrinsic dynamics of the cell membrane, but is also at least partially influenced by the electrotonic interaction with neighboring cells. In the discrete- region model of the SAN, the observed heterogeneity in AP waveshape was, therefore, attributed to the electrotonic load imposed on the SAN by the surrounding more hyperpolarized atrial tissue.

Though not the primary focus of that study, the discrete- region model of Joyner and van Capelle [16] appeared to exhibit a central- peripheral variation in SAN AP waveshapes at least qualitatively consistent with that observed in the intact SAN. This variation in AP waveshape was due entirely to the electrotonic influence of the quiescent atrial tissue region.

Using their models of central and peripheral SAN myocytes, Zhang et al. [24] also formulated 2- D mosaic models of central and peripheral SAN tissue. They randomly assigned either SAN or atrial cell membrane properties to each node in the central and peripheral network models according to the proportions reported by Verheijck et al. [4], although they incorrectly assigned a higher proportion of atrial cells in the center of the node (41%) compared with the data of Verheijck et al. (22%). Zhang et al.

concluded that the mosaic model of the SAN could not account for the observed heterogeneity in AP characteristics [24].

In this paper, we have employed single SAN cell models capable of reproducing in isolation the experimental AP recordings from the center and periphery of the SAN. The Discrete- Region, Gradient, Mosaic- CP, and Mosaic- CPA models all displayed AP warehouses characteristic of both the center and periphery of the SAN. However, the Mosaic- PA variation of the mosaic model contained no central SAN cells and was, therefore, unable to produce AP warehouses characteristic of the central region of the SAN.

### E. Entrainment of the SAN and Activation of the Atrial Tissue

The Gradient model of SAN heterogeneity was found to achieve frequency entrainment of the SAN considerably more easily than either the Discrete- Region or the mosaic models. However, in terms of the critical conductivity for activation of the atrial tissue region, there was little to distinguish between the different models. This was true for both the uniform and the linear conductivity profiles, although the linear conductivity profile slightly favored activation of the atrial tissue. This suggests that successful propagation of the AP from the SAN into the atrial tissue is largely independent of the nature of the heterogeneity within the SAN. Considering all of the results together, the Gradient model of SAN heterogeneity, with the uniform conductivity profile, was most able to achieve frequency entrainment and successfully drive the atrial tissue.

### F. Limitations of the Present Study

Based on the results presented above, and the points already noted in the discussion, it seems that the Gradient model with the uniform conductivity profile represents the most plausible model of heterogeneity in the SAN. Yet, conventional wisdom suggests that the site of earliest activation in the presence of the atrial load [see Fig. 6(b)] should lie at the center of the SAN region, i.e., at \(l = 0\) . The apparent off- center site of pacemaker initiation in Fig. 6(b) may be reconciled by noting that the upstroke velocity of the central cells is slower than cells off- center. It is difficult to compare activation times in cells with markedly differing upstroke rates, in order to determine which is activated first. The important observation, as noted above, is that the site of initial activation shifts toward the center in the presence of the atrial tissue load, in accordance with experimental observations.

In the simulations involving the linear conductivity profile, the conductivity at the center of the SAN region \((\sigma_{s - c})\) , is lower than might be expected in the SAN. However, the value for \(\sigma_{s - c}\) was chosen to facilitate differentiation between the different models based on their ability to achieve frequency entrainment under the linear conductivity profile. The AP warehouses illustrated in Figs. 5- 9 for the linear conductivity profile, therefore, represent an extreme of the behavior expected of the different models in the presence of a gradient in conductivity. As can be seen in these figures, increasing \(\sigma_{s - c}\) , even to the value corresponding to the uniform conductivity profile, has only a marginal effect on both the site of earliest activation and the observed AP warehouses.

In their study of gap junction distribution in the SAN, Osthoek et al. [23] observed small bundles of nodal cells penetrating the atrial myocardium. Inspired by this tissue architecture, Noble and Winslow [26] formulated a 2- D network model of the rabbit SAN and surrounding atrial tissue. This model incorporated fingers of SAN tissue extending from the periphery of the SAN into the surrounding atrial tissue region. They demonstrated that the interdigitation of SAN and atrial tissue provided a viable mechanism to prevent suppression of spontaneous activity in the SAN and facilitate propagation of the activation wavefront from the SAN into the surrounding atrial tissue. The results of Noble and Winslow highlighted the potential importance of tissue geometry in facilitating propagation of the AP from the SAN into the atrial tissue. In the 1- D models described above, it was not possible to model different geometric configurations. Nevertheless, we were able to achieve activation of the atrial tissue, in the presence and absence of a gradient in conductivity, in all but the Mosaic- CA model. Furthermore, a 1- D model may serve as a reasonable approximation of a radially symmetric 2- D model of comparable dimension [16], [19]. Therefore, given the reduced computational demands compared to higher dimensional models, the 1- D model described here provides a viable tool for the investigation of SAN function. The use of a 1- D model in this paper also facilitates a direct comparison with 1- D modeling studies reported by others (e.g., [19] and [20]).

## V. CONCLUSION

We have previously demonstrated that heterogeneity in AP warehouse assists frequency entrainment of electrically coupled pacemaker cell pairs [2]. In this paper we have investigated a number of different conceptual models of SAN heterogeneity using detailed ionic models of electrical activity in SAN and atrial myocytes. To our knowledge, this represents the first attempt to formulate and compare each of the different models of SAN heterogeneity.

A total of six different 1- D models of SAN heterogeneity were formulated, namely the Discrete- Region, Gradient, Mosaic- CA, Mosaic- PA, Mosaic- CP and Mosaic- CPA models. Each of the different models were assessed on their ability to achieve frequency entrainment of the SAN and activation of the adjoining atrial tissue.

We observed that both the Gradient and Mosaic- CP models displayed AP warehouses characteristic of central and peripheral SAN myocytes, and displayed a shift in the site of earliest activation from the periphery toward the center of the SAN in the presence of the atrial load. Both the Gradient and Mosaic- CP models would, therefore, appear to produce behavior consistent with experimental observations in the intact SAN. The Gradient model achieved frequency entrainment considerably more easily than the other models of SAN heterogeneity, including the Mosaic- CP model. In contrast, SAN heterogeneity appears to play only a minor role in facilitating propagation of the AP from the SAN into the atrial tissue.

We observed that a uniform conductivity throughout the SAN significantly promoted frequency entrainment of the SAN while

a gradual increase in conductivity from the center to the periphery of the SAN marginally promoted propagation of the AP from the SAN into the atrial tissue. Based on these results, the gradient model of SAN heterogeneity with a uniform SAN conductivity is the most likely model of SAN organization, able to qualitatively reproduce known behavior of the intact cardiac pacemaker.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
