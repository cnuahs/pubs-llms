```
@article{cloherty2003gradient,
  title={A gradient model of the rabbit sinoatrial node},
  author={Shaun L. Cloherty and Socrates Dokos and Nigel H. Lovell},
  journal={25th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2003},
  volume={1},
  pages={24-27},
  doi={10.1109/iembs.2003.1279487},
  url={https://ieeexplore.ieee.org/document/1279487}
}
```

---

# A GRADIENT MODEL OF THE RABBIT SINOATRIAL NODE

S. L. Cloherty, 
S. Dokos and 
N. H. Lovell

Graduate School of Biomedical Engineering University of New South Wales, Sydney 2052, Australia.

Abstract—We have formulated a gradient model of the rabbit sinoatrial node based on cell- specific ionic models of electrical activity from its central and peripheral regions. The gradient model exhibits a smooth transition in action potential characteristics such as maximum diastolic potential, overshoot potential, upstroke velocity, action potential duration and cycle length, and is suitable for developing higher dimensional models of the right atrium. Spontaneous pacemaker activity is simulated in a one- dimensional monodomain model of the sinoatrial node and adjoining atrial tissue.

Keywords—sinoatrial node, gradient model, monodomain equation

## I. INTRODUCTION

I. INTRODUCTION  I. NITIATION of the heartbeat occurs in a region of specialized pacemaker cells known as the sinoatrial node (SAN). The SAN is a highly complex spatially distributed structure, exhibiting a smooth spatial transition in action potential (AP) characteristics from the center of the node to the periphery [1][2]. Action potentials observed in the periphery of the SAN tend to exhibit an increase (hyperpolarization) in maximum diastolic potential (MDP), an increase in overshoot potential (OS) and upstroke velocity (UV), and a decrease in cycle length (CL) and action potential duration (APD) [2][3].

Kodama and Boyett [2] observed this regional variation in AP characteristics in small electrically isolated tissue specimens ( \(\sim 0.3mm\) in diameter). They concluded that the observed variation in AP characteristics must be the result of a genuine transition in the electrophysiological properties of cells within the SAN and proposed the so called gradient model.

In this paper, we use a custom least squares optimization technique to formulate cell- specific ionic models of pacemaker activity in central and peripheral regions of the SAN. We then formulate a gradient model of the SAN by using this same optimization technique to fit a smooth transition in ionic model parameters to achieve an assumed variation in AP characteristics. The suitability of the resulting gradient model for the development of higher dimensional models of the SAN is then demonstrated by simulating spontaneous activity in a one- dimensional monodomain model of the SAN and adjoining atrial tissue.

## II. METHODS

### A. Cell-Specific Central and Peripheral SAN Ionic Models

The underlying SAN ionic models are based on a generic model of a single rabbit SAN cell including Markov- state kinetic descriptions for 12 membrane currents [4]. The generic single cell ionic model parameters were selected in agreement with published voltage- clamp data. A subset comprising 175 parameters was then fine- tuned via a custom nonlinear least squares optimization procedure [5] to fit AP recordings from central and peripheral regions of the SAN [6]. During the optimization process the model parameters were subject to tight constraints designed to ensure reasonable correlation with the default values and that the peak ion current amplitudes remain in close agreement with experimental observations [4].

### B. A Gradient Model of Central-Peripheral SAN Transition

The central and peripheral SAN cell models can be used as a basis for formulating a gradient model of the SAN. The task at hand is essentially that of determining a suitable interpolation function for the ionic model parameters in the intermediate region between the central and peripheral type cells.

We formulate the problem as follows;

\[P_{\phi} = (1.0 - W(\phi))P_{c} + W(\phi)P_{p} \quad (1)\]

where \(\phi\) is a dimensionless variable \((0.0 \leq \phi \leq 1.0)\) which denotes the point of interest between the central \((\phi = 0.0)\) and peripheral \((\phi = 1.0)\) type cells, \(P_{\phi}\) denotes the interpolated ionic model parameters, \(P_{c}\) and \(P_{p}\) denote the cell- specific central and peripheral SAN cell model parameters, and \(W(\phi)\) denotes an interpolation weight function which varies from 0.0 in the center to 1.0 in the periphery.

We assume the interpolation weight \(W(\phi)\) varies exponentially with \(\phi\) as follows;

