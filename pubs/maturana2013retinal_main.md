```
@article{maturana2013retinal,
  title={Retinal ganglion cells electrophysiology: The effect of cell morphology on impulse waveform},
  author={Matias I. Maturana and Raymond C. S. Wong and Shaun L. Cloherty and Michael R. Ibbotson and Alex E. Hadjinicolaou and David B. Grayden and Anthony N. Burkitt and Hamish Meffin and Brendan J. O'Brien and Tatiana Kameneva},
  journal={35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)},
  year={2013},
  pages={2583-2586},
  doi={10.1109/embc.2013.6610068},
  url={https://ieeexplore.ieee.org/document/6610068}
}
```

---

# Retinal ganglion cells electrophysiology: the effect of cell morphology on impulse waveform

Matias I. Maturana \(^{3,6}\) , Raymond Wong \(^{1,2}\) , Shaun L. Cloherty \(^{1,2,7}\) , Michael R. Ibbotson \(^{1,2,7}\) , Alex E. Hadjinicolaou \(^{1,2,*}\) , David B. Grayden \(^{3,4,5,6}\) , Anthony N. Burkitt \(^{3,4,5,6}\) , Hamish Meffin \(^{3,4,6}\) , Brendan J. O'Brien \(^{1,2,7}\) , Tatiana Kameneva \(^{3,4,6,*}\)

Abstract—There are 16 morphologically defined classes of rats retinal ganglion cells (RGCs). Using computer simulation of a realistic anatomically correct A1 mouse RGC, we investigate the effect of the cell's morphology on its impulse waveform, using the first-, and second- order time derivatives as well as the phase plot features. Using whole cell patch clamp recordings, we recorded the impulse waveform for each of the rat RGCs types. While we found some clear differences in many features of the impulse waveforms for A2 and B2 cells compared to other cell classes, many cell types did not show clear differences.

## I. INTRODUCTION

Retinal ganglion cells (RGCs) have been categorized into morphological classes in a number of species, including rats [11], cats [2], monkey [6] and rabbits [16]. The classification criteria commonly used are the soma and dendrites size, dendritic field diameter and angle of the dendritic stratifications. The similarities in the intrinsic electrophysiology between homologous morphological classes in different species (cats and rats) have been explored in [21]. The correspondence between morphological and electrophysiological classification has been explored in [15], [20]. How the morphological properties of mice RGCs relate to the stratification pattern of the dendrite is explored in [5]. There are 16 morphologically defined classes of rats RGCs [11]. The focus of this paper is upon the analysis of rat RGCs.  

The action potential waveform in many neurons consists of several components, that can be determined by examining the first- and second- order derivatives of the membrane potential [3], [13], [14]. In this paper we focus on this technique as an objective method to analyze the impulse waveform for different morphological RGCs types. In addition, we analyze the features of the phase plot, which shows the rate of change of the membrane potential against the membrane potential itself. It has been shown that for recordings made at the soma, the first peak in the second- order derivative arises from the axonal spike arriving at the site of the recording; the time between the first and the second peak in the second- order derivative corresponds to the time it takes to fully activate somatic sodium channels (time to charge soma capacitance). The second peak in the second- order derivative corresponds to the maximal recruitment of somatic sodium channels [3], [13], [14].

Phase plot analysis allows to measure the subtle differences in the impulse waveform, such as the initial segment- soma/dendritic break (ISSD), that correspond to the early rising phase of the action potential. When the recording is made at the soma, the presence of the ISSD in the phase plot indicates that the impulse was initiated at a region neighboring to the soma that has a lower threshold [4]. The shallow phase plot usually suggests that the action potential initiation site is at the soma rather than at the axon initial segment. The site of action potential initiation is an active area of research [10], [12]. The ISSD break is a purely electrotonic effect at the soma due to the lower threshold of the axon initial segment [8].

