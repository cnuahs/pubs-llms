```
@article{chen2026optical,
  title={Optical Imaging of Electrically Evoked Visual Signals in Cats: II. ICA "Harmonic Filtering" Noise Reduction},
  author={Spencer C. Chen and Yan T. Wong and Luke E. Hallum and Norbert B. Dommel and Shaun L. Cloherty and John W. Morley and Gregg J. Suaning and Nigel H. Lovell},
  journal={29th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2007},
  pages={3380-3383},
  doi={10.1109/iembs.2007.4353056},
  url={https://ieeexplore.ieee.org/document/4353056}
}
```

---

# Optical Imaging of Electrically Evoked Visual Signals in Cats: II. ICA "Harmonic Filtering" Noise Reduction

Spencer C. Chen, Student Member, IEEE, Yan T. Wong, Student Member, IEEE, Luke E. Hallum, Norbert B. Dommel, Student Member, IEEE, Shaun L. Cloherty, Member, IEEE, John W. Morley, Gregg J. Suaning, Member, IEEE, Nigel H. Lovell, Senior Member, IEEE

Abstract—Optical imaging of intrinsic signals (OIS) is a tool for visualizing differential areas in the primary visual cortex devoted to visual functions such as ocular dominance and spatial orientation preferences. The OIS methodology was employed to verify visual cortical response to a retinal vision prosthesis whereby electrical stimulation is applied to the neural retina in order to elicit visual percepts. However, OIS recording is quite susceptible to cardiac and respiratory artifact, and inherent noise related to the measurement process. This complicates the identification of evoked signals using standard ensemble averaging based image processing. We therefore developed an independent component analysis (ICA) "harmonic filtering" technique to improve the signal- to- noise ratio. This technique is capable of reducing noise components, highlighting response signals to visual and electrical stimuli. Particularly, we demonstrated extraction of an ocular dominance map due to corneal stimulation and localized cortical activation due to intravitreal stimulation.

## I. INTRODUCTION

A n electronic retinal prosthesis is currently being developed by various research groups around the world. Advancements in research have been encouraged by trials of rudimentary prototypes that have elicited sensations of light in human recipients [1- 3]. In order to determine whether our experimental device successfully elicited a visual response in anesthetized cats, an optical imaging of intrinsic signals (OIS) technique was employed on the primary visual cortex of the animals to capture cortical activity correlating with electrical stimulation of the retina.

The OIS technique has been widely used in visual neuroscience, demonstrating functional maps such as differential cortical activation due to ocular dominance and spatial orientation of the stimuli [4]. In our companion paper [5], we described the effectiveness of the OIS technique in

imaging electrically evoked responses in the primary visual cortex, with electrical stimulation applied using our group's epiretinal microelectronic neurostimulator [6]. However, the extraction of signals from the OIS recording was complicated by relatively large noise from physiological (respiratory, cardiac, etc.) and external sources (lighting, camera, etc.). It is not uncommon to observe a signal- to- noise ratio (SNR) of 1:1000 in the raw images. Standard OIS processing relies heavily on ensemble averaging, for which Sirovich and Kaplan estimated that it may require up to 2500 recording in order to achieve a 1:1 SNR [7]. In this paper, we describe a novel technique supplementing the standard processing and demonstrate its effectiveness in noise reduction in a practical application.

Many investigators have proposed different techniques to improve OIS signal identification: blind source separation (BSS) [7- 10], and temporal periodic filtering [11], etc. We were particularly attracted to the BSS techniques [7- 10] employed by Sirovich et al. Blind source separation techniques make no a priori assumptions about the characteristics of the signals of interest such as their spectral content (i.e. "blind"), so that signal extraction is solely based on sources of information such as the correlation with the known stimulus duration.

We focused on one particular BSS methodology namely independent component analysis (ICA) [12, 13]. ICA decomposes an image series \(I[\mathbf{x},t]\) into components in \(\mathbf{x}\) (spatial domain) and \(t\) (temporal domain) as follows:

\[I[\mathbf{x},t] = \sum_{i}A_{i}[t]P_{i}[\mathbf{x}] \quad (1)\]

where the maximum number of components is equal to the dimensionality of \(\mathbf{x}\) or \(t\) , whichever is smaller. This technique is often described in light of a 'cocktail party' problem such that separation of unrelated voices from a noisy mixture is required. The decomposition seeks statistically independent and non- Gaussian components by maximizing a measure of the components 'joint entropy'; that is, the ICA components are sought so that mutual information is minimized.