\[W(\phi) = \frac{1.0 - \exp(\phi X)}{1.0 - \exp(X)} \quad (2)\]

where \(X\) denotes an unknown parameter vector which determines the shape of the interpolation weight function.

In the present study, the interpolation weight parameter vector \(X\) was adjusted to produce a linear variation in AP characteristics with respect to \(\phi\) using the same nonlinear least

squares optimization technique employed in determining the cell- specific ionic model parameters above.

It should be noted that the assumed linear variation in AP characteristics with respect to \(\phi\) is somewhat arbitrary and does not necessarily translate into a linear variation in AP characteristics with respect to physical distance within the SAN. The mapping from \(\phi\) to physical distance may be nonlinear, in which case the variation in AP characteristics with respect to physical distance would also be nonlinear.

### C. A One-Dimensional Monodomain Model of the SAN

In order to demonstrate the suitability of the gradient model for integration into higher dimensional models of the SAN and surrounding atria, we have implemented a one- dimensional monodomain model of the SAN and adjoining atrial tissue. The fine structure of the SAN is approximated, in a space averaged sense, by the monodomain equation;

\[\nabla \cdot (\sigma \nabla E_{m}) = A_{m}\left(C_{m}\frac{\partial E_{m}}{\partial t} +i_{tot}\right) \quad (3)\]

where \(\sigma\) is the effective conductivity \((nS / mm)\) , \(E_{m}\) is the transmembrane potential \((mV)\) , \(A_{m}\) is the cell surface- to- volume ratio \((mm^{- 1})\) , \(C_{m}\) is the cell specific membrane capacitance \((nF / mm^2)\) , and \(i_{tot}\) is the sum of the transmembrane ionic currents \((pA / mm^2)\) , the kinetics of which are governed by the underlying single cell ionic models.

The one- dimensional model consists of a length \((l_{s})\) of SAN tissue adjoining a length \((l_{a})\) of atrial tissue. The total length of the model was set to \(3.0mm\) , with \(l_{s} = l_{a} = 1.5mm\) .

The SAN region was simulated using the generic SAN cell model mentioned above, with parameters \((P_{\phi})\) assigned according to equation 1, with an assumed linear variation in \(\phi\) with respect to physical distance. Atrial tissue was simulated using the Earm and Noble model of a single rabbit atrial cell [7].

Constant conductivities \(\sigma_{s}\) and \(\sigma_{a}\) were assigned in the SAN and atrial tissue respectively. This resulted in a discontinuity in \(\sigma\) \((\sigma_{s}< \sigma_{a})\) at the boundary between the SAN and atrial regions \((l = l_{s})\) . At this boundary, the diffusion term on the left hand side of equation 3 is undefined. We have therefore imposed a conservation of flux condition at that point given by;

\[\sigma_{s}\nabla E_{m}\big|_{(l - l_{s}) - 0 - } = \sigma_{a}\nabla E_{m}\big|_{(l - l_{s}) - 0 + } \quad (4)\]

Neumann (zero- flux) boundary conditions were imposed at both ends of the one- dimensional model, i.e.,

\[\nabla E_{m}|_{(t = 0,0)} = \nabla E_{m}|_{(t = l_{s} + l_{a})} = 0 \quad (5)\]

In order to ensure the AP propagated successfully into the atrial domain, it was necessary to reduce the surface- to- volume ratio in the atrial tissue by a factor of 1000. This

may reflect an inherent low excitability of the Earm and Noble atrial cell model.

### D. Computational Methods

The simulation code was implemented in C and run on a dual CPU Dell workstation running the GNU/Linux operating system. The ordinary differential equations of the underlying ionic models were evolved using the CVODE solver for stiff systems [8] with a relative error tolerance of \(10^{- 4}\) . The one- dimensional monodomain model of the SAN was solved using a finite- difference approximation of the Laplacian operator with a space step of \(0.1mm\) and a maximum time step of \(0.1ms\) . These values were deemed sufficiently small to ensure a suitably converged solution.

## III. RESULTS

### A. Cell-Specific Central and Peripheral SAN Ionic Models

Fig. 1 shows the simulated APs from the central and peripheral cell ionic models. Also shown are the corresponding experimental recordings (dashed lines) of the transmembrane potential from central and peripheral SAN cells. As can be seen, the correlation between the simulated and recorded transmembrane potential is extremely high, demonstrating the suitability of the optimization technique for optimization of large multivariate systems.