How the sodium, potassium, and calcium voltage- gated channel density in different morphological compartments, electrotonic current and temperature affect the features of the phase plot is explored in [8], [17]. In this paper, we investigate the effect of a RGC's morphology on its impulse waveform using computer simulation of RGCs that are anatomically correct. In addition, using experimental recordings from 90 rat RGCs, we investigated the effect of the morphology of different classes RGCs on some features of their impulse waveforms.

## II. METHODS

### A. Simulation

The multicompartment mouse RGC structure was obtained from the NeuroMorpho database [1]. It was shown that mice and rats cell types are similar [13]. The cell was classified as A1 based on the soma and dendritic diameter, soma shape, dendritic stratification and length. The membrane properties were described using Hodgkin- Huxley type equations:

\[C_{\mathrm{m}}\frac{dV}{dt} = I_{\mathrm{L}} + I_{\mathrm{Na}} + I_{\mathrm{Ca}} + I_{\mathrm{K}} + I_{\mathrm{K,A}} + I_{\mathrm{K(Ca)}} + I_{\mathrm{stim}}, \quad (1)\]

where \(V\) is the membrane potential, \(C_{\mathrm{m}}\) is the specific capacitance of the membrane, and \(I_{\mathrm{stim}}\) is intracellular stimulation current. Leak \((I_{\mathrm{L}})\) , sodium \((I_{\mathrm{Na}})\) , calcium \((I_{\mathrm{Ca}})\) , delayed rectifier \((I_{\mathrm{K}})\) , A- type \((I_{\mathrm{K,A}})\) , and Ca- activated \((I_{\mathrm{K(Ca)}})\) potassium currents had dynamics as described by [9]. All parameters were taken as in [9]. The effect of the following parameters on the phase plot was investigated:

Sodium channel band (SOCB) location: SOCB distance from the soma was varied from 15 to \(80\mu \mathrm{m}\) in \(15\mu \mathrm{m}\) steps. Base potassium conductance \((\bar{g}_{\mathrm{K}})\) : \(\bar{g}_{\mathrm{K}}\) in the soma was increased from the soma from 0.03 to \(0.1\mathrm{S / cm}^2\) in \(0.007\mathrm{S / cm}^2\) steps. Potassium conductance in all other compartments varied in the proportion of the soma conductance as discussed in [9]. Potassium conductance in the dendrites. According to [9], \(\bar{g}_{\mathrm{K}}^{\mathrm{dendrites}} = 0.5K\bar{g}_{\mathrm{K}}^{\mathrm{oma}}\) , where \(K = 1\) . In this study, \(K\) was varied from 0.15 to \(1.5\mathrm{S / cm}^2\) in 0.15 \(\mathrm{S / cm}^2\) steps. Sodium \((\bar{g}_{\mathrm{Na}})\) conductance in the dendrites. According to [9], \(\bar{g}_{\mathrm{Na}}^{\mathrm{dendrites}} = 0.5N\bar{g}_{\mathrm{Na}}^{\mathrm{oma}}\) , where \(N = 1\) . In this study, \(N\) was varied from 0.15 to \(1.5\mathrm{S / cm}^2\) steps.

The first- and second- order time derivatives of the membrane potential were calculated at each time point. The derivatives were calculated using the central difference algorithm. The ISSD break was defined as the point in the first- order derivative where the second- order derivative reaches a minimum: i.e. the point in the phase plot where the gradient is a minimum. The trough refers to the trough in the second- order derivative between the two peaks (the lowest part of the second- order derivative wave). Refer to Fig. 1 for graphical interpretation. Cells responses were simulated in the NEURON environment (Hines 1993). Data was analyzed in Matlab.

