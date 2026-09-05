```
@article{schwenk2026thalamocortical,
  title={Thalamocortical network dynamics can explain visual impulse responses and perceptual echoes},
  author={Jakob C.B. Schwenk and Maureen A. Hagan and Shaun L. Cloherty and Elizabeth Zavitz and Adam P. Morris and Nicholas S.C. Price and Marcello G.P. Rosa and Andrea Alamia and Frank Bremmer},
  journal={iScience},
  year={2026},
  volume={29},
  number={9},
  pages={117311},
  doi={10.1016/j.isci.2026.117311},
  url={https://www.sciencedirect.com/science/article/pii/S2589004226026891}
}
```

---

# Article

# Thalamocortical network dynamics can explain visual impulse responses and perceptual echoes

Jakob C.B. Schwenk, \(^{1,2,3,8,*}\) Maureen A. Hagan, \(^{4}\) Shaun L. Cloherty, \(^{4,5}\) Elizabeth Zavitz, \(^{6}\) Adam P. Morris, \(^{4,7}\) Nicholas S.C. Price, \(^{4}\) Marcello G.P. Rosa, \(^{4}\) Andrea Alamia, \(^{1}\) and Frank Bremmer \(^{2,3,4}\) \(^{1}\) Centre de Recherche Cerveau and Cognition (CerCo), CNRS, Université de Toulouse, Toulouse, France \(^{2}\) Department of Neurophysics, Marburg University, Marburg, Germany \(^{3}\) Center for Mind, Brain and Behavior - CMBB, Universities of Marburg, Giessen and Darmstadt, Marburg, Germany \(^{4}\) Department of Physiology and Neuroscience Program, Biomedicine Discovery Institute, Monash University, Clayton, VIC 3800, Australia \(^{5}\) School of Engineering, RMIT University, Melbourne, VIC, Australia \(^{6}\) Department of Electrical and Computer Systems Engineering, Monash University, Wellington Road, Clayton, VIC 3800, Australia \(^{7}\) Data Science and AI platform, Monash eResearch Centre, Monash University, Clayton, VIC 3800, Australia \(^{8}\) Lead contact \(^{*}\) Correspondence: jakob.schwenk@cnrs.fr https://doi.org/10.1016/j.isci.2026.117311

## SUMMARY

Although temporal information is ubiquitous in natural vision, the cortex shows strong intrinsic rhythmicity. Recent electroencephalogram (EEG) studies have revealed a component of the visual impulse response function (IRF) resembling a narrow alpha- band (7- 13 Hz) filter with a slow decay (the "perceptual echo"), but so far this has not been investigated at the cellular level. Here, we characterize responses in marmoset V1 to broadband visual flicker. The stimulus- locked dynamics were characterized by a non- oscillatory IRF and dominated by low frequencies. Spiking activity was coupled to the stimulus in a temporally sparse steady state, with individual units showing expected temporal frequency tuning. These dynamics can be explained by an established thalamocortical network model. We further show that under reduced damping the model reproduces the oscillatory dynamics observed in the awake human IRF. Our findings newly suggest a role for thalamocortical alpha resonance in the generation of the perceptual echoes.

## INTRODUCTION

The accurate representation of temporal information is a critical part of visual processing, as it forms the basis for any adaptive interaction with a constantly changing environment. Yet, the visual cortex also exhibits intrinsic rhythmicity at various scales, resulting from its structural and functional organization. Of these, alpha rhythmicity (7- 13 Hz) is the most prominent feature, which has been linked to diverse visual, cognitive, and attentional functions. \(^{1}\) However, the question of how this regular, high- amplitude oscillation interacts with the continuous and temporally flexible encoding of visual information remains the subject of theories. \(^{2 - 4}\)

The resonance properties of the visual system have been studied in the human electroencephalogram (EEG) with the use of steady- state visual evoked potentials (SSVEPs), i.e., the periodic responses to prolonged visual flicker at a constant temporal frequency (see Herrmann \(^{5}\) ; for a comprehensive review on SSVEPs, see Vialatte et al. \(^{6}\) ). Similar stimulation protocols with regular flicker have been used to characterize the temporal response properties of V1 neural populations in animal models. \(^{7 - 9}\) Both lines of studies revealed resonance characteristics, indicating that the visual cortex is more responsive to visual stimulation at certain temporal frequencies, and most strongly in

the alpha range. However, the regular stimulation at a single frequency at a time does not reflect the temporal information that is available in natural vision, which is generally not fully predictable and comprises a broader spectrum of frequencies. A recent line of human EEG studies (following VanRullen and MacDonald \(^{10}\) ) has instead used broadband random luminance flicker combined with reverse- correlation to derive visual impulse- responses from a steady state (in the order of a few seconds per trial). This approach revealed a sustained oscillatory response component in the alpha range that follows the transient early response, and decays over a long period of up to 1 s. This narrow- band component, dubbed the "perceptual echo" by VanRullen and MacDonald, shows a spatiotemporal distribution that suggests propagation across the cortex in the form of a traveling wave. \(^{11,12}\) More recent studies have suggested possible functional roles of the echo component in active rhythmic sampling and prediction of visual input. \(^{12 - 17}\) However, the neural basis of the response remains largely unclear.

Our goal in this study was two fold: first, noting that the stimulation paradigm used to record the perceptual echo response in humans has not been applied in the animal model, we were interested in the neural response dynamics at the cortical level to this type of stimulus (broadband luminance flicker). To this end, we recorded from the primary visual cortex (area V1) of

marmoset monkeys under anesthesia, while matching the human paradigm as closely as possible to establish a link between the two scales.

Second, we asked whether the observed responses and the human perceptual echoes could be explained by existing dynamical models of V1 activity. From a dynamical systems perspective, the shape of the perceptual echo characterizes a narrow- band alpha filter with a slowly decaying impulse response. Over the last decades, several network models have been developed that can account for the generation of intrinsic alpha activity in the visual cortex (see the recent review by Bastiaens et al.15). Between these models and experimental findings, it is generally assumed that both cortico- cortical and thalamo- cortical alpha generators exist, which interact at a more global scale.19 Here, we use an established network model of the geniculo- cortical pathway, which has previously been shown to accurately reproduce the dynamics of spontaneous (noise- driven) alpha activity and alpha resonance in steady state visual responses.20,21

## RESULTS

We first present neural responses to broadband visual flicker stimulation recorded in marmoset V1 under anesthesia. The animals were stimulated with random luminance sequences (covering the population receptive field [RF] of the recording array), and steady- state impulse response functions (IRFs) were derived by cross- correlating the stimulus with the recorded signals (Figure 1A). In subsequent sections, we use an established thalamocortical model to describe the data and show potential links to the human EEG response.

## LFP responses

All V1 contacts showed a clear response to the onset of the stimulus sequence (trial average for a single electrode channel in Figure 1B). Response latencies (onset- and to the largest peak) were in the expected range of V1 latencies22 (Figure 1B), with a slight difference between animals (Figure 1C; median latencies, monkey 1: onset, 46 ms, peak, 78 ms; monkey 2: onset, 52 ms, peak, 94 ms). This confirmed that stable V1 responsivity was preserved in the anesthetized state, forming the basis for further investigation.

The continuous responses to the stimulus in the steady state (>250 ms after sequence onset) showed a similar pattern in both monkeys, with a primary response peak and a slow return to baseline (channel- averages shown in Figure 1D). Neither response exhibited a sustained oscillatory component at the level of individual channels or the channel average. Correspondingly, the spectrum of phase coupling between LFP and stimulus (shown in Figure 1E) revealed broadband coupling to frequencies between approximately 5 and 50 Hz, following a linear decrease with frequency, with peak coupling in the theta range in both monkeys (monkey 1: 6.98 Hz; monkey 2: 3.26 Hz). The phase offset (right axes, dashed lines) showed an approximately linear increase with frequency, consistent with frequency- independent coupling at a constant temporal delay.  

A comparison of the steady state and sequence onset responses at the level of individual channels (examples in Figure 1F) showed largely comparable impulse waveforms, with a consistent shift to lower peak latencies in the steady state (Figure 1G). This shift was statistically significant in both animals (Rank- sum test, both \(p < 0.001\) [corrected]) (mean decrease in peak latency, monkey 1: \(- 7.47\) ms; monkey 2: \(- 13.75\) ms). At the same time, onset latencies were comparable between the two responses (both n.s.). This pattern is consistent with a linearly adapted state in which the continuous response is reduced in amplitude and thus reaches its peak faster.

## Spiking responses

In addition to the continuous LFP response, we were also interested in how the stimulus information was represented in V1 local spiking activity. To this end, we isolated spiking units (both single- and multi- unit, final sample included in the analysis: \(n = 50\) in monkey 1 and \(n = 31\) in monkey 2) and correlated their spike trains with the stimulus sequence. Figure 2A shows an example of the response to sequence onset for one unit, characteristic of the population response in both monkeys. Spiking activity returned to pre- stimulus baseline levels within a few hundred milliseconds after a brief transient burst following sequence onset (as quantified later). We derived the continuous impulse response of the spike trains from the spike- triggered average (STA) stimulus luminance (Figure 2B). Figure 2C shows an overlay of the average STA and sequence onset responses for both monkeys, revealing again similar responses that are shifted to lower peak latencies in the steady state (Figure 2D; paired \(t\) test, pooled: \(\mathrm{t}(80) = 3.89\) , \(p < 0.001\) ). Analogous to the LFP analysis, we computed an index of phase coupling to the stimulus. Here, for a given unit, this is defined by the consistency (phase- locking value [PLV]) of the STA stimulus phase preceding a spike. The left axes in Figure 2E show the average PLV spectra for each monkey (evaluated for each unit at their peak response latency). At the level of individual units, responses showed some diversity in their coupling to specific frequency bands, as visible from the histograms of peaks extracted from PLV spectra across the population of units (Figure 2E, right axes). However, the average spectrum followed a similar slope as observed in the LFP responses (cf. Figure 1E), with peak coupling again in the theta range (monkey 1: 7 Hz; monkey 2: 6.6 Hz). This pattern is expected for a population of V1 neurons with different temporal- frequency tuning,22- 24 summing to a representation of a broader spectrum in the population.

Lastly, we quantified the firing rate adaptation in the steady state by computing the log- ratio between a baseline time window (within 1 s before sequence onset) and the sequence (>250 ms) (Figure 2F). For this, we split units into ON- and OFF- responsive units based on whether the largest peak in the STA was positive or negative. This analysis confirmed that rates were overall indistinguishable from baseline levels during the steady state (paired \(t\) tests, pooled: ON- response units: \(\mathrm{t}(58) = - 0.48\) , \(p = 0.63\) ; OFF- response units: \(\mathrm{t}(21) = - 1.32\) , \(p = 0.20\) ), indicating that the observed stimulus coupling occurs in a regime that does not rely on an increase in firing rate.

## Thalamocortical model

After characterizing the IRF to broadband input in the steady state, we next asked whether the observed responses could