Our ICA analysis approach builds on work by Sornborger et al. [8- 10]. By concatenating matching image sequences of the target tissue responding to the same stimulus condition, Sornborger et al. constructed a stacked sequence in the temporal domain (t). If the signal of interest does exist in the captured data, then it must appear in a fixed periodic fashion in the stack corresponding to the periodicity of the original

sequence length. Further, statistics were used to identify frequency components that were significantly different from the background noise. We refer to this technique as "harmonic filtering" (HF). Sornborger et al. demonstrated the effectiveness of this routine in optical imaging of the cat primary visual cortex [8, 10] and of the mouse heart [9].

Sornborger et al. applied HF in the principle component analysis (PCA) space of the image stack. This is a decomposition technique similar to ICA, except that resultant components are linearly independent to each other (orthogonal) instead of statistically independent. We believe that ICA may be a better basis for identifying the desired signals since there is no prerequisite for physiological signals to be orthogonal to each other as per PCA decomposition. Applying HF in the ICA space, we showed that this technique is an effective supplement to standard ensemble averaging in removing artifacts, and highlighting signal patterns from a noisy background.

## II. METHODOLOGY

### A. Animal Preparation

Adult cats aged 5- 12 months were anesthetized before undergoing craniotomy and exposure of the primary visual cortex. Details of the animal preparation are presented in [5]. All procedures were carried out in accordance with the National Health and Medical Research Council of Australia guidelines for animal experimentation, and approved by the University of New South Wales Animal Ethics Committee.

### B. Optical Imaging Apparatus

The optical imaging was performed on the primary visual cortex of the anesthetized cats. The apparatus was built in- house, based on a description provided in [4] and [14]. It consisted of a 12- bit CCD camera (CoolSnap EZ, Photometrics, USA), a 50- 50 mm tandem- lens system, and light- emitting diodes at \(530\mathrm{nm}\) or \(615\mathrm{nm}\) for illumination.

### C. Visual Stimulation Recording

Drifting square gratings at 0.25 cycles per degree spatial frequency and 2 cycles per second velocity were displayed in the visual field of the animals. Four orientations at \(0^{\circ}\) (horizontal), \(45^{\circ}\) , \(90^{\circ}\) (vertical) and \(135^{\circ}\) were used during the experiment for evoking orientation preference maps in the primary visual cortex. For ocular dominance, images were captured with one or the other eye covered. In between stimuli, animals were shown a uniform gray background.

During the recording, the camera was focused at \(400 - 800\mathrm{um}\) below the cortical surface, and imaged at \(4 - 8\mathrm{Hz}\) . For each recording, \(15 - 40\mathrm{s}\) of data was captured, during which the visual stimulus was presented for \(2 - 6\mathrm{s}\) subsequent to a pre- stimulus recording period. One such recording is referred to as an image "sequence". We recorded sequences for each condition repeated several times, constituting one dataset.

### D. Electrical Stimulation Recording

Optical imaging recording was also made while electrically stimulating at the cornea and in the intravitreal space of the animal. Image collection was made similar to that for visual stimuli. Details regarding the stimulation setup are presented in [5].

### E. Image Processing

The desire is to arrive at a difference map between two stimulus conditions, such as showing ocular dominance or orthogonal spatial orientation preferences.

1) Preprocessing: Each sequence \(I_{t}\big[\mathbf{x},t\big]\) , indexed by \(k\) , was normalized by subtracting the mean of the "pre-stimulus" images \(\rho_{k}\big[\mathbf{x}\big]\) from all the images, obtaining:

\[\begin{array}{l}{\widetilde{I}_{k}\big[\mathbf{x},t\big] = I_{k}\big[\mathbf{x},t\big] - \rho_{k}\big[\mathbf{x}\big]}\\ {\rho_{k}\big[\mathbf{x}\big] = \frac{1}{R}\sum_{t = 0}^{k - 1}I_{k}\big[\mathbf{x},t\big]} \end{array} \quad (2)\]

where the stimulus was applied at \(t = R\) . This process corrects for a slowly fluctuating image baseline.

