```
@article{kameneva2016retinal,
  title={Retinal ganglion cells: mechanisms underlying depolarization block and differential responses to high frequency electrical stimulation of ON and OFF cells},
  author={Tatiana Kameneva and Matias I. Maturana and Alex E. Hadjinicolaou and Shaun L. Cloherty and Michael R. Ibbotson and David B. Grayden and Anthony N. Burkitt and Hamish Meffin},
  journal={Journal of Neural Engineering},
  year={2016},
  volume={13},
  number = {1},
  pages = {016017},
  doi={10.1088/1741-2560/13/1/016017},
  url={https://iopscience.iop.org/article/10.1088/1741-2560/13/1/016017}
}
```

---

# Retinal ganglion cells: mechanisms underlying depolarization block and differential responses to high frequency electrical stimulation of ON and OFF cells

T Kameneva<sup>1</sup>, M I Maturana<sup>1,2</sup>, A E Hadjinicolaou<sup>2,3</sup>, S L Cloherty<sup>1,2,3</sup>, M R Ibbotson<sup>2,3</sup>, D B Grayden<sup>1</sup>, A N Burkitt<sup>1</sup> and H Meffin<sup>2,3</sup>

<sup>1</sup> NeuroEngineering Laboratory, Department of Electrical and Electronic Engineering, The University of Melbourne, Australia  <sup>2</sup> National Vision Research Institute, Australian College of Optometry, Australia  <sup>3</sup> Department Optometry and Vision Sciences, The University of Melbourne, Australia

E- mail: tkam@unimelb.edu.au

Received 4 June 2015, revised 2 December 2015  Accepted for publication 11 December 2015  Published 6 January 2016

## Abstract

Objective. ON and OFF retinal ganglion cells (RGCs) are known to have non- monotonic responses to increasing amplitudes of high frequency \((2\mathrm{kHz})\) biphasic electrical stimulation. That is, an increase in stimulation amplitude causes an increase in the cell's spike rate up to a peak value above which further increases in stimulation amplitude cause the cell to decrease its activity. The peak response for ON and OFF cells occurs at different stimulation amplitudes, which allows differential stimulation of these functional cell types. In this study, we investigate the mechanisms underlying the non- monotonic responses of ON and OFF brisk- transient RGCs and the mechanisms underlying their differential responses. Approach. Using in vitro patch- clamp recordings from rat RGCs, together with simulations of single and multiple compartment Hodgkin- Huxley models, we show that the non- monotonic response to increasing amplitudes of stimulation is due to depolarization block, a change in the membrane potential that prevents the cell from generating action potentials. Main results. We show that the onset for depolarization block depends on the amplitude and frequency of stimulation and reveal the biophysical mechanisms that lead to depolarization block during high frequency stimulation. Our results indicate that differences in transmembrane potassium conductance lead to shifts of the stimulus currents that generate peak spike rates, suggesting that the differential responses of ON and OFF cells may be due to differences in the expression of this current type. We also show that the length of the axon's high sodium channel band (SOCB) affects non- monotonic responses and the stimulation amplitude that leads to the peak spike rate, suggesting that the length of the SOCB is shorter in ON cells. Significance. This may have important implications for stimulation strategies in visual prostheses.

Keywords: neural stimulation, computer simulations, retinal ganglion cells, retinal prostheses, depolarization block

(Some figures may appear in colour only in the online journal)

## 1. Introduction

Electrical stimulation of the retina generates a perception of spots of light called phosphenes in blind patients [1- 6]. Some

patients with retinal prostheses are able to see basic shapes, navigate in a simple environment, and read large font print. All currently available retinal prostheses provide only rudimentary vision; an increased number of the stimulating

> **Image description.** A line graph titled "Figure 1. A diagrammatic illustration of the shift between non..." (the full caption is partially visible) that compares the spike rate responses of two types of retinal neurons: OFF cells and ON cells, across varying stimulation amplitudes.
>
> The graph features two primary axes:
> *   The vertical Y-axis is labeled "Spiking Rate."
> *   The horizontal X-axis is labeled "Stimulation Amplitude."
>
> Two distinct, non-monotonic response curves are plotted:
> 1.  **OFF cell:** Represented by a black line, this curve shows a response that increases, reaches a peak, and then decreases as the stimulation amplitude increases.
> 2.  **ON cell:** Represented by a blue line, this curve also exhibits a non-monotonic response, increasing to a peak and then decreasing.
>
> The graph includes three specific points of comparison marked by vertical dashed lines, labeled $a_1$, $a_0$, and $a_2$ along the X-axis. At each of these points, a black arrow is drawn to illustrate the difference in spike rate between the two cell types.
> *   At $a_1$, the arrow points from the OFF cell curve to the ON cell curve.
> *   At $a_0$, the arrow points from the OFF cell curve to the ON cell curve.
> *   At $a_2$, the arrow points from the OFF cell curve to the ON cell curve.
>
> The top left corner of the image contains a journal citation: "J. Neural Eng. 13 (2016) 016017." The overall visual representation is a technical diagram illustrating how the spike rate difference between ON and OFF cells changes as the stimulation amplitude is varied.

<center>Figure 1. A diagrammatic illustration of the shift between nonmonotonic response curves in ON and OFF cells. Black arrows show the direction of the difference between ON and OFF spike rates at different stimulation amplitude. </center>

electrodes in the devices does not necessarily lead to patients perceiving finer details of an image [5]. To improve the efficacy of current visual prostheses, one approach is to identify stimulation strategies that allow differential stimulation of the various types of neurons in the retina, each of which convey different types of information to the brain during normal vision. This has been investigated experimentally [7- 12] and in simulations [13, 14]. Such strategy may have the potential to increase the spatial and temporal resolution of visual prostheses and provide more natural vision to the implant user.

One approach to improve the efficacy of retinal implants is differential stimulation of ON and OFF retinal ganglion cells (RGCs). RGCs are the output neurons of the retina; their axons form the optic nerve, the pathway by which their signals are transmitted to the brain. Most RGCs can be classified as either ON or OFF cells. The spike rate of ON cell increases when light illuminates the center of the cell's receptive field, while the spike rate of OFF cell increases at light offset. ON and OFF cells have a different balance of excitatory and inhibitory input, and display differences in their intrinsic electrophysiology [15, 16]. While ON and OFF cells respond differentially to light, both RGC types are stimulated simultaneously with conventional biphasic electrical stimulation in patients with a retinal implant [1]. Such simultaneous activation potentially makes it difficult for the visual system to interpret the incoming signals.  

Recently, it was demonstrated that brisk- transient ON and OFF RGCs respond differentially to high frequency \(2\mathrm{kHz}\) biphasic electrical stimulation [10]. Differential responses result from a combination of two effects: a nonmonotonic response to increased amplitudes of high frequency stimulation and the displacement of the peak response of the ON curve with respect to the OFF curve (figure 1). The non- monotonic response curve illustrates that the spike rate of a cell increases up to a peak value above which further increases in the stimulation amplitude cause the cell to gradually shut down its response. Stimulation at a baseline amplitude, \(a_0\) , evokes activity in both types of cells; an increase in stimulation amplitude towards \(a_2\) results in an increase in spike rate in ON cells and a decrease in OFF cell responses. A decrease in stimulation amplitude towards \(a_1\) has the opposite effect.

The mechanisms behind the non- monotonic response curve and the differential responses of ON and OFF RGCs to high frequency stimulation remain unknown [10]. Using computer simulations, Guo et al optimized model parameters to fit the experimental data from Twyford et al [10] and incorporated the detailed morphology of ON and OFF RGCs [17]. Their results suggest that the differences between ON and OFF RGC responses to high frequency \(2\mathrm{kHz}\) stimulation may be due to the unique (unspecified) ionic channel expressions and cell- specific morphologies of the two cell types. The framework presented in our study allows the identification of the specific ionic currents that underlie the differences between ON and OFF cell responses.

Depolarization block is a phenomenon where a change in the neuronal membrane potential leads to the prolonged inability of a cell to generate action potentials. In this paper, we refer to the depolarization block as the transition from a spiking to a non- spiking state as the level of excitation is increased. Depolarization block has been observed in a variety of cell types in response to external excitatory stimuli [7, 18, 19], and to changes in the extracellular environment such as selective chemical and peptide channel blockers [20], and it can explain the therapeutic effect of drugs in treatment of schizophrenia and epilepsy [21- 23].

Experimental evidence suggests that potassium and sodium channels play a role in neuronal depolarization block [20, 24, 25]. Mathematical modeling and computer simulations have also examined the depolarization block in detail and, similarly, lead to the conclusion that the electrophysiological dynamics of the potassium and sodium channels underlie the phenomenon of depolarization block [18, 26, 27].

Depolarization block in response to high frequency electrical stimulation has been examined experimentally [7, 10, 19, 28, 29] and in computer simulations [17, 30- 32]. The unexpected effect of high frequency stimulation was examined first in 1935 when Catell and Gerard showed that high frequency \(5\mathrm{kHz}\) stimulation may lead to a diminished neural response [28]. More recently, Kilmore and Bhadra have shown that high frequency \(2\mathrm{kHz}\) sinusoidal and biphasic currents can produce a reversible nerve block in frog sciatic nerve [29]. In a subsequent paper by the same research group, it was shown using computer simulation that high frequency \(3\mathrm{kHz}\) sinusoidal current injection can block conduction in mammalian peripheral nerves [30]. Modulation of axonal excitability with high frequency biphasic stimulation has been examined by Liu and colleagues using a lumped circuit model of the myelinated axon; their simulations results have shown that the response of neurons can be modulated by high frequency \(5\mathrm{kHz}\) stimulation [31].

We hypothesize that the non- monotonic response to increasing amplitudes of high frequency stimulation is due to depolarization block arising in RGCs at high stimulation amplitudes, and that differences in the sodium or potassium currents of ON and OFF cells determine the stimulation amplitude at which depolarization block occurs leading to

displacement of the peak response between the ON and OFF curves.

The goal of the present study is to investigate the mechanisms underlying differential responses of ON and OFF RGCs to high frequency electrical stimulation. We test the hypothesis that ON and OFF cells have non- monotonic responses to the increased amplitude of high frequency biphasic stimulation due to the phenomenon of depolarization block. We propose that ON and OFF cells have different concentrations of potassium or sodium channels and this difference between ON and OFF cells underlies their differential responses, as observed in recent electrophysiological studies (Twyford et al [10]). We also investigate how the length of the axon sodium channel band (SOCB) and its distance from the soma affect the non- monotonic response curves and the stimulation amplitudes that lead to their maximum spike rate. We use computer simulations, based on the models of Kameneva et al [33] and Maturana et al [34], to investigate the extent to which the experimental data of Twyford et al [10] is consistent with these hypotheses. We collect electrophysiology data from ON \((n = 33)\) and OFF \((n = 54)\) RGCs from Long Evans rats to support our computer simulations results. The amplitude of spontaneous spikes and after- hyperpolarization level of ON and OFF cells are analyzed to infer differences in sodium and potassium currents between these cell types. In addition, the spike amplitudes and after- hyperpolarization levels are compared between different morphological classes of RGCs.

## 2. Methods

### 2.1. Numerical simulations

Morphology. First, a single compartment model is simulated, which consists of a single segment taken as a cylinder with a diameter and length of \(20\mu \mathrm{m}\) , similar to the soma of alphatype RGC. Then, a multiple compartment model is simulated with each model cell segment taken as a cylinder of variable diameter and length. A mouse RGC structure is taken from the NeuroMorpho database [35]: cell ID—Fohlmeister Medium Complex Cell ctt1290a [36]. The cell model exported from NeuroMorpho is divided into compartments representing the dendrites, soma, axon initial segment, SOCB, narrow segment, and distal axon. The soma is a cylinder with a diameter of \(10\mu \mathrm{m}\) and length of \(23\mu \mathrm{m}\) . The imported morphology does not include an axon; the mouse cell morphology was modified to include the distal axon. The distal axon has a diameter of \(1\mu \mathrm{m}\) and length of \(5340\mu \mathrm{m}\) . The initial segment is the proximal portion of the axon leading to the soma and is a cylinder with a diameter of \(1\mu \mathrm{m}\) and length of \(40\mu \mathrm{m}\) . The narrow segment connects to the initial segment \(40\mu \mathrm{m}\) from the soma; this segment is a cylinder with a diameter of \(0.4\mu \mathrm{m}\) and length of \(90\mu \mathrm{m}\) , similar to that used in previous studies [37]. The SOCB is a part of the axon located \(30\mu \mathrm{m}\) proximal to the soma; it is \(40\mu \mathrm{m}\) length and consists of the distal part of the initial segment and the proximal part of the narrow segment. First, the SOCB length and distance from the soma are fixed. Then, the length and distance of the SOCB from the soma are varied to investigate their effects on the stimulus response curves.

the SOCB length and distance from the soma are fixed. Then, the length and distance of the SOCB from the soma are varied to investigate their effects on the stimulus response curves..

Biophysical model. To model neural membrane potential dynamics, the Hodgkin- Huxley- type formalism is used. Sodium, calcium, delayed rectifier potassium, A- type, and Ca- activated potassium currents are included in the model dynamics, similar to Fohlmeister and Miller [38]. In addition, hyperpolarization- activated, T- type low- voltage- activated calcium, and sodium persistent currents are added to the model, based on the results presented in [33]. It has been shown experimentally and in simulations that T- type low- voltage- activated calcium is present in OFF cells and absent in ON cells [33, 39]. We specify in the text the type of the cell that is simulated for each of the results.

The dynamics of the membrane potential, \(V(t)\) , are described by Kirchoff's law using a Hodgkin- Huxley- type equation

\[\begin{array}{rl} & C_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} -\bar{g}_{\mathrm{L}}(V - V_{\mathrm{L}}) - \bar{g}_{\mathrm{Na}}m^{3}h(V - V_{\mathrm{Na}})\\ & \quad -\bar{g}_{\mathrm{Ca}}c^{3}(V - V_{\mathrm{Ca}}) - (\bar{g}_{\mathrm{K}}n^{4} - \bar{g}_{\mathrm{K,A}}a^{3}h_{\mathrm{A}}\\ & \quad -\bar{g}_{\mathrm{K(Ca)}}(V - V_{\mathrm{K}})\\ & \quad -\bar{g}_{\mathrm{h}}l(V - V_{\mathrm{h}}) - \bar{g}_{\mathrm{T}}m_{\mathrm{T}}^{3}h_{\mathrm{T}}(V - V_{\mathrm{T}})\\ & \quad -\bar{g}_{\mathrm{NaP}}p(V - V_{\mathrm{Na}}) - l_{\mathrm{syn}} = l_{\mathrm{stim}}, \end{array} \quad (1)\]

where \(C_{\mathrm{m}}\) is the specific membrane capacitance and \(\bar{g}_{\mathrm{c}}\) is the maximum conductance of the ionic current defined by it subscript \(x\) . The dynamics of leak \((I_{\mathrm{L}})\) , sodium \((I_{\mathrm{Na}})\) , calcium \((I_{\mathrm{Ca}})\) , delayed rectifier potassium \((I_{\mathrm{K}})\) , A- type \((I_{\mathrm{K,A}})\) , Ca- activated potassium \((I_{\mathrm{K(Ca)}})\) , hyperpolarization- activated \((I_{\mathrm{h}})\) , T- type low- voltage- activated calcium \((I_{\mathrm{T}})\) , and sodium persistent \((I_{\mathrm{NaP}})\) currents are given in table 4, and are similar to those used in our earlier study [33]. \(I_{\mathrm{stim}}(t)\) is the stimulation current.