> **Image description.** A complex scientific figure, Figure 1, presenting neurophysiological data from experiments on visual cortex (V1) responses to broadband visual flicker in two monkeys. The figure is composed of seven distinct panels (A through G), each illustrating a different aspect of the experimental results.
>
> **Panel A: Experimental Setup**
> This panel is a schematic diagram showing the experimental paradigm. It depicts a side view of a monkey's head with a Utah array (a grid of electrodes) implanted in the visual cortex. A stimulus, represented by a white circle, is shown projecting onto the visual field, and the text "patch in pop. RF" is visible, indicating the recording location.
>
> **Panel B: Mean Response to Sequence Onset**
> This is a line graph showing the mean LFP response over time. The Y-axis is labeled "potential," and the X-axis spans 0 to 250 ms. A single line traces the response, showing a rapid increase immediately following the stimulus onset, followed by a gradual decay. The stimulus start is marked by the label "seq. onset."
>
> **Panel C: Latency Distributions**
> This panel contains two histograms comparing response timing. The top histogram shows a distribution of responses across channels. The bottom section displays two histograms: "Onset" (shaded) and "Peak" (white). Both distributions are centered roughly between 60 and 80 ms, indicating the average time for the initial response versus the time for the maximum response across all recorded channels.
>
> **Panel D: Impulse Response Functions (IRFs)**
> This is a line graph representing the average IRF in the steady state. The Y-axis is labeled "Corr." (correlation), and the X-axis is "Lag," ranging from 0 to 400 ms. A central line shows the average correlation, and a shaded area surrounding it represents the $\pm 1$ SD across channels, illustrating the variability of the response.
>
> **Panel E: Phase Coupling**
> This panel consists of two side-by-side line graphs, one for "Monkey 1" and one for "Monkey 2." Both graphs measure phase coupling at a fixed lag of 50 ms.
> *   The left Y-axis in each graph is "PLV" (Phase Locking Value), ranging from 0 to 0.3, with a shaded area indicating $\pm 1$ SD.
> *   The right Y-axis shows "Phase offset" in radians, indicated by dashed lines.
> *   The X-axis for both graphs is "Frequency," ranging from 10 to 50 Hz.
>
> **Panel F: Individual Channel Responses**
> This panel shows two side-by-side line graphs, one for "Monkey 1" (channel ch3) and one for "Monkey 2" (channel ch25). Both graphs plot "Response" (normalized) on the Y-axis against "Time/Lag" on the X-axis (0 to 200 ms). Each graph overlays two lines: "IRF" (Impulse Response Function) and "Seq. Onset" (Sequence Onset response), allowing for a visual comparison of the shape and timing of the two responses.
>
> **Panel G: Latency Shifts**
> This panel contains four box plots arranged in a 2x2 grid, comparing latency shifts. The top row is labeled "Monkey 1" and "Monkey 2." The bottom row is labeled "Onset" and "Peak." Each box plot displays the distribution of latency shifts (normalized) for either the onset or peak response, comparing the initial response timing to the steady-state IRF timing. The plots show the median, quartiles, and range of these shifts.

<center>Figure 1. LFP responses in V1 to broadband visual flicker </center>

(A) Summary of experimental paradigm. Animals were anesthetized and stimulated with random luminance sequences while neural data were recorded with a Utah array. Impulse response functions (IRFs) were computed from cross-correlation of stimulus sequence and LFP.  
(B and C) Mean response to sequence onset for a single channel (B) and for all channels (C) and both monkeys (top). Histograms of onset (shaded) and peak response (white) latencies across channels (bottom).  
(D) IRFs in the steady state, as trial- and channel-averages. Shaded areas show \(\pm 1\) SD across channels.  
(E) Phase coupling between stimulus and LFP, evaluated for a fixed lag of 50 ms. Left axes in each image show mean coupling strength (PLV, \(\pm 1\) SD in the shaded area), right axes (dashed lines) show the mean phase offset between the signals in radians.  
(F) Overlay of IRFs and sequence-onset responses for a single channel in each monkey (with normalized response amplitudes).  
(G) Distributions of shifts in latency (onset/peak as in C) from sequence-onset response to the steady state IRF. Shifts in peak latency were significantly different from zero (rank-sum test, both \(p < 0.001\) [corrected]).

> **Image description.** This is a complex, multi-panel scientific figure (Figure 2) presenting various analyses of spiking responses in V1 (Visual Cortex) to broadband visual flicker, utilizing line graphs, scatter plots, and raster plots.
>
> The figure is organized into six distinct panels (A through F), each detailing a specific aspect of the neural response.
>
> **Response Dynamics (Panels A, B, and C):**
> *   **Panel A (Spike Raster Plot):** This panel displays a raster plot showing individual spike timing across multiple trials. The x-axis represents time from 0 to 250 ms, and the y-axis represents the trial number. A marker labeled "seq onset" is visible near the beginning of the time axis.
> *   **Panel B (STA Analysis):** This line graph plots "Average rate (norm)" on the y-axis against time (0 to 250 ms) on the x-axis. It shows two distinct lines, one green and one red, representing the average response to the stimulus, labeled "Stimulus: Lum" and "V1 Spikes."
> *   **Panel C (Average STA and Sequence Onset):** This line graph compares two average responses, plotted against "Latency [ms]" (0 to 250). The y-axis is "Average rate (norm)" (0 to 0.6). A purple line, labeled "Seq On," and a green line, labeled "STA," are shown, with a shaded area surrounding the traces representing variability. The panel is labeled "Monkey 1."
>
> **Firing Rate and Latency (Panels D and F):**
> *   **Panel D (Peak Latencies):** This scatter plot relates baseline firing rate to steady-state response latency. The x-axis, "Baseline rate (spk/s)," is on a logarithmic scale (10 to 100). The y-axis, "Steady state response latency [ms]," ranges from 0 to 200. The data points are categorized by color and shape: green dots represent "ON units," and purple circles represent "OFF units."
> *   **Panel F (Firing Rates):** Similar to Panel D, this scatter plot also relates baseline rate to steady-state response latency. The x-axis is "Baseline rate (spk/s)" (log scale, 10 to 100), and the y-axis is "Steady state response latency [ms]" (0 to 200). It uses the same color coding: green dots for "ON units" and purple circles for "OFF units."
>
> **Phase Coupling (Panel E):**
> *   **Panel E (Phase coupling):** This dual-axis plot measures phase coupling across different frequencies. The x-axis is "Frequency [Hz]" (0 to 50). The left y-axis is "PLV" (Phase Locking Value, 0 to 0.06), represented by a purple line. The right y-axis is "$\#$ Peaks" (0 to 0.15), represented by a green histogram showing the distribution of peak frequencies extracted from individual units. The panel is titled "Phase coupling (at peak latency per unit)."

<center>Figure 2. Spiking responses in V1 to broadband visual flicker (A) Spike raster plot for an example unit (monkey 1) showing the response to sequence onset. (B) Continuous responses to the stimulus were analyzed using the spike-triggered average (STA) stimulus luminance, separately for each unit. (C) Average STA and sequence onset responses overlayed (amplitude normalized). All traces represent mean across units \(\pm 1\) SEM in the shaded area. (D) Scatterplot of peak latencies for STA and sequence onset responses, with single dots corresponding to individual units. Colors correspond to the two monkeys as in (C). On average, latencies were significantly lower during the steady state \((p< 0.001)\) . (E) Frequency spectra of spike-to-stimulus phase coupling. Left axes show PLV as an index of coupling strength, as mean \(\pm 1\) SEM across units in the shaded area. Right axes show the histograms of peaks extracted from the PLV spectra of individual units, to illustrate the variability in temporal frequency tuning. Coupling was evaluated for each unit at the lag corresponding to their peak STA latency (positive or negative). (F) Scatterplot of firing rates at baseline (pre-stimulus) and during the steady state. Single data points represent individual units, with dots and circles corresponding to units for which the largest STA peak was positive and negative, respectively. </center>

be explained by existing models of the neural dynamics in the geniculo- cortical pathway leading up to V1. For this, we focused specifically on the LFP, since our broader aim was to establish a link between local field recordings and the human EEG, which is dominated by the perceptual echo response.10  

We made use of a well- established thalamocortical neural field model,20,25 which models the geniculo- cortical pathway with three areas (Figure 3A): the thalamic relay (LGN) with bilateral connections to the inhibitory thalamic reticular nucleus (TRN), and V1, comprising excitatory and inhibitory populations, which receives feedforward stimulus information from the LGN and sends feedback to both thalamic nuclei. Previous studies have shown that the alpha activity observed in human EEG spectra can be explained as arising from the thalamic loop in this model.21,26

We modeled our experimental recordings by stimulating the network with random noise sequences and computing the IRF from the resulting V1 rate output, directly analogous to the LFP analysis (Figure 3B). When using standard human parameters, this IRF defaults to a composite response shape consisting of a sharp primary response followed by a late oscillatory component in the alpha range (with similarities to the human echo response, as we will explore later). This late component represents (alpha) rhythmicity that is intrinsically generated from the random input by the thalamic feedback loop (LGN/TRN). Its oscillatory envelope (decay time) depends directly on how

> **Image description.** A complex scientific figure, Figure 3, titled "Thalamocortical model of the IRF in V1," which illustrates a computational model architecture, example data traces, and various plots showing the modulation of the impulse response function (IRF) in V1. The figure is divided into seven panels (A through G).
>
> **Panel A: Model Schematic**
> This panel is a flow diagram illustrating the thalamocortical model architecture. It features four main components represented by boxes: TRN (thalamus), LGN (thalamus), V1-excitatory (cortical), and V1-inhibitory (cortical). Arrows indicate connections between these components. The connections are generally excitatory, but specific feedback loops are noted: feedback from the TRN ($v_{sr}$) and local cortical inhibition ($e_i$).
>
> **Panel B: Example Traces**
> This panel displays time-series traces representing the continuous model output. Multiple colored lines (traces) are plotted against time, showing the V1 potential in response to random noise stimulation. The y-axis is labeled "V1" and the x-axis is labeled "Time."
>
> **Panel C: Late IRF Component Modulation (Scatter Plot)**
> This panel is a 2D scatter plot showing the modulation of the late IRF component. The x-axis is labeled "TRN-LGN weight ($v_{sr}$)" and the y-axis is labeled "V1-LGN weight ($v_{se}$)." Several colored dots (red, green, blue, purple) are scattered across the plot. A label on the left side indicates "Peak Frequency ($\log_{10}$ Hz)," suggesting that the color of the dots corresponds to the peak frequency.
>
> **Panel D: Late IRF Component Modulation (Line Graph)**
> This panel is a line graph corresponding to the data points in Panel C. The x-axis is labeled "Lag (ms)" and the y-axis is labeled "Corr. (peak, norm)." Multiple colored lines are plotted, illustrating a trajectory. The caption notes that the lines show a trajectory from an overdamped (red) to an oscillatory regime (purple).
>
> **Panel E: TRN-LGN Feedback Weight vs. Decay Time**
> This panel is a line graph showing the relationship between TRN-LGN IPSP decay time and peak frequency. The x-axis is labeled "TRN-LGN IPSP decay ($\tau_{sr}$)" and the y-axis is labeled "Peak Frequency (Hz)." A single line slopes downward, indicating that as the decay time increases, the peak frequency decreases.
>
> **Panel F: V1-LGN Feedback Weight vs. Lag**
> This panel is a line graph showing the effect of V1-LGN feedback weight. The x-axis is labeled "Lag (ms)" and the y-axis is labeled "Corr. (peak, norm)." Six distinct colored lines (labeled 1 through 6) are plotted, representing different values of the V1-LGN feedback weight ($v_{se}$).
>
> **Panel G: Impulse Response (IRF) in Monkeys**
> This panel consists of two side-by-side line graphs, labeled "Monkey 1" and "Monkey 2." Both graphs plot the normalized correlation (Corr. (norm)) against Lag (ms). In both graphs, two lines are shown: "IRF (Data)," which is a noisy line representing experimental data, and "Best model fit," which is a smoother line representing the model's prediction.

<center>Figure 3. Thalamocortical model of the IRF in V1 (A) Schematic of the model architecture (for details, see STAR Methods), comprising two thalamic (LGN [s] and TRN [r]) and two cortical populations (V1-excitatory [e] and inhibitory [i]). Connections are excitatory except for feedback from the TRN (sr) and local cortical inhibition (ei). (B) Example traces for the continuous model output in response to random noise stimulation. Model IRFs were computed by cross-correlating the input with the resulting V1 potential (with inverted sign to model the recorded LFP). (C and D) Modulation of the late IRF component by thalamic net inhibition (here shown as \([v_{se} + v_{se}]\) with fixed feed-forward weights). Colored dots in (C) correspond to traces in (D), illustrating a trajectory from an overdamped (red) to an oscillatory regime (purple). The images in (C) show the peak frequency (left) </center>

(legend continued on next page)

much the excitatory feed- forward drive is damped in the network, with two points of inhibition: in the thalamus and in the cortex.

First, Figures 3C and 3D show the effects of damping at the thalamic level. Here, for fixed feedforward weights, oscillatory damping scales with the net weight of feedback into the LGN (inhibitory from TRN, \(v_{sr}\) , excitatory from V1, \(v_{se}\) ). The highlighted trajectory shows how the IRF changes when moving across this parameter space. In the over- damped regime (red dot), the IRF is non- oscillatory and dominated by low frequencies, qualitatively similar to our observations in the anesthetized marmoset. A sustained oscillation with a stable frequency ( \(\sim 10\) Hz for the parameters used here) and an increasing number of cycles emerges when approaching the stability boundary (solid lines in Figure 3C). The frequency of this oscillation depends chiefly on the time constants of the LGN- TRN feedback loop, as shown in Figure 3E for the decay time of the inhibitory connection. For plausible human parameter values (see Table 1), it falls within the alpha range.

