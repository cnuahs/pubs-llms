```
@article{cloherty2001inhomogeneity,
  title={Inhomogeneity of action potential waveshape assists frequency entrainment of cardiac pacemaker cells},
  author={Shaun L. Cloherty and Nigel H. Lovell and Branko G. Celler and Socrates Dokos},
  journal={IEEE Transactions on Biomedical Engineering},
  year={2001},
  volume={48},
  number={10},
  pages={1108-1115},
  doi={10.1109/10.951513},
  url={https://ieeexplore.ieee.org/document/951513}
}
```

---

# Inhomogeneity of Action Potential Waveshape Assists Frequency Entrainment of Cardiac Pacemaker Cells

Shaun L. Cloherty\*, Nigel H. Lovell, Senior Member, IEEE, Branko G. Celler, Member, IEEE, and Socrates Dokos, Member, IEEE

Abstract—In this paper, we have employed ionic models of sinoatrial node cells to investigate the synchronization of a pair of coupled cardiac pacemaker cells from central and peripheral regions of the sinoatrial node. The free- running cycle length of the cell models was perturbed using two independent techniques and the minimum coupling conductance required to achieve frequency entrainment was used to assess the relative ease with which various cell pairs achieve entrainment. The factors effecting entrainment were further investigated using single- cell models paced with an artificial biphasic coupling current.

Our simulation results suggest that dissimilar cell types, those with largely different upstroke velocities entrain more easily, that is, they require less coupling conductance to achieve 1:1 frequency entrainment. We, therefore, propose that regional variation in action- potential waveshape within the sinoatrial node assists frequency synchronization in vivo.

Index Terms—Action- potential waveshape, frequency entrainment, mathematical modeling, sinoatrial node.

## I. INTRODUCTION

T HE NORMAL electrical activity of the heart is initiated by a small region of specialized pacemaker cells, known as the sinoatrial node, located in the wall of the right atrium near the opening of the superior vena cava. The pacemaker cells are spontaneously active, exhibiting a slow depolarization to threshold (pacemaker potential) rather than a stable resting potential. The sinoatrial node is known to consist of a large number of heterogeneous cells with at least a moderate degree of electrotonic interconnection [1]. Microelectrode recordings from the intact sinus node reveal a marked change in action- potential characteristics from the center to the periphery of the sinus node, including an increase (hyperpolarization) in the maximum diastolic potential (MDP), an increase in overshoot potential (OS), upstroke velocity (UV) and a decrease in intrinsic cycle length (CL) [2]. Kodama and Boyett [3] observed this same variation in action- potential characteristics in small electrically isolated tissue specimens ( \(\sim 0.3\mathrm{mm}\) in diameter). They concluded that

action- potential heterogeneity, including variation in intrinsic CL, was the result of a genuine transition in cell membrane electrophysiological characteristics.

Despite the variation in action- potential characteristics, cells of the sinus node synchronize their firing rate and drive contraction of the entire myocardium in a robust synchronous rhythm. This synchronization of cells, despite differences in intrinsic CL, has been attributed to the electrical coupling of neighboring cells via gap junctions, a hypothesis supported both experimentally and via simulation studies [4], [5]. In the present study, we investigate the possible role of regional variation in action- potential characteristics in frequency synchronization of the sinoatrial node.

Cai et al. [6] attempted to model the central- peripheral variation in action- potential characteristics and coupled pairs of central and peripheral cells via a constant conductance. They reported that the minimum coupling conductance required for frequency entrainment decreased as the difference in intrinsic CL was reduced. Our simulations of coupled cell pairs suggest that in addition to intrinsic CL, action- potential waveshape also influences entrainment. We find that cells with largely different action- potential characteristics require less coupling conductance to achieve frequency entrainment and, thus, entrain more easily. Our simulation results suggest that the observed variation in action- potential characteristics of cells of the sinus node may well aid in the synchronization of their firing rate.

## II. METHODS

### A. The Single-Cell Model

Single sinoatrial node cells were modeled using a modified version of the equations of Dokos et al. [7]. These modifications were the addition of both rapid and slow components of the delayed rectifier potassium current \(i_{\mathrm{K}},r\) and \(i_{\mathrm{K}},s\) , and setting the reversal potential of the \(L\) and \(T\) type calcium currents, \(i_{\mathrm{Ca}},L\) and \(i_{\mathrm{Ca}},T\) to a constant value of \(\sim 40\mathrm{mV}\) (See Appendix A). A set of 38 model parameters was identified which determined the action- potential characteristics of the model. Values of these parameters were chosen to accurately reproduce the central- peripheral variation in action- potential characteristics observed by Kodama et al. [8]. An additional parameter specifying a voltage offset was applied to the experimental recordings to minimize the disparity between the experimental recording and the simulated membrane potential. This offset is analogous to the un

