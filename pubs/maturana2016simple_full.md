```
@article{maturana2016simple,
  title={A Simple and Accurate Model to Predict Responses to Multi-electrode Stimulation in the Retina},
  author={Matias I. Maturana and Nicholas V. Apollo and Alex E. Hadjinicolaou and David J. Garrett and Shaun L. Cloherty and Tatiana Kameneva and David B. Grayden and Michael R. Ibbotson and Hamish Meffin},
  journal={PLoS Computational Biology},
  year={2016},
  volume={12},
  doi={10.1371/journal.pcbi.1004849},
  url={https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1004849}
}
```

---

# RESEARCH ARTICLE

# A Simple and Accurate Model to Predict Responses to Multi-electrode Stimulation in the Retina

Matias I. Maturana \(^{1,2}\) , Nicholas V. Apollo \(^{3}\) , Alex E. Hadjinicolaou \(^{1}\) , David J. Garrett \(^{3}\) , Shaun L. Cloherty \(^{1,2,4}\) , Tatiana Kameneva \(^{2}\) , David B. Grayden \(^{2,5}\) , Michael R. Ibbotson \(^{1,4}\) , Hamish Meffin \(^{1,4,*}\)

> **Image description.** A logo or branding graphic centered on a plain white background. The image consists of a stylized emblem positioned above text.
>
> The central emblem is a circular design. It features a thick, dark blue or slate-grey outer ring. Inside this ring is a stylized, reddish-orange or terracotta shape that resembles a folded ribbon or banner. This ribbon shape is curved and tapers to a point at the bottom center.
>
> Below the emblem, the text is arranged in two lines:
> 1. The word "CrossMark" is displayed prominently in a dark, sans-serif font.
> 2. Directly beneath "CrossMark," the phrase "click for updates" is written in a smaller, lighter font.
>
> The overall design is clean and professional, utilizing a limited color palette of dark blue, reddish-orange, and black text.

CrossMark click for updates

1 National Vision Research Institute, Australian College of Optometry, Carlton, Victoria, Australia, 2 Department of Electrical and Electronic Engineering, NeuroEngineering Laboratory, University of Melbourne, Parkville, Victoria, Australia, 3 Department of Physics, University of Melbourne, Parkville, Victoria, Australia, 4 Department of Optometry and Vision Sciences, ARC Centre of Excellence for Integrative Brain Function, University of Melbourne, Parkville, Victoria, Australia, 5 Centre for Neural Engineering, University of Melbourne, Parkville, Victoria, Australia

\* hmeffin@unimelb.edu.au

## 6 OPEN ACCESS

Citation: Maturana MI, Apollo NV, Hadjinicolaou AE, Garrett DJ, Cloherty SL, Kameneva T, et al. (2016) A Simple and Accurate Model to Predict Responses to Multi- electrode Stimulation in the Retina. PLoS Comput Biol 12(4): e1004849. doi:10.1371/journal.pcbi.1004849

Editor: Jonathan W. Pillow, The University of Texas at Austin, UNITED STATES

Received: December 4, 2015

Accepted: March 4, 2016

Published: April 1, 2016

Copyright: © 2016 Maturana et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: All relevant data contained within this manuscript can be found on GitHub: https://github.com/matiasm- UoM/Multi- electrode- white- noise.

Funding: This work was funded by: Centre of Excellence for Integrative Brain Function, Australian Research Council, CE140100007, http://www.arc.gov.au; Discovery Early Career Researcher Award, Australian Research Council, DE120102210, http://www.arc.gov.au; and Discovery Project, Australian Research Council, DP140104533, http://www.arc.gov.au/. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing Interests: The authors have declared that no competing interests exist.

## Abstract

Implantable electrode arrays are widely used in therapeutic stimulation of the nervous system (e.g. cochlear, retinal, and cortical implants). Currently, most neural prostheses use serial stimulation (i.e. one electrode at a time) despite this severely limiting the repertoire of stimuli that can be applied. Methods to reliably predict the outcome of multi- electrode stimulation have not been available. Here, we demonstrate that a linear- nonlinear model accurately predicts neural responses to arbitrary patterns of stimulation using in vitro recordings from single retinal ganglion cells (RGCs) stimulated with a subretinal multi- electrode array. In the model, the stimulus is projected onto a low- dimensional subspace and then undergoes a nonlinear transformation to produce an estimate of spiking probability. The low- dimensional subspace is estimated using principal components analysis, which gives the neuron's electrical receptive field (ERF), i.e. the electrodes to which the neuron is most sensitive. Our model suggests that stimulation proportional to the ERF yields a higher efficacy given a fixed amount of power when compared to equal amplitude stimulation on up to three electrodes. We find that the model captures the responses of all the cells recorded in the study, suggesting that it will generalize to most cell types in the retina. The model is computationally efficient to evaluate and, therefore, appropriate for future real- time applications including stimulation strategies that make use of recorded neural activity to improve the stimulation strategy.

## Author Summary

Implantable multi- electrode arrays (MEAs) are used to record neurological signals and stimulate the nervous system to restore lost function (e.g. cochlear implants). MEAs that can combine both sensing and stimulation will revolutionize the development of the next generation of devices. Simple models that can accurately characterize neural responses to electrical stimulation are necessary for the development of future neuroprostheses controlled by neural feedback. We demonstrate a model that accurately predicts neural responses to concurrent stimulation across multiple electrodes. The model is simple to evaluate, making it an appropriate model for use with neural feedback. The methods described are applicable to a wide range of neural prostheses, thus greatly assisting future device development.

## Introduction

Implantable electrode arrays are widely used in clinical studies, clinical practice and basic neuroscience research and have advanced our understanding of the nervous system. Implantable electronic devices can be used to record neurological signals and stimulate the nervous system to restore lost functions. Sensing electrodes have been used in applications such as brain- machine interfaces [1] and localization of seizure foci in epilepsy [2]. Stimulating electrodes have been used for the restoration of hearing [3], sight [4,5], bowel control [6], and balance [7], and in deep brain stimulation (DBS) to treat a range of conditions [8]. Most neuroprostheses operate in an open- loop fashion; they require psychophysics to tune stimulation parameters. However, devices that can combine both sensing and stimulation are desirable for the development of a new generation of neuroprostheses that are controlled by neural feedback. Feedback in neuroprostheses is being explored in applications such as DBS for the enhancement of memory [9], abatement of seizures [10], control of Parkinson's disease [11], and the control of brain machine interfaces [12].

Models that can accurately characterize a neural system and predict responses to electrical stimulation are beneficial to the development of improved stimulation strategies that exploit neural feedback. Volume conductor models are typically used to describe retinal responses to electrical stimulation, however these are computationally intensive and can be difficult to fit to neural response data [13- 15]. Simpler models that can be constrained using neural recordings are necessary for real- time applications. Linear- nonlinear models based on a spike- triggered average (STA) have been successfully used to characterize retinal responses to light [16- 19]. Models that incorporate higher dimensional components identified through a spike- triggered covariance (STC) analysis have been explored to describe higher order excitatory and suppressive features of the visual system [20- 25]. Generally, STA and STC models make use of white noise inputs and have the advantage that a wide repertoire of possible inputs patterns can be explored. White noise models have previously been explored to describe the temporal properties of electrical stimulation in the retina [26,27]. Spatial interactions between stimulating electrodes has not been previously investigated. An example of a stimulation algorithm that could benefit from an accurate description of the spatial interactions is current steering, which attempts to improve the resolution of a device by combining stimulation across many electrodes to target neurons at a particular point [28].

Two benefits obtained by using neural feedback algorithms are (1) the accurate prediction of the response to an arbitrary stimulus across the electrode array and (2) the ability to fit the device to individual patients from the recorded neural responses to a set of stimuli presented in a reasonable amount of time. Here, we combine whole cell patch clamp recordings from individual retinal ganglion cells (RGCs) with stimulation using a multi- electrode array to demonstrate a model with the above advantages. We find that a simple linear- nonlinear model

accurately captures the effects of multi- electrode interactions and estimates the spatial relationship between stimulus and response. The approach is scalable to a large number of electrodes, which is prohibitive to accomplish with psychophysics. In contrast to conventional volume conductor models of electrical stimulation [13–15], our model is straightforward to constrain using neural response data and is orders of magnitude more computationally efficient, making it suitable for use in real- time applications.

## Materials and Methods

## Retinal whole mount preparation

Methods conformed to the policies of the National Health and Medical Research Council of Australia and were approved by the Animal Experimentation Ethics Committee of the University of Melbourne (Approval Number: 1112084). Data were acquired from retinae of Long- Evans rats ranging from 1 to 6 months of age. Long- Evans rats were chosen for several reasons. First, rat RGC morphological types have been examined in detail [29,30] and have similarities to RGCs found in other species, including the macaque monkey [31] and cat [32,33]. Second, the size of the rat retina is larger than the mouse retina and so we were able to cover the entire stimulating electrode array with half of the retina.

The animals were initially anesthetized with a mixture of ketamine and xylazine prior to enucleation. After enucleation, the rats were euthanized with an overdose of pentobarbital sodium (350 mg intracardiac). Dissections were carried out in dim light conditions to avoid bleaching the photoreceptors. After hemisecting the eyes behind the ora serrata, the vitreous body was removed and each retina was cut into two pieces. The retinae were left in a perfusion dish with carbonated Ames medium (Sigma) at room temperature until used. Pieces of retina were mounted on a multi- electrode array (MEA) with ganglion cell layer up and were held in place with a perfusion chamber and stainless steel harp fitted with Lycra threads (Warner Instruments) (Fig 1A). Once mounted in the chamber, the retina was perfused (4–6 mL/min) with carbonated Ames medium (Sigma- Aldrich, St. Louis, MO) at room temperature. The chamber was mounted on the stage of an upright microscope (Olympus Fluoview FV1200) equipped with a \(\times 40\) water immersion lens and visualized with infrared optics on a monitor with \(\times 4\) additional magnification.

## Multi-electrode array fabrication

Electrical stimulation was applied subretinally through a custom- made MEA fabricated on a glass coverslip consisting of 20 platinum stimulating electrodes (Fig 1). Each electrode had an exposed disc of \(400 \mu \mathrm{m}\) diameter, and a vertical pitch of \(1 \mathrm{mm}\) . The stimulating area of the MEA spanned an area of \(3.5 \times 3.5 \mathrm{mm}^2\) (excluding the outer ring which was not used). Glass coverslips were cleaned in an oxygen plasma chamber for 20 minutes (Fig 1B). Next, a positive (UV- removable) photoresist (AZ1415H, Microchemicals) was spin- coated onto the surface at 4000 revolutions per minute for 60 seconds (Fig 1C). A laser- printed chrome on soda glass photolithography mask was used to expose a pattern in the photoresist, then developed chemically (MIF726, Microchemicals) revealing openings for electrode pads and tracks (Fig 1D and 1E). The developed cover slips were loaded into an electron beam deposition chamber (Thermionics) and pumped to a vacuum pressure of \(1.5 \times 10^{- 6}\) mbar. A 20 nm titanium adhesion layer was deposited at a rate of \(0.2 \mathrm{\AA / sec}\) , followed by a platinum deposition of \(130 \mathrm{nm}\) at a rate of \(0.6 \mathrm{\AA / sec}\) . Residual photoresist was removed by soaking in acetone for 30 minutes, rinsing with deionized water, and finally oxygen plasma cleaning for 10 minutes. For electrode isolation, a negative (UV- curing) photoresist (SU8- 2002, Microchemicals) was spin- coated onto the coverslip and exposed through a different photolithography mask leaving only metal exposed for

> **Image description.** A multi-panel technical diagram illustrating the fabrication process and final application of a platinum stimulating electrode array for retinal research. The figure is divided into eight labeled panels (a through h), detailing the progression from raw materials to the final biological setup.
>
> The fabrication steps are shown in panels (b) through (g):
> *   **Panel (b)** shows the starting material: a flat, gray, rectangular glass cover slip labeled "Plasma-cleaned glass cover slip."
> *   **Panel (c)** depicts the application of a uniform layer of positive photoresist onto the cover slip, labeled "Glass cover slip spin-coated with positive photoresist."
> *   **Panel (d)** illustrates the patterning stage, where the photoresist has been selectively removed using a photolithography mask, resulting in a distinct, irregular, dumbbell-shaped pattern of exposed material.
> *   **Panel (e)** shows the deposition of a metal layer (Titanium/platinum) onto the patterned substrate, labeled "Titanium/platinum metal evaporation to create pattern where photoresist from (d) was removed; the residual photoresist was removed using acetone."
> *   **Panel (f)** shows the application of an insulating layer, SU-8, which covers the platinum pattern, labeled "An insulating layer of SU-8 is spin-coated onto the platinum pattern."
> *   **Panel (g)** shows the insulation being opened to reveal the finished platinum electrodes, which are described as having a 400\mu m diameter.
>
> The final product and application are shown in panels (h) and (a):
> *   **Panel (h)** is a high-magnification photograph of the completed platinum electrode array. It displays numerous small, circular metallic electrodes arranged in a grid. A red dashed box highlights a specific electrode, with scale indicators showing the electrode diameter is 400\mu m and the center-to-center pitch is 600\mu m.
> *   **Panel (a)** shows the final experimental setup. A biological sample, the Retina, is placed on the array of Electrodes. A thin, green glass Patch clamp pipette is positioned over the retina, indicating the method used for recording from exposed retinal ganglion cell bodies.
>
> The overall figure provides a visual guide to the microfabrication techniques used to create the stimulating array and its subsequent use in whole-cell intracellular recordings.