> **Image description.** A scientific figure consisting of four panels (a, b, c, and d) arranged in a 2x2 grid, illustrating the graphical interpretation of simulated neuronal data. All panels share a common horizontal axis representing "Sampling time [ms]" ranging from 5000 ms to 5200 ms, except for panel (d).
>
> **Panel (a): Membrane Potential**
> This line graph plots the membrane potential (V) in millivolts (mV) against sampling time. The potential starts around -60 mV, rises sharply to a positive peak near 0 mV, and then gradually decays back toward a negative value. The Y-axis ranges from -80 mV to 20 mV.
>
> **Panel (b): First-Order Time Derivative**
> This graph shows the first-order time derivative of the membrane potential (dV/dt) in mV/s. The data line starts near zero, rises to a positive peak (approximately 3-4 mV/s), and then drops sharply into a negative trough (approximately -3 mV/s). The Y-axis ranges from -5 mV/s to 5 mV/s.
>
> **Panel (c): Second-Order Time Derivative**
> This graph plots the second-order time derivative of the membrane potential (d²V/dt²) in mV/s². The data line exhibits distinct features:
> *   A positive peak labeled $A_1$ (marked with a red star).
> *   A trough labeled $B$ (indicated by red text).
> *   A second positive peak labeled $A_2$ (marked with a red star).
> The Y-axis ranges from -1.0 to 1.0 mV/s².
>
> **Panel (d): Phase Plot**
> This panel is a phase plot, showing the relationship between the membrane potential (V) on the X-axis and the first-order time derivative (dV/dt) on the Y-axis. The data forms a smooth, closed loop trajectory. Two specific points on this trajectory are marked with red stars and labeled $C_1$ and $C_2$. The X-axis ranges from -40 mV to 20 mV, and the Y-axis ranges from -40 mV/s to 5 mV/s.
>
> The figure collectively demonstrates the relationship between the membrane potential, its rate of change, its acceleration, and the resulting phase space trajectory during a simulated neuronal event. The labels $A_1$ and $A_2$ correspond to peaks in the second derivative, $B$ corresponds to the trough in the second derivative, and $C_1$ and $C_2$ are points on the phase plot.

<center>Fig. 1. Graphical interpretation of the data used for analysis. a) Experimentally recorded membrane potential of an A2i (inner) cell, b) First-order time-derivative of the membrane potential, c) Second-order time-derivative of the membrane potential, d) Phase plot. \(A_{1}\) , \(A_{2}\) and \(B\) two peaks and a trough in the second-order derivative used for analysis. \(C_{1}\) , \(C_{2}\) two peaks in the phase plot used for analysis. </center>

### B. Experiments

Whole- cell current clamp recordings from 90 RGCs were obtained using procedures described previously [15], [20]. Data was obtained from Long Evans rats aged between 3 and 15 month. Recordings were made at room temperature. Physiological data were acquired at \(20\mathrm{kHz}\) using custom software developed in LabView (National Instruments). Cells were excluded from analysis if they exhibited markedly inconsistent responses to stimuli, or if their morphological clas

sification could not be reliably ascertained after performing the immunocytochemistry. Filled RGCs were reconstructed in 3D with a confocal microscope (Zeiss PASCAL) and classified morphologically into morphological types according to the criteria described in [11], [18]. The number of cells used for analysis and number of recordings for each morphological class is shown in Fig. 2. RGCs responses