known experimental liquid junction potential. Recently, Zhang et al. [9] published ionic models of central and peripheral sinoatrial node cells, however, the models employed in the present study appear to exhibit a superior correlation with the published experimental recordings.

### B. Coupled Cell Pairs

Electrotonic interaction between cells was modeled using a constant coupling conductance \(G_{c}\) . The total ionic current for each cell was given by the algebraic sum of its individual ion currents and a coupling current \(i_{c}\) , defined as

\[i_{c} = G_{c}\times (E - E_{n}) \quad (1)\]

where

\(E\) membrane potential of a given cell; \(E_{n}\) membrane potential of its neighbor; \(G_{c}\) coupling conductance.

In order to investigate the effect of action- potential characteristics on entrainment, the free- running CL of the central and peripheral models was adjusted by two separate means; first, by scaling the background sodium current \(i_{b,\mathrm{Na}}\) ; second by simultaneously scaling \(i_{f}\) and \(i_{\mathrm{Ca},T}\) while maintaining \(i_{b,\mathrm{Na}}\) at its control value. This facilitated the investigation of interaction between both similar and dissimilar cell types while maintaining a constant CL disparity in all simulations. Cai et al. [6] modeled a CL disparity of approximately \(25\%\) . In the present study, we have opted for a CL disparity of approximately \(14\%\) as reflected by the experimental recordings of Kodama et al. [8]. This is comparable to the disparity in CL of approximately \(18\%\) previously reported by Kodama and Boyett [3], for comparable recording sites.

In the discussion below, cell models in which the CL has been modified are referred to as perturbed cell models and are designated by a symbolic suffix indicating the technique used to modify the CL. For example, "Centralo" denotes a central cell model in which the CL has been modified by scaling \(i_{b,\mathrm{Na}}\) , while "Centralo" denotes a central cell model in which the CL has been modified by simultaneously scaling \(i_{f}\) and \(i_{\mathrm{Ca},T}\) .

When simultaneously scaling two current systems, there exists an essentially infinite number of combinations of the scaling factors which result in the desired CL disparity. In the discussion below, two different sets of scaling factors have been chosen for each of the central and peripheral cell models. The perturbed model resulting from the first set of scaling factors is denoted by a single symbolic suffix, and that resulting from the second set by a repeated suffix. For example, "Centralo" denotes a central cell model in which the CL has been modified by simultaneously scaling \(i_{f}\) and \(i_{\mathrm{Ca},T}\) using the first set of scaling factors, while "Centralo" denotes the perturbed central cell model resulting from the second set of scaling factors.

For each of the control and perturbed cell models, suitable initial conditions were obtained by integrating the model equations for 200 s, after which steady- state was achieved. Steady- state was taken as that condition in which no further change in the model state variables or action- potential characteristics was evident. The state variables corresponding to this steady- state were saved and used as initial conditions in all subsequent simulations.

> **Image description.** A technical diagram illustrating a rectangular pulse waveform, specifically titled "Fig. 1. The artificial biphasic coupling current waveform." The image is a time-series plot showing the relationship between coupling current and time.
>
> The graph features two axes:
> *   The vertical axis (Y-axis) is labeled "Coupling Current (pA)," indicating the current is measured in picoamperes.
> *   The horizontal axis (X-axis) is labeled "Time (s)," indicating the duration is measured in seconds.
>
> The waveform itself is composed of two distinct positive current pulses separated by periods of zero current. The sequence of the waveform is as follows:
> 1.  The current starts at zero and rises to a peak value, labeled 'P'.
> 2.  It maintains this peak value for a duration labeled $D_1$.
> 3.  The current drops back to zero and remains there for a duration labeled $D_2$.
> 4.  The current rises again to the same peak value 'P'.
> 5.  It maintains this peak value for a duration labeled $D_2$.
> 6.  The current drops back to zero and remains there for a final duration labeled 'Q'.
>
> The labels provide specific definitions for the components of the waveform:
> *   'P' represents the peak magnitude of the coupling current.
> *   $D_1$ represents the duration of the first current pulse.
> *   $D_2$ represents the duration of the second current pulse.
> *   'Q' represents the total time duration of the entire cycle shown in the diagram.
>
> The caption below the figure reads: "Fig. 1. The artificial biphasic coupling current waveform."