\(I_{\mathrm{syn}}\) is a current created by spontaneous synaptic input and is represented by a stochastic model [40],

\[I_{\mathrm{syn}} = g_{\mathrm{e}}(V - V_{\mathrm{c}}) + g_{\mathrm{i}}(V - V_{\mathrm{i}}), \quad (2)\]

where \(V_{\mathrm{e}}\) and \(V_{\mathrm{i}}\) are the reversal potentials for the excitatory and inhibitory synaptic currents and \(g_{\mathrm{e}}\) and \(g_{\mathrm{i}}\) are the fluctuating excitatory and inhibitory conductances that vary with time

\[\begin{array}{r}\frac{\mathrm{d}g_{\mathrm{e}}}{\mathrm{d}t} = -\frac{(g_{\mathrm{e}} - g_{\mathrm{e0}})}{\tau_{\mathrm{e}}} +F_{\mathrm{i}}\sqrt{D_{\mathrm{e}}},\\ \frac{\mathrm{d}g_{\mathrm{i}}}{\mathrm{d}t} = -\frac{(g_{\mathrm{i}} - g_{\mathrm{i0}})}{\tau_{\mathrm{i}}} +F_{\mathrm{i}}\sqrt{D_{\mathrm{i}}}. \end{array} \quad (4)\]

Here, \(g_{\mathrm{e0}}\) and \(g_{\mathrm{i0}}\) are the average excitatory and inhibitory conductances, and \(\tau_{\mathrm{e}}\) and \(\tau_{\mathrm{i}}\) are time constants. \(F_{\mathrm{i}}\) is Gaussian white noise of zero mean and unit standard deviation. \(D_{\mathrm{e}}\) and \(D_{\mathrm{i}}\) are noise diffusion coefficients estimated from the variance of the noise: \(D_{\mathrm{e / i}} = 2\sigma_{\mathrm{e / i}}^{2} / \tau_{\mathrm{e / i}}\) , where \(\sigma_{\mathrm{e / i}}\) is the standard deviation of the excitatory/inhibitory conductances, respectively. The values for the parameters used to calculate the synaptic input are given in table 1. Experimental data shows that the spiking rate in RGCs without blocking synaptic

Table 1. Parameters used to calculate the synaptic input, \(I_{\mathrm{syn}}\)

| Parameter | SC Value | MC Value |
| :--- | :--- | :--- |
| Excitatory reverse potential | 0 mV | |
| Inhibitory reverse potential | -75 mV | |
| Average excitatory conductance | $1.21 \times 10^{-3} \text{ S cm}^{-2}$ | $6 \times 10^{-7} \text{ S cm}^{-2}$ |
| Average inhibitory conductance | $5.7 \times 10^{-4} \text{ S cm}^{-2}$ | $2 \times 10^{-5} \text{ S cm}^{-2}$ |
| Excitatory time constant | 2.728 ms | |
| Inhibitory time constant | 10.49 ms | |
| Standard deviation of the excitatory conductance | $1 \times 10^{-2} \text{ S cm}^{-2}$ | $1.5 \times 10^{-4} \text{ S cm}^{-2}$ |
| Standard deviation of the inhibitory conductance | $2 \times 10^{-3} \text{ S cm}^{-2}$ | $3 \times 10^{-3} \text{ S cm}^{-2}$ |

SC: Single compartment simulations. MC: Multiple compartment simulations.

Table 2. Simulation parameters.

| Parameter | Value |
| :--- | :--- |
| Temperature | T = 22 °C |
| Specific membrane capacitance | Cm = 1 μF cm⁻² |
| Potassium reversal potential | VK = -70 mV |
| Hyperpolarization-activated current | Vh = 0 mV |
| T-type Calcium reversal potential | VT = 120 mV |
| Sodium reversal potential | VNa = 35 mV |
| Leak reversal potential | Vi = -60 mV |
| Gas constant | R = 8.314 J/(M·K) |
| Faraday's constant | F = 96849 C/M |
| Time constant for the calcium current | τCa = 1.5 ms |
| Depth of the shell for the calcium pump | r = 0.1 μm |
| Calcium dissociation constant | [Ca²⁺]diss = 0.001 mM |
| Calcium residual constant | [Ca²⁺]res = 0.0001 mM |
| Extracellular Calcium ion concentration | [Ca²⁺]k = 1.8 mM |

currents is approximately \(20\mathrm{Hz}\) [15]. The values of \(\sigma_{\mathrm{i}}\) and \(\sigma_{\mathrm{i}}\) in table 1 give approximately \(20\mathrm{Hz}\) spike rates for a modeled multiple compartment neuron and \(35\mathrm{Hz}\) rate for a single compartment neuron. We do not expect our qualitative results to change for different values of the spontaneous rate. The synaptic input current is injected into the soma only as a point process in multiple compartment simulations. Note, the single compartment model soma is larger than the soma in the multiple compartment model.

The gating variables \(x = \{m,h,c,n,a,h_{\mathrm{A}},l,m_{\mathrm{T}},p\}\) of the voltage- gated ion channels operate according to

\[\frac{\mathrm{d}x}{\mathrm{d}t} = -(\alpha_x + \beta_x)x + \alpha_x. \quad (5)\]

The inactivation gating variable, \(h_{\mathrm{T}}\) , for the \(I_{\mathrm{T}}\) current is modeled as having two closed states, as in Wang et al [41],

\[\frac{\mathrm{d}h_{\mathrm{T}}}{\mathrm{d}t} = \alpha_{h_{\mathrm{T}}}(1 - h_{\mathrm{T}} - b) - \beta_{h_{\mathrm{T}}}h_{\mathrm{T}},\]

where \(b\) satisfies

\[\frac{\mathrm{d}b}{\mathrm{d}t} = \beta_{b}(1 - h_{\mathrm{T}} - b) - \alpha_{b}b.\]

Similar to Fohlmeister and Miller [38], the calcium reversal potential, \(V_{\mathrm{Ca}}\) , is allowed to vary with time, according

to cellular calcium dynamics

\[V_{\mathrm{Ca}}(t) = \frac{RT}{2F}\ln \left(\frac{[\mathrm{Ca}^{2 + }]_{\mathrm{ic}}}{[\mathrm{Ca}^{2 + }]_{\mathrm{i}}(t)}\right). \quad (6)\]

All other reversal potentials are fixed (refer to table 2). \(R\) is the gas constant, \(F\) is Faraday's constant, \(T\) is temperature, \([\mathrm{Ca}^{2 + }]_{\mathrm{ic}}\) is the extracellular calcium ion concentration set to a constant value as in Fohlmeister and Miller [38], and \([\mathrm{Ca}^{2 + }]_{\mathrm{i}}\) is the intracellular calcium ion concentration that is varied in response to the calcium current changes

\[\frac{\mathrm{d}[\mathrm{Ca}^{2 + }]_{\mathrm{i}}(t)}{\mathrm{d}t} = \frac{-3I_{\mathrm{Ca}}(t)}{2Fr} -\frac{[\mathrm{Ca}^{2 + }]_{\mathrm{i}}(t) - [\mathrm{Ca}^{2 + }]_{\mathrm{res}}}{T_{\mathrm{Ca}}}, \quad (7)\]

where \(\tau_{\mathrm{Ca}}\) is the time constant for the calcium current, \(r\) is the depth of the shell for the calcium pump beneath the membrane, and \([\mathrm{Ca}^{2 + }]_{\mathrm{res}}\) is the calcium ion residual constant.

The conductance of the Ca- activated potassium channels is modeled as