> **Image description.** A bar chart displaying comparative data across eight distinct categories (A1 through C2). The chart uses two distinct colors to represent two different metrics for each category.
>
> The vertical Y-axis is a numerical scale ranging from 0 to 25, representing the measured value. The horizontal X-axis lists eight categorical labels: A1, A2, B1, B2, B3, B4, C1, and C2.
>
> The data is presented using two sets of bars for each category:
> 1.  **Blue Bars:** Represent the "number of cells used for analysis," as indicated by the partial legend visible at the bottom left.
> 2.  **Orange/Salmon Bars:** Represent a second, unnamed metric (the label is cut off).
>
> **Key Visual Observations:**
> *   **General Trend:** In almost all categories, the orange bars are significantly taller than the blue bars, indicating that the second metric consistently yields higher values than the number of cells used for analysis.
> *   **Highest Values:** The highest values for both metrics occur in category A2, where the orange bar reaches approximately 18 and the blue bar reaches approximately 7. Category B2 also shows a high orange bar, reaching approximately 18.
> *   **Lowest Values:** The lowest values for the blue bars are observed in categories A1, B1, and B3, all hovering around 5. The lowest overall value is the blue bar in A1, which is approximately 4.
> *   **Specific Category Breakdown (Approximate Values):**
>     *   **A1:** Blue $\approx 4$, Orange $\approx 10$
>     *   **A2:** Blue $\approx 7$, Orange $\approx 18$
>     *   **B1:** Blue $\approx 5$, Orange $\approx 14$
>     *   **B2:** Blue $\approx 6$, Orange $\approx 18$
>     *   **B3:** Blue $\approx 5$, Orange $\approx 13$
>     *   **B4:** Blue $\approx 6$, Orange $\approx 10$
>     *   **C1:** Blue $\approx 7$, Orange $\approx 10$
>     *   **C2:** Blue $\approx 8$, Orange $\approx 10$
>
> The chart is presented against a white background, and the axes and labels are in black text. The partial legend reads: "number of cells used for analysis (blue) and number of..."

<center>Fig. 2. Number of cells used for analysis (blue) and number of recordings (red) for each morphological class. </center>

were tested with a series of depolarizing current steps of \(400\mathrm{ms}\) duration. Spontaneous spikes or spikes evoked by just- threshold current were used for analysis. If a spike was elicited less than approximately \(100\mathrm{ms}\) after the current injection time, the data for such recording was discarded. This protocol was used because in this case it was difficult to judge if a spike was elicited by the threshold current (therefore may be similar in shape to a spontaneous spike) or this was a spike elicited by a current injection and therefore had distinct properties from the spontaneous spike. For each of the recordings the following was analyzed:

- The amplitude and time of the trough between the peaks in the second-order derivative.- The difference between the first peak and the trough in the second-order derivative.

## III. RESULTS

### A. Simulation

Sodium channel band (SOCB) location. Fig. 3. a shows that as the SOCB moves away from the soma, the ISSD break becomes more pronounced, resulting in a larger ISSD break with a deeper trough between the two peaks in the phase plot. Fig. 3. b shows an emergence of an initial peak with a deeper trough between the two peaks in the second- order derivative as the distance of the SOCB from the soma is increased. Similar result was shown experimentally in [13]. This occurs because there is a larger number of sodium channels between the soma and low threshold region as the SOCB is moved away from the soma. This results in a larger initial current invading the soma at the onset of the action potential.

Base potassium conductance. Fig. 4. a shows a deeper trough between the two peaks, a lowering of the maximal peak, and a higher peak in the re- polarizing phase in the phase plot with increasing conductance of potassium in the soma. Fig. 4. b shows a deeper trough between the two peaks in the second- order derivative when the potassium conductance in the soma is increased. This occurs because there is a larger number of potassium channels being activated during the onset of the action potential (as the action

potential reaches approximately \(- 30\mathrm{mV}\) ) that inhibits the depolarization of the cell, resulting in a lower trough in the two plots and a lower maximal peak in the phase plot. A larger number of potassium channels also results in a faster return to the resting potential in the re- polarizing phase of the plot. As a result, the spike width (spike width at half height) becomes shorter.

Dendritic potassium conductance. Fig. 5. a shows a reduction in the maximal peak and the emergence of a trough between the ISSD break and the maximal peak in the phase plot with increasing concentration of potassium in the dendrites. Fig. 5. b shows a large reduction in the maximal peak and the emergence of the initial (small) peak.

Dendritic sodium conductance. Fig. 6. a shows an increase in the maximum peak of the phase plot when the conductance of sodium in the dendrites is increased. The second- order derivative shows a large increase in the maximal peak and the disappearance of the initial peak when the conductance of sodium in the dendrites is increased. The maximal peak becomes much larger, and the first peak disappears entirely, refer to Fig. 6. b.

