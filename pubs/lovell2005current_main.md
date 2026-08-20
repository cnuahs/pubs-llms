```
@article{lovell2005current,
  title={Current Distribution During Parallel Stimulation: Implications for an Epiretinal Neuroprosthesis},
  author={Nigel H. Lovell and Socrates Dokos and Shaun L. Cloherty and Philip Preston and Gregg J. Suaning},
  journal={27th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2005},
  pages={5242-5245},
  doi={10.1109/iembs.2005.1615661},
  url={https://ieeexplore.ieee.org/document/1615661}
}
```

---

# Current Distribution During Parallel Stimulation: Implications for an Epiretinal Neuroprosthesis

N.H. Lovell \(^{1,2}\) , S. Dokos \(^{1}\) , S.L. Cloherty \(^{1,3}\) , P.J. Preston \(^{1}\) , G.J. Suaning \(^{3}\)

\(^{1}\) Graduate School of Biomedical Engineering, University of New South Wales, Sydney, Australia \(^{2}\) National Information Communications Technology Australia (NICTA) \(^{3}\) School of Engineering, University of Newcastle, Newcastle, Australia

Abstract- A simplified mathematical model has been developed in order to better understand local current spread when multiple simultaneous current sources are used in an epiretinal neuroprosthesis. To test the model, pairs of platinum electrodes of \(430 \mu \mathrm{m}\) diameter and an intra- pair spacing of \(1 \mathrm{mm}\) between centers, were arranged either in- line or in parallel, in a bath of physiological saline. Each pair was separated by distances from \(1 \mathrm{mm}\) to \(6 \mathrm{mm}\) . The currents in each electrode in the bath were measured and compared with the computational model of the same arrangement. This approach allowed us to quantify return current interaction between parallel sources. As predicted, with parallel electrodes and matching currents in each electrode pair, there is no current cross- talk. However with imbalanced current sources, significant cross- talk is evident. The cross- talk decreases as a function of electrode pair separation. The implication of this work in the design of an epiretinal neuroprosthesis is discussed.

Keywords - vision prosthesis, modeling, current source, retina, neurostimulation

## I. INTRODUCTION

The concept of charge injection causing a localized voltage gradient that is capable of depolarizing excitable tissue to threshold, is well understood. Less researched and reported is the interaction of concurrent charge injection from multiple sources. The reason behind this is that many organ systems in which neurostimulation is used do not benefit greatly from parallel stimulation strategies.

Past research in the area of epiretinal vision prosthetics by our group [1] and others [2] has adopted the traditional single current source approach. However, recent work by ourselves [3- 5] and others [6] has reported alternate stimulation paradigms that could be incorporated into an intra- ocular implant for epiretinal stimulation. This approach has been pioneered by other researchers [7, 8] in the vision prosthetics area that are working on subretinal implants, owing to the inherent parallel design of the photodetector- electrode elements.

There is a need to investigate parallel stimulation in the neural retina. This is the way the retina works in its normal

physiological function. An epiretinal device capable of providing meaningful visual percepts, will require electrode numbers and communications bandwidth that far exceed that possible by multiplexing a single current across the requisite number of electrodes.

In this paper, as a first step towards greater understanding of parallel stimulation, we model the flow of current between electrode pairs arranged in different orientations and with differing separations. These models are compared with measurements taken with platinum electrodes immersed in a bath of physiological saline.

## II. METHODS

### A. Computational Model

In order to examine the current flows and voltage gradients of an electrode array immersed in a thin layer of physiological saline (dimensions \(20 \times 20 \times 0.2 \mathrm{mm}\) ), a computational model was developed as described previously [5]. In brief, the model was formulated using pairs of cylindrical electrodes of \(430 \mu \mathrm{m}\) diameter with the voltage distribution, \(V\) , throughout the saline region governed by the Poisson equation

\[- \nabla .(\sigma \nabla V) = I \quad (1)\]

where \(\sigma\) is the conductivity of the medium and \(I\) is the volume current density injected into the medium at the given location [9]. For physiological saline, \(\sigma\) was taken to be \(1 \mathrm{~S / m}\) [10]. Capacitive effects of the electrode- electrolyte bilayer were ignored.

By using assuming a cylindrical electrode geometry and a constant conductivity \((\sigma)\) , equation (1) was reduced to the 2D partial differential system