\[\delta_{K(\mathrm{Ca})}(t) = g_{K(\mathrm{Ca})}\cdot \frac{([\mathrm{Ca}^{2 + }]_{\mathrm{i}}(t) / ([\mathrm{Ca}^{2 + }]_{\mathrm{diss}})^{2}}{1 + ([\mathrm{Ca}^{2 + }]_{\mathrm{i}}(t) / [\mathrm{Ca}^{2 + }]_{\mathrm{diss}})^{2}}, \quad (8)\]

where \(g_{K(\mathrm{Ca})}\) is a constant parameter and \([\mathrm{Ca}^{2 + }]_{\mathrm{diss}}\) is the calcium dissociation constant.

The numerical values for the parameters used in the simulations are given in table 2.

Conductance values used in the simulations are given in table 3. Gating parameters for the voltage- gated ion channels used in the simulations are given in table 4.

Both single compartment and multiple compartment models are simulated in the NEURON environment [42]. A standard Euler integration method is used for the simulations. Since the physiological data used to fit the gating parameters were collected at room temperature [38, 41, 43, 44], all our simulations are run at \(T = 22^{\circ}\mathrm{C}\) . It is not stated at what temperature the data was collected in Twyford et al [10]. The effects of temperature changes on RGC responses to electrical stimulation is discussed in [45]. At higher temperatures, spike widths become narrower, spike amplitudes are higher, response latencies and thresholds are reduced, spontaneous frequency is increased, and spike timing is more consistently locked to the stimulus. These findings do not affect our qualitative results. The spike times are calculated based on the time at which the membrane potential crosses a spiking threshold (20 mV for single compartment simulations, 10 mV for multiple compartment simulations). All parameters are initialized at the resting membrane potential of \(- 65\mathrm{mV}\) .

Table 3. Conductance values used in the simulations unless otherwise stated, (S cm-2).

| | SC | | | | | | | MC | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | Soma | Soma | Dendrites | In.segm. | Narr.segm. | SOCB | Axon | Soma | Soma | Dendrites | In.segm. | Narr.segm. | SOCB | Axon |
| $\bar{g}_{\mathrm{Na}}$ | 0.04 | 0.08 | 0.025 | 0.15 | 0.2 | 0.4 | 0.07 | 0.07 | 0.0015 | 0.002 | 0.0015 | 0 | 0.0015 | 0.018 |
| $\bar{g}_{\mathrm{Ca}}$ | 0.002 | 0.0015 | 0.002 | 0.0015 | 0 | 0.0015 | 0.018 | 0.0015 | 0.002 | 0.0015 | 0 | 0.0015 | 0.018 | 0.018 |
| $\bar{g}_{\mathrm{K}}$ | 0.012 | 0.018 | 0.012 | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 |
| $\bar{g}_{\mathrm{K,A}}$ | 0.0036 | 0.054 | 0.036 | 0 | 0.054 | 0 | 0 | 0.054 | 0 | 0 | 0 | 0 | 0 | 0 |
| $\bar{g}_{\mathrm{K(Ca)}}$ | $5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $10^{-6}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ | $6.5 \times 10^{-5}$ |
| $\bar{g}_{\mathrm{th}}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ | $10^{-7}$ |
| $\bar{g}_{\mathrm{Nap}}$ | $5 \times 10^{-8}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ | $5 \times 10^{-5}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ | $2 \times 10^{-5}$ | $1 \times 10^{-5}$ | $1 \times 10^{-5}$ |
| $\bar{g}_{\mathrm{T}}$ | 0.0004 | $2.15 \times 10^{-4}$ | 10.6 $\times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ | $2.15 \times 10^{-4}$ |
| $\bar{g}_{\mathrm{L}}$ | $5 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ | $2 \times 10^{-3}$ | $1.2 \times 10^{-3}$ |

SC: Single compartment simulations. MC: Multiple compartment simulations. SOCB refers to the high concentration sodium channel band.

Table 4. Gating parameters for voltage-gated ion channels.

| Channel | Parameter | Value |
| :--- | :--- | :--- |
| Na+ channel | $\alpha_m$ | $-0.6(V + 30)$ |
| | $\alpha_h$ | $0.4e^{-(V+50)/20}$ |
| Ca2+ channel | $\alpha_c$ | $-0.3(V + 13)e^{-0.1(V+13) - 1}$ |
| K+ channel | $\alpha_n$ | $-0.02(V + 40)e^{-0.1(V+40) - 1}$ |
| A channel | $\alpha_a$ | $-0.006(V + 90)e^{-0.1(V+90) - 1}$ |
| | $\alpha_h$ | $0.04e^{-(V+70)/20}$ |
| h channel | $\alpha_l$ | $e^{0.08316(V+75)}$ |
| T channel | $\alpha_m$ | $(1.7 + e^{-(V+28.8)/13.5}) - 1$ |
| | $\alpha_h$ | $e^{-(V+160.3)/17.8}$ |
| | $\alpha_b$ | $1 + e^{(V+37.4)/30}$ |
| NaP channel | $\alpha_p$ ($V < -40$) | $\frac{0.025 + 0.14e^{(V+40)/10}}{1 + e^{-(V+48)/10}}$ |
| | $\alpha_p$ ($V > -40$) | $\frac{0.02 + 0.145e^{-(V+40)/10}}{1 + e^{-(V+48)/10}}$ |

After initial simulations indicated an influence of sodium and potassium conductances on the depolarization block, \(\bar{g}_{\mathrm{Na}}\) and \(\bar{g}_{\mathrm{K}}\) were varied in all subsequent simulations. To validate the depolarization block hypothesis, the simulation results are compared to the experimental data of Twyford et al [10], where the responses of ON and OFF cells to high frequency electrical stimulation are investigated. In our simulations, for the ON RGC model, \(\bar{g}_{\mathrm{T}} = 0.5\mathrm{cm}^{- 2}\) , similar to Kameneva et al [33]. For the OFF RGC model, \(\bar{g}_{\mathrm{T}}\) is varied and the value is stated in the text.  

Electrical stimulation. To investigate depolarization block in RGCs, the models of ON and OFF cells are simulated in response to high frequency biphasic pulse train stimulation. Note that the amplitude of stimulation in single compartment simulations should be taken as a qualitative result since the current is applied into a single compartment.

For the multiple compartment model, extracellular stimulation, \(I_{\mathrm{stim}}\) , is used. An extracellular point electrode is placed \(100\mu \mathrm{m}\) directly above the center of the soma, similar to the setup in [10]. The extracellular medium is assumed to be linear and homogeneous. The coupling between the stimulating electrode and the locations in space \((x,y,x)\) is represented by their transfer impedance, \(Z(x,y,z)\) (the potential at \((x,y,z)\) that results when 1 unit of current is

Table 5. Electrical stimulation parameters.

| Parameter | Value |
| :--- | :--- |
| Duration of the cathodic phase | 100 μs |
| Duration of the anodic phase | 100 μs |
| Gap between cathodal and anodal phases | 160 μs unless otherwise stated |
| Gap between anodal and cathodal phases | 140 μs |
| Frequency of stimulation | 2 kHz unless otherwise stated |
| Amplitude of the cathodic and anodic phases | varied |

applied to the electrode). The extracellular potential, \(V_{\mathrm{ext}}\) , at a point \((x, y, z)\) , produced by the stimulus current \(I_{\mathrm{stim}}\) applied through the extracellular electrode is

\[V_{\mathrm{ext}}(x,y,z) = Z(x,y,z)I_{\mathrm{stim}}. \quad (9)\]

The effect of the extracellular potential is taken into account for each segment in the model. The parameters of the stimulation waveform are given in table 5 and are the same as in Twyford et al [10] to allow comparison with the experimental data. To examine the effect of the stimulation amplitude on the depolarization block in RGCs, the amplitude of the cathodic and anodic phases are varied in the simulations.

Gaps between phases are set to give \(2\mathrm{kHz}\) stimulation. In addition to the constant amplitude, charge- balanced pulse train stimulation, the model cells are stimulated with diamond- shaped modulation, similar to those used experimentally by Twyford et al [10]. These stimuli consist of a diamond shaped envelope shown in figure 2; the maximum amplitude of the diamond and the baseline amplitude are varied. This type of stimulation allows differential stimulation of ON and OFF RGCs, as shown in the Results section.

### 2.2. Electrophysiological experiments

Retinal preparation. The experimental procedures conformed with the policies of the National Health and Medical Research Council of Australia and were approved by the Animal Experimentation Ethics Committee of the Faculty of Science, The University of Melbourne. Data were collected from pigmented Long Evans rats \((n = 125\) ; ages 3- 15 months). Rats were anaesthetized with isoflurane (3%- 5% in \(\mathrm{O}_2\) ) and enucleated. Animals were then unheased with an overdose of Sodium Pentabarbitone (350 mg, intracardiac). The vitreous body was removed and the eyecup was cut into several pieces after hemisecting the eyes behind the ora serrata. The retinal pieces were placed in the bottom of a perfusion chamber, RGC layer up (Warner Instruments, Hamden, CT USA, RC- 26GLP). A stainless steel harp and Lycra threads were used to hold the tissue in place (Warner Instruments, CT USA). The retina was perfused (4- 6 ml min- 1) with carbonated Ames' medium (Sigma- Aldrich, St. Louis, MO) at room temperature and mounted in a chamber in an upright microscope (Olympus, BX51WI) with 40x water immersion lenses. The tissue was

> **Image description.** This image is a technical figure consisting of two panels, (a) and (b), which are time-series graphs illustrating a "Biphasic diamond envelope stimulation" waveform used in electrophysiological simulations. Both panels plot the stimulation amplitude ($I_{\text{stim}}$) over time.
>
> **General Structure and Axes:**
> Both graphs share identical axes and visual characteristics:
> *   **Y-axis:** Labeled "Stim Amp $I_{\text{stim}}$ [nA]," representing the stimulation amplitude in nanoamperes. The scale ranges from -10 to 10 nA.
> *   **X-axis:** Labeled "Time [ms]," representing time in milliseconds. The scale ranges from 0 to 700 ms.
> *   **Color and Style:** The data is represented by a solid blue line and shape against a white background.
>
> **Panel (a) Description:**
> Panel (a) displays a large, blue, diamond-shaped envelope superimposed over a series of small, rectangular pulses.
> *   **Envelope Shape:** The envelope starts near 0 nA at time 0 ms, rises sharply to a peak amplitude of approximately +10 nA around 200 ms, descends to a trough of approximately -10 nA around 400 ms, and returns to the baseline of 0 nA at 700 ms.
> *   **Inset:** A smaller inset graph is located in the upper left corner of Panel (a). This inset shows the actual stimulation pulses, which are small, rectangular spikes oscillating between approximately +8 nA and +10 nA, occurring during the rising phase of the main diamond envelope.
>
> **Panel (b) Description:**
> Panel (b) also displays a large, blue, diamond-shaped envelope superimposed over a series of small, rectangular pulses.
> *   **Envelope Shape:** The envelope follows a similar trajectory to Panel (a). It starts near 0 nA at time 0 ms, rises to a peak amplitude of approximately +10 nA around 200 ms, descends to a trough of approximately -8 nA around 400 ms, and returns to the baseline of 0 nA at 700 ms.
> *   **Inset:** Similar to Panel (a), a smaller inset graph is located in the upper left corner of Panel (b). This inset shows the actual stimulation pulses, which are small, rectangular spikes oscillating between approximately +8 nA and +10 nA, occurring during the rising phase of the main diamond envelope.
>
> **Text Transcription:**
> *   Panel Label: (a)
> *   Panel Label: (b)
> *   Y-axis Label: Stim Amp $I_{\text{stim}}$ [nA]
> *   X-axis Label: Time [ms]
> *   Figure Caption (Partial): Figure 2. Biphasic diamond envelope stimulation used in simula...

<center>Figure 2. Biphasic diamond envelope stimulation used in simulations, similar to the experimental data by Twyford et al [10]. Maximum amplitude of the envelope is varied in simulations. (a) An example of diamond stimulation. (b) An example of inverted diamond stimulation. </center>

visualized with infrared optics and viewed on a \(4\mathrm{x}\) magnified monitor.

Physiological data collection and analysis. Recordings were initiated by making a hole in the inner limiting membrane and optic fiber layer. Cells with smooth surfaces and agranular cytoplasm were selected as targets for recording. The electrode internal solution contained (in mM): K- gluconate 115, KCl 5, EGTA 5, HEPES 10, Na- ATP 2, Na- GTP 0.25; (mOsm \(= 273\) , pH \(= 7.3\) ) including Alexa Hydrazide 488 (250 \(\mu \mathrm{m}\) ) and biocytin \((0.5\%)\) . Pipette resistance at the beginning of the recordings was \(3 - 7\mathrm{M}\Omega\) . The pipette voltage in the bath was nulled prior to recording and checked at the end of each recording after clearing the pipette tip with elevated pressure. If the pre- and post- recording potentials differed, the post- recording value was used as the ground potential. A gigaohm seal was attained and the cellular membrane was ruptured. Then the pipette series resistance was measured and compensated with the bridge balance circuit of the amplifier. Resting potentials were corrected for the change in liquid junction potential caused by cell break- in and cell dialysis (liquid junction potential was \(- 5\mathrm{mV}\) ). RGCs were reconstructed using a confocal microscope (Zeiss PASCAL) and classified morphologically using the criteria established by Sun et al (2002) and Huxlin and Goodchild (1997). Each cell was classified as either ON or OFF- center if its dendrites were localized mainly within sublamina a (OFF \(n = 54\) ) or sublamina b (ON \(n = 33\) ) of the inner plexiform layer. The cells that had stratification of the dendrites in both sublamina were classified as ON- OFF \((n = 38)\) and were excluded from the analysis.

Data analysis. Spikes were extracted and analyzed using LabVIEW programs (National Instruments, 2010 and 2011, USA) from the collected traces. For each, an average spike was computed from at least 15 single spikes that were aligned to their peaks. Generally, the individual waveforms of each RGC spike were homogeneous in shape when evoked spontaneously. The maximum amplitude of the action potential, \(V_{\mathrm{max}}\) , and the minimum after- hyperpolarization amplitude (with reference to the resting potential), \(V_{\mathrm{min}}\) , were computed for each spike. The data was plotted by OriginPro (OriginLab, 8.6, USA) and analyzed in Matlab (Mathworks, 2012a, USA).

## 3. Results

### 3.1. Depolarization block. Single compartment simulations

Depolarization block without synaptic noise, \(I_{\mathrm{syn}} = 0\) . To explore the depolarization block in detail, a single compartment neuron is simulated in response to high frequency stimulation and the synaptic input is initially set to zero.  

The response of a modeled ON RGC to high frequency \(2\mathrm{kHz}\) biphasic pulse stimulation is shown in figure 3. There is a gradual increase in spike rate with increasing amplitude of stimulation up to a peak value after which further increases in amplitude lead abruptly to depolarization block and the modeled cell falls silent.

> **Image description.** A line graph titled "Figure 3. Depolarization block in RGCs. Spike rates in response to" displays the relationship between stimulus amplitude and the resulting spiking rate in retinal ganglion cells (RGCs).
>
> The graph features two primary axes:
> *   **Y-axis (Vertical):** Labeled "Spiking Rate [Hz]," ranging from 0 to 300, with major tick marks every 100 Hz.
> *   **X-axis (Horizontal):** Labeled "Stim Amp, $I_{stim}$ [nA]," ranging from 0 to 12, with major tick marks every 2 nA.
>
> The data is represented by a single black curve connecting blue data points (marked with asterisks). The curve shows a positive, non-linear correlation: as the stimulus amplitude ($I_{stim}$) increases, the spiking rate increases. The rate remains low at small stimulus amplitudes, then rises sharply, reaching a peak near the end of the plotted range (around 9-10 nA).
>
> Two vertical green dashed lines are present on the graph, indicating a specific range of interest. The first dashed line is positioned at approximately 8.5 nA, and the second is positioned at approximately 9.5 nA, bracketing the region where the spiking rate reaches its maximum observed value.
>
> Visible text elements include:
> *   **Title/Caption:** "Figure 3. Depolarization block in RGCs. Spike rates in response to"
> *   **Author Attribution:** "T. Kameva et al." (located in the top right corner)
> *   **Axis Labels:** "Spiking Rate [Hz]" and "Stim Amp, $I_{stim}$ [nA]"

<center>Figure 3. Depolarization block in RGCs. Spike rates in response to high frequency \(2\mathrm{kHz}\) stimulation of a modeled ON RGC. The dashed rectangle shows the range of stimulation amplitudes at which bistability in the system is observed (see text for details). Blue stars indicate amplitudes used in figure 4. In simulations, \(\bar{g}_{\mathrm{Na}} = 0.04\mathrm{Scm}^{-2}\) , \(\bar{g}_{\mathrm{K}} = 0.012\mathrm{Scm}^{-2}\) , \(\bar{g}_{\mathrm{T}} = 0\mathrm{Scm}^{-2}\) , all other conductances as in table 3. \(I_{\mathrm{syn}} = 0\) . Spike rate is calculated over 5 s. </center>

The membrane potential dynamics for three representative amplitudes of stimulation (shown by blue stars in figure 3) are illustrated in figure 4 at low temporal resolution (subplots (a), (c) and (e)) and at higher temporal resolution (subplots (b), (d) and (f)). Results show the presence of action potentials riding on top of the oscillations for smaller stimulation amplitudes (subplots (a)–(d)), and only the oscillations at the stimulus frequency for higher amplitudes of stimulation (subplots (e) and (f)).

The stimulation amplitude at which depolarization block is observed depends on the frequency of stimulation (figure 5). The increase in stimulation frequency up to \(2\mathrm{kHz}\) causes the response curves to shift leftward (dotted lines), after which the increase in frequency causes the curves to shift rightward (solid lines). Our results are consistent with the analytical analysis by Pyragas et al [32], which implies that a neuron's response is the same when \(a / \omega\) is constant for \(1 / \omega\) greater than the characteristic time constant of the neuron; \(a\) is the stimulation amplitude and \(\omega\) is the stimulation frequency. Figure 5 illustrates that the solid lines shift in the direction consistent with Pyragas' analysis ( \(1 / \omega\) is large), while the dashed lines shift in the opposite direction and the maximum amplitude of the response decreases ( \(1 / \omega\) is smaller and the conclusions from Pyragas et al do not apply). Results suggest for the neuron simulated in figure 5 that the characteristic time constant is approximately \(1 / \omega = 1 / 2\mathrm{kHz} = 0.5\mathrm{ms}\) . Results show the presence of the depolarization block in RGCs in response to high frequency stimulations and that the onset for depolarization block is dependent upon both the stimulation amplitude and frequency.

The results illustrated in figure 4 are from separate trials for each amplitude of stimulation where the simulation parameters are initialized at \(- 65\mathrm{mV}\) at the beginning of each trial for each stimulation amplitude. Previous theoretical work has indicated that the behavior of the model can depend on the recent history of the membrane potential, i.e. the initial

> **Image description.** A scientific figure, Figure 4, consisting of six time-series line graphs arranged in two columns and three rows, illustrating the membrane potential dynamics of a modeled Retinal Ganglion Cell (RGC) in response to high-frequency stimulation.
>
> The figure is titled "Figure 4. Depolarization block in RGCs. Response of a modeled ON RGC to high frequency 2 kHz stimulation."
>
> **General Graph Features:**
> All six subplots display the "Membrane potential V" on the Y-axis, ranging from -100 mV to 60 mV. The data is represented by continuous blue lines. The graphs are organized into two columns based on temporal resolution:
> 1.  **Left Column (Subplots a, c, e):** Represents low temporal resolution, with the X-axis labeled "Time [ms]" spanning 0 to 500 ms.
> 2.  **Right Column (Subplots b, d, f):** Represents high temporal resolution, with the X-axis labeled "Time [ms]" spanning a zoomed-in range from 200 to 230 ms.
>
> **Detailed Panel Descriptions (Left Column - Low Temporal Resolution):**
> *   **Panel (a):** Shows the response to a 6 nA pulse amplitude. The graph displays a series of rapid, repetitive spikes (action potentials) occurring over the 500 ms duration.
> *   **Panel (c):** Shows the response to a 9 nA pulse amplitude. The spiking pattern is similar to (a) but appears slightly more frequent or robust.
> *   **Panel (e):** Shows the response to a 9.5 nA pulse amplitude. This panel displays a very dense and sustained pattern of spiking activity.
>
> **Detailed Panel Descriptions (Right Column - High Temporal Resolution):**
> These panels provide a magnified view of the spike shapes seen in the corresponding low-resolution panels.
> *   **Panel (b):** Corresponds to 6 nA pulse amplitude. It shows the detailed, sharp depolarization and repolarization of the action potentials.
> *   **Panel (d):** Corresponds to 9 nA pulse amplitude. The spikes are clearly visible and appear slightly larger or more pronounced than those in (b).
> *   **Panel (f):** Corresponds to 9.5 nA pulse amplitude. It shows a highly dense and sustained pattern of spikes, mirroring the activity in panel (e).
>
> **Text and Source Information:**
> *   **Top Left:** "J. Neural Eng. 13 (2016) 01617"
> *   **Top Right:** "T. Kamena et al."
> *   **Bottom Caption:** "Figure 4. Depolarization block in RGCs. Response of a modeled ON RGC to high frequency 2 kHz stimulation. Subplots (a), (c) and (e): low temporal resolution. Subplots (b), (d) and (f): high temporal resolution. Membrane potential dynamics in response to high frequency stimulation with (a) and (b) 6 nA pulse amplitude; (c) and (d) 9 nA pulse amplitude; (e) and (f) 9.5 nA pulse amplitude. In simulations, \(\bar{g}_{\mathrm{NN}} = 0.04 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{K}} = 0.012 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{T}} = 0 \mathrm{S cm}^{-2}\) , all other conductances as in table 3. \(I_{\mathrm{syn}} = 0\) ."

<center>Figure 4. Depolarization block in RGCs. Response of a modeled ON RGC to high frequency 2 kHz stimulation. Subplots (a), (c) and (e): low temporal resolution. Subplots (b), (d) and (f): high temporal resolution. Membrane potential dynamics in response to high frequency stimulation with (a) and (b) 6 nA pulse amplitude; (c) and (d) 9 nA pulse amplitude; (e) and (f) 9.5 nA pulse amplitude. In simulations, \(\bar{g}_{\mathrm{NN}} = 0.04 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{K}} = 0.012 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{T}} = 0 \mathrm{S cm}^{-2}\) , all other conductances as in table 3. \(I_{\mathrm{syn}} = 0\) . </center>  