The second point of damping in the network is the local inhibition of feedforward input in V1. The effect of modulating the corresponding weight \((v_{w})\) is shown in Figure 3F. Notably, here, increased inhibition does not affect the early parts of the response (since the inhibition is applied only after the first excitatory pass into V1), thus not leading to a shift to a lower frequency as for the thalamic damping. The effect on the late part of the response (>200 ms lag) is comparable with that of the thalamic damping.

We performed an algorithmic fitting procedure (with connection weights, decay time constants, and temporal delays as free parameters, see Table 1) to find the closest approximation of the model to our marmoset data, based on matching in both time- and frequency- domains. The resulting best fits to the average IRFs in both monkeys (Figure 3G) put the network in an over- damped regime as described earlier (compare with red traces in Figures 3D and 3F).

Thus, our model exploration suggests that the anesthetized state in our recordings corresponds to the overdamped state of a system that supports the emergence of an oscillatory IRF in a less- inhibited state. Notably, as pointed out earlier, this oscillatory regime closely resembles the response behavior observed in the human EEG (the perceptual echo \(^{15}\) ). While a detailed modeling of EEG responses is not within the scope of this study (this would require expanding the network by further cortical areas downstream, as discussed in more detail later), we consider it relevant to briefly highlight the qualitative similarities.

Figures 4A- 4D compare the V1 IRF obtained from the model to EEG responses measured in two human subjects (data from Schwenk et al. \(^{7}\) ). Figure 4A shows again the IRFs corresponding

to the two regimes described earlier (here, modulating only the thalamic inhibitory feedback weight). The corresponding spectra of phase coupling over time (i.e., lag) and frequency (Figure 4B) show that the oscillatory regime is characterized by a sustained coupling in the alpha range that is delayed relative to the early broadband component. In other words, alpha information contained in the stimulus reverberates for a prolonged duration in the network. This is a pattern also observed in the human EEG responses: the IRFs over occipital regions show the sustained oscillatory alpha component (Figure 4C), which is visible in the PLV spectra (Figure 4D) as delayed coupling, strikingly similar to the model output. Notably, while the decay time of the IRF oscillation in the model can be arbitrarily increased (up to and beyond the \(\sim 1\) s lag observed in the EEG) by moving closer to the stability boundary (sold line in Figure 3C), its envelope is always monotonically decreasing in the stable regime. In contrast, peak alpha coupling in the EEG in some subjects occurs for intermediate lags (e.g., around 500 ms for subject 2 in Figures 4C and 4D).

Figure 4E outlines a schematic model of how the echo response may be generated along the early visual pathway, summarizing the presented results. In the anesthetized state (bottom), the marmoset V1 IRF is non- oscillatory and dominated by low frequencies, which corresponds to strong damping of thalamic rhythmicity in the model. When this damping is reduced (top), the IRF in V1 becomes oscillatory. As we will discuss later, human EEG studies suggest that this oscillatory activity then propagates further along the visual hierarchy as a traveling wave, interacting with rhythmicity generated by feedback loops between areas and possibly modulation through the pulvino- cortical pathway. \(^{11,12,27,28}\) This secondary, corticocortical propagation, which is not included in our model, likely accounts for the late peak in alpha coupling in the summed EEG response.

## DISCUSSION

We reported results from neural recordings in V1 of the anesthetized marmoset in response to random luminance sequences. Our findings show that the IRF in this state is non- oscillatory and dominated by low frequencies. Spiking responses showed a similar pattern in the population, with some diversity in temporal frequency tuning between units. We found that our data are well explained by an established thalamocortical neural field model, which explains the recorded state as resulting from increased inhibitory gain. Moreover, we showed that, with more balanced weights, the same model assumes an oscillatory mode that exhibits striking resemblance to the human perceptual echo response.

Table 1. Values for parameters in the thalamocortical model

| Parameter | Sub-Parameter | Marmoset IRF fits (range for free parameters in brackets) | Human IRF (oscillatory regime) |
| :--- | :--- | :--- | :--- |
| | | **Monkey 1** | **Monkey 2** | |
| Qmax | Max. firing rate | 250 Hz | 250 Hz | 250 Hz |
| θ | Sigmoid threshold | 15 mV | 15 mV | 15 mV |
| σ' | Sigmoid threshold variability | 3.8 mV | 3.8 mV | 3.8 mV |
| γo | Cortical damping | 285 s-1 | 285 s-1 | 110 s-1 |
| τo | Input delay (Retina → LGN) | 40.1 [10, 50] ms | 26.8 [10, 50] ms | 25 ms |
| τ1 | Thalamocortical delay | 11 [10, 50] ms | 27.5 [10, 50] ms | 28 ms |
| α | Inverse PSP decay time | 43.31 [5, 80] s-1 | 33.45 [5, 80] s-1 | 20 s-1 |
| αgr | Inverse PSP decay time (TRN → LGN) | 45.96 [5, 80] s-1 | 7.66 [5, 80] s-1 | 7.5 s-1 |
| β, βgr | Inverse PSP rise time | 800 s-1 | 800 s-1 | 800 s-1 |
| νsri | Input weight to LGN | 5.56 [0, 6] | 4.93 [0, 6] | 1 |
| νee | Syn. weight V1exc → V1exc | 0.81 [0, 6] | 2.44 [0, 6] | 2.8 |
| νel | Syn. weight V1inh → V1exc | -3.45 [-6, 0] | -4.96 [-6, 0] | -3.5 |
| νes | Syn. weight LGN → V1 | 5.06 [0, 6] | 5.89 [0, 6] | 3 |
| νso | Syn. weight V1exc → LGN | 1.49 [0, 6] | 1.52 [0, 6] | 2.7 |
| νsr | Syn. weight TRN → LGN | -3.39 [-6, 0] | -4.74 [-6, 0] | -1.53 |
| νre | Syn. weight V1exc → TRN | 5.51 [0, 6] | 3.95 [0, 6] | 0.15 |
| νrs | Syn. weight LGN → TRN | 2.17 [0, 6] | 2.76 [0, 6] | 2.9 |

## Steady-state response to random luminance sequences in V1

Our results obtained for stimulus responses in the LFP and spikes are generally in line with previously reported response behavior of V1. Specifically, the broadband stimulus- coupling is in line with studies demonstrating that V1/area 17 responses phase- lock to regular rhythmic flicker across a broad range of frequencies (cat, anesthetized; mouse, awake). Comparable stimulus coupling has been found for human EEG responses in (regular flicker) SSVEPs, and indeed in the early broadband response component of the IRF characterized by random luminance sequences. The present findings add to this by establishing phase coupling to broadband flicker directly in the local field in V1.

The random sequences used in our experiment were presented as luminance information within a uniform patch, which is not the preferred stimulus to drive V1 neurons (which show similar gabor- like receptive field characteristics in marmosets as in macaques). Several studies have demonstrated robust encoding of luminance information (as independent of contrast) in V1 (macaque- 33- 35 and area 17 in cats- 34). Indeed, one study showed that cat area 17 responses to luminance changes precede those to changes in contrast, linked to an encoding by neurons with low spatial frequency preference and shorter latencies. In the primate visual system, this is consistent with activation of the magnocellular pathway, which exhibits tuning to lower spatial frequencies and larger receptive fields than parvocellular LGN neurons (macaque37 and marmoset38,39). The responses reported here were likely also strongly driven by this pathway.  

The specificity of our stimulus design (isoluminant patch) raises some caveats in the interpretation of our findings. First, the representation of uniform surfaces in V1 has been shown to involve two distinct response components that correspond to encoding of the edges and the surface of the stimulus, respectively (macaque40- 43). Importantly, the surface representation is slower than that of the edges and is hypothesized to result from neural "filling- in." This process is not fully understood, but appears to involve both feedforward modulation and cortical feedback signals.44

It is unclear how this secondary surface processing may have impacted the neural dynamics characterized here (and, correspondingly, human EEG paradigms using the same stimulus design, following VanRullen and MacDonald). One possibility is that the continuous patch representation is slower than that of edge- like stimuli with the same luminance profile. Alternatively, since the patch remains on screen, the "filling- in" may only affect the response to its onset and not the steady state. Future studies may consider extending our dynamical model to include the separation of signals into magno- and parvo- cellular pathways, building on existing models that explain the temporal dynamics of contour and surface processing from the interaction of these systems.45

More generally, lateral connectivity (within V1 or in the feedback to LGN) likely plays a role in the dynamics we observed. The early representation of luminance is known to be strongly modulated from the extra- classical receptive field (in cat LGN and visual cortex46,47), and magnocellular LGN neurons exhibit strong surround inhibition (in marmoset48- 50). Given the large size of the stimulus patch, this may have led to a suppression of responses in our data (as supported by the absence of any tonic rate response in the spiking activity). Conversely, responses from the immediate and more remote patch surroundings may show different dynamics. A recent study in mouse V1 showed that responses to regular flicker evoke standing wave patterns extending beyond the retinotopic stimulus

> **Image description.** This image is a complex, multi-panel scientific figure (Figure 4) that compares theoretical models of neural processing with empirical data from human EEG recordings, illustrating the generation of perceptual echo responses in the thalamocortical pathways. The figure is divided into five distinct panels (A, B, C, D, and E).
>
> **Model Comparison (Panels A and B):**
> Panel A is a line graph titled "Model: IRF" (Impulse Response Function). The Y-axis represents "Corr. (norm)" (normalized correlation), ranging from -1 to 1, and the X-axis represents "Lag [ms]" (Lag in milliseconds), ranging from 0 to 1000. Two lines are plotted: a blue line and a red line, both labeled "TRN-LGN Weight $\nu_{sr}$." The blue line shows a rapid, heavily damped oscillation, while the red line shows a more sustained, less damped oscillatory pattern. Panel B is a heatmap titled "Phase Coupling." It plots "PLV" (Phase Locking Value) on a color scale (from dark blue/black to bright yellow), against "Frequency [Hz]" (Y-axis, 0 to 40) and "Lag [ms]" (X-axis, 0 to 1000). This panel corresponds to the blue, damped state from Panel A, labeled with $\nu_{sr} = -4.2$.
>
> **Human EEG Data (Panels C and D):**
> Panel C presents two line graphs, "Subject 1 Oz" and "Subject 2 Oz," showing the "Corr." (correlation) versus "Lag [ms]" (0 to 1000). Both subjects exhibit a clear, oscillatory response (the perceptual echo) starting after an initial delay. Panel D is a corresponding heatmap titled "Phase Coupling" for the two subjects. Like Panel B, it plots "PLV" (0 to 1) against "Frequency [Hz]" (0 to 40) and "Lag [ms]" (0 to 1000). This panel corresponds to the oscillatory state, labeled with $\nu_{sr} = -1.4$.
>
> **Generative Model Schematic (Panel E):**
> Panel E is a schematic flow diagram illustrating the proposed generative model. It is divided into two main sections:
> 1.  **Top Section (Oscillatory):** Labeled "Awake/oscillatory," this section shows a visual hierarchy involving V1 (Visual Cortex), LGN (Lateral Geniculate Nucleus), and TRN (Thalamus Reticular Nucleus). Arrows indicate rhythmic activity propagating from V1 through LGN and TRN to higher visual areas and ultimately generating the "Human EEG."
> 2.  **Bottom Section (Damped):** Labeled "Anesthetized/strong damping," this section shows the same neural components (V1, LGN, TRN) but implies a lack of rhythmic propagation, resulting in a different output.
>
> The overall figure visually contrasts the damped, non-oscillatory model state with the oscillatory, rhythmic state, demonstrating how the latter is hypothesized to generate the complex, wave-like perceptual echo responses observed in human EEG data.

<center>Figure 4. Comparison of model IRF with human EEG perceptual echo responses and proposed model of their generation in the thalamocortical pathways (A) IRFs for model regimes between strong damping (blue) and the oscillatory state (red), by modulation of the thalamic inhibitory weight. (B) Phase coupling spectra, plotted as PLV over lag and frequency corresponding to the two opposing states in (A). (C) IRFs obtained from human EEG recordings in two exemplary subjects with large echo responses. Data taken from Schwenk et al.17 (binocular stimulus presentation in the upper visual periphery). Plots show mean \(\pm 1\) SEM across trials for occipital electrode Oz. (D) PLV lag-frequency spectra (as in B), for the two subjects in (C). PLV values at each bin represent the maximum coupling across an 11-electrode ROI over parieto-occipital areas, accounting for different topographies between the broadband early response and the perceptual echo. (E) Schematic illustrating how the present results could be integrated with previous findings into a generative model of the perceptual echo response. (Bottom) The anesthetized (or otherwise strongly damped) case in which no rhythmic activity is generated. In the oscillatory regime (top), rhythmic activity from V1 is likely propagated across the visual hierarchy through cortico-cortical connections, possibly with additional modulation by the pulvino-cortical pathway. This propagation would give rise to the global, wave-like echo response recorded in the EEG. </center>

