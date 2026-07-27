```
@article{hietanen2013phase,
  title={Phase sensitivity of complex cells in primary visual cortex.},
  author={Markus A. Hietanen and Shaun L. Cloherty and Joshua P. van Kleef and Chun Wang and Bogdan Dreher and Michael R. Ibbotson and Michael R. Ibbotson},
  journal={Neuroscience},
  year={2013},
  volume={237},
  pages={19-28},
  doi={10.1016/j.neuroscience.2013.01.030},
  url={https://www.sciencedirect.com/science/article/pii/S0306452213000675}
}
```

---

# PHASE SENSITIVITY OF COMPLEX CELLS IN PRIMARY VISUAL CORTEX

M.A.HIETANEN,a,b,c\\*
S.L.CLOHERTY,a,b,c 
J.P.VAN KLEEF,d
C.WANG,d,
B.DREHER,d AND 
M.R.IBBOTSON,a,b,c

\(^{a}\) National Vision Research Institute, Australian College of Optometry, Carlton, Vic. 3053, Australia \(^{b}\) Department of Optometry and Vision Sciences, University of Melbourne, Parkville, Vic. 3010, Australia \(^{c}\) ARC Centre of Excellence in Vision Science, Research School of Biology, Australian National University, Canberra, ACT 2601, Australia \(^{d}\) School of Medical Sciences & Bosch Institute, University of Sydney, Sydney, NSW 2606, Australia

Abstract—Neurons in the primary visual cortex are often classified as either simple or complex based on the linearity (or otherwise) of their response to spatial luminance contrast. In practice, classification is typically based on Fourier analysis of a cell's response to an optimal drifting sine-wave grating. Simple cells are generally considered to be linear and produce responses modulated at the fundamental frequency of the stimulus grating. In contrast, complex cells exhibit significant nonlinearities that reduce the response at the fundamental frequency. Cells can therefore be easily and objectively classified based on the relative modulation of their responses – the ratio of the phase-sensitive response at the fundamental frequency of the stimulus \((F_{1})\) to the phase-invariant sustained response \((F_{0})\) . Cells are classified as simple if \(F_{1} / F_{0} > 1\) and complex if \(F_{1} / F_{0} < 1\) . This classification is broadly consistent with criteria based on the spatial organisation of cells' receptive fields and is accordingly presumed to reflect disparate functional roles of simple and complex cells in coding visual information. However, Fourier analysis of spiking responses is sensitive to the number of spikes available – \(F_{1} / F_{0}\) increases as the number of spikes is reduced, even for phase-invariant complex cells. Moreover, many complex cells encountered in the laboratory exhibit some phase sensitivity, evident as modulation of their responses at the fundamental frequency. There currently exists no objective quantitative means of assessing the significance or otherwise of these modulations. Here we derive a statistical basis for objectively assessing whether the modulation of neuronal responses is reliable, thereby adding a level of statistical certainty to measures of phase sensitivity. We apply our statistical analysis to neuronal responses to moving sine-wave gratings recorded from 367 cells in cat primary visual cortex. We find that approximately \(60\%\) of complex cells exhibit statistically significant \((x < 0.01)\) modulation of their responses to optimal moving gratings. These complex cells are phase sensitive and reliably encode spatial phase. © 2013 IBRO. Published by Elsevier Ltd. All rights reserved.

significant \((x < 0.01)\) modulation of their responses to optimal moving gratings. These complex cells are phase sensitive and reliably encode spatial phase. © 2013 IBRO. Published by Elsevier Ltd. All rights reserved.

Key words: simple cells, response modulation, \(F_{1} / F_{0}\) , V1, vision.

## INTRODUCTION

Two classes of cells, simple and complex (Hubel and Wiesel, 1962), have been identified in the primary visual cortices of all mammalian species studied to date (Skottun et al., 1991; Girman et al., 1999; Baker et al., 2001; Ibbotson et al., 2005; Niell and Stryker, 2008). This classification reflects the spatial arrangement of their receptive fields and the linearity of their response to spatial luminance contrast. Simple cells have spatially separate sub- regions within their receptive fields which evoke increased firing rates for light (ON) and dark (OFF) luminance contrast whereas complex cells have spatially overlapping light (ON) and dark (OFF) sub- regions. Simple cells combine responses to local stimuli presented within their receptive field approximately linearly while complex cells combine local responses in a highly nonlinear manner. By virtue of their receptive field organisation, simple cells preserve the sign of local stimulus contrast while complex cells do not (Movshon et al., 1978a; Skottun et al., 1991). Moreover, by virtue of their near linearity, the firing rate response of simple cells driven by moving sine- wave gratings are modulated in synchrony with the stimulus: their responses are phase sensitive (Movshon et al., 1978a,b,c; Skottun et al., 1991). In contrast, the canonical view holds that complex cells are phase invariant. When driven by optimal moving sine- wave gratings, complex cells' overlapping receptive field sub- regions and inherent nonlinearities reduce or even eliminate the response component at the fundamental stimulus frequency. This has lead to widespread use of Fourier analysis as a measure of relative modulation – the ratio of the amplitude of the phase- sensitive response at the fundamental frequency of the stimulus \((F_{1})\) to the amplitude of the phase- invariant sustained response \((F_{0})\) – as an objective means of classifying cortical neurons (Movshon et al., 1978a,b; Skottun et al., 1991). In striate cortices the discrepancy between classification based on relative modulation and that based on quantitative measures of receptive field organisation is estimated to be very small (Area 17/V1: Dean and Tolhurst, 1983; Skottun et al., 1991; Mata and Ringach, 2005; Bardy et al., 2006. Area

18/V2: Romo et al., 2011). Estimates of relative modulation therefore provide a viable means of inferring qualitative receptive field structure and quantifying phase sensitivity.

Here we demonstrate, using a stochastic model of an ideal phase- invariant complex cell, that estimating relative modulation (i.e., \(F_{1} / F_{0}\) ) is sensitive to the number of spikes observed. Many investigators have noted that even when driven by optimal sine- wave gratings, some complex cells exhibit highly modulated responses together with a substantial sustained or mean response component (e.g., Mechler and Ringach, 2002). However, to date there exists no objective, quantitative method of assessing the reliability or otherwise of response modulations often observed in the laboratory. To this end we derive an analytic relationship for the dependence of \(F_{1} / F_{0}\) on spike count and develop a sound statistical basis for assessing the reliability of estimates of \(F_{1} / F_{0}\) in the laboratory. We then analyse spiking responses recorded under typical experimental conditions from 376 neurons in cat primary visual cortex (area 17 and 18). We find that when driven by optimal moving sine- wave gratings, a substantial proportion \((\sim 60\%)\) of complex cells exhibit statistically reliable \((p < 0.01)\) phase- sensitive response components modulated at the fundamental frequency of the stimulus. This has implications for models of visual processing in the primary visual cortex.

## EXPERIMENTAL PROCEDURES

## Modelling an ideal phase-invariant complex cell

Spiking responses of an ideal phase- invariant complex cell to an optimal moving sine- wave grating were modelled by assuming spike arrival times \((t_i)\) to be independent identically distributed random variables uniformly distributed over the response interval. We defined the response interval to be one cycle of the stimulus grating such that \(t_i \in [-\pi , \pi ]\) , \(i = 1 \ldots n\) , where \(n\) is the number of spikes (proportional to the response spike rate). This model makes no attempt to model the spatio- temporal tuning of the cell, stimuli are assumed to be optimal moving sine- wave gratings. Similarly, no attempt is made to model the biophysics of spike generation (refractory period etc.).

Simulated spiking responses \((r(t))\) were expressed as a sum of delta functions,

\[r(t) = \sum_{i = 1}^{n}\delta (t - t_i) \quad (1)\]

We then calculated the relative modulation \((F_{1} / F_{0})\) of the response by taking the ratio of the amplitude of the response component modulated at the fundamental frequency of the stimulus \((F_{1})\) and the amplitude of the sustained response \((F_{0})\) . The amplitudes of the sustained and modulated components of the response \((F_{0}\) and \(F_{1}\) ) were given by the first two terms of the Fourier series expansion of \(r(t)\) (for details, see the Appendix). For each simulated spike count \((n)\) this process was repeated 100,000 times to generate an empirical distribution of \(F_{1} / F_{0}\) . From this distribution we calculate \((F_{1} / F_{0})\) , the expected value of \(F_{1} / F_{0}\) for the given spike count \((n)\) . This simple model reveals the dependence of \((F_{1} / F_{0})\) upon the number of spikes \((n)\) available. We then compare \(F_{1} / F_{0}\) values from experimentally observed responses to the corresponding probability distribution based on the number of spikes collected. Cells whose measured \(F_{1} / F_{0}\) values lay outside the bottom \(99\%\) of their associated probability distribution were considered to have a statistically significant \(F_{1}\) component.