<center>Fig 1. Whole mount preparation and fabrication steps of the platinum stimulating electrode array. (a) The retina was placed on the stimulating array ganglion cell side up. An intracellular patch pipette was used to record from exposed retinal ganglion cell bodies. b) Plasma-cleaned glass cover slip. (c) Glass cover slip spin-coated with positive photoresist. (d) Photoresist removed selectively (dumb-bell shaped pattern for demonstration only) using photolithography mask. (e) Titanium/platinum metal evaporation to create pattern where photoresist from (d) was removed; the residual photoresist was removed using acetone. (f) An insulating layer of SU-8 is spin-coated onto the platinum pattern. (g) The insulation is opened to reveal platinum electrodes having \(400\mu \mathrm{m}\) diameter. (h) The platinum electrode array is surrounded by a ring of shorted electrodes, which was not used in this work. All electrodes have an exposed disc of \(400\mu \mathrm{m}\) diameter and a \(1\mathrm{mm}\) center-to-center pitch in the vertical direction. The central portion of the stimulating array (excluding the outer ring) covered an area of approximately \(3.5\mathrm{mm}\times 3.5\mathrm{mm}\) . </center>

doi:10.1371/journal.pcbi.1004849. g001

stimulating electrodes and contact pads (Fig 1F and 1G). The entire device was then cured at \(200^{\circ}\mathrm{C}\) on a temperature- controlled hotplate.

## Data acquisition

Whole cell intracellular recordings were obtained using standard procedures [34] at room temperature. The main reason for recording at room temperature was to ensure that recordings lasted for many hours. To obtain a whole cell recording, a small hole was made in the inner limiting membrane to expose a small number of RGC somas. A pipette was then filled with internal solution containing (in mM) 115 K- gluconate, 5 KCl, 5 EGTA, 10 HEPES, 2 Na- ATP, 0.25 Na- GTP (mosM = 273, pH = 7.3), Alexa Hydrazide 488 (250 mM), and biocytin (0.5%) (Fig 1A). Initial pipette resistance in the bath ranged between \(5 - 10\mathrm{M}\Omega\) . Prior to recording, the pipette voltage was nulled, pipette resistance was compensated with the bridge balancing circuit of the amplifier, and capacitance was compensated on the amplifier head stage. Voltage recordings were collected in current clamp mode and amplified (SEC- 05X, NPI electronic), digitized with 16- bit precision at \(25\mathrm{kHz}\) (National Instruments BNC- 2090), and stored for offline analysis.

Intracellular recordings lasting up to 4 hours were obtained. Stimulation artefacts that were present in the intracellular recording were removed offline by setting the membrane potential

> **Image description.** This image is a technical figure, labeled "Fig 2," illustrating the parameters of random electrical pulses applied to 20 electrodes. It is composed of two distinct panels, (a) and (b), which provide a snapshot of amplitude and a time-course view of the applied pulses.
>
> **Panel (a): Amplitude Snapshot**
> Panel (a) displays a 4x5 grid containing 20 circular icons, each representing an electrode. Each circle contains a stylized biphasic pulse waveform. The color of the waveform indicates the pulse amplitude, as defined by a vertical color bar (legend) positioned to the right of the grid.
> *   **Color Scale:** The legend is labeled "Pulse amplitude ($\mu$A)" and ranges from -300 (dark blue) to +300 (dark red), with 0 in the center.
> *   **Electrode Identification:** Below each circular icon, a number (1 through 20) identifies the specific electrode.
> *   **Interpretation:** The colors visually represent the random amplitude sampled from a Gaussian distribution. Positive amplitudes (red tones) correspond to anodic-first pulses, while negative amplitudes (blue tones) correspond to cathodic-first pulses.
>
> **Panel (b): Time Course**
> Panel (b) is a time-series plot showing the temporal application of the biphasic pulses to each electrode.
> *   **Axes:** The vertical axis is labeled "Electrode number," ranging from 1 to 20. The horizontal axis is labeled "Time (ms)," ranging from 0 to 1.
> *   **Waveforms:** Twenty distinct waveforms are plotted, one for each electrode. These waveforms are biphasic pulses, characterized by a rapid positive and negative deflection.
> *   **Visual Pattern:** The pulses vary in duration and amplitude across the 20 electrodes, demonstrating the random nature of the stimulation. The pulses are generally rectangular in shape, representing the constant application of the stimulus for a set duration.
>
> **Overall Caption and Context**
> The figure is accompanied by a detailed caption: "Fig 2. Sample of the random pulses applied to 20 electrodes at a given time. (a) Snapshot of the random amplitude of biphasic pulses applied to all electrodes; the colors indicate amplitudes in $\mu$A. A positive amplitude produces an anodic-first pulse; a negative amplitude produces a cathodic-first pulse. Electrode amplitudes were sampled from a Gaussian distribution with variance $\sigma^2$. Electrode numbers are shown below each electrode. (b) Time course of the biphasic pulse applied to each electrode."

<center>Fig 2. Sample of the random pulses applied to 20 electrodes at a given time. (a) Snapshot of the random amplitude of biphasic pulses applied to all electrodes; the colors indicate amplitudes in \(\mu \mathrm{A}\) . A positive amplitude produces an anodic-first pulse; a negative amplitude produces a cathodic-first pulse. Electrode amplitudes were sampled from a Gaussian distribution with variance \(\sigma^2\) . Electrode numbers are shown below each electrode. (b) Time course of the biphasic pulse applied to each electrode. </center>

doi:10.1371/journal.pcbi.1004849. g002

to a constant value for the duration of the stimulus. Spikes in the remaining membrane potential waveform could be easily detected by finding peaks that crossed a set value. Spike times were calculated as the time that the action potential reached its peak value. Spike delay times were calculated by taking the difference between the spike time and the preceding stimulus offset time.

Intrinsic physiological differences, such as spike width, membrane time constant, and input resistance, among RGC types have been described [35,36], which could lead to differences in response latencies to electrical stimulation. Therefore, we performed a k- means cluster analysis on the spike latency from stimulation offset time. The number of clusters (k) to fit was set manually by visual inspection of the clusters. From the cluster analysis, we could detect if there were two or more clusters that might be attributed to direct activation or indirect activation via activation of presynaptic neurons. Unless otherwise stated, responses to electrical stimulation were evaluated by analyzing the short- latency responses. Short- latency responses were spikes that fell within two standard deviations of the mean of the shortest- latency cluster. Long- latency responses fell within the cluster that occurred directly after the short- latency response.

## Electrical stimulation

Stimulation consisted of biphasic pulses of equal phase duration (500 \(\mu \mathrm{s}\) ) with an interphase gap (50 \(\mu \mathrm{s}\) ) and random amplitude. The random amplitudes were sampled from a Gaussian distribution with variance \(\sigma^2\) . Fig 2 illustrates the random amplitude pulses applied to all electrodes. Stimulation waveform signals were generated by a custom- made MATLAB (MathWorks version 2014a) interface commanding a multi- channel stimulator (Tucker Davis Technologies: RZ2 base station and IZ2 multichannel stimulator). All stimulus amplitudes were bounded by the limits of the stimulator \((\pm 300 \mu \mathrm{A})\) . Biphasic pulses were applied to all electrodes at a frequency of \(10 \mathrm{~Hz}\) and the numbers of short- latency responses were recorded.

To avoid overstimulation of a cell, an appropriate value of \(\sigma\) was chosen for each cell. Three stimulus trains of 500 pulses were initially generated with fixed \(\sigma = 50 \mu \mathrm{A}\) and applied to the tissue. Next, a new set of stimulus trains were generated using a \(\sigma\) that varied between \(50 \mu \mathrm{A}\)

and \(250~\mu \mathrm{A}\) in steps of \(50~\mu \mathrm{A}\) . The number of spikes detected within \(5\mathrm{ms}\) from the stimulus time was used to compute a response probability. A sigmoidal curve was fit to the data of \(\sigma\) versus response probability to find the value of \(\sigma\) that resulted in half the maximum level of response. For cells where the maximum response probability was close to 1, \(\sigma\) was chosen to be a value that resulted in a response probability of 0.5. For other cells that saturated at a response probability less than 1, \(\sigma\) was a lower value.

Once an appropriate value for \(\sigma\) was chosen for the cell, a stimulus vector, \(\vec{S_{i}}\) , of length 20 (equal to the number of electrodes) was generated by sampling each element from a Gaussian distribution. If the amplitude of stimulation of an electrode exceeded the stimulator limits \((\pm 300~\mu \mathrm{A})\) , then the amplitude value was discarded and a new value was generated from the distribution. Each stimulus was applied 3–5 times before a new \(\vec{S_{i}}\) was generated. The experiment continued for as long as the cell's responses remained stable (usually 3–4 hours). Once cells started to show signs of deterioration (e.g. unstable high frequency spontaneous activity), the experiment was terminated.

## Immunocytochemistry and morphological identification

After recording, the retinal tissue was removed from the chamber and mounted onto filter paper. The tissue was then fixed for \(\sim 45\mathrm{min}\) in phosphate- buffered \(4\%\) paraformaldehyde and stored for up to 2 weeks in \(0.1\mathrm{M}\) phosphate- buffered saline (PBS; pH 7.4) at \(4^{\circ}\mathrm{C}\) . The tissue was then immersed in \(0.5\%\) Triton X- 100 ( \(20\mu \mathrm{g / ml}\) streptavidin conjugated Alexa 488; Invitrogen) in PBS overnight to expose biocytin- filled cells. Tissue was washed thoroughly in PBS, mounted onto Superfrost+ slides, and coverslipped in \(60\%\) glycerol. Cells were then reconstructed in 3D using a confocal microscope (FluoView FV1200).

RGC types were initially identified by their focal light response at the beginning of each experiment. ON cells showed an increase in spike rate at the onset of light; OFF cells showed an increase in spike rate at the offset of light; ON- OFF cells showed an increase in spike rate at the onset or offset of light. Additionally, RGC classification was correlated with morphology based on dendritic stratification in the inner plexiform layer (IPL) [29,30]. The level of stratification was defined as \(0 - 100\%\) from the level of the inner nuclear layer to the level of the ganglion cell layer. The stratification depth \((s(x))\) was quantified as a percentage of the inner plexiform layer (IPL) thickness, according to

\[s(x) = 100\left(\frac{L_{\mathrm{s}} - x}{L_{\mathrm{s}} - L_{\mathrm{c}}}\right). \quad (1)\]

Here, \(x\) refers to the depth of a terminal dendrite and \(L_{\mathrm{s}}\) and \(L_{\mathrm{c}}\) represent the IPL- GCL border and the GCL- INL border of the inner plexiform layer, respectively, where depth decreases from the ganglion cell layer towards the photoreceptor layer. Cells that stratified in the inner part of the IPL \((s(x)\leq 40\%)\) are denoted as OFF- cells. Cells that stratified in the outer part of the IPL \((s(x)\geq 60\%)\) are referred to as ON- cells. For all cells in this study, the physiological and morphological classifications correlated well. Dendritic field sizes were calculated by tracing out a region connecting the dendritic tips of each cell and fitting an ellipse to the region. The major axis of the ellipse was used to estimate the dendritic field size.

## Mathematical model & model estimation

Our objective was to find a mathematical description able to accurately capture the spiking probability of RGCs to subretinal stimulation using a MEA. We characterized neural responses using an \(N\) - dimensional linear subspace of the stimulus space, combined with a nonlinearity

> **Image description.** This image is a technical diagram consisting of two panels, (a) and (b), illustrating the process of recovering spike-triggered stimuli for spike-triggered covariance (STC) analysis.
>
> Panel (a) is a schematic timeline showing the relationship between neural response and applied stimuli. The vertical axis represents time, indicated by an arrow pointing right. The top section is labeled "Response" and shows a horizontal line with several vertical bars, representing neural activity. Below this, the section labeled "Stimuli $S_T$" shows a sequence of vertical lines representing all applied stimuli. Arrows point from these stimuli down to a box labeled "$S_D$," indicating that $S_D$ is the subset of stimuli that successfully evoked a spike.
>
> Panel (b) is a scatter plot representing the projection of stimuli onto a two-dimensional subspace derived from the STC analysis. The axes are labeled "Principal component 1 ($\mu$A)" on the horizontal axis and "Principal component 2 ($\mu$A)" on the vertical axis. The plot contains a dense cloud of small black dots, representing the total applied stimuli ($S_T$). Scattered within this cloud are white crosses ($\times$), which represent the stimuli that generated a response ($S_D$). Two large geometric shapes are overlaid on the data cloud: a large white circle ($\circ$) labeled $\overline{w}^-$ (representing the projection of the negative electrical receptive field) and a large white diamond ($\diamond$) labeled $\overline{w}^+$ (representing the projection of the positive electrical receptive field). The overall arrangement shows the distribution of the stimuli in the reduced principal component space.

<center>Fig 3. Recovery of the spike-triggered stimuli for the spike-triggered covariance (STC) analysis. (a) Discretized sequence of the neural response and stimulus. Each stimulus consists of a combination of biphasic pulses applied to all 20 electrodes. Stimuli that evoked a spike in the neuron are recorded in the stimulus matrix \(\mathbf{S}_{\mathrm{D}}\) . (b) STC was conducted on the stimuli generating a response, \(\mathbf{S}_{\mathrm{D}}\) , to separate the stimulus space into a positive and negative region (+ and \(\times\) ). The \(x\) -axis corresponds to the first eigenvector \((\overline{\nu})\) ; the y-axis corresponds to the second eigenvector \((\overline{\nu})\) . Not all stimuli generated a response in the neuron. Shown in black are the total applied stimuli, \(\mathbf{S}_{\mathrm{T}}\) , which are overlaid by stimuli \(\mathbf{S}_{\mathrm{D}}\) (white crosses). Also shown are the projections of the electrical receptive fields, \(\overline{\mathbf{w}}^{+}\) (large diamond) and \(\overline{\mathbf{w}}^{-}\) (large circle). </center>