> **Image description.** This image consists of two scientific line graphs, labeled 'a' and 'b', which display electrical activity data (action potentials and their derivatives) under varying experimental conditions.
>
> **Panel (a): Phase Plot**
> This panel is a line graph representing the phase plot.
> *   **Y-axis:** Labeled "dV/dt [mV]", ranging from approximately -200 to 300.
> *   **X-axis:** Labeled "V [mV]", ranging from approximately -100 to 100.
> *   **Data:** Multiple colored traces (including blue, green, and red) are plotted. These traces show the rate of voltage change (dV/dt) as a function of voltage (V). The curves exhibit characteristic action potential shapes, showing a rapid increase, a peak, and a subsequent decay. The traces vary in their peak height and overall shape, indicating different experimental parameters.
>
> **Panel (b): Second-Order Derivative Plot**
> This panel is a line graph representing the second-order derivative of the voltage.
> *   **Y-axis:** Labeled "d²V/dt² [mV/ms]", ranging from approximately -500 to 1000.
> *   **X-axis:** Labeled "t [ms]", ranging from approximately 3.0 to 4.5.
> *   **Data:** Multiple colored traces (matching the colors in Panel a) are plotted. These traces show the second derivative of voltage over time (t). The data is characterized by sharp, distinct peaks and troughs, which represent the acceleration of the voltage change. The height and timing of these peaks vary significantly across the different colored traces.
>
> **Text and Context**
> Below the graphs, a caption provides context for the figure: "Fig. 3. The effect of the SOCB location on a) the phase plot, and b) the second-order derivative. Traces change from blue to red as the SOCB distance from the soma changes from 15 to 80\mu m in 15\mu m steps." The traces in both panels represent different experimental conditions, specifically varying the distance of the SOCB (Spike-Onset Control Block) from the soma.

<center>Fig. 3. The effect of the SOCB location on a) the phase plot, and b) the second-order derivative. Traces change from blue to red as the SOCB distance from the soma changes from 15 to \(80\mu \mathrm{m}\) in \(15\mu \mathrm{m}\) steps. </center>

> **Image description.** A composite scientific figure consisting of two line graphs, labeled 'a' and 'b', illustrating the effect of varying parameters on electrical activity traces. Both panels display multiple colored traces (primarily shades of blue and cyan) representing different experimental conditions.
>
> Panel (a) is a phase plot, showing the rate of change of voltage over voltage.
> *   **Y-axis:** Labeled "dV/dt [mV]", ranging from approximately -150 to 150.
> *   **X-axis:** Labeled "V [mV]", ranging from approximately -80 to 60.
> *   **Data:** Multiple traces are visible, depicting action potential-like shapes. The traces show variations in the maximal peak height and the presence of a trough between the initial depolarization and the maximal peak, with the traces appearing to shift and change morphology across the different conditions.
>
> Panel (b) is a plot of the second-order derivative of voltage over time.
> *   **Y-axis:** Labeled "d²V²/dt² [mV/ms]", ranging from approximately -400 to 400.
> *   **X-axis:** Labeled "t [ms]", ranging from approximately 2.5 to 5.0.
> *   **Data:** Multiple traces are shown, characterized by sharp, high-amplitude peaks and troughs. The traces exhibit significant variation in the height and timing of these peaks across the different conditions, with some traces showing a large maximal peak and others showing a smaller initial peak.
>
> Both panels use a consistent color scheme of varying shades of blue and cyan to distinguish between the different experimental conditions being compared. The overall visual presentation is typical of computational neuroscience data analysis, comparing how changes in conductance affect the shape and timing of action potentials and their derivatives.

<center>Fig. 4. The effect of the base potassium conductance value in the soma on a) the phase plot, and b) the second-order derivative. Potassium conductance in all other compartments varied in the proportion of the soma conductance as discussed in [9]. Traces change from blue to red as \(\bar{g}_{\mathrm{K}}\) in the soma is increased from \(0.03\) to \(0.1\mathrm{S/cm}^2\) in \(0.007\mathrm{S/cm}^2\) steps. </center>