2) Temporal Stacking: An image stack \(S\big[\mathbf{x},t\big]\) was formed by concatenating sequences in the time domain \((t)\) . So that the difference map would exhibit itself in a periodic fashion in the stack, we alternated between sequences from two stimulus conditions \(\widetilde{I}_{1,k}\big[\mathbf{x},t\big]\) and \(\widetilde{I}_{2,k}\big[\mathbf{x},t\big]\) such that:

\[\begin{array}{l}{S\big[\mathbf{x},2kT + t\big] = \widetilde{I}_{1,k}\big[\mathbf{x},t\big]}\\ {S\big[\mathbf{x},(2k + 1)T + t\big] = \widetilde{I}_{2,k}\big[\mathbf{x},t\big]} \end{array} \quad (4)\]

where \(T\) is the number of frames in one sequence. The difference map was expected to correlate to a period of \(2T\) .

3) ICA Decomposition: Decompositions were performed in Matlab (R2006b, Mathworks Inc., USA) using the FastICA toolbox [13]. The image stack \(S\big[\mathbf{x},t\big]\) was decomposed as per (1):

\[S\big[\mathbf{x},t\big] = \sum_{i\in I}A_i\big[t\big]P_i\big[\mathbf{x}\big] \quad (6)\]

Now, we assumed that if an ICA component \(P_{i}\big[\mathbf{x}\big]\) contains information of the difference map, then the power spectrum of its corresponding \(A_{i}\big[t\big]\) should register statistically significant spectral components at a fundamental frequency of \(1 / 2T\) or in its odd- numbered harmonics.

4) Harmonic filtering: HF retains statistically significant harmonics from the spectral power estimates of the time series data based on Thomson's adaptive multitaper approach [15]. The \(F\) -distribution was used to determine the statistical significance of spectral components against Gaussian distributed noise [16]. Sornborger et al. [8-10] used \(\alpha = 1 - 1 / N\) significance level for filtering, where \(N\) is the length of the time series data. This criterion rejects spectral components with at least one spurious data point. In this paper, we used a more relaxed \(\alpha = 1 - 2 / N\) to allow for spectral components that exist only under one stimulus condition but not in the other condition.

HF, denoted as \(\mathrm{H}_{\alpha}\{\bullet \}\) , was performed on each \(A_{i}[t]\) by examining the estimated power spectra. \(A_{i}[t]\) with statistically significant harmonics of interest were retained to form a post- filtered subset \((j\in \mathbf{J},\mathbf{J}\subseteq \mathbf{I})\) . A post- filtered stack \(\hat{S} [\mathbf{x},t]\) was reconstructed:

\[\hat{S} [\mathbf{x},t] = \mathrm{H}_{1 - 2 / N}\{\hat{S} [\mathbf{x},t]\} = \sum_{j\in \mathbf{J}}A_{j}[t]P_{j}[\mathbf{x}] \quad (7)\]

\(\hat{S} [\mathbf{x},t]\) was then segmented into individual sequences \(\hat{I}_{i,k}[\mathbf{x},t]\) and \(\hat{I}_{2,k}[\mathbf{x},t]\) , reversing the stacking routine.

5) Ensemble Differencing: Corresponding images from sequences of the same stimulus condition are averaged together to form an ensemble averaged sequence, one for each condition of interest. For example:

\[M_{1}[\mathbf{x},t] = \frac{1}{K}\sum_{k}I_{1,k}[\mathbf{x},t] \quad (8)\]

where \(K\) is the number of recorded sequences per condition. The subtraction between two ensemble- averaged sequences gives a difference sequence \(\Delta [\mathbf{x},t]\) of the relative cortical activities between the two different stimulus conditions:

\[\Delta [\mathbf{x},t] = M_{1}[\mathbf{x},t] - M_{2}[\mathbf{x},t] \quad (9)\]

Lastly, the difference map \(\overline{\Delta} [\mathbf{x}]\) should be maximal during stimulus presentation (between \(t = R\) and \(t = R + D\) ):

\[\overline{\Delta} [\mathbf{x}] = \frac{1}{D}\sum_{t = R}^{R + D - 1}\Delta [\mathbf{x},t] \quad (10)\]

We performed ensemble differencing on the baseline adjusted sequences \(\hat{I}_{k}[\mathbf{x},t]\) as per standard ensemble averaging based OIS processing (pre- filtered difference), and we compared the results against the ensemble difference of HF filtered sequences \(\hat{I}_{k}[\mathbf{x},t]\) (post- filtered difference).