doi:10.1371/journal.pcbi.1004849. g003

describing the intrinsic nonlinear firing properties of neurons. Using STC analysis, we derived the lower dimension stimulation subspace that led to a short- latency response in the neuron. By projecting the raw and spike- triggered stimuli onto the lower dimension subspace, we estimated the intrinsic nonlinearity. The probability of generating a spike, given stimulus \(\overline{S_{i}^{*}}\) , was estimated as

\[P(R = \mathrm{spike}|\overline{S_{i}^{*}}) = \mathcal{N}_{N}(\overline{\nu}_{1}\cdot \overline{S_{i}^{*}},\overline{\nu}_{2}\cdot \overline{S_{i}^{*}},\ldots ,\overline{\nu}_{N}\cdot \overline{S_{i}^{*}}), \quad (2)\]

where \(\mathcal{N}\) represents the static nonlinear function operating on arguments in \(\mu \mathrm{A}\) and \(\overline{\nu}_{i}\) \((i = 1,2,\ldots ,N)\) represent the \(N\) significant principal components. To find \(\overline{\nu}_{i}\) \((i = 1,2,\ldots ,N)\) , the stimulus data were first separated into a matrix containing only stimuli generating a short- latency response, \(\mathbf{S}_{\mathrm{D}}\) , and a matrix containing all stimuli, \(\mathbf{S}_{\mathrm{T}}\) (Fig 3A). We found the low- dimensional linear subspace that best captured the difference between the spike- triggered stimuli and the raw ensemble by performing principal component analysis (PCA) on the covariance matrix of the spike- triggered ensemble,

\[C_{s} = cov(\mathbf{S}_{\mathrm{D}}), \quad (3)\]

and comparing it to the variance of the raw ensemble which was approximately \(\sigma^{2}\) in all stimulus directions due to the Gaussian nature of \(\mathbf{S}_{\mathrm{T}}\) . PCA on \(C_{s}\) produce a set of eigenvectors giving a rotated set of axes in stimulus space and a corresponding set of eigenvalues giving the variance of the spike- triggered ensemble along each of the axes. Eigenvalues that are greater than the variance of the input stimuli reveal the directions where the spike- triggered stimuli have experienced an increase in variance from the raw ensemble. Similarly, eigenvectors that are smaller than the variance of the input stimuli reveal directions where the spike- triggered stimuli have experienced a decrease in variance from the raw ensemble. The eigenvalues that are sufficiently different from the raw ensemble correspond to eigenvectors \((\overline{\nu}_{i}, i = 1,2,\ldots ,N)\) pointing in directions in the stimulus space that carry information about the spiking probability of the neuron.

To test if the neural response could be accurately characterized by a one- dimensional model, we examined how many eigenvalues resulting from PCA were significantly different to chance [20]. We compared the eigenvalues obtained by PCA on spike- triggering stimuli to a distribution of eigenvalues for a randomly chosen ensemble of stimuli. This was done by randomly time- shifting the spike train and performing PCA on the corresponding randomized spike- triggered stimuli to recover a new set of eigenvalues. By repeating these 1000 times, we construct a distribution of eigenvalues and set a confidence criterion outside of which we presumed the magnitude of the true eigenvalues to be significant. The confidence criterion used was two standard deviations, or a \(95\%\) confidence interval. If the greatest or least eigenvalue fell outside these bounds, we rejected the null hypothesis that the spike- triggered ensemble was not significantly different to the full ensemble. We then projected out the axis corresponding to this eigenvalue from the raw data. We repeated the test until all remaining eigenvalues fell within the bounds of the null distribution, suggesting that the remaining eigenvalues were insignificant in affecting the variance of the neuron. Components having an eigenvalue significantly greater than the variance of the randomly time- shifted ensemble were considered to be components that generate an excitatory response on the cell. Conversely, components that are significantly smaller than the variance of the raw ensemble were considered to be components that suppressed the cell's response.

For the majority of cells, we found that a simplification to one- dimension \((\overrightarrow{\nu}_{1})\) accurately captured the spike- triggering information, thereby reducing the equation to one dimension. Using this simplification, Eq (2) becomes

\[P(R = \mathrm{spike}|\overrightarrow{S_{i}}) = \mathcal{N}_{1}(\overrightarrow{\nu}_{1}\cdot \overrightarrow{S_{i}}). \quad (4)\]

Results in the literature indicate that response thresholds to electrical stimulation for some cell types might differ depending on pulse polarity [37]. To explore difference in response to pulse polarity, we allowed the probability to be described by two different nonlinear functions and we found the electrical receptive fields (ERFs) for stimuli having a net effect that was either cathodic- first or anodic- first. Eq (4) then becomes

\[P(R = \mathrm{spike}|\overrightarrow{S_{i}}) = \mathcal{N}^{+}(\overrightarrow{w}^{+}\cdot \overrightarrow{S_{i}}) + \mathcal{N}^{-}(\overrightarrow{w}^{-}\cdot \overrightarrow{S_{i}}) + c\mathbf{R}_{s}, \quad (5)\]

where \(\mathcal{N}^{+}\) and \(\mathcal{N}^{- }\) represent static nonlinear functions and \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) represent the ERFs for stimuli with positive projections \((\overrightarrow{\nu}_{1}\cdot \overrightarrow{S_{i}} >0\) , net anodic- first) and negative \((\overrightarrow{\nu}_{1}\cdot \overrightarrow{S_{i}} < 0\) net cathodic- first), respectively. \(\mathbf{R}_{s}\) represents the spontaneous firing rate in Hz and \(c\) represents a scaling factor of units \(\mathrm{Hz}^{- 1}\) . To find the nonlinearities and the ERFs, the first principal component \((\overrightarrow{\nu}_{1})\) was used to divide the stimulus space into positive and negative regions by projecting all stimuli of \(\mathbf{S}_{\mathrm{D}}\) and \(\mathbf{S}_{\mathrm{T}}\) onto the first principal component (Fig 3B). Positive and negative regions were defined by the stimuli having either a positive or negative projection onto the first principal component. This produced two spike- triggered stimulus matrices, \(\mathbf{S}_{\mathrm{D}}^{+}\) and \(\mathbf{S}_{\mathrm{D}}^{*}\) . The means of the matrices are analogous to the spike- triggered average for net anodic- first and net cathodic- first stimuli [16], and provide an estimate of the ERFs, \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) , respectively. Fig 3B shows an example of the stimuli projected onto the first two principal components and the ERFs, \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) . After the stimuli were separated into two regions, the nonlinear functions, \(\mathcal{N}^{+}\) and \(\mathcal{N}^{- }\) , were recovered by projecting all stimuli onto the normalized vectors \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) and segmenting the projected stimuli into 30 bins (15 for the net anodic- first and 15 for the net cathodic- first regions) such that each bin contained an equal number of spikes. By comparing the number of spike- eliciting stimuli to the total number of stimuli in each bin, an estimate of the spike probability was generated. The nonlinear function from Eq

(5) was then fit to the data, with the following equations for the sigmoidal curves:

\[\mathcal{N}^{+}(x_{+}) = \frac{a_{+}}{1 + \exp(-b_{+}(x_{+} - c_{+}))} \quad (6)\]

\[\mathcal{N}^{-}(x_{-}) = a_{-} - \frac{a_{-}}{1 + \exp(-b_{-}(x_{-} - c_{-}))}, \quad (7)\]

where \(x_{+} = \overrightarrow{w}^{+}\cdot \overrightarrow{S}_{i}^{+}\) and \(x_{- } = \overrightarrow{w}^{- }\cdot \overrightarrow{S}_{i}^{+}\) . Coefficients \(a_{+}\) and \(a_{- }\) represent scaling factors that determine the saturation amplitudes, \(b_{+}\) and \(b_{- }\) represent the gain of the sigmoidal curves, and \(c_{+}\) and \(c_{- }\) represent the thresholds ( \(50\%\) of the saturation level) for the net anodic-first and net cathodic-first stimulation, respectively. Note that the vectors \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) might not necessarily be parallel to each other, nor parallel to \(\overrightarrow{v}_{1}\) . This may result in electrodes that differentially influence the neuron's response to anodic-first or cathodic-first stimulation.

To test the similarity between the positive and negative ERFs, we calculated the correlation coefficient between them. A correlation coefficient close to - 1 indicated that the two ERFs are approximately equal in magnitude but opposite in sign, and therefore the cell was equally influenced by the same combination of electrodes. A value closer to 0 indicates that the two ERFs have no correlation, and therefore the cell is not influenced by the same electrodes. Positive correlation coefficients were not expected and did not occur. The spatial extent over which a cell was influenced by electrical stimulation was estimated by computing a weighted mean of the distance between the cell and the electrodes. The distance between the cell and each electrode center was weighted by the electrode's influence on the cell as given by the ERFs. The weighted mean for both ERFs was given by,

\[D^{+} = \frac{\sum_{i = 1}^{20}w_{i}^{+}d_{i}}{\sum_{i = 1}^{20}w_{i}^{+}} \quad (8)\]

\[D^{-} = \frac{\sum_{i = 1}^{20}w_{i}^{-}d_{i}}{\sum_{i = 1}^{20}w_{i}^{-}} \quad (9)\]

where \(w_{i}^{+}\) and \(w_{i}^{- }\) are the weights given by \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) respectively, and \(d_{i}\) is the distance between the cell and electrode \(i\)

To test which electrodes significantly affected the cell's response, \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) were recalculated 1000 times by projecting the data onto the first eigenvector of the randomly time- shifted distribution of eigenvectors from the significance test. A distribution for \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) was constructed from which the true \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) could be compared. Electrodes from the true \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) were compared to the root mean square (RMS) of the distribution and electrodes that were larger than the RMS bounds were considered significant.

For cells where more than one significant principal component was obtained from the significance test, we compared the variance explained by the first principal component to that of the next most significant component. This was done by comparing the separation of the first eigenvalue \(e_{1}\) from the mean of the randomized distribution of eigenvalues \((\bar{e}_{\mathrm{md}})\) with the separation between the next most significant eigenvalue \((e_{2})\) and the same mean. The strength was defined as

\[G = \frac{|e_{1} - \bar{e}_{\mathrm{md}}|}{|e_{2} - \bar{e}_{\mathrm{md}}|}, \quad (10)\]

and gives a relative measure of how much larger \(e_1\) is compared to the next most significant eigenvalue. \(\bar{e}_{\mathrm{md}}\) was calculated from the first iteration of the hypothesis test.

## Model validation

For each cell, \(80\%\) of the data were used to fit the model parameters, while the remaining data were used to validate the model. To obtain a quantitative estimate of the performance of the model, the probability of response given a stimulus was calculated from the validation data and compared to the model prediction. The validation stimuli were assigned 1 if they produced a direct response and 0 otherwise. Each stimulus was also assigned a predicted probability using the model (Eq (5)) recovered from the training data. The stimuli were then binned into segments in the range of 0 to 1 depending on their predicted probability and an actual probability for each bin was calculated by the fraction of stimuli assigned a 1. The mean square error \((E^{\mathrm{MS}})\) was then calculated,

\[E^{\mathrm{MS}} = \frac{1}{B}\sum_{i = 1}^{B}(\hat{P}_{i} - P_{i})^{2}, \quad (11)\]

where \(B\) is the number of bins, \(\hat{P}_i\) is the predicted probability, and \(P_i\) is the calculated probability from the data for a particular bin. For all cells, \(B\) was equal to 10. The root mean square error \((E^{\mathrm{RMS}})\) of the model, given by

\[E^{\mathrm{RMS}} = \sqrt{E^{\mathrm{MS}}}, \quad (12)\]

was used as a quantitative measure of the model accuracy.

We also compared the error of a one- dimensional model to that of a two- dimensional model. The two- dimensional spike probability was estimated by

\[P(R = \mathrm{spike}|\vec{S_i}) = \mathcal{N}_2(\vec{\nu}_1\cdot \vec{S_i},\vec{\nu}_2\cdot \vec{S_i}), \quad (13)\]

where \(\vec{\nu}_2\) represented the next most significant component, either the second (excitatory) or last (suppressive) principal component. To find the two- dimensional nonlinearity \((\mathcal{N}_2)\) , a surface was fit to the spike- triggered data projected onto these two most significant components. The surface fit was obtained using a cubic spline interpolation on MATLAB's curve fitting toolbox. Once the surface was fit, the validation data was used to calculate the mean model error calculated using Eqs (11) and (12).

## Results

## Stimulation

Intracellular recordings lasting up to 4 hours were obtained from 25 cells. This population included 7 ON, 13 OFF, 3 ON- OFF, and 2 cells where 3- D morphological reconstructions were not possible. Our comparison of histological and physiological results were consistent with those of Huxlin and Goodchild [29]: ON center cells stratify in the inner IPL (40- 100% depth), while OFF center cells stratify in the outer IPL (0- 40% depth). ON- OFF types stratify in both the inner and outer layers of the IPL. Fig 4 shows an example of an ON- OFF RGC with dendrites stratifying in both inner and outer layers of the IPL. A summary of the stratification depths for the ON, OFF, and ON- OFF cells are given in Table 1.

To fit the model parameters, cells were simultaneously stimulated with biphasic pulses on all electrodes, where the amplitude of the pulses were randomly chosen from a Gaussian distribution of zero mean and standard deviation \(\sigma\) (here after white noise stimuli). To determine an appropriate value of \(\sigma\) for each cell, three short stimulus trains (approximately 3 min each) of