### B. Experiments

We found that some morphological classes have some features in their impulse waveforms that are distinct from other classes. A comparison of the phase plots for two cells that have ISSD break and those that do not is given in Fig. 7. Due to space constraints, we present data on the amplitude of the trough in the second- order derivative only. Fig. 8 shows the amplitude of the trough in the second- order derivative for different classes of RGCs. This histogram is informative of the ISSD break. If the trough in the second derivative reaches zero or is below zero, then the ISSD break becomes

> **Image description.** A scientific figure consisting of two line graphs, labeled 'a' and 'b', illustrating the effect of increasing potassium conductance on neuronal impulse waveforms.
>
> **Panel (a): Phase Plot (dV/dt vs. V)**
> This panel is a line graph showing the rate of change of voltage (dV/dt) against the voltage (V).
> *   **Y-axis:** Labeled "dV/dt [mV/ms]", ranging from approximately -300 to 300.
> *   **X-axis:** Labeled "V [mV]", ranging from approximately -80 to 60.
> *   **Data:** Multiple traces are plotted, representing action potentials. The traces transition in color from blue (representing a lower conductance value) to red (representing an increased conductance value).
> *   **Visual Pattern:** As the traces transition from blue to red, the maximal peak of the action potential decreases in height. Additionally, a distinct trough emerges between the initial depolarization and the maximal peak.
>
> **Panel (b): Second-Order Derivative (d²V/dt² vs. t)**
> This panel is a line graph showing the second-order derivative of voltage (d²V/dt²) against time (t).
> *   **Y-axis:** Labeled "d²V/dt² [mV/ms]", ranging from 0 to 1000.
> *   **X-axis:** Labeled "t [ms]", ranging from approximately 3.0 to 4.5.
> *   **Data:** Multiple traces are plotted, also transitioning in color from blue to red.
> *   **Visual Pattern:** As the traces transition from blue to red, the maximal peak of the second-order derivative significantly reduces in height. Concurrently, a small initial peak emerges on the left side of the plot.
>
> The overall figure demonstrates how increasing potassium conductance (indicated by the color change from blue to red) alters the shape of the action potential and its corresponding derivatives. The partial caption visible at the bottom reads: "The effect of the potassium conductance value in the..."

<center>Fig. 5. The effect of the potassium conductance value in the dendrites on a) the phase plot, and b) the second-order derivative (b). Traces change from blue to red as the \(\bar{g}_{\mathrm{K}}\) in the soma is increased. </center>

> **Image description.** A scientific figure consisting of two line graphs, labeled 'a' and 'b', illustrating the effect of sodium conductance in the dendrite on electrical activity.
>
> **Panel (a): Phase Plot (dV/dt vs. V)**
> This panel displays a line graph representing the phase plot.
> *   **Y-axis:** Labeled "dV/dt [mV]", ranging from approximately -100 to 300.
> *   **X-axis:** Labeled "V", ranging from -80 to 40.
> *   **Data:** Multiple colored traces are plotted, showing the rate of change of voltage (dV/dt) as a function of voltage (V). These traces exhibit characteristic action potential shapes, varying in peak height and overall morphology across the different curves.
> *   **Annotation:** A black arrow points to a specific feature on the traces, indicating a point of interest in the waveform.
>
> **Panel (b): Second-Order Derivative Plot (d²V/dt² vs. t)**
> This panel displays a line graph representing the second-order derivative of the voltage.
> *   **Y-axis:** Labeled "d²V/dt² [mV/ms]", ranging from 0 to 2000.
> *   **X-axis:** Labeled "t [ms]", ranging from 0 to 5.
> *   **Data:** Multiple colored traces are plotted, showing the second derivative of voltage over time. These traces show sharp, high-magnitude peaks and troughs, with variations in the timing and height of these features across the different curves.
> *   **Annotation:** A black arrow points to a specific peak on the traces, highlighting a key feature of the derivative waveform.
>
> **Text and Caption**
> A partial caption is visible beneath the graphs, reading: "The effect of the sodium conductance in the dendrite".