conditions. To examine this possible effect, a modeled RGC is simulated in response to both continuously increasing and decreasing amplitudes of stimulation (the initialization of the membrane potential for each new amplitude of stimulation is the last value of the membrane potential obtained with the lower amplitude of stimulation). The dynamics of a simulated neuron is illustrated in figure 6 for continuously increasing (subplots (a) and (c)) and decreasing (subplots (b) and (d))

> **Image description.** A line graph titled "Figure 5" that plots the spiking rate of an ON RGC (Rectangular Granule Cell) against the amplitude of a stimulus. The graph illustrates how the frequency of the stimulus affects the required stimulation amplitude to achieve a certain spiking rate.
>
> The graph features two primary axes:
> *   **Y-axis (Vertical):** Labeled "Spiking Rate [Hz]," ranging from 0 to 300.
> *   **X-axis (Horizontal):** Labeled "Stim Amp, $I_{stim}$ [nA]," ranging from 0 to 12.
>
> A legend in the upper left corner identifies eight different frequencies ($\omega$), each corresponding to a specific line style and color:
> *   **Solid Lines (Higher Frequencies):** 2.9 kHz (black), 2.5 kHz (blue), 2.3 kHz (red), 2 kHz (green), and 1.9 kHz (purple).
> *   **Dashed Lines (Lower Frequencies):** 1.4 kHz (dark blue), 1 kHz (light blue), and 0.9 kHz (red).
>
> The data curves exhibit highly non-linear behavior. All lines originate near the origin (0, 0) and rise sharply as the stimulation amplitude increases.
>
> The primary visual pattern observed is the shift in the curves based on frequency:
> 1.  **High Frequency Shift (Solid Lines):** The solid lines, representing higher frequencies (2.9 kHz down to 1.9 kHz), are consistently shifted toward the right. This indicates that for a given spiking rate, a higher stimulation amplitude ($I_{stim}$) is required at higher frequencies.
> 2.  **Low Frequency Shift (Dashed Lines):** The dashed lines, representing lower frequencies (1.4 kHz down to 0.9 kHz), are shifted toward the left. This indicates that lower stimulation amplitudes are sufficient to achieve the same spiking rate at lower frequencies.
>
> The curves generally plateau or show a sharp increase in spiking rate as the stimulation amplitude approaches 10 nA, with the highest spiking rates (approaching 300 Hz) being achieved by the highest frequency (2.9 kHz) at the maximum plotted stimulation amplitude. The curves demonstrate a clear frequency-dependent relationship between stimulus amplitude and neuronal response.

<center>Figure 5. Spike rate for ON RGC as a function of the amplitude of various high frequency stimuli, illustrating a shift in the depolarization block amplitude for different frequencies of stimulation, \(\omega\) indicated in the legend. Solid lines: increase in frequency causes the response curve to shift rightward \((1 / \omega\) is larger than the characteristic time constant of the simulated neuron). Dashed lines: increase in frequency causes the response curve to shift leftward. In simulations, \(\bar{g}_{\mathrm{Na}} = 0.04 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{K}} = 0.012 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{T}} = 0 \mathrm{S cm}^{-2}\) , all other conductances as in table 3. \(I_{\mathrm{syn}} = 0\) . Spike rate is calculated over 5 s. </center>

amplitudes of the stimulation. The representative cell is stimulated with the biphasic pulse stimulation of a constant amplitude for \(200 \mathrm{ms}\) . During each step, 400 pulses are delivered. Green steps in figure 6 show the amplitude of the pulses on the right- hand \(y\) - axis. Note, the simulated neuron continues to spike at a stimulation amplitude of \(8 \mathrm{nA}\) when the stimulation amplitude is increased (figure 6(a)). However, when the amplitude is decreased the same neuron is silent at \(8 \mathrm{nA}\) , but does spike at \(7 \mathrm{nA}\) (figure 6(b)).

This phenomenon is due to a Hopf bifurcation, which is exhibited by Hodgkin- Huxley- type equations. That is, with the varying stimulation amplitude, the system experiences jumps and hysteresis. A detailed theoretical analysis of the bifurcation that occurs in the Hodgkin- Huxley type equations is given by Pyragas et al [32]. The approximate range of the stimulation amplitudes where bistability of the system is observed is shown by the green dashed rectangle in figure 3. This range is frequency- dependent, as illustrated by comparison between subplots (a)–(d) in figure 6. The black arrows in figure 6 indicate the amplitude of stimulation at which the depolarization block occurs. While the depolarization block occurs at \(9.5 \mathrm{nA}\) during the increasing amplitudes of stimulation for the \(2 \mathrm{kHz}\) - frequency stimulation (subplots (a)), the block is observed at \(11 \mathrm{nA}\) for the \(1 \mathrm{kHz}\) - frequency stimulation (subplot (c)). Similar phenomena are observed for the continuously decreasing amplitude of stimulation (compare subplots (b) and (d)). Therefore, the stimulation amplitude at which the depolarization block is observed is related to a Hopf- bifurcation phenomena.

To explore the depolarization block in more detail, simulations are run with all conductances in (1) set to zero except for \(\bar{g}_{\mathrm{Na}}\) , \(\bar{g}_{\mathrm{K}}\) , and \(\bar{g}_{\mathrm{L}}\) . Results show that the incomplete return of the \(\mathrm{Na}^+\) current to a fully de- inactivated state between action potentials (figure 7(c)) and a small activation of the \(\mathrm{K}^+\) current (figure 7(d)) lead to a progressive reduction in the availability of \(\mathrm{Na}^+\) to generate action potentials (figure 7(a)).

Essentially, the time constants of the sodium inactivation variable, \(\tau_h = - 1 / (\alpha_h + \beta_h)\) , and potassium activation variable, \(\tau_n = - 1 / (\alpha_n + \beta_n)\) , prevent these variables from following the rapidly changing stimulation. This leads to passive oscillations of the membrane potential without the activation of ion currents for higher amplitudes of stimulation. This indicates that sodium, potassium, and leak currents are sufficient to produce a depolarization block during high frequency stimulation.

Depolarization block with synaptic noise, \(I_{\mathrm{syn}} \neq 0\) . A single compartment neuron with synaptic noise is simulated in response to high frequency stimulation. A very sharp drop in spike rate is observed in the numerical simulations at high stimulation amplitudes (figure 3 at \(9.5 \mathrm{nA}\) ), which does not replicate the experimental data [10]. Conversely, a gradual decrease in spike rate is observed in experimental data. To investigate the possible causes for this discrepancy, we tested whether the introduction of noise in the form of stochastic synaptic input interacts with the bistability of the system described above to produce a more gradual reduction in spike rate as the amplitude of the stimulation is increased.

The response to high frequency biphasic pulse stimulation of a modeled OFF cell with synaptic input is shown in figure 8(a). The amplitude of the stimulus is held constant during a single trial but varied from trial to trial (from 2 to \(14.75 \mathrm{nA}\) ). The response curve (derived from spike counts) shows a non- monotonic response as a function of stimulation frequency. Note the more gradual decrease in spike rate at higher stimulation amplitudes for a cell with synaptic input (figure 8(a)) compared to a modeled cell without the synaptic input (figure 3). Therefore, the inclusion of stochastic noise to the system causes a more gradual decrease in spike rate from its peak value as the amplitude of the high frequency stimulation increases, i.e., the onset of depolarization block is more gradual.

The decrease in spike rate observed for higher amplitudes of stimulation (from 8 to \(13.75 \mathrm{nA}\) ) is more noticeable for a longer duration of stimulation (such as the spike count over 1 s shown by blue squares in figure 8(a)). The spike count over the first \(250 \mathrm{ms}\) for this amplitude range does not decrease as noticeably (see red diamonds in figure 8(a)). Therefore, the depolarization block occurs at lower stimulation amplitudes for more prolonged durations of stimulation (>1s versus first \(250 \mathrm{ms}\) ).

A raster plot response of the same modeled cell as in figure 8(a) to a range of stimulation amplitudes is illustrated in figure 8(b). Our model does not include an adaptation effect; therefore, the initial increase followed by a gradual

> **Image description.** A complex scientific figure consisting of six time-series line graphs, labeled (a) through (f), illustrating the membrane potential dynamics of a simulated neuron (RGC) under varying stimulation conditions. The figure is titled "Figure 6. The Hopf bifurcation phenomenon in RGCs."
>
> **General Structure and Axes:**
> The six panels are arranged in two columns. Each panel is a line graph with "Time [s]" on the horizontal X-axis, ranging from 0 to 4 seconds. Each panel features a dual Y-axis:
> 1.  **Left Y-axis:** Labeled "Membrane potential [mV]," corresponding to the blue line, which tracks the cell's electrical activity.
> 2.  **Right Y-axis:** Labeled "Stim Amp [mV]," corresponding to the green line, which represents the applied stimulation amplitude.
>
> **Panel Descriptions (Dynamics):**
> The panels are grouped based on whether the stimulation amplitude is increasing or decreasing:
>
> *   **Increasing Stimulation (Panels a, c, e):** These panels show the membrane potential (blue line) responding to a continuously increasing stimulation amplitude (green line).
>     *   In all three panels, the blue line exhibits a "biphasic pulse train," characterized by rapid, repetitive spikes.
>     *   The green line in (a) shows the lowest stimulation amplitude, while the green lines in (c) and (e) show progressively higher stimulation amplitudes.
> *   **Decreasing Stimulation (Panels b, d, f):** These panels show the membrane potential dynamics as the stimulation amplitude (green line) is continuously decreased.
>     *   The blue line in (b) shows the spiking pattern corresponding to the stimulation in (a).
>     *   The blue line in (d) shows the spiking pattern corresponding to the stimulation in (c).
>     *   The blue line in (f) shows the spiking pattern corresponding to the stimulation in (e).
>     *   In panels (b), (d), and (f), as the green line decreases, the blue line transitions from a spiking state to a stable, non-spiking state. Black arrows are used in these panels to indicate the maximum stimulation amplitude at which the cell ceases to spike.
>
> **Text and Labels:**
> The figure includes extensive technical text:
>
> *   **Header:** Top left reads "J. Neur. Eng. 13 01017," and top right reads "T. Kaneva et al."
> *   **Figure Caption:** The detailed caption below the graphs provides specific parameters:
>     *   "Figure 6. The Hopf bifurcation phenomenon in RGCs. Membrane potential dynamics of the same ON RGC as in figure 3 for (a), (c) and (e) continuously increasing and (b), (d) and (f) continuously decreasing amplitude of the biphasic pulse train. Membrane potential is shown in blue (left y-axis). The amplitude of the biphasic pulses is shown in green (right y-axis). During each of the steps, a train of 400 pulses of constant amplitude is delivered. (a) and (b) Cathodal-anodal gap is $60~\mu \mathrm{s}$ (stimulation frequency is $2.5\mathrm{kHz}$ ). (c) and (d) Cathodal-anodal gap is $160~\mu \mathrm{s}$ (stimulation frequency is $2\mathrm{kHz}$ ). (e) and (f) Cathodal-anodal gap is $600~\mu \mathrm{s}$ (stimulation frequency is $1\mathrm{kHz}$ ). Maximum stimulation amplitude at which the cell does not spike is shown by black arrows. In simulations, $g_{\mathrm{Nd}} = 0.04\mathrm{S cm}^{-2}$ , $g_{\mathrm{K}} = 0.012\mathrm{S cm}^{-2}$ , $g_{\mathrm{T}} = 0\mathrm{S cm}^{-2}$ , all other conductances as in table 3. $I_{\mathrm{syn}} = 0$."

<center>Figure 6. The Hopf bifurcation phenomenon in RGCs. Membrane potential dynamics of the same ON RGC as in figure 3 for (a), (c) and (e) continuously increasing and (b), (d) and (f) continuously decreasing amplitude of the biphasic pulse train. Membrane potential is shown in blue (left y-axis). The amplitude of the biphasic pulses is shown in green (right y-axis). During each of the steps, a train of 400 pulses of constant amplitude is delivered. (a) and (b) Cathodal-anodal gap is \(60~\mu \mathrm{s}\) (stimulation frequency is \(2.5\mathrm{kHz}\) ). (c) and (d) Cathodal-anodal gap is \(160~\mu \mathrm{s}\) (stimulation frequency is \(2\mathrm{kHz}\) ). (e) and (f) Cathodal-anodal gap is \(600~\mu \mathrm{s}\) (stimulation frequency is \(1\mathrm{kHz}\) ). Maximum stimulation amplitude at which the cell does not spike is shown by black arrows. In simulations, \(g_{\mathrm{Nd}} = 0.04\mathrm{S cm}^{-2}\) , \(g_{\mathrm{K}} = 0.012\mathrm{S cm}^{-2}\) , \(g_{\mathrm{T}} = 0\mathrm{S cm}^{-2}\) , all other conductances as in table 3. \(I_{\mathrm{syn}} = 0\) . </center>  

decrease in spike rate due to adaptation is not expected with this model. The raster plot reveals that there are periods of spikes followed by periods of suppression during higher amplitudes of stimulation, as observed in the experimental data [10]. This phenomenon is due to the bistability described above. The added synaptic input (modeled as Gaussian white noise) allows the system to jump between two stable states (from clusters of spikes to regions of suppression), i.e. the system experiences jumps and hysteresis.

### 3.2. Different onsets for depolarization block between ON and OFF RGCs. Single compartment simulations

To explore the mechanisms underlying the shift in the peak response between ON and OFF RGCs when high frequency

> **Image description.** A technical figure consisting of five stacked line graphs (panels a through e) that illustrate the results of a biological simulation, likely modeling neuronal activity. All five panels share a common horizontal x-axis labeled "Time [ms]," ranging from 0 to 80 milliseconds.
>
> The graphs display various variables over time, representing the response of a simulated cell to high-frequency electrical stimulation.
>
> *   **Panel (a): Membrane potential, V [mV]**
>     This graph shows the membrane potential of the cell. The line exhibits rapid, high-frequency spikes (action potentials) occurring throughout the 80 ms duration, fluctuating between approximately -60 mV and 40 mV.
>
> *   **Panel (b): Na+ activation, m**
>     This graph tracks the sodium ion activation variable, $m$. The line fluctuates rapidly between 0 and 0.8, showing corresponding changes that align with the spikes observed in the membrane potential in Panel (a).
>
> *   **Panel (c): Na+ inactivation, h**
>     This graph tracks the sodium ion inactivation variable, $h$. Similar to Panel (b), the line fluctuates rapidly between 0 and 0.8, mirroring the dynamic changes in the sodium channels.
>
> *   **Panel (d): K+ activation, n**
>     This graph tracks the potassium ion activation variable, $n$. The line fluctuates rapidly, generally staying between 0 and 0.6, indicating the activation of potassium channels in response to the stimulation.
>
> *   **Panel (e): Stim Amp, I_stim [nA]**
>     This graph represents the high-frequency electrical stimulation applied to the cell. It consists of a series of rectangular pulses (square waves) that are applied at regular intervals, fluctuating between -10 nA and 10 nA.
>
> Visible text includes the journal citation "J. Neural Eng. 13 (2016) 01617" in the top left corner. At the bottom, the caption begins: "Figure 7. Na+, K+ and leak currents are sufficient to produce a..." The overall visual pattern demonstrates how the applied stimulation (e) triggers rapid changes in the ion channel variables (b, c, d), which in turn drive the membrane potential (a) to produce action potentials.