## Anaesthesia and surgical procedures

Extracellular recordings of spiking responses were made from single units in the primary visual cortex (area 17 and 18) in anaesthetized cats \((n = 19; 2 - 5 \text{kg})\) , as described previously [3, 7, 21, 46]. All experiments were performed in accordance with the National Health and Medical Research Council's Australian Code of Practice for the Care and Use of Animals for Scientific Purposes and were approved either by the Animal Experimentation Ethics Committee of the Australian National University (R.V.S.20.05) or the Animal Care Ethics Committee of the University of Sydney (KO3/3- 2008/1/4673 & KO3/3- 2008/3/4673).

In Sydney, animals were initially anaesthetised by inhalation of \(2 - 4\%\) isoflurane (Abbott Australasia Pty Ltd, Kurnell, NSW, Australia) in a \(2:1\) mixture of \(\mathrm{N}_2\mathrm{O}\) and \(\mathrm{O}_2\) . In Canberra, animals were initially anaesthetised by intramuscular injection of ketamine hydrochloride (20 mg/kg; i.m.) and xylazine (1 mg/kg). A suitable depth of anaesthesia was determined by absence of the toe pinch reflex. Animals were then intubated to ensure accurate respiration and the right cephalic vein was cannulated. Animals were then placed in a stereotaxic frame and anaesthesia was maintained for the duration of the experiment by inhalation of gaseous isoflurane (0.75- 1.5% during surgery, 0.5% during unit recordings; Sydney) or halothane (1- 2% during surgery, 0.5% during unit recordings; Canberra) in a 2:1 mixture of \(\mathrm{N}_2\mathrm{O}\) and \(\mathrm{O}_2\) . Animals were instrumented to facilitate continuous monitoring of the electrocardiogram (ECG), the electroencephalogram (EEG) and end- tidal \(\mathrm{CO}_2\) concentration to ensure an adequate level of anaesthesia was maintained at all times. Changes in the physiological indicators (ECG, EEG or expired \(\mathrm{CO}_2\) ) that may have suggested the level of anaesthesia was not sufficient were mitigated by immediately increasing the concentration of inhaled isoflurane or halothane. For fluid replacement, animals received a continuous intravenous infusion (2.5 ml/kg/h) containing Hartmann's (lactated Ringer) solution (25% by volume), 5% glucose- 0.9% NaCl solution (25% by volume) and an amino acid solution (50% by volume). Body temperature was maintained at 37.7 °C by way of an electric heating blanket under feedback control.

To allow access to the primary visual cortex (area 17 and 18), the scalp was reflected and a craniotomy was performed 0- 8 mm posterior to internal zero and 2- 8 mm lateral to the midline. To minimise eye movements during single unit recordings animals were subject to neuromuscular blockade by intravenous injection of 50 mg of gallamine triethiodide (Flaxeldil; Sigma, St. Louis, MO) in 2 ml of Hartmann's solution. Blockade was then maintained by continuous intravenous infusion of Flaxeldil at a rate of 10 mg/kg/h. Animals were mechanically ventilated to maintain end- tidal \(\mathrm{CO}_2\) between 3.5% and 4%.

The pupils were dilated and the nictitating membranes retracted by topical application of ophthalmic atropine sulphate \((1\%)\) and phenylephrine hydrochloride \((2.5\%)\) . Neutral power rigid gas- permeable contact lenses were fitted to the eyes to ensure corneal perfusion and corrective lenses were placed in front of the eyes to focus the stimulus on the retina. Spherical and chromatic aberrations were minimised by interposing 3- mm diameter artificial pupils between the eyes and the corrective lenses. Animals received daily injections to reduce salivation (atropine, \(0.2 \text{mg / kg}\) ; s.c.), cerebral oedema (dexamethasone phosphate, \(1.5 \text{mg / kg}\) ; i.m.) and the risk of infection (Clavulox, a broad spectrum antibiotic, \(0.5 \text{ml / kg}\) ; i.m.).

At the conclusion of the experiment animals were killed by intravenous injection of an overdose of barbiturate (sodium pentobarbitone, \(150 \text{mg / kg}\) ) and immediately transcardially perfused with \(0.9\%\) saline followed by \(10\%\) formal saline. The brain was then extracted for histological reconstruction of recording track locations (for details see Crowder et al., 2006).

## Extracellular recordings and visual stimuli

Extracellular signals from single units were acquired using either gold- tipped, lacquer- coated tungsten (Canberra) or stainless steel (Sydney) microelectrodes (FHC, Bowdoin, ME USA). The extracellular potential was then amplified and bandpass filtered \((300\mathrm{Hz} - 5\mathrm{kHz})\) . In Canberra, this signal was then sampled at \(40\mathrm{kHz}\) using a CED1401 interface and Spike2 software (Cambridge Electronic Designs, Cambridge, UK). In Sydney, the signal was sampled using Expo (P. Lennie, University of Rochester, Rochester, NY), which also controlled presentation of the visual stimuli. After isolating a neuron (based on the shape and consistency of the extracellular spike waveform) its dominant eye and receptive field location were qualitatively determined using hand- driven bright or dark bars projected onto a tangent screen. The non- dominant eye was then covered and all quantitative testing was performed using the dominant eye only. In Sydney, visual stimuli were generated by Expo and presented on a calibrated CRT monitor (Barco, Kortrijk, Belgium) placed \(57\mathrm{cm}\) in front of the animal. In Canberra, visual stimuli were produced by a VGS 215 series or a ViSAGE visual stimulus generator (Cambridge Research Systems, Cambridge, UK), and presented on a calibrated CRT monitor (Eizo T662- T, \(100\mathrm{Hz}\) refresh, \(1024\mathrm{by}768\) pixels) at a viewing distance of \(57\mathrm{cm}\) . Moving sine- wave gratings were presented in a circular aperture surrounded by a grey background of mean luminance \((50\mathrm{cd} / \mathrm{m}^2\) ,Sydney; \(57\mathrm{cd} / \mathrm{m}^2\) Canberra). Each neuron's preferred direction, spatial frequency, temporal frequency, and receptive field size and location was determined using on- line tuning functions derived from the neuron's response to drifting sine- wave gratings of \(100\%\) Michelson contrast. The receptive fields of all neurons analysed here were located within \(10^{\circ}\) of the area centralis.

## Data analysis

For each neuron we calculated the relative modulation \((F_{1} / F_{0})\) of its response to a \(100\%\) contrast moving sine- wave grating of optimal direction, spatial and temporal frequency presented within a circular aperture of optimal size centred on its receptive field. Stimuli were presented 8- 10 times interleaved by periods of mean luminance. Spiking responses were represented as spike density functions (SDFs) with 1- kHz resolution generated by convolution of a Gaussian kernel of unit area and \(\sigma = 8\mathrm{ms}\) with a train of Dirac delta functions; one delta function corresponding to the arrival time of each spike. Mean SDFs were then calculated by trial averaging responses to individual stimulus presentations. The spontaneous firing rate of each neuron was estimated by averaging spike rate over periods of \(500\mathrm{ms}\) immediately prior to each stimulus presentation during which the stimulus monitor displayed a mean grey screen. Fourier analysis was performed on a section of the mean response (averaged across trials) whose duration was an integer multiple of the stimulus period. The sustained or mean response component \((F_{0})\) was calculated as the increase in the mean firing rate above the spontaneous baseline. The modulated response component \((F_{1})\) , defined as the Fourier coefficient corresponding to the fundamental frequency of the stimulus grating, was calculated using the fast Fourier transform (FFT) function in Matlab (The Mathworks Inc. Natick, MA, USA).

## RESULTS

## The influence of spike count on a model complex cell  

