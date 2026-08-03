```
@article{cloherty2000simulated,
  title={Simulated Dynamic Interaction of Coupled Sinoatrial Node Pacemaker Cell Pairs},
  author={Shaun Cloherty and Nigel Lovell and Branko Celler and Socrates Dokos},
  journal={22nd Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2000},
  pages={395-397},
  doi={10.1109/iembs.2000.900758},
  url={https://ieeexplore.ieee.org/document/900758} 
}
```

---

# Simulated Dynamic Interaction of Coupled Sinoatrial Node Pacemaker Cell Pairs

Shaun Cloherty \(^{1}\) , Nigel Lovell \(^{1}\) , Branko Celler \(^{2}\) and Socrates Dokos \(^{1}\)

Abstract - Previous modelling studies by other investigators indicates that electrotonic coupling between cells underlies mutual entrainment and synchronization of the intact sinus node. In this study, interaction between a pair of resistively coupled pacemaker cells was investigated using a complex, physiologically accurate model of the single sinoatrial node cell.

Variation in intrinsic cycle length was achieved by multiplying the background sodium conductance \(\mathbf{g}_{\mathrm{Na}}\) by a constant modulating parameter \((0 < \alpha \leq 1.0)\) . For each value of the modulating parameter a single cell was integrated until a steady state was achieved, at which point the model parameters were saved for use as initial conditions in the simulations of coupled cell pairs.

The effect of cycle length and magnitude of coupling resistance on entrainment were investigated. Simulation results are presented demonstrating both simple and complex entrainment phenomena.

Keywords - modeling, sinoatrial node, dynamic interaction, mutual entrainment

## INTRODUCTION

Despite regional variation of intrinsic cell characteristics (notably cycle length) within the sinus node region, rhythmic electrical activity results. Two hypotheses have been proposed to explain this phenomenon; firstly, it was suggested that the coordinated activity of the sinus node was the result of a single dominant pacemaker cell, driving all other pacemaker cells at its higher intrinsic frequency. More recently Michaels et al. [1][2] proposed a "democratic" process in which coordinated activity of the sinus node may be attributed to the equal interaction of all cells.  

In addition to those of Michaels et al., a number of other simulation studies [5], employing a variety of model formulation have appeared in the literature. The single cell model of a rabbit pacemaker cell developed by Dokos et al. [3], exhibits good long term stability, even for simulations spanning several minutes and containing hundreds of action potentials. This makes it a particularly attractive tool for nonlinear dynamics time series analysis of pacemaker synchronization. To this end, we have extended the Dokos et al. model of a single rabbit sinoatrial node cell to include electrical interaction between cells.

## METHODS

## The Single Cell Model

As mentioned above, in simulating the single sinoatrial node cell we have employed the model equations of Dokos et al. [3]. Briefly, the model employs the classic Hodgkin- Huxley parallel conductance formulation, incorporating nine membrane currents, variation in intracellular and extracellular ion concentrations as well as calcium uptake and release from the sarcoplasmic reticulum. The model also includes formulations for modulation of the membrane currents by acetylcholine (ACh).

## Control of Cycle Length

Variation in intrinsic cycle length was achieved by reducing the outward background sodium current \(\mathbf{i}_{\mathrm{b,Na}}\) by a fractional amount, specifically, the channel conductance \(\mathbf{g}_{\mathrm{b,Na}}\) was multiplied by a constant modulating parameter;

\[\mathbf{g}_{\mathrm{b,Na}} = \alpha \mathbf{g}_{\mathrm{b,Na}} \quad (1)\]

where \(\alpha\) is the modulating parameter taking a value in the range \(0 < \alpha \leq 1.0\) , and \(\mathbf{g}_{\mathrm{b,Na}} = 0.24\) nS [3]. For each value of the modulating parameter, suitable initial conditions were obtained by integrating the single cell equations until an approximate steady state was achieved. An approximate steady state was taken as the condition in which no further change in the sinus cycle length was evident. The model parameters corresponding to the steady state were saved and later used as initial conditions in subsequent simulations.