> **Image description.** A composite scientific figure consisting of two panels, (a) and (b), presenting microscopic views of retinal ganglion cells (RGCs) and their surrounding tissue.
>
> Panel (a) is a stained micrograph showing a single RGC and its dendritic field. The background tissue is stained red, while the cell body (soma) is a bright green, and its radiating dendrites are also stained green. The dendrites extend outwards from the central soma, filling a large area. Two geometric overlays are visible: a thin white rectangular bounding box that encompasses the entire dendritic field, and a thick blue ellipse fitted within this box, used to estimate the overall size of the dendritic field. A scale bar labeled "100 μm" is located in the bottom right corner of this panel.
>
> Panel (b) is a cross-sectional view of the retinal tissue, illustrating the layered structure. The image shows distinct horizontal layers, with signals in red and green. Key structural elements are marked with labels and lines:
> *   The top and bottom boundaries of the Inner Plexiform Layer (IPL) are indicated by solid horizontal lines labeled "IPL."
> *   A dashed horizontal line running through the center of the IPL is labeled "ON/OFF border," separating the ON and OFF layers.
> *   A scale bar labeled "100 μm" is present in the bottom left corner of this panel.
>
> Overall, the figure uses fluorescent staining and geometric overlays to visualize the morphology and stratification of retinal ganglion cells, specifically analyzing the extent of their dendritic fields (Panel a) and the depth at which their dendrites are organized within the IPL (Panel b).

<center>Fig 4. ON-OFF retinal ganglion cell. (a) A stained image of a RGC from which dendritic stratification and dendritic field size can be analyzed. The bounding box (thin white line) shows the region encompassing the dendritic field of the cell. An ellipse was fit to this region (thick blue line) to estimate the dendritic field size. The major axis of the elliptical fit for this cell was 508 μm. (b) Dendritic stratification for this cell is in two distinct layers of the inner-plexiform layer (IPL). Dendrites in the ON sublaminar of the IPL stratify at an average depth of 66.9%, while the OFF dendrites stratify at an average depth of 27.2%. The solid horizontal lines represent the edge of the IPL. The dashed line represents the approximate ON/OFF border; the region above the dashed line is the ON layer, the region below is the OFF layer. </center>

Table 1. Summary of results.

| | Mean | Standard deviation | Min | Max |
| :--- | :--- | :--- | :--- | :--- |
| ON (depth %) | 57.1 | 6.6 | 49.2 | 69.6 |
| OFF (depth %) | 24.1 | 9.7 | 11.0 | 37.6 |
| ON-OFF (inner) (depth %) | 63.8 | 0.16 | 57.7 | 66.9 |
| ON-OFF (outer) (depth %) | 20.8 | 7.7 | 16.3 | 27.2 |
| Negative threshold (c.) | -233 | 124 | -39 | -469 |
| Positive threshold (c.) | 235 | 136 | 59 | 416 |
| Average model RMSE | 0.064 | 0.027 | 0.028 | 0.117 |
| Mean latency for SL responses (ms) (N = 20) | 1.75 | 10.5 | 0.5 | 4.35 |
| Mean latency for LL responses (ms) (N = 17) | 11 | 2.59 | 4.2 | 20.27 |
| 1-dimensional nonlinear fit coefficient (r²) | 0.92 | 0.04 | 0.83 | 0.99 |

doi:10.1371/journal.pcbi.1004849. t001

> **Image description.** A two-panel scientific figure, labeled "Fig 5. White noise stimulation amplitudes," consisting of two line graphs (a and b) that illustrate the relationship between stimulation amplitude and spike probability for two different cells.
>
> **Panel (a): Spike Probability vs. Amplitude**
> This panel is a line graph showing the "Spike probability" on the vertical Y-axis (ranging from 0 to 1) against the "Amplitude ($\mu$A)" on the horizontal X-axis (ranging from 0 to 250, marked in increments of 50).
> *   **Data Series:** Two distinct curves are plotted: a solid black line labeled "Cell 1" and a dashed black line labeled "Cell 2."
> *   **Visual Trend:** Both curves exhibit a sigmoidal (S-shaped) increase, indicating that spike probability increases as the stimulation amplitude increases.
> *   **Comparison:** The solid line (Cell 1) reaches a higher maximum spike probability, approaching 1.0, while the dashed line (Cell 2) plateaus at a lower maximum probability, approximately 0.6.
> *   **Error Bars:** Vertical error bars are visible on both curves, representing the standard deviation from the mean at various amplitude points.
>
> **Panel (b): Probability Density Functions**
> This panel is a line graph showing "Probability" on the vertical Y-axis (scaled in units of $10^{-3}$, ranging from 0 to $5 \times 10^{-3}$) against the "Amplitude ($\mu$A)" on the horizontal X-axis (ranging from -300 to 300, marked in increments of 100).
> *   **Data Series:** Two bell-shaped curves, representing Gaussian distributions derived from the $\sigma$ values found in Panel (a), are plotted.
> *   **Visual Pattern:** Both curves are centered near 0 $\mu$A and are truncated at the $\pm 300 \mu$A limits of the X-axis.
> *   **Comparison:** The dashed curve (corresponding to Cell 2) is slightly wider and flatter than the solid curve (corresponding to Cell 1), suggesting a broader distribution of stimulation amplitudes for Cell 2. The solid curve appears slightly narrower and taller.
>
> The overall figure uses these graphs to demonstrate how the response characteristics (spike probability and distribution of effective stimulation amplitudes) differ between Cell 1 and Cell 2 under white noise stimulation.

<center>Fig 5. White noise stimulation amplitudes. (a) The increase in spike probability with increasing amplitude of the standard deviation of the white noise for two cells. To avoid over stimulation of recorded cells, white noise stimulation with a standard deviation \((\sigma)\) was initially applied to each cell. The value of \(\sigma\) corresponding to half the maximal spike probability was used as the standard deviation of white noise stimulation for the experiment. Cell 1 reached a maximum value close to 1. The value of \(\sigma\) corresponding to a 0.5 spike probability was \(85 \mu \mathrm{A}\) . Cell 2 reached a maximal value close to 0.6. The value of \(\sigma\) corresponding to a spike probability of 0.3 was \(145 \mu \mathrm{A}\) . Error bars refer to the standard deviation from the mean. (b) The \(\sigma\) values from (a) were used to generate Gaussian distributions from which stimulation amplitudes on each electrode were sampled. Stimulus amplitudes were limited to \(\pm 300 \mu \mathrm{A}\) , hence the distribution is truncated at these values. doi:10.1371/journal.pcbi.1004849. g005 </center>

doi:10.1371/journal.pcbi.1004849. g005

white noise stimuli with different \(\sigma\) were initially presented to the cell ( \(\sigma\) varied from 50–250 \(\mu \mathrm{A}\) in steps of \(50 \mu \mathrm{A}\) ). The number of times the cell responded within 5 ms was used to obtain a response probability. Each cell responded with a different maximum response probability when stimulated with white noise at the highest value of \(\sigma\) ; some cells could respond with a spike probability close to one, while others only responded with a spike probability less than one. However, cells that responded to fewer pulses tended to show an increased level of long- latency activity \((>5 \mathrm{ms})\) , most likely due to intensified network activation. The value of \(\sigma\) used for white noise stimulation for each cell in the rest of the experiment was the value corresponding to half the saturation level.

Fig 5 shows examples of two cells with different \(\sigma\) values. Cell 2 responded with a spike probability close to one even at low \(\sigma\) values while cell 1 responded maximally with a spike probability of around 0.6 (Fig 5A). The value of \(\sigma\) used for white noise stimulation for cell 1 was \(85 \mu \mathrm{A}\) and for cell 2 was \(145 \mu \mathrm{A}\) . Note that we used this method to calibrate our experiments and the nonlinear curves do not show the maximum probability of firing, as each point is an average over a variety of stimulus amplitudes. Following this calibration, longer trains of white noise stimulation (approximately 2 minutes each) with the corresponding value of \(\sigma\) for each cell were used to obtain data for recovering the model parameters. The corresponding Gaussian distributions for cells 1 and 2 are shown in Fig 5B. The experiment for each cell lasted approximately 3–4 hours.

Stimulation artefacts were present in the recordings that could be removed by blanking without affecting the ability to detect the cells' spikes. Fig 6A shows examples of some of the spiking patterns observed during experiments: (i) a failed anodic- first stimulus, (ii) a successful short- latency anodic- first stimulus, (iii) a successful short- latency cathodic- first stimulus, and (iv) a successful long- latency cathodic- first stimulus. The top panel in each subplot shows the raw recording and the bottom panels show the same signals with the artefact removed by blanking. Also shown in the bottom panels are the thresholds used to detect spikes (horizontal lines). These figures show that spikes could be easily identified without interference from the stimulus artefact.

The spike latencies after a stimulus pulse were analyzed for each cell. Some cells produced a bimodal distribution attributed to the short- and long- latency responses \(\mathrm{(N = 13)}\) , with four cells showing overlapping distributions for the two latencies. The remaining cells only produced short- latency spikes that were close to the timing of the stimulus pulse \(\mathrm{(N = 8)}\) . Fig 6B depicts the spike latencies for all cells. The average short- latency cluster mean for all cells was \(1.75\mathrm{ms}\) from stimulus offset (SD 1 ms). The longest short- latency cluster for a cell had a mean of \(4.35\mathrm{ms}\) (SD 1.37 ms). Fig 6C and 6D show the distributions of spike latencies for two sample cells, along with fitted Gaussian distributions obtained from the cluster analyses. Fig 6C shows a cell with two distinct clusters, with a short- latency cluster mean at \(1.95\mathrm{ms}\) . Fig 6D shows two overlapped clusters with the short- latency cluster mean at \(4.35\mathrm{ms}\) .

## Model estimation

Our aim was to find a mathematical description that could accurately capture the response probability of neurons to concurrent stimulation using a MEA. To do this we first performed a

> **Image description.** This image is a composite scientific figure (Figure 6) titled "Spike detection and spike latency analysis," presenting four panels (a, b, c, and d) that illustrate neuronal membrane potentials and the statistical analysis of spike latencies.
>
> **Panel (a): Membrane Potentials**
> This panel displays four sub-traces (i, ii, iii, and iv) representing membrane potentials over time.
> *   **Axes:** The vertical axis is labeled "100 mV" (voltage), and the horizontal axis is labeled "5 ms" (time).
> *   **Content:** Each trace shows a baseline (represented by a red horizontal line) and the resulting electrical response.
>     *   Trace (i) shows a failed response.
>     *   Traces (ii), (iii), and (iv) show successful responses characterized by sharp, upward deflections (action potentials or spikes) occurring shortly after the stimulus.
> *   **Interpretation:** These traces illustrate the neuron's response to four different stimulus types, including successful short-latency and long-latency responses.
>
> **Panel (b): Latency Scatter Plot**
> This panel is a scatter plot showing the relationship between short and long spike latencies across various cells.
> *   **Axes:** The X-axis is labeled "Short latency" (ranging from 1 to 5), and the Y-axis is labeled "Long latency" (ranging from 0 to 25).
> *   **Data Points and Legend:** Various data points are plotted and categorized by condition:
>     *   "OFF" (Black circles)
>     *   "ON" (White circles)
>     *   "ON/OFF" (Black squares)
>     *   "N/A" (White squares)
>     *   "Mean" (Black 'x')
> *   **Visual Elements:** The data points generally trend upward, suggesting a positive correlation between short and long latency. Horizontal lines indicate the standard error of the short latency clusters, and vertical lines indicate the standard error for the long latency clusters.
>
> **Panel (c): Spike Latency Distribution (Cell 1)**
> This panel is a histogram showing the distribution of spike latencies for a specific cell.
> *   **Axes:** The X-axis is labeled "Time (ms)" (ranging from 0 to 20), and the Y-axis is labeled "Spike count" (ranging from 0 to 3000).
> *   **Content:** The histogram displays a distribution that is clearly bimodal, meaning it has two distinct peaks, representing two separate clusters of spike times. A smooth, fitted Gaussian curve is overlaid on the histogram, representing the cluster analysis.
>
> **Panel (d): Spike Latency Distribution (Cell 2)**
> This panel is a histogram showing the distribution of spike latencies for a second specific cell.
> *   **Axes:** The X-axis is labeled "Time (ms)" (ranging from 0 to 20), and the Y-axis is labeled "Spike count" (ranging from 0 to 1200).
> *   **Content:** The histogram shows a distribution where the two potential clusters are more overlapped compared to Panel (c). A smooth, fitted Gaussian curve is overlaid on the histogram.
>
> **Figure Caption Text:**
> The caption below the panels reads: "Fig 6. Spike detection and spike latency analysis. (a) Membrane potentials showing the response to four stimulus types; (i) a failed anodic first stimulus, (ii) a successful anodic first stimulus with a short-latency response, (iii) a successful cathodic first stimulus with a short-latency response and (iv) a successful cathodic first stimulus with a long-latency response. Bottom traces in each panel show the stimulus artefact removed by setting the artefact to a constant value, and the threshold used to detect spikes (horizontal line at zero). (b) Short and long spike latencies for all cells. Horizontal lines show the standard error of the short latency clusters. Vertical lines show the standard error for the long latency clusters. Note that for many of the..." (The caption is truncated).