<center>Fig. 6. The effect of the sodium conductance value in the dendrites on a) the phase plot, and b) the second-order derivative (b). Traces change from blue to red as the \(\bar{g}_{\mathrm{Na}}\) in the soma is increased. </center>

visually well defined (that is if the first peak is also present). If the trough is above zero, then it becomes harder to see the ISSD break. Note a large positive amplitude of the trough for A2 cells. The difference between the first peak and the trough in the second- order derivative is given in Fig. 9 that shows that B2 cells have a clear distinction from all other cells except A2i.

> **Image description.** A scientific figure composed of four distinct phase plots arranged in a 2x2 grid. All plots display cyclical waveforms, characteristic of neuronal firing patterns, and share common axes.
>
> The overall structure is as follows:
> *   **Top Row:** Panel A2a (left) and Panel C3 (right).
> *   **Bottom Row:** Panel C4i (left) and Panel D2 (right).
>
> **Axes Details:**
> Each panel features a horizontal axis (x-axis) and a vertical axis (y-axis).
> *   The x-axis in all panels ranges approximately from -50 to 50.
> *   The y-axis in all panels ranges approximately from -100 to 150.
> The plots are rendered in a single dark color.
>
> **Panel Descriptions:**
> *   **Panel A2a:** Displays a single, smooth, rounded cyclical waveform. The peak of the cycle reaches approximately 125 on the vertical axis.
> *   **Panel C3:** Shows a single, smooth cyclical waveform, similar in general shape to A2a, with a peak slightly lower than A2a.
> *   **Panel C4i:** Displays a more complex cyclical waveform. It features a distinct initial peak, followed by a noticeable trough, and then a larger, secondary peak.
> *   **Panel D2:** Also displays a complex cyclical waveform, similar to C4i. It shows an initial peak, followed by a trough, and then a larger peak, with the overall amplitude and shape differing slightly from C4i.

<center>Fig. 7. Phase plot for two cells with the ISSD break (a2o, c4i) and those without (c3, d2). Horizontal axis: membrane potential [mV], vertical axis: first-order derivative of the membrane potential [mV/ms] </center>

## IV. DISCUSSION AND CONCLUSION

Using computer simulation of a multicompartiment morphologically correct A1 mouse cell, we investigated the effects of the cell's biophysical properties on its impulse waveform. we found that the ISSD break becomes more pronounced as the SOCB moves away from the soma. This result may lead to the prediction of the location of the SOCB based on the recordings of the impulse waveform. We analyzed experimentally recorded membrane potential data for different morphological classes of RGCs. While we found some clear differences in many features of the impulse waveforms for A2 and B2 cells compared to other cell classes, many cell types did not show clear differences

> **Image description.** A bar chart, labeled Figure 8, which displays the histogram of the amplitude of the trough in the second-order derivative across various classes of Retinal Ganglion Cells (RGCs).
>
> The chart is structured with the "Cell type" listed along the horizontal X-axis and the amplitude measured in "mV/ms" along the vertical Y-axis. The Y-axis ranges from -300 to 300, with major tick marks every 100 units.
>
> The X-axis categorizes the data into 14 distinct cell types: A1, A2, A2a, B1, B2, B3, B4, C1, C2, C3, C4, D1, and D2. Each cell type is represented by a vertical bar, and each bar includes a vertical error bar extending above and below the mean value.
>
> The data generally shows positive amplitudes for all cell types. The cell types A1 and A2 exhibit the highest mean amplitudes, with A1 appearing to have the largest mean value, followed closely by A2. The remaining cell types (A2a through D2) show lower mean amplitudes, generally clustered between 0 and 100 mV/ms.
>
> A notable visual feature is the presence of large error bars across many of the cell types, indicating significant variability in the measured amplitude within those groups. The error bars for A1 and A2 are also substantial, suggesting high variability even among the cell types with the highest mean amplitudes.
>
> In summary, the figure visually compares the characteristic amplitude of the trough in the second-order derivative—a feature related to the impulse waveform—across different RGC classifications, highlighting differences in mean amplitude and the degree of variability between these cell types.