The most common method used for rapidly classifying a cortical neuron as either simple or complex is based on Fourier analysis of the neuron's response to drifting sine- wave gratings (Movshon et al., 1978a,b,c). Cells are classified based on the ratio of the first Fourier component \((F_{1})\) of the response to the mean response \((F_{0})\) , i.e., \(F_{1} / F_{0}\) . If the ratio is below one, the cell is classified as simple, otherwise the cell is classified as complex (De Valois et al., 1982; Skottun et al., 1991). This method is easy, intuitive and, where sufficient data are available, yields reliable classification of neurons. However, Fourier analysis becomes problematic when fewer spikes are available, either due to low spike rates observed in some neurons even for optimal stimuli, or in experiments that specifically employ stimulus manipulations that alter the spike rate (e.g., Bardy et al., 2006; Crowder et al., 2007; van Kleef et al., 2010). To demonstrate the importance of taking into account the number of spikes when performing Fourier analysis we simulated spiking responses of an ideal phase- invariant complex cell (see Experimental procedures). The model produces a specified number of spikes \((n)\) at random times during one cycle \((T)\) of a sine- wave grating stimulus, i.e., its response is insensitive to the phase of the stimulus. Fig. 1A shows an example response produced by this model for \(n = 25\) . Vertical lines indicate spike arrival times over the response interval \((0\ldots T)\) . This response yields \(F_{1} / F_{0} = 0.3\) . The solid grey line shows the sum of the first two terms of the Fourier series expansion \((F_{0}\) and \(F_{1}\) ) of the response. Fig. 1B shows the distribution of \(F_{1} / F_{0}\) derived from many simulated responses produced by the model for \(n = 25\) . The mean of this distribution is \(\langle F_{1} / F_{0}\rangle = 0.35\) . Given that the mechanism generating the spikes is phase invariant, the apparent modulation of some responses is due entirely to the finite number of spikes available. The problem is compounded as the number of spikes \((n)\) decreases. Fig. 1C shows an example response produced by the model for \(n = 4\) . Fourier analysis of this response produces \(F_{1} / F_{0} = 0.9\) . Fig. 1D shows the distribution of \(F_{1} / F_{0}\) derived from many simulated responses produced by the model for \(n = 4\) . The mean of this distribution is \(\langle F_{1} / F_{0}\rangle = 0.89\) .

Fig. 1E shows \(\langle F_{1} / F_{0}\rangle\) , the expected value of \(F_{1} / F_{0}\) , as a function of spike count \((n)\) for the ideal complex cell model (dashed curve). In the Appendix we show that for our ideal complex cell model \(F_{1}\) is Rayleigh distributed and derive an analytic expression for this relationship. There we show that,

\[\langle F_{1} / F_{0}\rangle = \frac{2}{\sqrt{n}} \quad (2)\]

This relationship demonstrates that even with no underlying phase sensitivity (i.e., spikes are equally likely to arrive at any point in the stimulus cycle), \(\langle F_{1} / F_{0}\rangle\) increases with decreasing total spike count. It is important to note that the crucial parameter is the total number of spikes \((n)\) , not the spike rate. Even modest spike counts can lead to over estimation of \(F_{1} / F_{0}\) , even for an ideal complex cell whose response is insensitive to the phase of the stimulus.

Our model complex cell is simplistic in that each spike is independent and identically distributed with uniform probability over the response interval: we make no attempt to explicitly model the temporal dynamics of neuronal responses. Nevertheless, the model is informative in demonstrating the importance of the

> **Image description.** This is a multi-panel scientific figure (Figure 1) titled "Modelling the affect of spike count on response modulation in an ideal complex cell," which illustrates how the number of spikes influences the statistical distribution of the $F_1/F_0$ ratio. The figure is composed of five distinct panels (A, B, C, D, and E).
>
> **Panels A and C (Spike Train Visualizations):**
> *   **Panel A:** Displays a simulated spike train containing 25 spikes. The spikes are represented by thin vertical black lines plotted against a horizontal axis labeled "Time." Overlaid on these spikes is a grey sinusoid, which the caption identifies as the sum of the first two terms ($F_0 + F_1$) of the corresponding Fourier series.
> *   **Panel C:** Displays a simulated spike train containing only four spikes. Similar to Panel A, the spikes are represented by thin vertical black lines plotted against "Time."
>
> **Panels B and D (Distribution Histograms):**
> *   **Panel B:** Shows a probability distribution (histogram) of the $F_1/F_0$ ratio generated by simulating many spike trains with 25 spikes. The distribution is a black, bell-shaped curve, and a small black arrow points to its mean, which is approximately 0.35.
> *   **Panel D:** Shows a probability distribution of the $F_1/F_0$ ratio generated by simulating spike trains containing only four spikes. This distribution is also a black, bell-shaped curve, and a small black arrow points to its mean.
>
> **Panel E (Model Graph):**
> *   **Type:** This is a line graph illustrating the relationship between spike count and the expected value of $F_1/F_0$.
> *   **Axes:** The horizontal x-axis is labeled "Spike Count" and uses a logarithmic scale, ranging from 1 to 100. The vertical y-axis is labeled $F_1/F_0$ and ranges from 0 to 2.
> *   **Data Curves:**
>     *   A dashed black curve represents $\langle F_1/F_0 \rangle$, the expected value of the ratio. This curve shows a clear upward trend, indicating that the expected value increases as the spike count decreases.
>     *   A solid black curve represents the $99\%$ confidence limit for $F_1/F_0$ as a function of spike count.
> *   **Shaded Regions:** Alternating white and grey bands surround the dashed curve. These bands represent regions of equal probability, with each band containing $10\%$ of the distribution of $F_1/F_0$ at any given spike count.
> *   **Markers:** Thin vertical lines are placed on the graph to indicate the specific spike counts used in the example distributions shown in Panels B (25 spikes) and D (4 spikes).

<center>Fig. 1. Modelling the affect of spike count on response modulation in an ideal complex cell. (A) A simulated spike train containing 25 spikes randomly distributed within a single stimulus cycle. The grey sinusoid shows the sum of the first two terms \((F_{0} + F_{1})\) of the corresponding Fourier series. This spike train yields an estimated \(F_{1} / F_{0}\) of 0.3. (B) The distribution of \(F_{1} / F_{0}\) generated by repeatedly simulating many such spike trains containing 25 spikes and calculating their corresponding \(F_{1} / F_{0}\) ratio. The mean of this distribution is 0.35 (arrow). (C) A simulated spike train containing only four randomly distributed spikes. (D) the distribution of \(F_{1} / F_{0}\) produced by the model when simulating spike trains containing only four spikes. (E) The dashed curve shows \(\langle F_{1} / F_{0}\rangle\) the expected value of \(F_{1} / F_{0}\) as a function of spike count; \(\langle F_{1} / F_{0}\rangle\) increases as spike count decreases. Bands of equal probability are shown alternately shaded in white and grey; each band contains \(10\%\) of the distribution of \(F_{1} / F_{0}\) at each spike count. The solid curve indicates the \(99\%\) confidence limit for \(F_{1} / F_{0}\) as a function of spike count. The thin vertical lines show the location of the example distributions shown in B and D. </center>  

number of spikes collected when using Fourier analysis. Moreover, the model provides a useful basis against which we can objectively assess the statistical reliability of modulated responses observed in real cortical neurons. Using the model we can estimate, for a given number of spikes, the probability of observing a given level of modulation (i.e., \(F_{1} / F_{0} = x\) ) under the null hypothesis that the underlying mechanism is phase invariant. This may be achieved by simulating the response of the model complex cell many times to generate an empirical distribution of \(F_{1} / F_{0}\) for the requisite number of spikes (e.g., Fig. 1B and D) and then estimating the desired probability \(P(F_{1} / F_{0} \geq x; n)\) as the proportion of simulated responses that produce an \(F_{1} / F_{0} \geq x\) . Alternatively, it is also possible to calculate, for a given significance level \(\alpha\) , the range of \(F_{1} / F_{0}\) that are unlikely to have been produced by a phase- invariant mechanism. In the Appendix we derive an analytic expression for this range for large \(n\) . Specifically, we show that the desired range is

\[\frac{F_1}{F_0} \geq \frac{k}{\sqrt{n}} \quad (3)\]

where \(k\) is given by,

\[k = 2\sqrt{-\ln(x)}.\]

This expression follows from the observation that for our ideal complex cell model, \(F_{1}\) is Rayleigh distributed (see Appendix). In Fig. 1E, bands of equal probability, \(P(a < F_{1} / F_{0} \leq b; n) = 0.1\) , are shown alternately shaded in white and grey. In the following section we employ the relationship given by Eq. (3) to objectively assess the statistical reliability of modulated responses observed in real cortical neurons.