<center>Fig. 1. The artificial biphasic coupling current waveform. </center>

For each cell pair; Central- Peripheral, Central- Centralo, Peripheral- Peripheralo, Central- Centralo, Peripheral- Peripheralo, Central- Centralo, and Peripheral- Peripheralo, series of simulations were performed in which the coupling conductance \(G_{c}\) was assigned values in the range \(2.0\mathrm{pS}\) to \(4.0\mathrm{nS}\) . At each value of the coupling conductance, the cells were coupled for 15 s, allowing sufficient time for any initial transients to cease. The first 5 s of each simulation was discarded and subsequent analysis was based only on the remaining 10 s of data. Simulation results are presented in Section III- B.

### C. A Biphasic Pacing Protocol

In addition to the cell pair simulations described in the previous section, we have also examined the entrainment of a single cell to an artificial periodic biphasic coupling current as shown in Fig. 1. This relatively simple artificial coupling current allows us to represent qualitatively, the coupling current observed in our cell pair simulations. Note that the waveform as shown in Fig. 1 represents the coupling current observed relative to the slower cell in an entrained cell pair. By injecting this artificial current, with various waveform parameters, into the single- cell model described above, and observing the resulting entrainment dynamics, we can infer at least qualitatively, which characteristics have the most significant effect on entrainment.

The artificial current waveform is completely characterized by five parameters; an amplitude ratio \(R = A / Q\) , two phase durations \(D_{1}\) and \(D_{2}\) , the period \(P\) , and an overall amplitude scaling parameter \(Q\) . An auxiliary parameter, the duty cycle \(D\) , was defined as \(D = (D_{1} + D_{2}) / P\) . We impose one constraint on these parameters in that the average charge transfer over one cycle must be zero. This is important in that a net positive or negative charge transfer would result in accumulation or depletion of one or more ion species in either the intra or extracellular space, resulting in an unconstrained drift in CL. In the simulations discussed here, \(D_{2}\) and \(R_{2}\) were adjusted for a desired \(D_{2}\) and \(P\) to satisfy the imposed constraint. In all simulations, the duty cycle \(D\) was equal to \(50\%\) .

### D. Computational Methods

The model equations were implemented in Gnu C/C++ and all simulations were performed in double precision on a PC

> **Image description.** A line graph titled "Fig. 2" displays the simulated and experimental cell membrane potential over a one-second time interval. The graph plots Membrane Potential in millivolts (mV) on the vertical Y-axis against Time in seconds (s) on the horizontal X-axis.
>
> The Y-axis ranges from -80 mV to 40 mV, while the X-axis spans from 0 to 1 second. Four distinct data series are plotted, representing two cell types (Central and Peripheral) and two data types (simulated and experimental).
>
> The data series are as follows:
> 1.  **Peripheral (Simulated):** Represented by a solid line, this curve shows a sharp, positive action potential spike, peaking near 30 mV, followed by a rapid return toward the resting potential.
> 2.  **Peripheral (Experimental):** Represented by a dashed line, this curve follows the same general shape as the simulated peripheral line but is visibly offset downward, consistent with the caption stating an offset of -11.2 mV.
> 3.  **Central (Simulated):** Represented by a solid line, this curve also exhibits a positive action potential spike, though its peak is lower than the peripheral simulated spike, reaching approximately 20 mV.
> 4.  **Central (Experimental):** Represented by a dashed line, this curve mirrors the central simulated line but is offset downward, consistent with the caption stating an offset of -2.8 mV.
>
> The figure caption, located below the graph, reads: "Fig. 2. Simulated cell membrane potential from the central and peripheral cell models. The dashed lines represent the corresponding experimental recordings from Kodama et al. [8] (Fig. 3), offset by (-2.8 mV) (central) and (-11.2 mV) (peripheral)." The visual evidence confirms that the solid lines represent the simulated models, while the dashed lines represent the experimental data, with the differences in their vertical positions corresponding to the specified offsets.

<center>Fig. 2. Simulated cell membrane potential from the central and peripheral cell models. The dashed lines represent the corresponding experimental recordings from Kodama et al. [8] (Fig. 3), offset by \(-2.8 \mathrm{mV}\) (central) and \(-11.2 \mathrm{mV}\) (peripheral). </center>

running the Linux operating system. Numerical integration was performed using the hybrid predictor- corrector method described by Dokos et al. [7], with a relative error tolerance of \(1.0 \times 10^{- 3}\) . Simulation results were saved to disk in IEEE double precision binary format and analyzed using Matlab.