presentation.7 Interestingly, the spatial frequency of those waves depended on the temporal frequency of the stimulus. This could lead to complex wave patterns emerging in the surroundings of a broadband flicker stimulus.  

Lastly, a limitation of our cross- correlation analyses is that they assume an approximately linear (or at least monotonically increasing) tuning to luminance in the population. At the level of individual units, it has been shown that some neurons prefer intermediate luminance values (macaque \(^{35}\) and cat \(^{35}\) ). The tuning of the wider V1 population has not been systematically studied, although pooling across neurons from early studies suggests that the relationship is indeed monotonic.30 In our study, an experimental control measure of responses to static luminance values would have allowed us to map the population tuning curve. It is possible that the IRF would differ if this nonlinearity were taken into account. It should be noted, however, that similar reverse correlation approaches in the EEG have proven valid for the estimation of IRFs across features and modalities (e.g., Crosse et al. \(^{51}\) ). The linearity assumption may generally be a reasonable approximation for larger populations.

From the present results and human EEG studies using the same paradigm, it is unclear whether the observed dynamics generalize to other types of stimuli. Future studies could utilize temporal modulation of other visual features (or other stimulus geometries tagged with luminance) to explore how the neural dynamics interact with feature encoding at different stages. Notably, a recent EEG study found that the modulation of visual target detection by spontaneous alpha oscillations also depends on which LGN- pathway is preferentially activated, with significant modulation only for stimuli biased toward the magnocellular pathway.52 This may indicate that the echo response is similarly restricted to this type of stimulus, although the degree to which ongoing and stimulus- locked alpha are independent remains an open question (as discussed later).

The stimulus- related spiking activity we observed was also in line with established response behavior of single neurons in V1, which are typically tuned to temporal frequency (macaque53,54 and marmoset22- 24). Responses in our data quickly reached a steady- state regime that was characterized by firing rates at or below baseline levels. This is consistent with strong adaptation or inhibition from the surround, combined with a non- preferred driving stimulus (as discussed earlier). Despite this, we found robust and temporally precise IRFs to the stimulus sequence, indicating a parsimonious encoding of temporal (luminance) information that is not based on increases in firing rate.

## Effects of anesthesia

Our modeling results suggest that the neural dynamics we observed in the LFP correspond to a state in which the thalamic input drive into V1 is strongly damped (either by an increase in thalamic inhibitory gain or a decrease in the excitatory loop gain between LGN and V1). The corresponding shift to overall lower frequencies is consistent with previously reported effects of deep anesthesia. The anesthetic agent used here, sufentanil (an analog of the mu- receptor agonist fentanyl55,56), is known to shift the EEG frequency spectrum toward low frequencies in human patients, an effect that accompanies loss of consciousness.57- 59 The temporal response properties of single neurons in the early visual pathway are generally altered under anesthesia (mice, urethane60; comparing three different anesthesia regimes in rats61).

Our observations are thus in line with the expected response dynamics in the anesthetized state. Importantly, our model fitting to IRFs should not be interpreted as a parametric estimate of the specific effects of anesthesia, for which we lack an awake control recording in the same animal. However, a number of dedicated modeling studies have used the same model framework we used here to explain neural dynamics under anesthesia, albeit for specific phenomena in the human EEG and propofol.62- 64 This, together with the good fits obtained for our data, shows that the thalamocortical network alone (i.e., consisting of LGN/TRN and V1) is suited to model a wide range of global dynamical states in the visual cortex.  

Notably, another study has previously applied the same stimulation paradigm to characterize IRFs at the meso- scale in V1 of macaques under propofol anesthesia (using voltage- sensitive dye [VSD] responses).65 In contrast to our findings, that study reported some evidence for sustained alpha oscill lations in the IRF in V1, similar to the human perceptual echo response, although only in two of three subjects. While it remains unclear to what extent this discrepancy is attributable to interspecies differences (as we will discuss in more detail later), it seems possible that the depth of anesthesia also plays a role. The results from our simple model predict that the oscillatory component should disappear with increasing inhibition. However, the actual relationship is likely significantly more complex, given that the effects of anesthetic agents are non- linear and interact with different network mechanisms at different stages.66

## Neural origins of the human perceptual echo response

One of the goals of this study was to investigate the neural correlates of the perceptual echo response described in the human EEG.10 We did not observe a phenomenological homolog of the human perceptual echo response in our data. The IRFs obtained for the LFP in V1 (in the anesthetized state) were non- oscillatory and dominated by low frequencies. However, our application of the thalamocortical model suggests that the thalamocortical network could produce an oscillatory IRF in the awake state, if the overall inhibitory gain is reduced. Moreover, the IRF obtained for parameter values chosen within established ranges for the human awake state20,67 closely resembles the decaying narrow- band filter of the perceptual echo. This opens up an intriguing new viewpoint on the neural origins of this response component. Our present results show that both states recorded with the same stimulation paradigm can be described by different regimes of a generalized thalamocortical network model. However, this should not be taken to suggest a direct link between the marmoset recordings and the human echo response. Both a description of the EEG IRF to random luminance flicker in any other species, and comparable analyses of V1 recordings from the awake state are still lacking (our own preliminary modeling of data from awake marmosets (limited by short fixation durations) suggests an oscillatory regime but with stronger damping than in the human model explored here; Schwenk et al., unpublished data).

The oscillatory regime we find for standard human parameters replicates early studies on the same model framework, which found robust alpha resonance in response to white noise stimulation.67- 69 These studies used the noise as background activity to model the emergence of spontaneous alpha activity at rest, but the response dynamics are the same when simulating a strong random input. Our work shows that this paradigm can be used to model the system's IRF and matched with IRF estimates from human EEG recordings.

Several studies on the perceptual echo response have speculated about its neural origins. This inference has primarily been based on its spatiotemporal pattern on the scalp, which shows propagation of the oscillation as a traveling wave.11,17,28 Specifically, evidence from different EEG paradigms17,70 and modeling28 suggests that the sustained oscillation of the echo is independent from the early response components of the IRF, with the latter originating in V1, while the former is a distributed response along multiple cortical sources. However, both the meso- scale IRFs reported by Chemla et al.65 and an fMRI study in humans71 showed that the sustained oscillation is also present

in V1 itself. From the available evidence, it remains an open question whether this oscillatory component is generated at the thalamocortical level, in V1 itself, or is relayed to it as feedback from higher areas.

So far, only one model of the echo response has been proposed that also includes a generating mechanism for the rhythmicity itself.12 That study explains the echo as arising entirely from feedback loops in the sequential activation of areas along the cortical hierarchy, reproducing both its frequency and wave- like propagation with plausible inter- areal delay parameters. Our present modeling results contrast this account by suggesting that alpha entrainment would occur already at the level of V1 input. Importantly, the two mechanisms are not exclusive. We recently showed27 that the hierarchical architecture proposed by Alamia and VanRullen12 still supports the same traveling wave propagation when the mechanism generating the fundamental oscillation is replaced by alpha pacemakers at each cortical level (which can be seen as a stand- in for any externally generated rhythmicity). Moreover, the inter- areal feedback loop still carried its own rhythmicity when the pacemakers were deactivated. Together with the results of the present study, this suggests that the echo response may in fact be sustained by two separate but frequency- coupled generating mechanisms. This is further supported by evidence gathered from neuromodulatory studies suggesting the presence of multiple generators for alpha rhythmicity at thalamic and cortical sources.19

Our tentative integrated model presented earlier (Figure 4E) reflects this interplay of mechanisms: we hypothesize that the echo as measured in the EEG arises from initial alpha resonance in the geniculocortical pathway, which is sustained and augmented through cortico- cortical propagation along the visual hierarchy, with possible modulation by the pulvinar.27

Our model exploration (expectedly) shows that the inverse decay of the oscillatory IRF component scales with the inhibitory gain in the geniculocortical pathway. This modulation is in line with empirical evidence and modeling work suggesting that the amplitude of the echo scales with excitatory gain12,17 and attention.10 As pointed out in previous studies, this contrasts with the dynamics of spontaneous alpha, which synchronizes during inhibition of visual input72- 74 and is inversely correlated with (cortical) excitability.75- 77 An interesting question for future studies will thus be how the stimulus- locked alpha arriving in V1 interacts, and possibly competes, with ongoing local alpha activity.  

A possible interaction between thalamocortical and ongoing alpha may additionally contribute to stabilizing the frequency of the oscillatory IRF component. Our model results show that inhibitory gain can be varied within a certain range with the response frequency remaining in the alpha range (as seen in Figure 3C). For ongoing alpha, however, the experimentally observed variations in peak frequency are typically even smaller and have been shown to be more strongly dependent on corticocortical circuits.72 The only frequency modulation of the perceptual echo response reported thus far is of similar magnitude.13 Interestingly, however, that study found that the frequency of spontaneous alpha was not modulated with the echo. Future studies in this direction could leverage similar known modulators of alpha frequency to determine the degree of independence and possible points of interaction between stimulus- locked and ongoing alpha oscillations.

## Limitations of the study

The conclusions of our integrated modeling have to be considered under the caveat of potential interspecies differences. Specifically, as pointed out earlier, a direct homolog of the human echo response has not been established in the awake marmoset (or macaque). It seems likely that such a homolog exists, given that alpha is a prominent and distributed rhythm also in the marmoset, and that dominant oscillatory modes and their distribution across laminae seem to be conserved across species.90 However, awake meso- scale recordings will be needed to fully establish an animal model for the study of perceptual echoes.

In particular, simultaneous recordings from multiple regions (LGN/V1 or V1 and higher cortical areas) would allow the proposed model to be tested directly and, potentially, macroscale projections for direct comparisons with the EEG to be estimated with higher accuracy. They could also clarify the relative contributions of the different circuits in which oscillatory activity could potentially be generated. Specifically, these are (1) the thalamocortical circuitry modeled here, (2) intra- cortical loops within V1 (for a review of both types of model, see Bastiaens et al.15), and (3) the inter- areal feedback loops proposed by Alamia and VanRullen.12 Importantly, as outlined earlier, we do not consider these as competing models but rather as different generative mechanisms for a distributed rhythm. The present study demonstrates that the thalamocortical loop can generally explain observed response dynamics. This should not be taken to suggest that other models cannot do so, or are less likely to play a role in the interplay of these mechanisms.

Another open question is the role of horizontal connectivity across retinotopic space within V1. The dynamical model used here, although still incorporating lateral propagation of activity across the cortex, integrates over cortical space and thus does not allow conclusions in this direction. However, mesoscale recordings have repeatedly demonstrated that evoked activity propagates across visual cortex in the form of a traveling wave.81,82 The spatiotemporal dynamics of these evoked responses and of similar spontaneous waves is directly shaped by horizontal connectivity in the cortex.82,83 At the macro- scale, EEG studies have furthermore shown that simultaneous echo responses can be evoked by separate stimuli in the two hemispheres.11,17 It will be crucial for our understanding of this response to investigate in future studies how localized stimulus- locked alpha is, and how its (putative) lateral propagation interacts between different retinotopic sites.

The ultimate goal of this line of research could be to establish a working dynamical model of the full stimulus- locked response (e.g., as outlined in Figure 4E), which could in turn be used to derive meaningful parametric measures at the level of subjects or conditions by fitting the model directly to EEG data. This perspective is particularly promising because the underlying EEG paradigm is relatively robust against noise and potentially flexible to be applied in various paradigms comparable to classical frequency- tagging.

## RESOURCE AVAILABILITY

## Lead contact

Any requests for additional information or resources should be addressed to the lead contact, Jakob C.B. Schwenk (jakob.schwenk@cnrs.fr).

## Materials availability

This study did not generate any new requests.

## Data and code availability

The data and original code to reproduce the findings of this study are publicly available under the following link: osf.io/25axi. Any additional information is available from the corresponding author upon request.