> **Image description.** A line graph titled "Fig. 1" that displays simulated action potentials (APs) over time, comparing a "Peripheral" cell model to a "Central" cell model.
>
> The graph plots the transmembrane potential ($E_m$) on the vertical Y-axis against time on the horizontal X-axis. The Y-axis, labeled "$E_m$ (mV)", ranges from approximately -80 mV to 40 mV. The X-axis, labeled "Time (s)", spans from 0 to 1 second.
>
> Two distinct curves represent the simulated APs:
> 1.  **Peripheral:** Represented by a solid line, this curve shows a characteristic action potential shape. It reaches a peak potential of approximately 30 mV and exhibits a relatively rapid repolarization phase.
> 2.  **Central:** Represented by a dashed line, this curve also shows an action potential shape. It reaches a slightly lower peak potential (around 25 mV) and appears to have a slightly slower repolarization phase compared to the peripheral model.
>
> Both models exhibit two distinct action potentials within the 1-second timeframe, occurring roughly at $t \approx 0.2$ seconds and $t \approx 0.6$ seconds. The visual comparison clearly shows that the peripheral model maintains a higher peak potential and a faster recovery than the central model.
>
> The figure includes the caption: "Fig. 1. Simulated APs from the central and peripheral SAN cell models." The labels "Peripheral" and "Central" are placed directly on the plot to identify the respective lines.

<center>Fig. 1. Simulated APs from the central and peripheral SAN cell models. APs are aligned at the time of maximum UV. The dashed lines show membrane potentials from central and peripheral SAN tissue recorded by Kodama et al. [6](Fig. 3), used in the optimization of the central and peripheral cell model parameters. </center>

Fig. 2 shows simulated APs corresponding to several values of \(\phi\) in equation 1 following optimization of the interpolation weight parameters \((X)\) in equation 2 as described in section II- B. The first AP in each case is shown aligned at the moment of maximum UV to illustrate the variation in APD and CL.

Fig. 3 shows the corresponding variation in AP characteristics (a) MDP and OS, (b) UV, (c) \(\mathrm{APD}_{90}\) and (d) CL) with respect to \(\phi\)

> **Image description.** A line graph titled "Fig. 2. Simulated APs for various values of $\phi$ (see equation 1)." The graph plots the membrane potential (Em) of a simulated cell over time, illustrating how the shape of the action potential (AP) changes based on the parameter $\phi$.
>
> The axes are clearly labeled:
> *   The vertical Y-axis represents the membrane potential, labeled "Em (mV)," with a scale ranging from -80 mV to 40 mV.
> *   The horizontal X-axis represents time, labeled "Time (s)," with a scale ranging from 0.0 to 1.0 seconds.
>
> The main visual content consists of multiple overlapping curves, each representing a simulated action potential for a specific value of $\phi$. A legend in the upper right corner identifies these values: 0.0, 0.2, 0.4, 0.6, 0.8, and 1.0.
>
> All curves exhibit the characteristic shape of an action potential: they begin near the resting potential (around -80 mV), undergo a rapid depolarization (a sharp upward spike), reach a peak, and then undergo repolarization, returning toward the resting potential.
>
> Visually, the curves demonstrate a clear dependence on the value of $\phi$:
> *   The action potentials corresponding to lower values of $\phi$ (e.g., 0.0 and 0.2) appear to have a certain duration and peak height.
> *   As the value of $\phi$ increases (moving toward 1.0), the overall shape and timing of the action potential change, with some curves showing variations in peak amplitude and duration compared to others. The curves are grouped closely together, showing the subtle differences in the simulated APs across the tested range of $\phi$.

<center>Fig. 2. Simulated APs for various values of \(\phi\) (see equation 1). </center>