## The influence of spike count on the measured phase sensitivity of neurons in areas 17/18

To assess the extent to which spike counts influence Fourier analysis of neuronal responses encountered under typical experimental conditions, we analysed extracellular recordings of spiking responses from 376 cells in cat primary visual cortex (areas 17 and 18). Cell populations from areas 17 and 18 were combined and analysed as a single population because there was no significant difference in the distribution of \(F_{1} / F_{0}\) (Kruskal- Wallis, \(p > 0.83\) ) or the number of spikes (Kruskal- Wallis, \(p > 0.36\) ) between areas 17 and 18.

Fig. 2A shows the relationship between estimated \(F_{1} / F_{0}\) and the number of observed spikes for each cell in our population (grey points). Black symbols and error bars show the mean and standard error of the relationship. For comparison, the dashed curve shows \(\langle F_{1} / F_{0}\rangle\) as a function of spike count \((n)\) for the ideal phase- invariant complex cell model described above (see Fig. 1). It is readily apparent that on average, cells for which fewer spikes were observed yield higher estimated \(F_{1} / F_{0}\) . However, across the range of spike counts, the mean relationship exceeds that predicted by the ideal complex cell model (dashed curve), suggesting that the null hypothesis of the model - a phase- invariant mechanism - is not common among cortical neurons. To quantify the prevalence of phase- sensitive neurons in our population we calculated an \(\alpha\) for each cell, taking into account the number of spikes observed (see Eq. (3)). The distribution of \(1 - \alpha\) for our cell population is shown in Fig. 2B. If \(F_{1} / F_{0}\) for each cell in our population fit the prediction of the model given by Eq. (3) (i.e., Rayleigh distributed \(F_{1}\) ), \(1 - \alpha\) should be uniformly distributed between 0 and 1. This is clearly not

the case with a large subset of cells showing very large \(1 - \alpha\) values.

The Inset to Fig. 2B is a histogram of \(1 - \alpha\) in the range 0.9- 1.0, revealing that deviation from a uniform distribution begins at very high values \((1 - \alpha \approx 0.99)\) . We therefore define the \(99\%\) confidence limit (i.e., \(k = 2\sqrt{-\ln(0.01)} = 4.29\) ) as a reasonable criterion for identifying significant relative modulation of neuronal responses. Cells exhibiting significant modulation of their responses are those for which \(F_{1} / F_{0} > 4.29 / \sqrt{n}\) , where \(n\) is the total number of spikes observed. This criterion is indicated by the solid curve in both Fig. 1E and in Fig. 2A. It is important to note that this criterion is dependent only on the total number of spikes collected and is independent of the number of cycles of the stimulus grating or the number of repeats of the

> **Image description.** This image is a scientific figure, labeled Figure 2, consisting of two panels, (A) and (B), which illustrate the effect of spike count on response modulation in cortical neurons.
>
> **Panel (A): Relationship between Response Ratio and Spike Count**
> Panel (A) is a scatter plot showing the relationship between the response ratio ($F_1 / F_0$) and the Spike Count.
> *   **Axes:** The vertical y-axis represents the response ratio ($F_1 / F_0$), ranging from 0 to 2. The horizontal x-axis represents the Spike Count, displayed on a logarithmic scale, ranging from 10 to 1000.
> *   **Data Points:** Numerous grey circles represent the estimated $F_1 / F_0$ for individual cortical neurons, with a total sample size of $n=374$. Black symbols with vertical error bars indicate the mean and standard error of the relationship at various spike counts.
> *   **Lines and Bands:** Two key lines are plotted: a dashed line, which represents the expected value of $F_1 / F_0$ for an ideal phase-invariant complex cell, and a solid line, which indicates the $99\%$ confidence limit for $F_1 / F_0$. Both lines show a downward trend as the Spike Count increases. Alternating white and grey bands are shown, representing bands of equal probability, where each band contains $10\%$ of the distribution of $F_1 / F_0$ at each spike count.
>
> **Panel (B): Distribution of Response Modulation**
> Panel (B) is a bar chart (histogram) illustrating the distribution of the modulation measure $1 - \alpha$ across the population of 374 cells.
> *   **Axes:** The vertical y-axis represents the percentage of cells (% of cells), ranging from 0 to 80. The horizontal x-axis represents the value of $1 - \alpha$, ranging from 0 to 1.
> *   **Data:** The bars show that the majority of cells have low values of $1 - \alpha$.
> *   **Inset:** A smaller inset histogram is included within Panel (B), specifically detailing the distribution of $1 - \alpha$ in the high-modulation range of 0.9 to 1.0, revealing a significant population of cells exhibiting high values of $1 - \alpha$.
>
> The overall figure uses technical notation ($F_1 / F_0$, $1 - \alpha$) to quantify neuronal response characteristics and demonstrates how the reliability of these measurements changes as the number of observed spikes increases.

<center>Fig. 2. The effect of spike count on response modulation in cortical neurons. (A) Relationship between observed and spike count for 374 neurons recorded in area 17 and 18 of cat visual cortex. Each grey symbol indicates estimated \(F_{1} / F_{0}\) for a single cortical neuron plotted against the number of spikes upon which the estimate is based. Black symbols and error bars show the mean and standard error of the relationship. The dashed line shows \(F_{1} / F_{0}\) the expected value of \(F_{1} / F_{0}\) as a function of spike count for an ideal phase-invariant complex cell. The solid line indicates the \(99\%\) confidence limit for \(F_{1} / F_{0}\) as a function of spike count (see Fig. 1). Cells plotted above this line exhibit modulated responses unlikely to have been produced by a phase-invariant mechanism. Bands of equal probability are shown alternately shaded in white and grey: each band contains \(10\%\) of the distribution of \(F_{1} / F_{0}\) at each spike count. (B) A histogram showing the distribution of \(1 - \alpha\) for the population of 374 cells. If all cells were phase invariant this distribution would be uniform with each bin containing \(5\%\) of the cells. The inset shows the distribution for \(1 - \alpha > 0.9\) . More than \(70\%\) of cells have \(F_{1} / F_{0}\) above their corresponding \(99\%\) confidence limit (indicated by the vertical line) and hence fall on the extreme right of this distribution. </center>

stimulus presented to a given cell. For example, 100 spikes collected over 10 cycles of the stimulus provides exactly the same \(\langle F_{1} / F_{0}\rangle\) , and hence the same criterion, as 100 spikes collected over five cycles. For points plotted above the \(99\%\) confidence limit (solid curve) in Fig. 2A, there is less than \(1\%\) chance that the observed response modulation is due to a phase- invariant mechanism.

The critical values of the Rayleigh distribution depend on \(n\) (Wilkie, 1983). However, our criterion for significance (i.e., \(F_{1} / F_{0} > 4.29 / \sqrt{n}\) ) is more conservative at low \(n\) than that suggested by Wilkie (1983). Therefore, for cells exceeding our criterion, it is statistically very likely that the observed modulation of their responses is due to an underlying phase- sensitive mechanism and not due to chance. Cells for which the observed \(F_{1} / F_{0}\) is below the \(99\%\) confidence limit have a higher chance that the observed modulation of their responses is due simply to chance and could well arise from an underlying phase- invariant mechanism. In our population of 376 cells, two cells had too few spikes to analyse reliably. Of the remaining 374 cells, 105 cells were simple cells \((F_{1} / F_{0} > 1)\) and 269 were complex \((F_{1} / F_{0} < 1)\) . However in total, 266 cells \((71\%)\) had \(F_{1} / F_{0}\) above the corresponding \(99\%\) confidence limit. This includes all 105 simple cells, but notably, also includes 161 complex cells. Therefore, \(60\%\) (161/269) of complex cells exhibit reliable modulation of their spiking responses suggesting some level of phase sensitivity in the underlying neuronal mechanism. The remaining complex cells (108/269; \(40\%\) ) exhibit responses consistent with an ideal phase- invariant mechanism.

## Diversity of responses to optimal moving sine-wave gratings