## III. RESULTS

### A. Simulated Membrane Potential

Fig. 2 shows the free- running simulated membrane potential using the parameters for the central and peripheral models. Experimental recordings are also shown for comparison (dashed lines).

The free- running action- potential characteristics of the Central and Peripheral cell models are summarized in Table I. Typical ranges of action- potential characteristics observed experimentally are shown in parentheses. MDP and OS are the most negative and most positive values of the membrane potential respectively. UV is the maximum rate of change of the membrane potential \(dE_{m} / dt|_{max}\) . CL is the duration between the point of maximum UV of one action potential and that of the next. Also shown in Table I are the action- potential characteristics for the perturbed cell models together with the corresponding scaling factors. Note that the CLs of the perturbed models are approximately equal to those of the unperturbed model of the reciprocal cell type.

Scaling the pacemaker currents, either \(\dot{u}_{b,\mathrm{Na}}\) or \(\dot{u}_{F}\) and \(\dot{u}_{\mathrm{Ca},T}\) , to control CL causes some change in the other action- potential characteristics. For the most part, these changes are small and in the interests of simplicity, no effort has been made to compensate.

### B. Coupled Cell Pairs  

As described above, a series of simulations were performed to determine the range of coupling conductances over which each of the different pairs of coupled cell types achieved frequency entrainment. The simulated CLs for cells with largely different action- potential characteristics, namely the Central- Peripheral cell pair, are shown as a function of coupling conductance in Fig. 3. The critical coupling conductance \((G_{c,\mathrm{crit}})\) , defined as the minimum coupling conductance required for 1:1 frequency entrainment, is readily identified as the point at which the system experiences an abrupt transition from complex entrainment to 1:1 frequency entrainment. For the Central- Peripheral cell pair shown in Fig. 3, this critical point lies at approximately \(22 \mathrm{pS}\) . The results from a similar series of simulations for each of the remaining cell pairs are summarized in Table II, where the columns denote each of the possible symbolic suffixes, \((\Delta = \circ , \bullet , \mathrm{or} \bullet \bullet)\) and rows denote the cell types of each pair. For example, the critical coupling conductance for the Peripheral- Peripheral \(\bullet \bullet\) cell pair is obtained by proceeding to the column corresponding to the perturbed cells symbolic suffix \((\Delta = \bullet \bullet)\) , and then proceeding down the column to the row denoting the appropriate cell types (Peripheral- Peripheral \(\Delta\) ). In all cases, the difference in CL for each pair of cells was approximately \(14\%\) . This figure is in agreement with the experimental observations of Kodama et al. [8].

> **Image description.** A line graph illustrating the relationship between coupling conductance and cycle length for two different cell models, labeled "Central" and "Peripheral."
>
> The graph features two axes:
> *   The Y-axis is labeled "Cycle Length (ms)" and ranges from 390 to 490, with linear increments.
> *   The X-axis is labeled "Coupling Conductance (pS)" and uses a logarithmic scale, ranging from $10^0$ (1) to $10^2$ (100).
>
> Two distinct sets of data points, representing simulation results, are plotted:
> 1.  **Central:** This data set is represented by a dense cluster of points forming a curve that generally slopes downward. It begins at a cycle length of approximately 470 ms at low coupling conductance and decreases to around 410 ms as the conductance increases.
> 2.  **Peripheral:** This data set is also represented by a dense cluster of points forming a curve that slopes downward. It starts at a cycle length of approximately 460 ms at low coupling conductance and decreases to a similar range as the Central model at higher conductance.
>
> A prominent annotation points to a specific region on the graph, indicating a critical threshold. An arrow points to the area where the curves begin to flatten and converge, accompanied by the text: "Gc crit = 22 pS". This suggests that 22 pS is the critical coupling conductance value. The overall visual pattern shows that as coupling conductance increases, the cycle length decreases for both the Central and Peripheral cell models, until reaching a critical point.

<center>Fig. 3. Simulated CL of the coupled Central–Peripheral cell pair as a function of coupling conductance \(G_{c}\) . The critical coupling conductance \(G_{c,\mathrm{crit}}\) lies at approximately \(22 \mathrm{pS}\) as indicated. </center>