> **Image description.** The image consists of two technical scientific figures, Fig. 2 and Fig. 3, which display simulated electrophysiological data related to action potentials (APs) and their characteristics as a function of a parameter $\phi$.
>
> **Fig. 2: Simulated APs**
> This figure displays multiple traces representing simulated action potentials (APs) for various values of $\phi$. The traces are plotted on a coordinate system, showing the characteristic spike shape of an action potential. The caption identifies this figure as showing "Simulated APs for various values of $\phi$ (see equation 1)." The traces are arranged sequentially, illustrating how the AP morphology changes across different values of the parameter $\phi$.
>
> **Fig. 3: Variation in AP Characteristics**
> Fig. 3 is a composite figure consisting of a 2x2 grid of line graphs, illustrating the variation of specific AP characteristics with respect to $\phi$ for the gradient model of the SAN. All four panels share a common horizontal axis labeled $\phi$, which ranges from 0.0 to 1.0.
>
> *   **Panel (a): MDP and OS**
>     *   The vertical axis is labeled "MDP and OS (mV)".
>     *   This panel shows two lines representing MDP and OS. Both lines exhibit a relatively flat trend across the range of $\phi$, with minor fluctuations.
>
> *   **Panel (b): UV**
>     *   The vertical axis is labeled "UV (mV/ms)".
>     *   This panel shows a line that demonstrates a clear, steady increasing trend as the value of $\phi$ increases from 0.0 to 1.0.
>
> *   **Panel (c): APD**
>     *   The vertical axis is labeled "APD (ms)".
>     *   This panel shows a line that demonstrates a clear, steady decreasing trend as the value of $\phi$ increases from 0.0 to 1.0.
>
> *   **Panel (d): CL**
>     *   The vertical axis is labeled "CL (ms)".
>     *   This panel shows a line that demonstrates a clear, steady decreasing trend as the value of $\phi$ increases from 0.0 to 1.0.

<center>Fig. 3. Variation in AP characteristics with respect to \(\phi\) for the gradient model of the SAN. (a) MDP and OS, (b) UV, (c) \(\mathrm{APD}_{90}\) and (d) CL. </center>

### C. A One-Dimensional Monodomain Model of the SAN

Fig. 4 shows simulated APs at regular intervals \((\Delta l = 0.1mm)\) along the length of the one- dimensional monodomain model with a gradient in electrophysiological properties as described above.

> **Image description.** A line graph titled "Fig. 4. Simulated APs in the one-dimensional monodomain model," illustrating a series of simulated Action Potentials (APs) over a one-second time period.
>
> The graph features two primary axes:
> *   **The X-axis (Horizontal):** Represents time, labeled "Time (s)," and is scaled from 0.0 to 1.0, with major tick marks at 0.2, 0.4, 0.6, 0.8, and 1.0.
> *   **The Y-axis (Vertical):** Represents the simulated potential (likely membrane potential), with numerical labels visible at 0.0, 1.5, and 3.0.
>
> The data consists of numerous closely spaced, overlapping curves, each representing a simulated Action Potential. These curves exhibit the characteristic shape of an AP: a rapid, sharp upward spike (depolarization), followed by a plateau, and concluding with a rapid downward spike (repolarization). The APs are distributed across the time axis, showing distinct pulses occurring throughout the 1.0-second duration. The overall pattern is a series of sharp, rhythmic electrical events.
>
> The figure caption, located at the bottom of the image, reads: "Fig. 4. Simulated APs in the one-dimensional monodomain model."

<center>Fig. 4. Simulated APs in the one-dimensional monodomain model. </center>

## IV. DISCUSSION

Formulation of the gradient model as described here is a two step process. The first step involves formulation of the ionic models of central and peripheral SAN activity by optimizing generic single cell ionic model parameters to fit experimental recordings of the membrane potential from central and peripheral regions of the SAN (see section II- A). In a second step, the full gradient model may then be derived from these boundary points by assuming a suitable interpolation function and fitting the interpolation weight parameters to produce a desired variation in AP characteristics.

While the resulting gradient model exhibits a range of behavior consistent with experimental observations, it is by no means unique. For any assumed interpolation function, there exists potentially large areas of the parameter space which yield different yet equally valid gradient models of the SAN. Reducing the number of potential solutions to such large scale optimization problems related to biological systems remains an active research focus within our group.

In the context of formulating a robust and accurate gradient model of the SAN, the problem may be suitably constrained by optimizing the gradient model parameters in a single step. In effect optimizing the model parameters to simultaneously fit i) the experimental recordings from central and peripheral regions of the SAN, and ii) the desired transition in AP char

acteristics at intermediate points. Such an approach may be extended to include additional experimental recordings from known spatial locations within the SAN should they become available.

## V. CONCLUSION

We have described a new gradient model of the rabbit SAN based on membrane potential recordings from central and peripheral regions of the SAN. The gradient model formulated here is suitable for integration into higher dimensional models of the SAN and surrounding atrial tissue.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