<center>Fig 6. Spike detection and spike latency analysis. (a) Membrane potentials showing the response to four stimulus types; (i) a failed anodic first stimulus, (ii) a successful anodic first stimulus with a short-latency response, (iii) a successful cathodic first stimulus with a short-latency response and (iv) a successful cathodic first stimulus with a long-latency response. Bottom traces in each panel show the stimulus artefact removed by setting the artefact to a constant value, and the threshold used to detect spikes (horizontal line at zero). (b) Short and long spike latencies for all cells. Horizontal lines show the standard error of the short latency clusters. Vertical lines show the standard error for the long latency clusters. Note that for many of the cells, the standard errors are very small. The dashed line shows the line of equality. Eight cells did not produce a long latency component, and hence lie below the dashed line. The \(\times\) symbol shows the mean of all short and long latencies. (c) Distribution of spike latencies for a sample cell. A k-means cluster analysis (2 clusters) on the spike latencies gives the two distributions shown by the Gaussian distribution. This cell had a short-latency distribution mean of \(1.95\mathrm{ms}\) (SD 0.54 ms). The long-latency distribution mean is \(5.03\mathrm{ms}\) (SD 2.58 ms). (d) Distribution of spike latencies for another sample cell. A k-means cluster analysis (2 clusters) on the spike latencies gives the two distributions shown by the Gaussian distribution. This cell had a short-latency mean of \(4.35\mathrm{ms}\) (SD 1.37 ms). The long-latency distribution mean is \(12.87\mathrm{ms}\) (SD 2.58 ms). </center>

principal components analysis on the ensemble of stimuli that triggered a short latency spike. For all cells we found that the neural response could be well predicted by projection onto a subspace spanned by the first principal component, \(\overrightarrow{\nu}_{1}\) . The variance explained by \(\overrightarrow{\nu}_{1}\) was significantly higher than that of next greatest component, \(\overrightarrow{\nu}_{2}\) , suggesting that the spiking information was well captured by \(\overrightarrow{\nu}_{1}\) .

Fig 7A shows the spike- triggered probabilities projected onto \(\overrightarrow{\nu}_{1}\) and \(\overrightarrow{\nu}_{2}\) from the sample cell in Fig 3B. The histograms show the number of stimuli (gray) and responses (black) along each axis; the ratio of the bars of the two histograms is used to determine the spike probabilities along each axis. From the histograms, it is clear that the distribution of the spike- triggered stimuli was bimodal in the \(\overrightarrow{\nu}_{1}\) axis; however, it remained unimodal along \(\overrightarrow{\nu}_{2}\) , similar to Gaussian distribution of the full stimulus ensemble.

A statistical hypothesis test was used to determine how many eigenvalues recovered by PCA revealed a significant amount of the spike- eliciting information. The test compares the eigenvalues recovered from the data, to a set of eigenvalues produced by randomly time- shifting the spike train and performing PCA on the new set of stimuli. From the set of time- shifted eigenvalues, a \(95\%\) confidence limit was set to determine which eigenvalues from the original spike- triggered data lie outside of the limits. Fig 7B illustrates an example of the hypothesis test. For the sample cell, the test revealed that a large amount of information was contained in the first component, which was excitatory ( \(\overrightarrow{\nu}_{1}\) , eigenvalue above the confidence interval, long red arrow in Fig 7B). A second suppressive component was also significant, but contained a very small amount of information (the last component, eigenvalue below the confidence interval, short red arrow in Fig 7B). The shaded region shows the \(95\%\) confidence intervals from the hypothesis test. The circles represent the eigenvalues obtained from PCA on the spike- eliciting data. After two iterations of the hypothesis test, all eigenvalues were within the \(95\%\) confidence intervals. The arrows shown in the figure represent the separation between the mean of the randomly time- shifted distribution of eigenvalues and the raw eigenvalues ( \(|e_{1} - \bar{e}_{\mathrm{mol}}|\) and \(|e_{2} - \bar{e}_{\mathrm{mol}}|\) in Eq (10)). For this cell, \(|e_{1} - \bar{e}_{\mathrm{mol}}|\) was approximately 12 times greater than \(|e_{2} - \bar{e}_{\mathrm{mol}}|\) ( \(G = 12\) ). Note that for this experiment, electrode 12 was not operational and hence only 19 components were produced.

The bimodal distribution of response probability along the axis of the first principal component indicates that this neuron responded to two categories of multi- electrode stimulation; one category that produced a positive projection onto this axis, and one with a negative projection onto this axis. For all cells, stimuli with a positive projection onto the axis produced a stimulus at the cell's location whose net effect was anodic- first, regardless of the fact that some electrodes may have been stimulated with cathodic- first pulses. The opposite was true for the negative projection. We therefore wondered if there may be differences in the one- dimensional stimulus subspace to which the cell responded, between net anodic- first and net cathodic- first stimulation. If so, the PCA analysis would only find the average direction of these two one- dimensional subspaces. To address this we used the PCA initial estimate of the subspace to break the stimulus space up into positive and negative regions determined by whether the stimuli had a positive or negative projection onto \(\overrightarrow{\nu}_{1}\) . By separating the data into the two regions, two electrical receptive fields (ERFs), \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) , corresponding to net anodic- first and net cathodic- first stimuli, were estimated (Fig 3B). The ratio of spike- eliciting stimuli to total stimuli was then used to determine a spike probability.

Fig 7C illustrates the spike probability for the sample cell. The raw data was projected onto \(\overrightarrow{w}^{+}\) and \(\overrightarrow{w}^{- }\) ( \(\times\) ) and the nonlinear curve from Eq (5) (solid line) was fit to the data. All cells obtained high \(r^{2}\) (coefficient of determination) values for the nonlinear fit; the average \(r^{2}\) for all

> **Image description.** This image is a complex, multi-panel scientific figure (Figure 7) detailing the recovery of model parameters for a sample cell, consisting of five distinct panels (a through e).
>
> **Panel (a): Principal Component Analysis (PCA) Visualization**
> This panel features a large square matrix (heatmap) representing spike probability. The axes are labeled "Principal Component 1" and "Principal Component 2." The matrix is filled with shades of gray, where black indicates a spike probability of 0 and white indicates a probability of 1. Above and to the right of this matrix are two histograms: one labeled "Stimuli" (gray) and the other "Spike-triggered stimuli" (black), showing the distribution of data along each principal component axis.
>
> **Panel (b): Eigenvalue Analysis**
> This is a line graph plotting "Normalized variance" on the y-axis against "Component number" on the x-axis (ranging from 1 to 20). The data points, represented by round circles, show a sharp decrease in variance from Component 1 to Component 2, followed by a gradual decline. A shaded region represents the 95% confidence interval. Red arrows are drawn, indicating the distance ($d_1$ and $d_2$) between the two most significant eigenvalues and the mean of a random distribution.
>
> **Panel (c): Spike Probability Function**
> This panel is a line graph showing "Spike probability" on the y-axis versus "Amplitude ($\mu$A)" on the x-axis (ranging from -500 to 500). Open circles represent the raw data points. A solid black line is fitted to the data, illustrating a double sigmoid function. The fit is noted to have an $r^2$ value of 0.98.
>
> **Panel (d): Electrode Amplitude Comparison**
> This line graph plots "Normalized amplitude" on the y-axis against "Electrode number" on the x-axis (ranging from 1 to 20). A solid black line represents the true $\bar{\nu}^{+}$ and $\bar{\nu}^{-}$, while a gray shaded area represents the root mean square (RMS) of a distribution of these values. Asterisks (*) are placed above certain electrodes to indicate significance. A note specifies that electrode 12 was not operational.
>
> **Panel (e): Electrode Representation**
> This panel is a schematic diagram showing two circular arrangements of electrodes, representing $\bar{\nu}^{+}$ (left) and $\bar{\nu}^{-}$ (right). Both arrangements consist of numerous small blue circles (electrodes). In the left arrangement ($\bar{\nu}^{+}$), one large red circle (labeled 9) is highlighted. In the right arrangement ($\bar{\nu}^{-}$), one large green circle (labeled 9) is highlighted. A scale bar is provided at the bottom right, indicating distances of 1 mm and 5 mm.

<center>Fig 7. Recovery of model parameters for a sample cell. (a) The stimuli are projected onto the first two principal components, \(\nu_{1}^{+}\) and \(\nu_{2}^{+}\) . The grey squares represent the spike probability, where a black value represents 0 probability, and a white value represents a probability of 1. Plotted above and to the right are the histograms of the stimuli (gray) and the spike-triggered stimuli (black) along each component axis. (b) Eigenvalues of the spike-triggered stimuli recovered by principal component analysis (round circles) are plotted. The eigenvalues are normalized by the variance of the input stimuli. The shaded region represents the \(95\%\) confidence interval from the statistical hypothesis test. The hypothesis test recovered one significant excitatory and one significant suppressive component. The red arrows show the distance between the two most significant eigenvalues and the mean of the random distribution recovered from the first iteration of the hypothesis test. The length of the arrows represent \(d_{1}\) and \(d_{2}\) from Eq (10). (c) The nonlinear function recovered by fitting a double sigmoid to the spike probability projected onto \(\bar{\nu}^{+}\) and \(\bar{\nu}^{-}\) . Open circles represent the raw data and the solid line shows the nonlinear equation fit \((r^{2} = 0.98)\) . This cell had a positive and negative threshold (parameters \(c_{+}\) and \(c_{-}\) in Eq (5)) of \(129\mu \mathrm{A}\) and \(-152\mu \mathrm{A}\) proportional to \(\bar{\nu}^{+}\) and \(\bar{\nu}^{-}\) , respectively. (d) The true \(\bar{\nu}^{+}\) and \(\bar{\nu}^{-}\) (solid black) are compared to the root mean square (dashed line) of a distribution of \(\bar{\nu}^{+}\) and \(\bar{\nu}^{-}\) (gray). Stars show which electrodes were significant. In this preparation, electrode 12 was not operational. (e) Representation of the amplitudes that generate the ERFs, \(\bar{\nu}^{+}\) (left) and \(\bar{\nu}^{-}\) (right). The large circles represent the electrode locations. A correlation coefficient of -0.97 was obtained between \(\bar{\nu}^{+}\) and \(\bar{\nu}^{-}\) . Three electrodes significantly affected the cell in \(\bar{\nu}^{+}\) and \(\bar{\nu}^{-}\) . In this experiment, the retina was placed such that the optic disc was located around electrode 9. The stimulation return electrode was placed distally above electrode 12. The green circle shows the approximate dendritic field of the recorded cell. Stimulus amplitudes ranged up to \(\pm 300\mu \mathrm{A}\) ; however, the range shown here is smaller to make the differences in electrode amplitudes clearer. </center>

cells was 0.92 (SD 0.04) (see Table 1 for summary). This suggests that a double sigmoidal curve is appropriate to describe the nonlinear firing probabilities of RGCs to electrical stimulation.

Significant electrodes in \(\overline{w}^{+}\) and \(\overline{w}^{- }\) were determined by comparing the electrodes to a distribution of \(\overline{w}^{+}\) and \(\overline{w}^{- }\) generated in the significance test. Fig 7D shows the true \(\overline{w}^{+}\) (solid black line) compared to the RMS of the distribution (dashed line). Up to three electrodes significantly affected this cell. To visualize the cell's ERF, the electrode amplitudes that generated \(\overline{w}^{+}\) and \(\overline{w}^{- }\) were plotted. Fig 7E depicts ERFs for the sample cell; the green dot shows the approximate location of the recorded cell soma. The filled circles represent the stimulus amplitudes on the electrode that generate \(\overline{w}^{+}\) and \(\overline{w}^{- }\) . Only significant electrodes are colored. For all cells, \(\overline{w}^{+}\) produced a stimulus at the cell location that was anodic- first, while \(\overline{w}^{- }\) produced a stimulus at the cell location that was cathodic- first. In this example, the retina was oriented such that the optic disc was approximately above electrode 9. \(\overline{w}^{+}\) and \(\overline{w}^{- }\) for this cell had a correlation coefficient of - 0.91, indicating that the cell was influenced by the same set of electrodes when the stimulus was net anodic or net cathodic- first. An estimate of the size of the ERFs was determined by calculating a weighted mean of the distance between the cell and electrodes, where the distance was weighted by the ERFs. For this sample cell, \(D^{+}\) and \(D^{- }\) were approximately equal to \(1\mathrm{mm}\) , which is also the separation of the electrodes.

We investigated the relationship between dendritic receptive field and ERF by comparing the morphological reconstructions to the ERFs obtained from the model. Two sample cells are shown in Fig 8A and 8B. In these images, the morphological reconstruction has been superimposed onto a photograph showing the stimulating array and the patch pipette during recordings. Using the estimate of the dendritic receptive field size obtained from the morphological reconstruction, we plotted the ERFs along with the dendritic receptive fields for 21 cells (Fig 8C). Two cells where morphological reconstruction was possible were omitted due to uncertainty of the location of the cell relative to the array. The dendritic fields were estimated by a circle with a diameter equal to the major axis from the elliptical fit. The electrode colours represent the amplitude of \(\overline{w}^{+}\) and the stars represent the approximate location of the optic disc. One cell (Fig 8C21) was only affected by cathodic- first stimulation and hence \(\overline{w}^{- }\) is shown for this cell. This cell was affected by both anodic- and cathodic- first stimulation in its long- latency responses.