The results presented in Table II, in which the critical coupling conductance was lowest for the Central- Peripheral cell pair suggests that dissimilar cells, those with largely different action- potential characteristics, entrain more easily than cells with similar action- potential characteristics. One possible explanation for this is suggested by Fig. 4 which compares the coupling current flowing between the cells for: (a) Central- Peripheral, (b) Central- Central, and (c) Peripheral- Peripheral cell pairs. Note that the coupling currents shown here are calculated relative to the slower cell. This convention is adhered to throughout this discussion, consequently, any reference to current direction, inward or outward, is relative to the slower cell. Of particular interest is the duration of the inward current phase occurring during action- potential

TABLE I SIMULATED FREE-RUNNING ACTION POTENTIAL CHARACTERISTICS

| Cell Pair | Scaling Factors | CL | MDP | OS | UV |
| :--- | :---: | :---: | :---: | :---: | :---: |
| | ib,Na | if | iCa,T | ms | mV | ms | mV | ms | mV/ms |
| Central (Experimental [3][22]) | --- | --- | --- | 465.9 | -61.8 | (380 - 386) | (-58 - -61) | (4 - 5) | (1.9 - 3.0) | (1.9 - 3.0) |
| Centralo | 1.1067 | --- | --- | 408.0 | -58.0 | --- | --- | --- | --- | 3.7 | 1.1 |
| Central● | -0.2039 | 1.65 | 407.0 | -59.9 | -0.6 | --- | --- | --- | --- | 1.3 |
| Central● | -0.4827 | 1.85 | 407.0 | -59.7 | -2.0 | --- | --- | --- | --- | 1.2 |
| Peripheral (Experimental [3][23]) | --- | --- | --- | 408.0 | -69.3 | (238 - 834) | (-53 - -85) | (11 - 35) | (7.9 - 33.0) | (7.9 - 33.0) |
| Peripheralo | 0.8510 | --- | --- | 465.8 | -71.4 | --- | --- | --- | --- | 8.3 |
| Peripheral● | -0.3032 | 0.25 | 462.0 | -70.5 | 35.1 | --- | --- | --- | --- | 9.7 |
| Peripheral● | -0.1650 | 0.50 | 462.0 | -70.7 | 35.3 | --- | --- | --- | --- | 9.7 |

TABLE II CRITICAL COUPLING CONDUCTANCES

| Cell Pair | $G_{c,crit}$ (pS) | $\Delta$ | $\circ$ | $\bullet$ |
| :--- | :--- | :--- | :--- | :--- |
| Central-Peripheral | 22 | 2 | 2 | 2 |
| Central-Central | 31 | 3 | 1 | 3 |
| Peripheral-Peripheral | 28 | 2 | 7 | |

upstroke. In the case of the Central- Peripheral cell pair, this phase is significantly prolonged compared to that observed in both the Central- Centralo and Peripheral- Peripheralo cell pairs. This increase in the duration of the inward current phase results in a greater inward charge transfer, \(0.4235\mathrm{pC}\) for the Central- Peripheral cell pair, compared with \(0.2117\mathrm{pC}\) and \(0.3768\mathrm{pC}\) for the Central- Centralo and Peripheral- Peripheralo cell pairs respectively. The duration of the inward coupling current phase, and hence the inward charge transfer, is largely determined by the disparity in UV and to a lesser extent OS, between the two cells.

It is our hypothesis that a prolonged inward current phase during action- potential upstroke, as would be expected in cell pairs with largely different upstroke velocities, assists entrainment.

### C. Single-Paced Cells

In order to test our hypothesis, a single central cell was paced using the artificial biphasic current waveform described above. The disparity in action- potential UV was modeled by increasing the duration of the inward current phase \(D_{1}\) . In all simulations, the pacing period \(P\) was \(416\mathrm{ms}\) , roughly corresponding to the entrained CL of the Central- Peripheral cell pair shown in Fig. 3. The duration of the inward current phase \((D_{1})\) was incremented from \(5\%\) to \(25\%\) of the pacing period \(P\) , in increments of \(5\%\) . At each value for \(D_{1}\) , the amplitude scaling parameter \(Q\) was incremented from \(0.1\mathrm{pA}\) to \(7.2\mathrm{pA}\) in increments of \(0.1\mathrm{pA}\) , roughly corresponding to the range of current amplitudes observed in our coupled cell pair simulations discussed above.