<center>Figure 7. \(\mathrm{Na}^+\) , \(\mathrm{K}^+\) and leak currents are sufficient to produce a depolarization block during high frequency stimulation. (a) Membrane potential, \(V\) , in response to high frequency stimulation. (b) and (c) \(\mathrm{Na}^+\) channel activation and inactivation variables, \(m\) and \(h\) in (1), respectively. (d) \(\mathrm{K}^+\) channel activation variable, \(n\) in (1). (e) High frequency electrical stimulation injected into the simulated cell, \(I_{\mathrm{stim}}\) in (1). In simulations, \(\bar{g}_{\mathrm{cy}} = 0.04 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{K}} = 0.012 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{L}} = 6 \times 10^{-5} \mathrm{S cm}^{-2}\) , all other conductances in (1) are set to zero. \(I_{\mathrm{syn}} = 0\) . </center>

> **Image description.** A two-panel scientific figure, Figure 8, illustrating the effects of synaptic currents on depolarization block in OFF Retinal Ganglion Cells (RGCs). The figure consists of a line graph (a) and a spike raster plot (b).
>
> **Panel (a): Response Curve**
> This panel is a line graph showing the relationship between stimulation amplitude and spiking rate.
> *   **Y-axis:** Labeled "Spiking Rate [Hz]," ranging from 0 to 300.
> *   **X-axis:** Labeled "Stim Amp, $I_{stim}$ [nA]," ranging from 0 to 14.
> *   **Data Lines:** Two distinct lines are plotted:
>     *   A blue line represents the spiking frequency calculated over a full 1 second of simulation. This line shows a sharp increase in spiking rate as stimulation amplitude increases, reaching a peak around 10 to 12 nA, followed by a steep decline.
>     *   A red line represents the spiking frequency calculated over the first 250 milliseconds of simulation. This line follows a similar trend to the blue line but generally remains slightly below it across the range.
> *   **Source:** The name "T. Kamewa et al." is visible in the top right corner.
>
> **Panel (b): Spike Raster Plot**
> This panel is a spike raster plot, showing the timing of individual spikes across different stimulation trials.
> *   **Y-axis:** Lists various stimulation amplitudes (0 nA, 2 nA, 4 nA, 6 nA, 8 nA, 10 nA, 12 nA, 13.75 nA, and 14 nA), representing different experimental conditions or trials.
> *   **X-axis:** Labeled "Time [ms]," ranging from 0 to 1000.
> *   **Data:** Blue dots represent individual spike times. The density of these blue dots increases significantly as the stimulation amplitude increases (moving down the Y-axis), visually demonstrating that higher stimulation amplitudes result in a higher firing rate.
>
> **Text and Labels**
> *   The figure title, located at the bottom left, reads: "Figure 8. Depolarization block in OFF RGCs with added synaptic currents, $I_{syn} \neq 0$."
> *   All axes are clearly labeled with units (Hz, nA, ms).

<center>Figure 8. Depolarization block in OFF RGCs with added synaptic currents, \(I_{\mathrm{syn}} \neq 0\) . (a) Response curve as a function of amplitude of high frequency stimulation. Blue: spiking frequency calculated over 1 s of simulations. Red: spiking frequency calculated over the first 250 ms of simulations. (b) Spike raster plots. The amplitude of the biphasic pulse is set constant over each trial, and is shown to the left of each raster. Spike times are shown by blue dots. In simulations, \(g_{\mathrm{Na}} = 0.13 \mathrm{S cm}^{-2}\) , \(g_{\mathrm{K}} = 0.08 \mathrm{S cm}^{-2}\) , \(g_{\mathrm{T}} = 0.0004 \mathrm{S cm}^{-2}\) , all other conductances as in table 3. Spike rate is calculated over 1 s. Synaptic input parameters as in table 1. </center>

\(2\mathrm{kHz}\) stimulation is applied, T- type calcium, sodium, and potassium conductance values are varied in simulated cells and the response curves are plotted as functions of stimulation amplitude.

Differences between depolarization block in ON and OFF cells without synaptic noise, \(I_{\mathrm{syn}} = 0\) . Previously, it has been shown that the T- type \(\mathrm{Ca}^{2 + }\) current is present in OFF cells and is absent in ON RGCs [39]. To verify that the shift in the response curves between ON and OFF RGCs reported in the experimental study [10] is not due to the difference in the T- type \(\mathrm{Ca}^{2 + }\) conductance, simulations are run with no synaptic currents and with all parameters in (1) fixed except \(\bar{g}_{\mathrm{T}}\) . The results of the simulations are illustrated in figure 9(a). Note that the black line shows the response of the cell with the value of \(\bar{g}_{\mathrm{T}}\) that lies on the boundary of the physiologically plausible range as determined by Kameneva

> **Image description.** This image is a scientific figure consisting of three line graphs, labeled (a), (b), and (c), which illustrate the relationship between stimulation amplitude and spike rate under varying conductance conditions. The figure is titled "Figure 9. Differences in $\mathrm{Na^{+}}$ or $\mathrm{K^{+}}$ conductances both lead to the shift of the response curve when there is no synaptic input in the model, $I_{\mathrm{syn}} = 0$."
>
> The overall structure of the figure is consistent across all three panels:
> *   **Y-axis:** Labeled "Spike Rate [Hz]".
> *   **X-axis:** Labeled "Stim Amp, $I_{stim}$ [nA]".
> *   **Data Representation:** Each panel displays three distinct colored curves (black, blue, and red), each representing a different conductance value.
>
> **Panel (a): Response curves for different values of $\bar{g}_T$**
> This panel shows the spike rate response to stimulation amplitude when the transconductance ($\bar{g}_T$) is varied. The Y-axis ranges from 0 to 300 Hz, and the X-axis ranges from 0 to 12 nA. The three curves are relatively close together, showing a sigmoidal (S-shaped) increase in spike rate. The curves are identified by their respective $\bar{g}_T$ values:
> *   Black line: $\bar{g}_T = 0.001\mathrm{Scm}^{-2}$
> *   Blue line: $\bar{g}_T = 0.0004\mathrm{Scm}^{-2}$
> *   Red line: $\bar{g}_T = 0.5\mathrm{cm}^{-2}$
> The visual pattern suggests that changing $\bar{g}_T$ results in only a minimal shift in the response curves.
>
> **Panel (b): Response curves for different values of $\bar{g}_K$**
> This panel illustrates the effect of varying the potassium conductance ($\bar{g}_K$). The Y-axis ranges from 0 to 300 Hz, and the X-axis ranges from 0 to 12 nA. The curves show a noticeable shift in their peak response. The curves are identified by their $\bar{g}_K$ values:
> *   Black line: $\bar{g}_K = 0.012\mathrm{Scm}^{-2}$
> *   Blue line: $\bar{g}_K = 0.0085\mathrm{Scm}^{-2}$
> *   Red line: $\bar{g}_K = 0.005\mathrm{Scm}^{-2}$
> Arrows are present in this panel, pointing from the red curve toward the black curve, indicating that increasing $\bar{g}_K$ shifts the peak response to higher stimulation amplitudes.
>
> **Panel (c): Response curves for different values of $\bar{g}_{Na}$**
> This panel shows the effect of varying the sodium conductance ($\bar{g}_{Na}$). The Y-axis ranges from 0 to 400 Hz, and the X-axis ranges from 0 to 12 nA. Similar to panel (b), the curves exhibit a clear shift. The curves are identified by their $\bar{g}_{Na}$ values:
> *   Black line: $\bar{g}_{Na} = 0.1\mathrm{Scm}^{-2}$
> *   Blue line: $\bar{g}_{Na} = 0.08\mathrm{Scm}^{-2}$
> *   Red line: $\bar{g}_{Na} = 0.04\mathrm{Scm}^{-2}$
> Arrows are present in this panel, pointing from the red curve toward the black curve, indicating that increasing $\bar{g}_{Na}$ shifts the peak response to higher stimulation amplitudes.
>
> The top left corner of the image contains the journal citation: "J. Neural Eng. 13 (2016) 016017".

<center>Figure 9. Differences in \(\mathrm{Na^{+}}\) or \(\mathrm{K^{+}}\) conductances both lead to the shift of the response curve when there is no synaptic input in the model, \(I_{\mathrm{syn}} = 0\) . (a) Response curves for different values of \(\bar{g}_{\mathrm{T}}\) . Black: \(\bar{g}_{\mathrm{T}} = 0.001\mathrm{Scm}^{-2}\) ; blue: \(\bar{g}_{\mathrm{T}} = 0.0004\mathrm{Scm}^{-2}\) ; red: \(\bar{g}_{\mathrm{T}} = 0.5\mathrm{cm}^{-2}\) . In simulations, \(\bar{g}_{\mathrm{Na}} = 0.04\mathrm{Scm}^{-2}\) , \(\bar{g}_{\mathrm{K}} = 0.012\mathrm{Scm}^{-2}\) . (b) Response curves for different values of \(\bar{g}_{\mathrm{K}}\) . Black: \(\bar{g}_{\mathrm{K}} = 0.012\mathrm{Scm}^{-2}\) ; Blue: \(\bar{g}_{\mathrm{K}} = 0.0085\mathrm{Scm}^{-2}\) ; red: \(\bar{g}_{\mathrm{K}} = 0.005\mathrm{Scm}^{-2}\) . In simulations, \(\bar{g}_{\mathrm{T}} = 0\mathrm{Scm}^{-2}\) , \(\bar{g}_{\mathrm{Na}} = 0.04\mathrm{Scm}^{-2}\) . (c) Response curves for different values of \(\bar{g}_{\mathrm{Na}}\) . Black: \(\bar{g}_{\mathrm{Na}} = 0.1\mathrm{Scm}^{-2}\) ; blue: \(\bar{g}_{\mathrm{Na}} = 0.08\mathrm{Scm}^{-2}\) ; red: \(\bar{g}_{\mathrm{Na}} = 0.04\mathrm{Scm}^{-2}\) . Arrows indicate the direction of the shift in the peak response. In simulations, \(\bar{g}_{\mathrm{T}} = 0\mathrm{Scm}^{-2}\) , \(\bar{g}_{\mathrm{K}} = 0.012\mathrm{Scm}^{-2}\) . (a)-(c) All other conductances as in table 3. Spike rate is calculated over 5 s. </center>

et al [33]. The results show that changing \(\bar{g}_{\mathrm{T}}\) results only in a minimal shift in the response curves.

Based on the results illustrated in figure 7, we hypothesize that differences in potassium or sodium conductances may lead to the shift in the response curve described by Twyford et al [10]. To test this hypothesis, \(\bar{g}_{\mathrm{K}}\) and \(\bar{g}_{\mathrm{Na}}\) values are varied and the resultant response curves are plotted for different stimulation amplitudes (figures 9(b) and (c)). The results show that the response curves are shifted when \(\bar{g}_{\mathrm{K}}\) and \(\bar{g}_{\mathrm{Na}}\) values are varied and there is no synaptic noise in the model. Note that the shift of the response curve

> **Image description.** A scientific line graph consisting of two stacked panels, labeled (a) and (b), illustrating the relationship between stimulation amplitude and spiking rate in a computational model.
>
> **General Information:**
> The figure is titled "Figure 10" and includes a partial caption at the bottom: "Figure 10. Difference in $K^+$ conductance leads to the shift of the...". The source credit "T. Kamewa et al" is visible in the top right corner.
>
> **Panel (a) Description:**
> Panel (a) displays the spiking rate as a function of stimulation amplitude ($I_{Stim}$).
> *   **Y-axis:** Labeled "Spiking Rate [Hz]", ranging from 0 to 150.
> *   **X-axis:** Labeled "Stim Amp, $I_{Stim}$ [nA]", ranging from 0 to 12.
> *   **Data:** Three distinct colored lines (black, blue, and red) are plotted. Each line exhibits a characteristic bell-shaped curve, where the spiking rate increases with stimulation amplitude, reaches a peak, and then decreases.
> *   **Annotation:** An arrow is present on the right side of the graph, pointing toward the increasing stimulation amplitude, and is labeled "$g_K$ increase," indicating the direction of the shift in the response curves.
>
> **Panel (b) Description:**
> Panel (b) also displays the spiking rate as a function of stimulation amplitude, but with different scales and data patterns compared to Panel (a).
> *   **Y-axis:** Labeled "Spiking Rate [Hz]", ranging from 0 to 300.
> *   **X-axis:** Labeled "Stim Amp, $I_{Stim}$ [nA]", ranging from 0 to 15.
> *   **Data:** Three colored lines (black, blue, and red) are plotted. Similar to Panel (a), these lines show a bell-shaped curve, but the overall spiking rates are higher, and the curves extend to a greater stimulation amplitude. No specific arrows or directional labels are present in this panel.
>
> The overall visual presentation uses distinct colors (black, blue, red) to represent different conductance values, demonstrating how changes in these parameters affect the peak spiking rate and the required stimulation amplitude.

<center>Figure 10. Difference in \(\mathrm{K^{+}}\) conductance leads to the shift of the stimulus response curves. Synaptic noise smoothes the effect of the stimulus response curve shift for different values of \(\mathrm{Na^{+}}\) conductance. Simulations with synaptic input, \(I_{\mathrm{syn}} \neq 0\) . (a) Response curves for different values of \(\bar{g}_{\mathrm{K}}\) . Black: \(\bar{g}_{\mathrm{K}} = 0.08\mathrm{Scm}^{-2}\) ; blue: \(\bar{g}_{\mathrm{K}} = 0.06\mathrm{Scm}^{-2}\) ; red: \(\bar{g}_{\mathrm{K}} = 0.04\mathrm{Scm}^{-2}\) . Green: values as in figure 9(b) with added synaptic noise as in table 1, \(\bar{g}_{\mathrm{K}} = 0.012\mathrm{Scm}^{-2}\) . In simulations, \(\bar{g}_{\mathrm{Na}} = 0.04\mathrm{Scm}^{-2}\) . (b) Response curves for different values of \(\bar{g}_{\mathrm{Na}}\) . Black: \(\bar{g}_{\mathrm{Na}} = 0.15\mathrm{Scm}^{-2}\) ; blue: \(\bar{g}_{\mathrm{Na}} = 0.13\mathrm{Scm}^{-2}\) ; red: \(\bar{g}_{\mathrm{Na}} = 0.1\mathrm{Scm}^{-2}\) . In simulations, \(\bar{g}_{\mathrm{K}} = 0.08\mathrm{Scm}^{-2}\) . (a) and (b) \(\bar{g}_{\mathrm{T}} = 0.0004\mathrm{Scm}^{-2}\) , all other conductances as in table 3. Arrow indicates the direction of the shift in the peak response. Synaptic noise parameters as in table 1. Spike rate is calculated over 5 s. </center>

with changes in sodium conductances is not observed when synaptic noise is introduced into the model (see below).