<center>Fig. 8. The histogram of the amplitude of the trough in the second-order derivative for different classes of RGCs. </center>

> **Image description.** A bar chart, or histogram, displaying data across various cell types, likely representing a measurement of amplitude or rate.
>
> The chart is structured with a vertical Y-axis and a horizontal X-axis.
>
> **Axes and Labels:**
> *   **Y-axis:** Labeled "mV/ms," representing the measured value. The scale ranges from 0.0 to 0.7, with major tick marks every 0.1 units.
> *   **X-axis:** Labeled "Cell type," listing 15 distinct categories: A1, A2, A2o, B1, B2, B3, B3o, C1, C2, C3, C4, C4o, D1, and D2.
>
> **Data Representation:**
> The data is presented as vertical bars, each corresponding to a specific cell type. The height of the bars indicates the mean value for that cell type.
> *   The values generally range between approximately 0.05 mV/ms and 0.4 mV/ms.
> *   The highest mean value is observed for cell type C2, reaching approximately 0.4 mV/ms.
> *   The lowest mean values are found in cell types such as B3 and B3o, which are close to 0.05 mV/ms.
>
> **Error Bars:**
> Each bar is accompanied by a vertical error bar, indicating variability in the data. These error bars are notably large for several cell types, suggesting high variance in those groups. The error bars are particularly prominent for cell types C2 and C3, where the vertical lines extend significantly above and below the mean bar height.
>
> Overall, the chart illustrates the distribution of a specific metric (mV/ms) across different classifications of cell types, highlighting both the mean values and the associated data variability.

<center>Fig. 9. The histogram of the normalized difference between the first peak and the trough in the second-order derivative. </center>

and the error bars were large. This may be due to a sample size.

In simulation, we found that potassium channel concentration changes in the soma and in the dendrites have different effects. While changing potassium conductance in the soma has only small effects on the phase plot, changing dendritic potassium concentration has dramatic changes in the maximum peak, trough and shape of the phase plot. The higher the dendritic potassium concentration is, the longer the cell takes to respond (refer to the time difference between peaks in second derivative, and the amplitude of the second peak in the second derivative in Fig. 5). Similar to potassium concentration changes in dendrites, the sodium conductance changes in the dendrites have a large effect on the maximum peak in phase plot. This may imply that dendritic electrophysiology may have a large effect on the impulse waveform.

In simulation, we found that the ISSD break becomes more pronounced in the phase plot with the increased distance of the SOCB from the soma. This result was shown experimentally in [13]. This is due to the fact that if the initial segment is far enough from the soma results in the local channels being not involved before the spike invades the soma. Based on the timing and amplitude of two peaks in the second- order derivative of the membrane potential, it may be possible to cluster cells based on the features of the ISSD break. Since the features of the ISSD break correspond to the site of the action potential initiation, this may lead to the classification of the cells based on the impulse initiation site.

This may have important implications for a visual prosthesis, such as finding a stimulation strategy to activate cell types selectively.

## V. ACKNOWLEDGMENTS

The authors wish to thank Emily O'Brien for her help classifying A1 mice RGC cell for simulations. This research was supported by the Australian Research Council (ARC) through its Special Research Initiative (SRI) in Bionic Vision Science and Technology grant to Bionic Vision Australia (BVA). The Bionics Institute acknowledges the support it receives from the Victorian Government through its Operational Infrastructure Support Program. This research was supported by NHMRC Project grant 585440 and ARC Discovery grant DP0881247.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