\[\frac{\partial^2 V(x,y)}{\partial x^2} +\frac{\partial^2 V(x,y)}{\partial y^2} = -\frac{i_n^m}{\sigma\pi^2h} \quad (2)\]

within the \(n\) th stimulus electrode

\[\frac{\partial^2 V(x,y)}{\partial x^2} +\frac{\partial^2 V(x,y)}{\partial y^2} = -\frac{i_n^m}{\sigma\pi^2h} \quad (3)\]

within the \(m\) th return electrode

\[\frac{\partial^2 V(x,y)}{\partial x^2} +\frac{\partial^2 V(x,y)}{\partial y^2} = 0 \quad (4)\]

outside all electrodes, and

\[V(x_{c},y_{c}) = 0 \quad (5)\]

at all return electrode center coordinates \((x_{c},y_{c})\)

In equations (2) and (3), \(i_{s}^{n}\) is the absolute value of the current injected into the \(n\) th stimulus electrode, \(i_{r}^{m}\) is the absolute value of current returned from the \(m\) th return electrode, and \(r\) and \(h\) are the radius and height of the electrode cylinders. In general, the injected currents \((i_{s}^{n})\) are given, whereas the return currents \((i_{r}^{m})\) are unknown when there is more than one return electrode. These return currents can be determined from the additional constraint given by equation (5). Zero- flux boundary conditions, \(\frac{\partial V}{\partial x} = 0,\quad \frac{\partial V}{\partial y} = 0\) , were imposed on the edges of the domain.

Small rectangular regions were used to enclose each circular electrode, the spaces between electrodes, and the spaces between electrodes and the domain boundary. The voltage at each node was determined by inverting the system of differentiation matrices. The system of equations were solved in MATLAB (The MathWorks Inc.) using a spectral collocation method [11].

Injecting and return electrodes in each pair were always separated by a distance \(p\) of \(1\mathrm{mm}\) . Pairs of electrodes were then arranged either in- line (zero degrees) in the \(x\) direction or in parallel in the \(y\) direction, separated by distances of 1 mm to \(6\mathrm{mm}\) in \(1\mathrm{mm}\) increments.

A stimulus current of \(1\mathrm{mA}\) (DC) was always injected in the first electrode pair. In the second pair, simulations were performed with injection currents of 1.0, 0.5, 0.25 and \(0.1\mathrm{mA}\) . The current cross- talk in the second return electrode was calculated as the percentage deviation from the nominal current injected from its corresponding electrode pair. Thus if \(0.1\mathrm{mA}\) was injected but \(0.15\mathrm{mA}\) returned due to cross- talk from the first electrode pair, then the cross- talk would be \(50\%\) .

### B. Experimental Measurements

To verify the model, saline bath tests were conducted using similar electrode configurations to the model. It was not possible to readily create the cylindrical platinum electrodes employed in the simplified 2D model, so platinum ball electrodes [12] were arranged on a circuit board and immersed in a thin layer of physiological saline (Fig. 1). The electrodes were covered with a glass coverslip in order to control the height of saline above the electrodes.

A \(1\mathrm{kHz}\) sinusoidal stimulus current with RMS amplitudes similar to those used in the mathematical model was employed. In order to test repeatability, three separate bath measurements were taken at each electrode position and current amplitude. In the graphs of these data, points are shown as mean \(\pm \mathrm{SEM}\) .

> **Image description.** A technical diagram illustrating the arrangement of multiple circular electrodes within a simulated domain, likely representing an experimental setup for electrical stimulation.
>
> The image features a light gray background containing several circular electrode representations, which are arranged in pairs and grouped horizontally. These electrodes are labeled with alphanumeric identifiers: L1, I1, L2, I2, P1, and P2.
>
> The electrodes are organized into distinct pairs:
> 1.  The pair (L1, I1) is located on the left.
> 2.  The pair (L2, I2) is located in the center-right.
> 3.  The pair (P1, P2) is located further to the right.
>
> The diagram uses colored ovals to highlight specific electrode pairs or regions of interest:
> *   **Yellow Ovals:** Two yellow oval shapes are used to highlight the pairs (L1, I1) and (L2, I2). These ovals encompass the two circular electrodes in each respective pair.
> *   **Red Ovals:** Two red oval shapes are used to highlight the pairs (I1, P1) and (I2, P2). These ovals also encompass the two circular electrodes in each respective pair.
>
> The arrangement suggests a linear array of electrode pairs, with the different colors (yellow and red) likely indicating different functional roles or measurement zones within the simulation, such as stimulus injection versus return current monitoring, as suggested by the surrounding technical context. The overall composition is clean and schematic, typical of a scientific visualization used to define the geometry of a computational model.