Differences in ON and OFF depolarization block with synaptic noise, \(I_{\mathrm{syn}} \neq 0\) . Although the addition of synaptic input changes the shape of the response curve, it does not affect the relative shift caused by differences in potassium conductances, as identified above (figure 10(a)). Similar to the results above, differences in \(\bar{g}_{\mathrm{K}}\) lead to the shift of the stimulus response curves. Shifts in depolarization block onset caused by changes in the magnitude of potassium conductances persist in the presence of synaptic noise. Addition of the synaptic noise smoothes the effect of the shift in the stimulus response curve when \(\mathrm{Na^{+}}\) conductance is varied (figure 10(b)). Our simulations suggest that the shift in depolarization block onset between ON and OFF RGCs may be due to differences in the magnitude of potassium conductance between these cell types.

Differential stimulation of ON and OFF cells with synaptic noise, \(I_{\mathrm{syn}} \neq 0\) . The shift in the response curves between ON

> **Image description.** A multi-panel scientific figure consisting of three stacked plots (a, b, and c) illustrating the simulated response of ON and OFF cell populations to a specific electrical stimulation envelope.
>
> **Panel (a) and Panel (b): Simulated Cell Population Responses**
> Both panels (a) and (b) are histograms showing the spike count over time.
> *   **Axes:** The vertical axis (Y-axis) is labeled "Spikes" and ranges from 0 to 5. The horizontal axis (X-axis) is labeled "Time" and ranges from 0 to 5 seconds, marked with increments every 0.5 seconds.
> *   **Data:** Both panels display blue vertical bars representing the frequency of spikes. The data shows a general pattern of activity that begins around 0.5 seconds, peaks, and then gradually decreases.
> *   **Annotations:** A prominent red rectangle is overlaid on the time axis in both panels, spanning approximately from 0.5 seconds to 4.5 seconds. This rectangle highlights the time window of interest for differential responses. Panel (a) is labeled "ON" and Panel (b) is labeled "OFF."
>
> **Panel (c): Stimulation Amplitude Envelope**
> Panel (c) is a line graph showing the amplitude of the applied electrical stimulation.
> *   **Axes:** The vertical axis (Y-axis) is labeled "Stim Amp $I_{\text{Stim}}$ [nA]" and ranges from -5 to 5 nanoamperes (nA). The horizontal axis (X-axis) is labeled "Time" and ranges from 0 to 5 seconds.
> *   **Data:** A blue line traces the stimulation amplitude, forming a distinct diamond or envelope shape. The stimulation starts at 0 nA, dips to -5 nA around 1.5 seconds, rises sharply to a peak of 5 nA around 3 seconds, and then dips back down to -5 nA around 4.5 seconds.
> *   **Relationship:** The red rectangles from panels (a) and (b) align temporally with the active, non-zero portion of the stimulation envelope shown in panel (c).
>
> **Text and Metadata**
> *   **Top Left:** The figure includes the text "13 (2016) 016017."
> *   **Labels:** The panels are clearly labeled (a), (b), and (c).
> *   **Units:** Units for the Y-axes include "Spikes" (unitless count) and "nA" (nanoamperes). The X-axis unit is "s" (seconds).
> *   **Technical Context (from visual labels):** The figure describes the response of simulated ON and OFF cell populations to a stimulation with a diamond envelope.

<center>Figure 11. Histogram of simulated ON and OFF cell populations in response to the stimulation with the diamond envelope and synaptic input. (a) ON cell population response, \(\bar{g}_{\mathrm{K}} = 0.08 \mathrm{S cm}^{-2}\) , (b) OFF cell population response, \(\bar{g}_{\mathrm{K}} = 0.012 \mathrm{S cm}^{-2}\) . (c) The amplitude of the intracellular electrical stimulation applied to simulated ON and OFF cells. (a) and (b) \(\bar{g}_{\mathrm{Na}} = 0.04 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{T}} = 0 \mathrm{S cm}^{-2}\) , all other conductances as in table 3. Histogram bin size is 100 ms. To plot a population response, cells are simulated with different level of synaptic noise, \(\sigma_{\mathrm{e}} = 0.01\) ; 0.075; 0.005 \(\mathrm{S cm}^{-2}\) and the results are averaged. All other synaptic noise parameters as in table 1. Red rectangles show the range of amplitudes that leads to differential responses between ON and OFF RGCs. </center>

> **Image description.** A multi-panel technical figure consisting of three stacked graphs, labeled (a), (b), and (c), illustrating the simulated response of ON and OFF cell populations to a specific electrical stimulation over time.
>
> Panel (a) is a histogram showing the "Spikes" count versus "Time" (0 to 5.0 s). The Y-axis ranges from 0 to 5, and the X-axis ranges from 0 to 5.0 s. The data is represented by numerous vertical blue bars, indicating the spike frequency over time. A prominent red rectangle is drawn around the time interval from approximately 1.5 s to 4.0 s, highlighting a specific range of stimulation. The panel is labeled "ON" on the right side.
>
> Panel (b) is also a histogram showing "Spikes" versus "Time" (0 to 5.0 s). The Y-axis ranges from 0 to 10, and the X-axis ranges from 0 to 5.0 s. Similar to panel (a), the data is represented by vertical blue bars. A red rectangle is also drawn around the time interval from approximately 1.5 s to 4.0 s. This panel is labeled "OFF" on the right side.
>
> Panel (c) is a line graph plotting "Stim Amp, $I_{Stim}$ [nA]" against "Time" (0 to 5.0 s). The Y-axis ranges from -5 to 5 nA. The data is represented by a continuous blue line that forms an inverted diamond envelope. The stimulation starts at 0 nA, rises to a positive peak around 1.5 s, drops to a negative trough around 3.0 s, and then rises again to a positive peak around 4.5 s.
>
> Overall, the figure visually compares the spike responses of two different cell populations (ON and OFF) to a specific, time-varying electrical stimulation (the inverted diamond envelope) applied to them. The red rectangles in panels (a) and (b) visually demarcate the time periods corresponding to the stimulation's active phases.

<center>Figure 12. Histogram of simulated ON and OFF cell populations in response to the stimulation with the inverted diamond envelope and synaptic input. (a) ON cells population PSTH response, \(\bar{g}_{\mathrm{K}} = 0.08 \mathrm{S cm}^{-2}\) , (b) OFF cells population PSTH response, \(\bar{g}_{\mathrm{K}} = 0.012 \mathrm{S cm}^{-2}\) . (c) The amplitude of the intracellular electrical stimulation applied to simulated ON and OFF cells. (a) and (b) \(\bar{g}_{\mathrm{Na}} = 0.04 \mathrm{S cm}^{-2}\) , \(\bar{g}_{\mathrm{T}} = 0 \mathrm{S cm}^{-2}\) , all other conductances as in table 3. Histogram bin size is 100 ms. To plot a population response, cells are simulated with different level of synaptic noise, \(\sigma_{\mathrm{e}} = 0.01\) ; 0.075; 0.005 \(\mathrm{S cm}^{-2}\) and the results are averaged. All other synaptic noise parameters as in table 1. Red rectangles show the range of amplitudes that leads to differential responses between ON and OFF RGCs. </center>

and OFF RGCs allows us to find a range of high frequency stimulation amplitudes that lead to differential stimulation of these cell types. It is reasonable to expect that individual cells have a different balance of excitatory and inhibitory inputs. To replicate physiological variability between individual cells, simulations are run with different values of synaptic noise and the results averaged for a population of ON and a population of OFF cells. The post-stimulus time histogram (PSTH) averaged between cells with different synaptic noise levels with the diamond envelope stimulation is shown in figures 11 and 12. Results show that it is possible to modulate the stimulus in such a way that only one type of RGCs is spiking (refer to the area inside red rectangles). Results show that different value of the potassium conductances lead to the differential response. Note, in figures 11 and 12, we set \(\bar{g}_{\mathrm{T}} = 0.5\mathrm{cm}^{- 2}\) for OFF cells (the same as for ON cells) to explore the effect of varying \(\bar{g}_{\mathrm{K}}\) independently. This value does not affect the results and conclusions. Similar to experimental data [10], our results show that during diamond envelope stimulation (inside red rectangles), ON cells increase spiking rate at each diamond, while OFF cells decrease their spiking rate. Note, different baseline amplitude is used in [10], similar to results presented in figures 11 and 12. The inverted diamond stimulation has an opposite effect on ON and OFF RGCs. Based on this experimental evidence [10] and the shift of the response curves in figure 10, our results suggest that potassium conductance is larger in ON than in OFF cells.

### 3.3. Multiple compartment simulations

To confirm that single compartment results hold for multiple compartment models, a multiple compartment neuron with synaptic noise is simulated in response to high frequency stimulation.

Simulations are run for a multiple compartment neuron with added synaptic currents and with all parameters in (1) fixed except \(\bar{g}_{\mathrm{T}}\) . Similar to the single compartment modeling, the results of the simulations indicate that changing T- Type \(\mathrm{Ca}^{2 + }\) conductance does not lead to any significant shifts of the response curves (results not shown).

Similar to the single compartment modeling, we found that varying potassium conductances may lead to the shift of the response curve described by Twyford et al [10] (figure 13). In simulations, all values for the conductances are fixed and the value of \(\bar{g}_{\mathrm{K}}\) is varied in all compartments (figures 13(a) and (b)) or in the dendrites only (figures 13(c) and (d)). The response curves are plotted for different stimulation amplitudes for different values of \(\bar{g}_{\mathrm{K}}\) , refer to figures 13(b) and (d). Figure 13 illustrates that increasing potassium conductance in all compartments or in the dendrites only leads to rightward shifts.

Multiple compartment modeling shows that varying sodium conductance in all compartments or only in the dendrites does not lead to the shift of the response curve (figure 14).  

Differences in the axon high sodium concentration segment length and distance from the soma, may contribute to different neural dynamics in response to electrical stimulation. To investigate this, all conductances are fixed and a multiple compartment neuron is simulated with varying SOCB length and distance from the soma does not affect the sensitivity curve shift (figures 15(a) and (b)). However, different values of the SOCB length cause the shift in the sensitivity curve (figures 15(c) and (d)). Note, this effect is not as strong as the impact of varying potassium conductance. Comparing the direction of the curve shift in figure 15 and the results of the differential stimulation discussed in [10], we suggest that ON RGCs may have shorter SOCB.

### 3.4. Comparison of electrophysiological and simulation results

We recorded from 87 RGCs in rat retina. For cells that did not have any spontaneous activity, we injected a minimum amount of current \((10 - 30\mathrm{pA})\) that was close to spike threshold to obtain a small number of spikes.

Simulation results suggest that potassium conductance is larger in ON cells. This implies that the minimum afterhyperpolarization amplitude (with reference to the resting potential), \(V_{\mathrm{min}}\) , is lower in ON cells. Our experiments confirm this hypothesis, as illustrated in table 6. The mean for all ON cells \((V_{\mathrm{min}}(\mathrm{ON}))\) is \(- 5.98(4.45)\mathrm{mV}\) and the mean for all OFF cells \((V_{\mathrm{min}}(\mathrm{OFF}))\) is \(- 4.23(3.67)\mathrm{mV}\) . Standard deviations are noted in brackets.

The direction of the shift of the simulated response curve illustrated in figure 9(c) indicates that sodium conductance is larger in OFF cells. This implies that the maximum amplitude of the action potential, \(V_{\mathrm{max}}\) , is higher in OFF cells. Our experiments supports this hypothesis, see table 6. Experimental data show that the mean of all ON cells \((V_{\mathrm{max}}(\mathrm{ON}))\) is \(57.5(10.2)\mathrm{mV}\) and the mean of all OFF cells \((V_{\mathrm{max}}(\mathrm{OFF}))\) is \(62.6(11.2)\mathrm{mV}\) . The shift in the stimulus response curve illustrated in figure 9(c) holds for small values of the synaptic noise; however, it is smoothed when the synaptic noise parameters are as in table 5.

The experimental data shows that \(V_{\mathrm{max}}\) (ON) \(< V_{\mathrm{max}}(\mathrm{OFF})\) and \(V_{\mathrm{min}}\) (ON) \(< V_{\mathrm{min}}(\mathrm{OFF})\) when the data is compared separately for each morphological type (table 6). The exception is \(V_{\mathrm{max}}\) for B3 cell, in which data for only one B3i cell was collected. The results presented in [10] are recorded from rabbit brisk- transient cells that correspond to alpha- type cells in cats, and A- type cells in mice. Note, A- type cells in table 6 have smaller standard deviations and more significant difference in \(V_{\mathrm{min}}\) between ON and OFF cells. Student T- test hypothesis shows that the average differences in \(V_{\mathrm{max}}\) and \(V_{\mathrm{min}}\) are significant, \(p = 0.02\) for \(V_{\mathrm{max}}\) and \(p = 0.03\) for \(V_{\mathrm{min}}\) when averaged between all cell types.

## 4. Discussion

In this paper, we show that depolarization block in RGCs in response to high frequency stimulation is consistent with experimental observations in rabbit [10] and rat retina. In

> **Image description.** This image is a scientific figure (Figure 13) consisting of four panels (a, b, c, and d) that illustrate the effect of varying potassium ($K^+$) conductances on the spiking rate of a neuron in response to different stimulus amplitudes. The figure combines 3D surface plots (heatmaps) and 2D line graphs.
>
> **Overall Caption and Context:**
> The caption reads: "Figure 13. Differences in $K^+$ conductances in all compartments or in the dendrites only lead to the shift of the stimulus response curves. Multiple compartment simulations with synaptic input, $I_{\text{syn}} = 0$."
>
> **Panel (a): All Compartments Surface Plot**
> Panel (a) is a 3D surface plot (heatmap) showing the spiking rate as a function of stimulus amplitude and the percentage of $K^+$ conductance in all compartments.
> *   **X-axis:** Stim Amp $I_{\text{stim}}$ (nA), ranging from 0 to 1.5.
> *   **Y-axis:** $\%$ original $g_K$ All Comps, ranging from 50% to 180%.
> *   **Z-axis (Color/Height):** Spiking Rate (Hz), indicated by a color bar ranging from 0 (dark blue) to 600 (red).
> *   **Visual Pattern:** The plot shows a peak response (yellow/red) that shifts slightly as the percentage of $g_K$ increases. An arrow is visible on the surface, indicating the direction of the shift in the peak response.
>
> **Panel (b): All Compartments Response Curves**
> Panel (b) is a 2D line graph showing the spiking rate versus stimulus amplitude for different $K^+$ conductance values in all compartments.
> *   **X-axis:** Stim Amp $I_{\text{stim}}$ (nA), ranging from 0 to 1.5.
> *   **Y-axis:** Spiking Rate (Hz), ranging from 0 to 600.
> *   **Data Curves:** Three distinct curves are plotted:
>     *   A black curve, labeled "$g_K$ increase," showing the highest peak response.
>     *   A blue curve, showing an intermediate peak.
>     *   A red curve, showing the lowest peak response.
>
> **Panel (c): Dendrites Only Surface Plot**
> Panel (c) is a 3D surface plot (heatmap) similar to panel (a), but focusing on $K^+$ conductance variations only in the dendrites.
> *   **X-axis:** Stim Amp $I_{\text{stim}}$ (nA), ranging from 0 to 1.5.
> *   **Y-axis:** $\%$ original $g_K$ Dend Only, ranging from 50% to 180%.
> *   **Z-axis (Color/Height):** Spiking Rate (Hz), indicated by a color bar ranging from 0 (dark blue) to 600 (red).
> *   **Visual Pattern:** Similar to panel (a), the plot displays a color gradient, and an arrow is present, indicating the direction of the shift in the peak response.
>
> **Panel (d): Dendrites Only Response Curves**
> Panel (d) is a 2D line graph showing the spiking rate versus stimulus amplitude for different $K^+$ conductance values specifically in the dendrites.
> *   **X-axis:** Stim Amp $I_{\text{stim}}$ (nA), ranging from 0 to 1.5.
> *   **Y-axis:** Spiking Rate (Hz), ranging from 0 to 600.
> *   **Data Curves:** Three distinct curves are plotted:
>     *   A black curve, labeled "$g_K$ increase," showing the highest peak response.
>     *   A blue curve, showing an intermediate peak.
>     *   A red curve, showing the lowest peak response.