> **Image description.** A scientific figure consisting of three vertical panels, labeled (a), (b), and (c), each displaying two stacked line graphs representing electrical activity traces. The figure illustrates voltage and coupling current over time for different cell pair configurations.
>
> The overall structure is a 3x2 grid of graphs. Each panel (a, b, and c) contains:
> 1.  **Top Graph (Voltage):** A trace showing membrane potential in millivolts (mV) versus time (s).
> 2.  **Bottom Graph (Current):** A trace showing coupling current in picoamperes (pA) versus time (s).
>
> **Detailed Panel Analysis:**
>
> *   **Panel (a):**
>     *   **Top Graph:** Shows a voltage trace starting near -80 mV, rising sharply to a peak near 0 mV, and then decaying back toward the resting potential.
>     *   **Bottom Graph:** Shows a coupling current trace that starts near 0 pA, rapidly drops to a negative peak of approximately -7 pA, and then returns toward zero.
> *   **Panel (b):**
>     *   **Top Graph:** Shows a voltage trace starting near -80 mV, rising to a peak slightly below 0 mV, and then decaying.
>     *   **Bottom Graph:** Shows a coupling current trace that starts near 0 pA, drops to a negative peak of approximately -6 pA, and then returns toward zero.
> *   **Panel (c):**
>     *   **Top Graph:** Shows a voltage trace starting near -80 mV, rising sharply to a peak near 0 mV, and then decaying.
>     *   **Bottom Graph:** Shows a coupling current trace that starts near 0 pA, drops to a negative peak of approximately -7 pA, and then returns toward zero.
>
> **Axes and Labels:**
> *   The horizontal axis for all graphs is labeled "Time (s)" and ranges from 0 to 0.5 seconds.
> *   The vertical axis for the top graphs is labeled "mV" and ranges from -80 to 40 mV.
> *   The vertical axis for the bottom graphs is labeled "Coupling Current (pA)" and ranges from -8 to 6 pA.
> *   The figure caption, partially visible at the bottom, begins: "Fig. 4. Observed coupling current for (a) Central-Peripheral (b) Central-Central (c) Peripheral-Peripheral..."
>
> The traces in all panels exhibit a characteristic shape: a rapid depolarization (upstroke) followed by a repolarization phase, with the coupling current tracing the inward flow of charge during the depolarization.

<center>Fig. 4. Observed coupling current for (a) Central-Peripheral, (b) Central-Centralo and (c) Peripheral-Peripheralo cell pair simulations. In all cases, \(G_{c} = 100\mathrm{pS}\) . </center>

The critical value for the amplitude scaling parameter, \(Q_{\mathrm{crit}}\) , defined as the minimum value required for frequency entrainment, was found to decrease as the duration of the inward current phase \((D_{1})\) was increased. Fig. 5 shows \(Q_{\mathrm{crit}}\) as a function of inward current phase duration \(D_{1}\) . The circles denote the results of the simulations described above. The solid line represents the optimal fit, in a least squares sense, of the classic strength- duration relationship described by (2) [10]

\[Q_{\mathrm{crit}} = \frac{Q_0}{1.0 - \exp(-D_1 / k)} \quad (2)\]

with

\[Q_{0} = 0.8085\mathrm{pA}\] \[k = 35.47\% \mathrm{CL}\]

It is easily verified that (2) does not support a constant charge hypothesis, in which frequency entrainment is simply dependent

> **Image description.** A scientific line graph titled "Fig. 5" that illustrates the relationship between the critical stimulus amplitude and the inward phase duration.
>
> The graph features two axes:
> *   The Y-axis, labeled "Critical Stimulus Amplitude (pA)," ranges from 1 to 7, with major tick marks every unit.
> *   The X-axis, labeled "Inward Phase Duration (% Cycle Length)," ranges from 5 to 25, with major tick marks every 5 units.
>
> The data is presented as a series of connected data points (circles) forming a downward-sloping curve. The curve demonstrates a non-linear relationship: the critical stimulus amplitude decreases sharply as the inward phase duration increases from 5% to approximately 15%, and then the rate of decrease slows down as the duration continues to increase toward 25%.
>
> An annotation is placed near the right side of the graph, featuring an arrow pointing from left to right. Next to this arrow, the text reads: "Increasing disparity in upstroke velocity."
>
> The caption below the graph provides further technical context: "Fig. 5. Critical amplitude scaling factor ($Q_{\mathrm{crit}}$) for the artificial coupling current waveform, as a function of inward current phase duration ($D_{1}$) . The circles denote the simulation results, while the solid line represents the classic strength-duration relationship observed in excitable tissue [see (2)]." This indicates that the plotted circles represent simulated data, while the solid line represents a known biological relationship.

<center>Fig. 5. Critical amplitude scaling factor \((Q_{\mathrm{crit}})\) for the artificial coupling current waveform, as a function of inward current phase duration \((D_{1})\) . The circles denote the simulation results, while the solid line represents the classic strength-duration relationship observed in excitable tissue [see (2)]. </center>