## III. RESULTS

We obtained functional maps in the cat visual cortex in response to visual stimuli (Fig. 1), corneal stimulation (Fig. 3) and intravitreal stimulation (Fig. 4). In Fig. 1D, The columnar patterns illustrate cortical areas responding preferentially to \(45^{\circ}\) (dark) and \(135^{\circ}\) (light) gratings. Comparing pre- filtered (Fig. 1B) and post- filtered (Fig. 1C) difference images, we noticed a dramatic reduction in vascular artifacts. These vascular artifacts were a result of cortical motion due to cardiac pulsations ( \(\sim 3.3\mathrm{Hz}\) ) and respiratory movements ( \(\sim 0.4\mathrm{Hz}\) ). In Fig. 2, we saw a reduction of these motion components as a proportion of overall power (note: cardiac peaks were folded to \(\sim 1.7\mathrm{Hz}\) due to the Nyquist limit of the sampling rate); spectral power near \(0\mathrm{Hz}\) increased in proportion instead.

For corneal stimulation (Fig. 3), OIS response to stimulation of one eye was compared to the response from stimulation to the other eye. Compared to pre- filtered difference (Fig. 3B), HF was successful at further emphasizing the cortical areas responding preferentially to the left (dark) and right (light) eyes (Fig. 3C).

> **Image description.** A multi-panel scientific figure, labeled Fig. 1, displaying four grayscale functional maps (A, B, C, and D) representing results from visually evoked OIS (Optic Information Stream) recording. Each panel is a square map with a coordinate system indicated by numerical labels on the left and bottom axes, ranging from 1 to 7 vertically and 1 to 4 horizontally.
>
> The caption below the figure reads: "Fig. 1 Results from visually evoked OIS recording between 45° and 135°".
>
> The four panels exhibit distinct visual patterns:
>
> *   **Panel A:** This map shows a relatively smooth and diffuse pattern. A bright, elongated area is visible in the upper-left quadrant, while the rest of the map is characterized by a generally uniform, medium-gray tone.
> *   **Panel B:** This map displays a highly complex and textured pattern. It features numerous irregular, wavy, and bright lines and patches scattered across the entire field, suggesting a high degree of spatial variability or complex activity.
> *   **Panel C:** Similar to Panel B, this map shows a mottled and intricate pattern of varying gray levels. The texture is dense and irregular, though perhaps slightly less sharply defined than in Panel B.
> *   **Panel D:** This map is characterized by a highly structured, repetitive pattern. It consists of clear, distinct, parallel horizontal bands (stripes) of varying brightness that span the entire width of the map.
>
> Overall, the figure presents four different spatial representations of cortical activity, likely corresponding to different stimulus conditions or processing methods, as indicated by the varying degrees of smoothness, texture, and pattern complexity across the panels.

<center>Fig. 1 Results from visually evoked OIS recording between \(45^{\circ}\) and \(135^{\circ}\) gratings \((K = 20\) for each condition). A. The cortical area imaged (focused at \(\sim 400\mathrm{um}\) ). B. Difference map from standard processing. C. Difference map after HF. (same grayscale range as B) D. Spatial filtering of C to highlight columnar patterns. Axes are in millimeters. </center>

> **Image description.** A line graph titled "Fig. 2" displays the temporal power spectrum for two different data processing conditions: pre-filtered and post-filtered. The graph plots the "Proportion of Power" against "Frequency (Hz)".
>
> The Y-axis, labeled "Proportion of Power," uses a logarithmic scale, ranging from $10^{-4}$ to $10^0$ (or 1). The X-axis, labeled "Frequency (Hz)," ranges from 0 to approximately 2.5.
>
> Two data series are plotted:
> 1.  **Pre-filtered:** Represented by a light gray line.
> 2.  **Post-filtered:** Represented by a dark gray/black line.
>
> The legend in the upper right corner clearly identifies these two series.
>
> Both lines exhibit a general downward trend, indicating that the proportion of power decreases as the frequency increases. However, the two lines differ significantly in magnitude and spectral characteristics:
> *   The "pre-filtered" line consistently maintains a higher proportion of power across the entire frequency range compared to the "post-filtered" line.
> *   The "post-filtered" line appears more structured, showing distinct peaks and troughs (spectral features) between 0.5 Hz and 2.0 Hz, while the "pre-filtered" line is smoother.
>
> The visible text includes the figure label "Fig. 2" and the beginning of the caption: "Temporal power spectrum of the pre-filtered and post-filtered...".