Data summarizing the model fit for the population of 25 cells is shown in Fig 9. The model nonlinear fit recovers an estimate of a cell's thresholds \((c_{+}\) and \(c_{- }\) in Eqs (6) and (7)). Most cells had similar threshold values for both their net anodic- first and net cathodic- first regions (see Table 1, Fig 9A), and no significant differences were found between or among ON, OFF or ON- OFF cell types (t- test, \(\mathrm{p} > 0.3\) ). The correlation coefficient of the ERFs, \(\overline{w}^{+}\) and \(\overline{w}^{- }\) , for the majority of cells was close to - 1 indicating that the cell was influenced by same electrodes for both net anodic- first and net cathodic- first stimulation (Fig 9B). Two OFF cells had a correlation coefficient greater than - 0.4 suggesting that the cell was differentially influenced by the electrodes depending on whether the stimulus was anodic- first or cathodic- first. The size of the positive ERF \((D^{+})\) was estimated for 23 cells and compared to the dendritic field size (Fig 9C). Cells were significantly influenced by only one (open circle), two (closed circle) or three (square) electrodes. The mean size of the ERFs produced by both \(\overline{w}^{+}\) and \(\overline{w}^{- }\) was approximately \(1.2\mathrm{mm}\) , and no significant difference was found between the size produced by \(\overline{w}^{+}\) and \(\overline{w}^{- }\) (t- test, \(\mathrm{p} > 0.4\) ).

The statistical hypothesis test showed that the spike- eliciting information was mostly contained in the first PCA component \((\overline{v}_{1}^{1})\) . For 17 cells, some information was also contained in up to two additional components; however this information was relatively small, as the effect

> **Image description.** This image, labeled Figure 8, is a composite technical figure illustrating the dendritic and electrical receptive fields of sample cells, combining high-magnification microscopy with schematic diagrams. The figure is divided into three main sections: panels (a) and (b) showing sample cells, and panel (c) showing electrical receptive field maps.
>
> **Panels (a) and (b): Sample Cell Visualization**
> Panels (a) and (b) are high-magnification microscopy images of biological tissue, likely retinal preparations. Both panels feature:
> *   **Stimulating Array:** A series of large, dark, circular structures running horizontally across the image, representing the stimulating array.
> *   **Dendritic Reconstruction:** A complex, light-colored, branching structure overlaid on the tissue, representing the morphological reconstruction of a sample cell's dendrites.
> *   **Recording Electrode:** A small white asterisk (*) is visible in both panels, indicating the approximate location of the patch-clamp recording electrode.
> *   **Labels and Scale:** Panel (a) is labeled "a" and "Electrode track," while panel (b) is labeled "b" and "Lycra thread." Both panels include a scale bar indicating "200 $\mu$m."
>
> **Panel (c): Electrical Receptive Field Maps**
> Panel (c) is a schematic grid displaying the electrical receptive fields for multiple cells.
> *   **Grid Structure:** The panel consists of a 4x6 grid, containing 24 individual plots, each numbered 1 through 24.
> *   **Plot Content:** Each plot shows a central area with surrounding colored circles, which represent the electrical response (pulse amplitude) across different electrode locations. A small white asterisk (*) is present in many plots, marking the approximate location of the optic disc.
> *   **Color Coding and Legend:** The color of the circles in the plots corresponds to the pulse amplitude, as defined by a color bar located to the right of the grid. The legend is titled "Pulse amplitude ($\mu$A)" and ranges from -200 $\mu$A (represented by dark blue) to 200 $\mu$A (represented by dark red), with 0 $\mu$A indicated by a white/light gray color.
>
> The overall figure provides a visual comparison between the physical location of the cells and recording equipment (a and b) and the resulting electrical response patterns across various electrode positions (c).

<center>Fig 8. Dendritic and electrical receptive fields. a-b) Sample cells depicting the stimulating array (large black discs) and the patch-clamp recording electrode (denoted by a \\*). Overlaid on the images are the morphological reconstructions of the cells. The sample cell in (a) is also shown in (c) 16. The sample cell in (b) is also shown in (c) 20. Note that the stimulating electrodes appear large, but the exposed area is only \(400\mu \mathrm{m}\) . Also visible are the lycra threads used to keep the retina affixed and the stimulating electrode tracks. c) The electrical receptive fields shown together with the dendritic receptive field estimates. The electrodes with stars above them show the approximate location of the optic disc for each preparation. </center>

doi:10.1371/journal.pcbi.1004849. g008

of omitting these higher components made little difference to the predicted result. We used a ratio \(G\) measuring how much of the variance in the response is accounted for by the first principal component \((\overline{\nu}_{1})\) compared to the next most significant component \((\overline{\nu}_{2})\) . \(G\) was generally much greater than one, signifying that for most cells a large proportion of the spike- triggered variance is contained in the first principal component. A histogram of \(G\) for all cells is given in Fig 9D, which shows that 18 of the 20 cells had a \(G\) value \(>4\) . Cells with a single dominant principal component have spatial interactions between electrodes that are linear to a good approximation.

## Model validation

\(80\%\) of the data was used to recover the model parameters and the remaining data was used to validate the model prediction. Fig 10A compares the validation spike probabilities and the model predicted probabilities for all cells (grey curves). For clarity, we show the curves without error bars. Also shown is the model prediction for one cell with standard error bars (black solid line). The model accurately predicted the responses of the RGCs to electrical stimulation. Small

> **Image description.** A composite figure consisting of four scientific plots (a, b, c, and d) titled "Fig 9. Population data," illustrating various statistical and physiological measurements derived from a population of cells.
>
> **Panel (a): Threshold Recovery Plot**
> This scatter plot displays the relationship between positive and negative electrical thresholds. The X-axis is labeled "Positive threshold ($\mu$A)" (ranging from 0 to 600), and the Y-axis is labeled "Negative threshold ($\mu$A)" (ranging from 0 to 600). Data points are represented by three types of symbols: black circles ("OFF"), white circles ("ON"), and white squares ("NA"). The points generally follow a positive linear trend, indicated by a dashed line. The caption notes that no significant differences were found between cell types ($p > 0.3$).
>
> **Panel (b): Correlation Coefficients**
> This bar chart shows the distribution of the correlation coefficients between positive and negative electrical receptive fields. The X-axis is labeled "Correlation coefficient" (ranging from -1 to 0), and the Y-axis is labeled "Number of cells" (ranging from 0 to 14). The bars show a distribution heavily skewed toward the negative end, with the highest count (14 cells) occurring in the range closest to -1.
>
> **Panel (c): Radius of Electrical Influence vs. Dendritic Field Size**
> This scatter plot compares the radius of electrical influence ($D^{+}$) to the dendritic field size. The X-axis is labeled "$D^{+}$ $\mu$m" (ranging from 0 to 2000), and the Y-axis is labeled "Dendritic field size ($\mu$m)" (ranging from 0 to 700). Data points are categorized by the number of electrodes influencing the cell: open circles ("One electrode"), closed circles ("Two electrodes"), and squares ("Three electrodes"). The data points show a general upward trend, suggesting that a larger radius of electrical influence tends to correspond to a larger dendritic field size.
>
> **Panel (d): Histogram of G**
> This histogram displays the distribution of the value $G$ (defined in Eq (10)). The X-axis is labeled "G" and is divided into bins: 1-2, 2-3, 3-4, 5-10, 10-20, 20-30, and 30+. The Y-axis is labeled "Number of cells" (ranging from 0 to 8). The distribution is centered around the 5-10 bin, which contains the highest number of cells (8).
>
> The overall figure is accompanied by a detailed caption providing context for each panel, including statistical findings and the specific biological parameters being measured (e.g., $W^{+}$ and $W^{-}$).

<center>Fig 9. Population data. (a) Threshold recovered from the nonlinear function for positive and negative regions for all cells; no significant differences were found between cell types \((p > 0.3)\) . (b) The correlation coefficients of the positive and negative electrical receptive fields \((W^{+}\) and \(W^{- })\) . (c) Radius of electrical influence for 21 cells. Shown is the approximate range of electrical influence for anodic-first stimulation \((D^{+})\) and the dendritic field size for each cell. Cells were only significantly influenced by one (open circle), two (closed circle) or three (square) electrodes in the ERF. (d) Histogram showing the value of \(G\) (Eq (10)) for all cells. 20 of the 25 cells recovered a \(W_{i}^{+}\) that was 4 or more times larger than \(W_{i}^{-}\) . </center>

doi:10.1371/journal.pcbi.1004849. g009

deviations in the prediction could likely be explained by modeling errors due to omission of some significant components. Using a different set of data to validate the model gave slightly different deviations, and slightly different estimates of the error. However, in all cases the model still accurately predicted the responses. The average \(E^{\mathrm{RMS}}\) for all cells was \(6.3\%\) error, with a maximum error of \(11.7\%\) (see Table 1).

There were 17 cells that recovered two or more components that fell outside the \(95\%\) confidence interval in the statistical hypothesis test. To test for improvements in the prediction by including higher components, we fit a two- dimensional surface to the probability data (e.g. Fig 7A). The same validation data used from the one- dimensional model was used to compute the error from a two- dimensional model. Note that for some cells the training data was undersampled in regions that were sampled with the validation data. These points were omitted when calculating the model error. The model error for the two- dimensional model \((E^{\mathrm{RMS2}})\) was compared to the error from the one- dimensional model \((E^{\mathrm{RMS1}})\) . For most cells, little improvement was found in model error, and a few cells resulted in a higher error (Fig 10B). A slightly higher error for a few cells is likely due to over fitting to increased noise, which occurs due to undersampling of the two- dimensional surface fit. For the two cells that had a low value

> **Image description.** A two-panel scientific figure, labeled "Fig 10. Model validation," which presents scatter plots comparing predicted probabilities and model errors across multiple data points.
>
> **Panel (a): Predicted vs. Actual Spike Probability**
> This panel is a scatter plot comparing the "Predicted spike probability" on the x-axis (ranging from 0 to 1) against the "Actual spike probability" on the y-axis (also ranging from 0 to 1).
> *   **Data Representation:** The plot contains numerous thin gray lines, representing the predicted versus actual probabilities for all cells. A single, prominent thick black solid line is overlaid on the data, representing the validation of a specific sample cell.
> *   **Visual Pattern:** The vast majority of the gray lines cluster closely around the diagonal line of perfect prediction (where predicted equals actual). The thick black line also follows this diagonal trend, indicating a high degree of accuracy for the sample cell.
> *   **Caption:** The panel is titled "Fig 10. Model validation."
>
> **Panel (b): Model Error Comparison**
> This panel is a scatter plot comparing two different measures of model error: "$E^{\mathrm{RMS1}}$" on the x-axis (ranging from 0 to 0.15) and "$E^{\mathrm{RMS2}}$" on the y-axis (ranging from 0 to 0.1).
> *   **Data Representation:** The plot consists of numerous black data points scattered across the graph. A dashed diagonal line is drawn, representing the relationship where $E^{\mathrm{RMS1}}$ equals $E^{\mathrm{RMS2}}$.
> *   **Visual Pattern:** The data points are generally scattered around the dashed diagonal line, showing a positive correlation between the two error metrics.
> *   **Highlighted Points:** Two specific data points are circled to draw attention to them: one is a gray circle and the other is a black circle, indicating specific cells where the model error was significantly reduced or changed.
>
> The overall figure serves to validate a model's performance by showing how well predicted probabilities match actual probabilities (Panel a) and how the two types of model error relate to each other (Panel b).

<center>Fig 10. Model validation. (a) The predicted probability compared to the actual probability from the validation data for all cells (gray). For clarity this data is shown without error bars. The validation of the sample cell from Fig 7 with standard error bars (black solid line) is also shown. The root mean square error for this cell was 0.056. (b) The 2-dimensional model error \((E^{\mathrm{RMS2}})\) is compared to the 1-dimensional model error \((E^{\mathrm{RMS1}})\) for all cells where the hypothesis test recovered 2 or more significant components. </center>

doi:10.1371/journal.pcbi.1004849. g010

of \(G\) , the model error was reduced by approximately half \((9.8\%\) to \(4.2\%\) ) for one cell and changed very little for the other \((3.3\%\) to \(3.5\%\) ) (See the two circled points in Fig 10B).

## Long latency responses

We examined if the model could also be applied to the long- latency responses to predict responses that were most likely of presynaptic network activity. Understanding the secondary effects of electrical stimulation is important in a clinical setting to understand differences between the perceived and expected responses. Responses originating from presynaptic origin can have excitatory or suppressive effects on postsynaptic RGCs. Fig 11A illustrates the positive ERF \((\overrightarrow{w}^{+})\) for the sample cell (same cell from Fig 7) that had an excitatory long- latency response. The negative ERF was almost the same in magnitude and location as the positive ERF and hence is not shown. In this preparation, the optic disc was placed above electrode 9. It is this electrode that most strongly influences the long- latency response in this neuron. The accuracy of the model was assessed in the same way as the model error for the short- latency responses. For this cell, the model predicted the long- latency response accurately (error approximately \(7\%\) ) (Fig 11B). It is evident from the corresponding eigenvalues (Fig 11C) that there is an excitatory and suppressive component that affects the long- latency responses. Excitatory or suppressive effects applied through the retinal network can be investigated by analysis of long- latency responses. Fig 11D illustrates an example of a cell that was very responsive in its short- latency responses; however, it became suppressed by high amplitude stimulation in its long- latency responses. The corresponding eigenvalues are shown in Fig 11E. Although our results on short- latency responses showed that RGCs were largely indifferent to the pulse polarity, analysis on the long- latency responses could produce responses that favored a particular pulse polarity. Fig 11F shows an example of a cell that was sensitive to both polarities of short- latency stimulation but its long- latency response resulted largely from cathodic- first stimulation. The corresponding eigenvalues are shown in Fig 11G.

## Application to efficient stimulation

When little is known about the neural system, a naive stimulation strategy might be to activate multiple nearby electrodes such that the amplitude of stimulation across the electrodes is