The scatter of points in Fig. 2A reflects the diversity of responses to optimal moving sine- wave gratings encountered under typical experimental conditions. To illustrate this diversity, Fig. 3 shows spike density functions of representative neurons from different regions of our cell population. Specifically, we chose four nominal values of \(F_{1} / F_{0}\) : 0.15, 0.4, 0.85 and 1.4. For each value of \(F_{1} / F_{0}\) we then chose three cells over the range of observed spike counts, nominally: low spike counts \((< 100\) spikes), moderate spike counts \((100 - 500\) spikes) and high spike counts \((>500\) spikes). These 12 cells are indicated in the context of the entire population in Fig. 3A and in Fig. 3B are labelled D- O. These labels correspond to panels D- O in Fig. 3, which show the mean response observed from the corresponding cell. Fig. 3C shows the relationship between spike count and the estimated level of response modulation for each of the representative cells (this analysis is described in the next section). All three simple cells \((F_{1} / F_{0} \cong 1.4\) ; Fig. 3D- F) exhibit clear modulated responses with very few spikes during the null phases. The three cells with \(F_{1} / F_{0} \cong 0.85\) (Fig. 3G- I) also exhibit clearly modulated responses. Indeed, the response shown in Fig. 3I is very similar to that of the simple cell shown above it in Fig. 3F. The difference is that the sustained response of the cell in Fig. 3I is moderately larger such that the response

during the null phases is non- zero. Responses of the cells with \(F_{1} / F_{0} \cong 0.4\) (Fig. 3J- L) are distinctly complex in nature but again some modulation of the responses is apparent, especially in Fig. 3L. Note that the cells illustrated in Fig. 3K and L lie well above the \(99\%\) confidence limit (Fig. 3A). Finally, all of the cells with \(F_{1} / F_{0} \cong 0.15\) (Fig. 3M- O) exhibit characteristic complex cell responses with no obvious modulated component.

## The influence of spike count on estimated \(F_{1} / F_{0}\)

Using our model of an ideal phase- invariant complex cell we demonstrated that we might reasonably expect \(F_{1} / F_{0}\) to increase as the number of spikes observed is reduced. We also derived a statistical criterion for objectively assessing response modulation that accounted for the number of spikes observed. However, it remains unclear how estimates of \(F_{1} / F_{0}\) vary with spike count under typical experimental conditions. Using a subset of our cell population we investigated the effect of recording fewer spikes on our estimate of a given cell's \(F_{1} / F_{0}\) . Due to limitations in the way that data from individual trials were stored for some cells, we were only able to utilise 220 cells from our total cell population. For each cell we first took the set of all available responses \(r_{j}, j = 1 \ldots N\) observed and calculated the total number of spikes \((n)\) and the relative modulation of the mean response \((F_{1} / F_{0})\) , as described above. This is the best estimate of \(F_{1} / F_{0}\) given the data available for each cell (these data are shown for all cells in our population in Fig. 2A). For each cell we then systematically reduced the number of stimulus repeats, and hence the number of spikes, available for analysis by drawing random samples of \(M\) responses \(r_{j}, j = 1 \ldots M (M \leq N)\) , with replacement, from \(r_{j}\) and recalculating the total number of spikes \((n^{*})\) and the relative modulation of the mean response \((F_{1} / F_{0})\) for each sample. This sampling procedure was repeated 1000 times for each value of \(M \leq N\) , thereby generating a distribution of \(n^{*}\) (the number of spikes) and \(F_{1} / F_{0}\) from which we calculated the means \(< n^{*} > _{M}\) and \((F_{1} / F_{0})_{M}\) . Fig. 3C plots these metrics for the 12 representative cells indicated in Fig. 3A. Cells for which the best estimate of \(F_{1} / F_{0}\) falls below the \(99\%\) confidence limit show characteristic increases in estimated \(F_{1} / F_{0}\) as the number of spikes available is reduced. These curves are consistent with the expectation of a Rayleigh distributed \(F_{1}\) and are therefore consistent with the assumption of an ideal phase- invariant mechanism. In contrast, cells for which the best estimate of \(F_{1} / F_{0}\) lies above the \(99\%\) confidence limit show very little change in estimated \(F_{1} / F_{0}\) as the number of spikes available is reduced. These curves (including those for the three representative simple cells) are not consistent with the assumption of an ideal phase- invariant mechanism. Fig. 4 plots estimated \(F_{1} / F_{0}\) for 220 cells from our population as the number of spikes available for analysis is reduced. Fig. 4A shows trajectories for phase- sensitive cells, both simple and complex while trajectories for phase- invariant cells are shown in Fig. 4B. The trends evident in the representative cells shown in Fig. 3C are also apparent in the larger cell population. Fig. 4C and D show histograms of \(F_{1} / F_{0}\) for various spike counts for

representative phase- sensitive and phase- invariant complex cells respectively. In each case the vertical black line indicates the mean of the distribution for each spike count. It is readily apparent that for the phase- sensitive cell (Fig. 4C) the mean \(F_{1} / F_{0}\) remains relatively constant as the spike count is reduced. In contrast, the mean \(F_{1} / F_{0}\) for the phase- invariant cell (Fig. 4D) increases as spike count is reduced.

Above, we observed that approximately \(60\%\) of complex cells in our population exhibited significant modulation of their responses to moving sine- wave gratings. This observation was based on the best estimate of the cells \(F_{1} / F_{0}\) derived from all available spikes. Comparing the trajectory for each cell in Fig. 4 with the trajectory expected for our ideal complex cell model (i.e., for which \(F_{1}\) is Rayleigh distributed) provides an additional assay for examining the extent to which cortical neuron responses deviate from those expected from a phase- invariant mechanism. To assess the agreement between the trajectories observed in our cell population with those predicted by our ideal complex cell model (i.e., Eq. (3)), we calculated the sum of the squared 2- norm of the residuals between the set of \(\langle F_{1} / F_{0} \rangle\) derived from the resampling procedure described above and those given by Eq. (3), for the corresponding set of \(\langle n^{*} \rangle\) , assuming constant \(\alpha\) for each cell. There was a highly significant difference between the sum- of- squared residuals for cells below \((x = 0.0805)\) and those above \((x = 1.4045)\) the \(99\%\) confidence limit of the Rayleigh distribution \((t = 8.014, p < 0.0001)\) . Cells with reliable phase sensitivity (i.e., \(1 - \alpha > 0.99\) ) exhibit the largest sum- of- squared residuals, indicating that the responses of these cells are poorly fit by the model. The sum- of- squared residuals for cells without reliable phase sensitivity were close to zero indicating that they were well fit by the Rayleigh model.

In summary, cells that lie above the \(99\%\) confidence limit exhibit relative modulation of their responses that is largely independent of the total number of spikes observed (i.e., the relationship between \(F_{1} / F_{0}\) and spike count is flat). In contrast, complex cells that fall within the \(99\%\) confidence limit exhibit relationships between \(F_{1} / F_{0}\) and spike count that are well fit by a model in which \(F_{1}\) is Rayleigh distributed. These cells are consistent with an ideal phase- invariant mechanism.

## DISCUSSION

Fourier analysis of neural spiking activity recorded in response to optimal moving sine- wave gratings is a widely employed measure of phase sensitivity of neurons in visual cortex. However, Fourier analysis of spiking responses is sensitive to the number of spikes recorded. We show that even for an ideal phase- invariant neural mechanism, conventional estimates of relative modulation \((F_{1} / F_{0})\) overestimate the level of underlying phase sensitivity when considering spike counts comparable to those obtained under typical experimental conditions (Fig. 1). Moreover, we show that among a representative sample of extracellular recordings from neurons in cat primary visual cortex, relative modulation is higher, on average, for neurons from which fewer spikes are