## ACKNOWLEDGMENTS

This work was supported by Deutsche Forschungsgemeinschaft (CRC/TRR- 135, project number: 222641018; IRTG- 1901; Excellence cluster EXC3066/1 "The Adaptive Mind - TAM", project number: 533717223), EU (PLACES) (all to F.B.), the Australian Research Council (DE180100344 to M.A.H.; DP200100179 to N.S.C.P. and M.A.H.; DP210103865 to M.G.P.R. and S.L.C.; DP210101042 to M.G.P.R. and E.Z.), and by the National Health and Medical Research Council of Australia (APP1194206 to M.G.P.R., APP1185442 to M.A.H. and S.L.C., APP1120667 to N.S.C.P.). J.C.B.S. and A.A. were funded by the European Union under the European Union's Horizon 2020 research and innovation program (grant agreements no. 101075930 to A.A.). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council (ERC). Neither the European Union nor the granting authority can be held responsible for them. The authors thank Janssen- Cilag for the donation of sufentanil citrate. The authors are grateful to Rufin VanRullen for helpful comments on the results.

## AUTHOR CONTRIBUTIONS

J.C.B.S., A.P.M., N.S.C.P., and F.B. conceived and designed research. M.A.H., S.L.C., E.Z., and N.S.C.P. performed experiments. J.C.B.S. analyzed data. J.C.B.S., A.P.M., N.S.C.P., M.G.P.R., A.A., and F.B. interpreted results of experiments. J.C.B.S. performed modeling. J.C.B.S. prepared figures and drafted manuscript. All authors edited, revised, and approved the final draft of the manuscript.

## DECLARATION OF INTERESTS

The authors declare no competing interests.

## STAR \(\times\) METHODS

Detailed methods are provided in the online version of this paper and include the following:

KEY RESOURCES TABLE EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS METHOD DETAILS \(\bigcirc\) Surgical and experimental procedures \(\bigcirc\) Visual stimulation \(\bigcirc\) LFP signal processing \(\bigcirc\) Analysis of spiking activity \(\bigcirc\) Steady- state LFP responses \(\bigcirc\) Steady- state spiking responses \(\bigcirc\) Thalamocortical model \(\bigcirc\) Model fitting of marmoset IRFs \(\bigcirc\) Comparison of model IRFs to human EEG responses \(\bigcirc\) QUANTIFICATION AND STATISTICAL ANALYSIS

Received: March 30, 2026 Revised: July 2, 2026 Accepted: August 7, 2026

## REFERENCES