<center>Fig. 2 Temporal power spectrum of the pre-filtered and post-filtered difference sequences from the same dataset as Fig. 1, calculated by summing the power spectrum from each pixel, normalized to total power. </center>

> **Image description.** This is a multi-panel scientific figure (Fig. 3) presenting four grayscale intensity maps, labeled A, B, C, and D, which represent results from an electrically evoked OIS (Optic Intensity Signal) recording. Each panel displays a square matrix of data, likely representing functional maps or power spectra, with spatial coordinates indicated by numerical labels.
>
> **General Layout and Structure:**
> The figure consists of four square panels arranged horizontally. Each panel is a grid with axes labeled 1, 2, 3, and 4 along both the horizontal (x-axis) and vertical (y-axis) dimensions, suggesting a 4x4 spatial or frequency resolution. The intensity within each panel is represented by grayscale, ranging from dark (low intensity) to bright (high intensity).
>
> **Detailed Panel Descriptions:**
> *   **Panel A:** This panel exhibits a smooth, radial intensity gradient. The highest intensity (brightest white) is concentrated in the center of the square, and the intensity gradually decreases towards the four corners and edges, forming a clear, smooth peak.
> *   **Panel B:** This panel displays a highly speckled and noisy pattern. The intensity is generally low across the entire map, but it is characterized by numerous scattered, bright, high-frequency points of activity against a darker background.
> *   **Panel C:** Similar to Panel B, this panel is also highly speckled and noisy. The distribution of bright points appears dense and somewhat uniform across the map, though perhaps slightly less intensely bright than the most prominent points in Panel B.
> *   **Panel D:** This panel shows a pattern that is more structured than the noise in B and C, but less smooth than the gradient in A. It features several distinct, localized patches or "blobs" of varying intensity, suggesting specific regions of localized activity or features within the recorded data.
>
> **Text and Labels:**
> The figure includes the following visible text:
> *   **Caption (Partial):** "Fig. 3 Results from electrically evoked OIS recording between left and" (The caption is cut off).
> *   **Panel Labels:** A, B, C, D (located in the top-left corner of each respective panel).
> *   **Axis Labels:** The numbers 1, 2, 3, and 4 are repeated along both the bottom and left edges of all four panels, serving as coordinate markers.

<center>Fig. 3 Results from electrically evoked OIS recording between left and right corneal electrodes \((K = 20\) for each condition). A. The cortical area imaged (focused at \(\sim 800\mathrm{um}\) ). B. Difference map from standard processing. C. Difference map after HF (same grayscale range as B). D. Spatial filtering of C to highlight columnar patterns. Axes are in millimeters. </center>

> **Image description.** A multi-panel scientific figure, labeled Fig. 4, displaying four grayscale spatial maps (A, B, C, and D) representing results from OIS (Optically Isolated Stimulus) recordings. Each panel shows a two-dimensional intensity map, likely representing cortical activity or feature detection, with a defined grid structure.
>
> **General Visual Characteristics:**
> *   **Format:** The image is composed of four square panels arranged horizontally.
> *   **Color Palette:** All panels utilize a grayscale palette, where darker areas indicate higher intensity or activity, and lighter areas indicate lower intensity.
> *   **Axes:** Each panel features a coordinate system defined by numerical labels. The vertical axis is labeled with integers 1 through 5, and the horizontal axis is labeled with integers 1 through 3. The caption indicates that the axes are measured in millimeters.
>
> **Detailed Panel Descriptions:**
> *   **Panel A:** This panel displays a relatively uniform and diffuse grayscale pattern. The intensity is generally moderate, with subtle, mottled variations across the map, but no sharp, highly localized features are visible.
> *   **Panel B:** This panel shows a significantly more complex and structured pattern compared to Panel A. It features several distinct, high-contrast, dark clusters or spots, indicating localized areas of high activity. The pattern is highly localized and appears more defined than in the other panels.
> *   **Panel C:** Similar to Panel B, this panel exhibits localized dark features. However, the clusters appear slightly more diffuse and less intensely concentrated than those in Panel B, suggesting a variation in the spatial distribution of activity.
> *   **Panel D:** This panel displays a pattern characterized by concentrated, dark regions. The features are localized, similar to B and C, but the overall background intensity appears lower, and the dark spots are tightly grouped, suggesting a specific, focused response.
>
> **Text and Context:**
> *   **Labels:** The panels are clearly labeled with capital letters A, B, C, and D.
> *   **Caption:** The visible text below the figure reads: "Fig. 4 Results from OIS recording between intravitreal stimulation and..." (The caption is truncated).
> *   **Interpretation:** Based on the context provided, these maps likely represent the functional activity of the cat visual cortex in response to different stimulus conditions (e.g., baseline vs. stimulated), with the differences in pattern complexity and localization (from A to D) illustrating the effect of the intravitreal stimulation on columnar patterns.