> **Image description.** A multi-panel scientific figure, labeled Figure 11, illustrating a model applied to long-latency neural responses, consisting of seven distinct panels (a) through (g). The figure uses scatter plots, line graphs, and heat maps to visualize receptive fields, response probabilities, and variance across principal components.
>
> The panels are organized as follows:
>
> *   **Panel (a):** This panel displays a dense field of small blue dots, representing the positive electrical receptive field for long-latency responses. Several points are highlighted: one in green and one in red. To the right of the field, a vertical scale lists numerical values ranging from 200 down to -200, indicating the magnitude of the response at specific locations.
> *   **Panel (b):** This is a line graph comparing predicted and actual spike probabilities. The X-axis is labeled "Predicted spike probability" (ranging from 0 to 1), and the Y-axis is labeled "Actual spike probability" (ranging from 0 to 1). A solid line shows the relationship between the two, starting below the diagonal and trending upward.
> *   **Panel (c):** This scatter plot shows the eigenvalues of long-latency spike-triggered stimuli. The X-axis is "Component number" (1 to 20), and the Y-axis is "Normalized variance" (ranging from 0 to 3). The data points exhibit a clear, steep downward trend.
> *   **Panel (d):** This scatter plot illustrates an example of a cell with a suppressive response for long-latency (LL) responses. The X and Y axes are both labeled "Principal component 1 (uA)" and "Principal component 2 (uA)," ranging from -400 to 400. The plot contains numerous gray dots (representing the LL response) and a few colored dots (representing the short-latency (SL) response) overlaid for comparison.
> *   **Panel (e):** This graph shows the corresponding eigenvalues for the long-latency responses in panel (d). The X-axis is "Component number" (1 to 20), and the Y-axis is "Normalized variance" (ranging from 0 to 1), showing a downward trend.
> *   **Panel (f):** This scatter plot shows an example of a cell with a preferred stimulus polarity for long-latency responses. Similar to panel (d), the X and Y axes are "Principal component 1 (uA)" and "Principal component 2 (uA)," ranging from -400 to 400. It displays gray dots (LL response) and colored dots (SL response) for comparison.
> *   **Panel (g):** This graph displays the corresponding eigenvalues for the long-latency responses in panel (f). The X-axis is "Component number" (1 to 20), and the Y-axis is "Normalized variance" (ranging from 0 to 1.5), showing a downward trend.
>
> The figure is titled "Fig 11. Model applied to long-latency responses." The accompanying text provides detailed context for each panel, explaining the significance of the receptive field, the prediction accuracy (root mean square error of 0.07), and the characteristics of the suppressive and preferred stimulus polarity responses.

<center>Fig 11. Model applied to long-latency responses. (a) The positive electrical receptive field for long-latency responses of the same cell as in Fig 7. This cell is largely influenced by electrode 9, which in this preparation was below the optic disc. (b) The predicted response vs. the actual response probability for the cell in (a). The root mean square error between prediction and actual response probability was 0.07. (c) The eigenvalues of the long-latency spike-triggered stimuli with one large excitatory and suppressive component evident. (d) An example of a cell with a suppressive response for long-latency (LL) responses. This cell fired with fewer spikes when the stimulus was stronger along the first or second principal component. Also shown is the short-latency (SL) response for comparison. (e) The corresponding eigenvalues for the long-latency responses in (d). (f) An example of a cell with a preferred stimulus polarity for long-latency responses. This cell responded with a greater number of spikes when the stimulus was cathodic-first, and very few spikes when the stimulus was anodic-first. Also shown is the short-latency response for comparison. (g) The corresponding eigenvalues for the long-latency responses in (f). doi:10.1371/journal.pcbi.1004849.g011 </center>

doi:10.1371/journal.pcbi.1004849. g011

equal. However, the ERF recovered from the model gives an insight into the stimulus that improves the efficacy of a response in the neuron. To compare a naive stimulation strategy to stimulation using currents on electrodes that are proportional to \(\overline{w}^+\) , we used the recovered model to compare the response probabilities for both strategies. Fig 12A compares stimulation on one, two, or three of the electrodes closest to the sample cell, to stimulation with currents proportional to \(\overline{w}^+\) . To make an unbiased comparison, comparisons were made while keeping the total power fixed. Since all of the electrodes were of the same geometry, this was equivalent to keeping a constant norm on the stimulation vector \(\overline{S}_i\) . For this example, a stimulus on three of the closest electrodes, where the current amplitudes on each electrode were equal, resulted in better efficacy than stimulating on only one or two electrodes. However, the efficacy was

> **Image description.** A technical figure consisting of two panels, (a) and (b), which are line graphs and scatter plots comparing different neural stimulation strategies. The overall figure is titled "Fig 12. Comparison of stimulation along $\overline{w}^{+}$ to a multi-electrode, constant amplitude strategy."
>
> **Panel (a): Response Probability vs. Stimulus Norm**
> This panel is a line graph showing the relationship between "Stimulus norm" on the x-axis and "Response probability" on the y-axis.
> *   **X-axis:** Labeled "Stimulus norm," ranging from 0 to 250.
> *   **Y-axis:** Labeled "Response probability," ranging from 0 to 1.
> *   **Data:** Three distinct curves are plotted, representing different electrode strategies:
>     *   "Single electrode" (represented by a dashed line).
>     *   "Two electrodes" (represented by a dotted line).
>     *   "Three electrodes" (represented by a solid line).
> *   **Visual Pattern:** All three curves exhibit a sigmoidal (S-shaped) pattern, starting near zero probability at a stimulus norm of zero and approaching a probability of 1 as the stimulus norm increases. The curves are closely clustered, indicating that the response probability is similar across the three stimulation strategies.
>
> **Panel (b): Threshold Comparison**
> This panel is a scatter plot showing the relationship between two threshold measures.
> *   **X-axis:** Labeled "Threshold ($\overline{w}^{+}$)," ranging from 0 to 600.
> *   **Y-axis:** Labeled "Threshold ($S_N$)," ranging from 0 to 600.
> *   **Data Points:** Data points are plotted for three strategies, distinguished by symbols:
>     *   "Single electrode" (represented by a star symbol, $\star$).
>     *   "Two electrodes" (represented by a triangle symbol, $\triangle$).
>     *   "Three electrodes" (represented by a circle symbol, $\circ$).
> *   **Visual Pattern:** The data points generally follow a diagonal trend, suggesting a strong positive correlation between the two threshold measures. The points are scattered around a visible trend line.
>
> The figure uses standard scientific notation and clear labeling to compare the efficacy of different electrical stimulation methods. The caption provides context, noting that the comparison is between stimulating along $\overline{w}^{+}$ and a naive strategy ($S_N$).

<center>Fig 12. Comparison of stimulation along \(\overline{w}^{+}\) to a multi-electrode, constant amplitude strategy. (a) The response probability when stimulating along \(\overline{w}^{+}\) is compared to a naive strategy that uses only one electrode, or equal amplitude currents on two or three electrodes. (b) The naive strategy \((S_{\mathrm{N}})\) is compared to stimulating along \(\overline{w}^{+}\) . Only the \(S_{\mathrm{N}}\) resulting in the lowest thresholds are shown; single electrode (star), two electrodes (triangle) or three electrodes (circle). </center>

doi:10.1371/journal.pcbi.1004849. g012

further improved when stimulating proportionally to \(\overline{w}^{+}\) . Fig 12B compares the threshold from a naive strategy \((S_{\mathrm{N}})\) , to the threshold of a stimulus proportional to \(\overline{w}^{+}\) for all cells. Here, we compare only \(S_{\mathrm{N}}\) resulting in the lowest threshold, single electrode (star), two electrodes (triangle), or three electrodes (circle). In all cases, stimulation proportional to \(\overline{w}^{+}\) results in a higher efficacy for a given power. On average, stimulation proportional to \(\overline{w}^{+}\) resulted in a threshold 0.8 (SD 0.2) times the threshold of the \(S_{\mathrm{N}}\) resulting in the lowest threshold.

## Discussion

The research presented here is motivated by the goal to improve the fidelity of neural prostheses by improving stimulation strategies through the use of predictive models of neural response to electrical stimulation. The model we present describes a method to predict the response of neurons to patterns of concurrent electrical stimulation. It is simple to construct and evaluate, and could be applied clinically and throughout the nervous system.

## Mathematical model

The model we present here was adapted from well established Gaussian white noise models developed to describe light responses in the retina [16,18,20,22]. With minor modifications, we have shown the application of this type of model to describe responses to electrical stimulation. The model is scalable and can be used to also describe retinal responses to electrical stimulation using small, high density electrodes, or to describe long- latency responses.

RGC responses to concurrent electrical stimulation across multiple electrodes could be accurately modeled by a nonlinear transformation of a linear spatially filtered stimulus. Simultaneous biphasic pulses were applied to all electrodes, with the stimulation amplitude on each electrode randomly sampled from a Gaussian distribution. The model's linear filter characterizes the neuron's electrical receptive field. The nonlinear function characterizes the neuron's intrinsic nonlinear firing properties. Stimulus- evoked spikes in the recorded neurons were analyzed using principal component analysis to determine the linear filter and reduce the dimensionality of the spike- triggered stimuli.

For most cells a single linear filter was sufficient to predict the neural response to a good approximation, indicating that interactions between concurrently stimulated electrodes are predominantly linear. High coefficients of determination for the nonlinear function fits were obtained (lowest \(\mathrm{r}^2 = 0.83\) ), demonstrating that the double sigmoid function is an accurate description of the nonlinearity. The model was trained with \(80\%\) of the data, with the remainder used for validation. The spike probability from the validation data was compared to the predicted probability, which resulted in an average error of \(6.4\%\) across the population (maximum error \(11.7\%\) ).

For many cells, short- latency responses were within 2–3 ms from the stimulation offset. While the origin of the spikes were not investigated, the latencies are consistent with latencies attributed to direct activation of RGCs in response to 1 ms pulses [38]. Four cells showed overlapping short- and long- latency clusters with spike latencies of up to 6 ms (Fig 6D). It is possible that some of the spikes in the four cells with overlapping clusters might have had a mixture of direct and indirect (network mediated) activity. Despite this, the model was able to accurately predict the response. The technique could also be applied to investigate the long- latency responses driven by synaptic activity. The effects seen in the long- latency responses can be excitatory, suppressive (also observed in [38]), or polarity- selective. Importantly, a separate analysis of long- latency responses produced distinct electrical receptive fields compared to the short- latency responses. Long- latency responses in the retina are mediated via the activation of retinal interneurons and might result in high acuity vision [39]. The techniques described can be used to gain a deeper understanding of the retinal network and the effects of electrical stimulation at distant sites. Investigation into the long- latency responses can give insight into the secondary effects of stimulation and how these might influence perception.

## Comparison to previous studies

Models recovered from white noise stimuli have been used to characterize light responses in the retina [16,18,20] and cortex [40], electrical responses in the retina [26,41], subthreshold responses in squid axons [42], and to characterize information transfer from the sensory periphery [43]. The advantage of estimating models with Gaussian white noise is that the neurons can be presented with a wide range of possible inputs and adaptation is reduced compared to more regularly structured stimuli. These properties make these models more suitable for characterizing neural responses to spatiotemporal patterns of electrical stimulation. Additionally, analysis techniques for white noise stimulation have been extensively explored in the retina to describe light responses [16,18,20,21]. We have used a spike- triggered covariance model and demonstrated that it can be accurately applied to describe electrical responses.

Jepson et al. [44] demonstrated the versatility of a piecewise linear model in capturing neural response probabilities to electrical stimulation. Their study used a high- density array with small electrode diameters and combined stimulation across two or three electrodes to achieve spatial selectivity. Only fixed ratios of stimulus amplitudes were explored. In contrast, our stimuli consisted of Gaussian white noise that allowed the exploration of a vast range of stimulus inputs across all available electrodes, to find an estimate of the cell's ERF. This has the potential to be more efficient when simultaneously recording from multiple neurons, as the same stimuli can be used to generate the model parameters for all recorded neurons. Our study also used large diameter electrodes due to their relevance to clinical visual prosthesis stimulation arrays [45].

No strong correlation between the area over which the cell was affected ( \(D^+\) or \(D^-\) ), and the size of the dendritic field was found. It is possible that much of the relationship is lost when using large diameter electrodes, or that the stimulation was largely axonal. The spatial ERFs

were generally as might be expected: i.e. the electrodes closest to the cell significantly affected the response. However, some unexpected results were apparent. For example, cells in Fig 8C17 and 8C18 both had a small dendritic field and they were located in a similar location in relation to the stimulating array. However, cell 17 only had two significant electrodes, whereas cell 18 had three. While the origin of these differences are unknown, complexities in ERF shapes have been previously observed [39,46]. As suggested by Sim et al. [46], the complex shapes could be due to axonal stimulation. Our results demonstrate the utility of our technique in identifying even complex ERFs.

Freeman et al. [26] explored single electrode stimulation of the retina using binary white noise to recover a temporal spike- triggered average stimulus. This study demonstrated that electrical white noise models can be used to estimate the temporal relationship between the stimulus and response, while our model describes the spatial relationship across electrodes. We assume that the effect of temporal interactions at \(10\mathrm{Hz}\) is small, an assumption that might account for some of the error in prediction. A model that also incorporates temporal effects is desirable, especially when considering higher stimulation frequencies, but technical challenges remain. A similar model to Chichilnisky [16] could be modified for electrical stimulation and incorporate spatiotemporal ERFs, but the accuracy of the model would decrease as the number of frames increased. The stimulus artefact could also be a problem when stimulating at high frequencies. To obtain longer recordings, one solution is to record extracellular potentials, which is also the only practical solution for patient testing. In this case, the stimulus artefact would be larger than the spike signal, making spike identification more challenging. At low stimulus frequencies, the stimulus artefact could be removed by artefact removal techniques [39,47,48], allowing detection of short- latency spikes.