1. Klimesch, W. (2012). Alpha-band oscillations, attention, and controlled access to stored information. Trends Cogn. Sci. 16, 606-617. https://doi.org/10.1016/j.tics.2012.10.007.  
2. Klimesch, W., Sauseng, P., and Hanslmayr, S. (2007). EEG alpha oscillations: The inhibition-timing hypothesis. Brain Res. Rev. 53, 63-88. https://doi.org/10.1016/j.brainresrev.2006.06.003.  
3. Van Diepen, R.M., Foxe, J.J., and Mazacheri, A. (2019). The functional role of alpha-band activity in attentional processing: the current zeitgeist and future outlook. Curr. Opin. Psychol. 29, 229-238. https://doi.org/10.1016/j.copsyc.2019.03.015.  
4. VanRullen, R. (2016). Perceptual Cycles. Trends Cogn. Sci. 20, 723-735. https://doi.org/10.1016/j.tics.2016.07.006.  
5. Herrmann, C.S. (2001). Human EEG responses to 1-100 Hz flicker: Resonance phenomena in visual cortex and their potential correlation to cognitive phenomena. Exp. Brain Res. 137, 346-353. https://doi.org/10.1007/s002210100682.  
6. Vialatte, F.B., Maurice, M., Dauwels, J., and Cichocki, A. (2010). Steady-state visually evoked potentials: Focus on essential paradigms and future perspectives. Prog. Neurobiol. 90, 418-438. https://doi.org/10.1016/j.pneurobiol.2009.11.005.  
7. Gulbinatie, R., Nazari, M., Rule, M.E., Bermudez-Contreras, E.J., Cohen, M.X., Mohajerani, M.H., and Heimel, J.A. (2024). Spatiotemporal resonance in mouse primary visual cortex. Curr. Biol. 34, 4184-4196. e7. https://doi.org/10.1016/j.cub.2024.07.091.  
8. Rager, G., and Singer, W. (1998). The response of cat visual cortex to flicker stimuli of variable frequency. Eur. J. Neurosci. 10, 1856-1877. https://doi.org/10.1046/j.1460-9568.1998.00197.x.  
9. Schneider, M., Tzanou, A., Uran, C., and Vinck, M. (2023). Cell-type-specific propagation of visual flicker. Cell Rep. 42, 112492. https://doi.org/10.1016/j.celrep.2023.112492.  
10. VanRullen, R., and MacDonald, J.S.P. (2012). Perceptual echoes at 10 Hz in the human brain. Curr. Biol. 22, 995-999. https://doi.org/10.1016/j.cub.2012.03.050.  
11. Lozano-Soldevilla, D., and VanRullen, R. (2019). The Hidden Spatial Dimension of Alpha : 10-Hz Perceptual Echoes Propagate as Periodic Traveling Waves in the Human Brain Report The Hidden Spatial Dimension of Alpha : 10-Hz Perceptual Echoes Propagate as Periodic Traveling Waves in the Human Brain. Cell Rep. 26, 374-380. e4. https://doi.org/10.1016/j.celrep.2018.12.058.  
12. Alamia, A., and VanRullen, R. (2019). Alpha oscillations and traveling waves: Signatures of predictive coding? PLoS Biol. 17, e3000487. https://doi.org/10.1371/journal.pbio.3000487.  
13. Benedetto, A., Lozano-Soldevilla, D., and VanRullen, R. (2018). Different responses of spontaneous and stimulus-related alpha activity to ambient luminance changes. Eur. J. Neurosci. 48, 2599-2608. https://doi.org/10.1111/eijn.13791.  
14. Brüers, S., and VanRullen, R. (2017). At What Latency Does the Phase of Brain Oscillations Influence Perception? eNeuro 4, 1-15. https://doi.org/10.1523/ENEURO.0078-17.2017.  
15. Chang, A.Y.-C., Schwartzman, D.J., VanRullen, R., Kanai, R., and Seth, A.K. (2017). Visual Perceptual Echo Reflects Learning of Regularities in Rapid Luminance Sequences. J. Neurosci. 37, 8486-8497. https://doi.org/10.1523/JNEUROSCI.3714-16.2017.  
16. Gulbinatie, R., Ilhan, B., and VanRullen, R. (2017). The Triple-Flash Illusion Reveals a Driving Role of Alpha-Band Reverberations in Visual Perception. J. Neurosci. 37, 7219-7230. https://doi.org/10.1523/JNEUROSCI.3929-16.2017.  
17. Schwenk, J.C.B., VanRullen, R., and Bremmer, F. (2020). Dynamics of Visual Perceptual Echoes Following Short-Term Visual Deprivation. Cereb. Cortex Commun. 1, tgaa012. https://doi.org/10.1093/texcom/tgaa012.  
18. Bastiaens, S.P., Momi, D., and Griffiths, J.D. (2025). A comprehensive investigation of intracortical and corticothalamic models of the alpha rhythm. PLoS Comput. Biol. 21, e1012926. https://doi.org/10.1371/journal.pcbi.1012926.  
19. Lozano-Soldevilla, D. (2018). On the Physiological Modulation and Potential Mechanisms Underlying Parieto-Occipital Alpha Oscillations. Front. Comput. Neurosci. 12, 23. https://doi.org/10.3389/fncom.2018.00023.  
20. Roberts, J.A., and Robinson, P.A. (2012). Quantitative theory of driven nonlinear brain dynamics. Neuroimage 62, 1947-1955. https://doi.org/10.1016/j.neuroimage.2012.05.054.  
21. Robinson, P.A., Rennie, C.J., Rowe, D.L., O'Connor, S.C., Wright, J.J., Gordon, E., and Whitehouse, R.W. (2003). Neurophysical Modeling of Brain Dynamics. Neuropsychopharmacology 28, S74-S79. https://doi.org/10.1038/sj.npp.1300143.  
22. Yu, H.H., Chaplin, T.A., Davies, A.J., Verma, R., and Rosa, M.G.P. (2012). A specialized area in limbic cortex for fast analysis of peripheral vision. Curr. Biol. 22, 1351-1357. https://doi.org/10.1016/j.cub.2012.05.029.  
23. Bourne, J.A., Tweedale, R., and Rosa, M.G.P. (2002). Physiological Responses of New World Monkey V1 Neurons to Stimuli Defined by Coherent Motion. Cereb. Cortex 12, 1132-1145. https://doi.org/10.1093/cercor/12.11.1132.  
24. Solomon, S.G., and Rosa, M.G.P. (2014). A simpler primate brain: the visual system of the marmoset monkey. Front. Neural Circuits 8, 96. https://doi.org/10.3389/fncir.2014.00096.  
25. Robinson, P.A., Rennie, C.J., Wright, J.J., and Bourke, P.D. (1998). Steady states and global dynamics of electrical activity in the cerebral cortex. Phys. Rev. E 58, 3557-3571. https://doi.org/10.1103/PhysRevE.58.3557.  
26. Rennie, C.J., Robinson, P.A., and Wright, J.J. (2002). Unified neurophysi-cal model of EEG spectra and evoked potentials. Biol. Cybern. 86, 457-471. https://doi.org/10.1007/s00422-002-0310-9.  
27. Schwenk, J.C.B., and Alamia, A. (2025). A hierarchical multiscale model of forward and backward alpha-band traveling waves in the visual system. PLoS Comput. Biol. 21, e1013294. https://doi.org/10.1371/journal.pcbi.1013294.  
28. Zhigalov, A., and Jensen, O. (2023). Perceptual echoes as travelling waves may arise from two discrete neuronal sources. Neuroimage 272, 120047. https://doi.org/10.1016/j.neuroimage.2023.120047.  
29. Di Russo, F., Pitzalis, S., Aprile, T., Spitoni, G., Patria, F., Stella, A., Spinelli, D., and Hillyard, S.A. (2007). Spatiotemporal analysis of the cortical sources of the steady-state visual evoked potential. Hum. Brain Mapp. 28, 323-334. https://doi.org/10.1002/hbm.20276.  
30. Maguire, W.M., and Baizer, J.S. (1982). Luminance coding of briefly presented stimuli in area 17 of the rhesus monkey. J. Neurophysiol. 47, 128-137. https://doi.org/10.1152/jn.1982.47.1.128.  
31. Kinoshita, M., and Komatsu, H. (2001). Neural Representation of the Luminance and Brightness of a Uniform Surface in the Macaque Primary Visual Cortex. J. Neurophysiol. 86, 2559-2570. https://doi.org/10.1152/jn.2001.86.5.2559.  
32. Vladusich, T., Lucassen, M.P., and Cornelissen, F.W. (2006). Do Cortical Neurons Process Luminance or Contrast to Encode Surface Properties? J. Neurophysiol. 95, 2638-2649. https://doi.org/10.1152/jn.01016.2005.  
33. Peng, X., and Van Essen, D.C. (2005). Peaked Encoding of Relative Luminance in Macaque Areas V1 and V2. J. Neurophysiol. 93, 1620-1632. https://doi.org/10.1152/jn.00793.2004.  
34. Dai, J., and Wang, Y. (2012). Representation of Surface Luminance and Contrast in Primary Visual Cortex. Cereb. Cortex 22, 776-787. https://doi.org/10.1093/cercor/bhr133.  
35. MacEvoy, S.P., and Paradiso, M.A. (2001). Lightness constancy in primary visual cortex. Proc. Natl. Acad. Sci. 98, 8827-8831. https://doi.org/10.1073/pnas.161280398.  
36. Wang, W.-L., Li, R., Ding, J., Tao, L., Li, D.-P., and Wang, Y. (2015). V1 neurons respond to luminance changes faster than contrast changes. Sci. Rep. 5, 17173. https://doi.org/10.1038/srep17173.  
37. Derrington, A.M., and Lennie, P. (1984). Spatial and temporal contrast sensitivities of neurones in lateral geniculate nucleus of macaque. J. Physiol. 357, 219-240. https://doi.org/10.1113/jphysiol.1984.sp015498.  
38. Kremers, J., and Weiss, S. (1997). Receptive field dimensions of lateral geniculate cells in the common marmoset (Callithrix jacchus). Vision Res. 37, 2171-2181. https://doi.org/10.1016/S0042-6989(97)00041-2.  
39. Forte, J.D., Hashemi-Nezhad, M., Dobbie, W.J., Dreher, B., and Martin, P.R. (2005). Spatial coding and response redundancy in parallel visual pathways of the marmoset Callithrix jacchus. Vis. Neurosci. 22, 479-491. https://doi.org/10.1017/S0952523805224094.  
40. Huang, X., and Paradiso, M.A. (2008). V1 Response Timing and Surface Filling-In. J. Neurophysiol. 100, 539-547. https://doi.org/10.1152/jn.00997.2007.  
41. Komatsu, H., Murakami, I., and Kinoshita, M. (1996). Surface representation in the visual system. Cogn. Brain Res. 5, 97-104. https://doi.org/10.1016/S0926-6410(96)00045-6.  
42. Zurawel, G., Ayzenshtat, I., Zweig, S., Shapley, R., and Slovin, H. (2014). A Contrast and Surface Code Explains Complex Responses to Black and White Stimuli in V1. J. Neurosci. 34, 14388-14402. https://doi.org/10.1523/JNEUROSCI.0848-14.2014.  
43. Lamme, V.A., Rodriguez-Rodriguez, V., and Spekreijse, H. (1999). Separate Processing Dynamics for Texture Elements, Boundaries and Surfaces in Primary Visual Cortex of the Macaque Monkey. Cereb. Cortex 9, 406-413. https://doi.org/10.1093/cercor/9.4.406.  
44. Yang, Y., Wang, T., Li, Y., Dai, W., Yang, G., Han, C., Wu, Y., and Xing, D. (2022). Coding strategy for surface luminance switches in the primary visual cortex of the awake monkey. Nat. Commun. 13, 286. https://doi.org/10.1038/s41467-021-27892-3.  
45. Breitmeyer, B.G., Kafaligonul, H., Ogmen, H., Mardon, L., Todd, S., and Ziegler, R. (2006). Meta- and paracontrast reveal differences between contour- and brightness-processing mechanisms. Vision Res. 46, 2645-2658. https://doi.org/10.1016/j.visres.2005.10.020.  
46. Rossi, A.F., Rittenhouse, C.D., and Paradiso, M.A. (1996). The Representation of Brightness in Primary Visual Cortex. Science 273, 1104-1107. https://doi.org/10.1126/science.273.5278.1104.  
47. Rossi, A.F., and Paradiso, M.A. (1999). Neural Correlates of Perceived Brightness in the Retina, Lateral Geniculate Nucleus, and Striate Cortex. J. Neurosci. 19, 6145-6156. https://doi.org/10.1523/JNEUROSCI.19-14-06145.1999.  
48. Felisberti, F., and Derrington, A.M. (2001). Long-range interactions in the lateral geniculate nucleus of the New-World monkey, Callithrix jacchus. Vis. Neurosci. 18, 209-218. https://doi.org/10.1017/S0952523801182064.  
49. Webb, B.S., Tinsley, C.J., Barraclough, N.E., Easton, A., Parker, A., and Derrington, A.M. (2002). Feedback from V1 and inhibition from beyond the classical receptive field modulates the responses of neurons in the primate lateral geniculate nucleus. Vis. Neurosci. 19, 583-592. https://doi.org/10.1017/S0952523802195046.  
50. Camp, A.J., Tailby, C., and Solomon, S.G. (2009). Adaptable Mechanisms That Regulate the Contrast Response of Neurons in the Primate Lateral Geniculate Nucleus. J. Neurosci. 29, 5009-5021. https://doi.org/10.1523/JNEUROSCI.0129-09.2009.  
51. Crosse, M.J., Di Liberto, G.M., Bednar, A., and Lalor, E.C. (2016). The multivariate temporal response function (mTRF) toolbox: A MATLAB toolbox for relating neural signals to continuous stimuli. Front. Hum. Neurosci. 10, 604-614. https://doi.org/10.3389/fnhum.2016.00604.  
52. Pilipenko, A., and Samaha, J. (2025). Selective Effects of Ongoing Alpha-Band Activity on Magno- and Parvo-Mediated Detection. Psychophysiology 62, e70070. https://doi.org/10.1111/psyp.70070.  
53. Foster, K.H., Gaska, J.P., Nagler, M., and Pollen, D.A. (1985). Spatial and temporal frequency selectivity of neurones in visual cortical areas V1 and V2 of the macaque monkey. J. Physiol. 365, 331- 363. https://doi.org/10. 1113/physiol.1985. sp015776.  
54. Hawken, M.J., Shapley, R.M., and Grosof, D.H. (1996). Temporal-frequency selectivity in monkey visual cortex. Vis. Neurosci. 13, 477- 492. https://doi.org/10.1017/s0952523800008154.  
55. Monk, J.P., Beresford, R., and Ward, A. (1988). Sufentanil. A review of its pharmacological properties and therapeutic use. Drugs 36, 286- 313. https://doi.org/10.2165/00003495- 198836030- 00003.  
56. Kelly, E., Sutcliffe, K., Cavallo, D., Ramos- Gonzalez, N., Alhosan, N., and Henderson, G. (2023). The anomalous pharmacology of fentanyl. Br. J. Pharmacol. 180, 797- 812. https://doi.org/10.1111/bph.15573.  
57. Bovill, J.G., Sebel, P.S., Waqier, A., and Rog, P. (1982). ELECTROENCEPHALOGRAPHIC EFFECTS OF SUFENTANIL ANAESTHESIA IN MAN. Br. J. Anaesth. 54, 45- 52. https://doi.org/10.1093/bja/54.1.45.  
58. Chi, O.Z., Sommer, W., and Jasaitis, D. (1991). Power spectral analysis of EEG during sufentanil infusion in humans. Can. J. Anaesth. 38, 275- 280. https://doi.org/10.1007/BF03007614.  
59. Smith, N.T., Dec- Silver, H., Sanford, T.J., Jr., Westover, C.J., Jr., Quinn, M.L., Klein, F., and Davis, D.A. (1984). EEGs during High- Dose Fentanyl- Sufentanil- or Morphine- Oxygen Anesthesia. Anesth. Analg. 63, 386- 393.  
60. Durand, S., Iyer, R., Mizuseki, K., De Vries, S., Mihalas, S., and Reid, R.C. (2016). A Comparison of Visual Response Properties in the Lateral Geniculate Nucleus and Primary Visual Cortex of Awake and Anesthetized Mice. J. Neurosci. 36, 12144- 12156. https://doi.org/10.1523/JNEUROSCI.1741- 16.2016.  
61. Assebo, I.E.J., Lepperd, M.E., Stavrinou, M., Nokkevangen, S., Einevoll, G., Hatting, T., and Fyhn, M. (2017). Temporal Processing in the Visual Cortex of the Awake and Anesthetized Rat. eNeuro 4, ENEURO.0059- 17.2017. https://doi.org/10.1523/ENEURO.0059- 17.2017.  
62. Hindriks, R., and Van Putten, M.J.A.M. (2012). Meanfield modeling of propofol- induced changes in spontaneous EEG rhythms. Neuroimage 60, 2323- 2334. https://doi.org/10.1016/j.neuroimage.2012.02.042.  
63. Hashemi, M., Hutt, A., and Sleigh, J. (2014). Anesthetic action on extra- synaptic receptors: effects in neural population models of EEG activity. Front. Syst. Neurosci. 8, 232. https://doi.org/10.3389/fnsys.2014.00232.  
64. Hashemi, M., Hutt, A., and Sleigh, J. (2015). How the cortico- thalamic feedback affects the EEG power spectrum over frontal and occipital regions during propofol- induced sedation. J. Comput. Neurosci. 39, 155- 179. https://doi.org/10.1007/s10827- 015- 0569- 1.  
65. Chemla, S., Roux, S., Reynaud, A., Chavane, F., and VanRullen, R. (2020). Revealing \(\alpha\) oscillatory activity using voltage- sensitive dye imaging in monkey V1. Preprint at bioRxiv. https://doi.org/10.1101/810325.  
66. Franks, N.P. (2008). General anaesthesia: from molecular targets to neuronal pathways of sleep and arousal. Nat. Rev. Neurosci. 9, 370- 386. https://doi.org/10.1038/nrn2372.  
67. Robinson, P.A., Rennie, C.J., Rowe, D.L., and O'Connor, S.C. (2004). Estimation of multiscale neurophysiologic parameters by electroencephalographic means. Hum. Brain Mapp. 23, 53- 72. https://doi.org/10.1002/hbm.20032.  
68. Robinson, P.A., Rennie, C.J., and Wright, J.J. (1997). Propagation and stability of waves of electrical activity in the cerebral cortex. Phys. Rev. E 56, 826- 840. https://doi.org/10.1103/PhysRevE.56.826.  
69. Robinson, P.A., Rennie, C.J., Wright, J.J., Bahramali, H., Gordon, E., and Rowe, D.L. (2001). Prediction of electroencephalographic spectra from neurophysiology. Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 63, 021903. https://doi.org/10.1103/PhysRevE.63.021903.  
70. Morrow, A., Turkovich, E., Sankaran, S., Pilipenko, A., and Samaha, J. (2026). Alpha- band echoes evoked by contrast and luminance changes emerge in and travel out from early visual cortex. J. Vis. 26, 16. https:// doi.org/10.1167/jov.26.1.16.  
71. Luo, C., Brüers, S., Berry, I., VanRullen, R., and Reddy, L. (2021). Tentative fMRI signatures of perceptual echoes in early visual cortex. Neuroimage 237, 118053. https://doi.org/10.1016/j.neuroimage.2021.118053.  
72. Foxe, J.J., and Snyder, A.C. (2011). The role of alpha-band brain oscillations as a sensory suppression mechanism during selective attention. Front. Psychol. 2, 1-13. https://doi.org/10.3389/fpsyg.2011.00154.  
73. Sauseng, P., Klimesch, W., Stadler, W., Schabus, M., Doppelmayr, M., Hanslmayr, S., Gruber, W.R., and Birbaumer, N. (2005). A shift of visual spatial attention is selectively associated with human EEG alpha activity. Eur. J. Neurosci. 22, 2917-2926. https://doi.org/10.1111/j.1460- 9568.2005.04482. x.  
74. Sauseng, P., Klimesch, W., Gerloff, C., and Hummel, F.C. (2009). Spontaneous locally restricted EEG alpha activity determines cortical excitability in the motor cortex. Neuropsychologia 47, 284-288. https://doi.org/10.1016/j.neuropsychologia.2008.07.021.  
75. Romei, V., Brodbeck, V., Michel, C., Arredi, A., Pascual-Leone, A., and Thut, G. (2008). Spontaneous fluctuations in posterior alpha-band EEG activity reflect variability in excitability of human visual areas. Cereb. Cortex 18, 2010-2018. https://doi.org/10.1093/cercor/bhm229.  
76. Romei, V., Rihs, T., Brodbeck, V., and Thut, G. (2008). Resting electroencephalogram alpha-power over posterior sites indexes baseline visual cortex excitability. Neuroreport 19, 203-208. https://doi.org/10.1097/WNR.0b013e328214544c.  
77. Samaha, J., Gosseries, O., and Postle, B.R. (2017). Distinct Oscillatory Frequencies Underlie Excitability of Human Occipital and Parietal Cortex. J. Neurosci. 37, 2824-2833. https://doi.org/10.1523/JNEUROSCI.3413-16.2017.  
78. Hindriks, R., and van Putten, M.J.A.M. (2013). Thalamo-cortical mechanisms underlying changes in amplitude and frequency of human alpha oscillations. Neuroimage 70, 150-163. https://doi.org/10.1016/j.neuroimage.2012.12.018.  
79. Bukhtiyarova, O., Chauvette, S., Seigneur, J., and Timofeev, I. (2022). Brain states in freely behaving marmosets. Sleep 45, 2sac106. https://doi.org/10.1093/sleep/zsac106.  
80. Mendoza-Halliday, D., Major, A.J., Lee, N., Lichtenfeld, M.J., Carlson, B., Mitchell, B., Meng, P.D., Xiong, Y.S., Westerberg, J.A., Jia, X., et al. (2024). A ubiquitous spectroalmanir motif of local field potential power across the primate cortex. Nat. Neurosci. 27, 547-560. https://doi.org/10.1038/s41593-023-01554-7.  
81. Muller, L., Reynaud, A., Chavane, F., and Destexhe, A. (2014). The stimulus-evoked population response in visual cortex of awake monkey is a propagating wave. Nat. Commun. 5, 3675. https://doi.org/10.1038/ncomms4675.  
82. Muller, L., Chavane, F., Reynolds, J., and Sejnowski, T.J. (2018). Cortical travelling waves: Mechanisms and computational principles. Nat. Rev. Neurosci. 19, 255-268. https://doi.org/10.1038/nrn.2018.20.  
83. Davis, Z.W., Busch, A., Steward, C., Muller, L., and Reynolds, J. (2024). Horizontal cortical connections shape intrinsic traveling waves into feature-selective motifs that regulate perceptual sensitivity. Cell Rep. 43, 114707. https://doi.org/10.1016/j.celrep.2024.114707.  
84. Yu, H.H., and Rosa, M.G.P. (2010). A simple method for creating wide-field visual stimulus for electrophysiology: mapping and analyzing receptive fields using a hemispheric display. J. Vis. 10, 15. https://doi.org/10.1167/10.14.15.  
85. Rajan, R., Dubaj, V., Reser, D.H., and Rosa, M.G.P. (2013). Auditory cortex of the marmoset monkey - complex responses to tones and vocalizations under opiate anaesthesia in core and belt areas. Eur. J. Neurosci. 37, 924-941. https://doi.org/10.1111/enj.12092.  
86. Pachitariu, M., Steinmetz, N., Kadir, S., Carandini, M., and Harris, K. (2016). Fast and accurate spike sorting of high-channel count probes with KiloSort. Adv. Neural Inf. Process. Syst., 4455-4463.  
87. Lachaux, J.P., Rodriguez, E., Martinerie, J., and Varela, F.J. (1999). Measuring phase synchrony in brain signals. Hum. Brain Mapp. 8, 194- 208. https://doi.org/10.1002/(SICI)1097- 0193(1999)8:4%3C194::AID- HBM4%3E3.0. C0;2- C.  
88. Robinson, P.A., Rennie, C.J., and Rowe, D.L. (2002). Dynamics of largescale brain activity in normal arousal states and epileptic seizures. Phys. Rev. E 65, 041924. https://doi.org/10.1103/PhysRevE.65.041924.  
89. Abeysuriya, R.G., Rennie, C.J., and Robinson, P.A. (2015). Physiologically based arousal state estimation and dynamics. J. Neurosci. Methods 253, 55- 69. https://doi.org/10.1016/j.jneumeth.2015.06.002.  
90. Breakspear, M., Roberts, J.A., Terry, J.R., Rodrigues, S., Mahant, N., and Robinson, P.A. (2006). A Unifying Explanation of Primary Generalized Seizures Through Nonlinear Brain Modeling and Bifurcation Analysis. Cereb. Cortex 16, 1296- 1313. https://doi.org/10.1093/cercor/bhj072.  
91. Benson, N.C., Yoon, J.M.D., Forenzo, D., Engel, S.A., Kay, K.N., and Winawer, J. (2022). Variability of the Surface Area of the V1, V2, and V3 Maps in a Large Sample of Human Observers. J. Neurosci. 42, 8629-8646. https://doi.org/10.1523/JNEUROSCI.0690-21.2022.  
92. Fritsches, K.A., and Rosa, M.G. (1996). Visuotopic organisation of striate cortex in the marmoset monkey (Callithrix jacchus). J. Comp. Neurol. 372, 264-282. https://doi.org/10.1002/(SICI)1096- 9861(19960819)372:2%3C264::AID-CNE8%3E3.0.C0;2- 1.  
93. Missler, M., Eins, S., Merker, H.- J., Rothe, H., and Wolff, J.R. (1993). Pre- and postnatal development of the primary visual cortex of the common marmoset. I. A changing space for synaptogenesis. J. Comp. Neurol. 333, 41-52. https://doi.org/10.1002/cne.903330104.