<center>Figure 1. Picture of a section of the saline bath comprising platinum ball electrodes mounted on a circuit board. Electrodes are then covered with a thin layer of physiological saline and then by a glass cover-slip. Injecting electrodes are labeled 11 and 12. In 'parallel' orientation the two return electrodes are P1 and P2. Electrodes L1 and L2 are used for 'in-line' orientation. To increase effective electrode separation the right-hand electrodes are moved one position to the right (electrodes not shown in this cutaway picture). </center>

## III. RESULTS AND DISCUSSION

Fig. 2 demonstrates simulation and measured results from the electrode pairs. As can be predicted theoretically, with a parallel orientation and equal injection currents, the cross- talk is zero. However, if the injected currents are not identical then the return electrode (associated with the injecting electrode that has the lower current), receives considerably more current, particularly at closer separations.

Model and measured results are in qualitative agreement. The model tends to over- predict the current cross- talk, particularly at higher current imbalances. This is likely due to the simplification in the model that the electrodes were cylindrical and that there was no saline above the electrodes. Indeed the model assumes no current flow in the z- direction. In the experiment, a thin layer of saline was present above the electrodes and the electrodes themselves were effectively hemispherical in shape. The layer of saline would promote current return in the closer paired return electrode.

There is considerable similarity between the parallel and in- line data. The electrode configurations in Fig. 2 are symmetrical. However, for the in- line orientation, when the return electrode is always to the left (or right) of the injecting electrode, then considerably different results are apparent with increased cross- talk at matching currents and reduced cross- talk (compared with symmetrical configurations) when mismatched currents are injected.

Fig. 3 illustrates the modeled voltage gradients for parallel electrodes separated by \(3\mathrm{mm}\) . The left panel is for matching \((1.0 / 1.0\mathrm{mA})\) currents. The asymmetry of the voltage profile is obvious in the right panel where the injected currents are mismatched \((1.0 / 0.1\mathrm{mA})\) .

> **Image description.** A composite figure consisting of four line graphs, labeled (A), (B), (C), and (D), which illustrate the percentage of leakage (cross-talk) in a second return electrode as a function of electrode separation, comparing theoretical models to measured experimental results.
>
> **General Structure and Axes:**
> All four panels share a similar structure. The horizontal X-axis in every graph is labeled "Electrode Separation (mm)" and ranges from 1 to 6. The vertical Y-axis in every graph is labeled "% Leakage (Electrode 2)" and ranges from -50 to 400. Each graph displays four distinct lines, representing different injection currents: 1.0 mA (solid line), 0.5 mA (dashed line), 0.25 mA (dotted line), and 0.1 mA (dash-dot line).
>
> **Panel (A): Model - Parallel Orientation (return electrode below)**
> This panel shows the theoretical results for electrodes arranged in parallel with the return electrode positioned below. The lines exhibit a clear downward trend as the electrode separation increases. The 1.0 mA current consistently results in the highest percentage of leakage, while the 0.1 mA current results in the lowest.
>
> **Panel (B): Model - In-line Orientation (return electrode outside)**
> This panel presents the theoretical results for electrodes arranged in an in-line configuration with the return electrode positioned outside. Similar to Panel (A), all four lines show a general downward trend as the electrode separation increases. The 1.0 mA line remains the highest, and the 0.1 mA line remains the lowest.
>
> **Panel (C): Measured - Parallel Orientation (return electrode below)**
> This panel displays the measured experimental results for the parallel orientation. Compared to the model in Panel (A), the lines in Panel (C) are generally flatter, indicating less sensitivity to electrode separation. Data points in this panel include visible error bars, representing experimental variability.
>
> **Panel (D): Measured - In-line Orientation (return electrode outside)**
> This panel shows the measured experimental results for the in-line orientation. Similar to Panel (C), the lines are relatively flat, showing only a slight decrease in leakage as separation increases. Error bars are visible on the data points, indicating the measured variability.
>
> **Summary of Visual Patterns:**
> The graphs visually demonstrate that for both model and measured data, increasing the electrode separation generally reduces the percentage of leakage. Furthermore, across all configurations, the magnitude of leakage is directly proportional to the injected current, with the 1.0 mA injection consistently producing the highest leakage percentage. The measured results (C and D) show less dramatic changes with separation compared to the theoretical models (A and B).