<center>Fig. 4 Results from OIS recording between intravitreal stimulation and no stimulation controls \((K = 20\) for each condition). A. The cortical area imaged (focused at \(\sim 800\mathrm{um}\) ). B. Difference map from standard processing. C. Difference map after HF (same grayscale range as B). D. Spatial filtering of C to highlight activation pattern. Axes are in millimeters. </center>

Finally, for intravitreal stimulation (Fig. 4), we compared data between sequences where electrical stimulation was delivered and control sequences where no stimulus was delivered. In contrast to a noisy pre- filtered difference image (Fig. 4B), HF was able to isolate localized areas responding to the intravitreal stimulation (Fig. 4C).

## IV. DISCUSSION

OIS recordings often contain prominent cardiac and respiratory induced vascular movement and lighting variations. There are also slow, unpredictable fluctuations luminance changes in the recorded images due to physiological activity uncorrelated to the stimulus, the health of the animal, and the state of anesthesia, etc. Standard OIS processing based on ensemble averaging cannot remove these various unwanted information; all luminance changes are retained in the averaged images, though their detrimental impact can be reduced with increasing number of samples. Often a large number of samples are required for averaging as these non- stimulus related luminance changes are quite often of the same order of magnitude if not greater than the actual response [7].

The HF technique seeks to retain luminance changes correlated with the stimulus onset through statistical analysis of the power spectrum, similar to the technique described by Kalatsky and Stryker [11]. In their approach, periodic bars of light were swept across the visual field of the animal. Functional maps were extracted by correlating cortical activity with the frequency of the sweeping bars. However, this technique suffers from two problems. Firstly, the need to capture sequences in the order of tens of minutes is quite demanding on the imaging system. This can be overcome by concatenating shorter sequences to identical stimuli in the form of temporal stacking described in this paper. The second problem is that to perform spectral analysis pixel by pixel with images containing more than \(100\mathrm{K}\) pixels can be computationally prohibitive. To resolve this, a method of reducing the dimensionality of the image sequence is required, and was readily provided in the form of PCA [8- 10] or ICA decomposition [12, 13].

In addition to dimensionality reduction, it is perhaps a reasonable assumption that the various sources of noise are uncorrelated to each other, and so are likely to exhibit themselves in separate ICA components. Having noise sources in separate components to the potential response increases the probability that they can be identified as uncorrelated to the stimulus. The effectiveness of HF is improved by the fact that the noise sources are better concentrated via ICA decomposition, and more easily identified. This was especially observed with vascular motion, which was reduced by and large in Fig. 1.

The current technique, however, is not without its drawbacks. The processing is a severe time consuming CPU and memory intensive process. (Processing of a single dataset on a 2.0 GHz Intel Xeon processor with 12 Gb of memory can take more than 24 hours at times.) Therefore in its current form, it cannot be used as an online processing tool for visualizing cortical activation patterns during the experiment. In addition, the stacking technique currently results in 'boundary' artifact due to the sudden change in image content between concatenated sequences. Further improvements are being made on the ICA HF routine to overcome these problems.

## V. CONCLUSION

Harmonic filtering is capable of improving the SNR of cortical activity patterns captured using the OIS methodology by identifying noise sources from ICA decomposed statistically independent components that do not exhibit statistically significant correlation to the applied stimulus. We demonstrated the effectiveness of this processing technique on visually and electrically evoked visual cortical response in anesthetized cats. We propose to apply this technique in further animal testing of our epiretinal microelectronic prosthesis design.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