on the magnitude of the inward charge transfer. As a result, inward charge transfer alone is not the sole factor governing frequency entrainment.

As mentioned above, the duration of the inward current phase \((D_{1})\) represents the disparity in UV. As shown by the arrow in Fig. 5, the minimum coupling current amplitude required for frequency entrainment decreases as the disparity in UV \((D_{1})\) increases. This is in agreement with our hypothesis stated earlier, that a prolonged inward current phase during action- potential upstroke assists frequency entrainment.

## IV. DISCUSSION

At present, there exists some uncertainty regarding the distribution of gap junction proteins (connexins, Cx) in the sinoatrial node. A recent immunohistochemical study by Coppen et al. [11] suggests that gap junctions in the rabbit sinoatrial node are predominantly composed of Cx40 and Cx45. Moreno et al. [12] reported a single channel conductance for human Cx45 gap junctions of \(32 \pm 8\) pS, comparable to that previously reported for chick Cx45 of \(29 \pm 5\) pS [13]. Assuming that the single channel conductance is characteristic of a given homologous connexin, then we might reasonably expect single gap junction channels of similar conductance to be present between cells of the rabbit sinoatrial node.  

Based on a theoretical calculation, Anumonwo et al. [14] estimated that three functional gap junction channels, of roughly 50 pS each, would be sufficient to achieve frequency entrainment of a pair of coupled pacemaker cells. They noted that depending on the CL disparity and the excitability of the cells, frequency entrainment may be possibly with as little as a single functional gap junction channel. Clapham et al. [15] also suggested that a pair of isolated cells could achieve frequency entrainment with only a single gap junction channel. Even if the single channel conductance of gap junctions within the sinoatrial node is as low as that reported for Cx45 \((\sim 30\) pS), the simulation results presented in the present study suggest that a single functional gap junction channel may be sufficient to achieve frequency entrainment.

Interestingly, Coppen et al. [11] also reported that the relative amount of Cx40 and Cx45 present in the sinoatrial node region was substantially lower than the amount of Cx43 observed in the surrounding atrial tissue. This is in agreement with the general consensus that there exists a relatively low level of interconnection within the sinoatrial node compared with other cardiac tissue [1]. The relatively sparse gap junction density in the central region has been hypothesized to be a means of protecting the central (primary) pacemaker region from the hyperpolarizing influence of the surrounding atrium [16]. While this is likely to be the case, the results of the present study suggest a new, somewhat novel interpretation. In the central region of the sinoatrial node, consisting of relatively few central pacemaker cells surrounded by peripheral pacemaker cells, the critical coupling conductance would be low, due to the difference in action- potential characteristics. Toward the periphery, where peripheral cells predominate and action- potential characteristics are much more homogeneous, the critical coupling conductance would be higher. As a result, we observe an increase in gap junction density toward the periphery of the sinoatrial node relative to that in the central region.

Cai et al. [6] in their simulations of coupled pacemaker cell pairs reported a critical coupling conductance of approximately \(220\) pS (3.7 pS/pF, normalized for membrane capacitance) for frequency entrainment. This figure is roughly five times larger than that of 0.7 pS/pF observed in our simulations. Although direct comparison is difficult, the discrepancy may plausibly be attributed to differences in the simulated action- potential characteristics and cell excitability. The CL disparity of \(26\%\) modeled by Cai et al. [6], is almost twice that of \(14\%\) modeled in the present study. Although they provide no quantitative information, Cai et al. [6] reported that the critical coupling conductance required for frequency entrainment decreased as the disparity in CL was reduced. Wilders et al. [17] made a similar observation, reporting a linear decrease in critical coupling conductance with decreasing CL disparity.

Verheijck et al. [18] performed five experiments in which pairs of isolated sinoatrial node cells were electrically coupled via an external circuit. For a CL disparity of roughly \(10\%\) , comparable to the \(14\%\) modeled in the present study, Verheijck et al. [18] report a critical coupling conductance on the order of \(125 - 150\) pS (3.1- 3.8 pS/pF). Again, direct comparison is difficult due to differences in action- potential characteristics and cell excitability. Nevertheless, we observe that the critical coupling conductances reported in the present study are on the same order of magnitude as those reported both experimentally and in simulation studies.

## V. CONCLUSION

Simulation results presented in this paper indicate that cardiac pacemaker cells with largely different action- potential characteristics, particularly UV, achieve frequency entrainment more readily than those with similar action- potential characteristics. Such cells also tend to exhibit a more prolonged inward coupling current phase during action- potential upstroke than that