<center>Figure 13. Differences in \(\mathrm{K}^{+}\) conductances in all compartments or in the dendrites only lead to the shift of the stimulus response curves. Multiple compartment simulations with synaptic input, \(I_{\mathrm{syn}} = 0\) . (a) Surface plot representing the spiking rate as a function of stimulus amplitude for different values of potassium conductance, varied equally in all compartments as a percentage of the value in the soma in table 3, e.g. \(\bar{g}_{\mathrm{K}}\) (All Comps) \(50\%\) means \(\bar{g}_{\mathrm{K}} = 0.5\times \bar{g}_{\mathrm{K}}(\mathrm{soma}) = 0.5\times 0.018 = 0.009\) S cm \(^{-2}\) . (b) Response curves for different values of \(\bar{g}_{\mathrm{K}}\) varied equally in all compartments as a percentage of the soma value in table 3. Black: \(\bar{g}_{\mathrm{K}} 110\%\) ; blue: \(\bar{g}_{\mathrm{K}} 80\%\) ; red: \(\bar{g}_{\mathrm{K}} 50\%\) . (c) Surface plot representing the spike rate as a function of stimulus amplitude for different values of potassium conductance in dendrites varying as a percentage of the dendrites value in table 3. (d) Response curves for different values of \(\bar{g}_{\mathrm{K}}\) , varied equally in dendrites as a percentage of the dendrites value in table 3. Black: \(\bar{g}_{\mathrm{K}} 185\%\) ; blue: \(\bar{g}_{\mathrm{K}} 95\%\) ; red: \(\bar{g}_{\mathrm{K}} 50\%\) . (a) and (c) Color bar indicates spiking rate in Hz. All other parameters are fixed as in table 3. Arrows indicate the direction of the shift in the peak response. Synaptic noise parameters as in table 1. Spike rate calculated over 1 s. </center>

particular, it causes the non- monotonic responses observed in ON and OFF RGCs when \(2\mathrm{kHz}\) high frequency electrical stimulation is applied. Results show that the onset for the depolarization block is dependent on the frequency and amplitude of stimulation. We illustrate that by adding synaptic noise to the system, it is possible to obtain a gradual reduction in spike rate with increases in the amplitude of stimulation, as observed by Twyford et al [10]. Our simulations suggest that although ON RGCs differ from OFF RGCs by the absence of T- Type calcium currents, the differences in the ON and OFF cell responses observed by Twyford et al [10] may be primarily due to differences in the magnitude of potassium currents and the length of the SOCB. In particular, we propose that ON RGCs have higher concentrations of potassium channels than OFF cells, and ON RGCs have shorter SOCB length than OFF cells. This may allow differential electrical stimulation of these two cell types, which could have important implications for stimulation strategies in retinal visual prostheses.

The difference in T- type calcium currents has been shown to affect subthreshold oscillations, burst firing, and rebound excitation present (absent) in OFF (ON) cells [33]. However, we find that this current does not lead to the sensitivity curve shift observed in [10]. The results of this study do not contradict the earlier findings of Kameneva et al [33].

While separate ranges for T- type calcium conductance were found for ON and OFF RGCs in [33], here we discuss a relative difference between the potassium conductance of ON and OFF cells and the lengths of the axon high sodium channel segments.

Experimental reports do not agree on the differences in the intrinsic electrophysiology of healthy and degenerate retina. While some studies find that RGCs are inherently stable during degeneration and maintain their intrinsic firing properties [46], others show a degeneration- induced hyperactivity in OFF cells and a decrease in firing rate in ON cells [47]. The activation thresholds in response to electrical stimulation are higher and the response latencies are longer in degenerative retina compared to healthy retina [48, 49]. In addition, extensive neural remodeling occurs during retinal degeneration [50]. The computer simulation approach presented here can be adapted to test the effects of high frequency stimulation in degenerative retina, provided that electrophysiological data can be provided for model fitting.

Clinical use of electrical stimulation has been implemented in various neuroprosthetic devices, including deep brain stimulators and implants in the spinal cord, cortex, retina, and cochlea. Spinal cord stimulation is an approved treatment for chronic neuropathic pain [51]. Deep brain stimulation is used to treat symptoms of movement disorders

> **Image description.** A scientific figure, Figure 14, consisting of four panels (a, b, c, and d) that illustrate the relationship between sodium conductance ($\bar{g}_{\mathrm{Na}}$) and stimulus amplitude ($I_{\mathrm{Stim}}$) on the resulting spiking rate in neural simulations. The figure is presented in a journal format, with text identifying the source and authors.
>
> **Text and Identification:**
> *   **Header:** The top left corner displays "J. Neural Eng. 13 (2016) 01617," and the top right corner displays "T. Kamewa et al."
> *   **Main Caption:** Below the panels, the caption reads: "Figure 14. Differences in $\mathrm{Na}^{+}$ conductances in all compartments or in the dendrites only do not lead to the shift of the stimulus response curves. Multiple compartment simulations with synaptic input, $I_{\mathrm{Syn}} = 0$."
>
> **Visual Components and Panels:**
>
> The figure utilizes two types of visualizations: color-coded heatmaps (panels a and c) and line graphs (panels b and d). A shared color bar is positioned to the right of panels (a) and (c), indicating the "Spiking Rate in Hz," ranging from dark blue (low rate) to bright red (high rate, up to 600 Hz).
>
> *   **Panel (a): All Compartments Heatmap**
>     *   This is a 2D color-coded grid (heatmap).
>     *   The X-axis represents "Stim Amp, $I_{\mathrm{Stim}}$" (Stimulus Amplitude), ranging from 0.5 to 1.5 nA.
>     *   The Y-axis represents "% original $\bar{g}_{\mathrm{Na}}$ All Comps" (Sodium Conductance in All Compartments), ranging from 50% to 180%.
>     *   The visual pattern shows that the highest spiking rates (red/orange) are concentrated in the upper right quadrant, corresponding to high stimulus amplitudes and high percentages of sodium conductance.
>
> *   **Panel (b): All Compartments Line Graph**
>     *   This is a line graph showing the "Spiking Rate [Hz]" on the Y-axis (0 to 600) versus "Stim Amp, $I_{\mathrm{Stim}}$" on the X-axis (0.5 to 1.5 nA).
>     *   Three distinct curves are plotted, representing different sodium conductance levels:
>         *   Black line: $\bar{g}_{\mathrm{Na}} 110\%$
>         *   Blue line: $\bar{g}_{\mathrm{Na}} 80\%$
>         *   Red line: $\bar{g}_{\mathrm{Na}} 50\%$
>     *   All three curves exhibit a bell-shaped response, peaking near 1.0 nA, with the black line consistently showing the highest spike rate.
>
> *   **Panel (c): Dendrites Only Heatmap**
>     *   This is a 2D color-coded grid (heatmap), similar in structure to Panel (a).
>     *   The X-axis is "Stim Amp, $I_{\mathrm{Stim}}$" (0.5 to 1.5 nA).
>     *   The Y-axis is "% original $\bar{g}_{\mathrm{Na}}$ Dend Only" (Sodium Conductance in Dendrites Only), ranging from 50% to 180%.
>     *   The visual pattern shows a similar distribution of high spiking rates (red/orange) in the upper right, indicating that increasing sodium conductance in the dendrites also increases the spike rate.
>
> *   **Panel (d): Dendrites Only Line Graph**
>     *   This is a line graph showing the "Spiking Rate [Hz]" on the Y-axis (0 to 600) versus "Stim Amp, $I_{\mathrm{Stim}}$" on the X-axis (0.5 to 1.5 nA).
>     *   Three distinct curves are plotted, representing different sodium conductance levels:
>         *   Black line: $\bar{g}_{\mathrm{Na}} 185\%$
>         *   Blue line: $\bar{g}_{\mathrm{Na}} 80\%$
>         *   Red line: $\bar{g}_{\mathrm{Na}} 50\%$
>     *   Similar to Panel (b), these curves are bell-shaped, peaking near 1.0 nA, with the black line (185%) showing the highest spike rate.
>
> The overall arrangement places the heatmaps (a and c) on the left and the corresponding line graphs (b and d) on the right, allowing for a direct visual comparison between the continuous color-coded data and the summarized line plots.

<center>Figure 14. Differences in \(\mathrm{Na}^{+}\) conductances in all compartments or in the dendrites only do not lead to the shift of the stimulus response curves. Multiple compartment simulations with synaptic input, \(I_{\mathrm{Syn}} = 0\) . (a) Surface plot representing the spike rate as a function of stimulus amplitude for different values of sodium conductance, varied equally in all compartments as a percentage of the value in the soma in table 3, e.g. \(\bar{g}_{\mathrm{Na}}\) (All Comps) \(50\%\) means \(\bar{g}_{\mathrm{Na}} = 0.5\times \bar{g}_{\mathrm{Na}}(\mathrm{soma}) = 0.5\times 0.018 = 0.009\mathrm{Scm}^{-2}\) . (b) Response curves for different values of \(\bar{g}_{\mathrm{Na}}\) , varied equally in all compartments as a percentage of the soma value in table 3. Black: \(\bar{g}_{\mathrm{Na}} 110\%\) ; blue: \(\bar{g}_{\mathrm{Na}} 80\%\) ; red: \(\bar{g}_{\mathrm{Na}} 50\%\) . (c) Surface plot representing the spiking rate as a function of stimulus amplitude for different value of sodium conductance in dendrites varying as a percentage of the dendrites value in table 3. (d) Response curves for different values of \(\bar{g}_{\mathrm{Na}}\) , varied equally in the dendrites as a percentage of the dendrites soma in table 3. Black: \(\bar{g}_{\mathrm{Na}} 185\%\) ; blue: \(\bar{g}_{\mathrm{Na}} 80\%\) ; red: \(\bar{g}_{\mathrm{Na}} 50\%\) . (a) and (c) Color bar indicates spiking rate in Hz. All other parameters are fixed as in table 3. Synaptic noise parameters as in table 1. Spike rate calculated over 1 s. </center>

such as essential tremor, Parkinson's disease, and dystonia [52], to treat symptoms of psychiatric disorders [53], to modulate neural networks in brain- injured patients with disorders of consciousness [51], and to reduce epileptic seizures [54]. Electrical stimulation of the auditory nerve provides hearing to profoundly deaf people [55] and electrical stimulation of the retina or higher parts of the visual pathway restores a sense of vision to blind patients [1]. Depolarization block has been observed in CA1 pyramidal neurons [18], rat hippocampal slices [21], and in dopamine cells [22, 23]. The methodology presented here can be implemented to explore depolarization block in neural tissue other than the retina. Our approach can be used to find optimal stimulation strategies targeted at a particular type of cortical, thalamic or hippocampal neuron. Physiological models of cortical and thalamic neurons would need to be simulated and the effect of various stimulation parameters on the ionic channel dynamics analyzed. The model presented in this paper could be used to explore in detail the therapeutic effect of high frequency stimulation in the treatments of tremors in patients with Parkinson's disease and to reduce seizures in epilepsy patients [52, 54].  

A systematic mathematical analysis revealed that depolarization block can co- exist with spiking behavior as a bistable system, where the state of the system is dependent on the recent time- history of a neuron [26, 32]. In particular, many neurons can display the presence of two states: 'bursting and tonic spiking' or 'tonic spiking and silence' (e.g., as observed during depolarization block). Dovzhenok and Kuznetsov have shown that the inactivation of sodium current contributes to the bistability of a neuron [26]. Pyragas and colleagues explained the effect of suppressed neuronal activity during high frequency stimulation using the method of averaging to derive an approximate solution to the Hodgkin- Huxley equation at the limit of high frequencies [32]. The authors showed that, for stimulation frequencies above the reciprocal of the neuron's characteristic time scale, the effect of suppression depends on the ratio between the stimulation amplitude and frequency. They also implicate sodium channel inactivation and potassium channel activation in depolarization block.

Here, the extracellular space is assumed to be isotropic; therefore, the extracellular membrane potential is calculated as a linear function of a current applied through an extracellular electrode. Effects of the confined extracellular space and the nonlinearity of the extracellular potentials on the membrane voltage are discussed in [56, 57]. This study employs Hodgkin- Huxley formalism. Other models, including Frankenstein- Huxley, Fitzhugh- Nagumo, and cable equations, have been used to address neural properties in

> **Image description.** This image is a scientific figure, Figure 15, which presents four panels (a, b, c, and d) illustrating the effects of the Spike-Output Compartment Body (SOCB) length and distance from the soma on neuronal stimulus response curves. The figure utilizes a combination of 3D surface plots and 2D line graphs.
>
> **Overall Structure and Labels:**
> The figure is titled "Figure 15. Effects of the SOCB length and distance from the soma on the stimulus response curves. Multiple compartment simulations with synaptic input, $I_{\mathrm{syn}} = 0$." The top left corner includes the journal citation: "J. Neural Eng. 13 (2016) 016017," and the top right corner includes the author attribution: "T. Kamena et al."
>
> **Panels (a) and (c): Surface Plots (Spiking Rate vs. Stimulus)**
> Panels (a) and (c) are 3D surface plots (heatmaps) that visualize the spiking rate as a function of stimulus amplitude and a specific SOCB parameter. Both plots use a color bar on the right to indicate the spiking rate in Hertz (Hz), ranging from 0 (blue) to 600 (red).
>
> *   **Panel (a):** This plot shows the spiking rate versus "Stim, $I_{\text{Stim}}$ [nA]" (on the x-axis, ranging from 0 to 2.0) and "SOCB dist from soma [$\mu$m]" (on the y-axis, ranging from 0 to 100). The surface shows a peak response (red/yellow) centered around $I_{\text{Stim}} = 1.0$ nA, with the peak shifting slightly as the distance from the soma changes.
> *   **Panel (c):** This plot shows the spiking rate versus "Stim, $I_{\text{Stim}}$ [nA]" (on the x-axis, ranging from 0 to 2.0) and "SOCB length [$\mu$m]" (on the y-axis, ranging from 0 to 120). Similar to panel (a), the surface displays a peak response (red/yellow) around $I_{\text{Stim}} = 1.0$ nA, demonstrating how the peak response is affected by the SOCB length.
>
> **Panels (b) and (d): Line Graphs (Spiking Rate vs. Stimulus)**
> Panels (b) and (d) are 2D line graphs that show the spiking rate as a function of stimulus amplitude for specific, fixed values of the SOCB parameter. Both graphs have "Stim, $I_{\text{Stim}}$ [nA]" on the x-axis (0 to 2.0) and "Spiking Rate [Hz]" on the y-axis (0 to 500).
>
> *   **Panel (b):** This panel shows three response curves representing different SOCB distances from the soma. The curves are color-coded: Black ($100~\mu\text{m}$), Blue ($40~\mu\text{m}$), and Red ($10~\mu\text{m}$). All curves exhibit a bell-shaped response, peaking near $I_{\text{Stim}} = 1.0$ nA.
> *   **Panel (d):** This panel shows three response curves representing different SOCB lengths. The curves are color-coded: Black ($130~\mu\text{m}$), Blue ($91~\mu\text{m}$), and Red ($13~\mu\text{m}$). A black arrow is present, pointing toward the curves and labeled "SOCB length increase," indicating the direction in which the peak response shifts as the SOCB length increases.