> **Image description.** This image is a complex scientific figure, Figure 3, titled "Diversity of response modulations in cortical neurons," which presents data through multiple panels (A, B, C, and D through O) to illustrate the relationship between neural response modulation ($F_1/F_0$) and spike count.
>
> The figure is divided into two main sections: three summary scatter plots at the top (A, B, C) and a grid of twelve time-series response plots below (D through O).
>
> **Summary Plots (A, B, C):**
> These three panels are scatter plots showing the relationship between $F_1/F_0$ (on the Y-axis) and Spike Count (on the X-axis).
> *   **Axes:** The Y-axis for all three plots is labeled "$F_1/F_0$" and ranges from 0 to 2. The X-axis is labeled "Spike Count" and uses a logarithmic scale, ranging from 1 to over 1000.
> *   **Data:** Various symbols (circles, triangles, diamonds, etc.) represent individual example cells.
> *   **Panel C:** This panel includes a dashed line representing a $99\%$ confidence limit, used to categorize the cells based on their modulation.
>
> **Response Examples Grid (D through O):**
> Below the summary plots is a grid of twelve panels (4 rows by 3 columns), each illustrating the spiking response of one of the example cells.
> *   **Structure:** Each panel (labeled D through O) displays a time-series plot.
> *   **Axes:** The X-axis is labeled "Time (ms)" and ranges from 0 to 2000 ms. The Y-axis is labeled "Response (spk/s)" and ranges from 0 to 500.
> *   **Data Representation:** The neural response is shown as a series of black vertical bars, where the height of each bar represents the spike count during a specific time interval.
> *   **Stimulus Overlay:** Above each response plot, a thin, continuous sinusoidal wave is drawn, representing the temporal frequency and phase of the stimulus applied to the cell.
> *   **Labels:** Each panel is labeled with the cell identifier (e.g., D, E, F) and its corresponding $F_1/F_0$ value (e.g., D: $F_1/F_0 = 1.32$).
>
> **Arrangement and Grouping:**
> The cells are organized in the grid based on their characteristics:
> *   **Rows:** Cells are grouped by row, showing different levels of response modulation ($F_1/F_0$).
> *   **Columns:** Cells are grouped by column, showing low, moderate, and high spike counts.
>
> **Visible Text and Labels:**
> *   **Figure Title:** "Fig. 3. Diversity of response modulations in cortical neurons."
> *   **Panel Labels:** A, B, C, D, E, F, G, H, I, J, K, L, M, N, O.
> *   **Axis Labels:** "Spike Count," "$F_1/F_0$," "Time (ms)," "Response (spk/s)."
> *   **Specific Data Labels (Examples):**
>     *   D: $F_1/F_0 = 1.32$
>     *   E: $F_1/F_0 = 1.32$
>     *   F: $F_1/F_0 = 1.53$
>     *   G: $F_1/F_0 = 0.82$
>     *   H: $F_1/F_0 = 1.32$
>     *   I: $F_1/F_0 = 0.97$
>     *   J: $F_1/F_0 = 0.36$
>     *   K: $F_1/F_0 = 0.45$
>     *   L: $F_1/F_0 = 0.16$
>     *   M: $F_1/F_0 = 0.13$
>     *   N: $F_1/F_0 = 0.16$
>     *   O: $F_1/F_0 = 0.15$

<center>Fig. 3. Diversity of response modulations in cortical neurons. (A) The same as Fig. 2A, highlighting twelve example cells (symbols) based on their estimated \(F_{1} / F_{0}\) and their corresponding spike count. (B) The example cells from A indicating the corresponding panel (D-O) in which example responses are illustrated. (D-O) Spiking responses from the 12 example cells indicated in A and B. Cells are grouped by row, showing different levels of response modulation \((F_{1} / F_{0})\) and column, showing low, moderate and high spike counts. A sinusoid representing the temporal frequency and phase of the stimulus is presented above each response. (C) The relationship between \(F_{1} / F_{0}\) and spike count for each of the example cells. The effect of reduced spike count was examined by artificially reducing the number of spikes available using a resampling technique (see text). Cells D-I, K and L, which lie above their corresponding \(99\%\) confidence limit show relatively little change in \(F_{1} / F_{0}\) as the number of spikes is reduced. Cells J and M-O, which lie below their corresponding \(99\%\) confidence limit tend to follow the trend predicted by an ideal phase-invariant mechanism, showing increases in \(F_{1} / F_{0}\) with reduced spike count. </center>

recorded (Fig. 2). These observations are important: while \(F_{1} / F_{0}\) provides an intuitive and quantitative measure of phase sensitivity, there currently exists no objective

quantitative means of assessing the significance or otherwise of any observed modulation. Based on a model of an ideal phase- invariant mechanism, we derived a

> **Image description.** This image is a multi-panel scientific figure (Figure 4) consisting of four distinct graphs arranged in a 2x2 grid, illustrating the relationship between the estimated ratio $F_1/F_0$ and the number of spikes recorded for cortical neurons.
>
> The figure is divided into two rows: the top row contains line graphs (Panels A and B), and the bottom row contains histograms (Panels C and D).
>
> **Top Row: Line Graphs (Panels A and B)**
>
> *   **Panel A (Top Left):** Titled "A phase sensitive," this graph plots $F_1/F_0$ on the vertical y-axis (ranging from 0 to 2) against "Spike Count" on the horizontal x-axis, which uses a logarithmic scale (ranging from 10 to 1000). The panel displays numerous solid black lines, each representing a different cell, showing how $F_1/F_0$ changes as the spike count decreases. A solid grey curve, representing the 99% confidence limit, is visible. The data points generally remain above this confidence limit, indicating relatively little change in $F_1/F_0$ as the spike count is reduced.
> *   **Panel B (Top Right):** Titled "B phase invariant," this graph shares the same axes as Panel A ($F_1/F_0$ vs. Spike Count on a log scale). It also shows multiple solid black lines. In contrast to Panel A, these lines trend sharply downward. A dashed grey curve, representing the trend predicted by an ideal phase-invariant mechanism, is visible, and the data points generally follow this downward trajectory, showing that $F_1/F_0$ increases as the spike count is reduced.
>
> **Bottom Row: Histograms (Panels C and D)**
>
> *   **Panel C (Bottom Left):** This panel displays histograms of $F_1/F_0$ for an example of a phase-sensitive complex cell. The x-axis represents the $F_1/F_0$ ratio (binned at 0, 0.5, and 1), and the y-axis represents frequency. Four separate distributions are shown, corresponding to different spike counts (34, 68, 101, and 135). Vertical black lines mark the mean of each distribution. Visually, the mean remains relatively constant across the different spike counts.
> *   **Panel D (Bottom Right):** This panel displays histograms of $F_1/F_0$ for an example of a phase-invariant complex cell. It uses the same x-axis ($F_1/F_0$ binned at 0, 0.5, and 1) and y-axis (frequency). Four distributions are shown for spike counts (32, 67, 103, and 133). In this panel, the distributions clearly shift toward higher $F_1/F_0$ values (to the right) as the spike count increases.
>
> The overall figure is accompanied by a caption at the top, which reads: "Fig. 4. Change in estimated $F_1/F_0$ with spike count for 220 cortical neurons. (A) The relationship between $F_1/F_0$ and spike count for cells which lie above their corresponding 99% confidence limit (solid grey curve). These cells show relatively little change in $F_1/F_0$ as the number of spikes is reduced. (B) The relationship between $F_1/F_0$ and spike count for cells which lie below their corresponding 99% confidence limit tend to follow the trend predicted by an ideal phase-invariant mechanism (dashed grey curve). For these cells $F_1/F_0$ increases as spike count is reduced. (C) Histograms of $F_1/F_0$ for various spike counts for an example of phase-sensitive complex cell. The mean of the distribution for each spike count, indicated by the vertical black lines, remains relatively constant as the spike count is reduced. (D) Histograms of $F_1/F_0$ for various spike counts for an example of phase-invariant complex cell. The mean of these distributions clearly increases as the number of spikes available is reduced."

<center>Fig. 4. Change in estimated \(F_{1} / F_{0}\) with spike count for 220 cortical neurons. (A) The relationship between \(F_{1} / F_{0}\) and spike count for cells which lie above their corresponding \(99\%\) confidence limit (solid grey curve). These cells show relatively little change in \(F_{1} / F_{0}\) as the number of spikes is reduced. (B) The relationship between \(F_{1} / F_{0}\) and spike count for cells which lie below their corresponding \(99\%\) confidence limit tend to follow the trend predicted by an ideal phase-invariant mechanism (dashed grey curve). For these cells \(F_{1} / F_{0}\) increases as spike count is reduced. (C) Histograms of \(F_{1} / F_{0}\) for various spike counts for an example of phase-sensitive complex cell. The mean of the distribution for each spike count, indicated by the vertical black lines, remains relatively constant as the spike count is reduced. (D) Histograms of \(F_{1} / F_{0}\) for various spike counts for an example of phase-invariant complex cell. The mean of these distributions clearly increases as the number of spikes available is reduced. </center>

statistical criterion for assessing the significance of modulation in observed spiking responses. This criterion accounts for the number of spikes recorded and allows differentiation of reliable phase- sensitive responses from those that appear modulated simply due to the limited data available. It is important to note that our statistical criterion is not itself a measure of phase sensitivity. Our criterion adds a measure of statistical significance to the established metric of \(F_{1} / F_{0}\) for assessing phase sensitivity.  