## Cellular Interaction

In modelling the electrotonic interaction between cells, we have adopted the approach taken by Michaels et al. [1]. For a given cell coupled to one or more neighboring cells, the total membrane current is given by the algebraic sum of its individual ion currents and a coupling current \(\mathbf{i}_{\mathrm{c}}\) given by;

\[\mathrm{i}_{\mathrm{c}} = (\mathrm{E} - \mathrm{E}_{\mathrm{m}}) / \mathrm{R}_{\mathrm{c}} \quad (2)\]

where \(\mathbf{E}\) is the cells membrane potential, \(\mathbf{E}_{\mathrm{m}}\) is the membrane potential of its neighboring cell, and \(\mathbf{R}_{\mathrm{c}}\) is the coupling resistance. In the simulations discussed below, the coupling resistance \((\mathbf{R}_{\mathrm{c}})\) was uniformly set to values in the range \(10\mathrm{k}\Omega\) to \(200\mathrm{M}\Omega\) .

## Computational Methods

The model equations were implemented in \(\mathrm{C / C + + }\) with all simulations performed using double precision arithmetic on a PC running the Linux operating system. Numerical integration of the system was performed using the hybrid predictorcorrector method described by Dokos et al. [3], with a relative error tolerance of \(1.0\mathrm{e - 3}\) . The Message Passing Interface (MPI) library [4] was used to facilitate interaction between cells. Use of the MPI library to manage the interaction between cells allows for future extension to larger simulations of \(10\%\) , \(100\%\) or even \(1000\%\) of cells with little or no additional effort. The MPI library also provides the flexibility to distribute the computational load of larger simulations across a number of heterogeneous machines connected by a network.

## RESULTS

## Simulated Action Potentials

Figure 1 shows the simulated spontaneous action potentials of a single cell corresponding to various values of the modulating parameter. The top trace corresponds to the control value i.e. \(\alpha = 1.0\) . As can be seen, prolongation of the intrinsic cycle length by reduction of the background sodium conductance was accompanied by an increase in both the maximum diastolic potential and the action potential overshoot.

> **Image description.** A multi-panel line graph, or trace plot, illustrating simulated spontaneous action potentials for a single cell. The image consists of four distinct horizontal panels stacked vertically, each displaying a single, continuous line representing an action potential cycle over time.
>
> The vertical axis (Y-axis) represents the membrane potential, with the scale changing for each panel. The horizontal axis (X-axis) represents time, though no explicit time markers are visible.
>
> The four panels are labeled on the far left with numerical values, which correspond to the modulating parameter ($\alpha$) for each trace:
> 1.  **Top Panel:** Labeled "385," with a voltage scale ranging from 0.4 to 1.0.
> 2.  **Second Panel:** Labeled "424," with a voltage scale ranging from 0.4 to 1.0.
> 3.  **Third Panel:** Labeled "472," with a voltage scale ranging from 0.4 to 1.0.
> 4.  **Bottom Panel:** Labeled "532," with a voltage scale ranging from 0.4 to 1.0.
>
> Each trace exhibits the characteristic shape of an action potential: a period of stable diastolic potential, followed by a rapid depolarization (upstroke) to a peak, and then a rapid repolarization back toward the diastolic potential.
>
> Visually, as the modulating parameter value increases from 385 (top) to 532 (bottom), the overall shape and timing of the action potential cycles appear to change, consistent with the context that the parameter affects the intrinsic cycle length and potential overshoot. The traces show a consistent pattern of repetitive firing across all four panels.

<center>Figure 1. Simulated spontaneous action potential for a single sinus node cell. Values for the modulating parameter \(\alpha\) are shown to the left, the corresponding cycle length is shown on each trace (cycle lengths are expressed in milliseconds). The horizontal and vertical scales in the lower left hand corner denote \(500\mathrm{mS}\) and \(50\mathrm{mV}\) respectively. </center>