TABLE III MODEL PARAMETERS

| Description | Symbol | Units | Central | Peripheral |
| :--- | :--- | :--- | :--- | :--- |
| icα,L membrane conductance | gCα,L | nS | 1.22844fe + 03 | 7.740700e + 01 |
| Ed,half | mV | | 1.981970e + 01 | 1.880320e + 01 |
| Ed,slope | mV | | -7.279700e + 00 | -5.456900e + 00 |
| τd,const | s | | 1.283300e - 03 | 3.316100e - 03 |
| Ef,half | mV | | 4.000000e + 01 | 3.777770e + 01 |
| Ef,slope | mV | | 6.772400e + 00 | 2.433900e + 00 |
| τf,L,final | s | | 3.862900e - 02 | 2.682100e - 02 |
| Ef,half | mV | | 3.177650e + 01 | 3.007710e + 01 |
| Ef,slope | mV | | 6.052900e + 00 | 2.550100e + 00 |
| Rate coefficient for f2L | αf2L | s-1 | 1.725100e + 00 | 1.270940e + 01 |
| Rate coefficient for f2L | βf2L | s-1 | 3.417983e + 05 | 1.000000e + 04 |
| icα,L, icα,T reversal potential | ECα,rev | mV | 4.118340e + 01 | 3.520120e + 01 |
| iK,r membrane conductance | gK,r | nS | 1.354600e + 00 | 7.463700e + 00 |
| Na+ permeability of iK,r | PKNa,r | | 4.000000e - 02 | 3.912900e - 02 |
| EK,half | mV | | -2.206970e + 01 | -1.534650e + 01 |
| EK,slope | mV | | 1.862420e + 01 | 1.051270e + 01 |
| a1,r | s-1 | | 2.666300e + 00 | 8.468400e - 02 |
| a2,r | mV | | 1.086560e + 01 | 4.456800e + 00 |
| a3,r | mV | | 2.000000e + 01 | 2.000000e + 01 |
| b1,r | s-1 | | 2.188400e + 00 | 6.481100e - 01 |
| b2,r | mV | | 8.165090e + 01 | 1.253405e + 02 |
| b3,r | mV | | 5.000000e + 01 | 4.436800e + 01 |
| iK,s membrane conductance | gK,s | nS | 2.606500e - 01 | 6.358800e - 02 |
| Na+ permeability of iK,s | PKNa,s | | 1.993000e - 02 | 2.305000e - 02 |
| a1,s | s-1 | | 5.000000e - 02 | 5.112000e - 01 |
| a2,s | mV | | -1.135720e + 00 | -6.772300e + 00 |
| a3,s | mV | | 1.511320e + 01 | 3.111270e + 01 |
| b1,s | s-1 | | 5.291100e - 02 | 5.519900e - 02 |
| b2,s | mV | | -1.135720e + 01 | -6.772300e + 00 |
| b3,s | mV | | 8.168200e + 00 | 1.400000e + 01 |
| Scaling parameter for iNaCaKNa | CapA | | 2.652811e + 03 | 2.532443e + 03 |
| icα,T membrane conductance | gCα,T | nS | 9.119000e + 01 | 5.000000e + 01 |
| Na+ conductance of if | gf | nS | 6.413300e + 00 | 7.135600e + 00 |
| K+ conductance of if | Kf | nS | 1.766210e + 01 | 1.230720e + 01 |
| iNa membrane conductance | gNan | nS | 3.268415e + 02 | 2.767960e + 02 |
| Max. Na-K pump current | ip,max | pA | 2.005199e + 02 | 1.500000e + 02 |
| iN,Na membrane conductance | gN,Na | nS | 2.583600e - 01 | 2.283700e - 01 |
| Scaling parameter for iN,K | Kb,Kp | A/mM | 1.400000e - 01 | 6.311600e - 02 |

observed between cells with similar action- potential characteristics. We have proposed that the duration of the inward coupling current phase during action- potential upstroke is a significant factor in achieving frequency entrainment. Specifically, that a longer lasting inward coupling current during action- potential upstroke assists frequency entrainment. Simulation of single cells paced with a simple biphasic artificial coupling current have confirmed that the minimum amplitude of the coupling current required for entrainment \((Q_{\mathrm{crit}})\) decreases as the duration of the inward current phase is increased. We conclude that action- potential heterogeneity within the intact sinoatrial node provides an important mechanism underlying pacemaker synchronization.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