We propose a conservative threshold for significance, rejecting the null hypothesis - that observed neural responses arise by way of an ideal phase- invariant neural mechanism - only if the observed \(F_{1} / F_{0}\) exceeds the corresponding \(99\%\) confidence limit. By this criterion, we show that approximately \(70\%\) of neurons in our sample of cat area 17/18 neurons exhibit statistically significant (i.e., reliable) modulation of their responses (Fig. 2). Notably, these cells showed virtually no change in \(F_{1} / F_{0}\) with changes in spike count (Fig. 4A), suggesting that these cells can reliably signal the phase of the stimulus - that is to say, these cells are phase sensitive. In contrast, complex cells that do not have highly modulated responses ( \(F_{1} / F_{0} < 1\) , and below the \(99\%\) confidence limit) exhibit highly predictable dependence on spike count. Specifically, estimates of their \(F_{1} / F_{0}\) follow that predicted by an ideal phase- invariant mechanism (Fig. 4B). Therefore, these cells are phase invariant.

A substantial population of phase- sensitive complex cells, such as that we observe, raises the question of whether the phase information carried by these cells could be used by higher cortical areas. While a detailed discussion of this topic is beyond the present study, we can address more mechanistic questions. For example, from a population of phase- sensitive complex cells, is it possible to estimate phase from a single stimulus presentation, and how many phase- sensitive complex cells would be required? Our ideal complex cell model provides some insight into this question. Using an average (median) phase- sensitive complex cell with an \(F_{1} / F_{0}\) of 0.48 and 19.08 spikes/cycle, we must pool responses from 4.26 cells to collect enough spikes in a single cycle to exceed the \(99\%\) confidence limit. This suggests that pooling responses from a population of as few as five phase- sensitive complex cells could reliably encode phase information with a confidence level of \(99\%\) .

The prevalence of phase- sensitive responses among neurons in primary visual cortex has implications for models of processing and coding of visual information in the brain. An enduring hypothesis regarding cortical processing holds that simple and complex cells represent hierarchical stages of processing (Hubel and Wiesel, 1962). In the first stage simple cells combine different input from the lateral geniculate nucleus (LGN) into spatially segregated zones within their receptive fields. In the second stage, complex cells combine input from phase- sensitive simple cells and in doing so become less selective for stimulus attributes such as position (i.e., spatial phase). The hierarchical model suggests a convergence of geniculate inputs from the thalamus onto simple cells and the convergence of simple cells onto complex cells (Hubel and Wiesel, 1962).

Consistent with such hierarchy, simple cells in cortical layer 4 receive monosynaptic input from cells in the LGN (Reid and Alonso, 1995; Martinez et al., 2005) and are known to project to layers 2/3 (Gilbert and Wiesel, 1979; Lund et al., 1979; Martin and Whittieridge, 1984; Hirsch et al., 1995). In turn, some complex cells in layer 2/3 receive monosynaptic excitatory input from simple cells in layer 4 (Alonso and Martinez, 1998). However, hierarchical convergence of simple cells onto complex cells is likely only one circuit evident in the cortex: inactivation of layer A in the LGN inactivates layer 4 simple cells but not all layer 2/3 complex cells (Malpeli, 1983) and some complex cells receive direct geniculate input (Hoffmann and Stone, 1971; Stone and Dreher, 1973; Toyama et al., 1973; Singer et al., 1975; Bullier and Henry, 1979; Heggelund, 1981; Ferster and Lindstrom,

1983; Tanaka, 1983, 1985; Martin and Whittieridge, 1984). Nevertheless, hierarchical convergence of simple cells onto complex cells is a common feature of a number of computational models able to reproduce many phenomena observed in real cortical neurons (Movshon et al., 1978b; Adelson and Bergen, 1985; Ohzawa et al., 1990; Heeger, 1992). In these models complex cells combine the squared output of simple cells whose spatial receptive fields are arranged in quadrature. In this context, modulated responses such as those we observe from many complex cells could arise through a number of deficiencies in the hierarchical circuits realised in the cortex, e.g., if the afferent simple cells are not perfectly in quadrature or if their receptive fields are spatially offset, or if they exhibit different spatio-temporal tuning or different gains (for a discussion of the possible mechanisms see Heeger, 1992). Our data quantify for the first time the prevalence of reliably modulated responses among complex cells and suggest that deficiencies such as these may be common in cortex (60% of complex cells in our population exhibit statistically reliable modulation of their response to optimal moving sine-wave gratings).

None of the feed- forward hierarchical models of cortical processing adequately account for the fact that the majority of synapses in primary visual cortex mediate local excitatory recurrent connections between cortical neurons. An alternative model of cortical processing holds that complex cells receive phase- sensitive excitatory input, either from simple cells or by directly combining inputs from the LGN, and are coupled in a recurrent network of excitatory connections (Chance et al., 1999, cf. also Bardy et al., 2006). In this model, phase invariance arises not by combining phase- sensitive excitatory inputs, but rather through recurrent excitatory connections between cortical neurons. Phase- sensitive modulated responses arise when recurrent connections are weak whilst phase- invariant unmodulated responses arise when recurrent connections are strong. We have previously argued against such a recurrent model, at least for a subset of complex cells (van Kleef et al., 2010). However, it is plausible that the prevalence of modulated responses among cortical neurons, as quantified here, reflects a balance between afferent and recurrent connections, biased towards afferent input. In which case, recurrent connections could arguably serve primarily to increase the dynamic range of cortical neurons by amplifying weak afferent input (Douglas et al., 1995; Tao et al., 2004; also Priebe and Ferster, 2012, for a wide- ranging review).

Acknowledgements—This work was supported by the Australian Research Council (Grant CE561903) and the National Health and Medical Research Council of Australia (Grants 457525 and 525461).

## REFERENCES