<center>Figure 2. Cross-talk in second (right-hand) return electrode (expressed as a percentage of the nominal injected current) when injecting concurrently into two separate electrodes arranged in different orientations. 1.0 mA was always injected in the left electrode pair, while the right-hand electrode pair had varying injection currents of 1.0, 0.5 0.25 and 0.1 mA. (A) Results from model with electrodes arranged in parallel. (C) Results from model with electrodes arranged in-line. (B) Measured results with same electrode configuration as in (A). (D) Measured </center>

> **Image description.** A pair of side-by-side heat map plots, likely representing voltage gradients or cross-talk measurements in a two-dimensional spatial domain. Both plots utilize a color gradient to represent the magnitude of a measured quantity, with red indicating high values and blue indicating low values.
>
> **Common Features:**
> *   **Axes:** Both panels share identical coordinate systems. The horizontal (X) and vertical (Y) axes range from -0.01 to 0.01.
> *   **Color Mapping:** Both plots use a continuous color scale. The lowest values are represented by dark blue/cyan, while the highest values are represented by dark red.
>
> **Left Panel:**
> *   **Color Scale:** The scale ranges from 0 (dark blue) to 3 (dark red).
> *   **Visual Pattern:** The plot displays a central region of high intensity (red and orange), which is somewhat elongated and appears to consist of two adjacent, high-value peaks. This central high-value area is surrounded by a transition zone of yellow and green, which gradually fades into the lowest values (blue) at the edges of the plot.
>
> **Right Panel:**
> *   **Color Scale:** The scale ranges from 0 (dark blue) to 2.5 (dark red).
> *   **Visual Pattern:** Similar to the left panel, this plot shows a central region of high intensity (red and orange). However, the high-value area appears more concentrated and slightly more symmetrical compared to the left panel, with the transition to the surrounding lower values (blue) occurring more sharply.
>
> The overall visual presentation suggests a comparison between two different experimental conditions or models, as indicated by the differences in the maximum values on the color scales (3 vs. 2.5) and the subtle variations in the shape and distribution of the central high-intensity regions.

<center>Figure 3. Voltage gradients (V) for electrode pairs immersed in the 20 mm by 20 mm bath of physiological saline. Electrodes are arranged in parallel with a 3 mm separation. In both panels 1 mA is injected in the left electrode pair. In the left panel, 1.0 mA was also injected in the right electrode pair. In the right panel, 0.1 mA was injected in the right electrode pair. Injecting electrodes are drawn as white circles and return electrodes as black circles. Bath dimensions are in meters. </center>

In a vision prosthesis there is a need to accurately inject and recover charge from various regions of the neural retina - hence charge recovery and controlling and localizing charge injection are obviously of considerable importance.

These results demonstrate that in the design of a retinal neuroprosthesis employing multiple current sources, careful attention must be paid to electrode orientation and stimulation paradigms. One possible approach is to employ an electrode configuration that reduces current cross- talk. Hexagonal arraying of electrodes is the subject of on- going research in our laboratory [13].

An alternate approach is to use a distant return electrode (monopolar stimulation) [14]. This requires further detailed examination, however, the bipolar approach investigated herein, has the appealing advantage that it does not require a breach of the scleral wall in order to implement - the entire device can be implanted intra- ocularly. Such breaches can lead to complications arising from long- term fixation and possible infection.

## IV. CONCLUSION

While there is concerted research in retinal neuroprostheses, there is very little published on concurrent stimulation of retinal tissue - or for that matter excitable tissue in general.

The models presented here are basic in that they do not consider the capacitive properties of the electrode- electrolyte interface, nor the known changes in bulk conductivity that occur between saline and the layers of the retina (as would exist with electrodes in close apposition with the neural retina). Despite this, the models highlight the need for a thorough examination of these effects in the retina.

We are currently combining the models of current injection with neural models of retinal tissue to create a bidomain model capable of simulating activation of retinal ganglion cells [15]. With additional modeling of distant return paths, the possible benefits of monopolar versus bipolar stimulation could also be investigated.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