<center>Figure 15. Effects of the SOCB length and distance from the soma on the stimulus response curves. Multiple compartment simulations with synaptic input, \(I_{\mathrm{syn}} = 0\) . (a) Surface plot representing the spike rate as a function of stimulus amplitude for different values of the SOCB distance from the soma. (b) Response curves for different values of the SOCB distance from the soma. Black: \(100~\mu \mathrm{m}\) ; blue: \(40~\mu \mathrm{m}\) ; red: \(10~\mu \mathrm{m}\) . (c) Surface plot representing the spike rate as a function of stimulus amplitude for different value of the SOCB length. (d) Response curves for different values of the SOCB length. Black: \(130~\mu \mathrm{m}\) ; blue: \(91~\mu \mathrm{m}\) ; red: \(13~\mu \mathrm{m}\) . (a) and (c) Color bar indicates spiking rate in Hz. All other parameters are fixed as in table 3. The arrow indicates the direction of the shift in the peak response. Synaptic noise parameters as in table 1. Spike rate calculated over 1 s. </center>

Table 6. Spike shape feature comparison.

| Type | Vmax (mV) | Vmin (mV) |
| :--- | :--- | :--- |
| A1 (ON) | 59.6 (8.44) | -7.21 (4.31) |
| A2i (ON) | 57.8 (11.7) | -4.48 (2.06) |
| A2o (OFF) | 66.6 (10.3) | -2.47 (1.93) |
| B2 (ON) | 53.8 (10.1) | -6.98 (5.19) |
| B3i (ON) | 61.0 | -7.04 |
| B3o (OFF) | 58.5 (13.6) | -5.8 (1.55) |
| C1 (ON) | 62.0 (9.24) | -6.37 (4.80) |
| C2i (ON) | 65.6 (6.82) | -6.41 (2.69) |
| C2o (OFF) | 61.5 (12.6) | -4.37 (4.44) |
| C3 (ON) | 54.3 (7.60) | -2.45 (3.51) |
| C4 (ON) | 63.9 (14.9) | -7.16 (5.84) |
| C4o (OFF) | 59.1 (8.04) | -6.13 (3.94) |
| ALL ON | 57.5 (10.2) | -5.98 (4.45) |
| ALL OFF | 62.6 (11.2) | -4.23 (3.67) |

response to high frequency stimulation [58]. The Hodgkin- Huxley model is deterministic, so stochastic membrane potential fluctuations are caused only by the synaptic current in our study.

## Acknowledgments

This research was supported by the Australian Research Council through Discovery Grants DE120102210, DP140104533, and

Special Research Initiative (SRI) in Bionic Vision Science and Technology grant to Bionic Vision Australia(BVA). HM and MI acknowledge the support of the ARC Centre of Excellence for Integrative Brain Function (CE140100007).

## References

[1] Shepherd R K, Shivdasani M N, Nayagam D A, Williams C E and Blamey P J 2013 Visual prostheses for the blind Cell 31 562- 71  
[2] Ayton L N et al 2014 First- in- human trial of a novel suprachoroidal retinal prosthesis PLoS One 9 e115239  
[3] Weiland J D, Cho A K and Humayun M S 2011 Retinal prostheses: current clinical results and future needs J. Ophthalmology 118 2227- 37  
[4] Da Cruz L et al Argus II Study Group 2013 The Argus II epiretinal prosthesis system allows letter and word reading and long- term function in patients with profound vision loss Br. J. Ophthalmology 97 632- 6  
[5] Stingl K et al 2013 Artificial vision with wirelessly powered subretinal electronic implant alpha- IMS Proc. R. Soc.: Biol. Sci. 280 20130077  
[6] Hadjinicoloau A E, Meffin H, Maturana M I, Cloherty S L and Ibbotson M R 2015 Prosthetic vision: devices, patient outcomes and retinal research J. Clin. Exp. Optom. 98 395- 410  
[7] Cai C, Ren Q, Desai N J, Rizzo J F III and Fried S I 2011 Response variability to high rates of electric stimulation in retinal ganglion cells J. Neurophysiol. 106 153- 62  
[8] Freeman D K, Eddington D K, Rizzo J F III and Fried S I 2010 Selective activation of neuronal targets with sinusoidal electrical stimulation J. Neurophysiol. 104 2778- 91  
[9] Jepson L H, Hottovy P, Mathieson K, Gunning D E, Dabrowski W, Litke A M and Chichilnisky E J 2013 Focal electrical stimulation of major ganglion cell types in the primate retina for the design of visual prostheses J. Neurosci. 33 7194- 205  
[10] Twyford P, Cai C and Fried S 2014 Differential responses to high- frequency electrical stimulation in ON and OFF retinal ganglion cells J. Neural Eng. 11 025011  
[11] DeMarco P J Jr, Yarbrough G L, Yee C W, McLean G Y, Sagdullaev B T, Ball S L and McCall M A 2007 Stimulation via a subretinally placed prosthetic elicits central activity and induces a trophic effect on visual responses Investigative Ophtalmology Vis. Sci. 48 916- 26  
[12] Eickenscheidt M, Jenkner M, Thewes R, Fromherz P and Zech G 2012 Electrical stimulation of retinal neurons in epiretinal and subretinal configuration using a multicapacitor array J. Neurophysiol. 107 2742- 55  
[13] Tsai D, Chen S, Protti D A, Morley J W, Suaning G J and Lovell N H 2012 Responses of retinal ganglion cells to extracellular electrical stimulation, from single cell to population: model- based analysis PLoS One 7 e53357  
[14] Werginz P, Benav H, Zrenner E and Rattay F 2015 Modeling the response of ON and OFF retinal bipolar cells during electric stimulation Vis. Res. 111 170- 81  
[15] Margolis D J and Detwiler P B 2007 Different mechanisms generate maintained activity in ON and OFF retinal ganglion cells J. Neurosci. 27 5994- 6005  
[16] Margolis D J, Newkirk G, Euler T and Detwiler P B 2008 Functional stability of retinal ganglion cells after degeneration- induced changes in synaptic input J. Neurosci. 28 6526- 36  
[17] Guo T, Lovell N H, Tsai D, Twyford P, Fried S, Morley J W, Suaning G J and Dokos S 2014 Selective activation of ON and OFF retinal ganglion cells to high- frequency electrical stimulation: a computational modeling study Proc. IEEE EMBS Conf. pp 6108- 6111  
[18] Bianchi D, Marasco A, Limongioilo A, Marchetti C, Marie H, Tirozzi B and Migliore M 2012 On the mechanisms underlying the depolarization block in the spiking dynamics of CA1 pyramidal neurons J. Comput. Neurosci. 33 207- 25  
[19] Cai C, Twyford P and Fried S 2013 The response of retinal neurons to high- frequency stimulation J. Neural Eng. 10 036009  
[20] Ji H, Tucker K R, Putzier I, Huertas M A, Horn J P, Canavier C C, Levitan E S and Shepard P D 2012 Functional characterization of ether- a- go- go- related gene potassium channels in midbrain dopamine neurons—implications for a role in depolarization block Eur. J. Neurosci. 36 2906- 16  
[21] Bikson M, Hahn P J, Fox J E and Jefferys J G 2003 Depolarization block of neurons during maintenance of electrographic seizures J. Neurophysiol. 90 2402- 8  
[22] Grace A A 1992 The depolarization block hypothesis of neuroleptic action: implications for the etiology and treatment of schizophrenia J. Neural Transm. 36 91- 131  
[23] Valenti O, Cifelli P, Gill K M and Grace A A 2011 Antipsychotic drugs rapidly induce dopamine neuron depolarization block in a developmental rat model of schizophrenia J. Neurosci. 31 12330- 8  
[24] Tucker K R, Huertas M A, Horn J P, Canavier C C and Levitan E S 2012 Pacemaker rate and depolarization block in nigral dopamine neurons: a somatic sodium channel balancing act J. Neurosci. 32 14519- 31  
[25] Ackermann D M, Bhadra N, Gerges M and Thomas P J 2011 Dynamics and sensitivity analysis of high- frequency conduction block J. Neural Eng. 8 065007  
[26] Dovzhenok A and Kuznetsov A S 2012 Exploring neuronal bistability at the depolarization block PLoS One 7 e42811  
[27] Qian K, Yu N, Tucker K R, Levitan E S and Canavier C C 2014 Mathematical analysis of depolarization block mediated by slow inactivation of fast sodium channels in midbrain dopamine neurons J. Neurophysiol. 112 2779- 90  
[28] Cattell M and Gerard R W 1935 The inhibitory effect of high- frequency stimulation and the excitation state of nerve J. Physiol. 83 407- 15  
[29] Kilgore K L and Bhadra N 2004 Nerve conduction block utilising high- frequency alternating current Med. Biol. Eng. Comput. 42 394- 406  
[30] Bhadra N, Lahowetz E A, Foldes S T and Kilgore K L 2007 Simulation of high- frequency sinusoidal electrical block of mammalian myelinated axons J. Comput. Neurosci. 22 313- 26  
[31] Liu H, Roppolo J R, de Groat W C and Tai C 2009 Modulation of axonal excitability by high- frequency biphasic electrical current IEEE Trans. Biomed. Eng. 56 2167- 76  
[32] Pyragas K, Novicenko V and Tass P A 2013 Mechanism of suppression of sustained neuronal spiking under high- frequency stimulation Biol. Cybern. 107 669- 84  
[33] Kameneva T, Meflin H and Burkitt A N 2011 Modelling intrinsic electrophysiological properties of ON and OFF retinal ganglion cells J. Comput. Neurosci. 31 547- 61  
[34] Maturana M I, Kameneva T, Burkitt A N, Meflin H and Grayden D B 2014 The effect of morphology upon electrophysiological responses of retinal ganglion cells: simulation results J. Comput. Neurosci. 36 157- 75  
[35] Ascoli G A, Donohue D E and Halavi M 2007 Neuromorpho. org: a central resource for neuronal morphologies J. Neurosci. 27 9247- 51  
[36] Coombs J, van der List D, Wang G Y and Chalupa L M 2006 Morphological properties of mouse retinal ganglion cells J. Neurosci. 140 123- 36  
[37] Toris C B, Eiesland J L and Miller R F 1995 Morphology of ganglion cells in the neotenuus tiger salamander retina J. Comparative Neurology 352 535- 59  
[38] Fohlmeister J F and Miller R F 1997 Mechanisms by which cell geometry controls repetitive impulse firing in retinal ganglion cells J. Neurophysiol. 78 1948- 64  
[39] Margolis D J, Gartland A J, Euler T and Detwiler P B 2010 Dendritic calcium signaling in ON and OFF mouse retinal ganglion cells J. Neurosci. 30 7127- 38  
[40] Destexhe A, Rudolph M, Fellows J M and Sejnowski T J 2001 Fluctuating synaptic conductances recreate in vivo- like activity in neocortical neurons J. Neurosci. 107 13- 24  
[41] Wang X J, Rinzel J and Rogawski M 1991 A model of the T- type calcium current and the low- threshold spike in thalamic neurons J. Neurophysiol. 66 839- 50  
[42] Carnevale N T and Hines M L 2006 The Neuron Book (Cambridge: Cambridge University Press)[43] Van Welie I, Remme M W, Van Hooft J A and Wadman W J 2006 Different levels of Ih determine distinct temporal integration in bursting and regular- spiking neurons in rat subiculum J. Physiol. 576 203- 14  
[44] Traub R D, Buhl E H, Gloveli T and Whittington M A 2003 Fast rhythmic bursting can be induced in layer 2/3 cortical neurons by enhancing persistent Na+ conductance or by blocking BK channels J. Neurophysiol. 89 909- 21  
[45] Maturana M I, Apollo N V, Garrett D J, Kameneva T, Meflin H, Ibbotson M R, Cloherty S L and Grayden D B 2015 The effects of temperature changes on retinal ganglion cell responses to electrical stimulation Proc. IEEE EMBS Conf. pp 1- 4  
[46] Margolis D J, Newkirk G, Euler T and Detwiler P B 2008 Functional stability of retinal ganglion cells after degeneration- induced changes in synaptic input J. Neurosci. 28 6526- 36  
[47] Sekirmjak C, Jepson L H, Hottowy P, Sher A, Dabrowski W, Litke A M and Chichilnisky E J 2011 Changes in physiological properties of rat ganglion cells during retinal degeneration J. Neurophysiol. 105 2560- 71  
[48] Jensen R J and Rizzo J F III 2008 Activation of retinal ganglion cells in wild-type and rd1 mice through electrical stimulation of the retinal neural network Vis. Res. 48 1562- 8  
[49] O'Hearn T M, Sadda S R, Weiland J D, Maia M, Margalit E and Humayun M S 2006 Electrical stimulation in normal and retinal degeneration (rd1) isolated mouse retina Vis. Res. 46 3198- 204  
[50] Marc R E, Jones B W, Watt C B and Strettoi E 2003 Neural remodeling in retinal degeneration Prog. Retinal Eye Res. 22 607- 55  
[51] Smith H, van Kleef M, Holsheimer J and Joosten E A 2012 Experimental spinal cord stimulation and neuropathic pain: mechanism of action, technical aspects, and effectiveness Spinal Cord Stimulation Neuropathic Pain 13 154- 68  
[52] Bronstein J M et al 2010 Deep brain stimulation for Parkinson disease Arch. Neurology 68 165- 71  
[53] Holtzheimer P E and Mayberg H S 2011 Deep brain stimulation for psychiatric disorders Annu. Rev. Neurosci. 34 289- 307  
[54] Halpern C H, Samadani U, Litt B, Jaggi J L and Baltuch G H 2008 Deep brain stimulation for epilepsy Neurotherapeutics 5 59- 67  
[55] Clark G M 2015 The multi- channel cochlear implant: multidisciplinary development of electrical stimulation of the cochlea and the resulting clinical benefit Hear. Res. 322 4- 13  
[56] Meffin H, Tahayori B, Sergeev E N, Mareels I M Y, Grayden D B and Burkitt A N 2014 Modelling extracellular electrical stimulation: III. Derivation and interpretation of neural tissue equation J. Neural Eng. 11 065004  
[57] Tahayori B, Meffin H, Sergeev E N, Mareels I M, Burkitt A N and Grayden D B 2014 Modeling extracellular electrical stimulation: IV. Analysis of point source solution in an extensive fibre bundle J. Neural Eng. 11 065005  
[58] Rattay F 1986 High frequency electrostimulation of excitable cells J. Theor. Biol. 123 45- 54

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