## Relevance for neural prostheses and clinical applications

A major goal of our work is to develop models that can be applied in real- time, closed- loop applications. The applications of closed- loop systems to modern technology are vast. There are several potential advantages to the development of neuroprostheses that make use of neural feedback. An obvious advantage of neural feedback is much tighter control of evoked neural activity, when that activity can be measured and the stimulus adjusted to match a desired outcome. A second advantage is automation of patient fitting procedures, minimizing the need for time- consuming psychophysics. Furthermore, many stimulation algorithms are limited to stimulation with one electrode at a time, in part because the time required to test myriad possible combinations of simultaneous electrode stimulation is prohibitive using a psychophysical approach. Closed- loop neural stimulation models can also take advantage of control theory and can be designed to adapt to changes in the system being controlled. Open- loop strategies cannot adapt to changes such as changes at the electrode- tissue interface.

The model we present is simple and appropriate for real- time computation; however, technical challenges remain. A requirement of in vivo or patient tests of closed- loop control is to obtain high density extracellular neural recordings. Devices that can combine stimulation and recording on the same electrode need to balance high surface area and charge capacity for stimulation, with electrodes of low geometric surface area for single- unit recordings [45]. Recent new materials have led to the development of flexible electrode wires capable of stimulation and recording [49]. However, a high density array capable of stable recordings and stimulation remains to be developed.

Our model can be extended by increasing the number of recording electrodes, to describe the response of multiple neurons across the array, thus making it a multi- input multi- output system. Multi- input multi- output control is a widely researched area of control and could be

applied to achieve patterns of activation across the array. In a visual prosthesis, a desired pattern of activation could be obtained from RGC activation models in response to patterned light [16,50]. Our model can be fit to individual patients based on recorded responses and used to develop control strategies that are patient specific. Devices that can record and stimulate can then be used to try and address some of the more complex problems in the field, namely that of relating stimulation to visual percept [51].

## Author Contributions

Conceived and designed the experiments: HM MIM MRI DBG TK SLC. Performed the experiments: MIM. Analyzed the data: MIM HM MRI DBG TK SLC AEH. Contributed reagents/ materials/analysis tools: NVA DJG MIM HM. Wrote the paper: MIM HM MRI DBG TK AEH.

## References

1. Aflalo T, Kellis S, Klaes C, Lee B, Shi Y, et al. (2015) Decoding motor imagery from the posterior parietal cortex of a tetraplegic human. Science. 348: 906-910. doi: 10.1126/science.aaa5417 PMID: 25999506  
2. van Mierlo P, Papadopoulou M, Carrette E, Boon P, Vandenberghe S, et al. (2014) Functional brain connectivity from EEG in epilepsy: Seizure prediction and epileptogenic focus localization. Prog Neurobiol. 121: 19-35. doi: 10.1016/j.pneurobio.2014.06.004 PMID: 25014528  
3. Grayden DB, Clark GM (2006) Implant design and development. Cochlear implants: a practical guide (Cooper H, Craddock L). pp. 1-20.  
4. Guenther T, Lovell NH, Suaning GJ (2012) Bionic vision: system architectures-a review. Expert Rev Med Devices. 9: 33-48. doi: 10.1586/ERD.11.58 PMID: 22145839  
5. Lewis PM, Ackland HM, Lowery AJ, Rosenfeld JV (2015) Restoration of vision in blind individuals using bionic devices: A review with a focus on cortical visual prostheses. Brain Res. 1595: 51-73. doi: 10.1016/j.brainres.2014.11.020 PMID: 25446438  
6. Findlay JM, Maxwell-Armstrong C (2011) Posterior tibial nerve stimulation and faecal incontinence: a review. Int J Colorectal Dis. 26: 265-273. doi: 10.1007/s00384-010-1085-4 PMID: 21069357  
7. Van De Berg R, Guinand N, Nguyen TK, Ranieri M, Cavuscens S, et al. (2014) The vestibular implant: frequency-dependency of the electrically evoked vestibulo-ocular reflex in humans. Front Syst Neurosci. 8.  
8. Benabid AL (2007) What the future holds for deep brain stimulation. Expert Rev Med Devices. 4: 895-903. PMID: 18035954  
9. Berger TW, Hampson RE, Song D, Goonawardena A, Marmarelis VZ, et al. (2011) A cortical neural prosthesis for restoring and enhancing memory. J Neural Eng. 8: 046017. doi: 10.1088/1741-2560/8/4/046017 PMID: 21677369  
10. Hamani C, Andrade D, Hodaie M, Wennberg R, Lozano A (2009) Deep brain stimulation for the treatment of epilepsy. Int J Neural Syst. 19: 213-226. PMID: 19575509  
11. Gorzelic P, Schiff S, Sinha A (2013) Model-based rational feedback controller design for closed-loop deep brain stimulation of Parkinson's disease. J Neural Eng. 10: 026016. doi: 10.1088/1741-2560/10/2/026016 PMID: 23449002  
12. Kim S-P, Sanchez JC, Rao YN, Erdogmus D, Carmena JM, et al. (2006) A comparison of optimal MIMO linear and nonlinear models for brain-machine interfaces. J Neural Eng. 3: 145. PMID: 16705271  
13. Plonsey R, Barr RC (2007) Bioelectricity: a quantitative approach. New York: Springer Science & Business Media.  
14. Meffin H, Tahayori B, Grayden DB, Burkitt AN (2012) Modeling extracellular electrical stimulation: I. Derivation and interpretation of neurite equations. J Neural Eng. 9: 065005. doi: 10.1088/1741-2560/9/6/065005 PMID: 23187045  
15. Meffin H, Tahayori B, Sergeev EN, Mareels IM, Grayden DB, et al. (2014) Modelling extracellular electrical stimulation: III. Derivation and interpretation of neural tissue equations. J Neural Eng. 11: 065004. doi: 10.1088/1741-2560/11/6/065004 PMID: 25419585  
16. Chichilnisky E (2001) A simple white noise analysis of neuronal light responses. Network-Comp Neural. 12: 199-213.
17. Sekirnjak C, Hottowy P, Sher A, Dabrowski W, Litke AM, et al. (2008) High-resolution electrical stimulation of primate retina for epiretinal implant design. J Neurosci. 28: 4446-4456. doi: 10.1523/JNEUROSCI.5138-07.2008 PMID: 18434523
18. Pillow JW, Simoncelli EP (2003) Biases in white noise analysis due to non-Poisson spike generation. Neurocomputing. 52: 109-115.
19. Pillow J, Shlens J, Paninski L, Sher A, Litke A, et al. (2008) Spatio-temporal correlations and visual signaling in a complete neuronal population. Nature. 454: 995-999. doi: 10.1038/nature07140 PMID: 18650810
20. Schwartz O, Pillow JW, Rust NC, Simoncelli EP (2006) Spike-triggered neural characterization. J Vis. 6: 484-507. PMID: 16889482
21. Samengo I, Gollisch T (2013) Spike-triggered covariance: geometric proof, symmetry properties, and extension beyond Gaussian stimuli. J Comput Neurosci. 34: 137-161. doi: 10.1007/s10827-012-0411-y PMID: 22798148
22. Pillow JW, Simoncelli EP (2006) Dimensionality reduction in neural models: an information-theoretic generalization of spike-triggered average and covariance analysis. J Vis. 6: 414-428. PMID: 16889478
23. Rust NC, Schwartz O, Movshon JA, Simoncelli E (2004) Spike-triggered characterization of excitatory and suppressive stimulus dimensions in monkey V1. Neurocomputing. 58: 793-799.
24. Rust NC, Schwartz O, Movshon JA, Simoncelli EP (2005) Spatiotemporal elements of macaque v1 receptive fields. Neuron. 46: 945-956. PMID: 15953422
25. Touryan J, Lau B, Dan Y (2002) Isolation of relevant visual features from random stimuli for cortical complex cells. J Neurosci. 22: 10811-10818. PMID: 12486174
26. Freeman DK, Eddington DK, Rizzo JF 3rd, Fried SI (2010) Selective activation of neuronal targets with sinusoidal electric stimulation. J Neurophysiol. 104: 2778-2791. doi: 10.1152/jn.00551.2010 PMID: 20810683
27. Kameneva T, Abramian M, Zarelli D, Nesic D, Burkitt AN, et al. (2015) Spike history neural response model. J Comput Neurosci. 38: 463-481. doi: 10.1007/s10827-015-0549-5 PMID: 25862472
28. Mueller JK, Grill WM (2013) Model-based analysis of multiple electrode array stimulation for epiretinal visual prostheses. J Neural Eng. 10: 036002. doi: 10.1088/1741-2560/10/3/036002 PMID: 23548495
29. Huxlin KR, Goodchild AK (1997) Retinal ganglion cells in the albino rat: revised morphological classification. J Comp Neurol. 385: 309-323. PMID: 9268130
30. Sun W, Li N, He S (2002) Large-scale morphological survey of rat retinal ganglion cells. Vis Neurosci. 19: 483-493. PMID: 12511081
31. Perry V, Oehler R, Cowey A (1984) Retinal ganglion cells that project to the dorsal lateral geniculate nucleus in the macaque monkey. Neuroscience. 12: 1101-1123. PMID: 6483193
32. Boycott B, Wassle H (1974) The morphological types of ganglion cells of the domestic cat's retina. J Physiol. 240: 397-419. PMID: 4422168
33. Wassle H, Boycott BB (1991) Functional architecture of the mammalian retina. Physiol Rev. 71: 447-480. PMID: 2006220
34. Hamill OP, Marty A, Neher E, Sakmann B, Sigworth F (1981) Improved patch-clamp techniques for high-resolution current recording from cells and cell-free membrane patches. Pflügers Archiv. 391: 85-100. PMID: 6270629
35. O'Brien BJ, Isayama T, Richardson R, Berson DM (2002) Intrinsic physiological properties of cat retinal ganglion cells. J Physiol. 538: 787-802. PMID: 11826165
36. Wong RC, Cloherty SL, Ibbotson MR, O'Brien BJ (2012) Intrinsic physiological properties of rat retinal ganglion cells with a comparative analysis. J Neurophysiol. 108: 2008-2023. doi: 10.1152/jn.01091.2011 PMID: 22786958
37. Jensen RJ, Rizzo JF III (2006) Thresholds for activation of rabbit retinal ganglion cells with a subretinal electrode. Exp Eye Res. 83: 367-373. PMID: 16616739
38. Tsai D, Morley J, Suaning G, Lovell N (2009) Direct activation and temporal response properties of rabbit retinal ganglion cells following subretinal stimulation. J Neurophysiol. 102: 2982-2993. doi: 10.1152/jn.00545.2009 PMID: 19741103
39. Lorach H, Goetz G, Smith R, Lei X, Mandel Y, et al. (2015) Photovoltaic restoration of sight with high visual acuity. Nature Med. 21: 476-482. doi: 10.1038/nm.3851 PMID: 25915832
40. Emerson RC, Bergen JR, Adelson EH (1992) Directionally selective complex cells and the computation of motion energy in cat visual cortex. Vision Res. 32: 203-218. PMID: 1574836
41. Marmarelis PZ, Naka K-I (1972) White-noise analysis of a neuron chain: an application of the Wiener theory. Science. 175: 1276-1278. PMID: 5061252
42. Guttman R, Feldman L, Lecar H (1974) Squid axon membrane response to white noise stimulation. Biophys J. 14: 941–955. PMID: 4429772
43. Metzner W, Koch C, Wessel R, Gabbiani F (1998) Feature extraction by burst-like spike patterns in multiple sensory maps. J Neurosci. 18: 2283–2300. PMID: 9482813
44. Jepson LH, Hottowy P, Mathieson K, Gunning DE, Dabrowski W, et al. (2014a) Spatially patterned electrical stimulation to enhance resolution of retinal prostheses. J Neurosci. 34: 4871–4881.
45. Cogan SF (2008) Neural stimulation and recording electrodes. Annu Rev Biomed Eng. 10: 275–309. doi: 10.1146/annurev.bioeng.10.061807.160518. PMID: 18429704
46. Sim S, Szalewski R, Johnson L, Akah L, Shoemaker L, et al. (2014) Simultaneous recording of mouse retinal ganglion cells during epiretinal or subretinal stimulation. Vis Res. 101: 41–50. doi: 10.1016/j.visres.2014.05.005. PMID: 24863584
47. Sekirnjak C, Hottowy P, Sher A, Dabrowski W, Litke AM, et al. (2006) Electrical stimulation of mammalian retinal ganglion cells with multielectrode arrays. J Neurophysiol. 95: 3311–3327. PMID: 16436479
48. Wagenaar DA, Potter SM (2002) Real-time multi-channel stimulus artifact suppression by local curve fitting. J Neurosci Methods. 120: 113–120. PMID: 12385761
49. Apollo NV, Maturana MI, Tong W, Nayagam DA, Shivdasani MN, et al. (2015) Soft, Flexible Freestanding Neural Stimulation and Recording Electrodes Fabricated from Reduced Graphene Oxide. Adv Funct Mater. 25: 3551–3559.
50. Smirnakis SM, Berry MJ, Warland DK, Bialek W, Meister M (1997) Adaptation of retinal processing to image contrast and spatial scale. Nature. 386: 69–73. PMID: 9052781
51. Fine I, Boynton GM (2015) Pulse trains to percepts: the challenge of creating a perceptually intelligible world with sight recovery technologies. Phil Trans R Soc B. 370: 20140208. doi: 10.1098/rstb.2014.0208. PMID: 26240423

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