Adelson EH, Bergen JR (1985) Spatiotemporal energy models for the perception of motion. J Opt Soc Am A 2:284- 299.  
Alonso JM, Martinez LM (1998) Functional connectivity between simple cells and complex in cat striate cortex. Nat Neurosci 1:395- 403.  
Baker GE, Thompson ID, Krug K, Smyth D, Tolhurst DJ (2001) Spatial- frequency tuning and geniculocortical projections in the visual cortex (areas 17 and 18) of the pigmented ferret. Eur J Neurosci 10:2657- 2668.  
Bardy C, Huang JY, FitzGibbon T, Dreher B (2006) 'Simplification' of responses of complex cells in cat striate cortex: suppressive surrounds and 'feedback' inactivation. J Physiol (Lond) 574:731- 750.  
Bullier J, Henry GH (1979) Laminar distribution of first order neurons and afferent terminals in cat striate cortex. J Neurophysiol 42:1271- 1281.  
Chance F, Nelson S, Abbott L (1999) Complex cells as cortically amplified simple cells. Nat Neurosci 2:277- 282.  
Crowder NA, Price NSC, Hietanen MA, Dreher B, Clifford CWG, Ibbotson MR (2006) Relationship between contrast adaptation and orientation tuning in areas V1 and V2 of cat visual cortex. J Neurophysiol 95:271- 283.  
Crowder NA, Van Kleef J, Dreher B, Ibbotson MR (2007) Complex cells increase their phase- sensitivity at low contrasts and following adaptation. J Neurophysiol 98:1155- 1166.  
Dean AF, Tolhurst DJ (1983) On the distinctness of simple and complex cells in the visual cortex of the cat. J Physiol (Lond) 344:305- 325.  
De Valois RL, Albrecht DG, Thorell LG (1982) Spatial frequency selectivity of cells in macaque visual cortex. Vision Res 22:545- 559.  
Douglas RJ, Koch C, Mahowald M, Martin KAC, Suarez HH (1995) Recurrent excitation in neocortical circuits. Science 269:981- 985.  
Ferster D, Lindstrom S (1983) An intracellular analysis of geniculocortical connectivity in area 17 of the cat. J Physiol (Lond) 342:181- 215.  
Gilbert CD, Wiesel TN (1979) Morphology and intracortical projections of functionally characterized neurons in the cat visual cortex. Nature 280:120- 125.  
Girman SV, Suave Y, Lund RD (1999) Receptive field properties of single neurons in rat primary visual cortex. J Neurophysiol 82:301- 311.  
Heeger DJ (1992) Normalization of cell responses in cat striate cortex. Vis Neurosci 9:181- 197.  
Heggelund P (1981) Receptive field organization of complex cells in cat striate cortex. Exp Brain Res 42:99- 107.  
Hirsch JA, Alonso JM, Reid RC (1995) Visually evoked calcium action potentials in cat striate cortex. Nature 378:612- 616.  
Hoffmann K- P, Stone J (1971) Conduction velocity of afferents of cat visual cortex: a correlation with cortical receptive field properties. Brain Res 32:460- 466.  
Hubel DH, Wiesel TN (1962) Receptive fields, binocular interaction and functional architecture in cats visual cortex. J Physiol (Lond) 160:106- 154.  
Ibbotson MR, Price NSC, Crowder NA (2005) On the division of cortical cells into simple and complex types: a comparative viewpoint. J Neurophysiol 93:3699- 3702.  
Lund JS, Henry GH, Macqueen CL, Harvey AR (1979) Anatomical organization of the primary visual cortex (area 17) of the cat. A comparison with area 17 of the macaque monkey. J Comp Neurol 184:599- 618.  
Malpeil JG (1983) Activity of cells in area 17 of the cat in absence of input from layer A of lateral geniculate nucleus. J Neurophysiol 49:595- 610.  
Martin KAC, Whitteridge D (1984) Form, function and intracortical projections of spiny neurons in the striate visual cortex of the cat. J Physiol (Lond) 353:463- 504.  
Martinez LM, Wang Q, Reid RC, Pillai C, Alonso JM, Sommer FT, Hirsch JA (2005) Receptive field structure varies with layer in the primary visual cortex. Nat Neurosci 8:372- 379.  
Mata ML, Ringach DL (2005) Spatial overlap of On and Off subregions and its relation to response modulation ratio in macaque primary visual cortex. J Neurophysiol 93:918- 928.  
Mechler F, Ringach DL (2002) On the classification of simple and complex cells. Vision Res 42:1017- 1033.  
Movshon JA, Thompson IF, Tolhurst DJ (1978a) Spatial summation in the receptive fields of simple cells in the cat's striate cortex. J Physiol (Lond) 283:53- 77.  
Movshon JA, Thompson IF, Tolhurst DJ (1978b) Receptive field organization of complex cells in the cat's striate cortex. J Physiol (Lond) 283:79- 99.  
Movshon JA, Thompson IF, Tolhurst DJ (1978c) Spatial and temporal contrast sensitivity of neurones in areas 17 and 18 of the cat's visual cortex. J Physiol (Lond) 283:101- 120.  
Niell CM, Stryker MP (2008) Highly selective receptive fields in mouse visual cortex. J Neurosci 28:7520- 7536.  
Ohzawa I, DeAngelis GC, Freeman RD (1990) Stereoscopic depth discrimination in the visual cortex: neurons ideally suited as disparity detectors. Science 243:1037- 1041.  
Priebe NJ, Ferster D (2012) Mechanisms of neuronal computation in mammalian visual cortex. Neuron 75:194- 208.  
Reid RC, Alonso JM (1995) Specificity of monosynaptic connections from thalamus to visual cortex. Nature 378:281- 284.  
Romo PA, Wang C, Zeater N, Solomon SG, Dreher B (2011) Phase sensitivities, excitatory summation fields, and silent suppressive receptive fields of single neurons in the parastriate cortex of the cat. J Neurophysiol 106:1688- 1712.  
Singer W, Tretter F, Cynader M (1975) Organization of cat striate cortex: a correlation of receptive- field properties with afferent and efferent connections. J Neurophysiol 38:1080- 1098.  
Skottun BC, De Valois RL, Grosfod DH, Movshon JA, Albrecht DG, Bonds AB (1991) Classifying simple and complex cells on the basis of response modulation. Vision Res 7:1079- 1086.  
Stone J, Dreher B (1973) Projection of X- and Y- cells of the cat's lateral geniculate nucleus to areas 17 and 18 of visual cortex. J Neurophysiol 36:551- 567.  
Tanaka K (1983) Cross- correlation analysis of geniculo- striate relationships in cats. J Neurophysiol 49:1303- 1318.  
Tanaka K (1985) Organization of geniculate inputs to visual cortical cells in the cat. Vision Res 25:357- 364.  
Toyama K, Maekawa K, Takeda T (1973) An analysis of neuronal circuitry for two types of visual cortical neurons classified on the basis of their responses to photic stimuli. Brain Res 61:395- 399.  
Tao L, Shelley M, McLaughlin D, Shapley R (2004) An egalitarian network model for the emergence of simple and complex cells in visual cortex. PNAS 101:366- 371.  
van Kleef JP, Cloherty SL, Ibbotson MR (2010) Complex cell receptive fields: evidence for a hierarchical mechanism. J Physiol (Lond) 588:3457- 3470.  
Wilkie D (1983) Rayleigh test for randomness of circular data. Appl Stat 32:311- 312.

## APPENDIX A

Here we derive an expression for the expected \(F_{1} / F_{0}\) of a neural response that consists of \(n\) spikes distributed randomly with uniform probability across a single grating cycle \([- \pi , \pi ]\) . Furthermore, for large \(n\) we derive an expression of the value of \(F_{1} / F_{0}\) required for a significance level of \(x\) .

If spikes occur at times \(t_{i} \in [- \pi , \pi ]\) , \(i = 1 \ldots n\) , where \(n\) is the number of spikes, then we may express the response of the cell as a sum of delta functions,

\[r(t) = \sum_{i = 1}^{n} \delta (t - t_{i}). \quad (A1)\]

We want to estimate the magnitude of the first two terms \((F_{0}\) and \(F_{1}\) ) of the Fourier series expansion of \(r(t)\) . From the definition of the Fourier series,

\[F_{0} = \frac{1}{2\pi}\int_{-\pi}^{\pi}r(t)\mathrm{d}t = \frac{1}{2\pi}\int_{-\pi}^{\pi}\sum_{i = 1}^{n}\delta (t - t_{i})\mathrm{d}t = \frac{n}{2\pi}, \quad (A2)\]

and

\[\begin{array}{l}{F_{1} = \frac{1}{\pi}\left|\int_{-\pi}^{\pi}r(t)\mathrm{e}^{-i t}\mathrm{d}t\right| = \frac{1}{\pi}\left|\int_{-\pi}^{\pi}\sum_{i = 1}^{n}\delta (t - t_{i})\mathrm{e}^{-i t}\mathrm{d}t\right|}\\ {= \frac{1}{\pi}\left|\sum_{i = 1}^{n}\mathrm{e}^{-i t}\right| = \frac{1}{\pi}\left|z\right|,} \end{array} \quad (A3)\]

where,

\[z = \sum_{i = 1}^{n}\mathrm{e}^{-it}. \quad (A3)\]

Combining Eqs. (A2) and (A3),

\[\frac{F_{1}}{F_{0}} = \frac{|z|}{\pi}\cdot \frac{2\pi}{n} = \frac{2|z|}{n} \quad (A4)\]

We note that \(z\) is equivalent to an \(n\) step random walk in 2- dimensional space with each step having a fixed length equal to one and a uniform probability of heading in any direction on \([- \pi , \pi ]\) . The expected squared length of such a walk is \(n\) and therefore the root- mean- square distance is \(\sqrt{n}\) . Thus, the expected value of \(F_{1} / F_{0}\) is given by

\[\frac{F_{1}}{F_{0}} = \frac{2\sqrt{n}}{n} = \frac{2}{\sqrt{n}}.\]

Furthermore, for any distance \(r > 0\) and for \(n \to \infty\) the function that describes the probability that \(|z| = r\) is asymptotic to the Rayleigh function,

\[f(r; n) = \frac{2r}{n} e^{-\frac{r^2}{n}},\]

which has a cumulative distribution function,

\[F(r; n) = 1 - \mathrm{e}^{-\frac{r^2}{n}}.\]

To achieve a significance level of \(x\) we need \(F(r; n) = 1 - x\) . Therefore,

\[1 - \mathrm{e}^{-\frac{r^2}{n}} = 1 - x.\]

Solving for \(r\) ,

\[r = \sqrt{-n\ln(x)}.\]

From Eq. (A4),

\[\frac{F_{1}}{F_{0}} = \frac{2\sqrt{-n\ln(x)}}{n} = \frac{k}{\sqrt{n}}, \quad (A5)\]

where

\[k = 2\sqrt{- \ln(x)}.\]

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