## Mutual Entrainment

A number of simulations were performed with the control cell \((\alpha = 1.0)\) resistively coupled to a slower cell \((\alpha < 1.0)\) over a range of values for the coupling resistance \((\mathbf{R}_{\mathrm{c}})\) . The mean cycle lengths for one set of simulations are shown as a function of \(\log (\mathbf{R}_{\mathrm{c}})\) in figure 2.

Generally speaking, for highly coupled cells (low coupling resistance), the cells were mutually entrained in a 1:1 fashion, with the common cycle length lying somewhere between that of the individual uncoupled cells. As the coupling resistance was increased the cells remained entrained in a 1:1 fashion with a reduced common cycle length. At some point 1:1 entrainment was lost and the cells entered a region of more complex entrainment. Further increasing the coupling resistance reduced the degree of interaction between the cells until all influence was lost, resulting in each cell depolarizing at its intrinsic rate.

The value of the coupling resistance at which 1:1 entrainment was lost decreased with decreasing values of the modulating parameter \(\alpha\) , i.e. for larger differences in intrinsic cycle length (not shown).

> **Image description.** A line graph titled "Figure 2. Mean cycle length of each cell in a coupled pair," illustrating the relationship between the mean cycle length and the logarithm of the coupling resistance (Rc).
>
> The graph features two primary axes:
> *   **Y-axis:** Labeled "Mean Cycle Length," this vertical axis represents the measured cycle length and is scaled from 360 to 540, with major tick marks every 20 units.
> *   **X-axis:** Labeled "Log(Rc)," this horizontal axis represents the logarithm of the coupling resistance and is scaled from 0.5 to 5.5, with major tick marks every 0.5 units.
>
> The data is presented as multiple distinct curves, each representing a different condition or simulation result. The overall trend shows how the mean cycle length changes as the coupling resistance increases (i.e., as Log(Rc) increases).
>
> Key visual patterns observed in the data include:
> 1.  **Low Log(Rc) Range (0.5 to approximately 3.0):** In this initial range, the curves are relatively stable and clustered. Most lines maintain a mean cycle length between approximately 420 and 460.
> 2.  **Transition Region (Approximately 3.0 to 4.0):** A noticeable change occurs in this region. The curves begin to diverge, and the slopes of several lines start to increase, indicating that the mean cycle length is becoming more sensitive to changes in Log(Rc).
> 3.  **High Log(Rc) Range (4.0 to 5.5):** In this final range, the curves generally trend upward. The highest curve rises steeply, reaching the maximum value of 540 at the end of the plotted range. Other curves also show an upward trend, though at varying rates, with some remaining lower than the peak curve.
>
> The graph visually demonstrates that as the coupling resistance (Rc) increases, the mean cycle length of the cells tends to increase, particularly after a critical threshold around Log(Rc) = 3.0.

<center>Figure 2. Mean cycle length of each cell in a coupled pair as a function of the logarithm to base 10 of the coupling resistance \(R_{\mathrm{c}}\) (in \(\mathrm{k}\Omega\) ). The solid line corresponds to the control cell \((\alpha = 1.0)\) with an intrinsic cycle length of 385 msec., the broken line corresponds to the slower cell, with an intrinsic cycle length of 532 msec \((\alpha = 0.4)\) . </center>

## CONCLUSION

In this study, the complex, physiologically accurate model of a single pacemaker cell developed by Dokos et al. [3] was extended to include interaction between cells via resistive pathways. The effects of different degrees of coupling between pairs of pacemaker cells possessing a variety of intrinsic cycle lengths was investigated and the general characteristics of the response described.

# Proceedings of the \(22^{\mathrm{nd}}\) Annual EMBS International Conference, July 23-28, 2000, Chicago IL.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