## STAR \(\star\) METHODS

## KEY RESOURCES TABLE

| REAGENT or RESOURCE | SOURCE | IDENTIFIER |
| :--- | :--- | :--- |
| **Chemicals, peptides, and recombinant proteins** | | |
| Atropine sulfate | Troy Laboratories | Atrosite |
| Diazepam | Ceva Animal Health Pty Ltd | Pamlin |
| Alfaxalone | Jurox, Rutherford, Australia | Alfaxan |
| Dexamethasone | Troy Laboratories | Dexason |
| Sufentanil citrate | Janssen P/L | Sufenta Forte |
| Pancuronium bromide | Organon, Sydney, Australia | 2190101 |
| 1% Atropine sulfate Eye Drops | Aspen Pharma Pty Ltd | Atropt Eye Drop |
| 10% Phenylephrine hydrochloride eye drops | Bausch and Lomb | Minims |
| **Experimental models: Organisms/strains** | | |
| Adult common marmoset monkey (callithrix jacchus) | Australian National Primate Breeding and Research Facility (Gippsland, VIC) | N/A |
| **Software and algorithms** | | |
| MATLAB(R2021a) | Mathworks, Natick, Massachusetts, USA | https://www.mathworks.com/ |
| Neurostim Toolbox | https://github.com/klabhub/neurostim | N/A |
| Global Optimization Toolbox (MATLAB) | Mathworks, Natick, Massachusetts, USA | https://www.mathworks.com/help/gads/ |
| Wavelet Toolbox (MATLAB) | Mathworks, Natick, Massachusetts, USA | https://www.mathworks.com/products/ wavelet.html |
| KiloSort 2 | https://github.com/jamesjun/Kilosort2 | N/A |
| Phy Software | https://github.com/cortex-lab/phy/ | N/A |
| **Deposited data** | | |
| Custom Code and Data | osf.io/25axj | https://doi.org/10.17605/OSF.IO/25AXJ |

## EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS

Recordings were performed during acute experiments in two adult marmoset monkeys (callithrix jacchus, \(N = 2\) , male). All experimental procedures were approved by the Monash Animal Research Platform Animal Ethics Committee (approval #13419, 10/04/18 to 16/12/20) and carried out in accordance with the Australian Code of Practice for the Care and Use of Animals for Scientific Purposes.

Before the experiments, animals were housed in family groups, with additional visual and auditory access to other marmosets in different cages. Access to food and water was unrestricted and regular in- cage enrichment was provided. Additionally, the animals were allowed daily access to an outdoor enclosure. The well- being of all animals was regularly monitored by a trained veterinarian and additional care provided as needed.

Given the small sample \((N = 2)\) , the influence of sex on the present results cannot be addressed with our data. While the early visual processing dynamics are unlikely to differ significantly between sexes, this nonetheless limits the generalizability of our results to the wider population.

## METHOD DETAILS

## Surgical and experimental procedures

The preparation for electrophysiological studies of marmosets has been described previously. Briefly, injections of atropine \((0.2 \text{mg / kg}, \text{i.m.})\) and diazepam \((2 \text{mg / kg}, \text{i.m.})\) were administered as premedication, 30 min prior to the induction of anesthesia with alfaxalone (Alfaxan, \(10 \text{mg / kg}, \text{i.m.},\) Jurox, Rutherford, Australia), allowing a tracheotomy, vein cannulation and craniotomy to be performed. The animal received an intravenous infusion of pancuronium bromide \((0.1 \text{mg / kg};\) Organon, Sydney, Australia) combined with sufentanil \((6 \mu \text{g / kg};\) Janssen- Cilag, Sydney, Australia) and dexamethasone \((0.4 \text{mg / kg / h})\) , and was artificially ventilated with a gaseous mixture of nitrous oxide and oxygen (7:3). This regime ensures long- term anesthesia with less suppression of early response components in primary sensory areas, in comparison with isoflurane or barbiturates. The electrocardiogram and level of cortical spontaneous activity were continuously monitored. Administration of atropine \((1\%)\) and phenylephrine

hydrochloride \((10\%)\) eye drops resulted in mydriasis and cycloplegia. Appropriate focus and protection of the corneas from desiccation were achieved by means of hard contact lenses selected by streak retinoscopy.

A craniotomy was performed to allow access to the left occipital cortex for the implantation of a \(10 \times 10\) , 96- channel Utah array (1.5 mm in length, spaced at \(400 \mu m\) intervals, with platinum electrode sites, Blackrock Microsystems, Salt Lake City, USA). Extracellular neural data were recorded using a Cerebus System (Blackrock Microsystems, Salt Lake City, USA) and digitally sampled at \(30 \text{kHz}\) .

## Visual stimulation

Visual stimuli were generated in MATLAB (The Mathworks, Inc.) and presented using Neurostim (https://github.com/klabhub/neurostim) on a Display++ LCD monitor (Cambridge Research Systems, Rochester, UK) with a resolution of \(1920 \times 1080\) px, running at \(120 \text{Hz}\) . The stimulation procedure followed the design established in, \(^{10}\) with minor adaptations to monkey neurophysiology. The stimulus was a circular patch of uniform luminance (diameter between 3 and 4 deg, adjusted online to cover the receptive field (RF) of the population) presented on a black background. The patch's luminance on each trial followed a white noise sequence over time between black and white (duration: 10 s) with a luminance change on every frame (120 fps, allowing for stimulus frequencies up to the Nyquist frequency of \(60 \text{Hz}\) ). Individual sequences were repeated pseudo- randomly between blocks of 40 or 20 unique trials (Monkey 1: one session of 40 sequences x 8 repetitions, two sessions of \(20 \times 8\) ; Monkey 2: two sessions of \(40 \times 8\) ). We found no effect of sequence repetition on any of the measures reported here and thus collapsed data from all recorded trials \((n = 640)\) in both monkeys. The position of the patch was chosen to cover best the population RF of the recorded units (determined online, adjustments made between recording sessions to account for fixational drift), and was always in the lower right visual field.

## LFP signal processing

Raw neural data were recorded at 30k samples/sec. To isolate the LFP, the broadband signal was low- pass filtered using an FIR filter with a cutoff- frequency of \(200 \text{Hz}\) . For all analyses involving correlation with the stimulus, the signal was low- pass filtered below the maximum temporal frequency contained in the stimulus sequence (i.e., \(60 \text{Hz}\) ) and then resampled to the time vector of frame presentation times on each trial. Instantaneous phase information was extracted from both signals (stimulus and LFP) by applying a continuous wavelet transform (MATLAB function 'cwt', using the analytic Morlet- wavelet with 10 voices per octave) to the preprocessed data.

## Analysis of spiking activity

Spiking clusters were initially classified from the continuous data using the unsupervised KiloSort 2 algorithm. \(^{86}\) The identified clusters were manually curated and flagged as either noise, multi- unit or single- unit neural signals using the Phy software (developed by Cyrille Rossant; https://github.com/cortex- lab/phy/). Our analysis did not rely on a strict isolation of single units. Therefore, we included all clusters, regardless of whether they were classified as multi- or single- unit. Spike sorting was performed on all data for each monkey, i.e., after concatenating the two recording sessions.

## Steady-state LFP responses

To quantify the steady- state response of the V1 LFP activity to the stimulus, we computed the impulse response function (IRF) \(^{10}\) :

\[\text{IRF}(I) = \sum_{t = 1}^{N_t} \text{Stim}(t) \cdot \text{LFP}(t + I) \quad (Equation 1)\]

where \(t\) is time \((1 \ldots N_t)\) and \(l\) denotes the lag between the stimulus and the LFP. Both signals were z- scored at the trial- level before cross- correlation. The IRF was computed separately for each electrode channel and trial, then subsequently averaged across trials.

Since the IRF reflects the absolute correlation in the time domain between the two signals (i.e., amplitude and phase) we also computed an isolated index of the phase- coupling, as follows:

\[\begin{array}{r}S(l,f) = \frac{1}{N_k}\sum_{k = 1}^{N_k}\frac{1}{(N_t - l)}\sum_{t = 1}^{N_t - l}g^{(i(\phi_{\mathrm{IP}}(t + l,f) - \phi_{\mathrm{stim}}(t)))} \end{array} \quad (Equation 2)\]

where \(\phi_{x}(t,f)\) is the instantaneous phase of signal \(x\) at time \(t\) and frequency \(f\) . For each lag \(l\) between LFP and stimulus, the phase differences between the two signals are averaged over time \((t, 1 \ldots N_t)\) , and trials \((k, 1 \ldots N_k)\) , as vectors of unit length. The resulting spectrum in \(S\) is complex- valued where the magnitude is the phase- locking value \((\text{PLV}, i^S)\) of the phase- difference between the two signals. The PLV is in the range zero to one, indicating random and perfect coupling to the stimulus, respectively. The phase angle of \(S\) at each bin represents the average phase difference at that lag and frequency.

For all analyses on the steady- state response (IRF and phase- coupling), the first \(250 \text{ms}\) following sequence onset in each trial were excluded to avoid an influence of the phasic sequence- onset response on the results. Units were excluded from the analysis if their mean firing rate did not exceed \(2.5 \text{spk/sec}\) either during the baseline- (within \(1 \text{s}\) before sequence onset) or the steady- state time- window \((>250 \text{ms}\) after sequence onset).

## Steady-state spiking responses

We quantified the impulse response for each spiking unit by computing the spike- triggered average (STA) stimulus luminance:

\[STA(l) = \frac{1}{N_t}\sum_{i = 1}^{N_t}Sim(t_i - l) \quad (Equation 3)\]

where \(i\) indexes spikes \((1\ldots N_t)\) \(t_i\) is the corresponding spike time and \(l\) is lag.

To quantify phase coupling to the stimulus, for a given unit, we computed the angular mean of the spike- triggered stimulus phase, as follows:

\[PLV(l,f) = \left|\frac{1}{N_k}\sum_{k = 1}^{N_k}\frac{1}{N_l}\sum_{i = 1}^{N_l}e^{i\nu_{stim}(t_i - l,f)}\right| \quad (Equation 4)\]

Here, the phase- locking value \(PLV(l,f)\) represents the consistency with which the spikes \((i, 1\ldots N_t)\) of the cluster followed a certain stimulus phase. It is computed, at each frequency bin \(f\) , from the angular sum of stimulus phases \(\nu_{stim}\) preceding each spike (occurring at time \(t_i\) ) by lag \(l\) , averaged over trials \((k, 1\ldots N_k)\) .

## Thalamocortical model

We used an established dynamical model of the geniculo- cortical pathway \(^{58,88}\) to model our V1 LFP data. This model has been extensively studied and shown to reproduce diverse features of the human EEG at rest (notably intrinsic alpha activity) and during stimulation \(^{20,21,67,88}\) as well as the dynamics during seizures. \(^{90}\)

We present only a brief summary of the model equations here, for a detailed derivation we refer to the original publications (see also \(^{18}\) for a comparison of this model with other models of the alpha rhythm). The model consists of four neuronal populations: the excitatory (e) and inhibitory (i) populations in V1, the LGN (denoted s for specific relay) and the thalamic reticular nucleus (TRN) (r). Each population a is described by a mean potential \(V_a\) which translates to an output firing rate through the sigmoidal transfer function S (parameters shared between all populations):

\[S(V_a) = \frac{Q_{max}}{1 + \exp\left(-\frac{V_a - \theta}{\sigma'}\right)} \quad (Equation 5)\]

where \(Q_{max}\) is the maximum rate, and \(\theta\) and \(\sigma '\) are threshold and spread parameters, respectively. The potential \(V_a\) evolves as a function of all inputs to the population, following:

\[V_a = \sum_b V_{ab} \quad (Equation 6)\]

\[D_{ab}V_{ab}(t) = \nu_{ab}\phi_b(t - \tau_{ab}) \quad (Equation 7)\]

\[D_{ab} = \frac{1}{\alpha_{ab}\beta_{ab}}\frac{d^2}{dt^2} +\left(\frac{1}{\alpha_{ab}} +\frac{1}{\beta_{ab}}\right)\frac{d}{dt} +1 \quad (Equation 8)\]

Here, \(V_{ab}\) denotes the potential corresponding to the input from population \(b\) to \(a\) , \(\phi_b\) is the firing rate of \(b\) , \(\nu_{ab}\) and \(\tau_{ab}\) are, respectively, the synaptic weight and delay corresponding to that connection. The parameters \(\alpha_{ab} - 1\) and \(\beta_{ab} - 1\) describe the decay and rise times of the postsynaptic potential.

The model architecture (illustrated in the corresponding Results Figure 3A) comprises bilateral connections between LGN and TRN, LGN and V1, unilateral feedback from V1 to TRN, and intracortical connectivity between the two populations in V1. The visual stimulus sequence is added as an excitatory input (subscript \(n\) ) into LGN.

We follow Roberts & Robinson \(^{20}\) in setting the time constants of all connections equal (parameters \(\alpha\) , \(\beta\) ) except the inhibitory TRN- LGN connection, which is dominated by slower dynamics. Furthermore, the intracortical connectivity is simplified by assuming identical receiving connectivity for both populations, leading to coupled population potentials \(V_i = V_a\) (see \(^{20,25}\) ). All connections between thalamus and cortex share the same delay \(\tau_1\) , the input into LGN is delayed by \(\tau_0\) and all other delays are zero. The resulting equations for the full model are:

\[D_{a}V_{a}(t) = \nu_{a}\phi_{a}(t) + \nu_{a}\phi_{a}(t) + \nu_{a}\phi_{a}(t - \tau_{1}) \quad (Equation 9)\]

\[D_{a}V_{r}(t) = \nu_{ra}\phi_{a}(t - \tau_{1}) + \nu_{ra}(t) \quad (Equation 10)\]

\[V_{a}(t) = V_{sa}(t) + V_{ar}(t) + V_{sn}(t) \quad (Equation 11)\]

\[D_{a}V_{sa}(t) = \nu_{sa}\phi_{a}(t - \tau_{1}) \quad (Equation 12)\]

\[D_{s}V_{sn}(t) = \nu_{sn}\Phi_{n}(t - \tau_{0}) \quad (Equation 13)\]

\[D_{sr}V_{sr}(t) = \nu_{sr}\Phi_{r}(t) \quad (Equation 14)\]

The firing rate of the excitatory cortical population is given by:

\[\left[\frac{1}{\gamma_{e}^{2}}\frac{d^{2}}{dt^{2}} +\frac{2}{\gamma_{e}}\frac{d}{dt} +1\right]\Phi_{e}(t) = S[V_{e}(t)] \quad (Equation 15)\]

where \(\gamma_{e}\) is a damping parameter reflecting propagation of activity along cortico- cortical (horizontal) fibers (see \(^{20}\) ). For all other populations, this parameter is set to infinite, leading to:

\[\Phi_{a}(t) = S[V_{a}(t)]\quad for a = i,s,r \quad (Equation 16)\]

Model simulations were performed by driving the network with random white noise sequences (simulating those used in the physiological experiment), with mean input rate \(\langle \Phi_{n}\rangle = 18 \mathrm{~s}^{- 1}\) and standard deviation \(\sigma_{n} = 5 \mathrm{~s}^{- 1}\) , in one continuous sequence of 60 s duration (90 s for the IRF fits). For a given simulation, the impulse response of the model was estimated by cross- correlating the V1 mean potential \(V_{e}\) with the stimulus input (see (1) above) and inverting the sign of the resulting function (accounting for the opposite polarity between the recorded extracellular field and modeled mean intracellular potential). The first second of each simulation was excluded from the cross- correlation to limit the analysis to a stable steady- state.

## Model fitting of marmoset IRFs

Model parameters were fit to the experimentally observed IRFs from both monkeys separately. This was done using a pattern search algorithm (MATLAB function 'patternsearch') over a defined range of free parameters (Table 1). For each iteration, the model's IRF was computed (as described above) and compared to the observed IRF, after normalization of both signals to the peak, using the loss function:

\[L = \log \left(\frac{\|\hat{y}_t - y_t\|}{\|\hat{y}_t\| + \|y_t\|}\right) + \lambda \log \left(1 - \langle \mathfrak{N}(C_{y_t,\hat{y}_t}(s,t))\rangle_{st}\right) \quad (Equation 17)\]

Here, L is to be minimized, \(\hat{y}\) and \(y\) are the predicted and observed IRF, respectively, t indexes (lag- t) time, \(\lambda = 0.7\) is a weighting factor, and \(C_{y_t,\hat{y}_t}(s,t)\) is the wavelet- cross- spectrum between the two IRFs, given by:

\[C_{y_t,\hat{y}_t}(s,t) = W_{y_t}(s,t)W_{\hat{y}_t}^*(s,t) \quad (Equation 18)\]

where \(W_{s}(s,t)\) is the complex- valued wavelet- transform of signal \(x\) over scales \(s\) and lags \(t\) , and \(W^{*}\) denotes the complex conjugate of \(W\) . The first term in (17) minimizes the difference between the two IRFs in the time- domain (normalized RMSE), while the second term maximizes similarity in the spectral domain (in- phase). The value for \(L\) was evaluated over a time- window between \(- 50\) and 350 ms lag.

Given the high dimensionality of the parameter space and the model's nonlinear behavior, reliable convergence of the pattern search algorithm can be difficult to control. We therefore performed the fitting in 20 runs, from which the best fit was ultimately selected. For each run, the starting point for the algorithm was chosen as the previous best fit, with some noise added to all parameter values. Specifically, for a given parameter \(\rho\) (normalized to the range between 0 and 1, representing the minimum and maximum of the parameter range, respectively), the new starting value \(\rho^{*}\) on run \(k\) was determined as follows:

\[\rho_{k}^{*} = (1 - w)\rho_{k - 1}^{*} + wx \quad (Equation 19)\]

\[with x\sim \left\{ \begin{array}{ll} \text{Beta}\left(2,\frac{1}{\rho_{k - 1}^{*}}\right),\rho_{k - 1}^{*}< 0.5\\ \text{Beta}\left(\frac{1}{\rho_{k - 1}^{*}},2\right),\rho_{k - 1}^{*}\geq 0.5 \end{array} \right. \quad (Equation 19)\]

Here, \(\rho_{k - 1}^{*}\) is the value for \(p\) from the best fit for runs 1 ... (k- 1) and \(w = 0.5\) is an update weight.

Our goal was not to estimate specific values for individual parameters, but to assess qualitatively whether the model could explain the observed dynamics. We therefore included a broad range of free parameters in the fitting, namely all synaptic weights, the two delays \((\tau_{0}, \tau_{r})\) and post- synaptic decay parameters \((a, a_{s\theta})\) . Fixed parameters were adopted from previous investigations. \(^{20,67,80}\) The only parameter value that we modified specifically to the marmoset model is the cortical damping \(\gamma_{e}\) , representing the ratio of cortico- cortical (excitatory) conduction velocity and axonal range. We adapted this to the smaller size of the marmoset brain by applying a scaling factor to the axonal range, derived from best estimates of the V1 surface area in both species (human: 25.8 cm \(^{2}\) , \(^{91}\) marmoset: 4 cm \(^{2}\) , \(^{92,93}\) resulting in a distance scaling factor of approx. 0.39). While

this is a very coarse approximation, we found that the impact of this parameter on our results is indeed negligible within a broader range of values.

## Comparison of model IRFs to human EEG responses

We used previously published data<sup>17</sup> from two subjects to illustrate qualitative similarities of the model- derived IRFs with the EEG. The experimental procedure is described in detail in the original study (presented data are from the pre- deprivation baseline sessions in experiment 1) and closely follow the original perceptual echo paradigm.<sup>10</sup> In brief, subjects were presented with a circular isoluminant patch (diameter \(5.5^{\circ}\) ) positioned in the upper hemifield at \(7^{\circ}\) from a central fixation dot. The luminance of the patch followed a random white noise sequence on every trial, each lasting 6.25 s. Subjects covertly monitored the patch for the appearance of a target square. Data pre- processing followed a standard pipeline, including band- pass filtering between 2 and 60 Hz. IRFs were computed for each electrode in the same way as described above (Equation 1). All experiments were approved by the local Ethics Committee (Psychology Department, University of Marburg), and the participants gave written informed consent before the experiment.

## QUANTIFICATION AND STATISTICAL ANALYSIS

Statistical testing was performed at the level of contacts (recorded channels) for all LFP results, separately for each monkey, with Bonferroni correction for multiple testing. Statistical tests on spiking units were performed after pooling units from both monkeys. Sample sizes (contacts/units) are indicated in the main text or figure captions where applicable. The threshold for statistical significance was set at \(p < 0.05\) (one- sided) or \(p < 0.025\) (two- sided).

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
