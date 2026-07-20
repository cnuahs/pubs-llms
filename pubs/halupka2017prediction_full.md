```
@article{halupka2017prediction,
  title={Prediction of cortical responses to simultaneous electrical stimulation of the retina},
  author={Kerry J. Halupka and Mohit N. Shivdasani and Shaun L. Cloherty and David B. Grayden and Yan Tat Wong and Anthony N. Burkitt and Hamish Meffin},
  journal={Journal of Neural Engineering},
  year={2017},
  volume={14},
  pages={016006},
  doi={10.1088/1741-2560/14/1/016006},
  url={https://iopscience.iop.org/article/10.1088/1741-2560/14/1/016006}
}
```

---

# Prediction of cortical responses to simultaneous electrical stimulation of the retina

Kerry J Halupka \(^{1,2,3}\) , Mohit N Shivdasani \(^{3,4}\) , Shaun L Cloherty \(^{1,5,6}\) , David B Grayden \(^{1,3,7}\) , Yan T Wong \(^{1}\) , Anthony N Burkitt \(^{1,3}\) and Hamish Meflin \(^{5,6}\)

\(^{1}\) NeuroEngineering Laboratory, Department of Electrical & Electronic Engineering, The University of Melbourne, VIC 3010, Australia \(^{2}\) National ICT Australia, Victoria Research Lab, The University of Melbourne, VIC 3010, Australia \(^{3}\) Bionics Institute, 384- 388 Albert St, East Melbourne, VIC 3002, Australia \(^{4}\) Department of Medical Bionics, The University of Melbourne, VIC 3010, Australia \(^{5}\) National Vision Research Institute, Australian College of Optometry, Carlton, VIC 3053, Australia \(^{6}\) Australian Research Council Centre of Excellence for Integrative Brain Function, Department of Optometry and Vision Sciences, The University of Melbourne, Melbourne, VIC 3010, Australia \(^{7}\) Centre for Neural Engineering, The University of Melbourne, VIC 3010, Australia

E- mail: kerry.halupka@gmail.com

Received 1 December 2015, revised 14 August 2016  Accepted for publication 24 August 2016  Published 30 November 2016

## Abstract

Objective. Simultaneous electrical stimulation of multiple electrodes has shown promise in diversifying the responses that can be elicited by retinal prostheses compared to interleaved single electrode stimulation. However, the effects of interactions between electrodes are not well understood and clinical trials with simultaneous stimulation have produced inconsistent results. We investigated the effects of multiple electrode stimulation of the retina by developing a model of cortical responses to retinal stimulation. Approach. Electrical stimuli consisting of temporally sparse, biphasic current pulses, with amplitudes sampled from a bi- dimensional Gaussian distribution, were simultaneously delivered to the retina across a 42- channel electrode array implanted in the suprachoroidal space of anesthetized cats. Visual cortex activity was recorded using penetrating microelectrode arrays. These data were used to identify a linear- nonlinear model of cortical responses to retinal stimulation. The ability of the model to generalize was tested by predicting responses to non- white patterned stimuli. Main results. The model accurately predicted two cortical activity measures: multi- unit neural responses and evoked potential responses to white noise stimuli. The model also provides information about electrical receptive fields, including the relative effects of each stimulating electrode on every recording site. Significance. We have demonstrated a simple model that accurately describes cortical responses to simultaneous stimulation of a suprachoroidal retinal prosthesis. Overall, our results demonstrate that cortical responses to simultaneous multielectrode stimulation of the retina are repeatable and predictable, and that interactions between electrodes during simultaneous stimulation are predominantly linear. The model shows promise for determining optimal stimulation paradigms for exploiting interactions between electrodes to shape neural activity, thereby improving outcomes for patients with retinal prostheses.

Keywords: multi- electrode stimulation, retinal prosthesis, white- noise analysis, suprachoroidal, animal model

(Some figures may appear in colour only in the online journal)

## Introduction

Retinal prostheses produce phosphenes by electrically stimulating surviving retinal neurons in patients with severe photoreceptor degeneration. Clinical trials have shown that retinal prostheses elicit useful perceptions, resulting in improvements in spatio- motor tasks (Barry et al 2012, Kotecha et al 2014, Stingl et al 2015) and reading (da Cruz et al 2013). However, spatial resolution with present devices is severely limited with the highest reported visual acuity achieved of 20/546 (Stingl et al 2013).

One strategy that shows promise to improve resolution is simultaneous stimulation of multiple electrodes. Interactions that occur when combinations of electrodes are stimulated simultaneously are capable of increasing the repertoire of visual percepts that can be elicited compared to conventional single- electrode stimulation. Simultaneous stimulation can activate groups of cells between electrodes (Dumm et al 2014), reduce current spread by using one or more local return electrodes (Cicione et al 2012, Habib et al 2013, Matteucci et al 2013), and elicit responses at the level of a single cell in vitro (Jepson et al 2014). Clinically, studies have mainly aimed to elucidate perceptual differences between sequential and simultaneous stimulation (Humayun et al 1999, Rizzo et al 2003, Auner et al 2008, Horsager et al 2010, Wilke et al 2011). Although these studies were limited to stimulation of electrodes in simple geometric patterns such as lines and squares with identical biphasic pulses on all electrodes, inconsistencies were reported regarding percept predictability and reproducibility.

It is clear that simultaneous stimulation is a promising strategy for eliciting useful percepts. However, the crucial next step in either reducing or harnessing electrode interactions is to investigate the predictability and reproducibility of responses to simultaneous stimulation, and gain a better understanding of how electrode interactions affect neural responses.

Here, we combine simultaneous stimulation of 42 suprachoroidal electrodes with multi- site recordings in the cat visual cortex, to demonstrate that electrode interactions at the level of the cortex are predominantly linear. Additionally, we show that a simple model comprised of a linear filter followed by a static nonlinearity (hereafter, linear- nonlinear (LN) model) can reliably predict neural spiking responses to several different simultaneous stimulation paradigms. We also demonstrate the ability of the same model to predict responses based on an alternative metric of cortical activity, namely, the power in the evoked responses. The predictive success of our model shows promise for efficiently determining optimal stimulation paradigms for shaping neural activity with a retinal prosthesis.

## Methods

Experiments were performed in eight normally- sighted, adult cats. All procedures were approved by the Bionics Institute Animal Research Ethics Committee (Projects 12/255AB and 14/304AB).

## Anesthesia and surgery

Cats were anesthetized with an initial dose of ketamine (intramuscular, \(20\mathrm{mgkg}^{- 1}\) ) and xylazil (subcutaneous, \(2\mathrm{mgkg}^{- 1}\) ). Anesthesia was maintained with an intravenous infusion of sodium pentobarbitone ( \(60\mathrm{mgkg}^{- 1}\mathrm{h}^{- 1}\) ) and Hartmanns solution (sodium lactate, \(2.5\mathrm{mlkg}^{- 1}\mathrm{h}^{- 1}\) ). Dexamethasone (intramuscular, \(0.1\mathrm{mgkg}^{- 1}\) ) and Clavulox (subcutaneous, \(10\mathrm{mgkg}^{- 1}\) ) injections were given daily to minimize brain swelling and infection. Vitals were continuously monitored throughout the experiment.

Details of the surgical implantation of the suprachoroidal array have been described previously (Shivdasani et al 2012). Briefly, a lateral incision through the sclera was performed to expose the choroid. The electrode array was then inserted into the suprachoroidal space via a pocket created between the sclera and choroid, and sutured into place (Villalobos et al 2012).

The suprachoroidal array (figure 1(a)) consisted of a flexible medical grade silicone substrate with 7 rows \(\times 3\) columns of platinum electrodes used in six experiments, and 7 rows \(\times 6\) columns of electrodes used in the remaining two experiments. Electrodes were \(600\mu \mathrm{m}\) in diameter arranged hexagonally with \(1\mathrm{mm}\) center- to- center spacing (Villalobos et al 2012).

The visual cortex contralateral to the implanted eye was exposed and penetrating microelectrode arrays (either \(6\times 10\) or \(6\times 6\) channels, \(1\mathrm{mm}\) length, \(400\mu \mathrm{m}\) spacing, Blackrock Micro., USA) were implanted (figure 1(b)). Evoked potentials (EPs) from the cortical surface in response to retinal stimulation were used to optimize the position of the implanted arrays (Cicione et al 2012, Dumm et al 2014). Neural signals were sampled at \(30\mathrm{kHz}\) (Cerebus Neural Processing System, Blackrock Microsystems, Salt Lake City, UT).

## White noise stimuli

Temporally sparse electrical pulses delivered simultaneously across the stimulating electrodes were used to characterize the system while responses were recorded in the visual cortex. The stimulus amplitude for each electrode was sampled from a bi- dimensional Gaussian distribution (hereafter, spatially white stimuli). To balance the effect of each electrode on cortical activation, the standard deviation of each Gaussian distribution was the activation threshold for that electrode.

Thresholds were acquired by stimulating each electrode individually with cathodic- first biphasic current pulses using a \(1\mathrm{ms}\) phase width, \(25\mu \mathrm{s}\) interphase gap, \(1\mathrm{Hz}\) presentation rate (the same pulse waveform was used for all electrical stimulation paradigms), and \(0–750\mu \mathrm{A}\) stimulus amplitude in \(50\mu \mathrm{A}\) steps. A spike- rate (or power) versus stimulus amplitude input- output function for each stimulating electroderecording channel combination was generated to which a sigmoid curve was fitted. For each sigmoid, the stimulus amplitude at \(50\%\) of the maximum response was defined as the threshold for that recording channel (Shivdasani et al 2012). The threshold for each stimulating electrode was chosen to be the lowest threshold over all recording channels

> **Image description.** A technical diagram consisting of two panels, (a) and (b), illustrating the schematic placement and dimensions of stimulating and recording arrays relative to anatomical structures in the eye and the visual cortex.
>
> **Panel (a): Stimulating Array in the Retina**
> This panel shows a schematic of the stimulating array positioned over the inferior retina. The overall shape of the retina is depicted as an irregular, curved area. A central dot labeled "Optic disc" is located on the left side of the diagram. The stimulating array is represented by a grid of small, red circular electrodes. The array is arranged in a rectangular pattern, with specific electrodes numbered (1, 7, 36, 42) highlighted in red. Various dimensions are indicated with dashed lines and text:
> *   The distance from the optic disc to the array is labeled "1 mm."
> *   The overall width of the array is labeled "0.8 mm."
> *   The diameter of the individual red electrodes is labeled "0.6 mm $\emptyset$."
> *   The text "Inferior retina" is positioned below the array.
>
> **Panel (b): Recording Array in the Visual Cortex**
> This panel illustrates the placement of the recording array within a cortical hemisphere. The cortical area is represented by a vertical, elongated shape. Two rectangular boxes, representing recording electrodes, are stacked vertically. These boxes are labeled with the numbers 1 (bottom) and 2 (top).
> *   The vertical distance between the two electrodes is labeled "4 mm."
> *   The horizontal distance between the electrodes is labeled "2.5 mm."
> *   Anatomical landmarks are labeled: "Mid-sagittal sulcus" is shown on the left, and "Lateral sulcus" is shown on the right.
> *   Orientation markers are provided at the bottom: "R" (rostral), "C" (caudal), "M" (medial), and "L" (lateral), with "Interaural zero" marked at the center.
>
> The diagrams use clear labels and measurements to define the precise spatial relationship and dimensions of the experimental arrays relative to the biological structures they are intended to interact with.

<center>Figure 1. (a) Schematic of stimulating array position and dimensions in relation to optic disc; electrode numbering for the four corner electrodes of the array are shown in red. (a) Schematic of the recording array placements in the hemisphere of the visual cortex contralateral to the implanted eye. R: rostral, C: caudal, M: medial, L: lateral. </center>

for which a sigmoid could be fit. All electrodes across the array were then stimulated simultaneously with charge- balanced waveforms using a mix of anodic- first and cathodic- first polarities with current amplitudes determined by the stimulus matrix. There were 3600 white noise stimulation patterns generated for each experiment; these were presented eight times, with the average of the responses on each recording channel used for analysis.

To investigate variability in cortical responses to repeated white noise stimuli, 60 repetitions of 30 different white noise patterns were presented in a randomized order in three of the experiments. The mean and standard deviation of the responses to each of these patterns was calculated.

## Oriented pattern stimuli  

Stationary, oriented electrical stimulus patterns were presented to test the prediction ability of the model with nonwhite stimuli. These patterns were electrical representations of sinusoidal gratings at six possible orientations \((0^{\circ}, 30^{\circ}, 60^{\circ}, 90^{\circ}, 120^{\circ},\) and \(150^{\circ}\) ), five spatial frequencies (ranging over approximately 1- 3 cycles per array length), and scaled by five stimulating currents (i.e., amplitudes of stimulating currents on each electrode were scaled by 175, 235, 295, 355, or \(415 \mu \mathrm{A}\) ). Patterns consisted of three main types: (i) mixed- phase first stimuli (figure 2(a)), where some electrodes on the array were stimulated with anodic- phase first biphasic pulses while others were stimulated with cathodic- phase first biphasic pulses; (ii) anodic- phase first stimuli (figure 2(b)), where all electrodes on the array were stimulated with anodic- phase first biphasic pulses; (iii) cathodic- phase first stimuli (figure 2(c)), where all electrodes on the array were stimulated with cathodic- phase first biphasic pulses. During each experiment, 30 different pattern stimuli were presented in a randomized order, with 10 repetitions of each pattern stimulus.

## Data pre-processing

Two measures were used to estimate the cortical activity: power in the evoked potential (EP power) that occurred within approximately \(20 \mathrm{ms}\) of the stimulus pulse and multi- unit activity (MUA) in the same time frame.

To estimate the power in the evoked responses, offline multi- taper spectral analysis (Thomson 1982, Mitra and Pesaran 1999) was used to filter the raw data (400- 1400 Hz, 2 tapers, taper length of \(4 \mathrm{ms}\) ). The log power was then calculated from \(3 \mathrm{ms}\) after the end of the stimulus pulse (to exclude the stimulus artifact) until \(20 \mathrm{ms}\) after the pulse with the power in the same band in the \(500 \mathrm{ms}\) prior to each stimulus subtracted to exclude spontaneous activity.

For the MUA analyses, stimulus artefacts were first removed (Heffer and Fallon 2008, Cicione et al 2012, Shivdasani et al 2012). Following band- pass filtering using a third- order Butterworth filter (300- 5000 Hz), multiunit spikes were detected as threshold crossings using a threshold of \(4 \mathrm{x}\) root- mean- square that was calculated within a \(60 \mathrm{s}\) moving time window. Typically, MUA occurred 3- 20 ms post- stimulus; however, in some instances, another burst of spikes followed at approximately \(30 \mathrm{ms}\) post- stimulus. Only the early component of spiking was analyzed as this is considered to be a result of direct stimulation of retinal ganglion cells (RGCs) and indirect activation of the inner retina, but not activation of the photoreceptors (Boinagrov et al 2014). The spontaneous spiking rate on each channel in the \(500 \mathrm{ms}\) prior to each stimulus was subtracted to account for variation in the

> **Image description.** A scientific figure consisting of three panels (a, b, and c) that illustrate example electrical stimulation patterns used as oriented electrical stimuli on an electrode array. The figure is accompanied by a grayscale legend and detailed captions.
>
> The overall layout features three square grids, each containing a 5x5 array of circular electrodes, totaling 25 electrodes per panel. The shading of these electrodes varies from solid black to solid white, representing different weighting or current amplitudes.
>
> **Grayscale Scale and Legend:**
> To the right of the panels, a vertical grayscale bar is labeled "Stimulus scale." This bar indicates the range of weighting, with white representing zero current amplitude (0) and black representing the strongest weighting (1). The scale also includes a value of -1 at the bottom.
>
> **Panel Descriptions:**
> *   **Panel (a) - Mixed-phase stimulus:** This panel displays a complex pattern of stimulation. It includes electrodes that are solid black, solid white, and several electrodes that are hatched with diagonal lines. According to the caption, the hatched electrodes represent those with cathodic-phase first stimuli. The pattern shows a mix of strong (black) and zero (white) weighting.
> *   **Panel (b) - Anodic-phase first only stimuli:** This panel shows a pattern where the overall weighting is generally lighter compared to panel (a). Many electrodes are solid white or light gray, indicating lower or zero current amplitude, consistent with an anodic-phase first stimulus pattern.
> *   **Panel (c) - Cathodic-phase first only stimuli:** This panel displays a pattern that is generally darker than panel (b). It features a higher concentration of solid black and dark gray electrodes, indicating stronger weighting and current amplitude, consistent with a cathodic-phase first stimulus pattern.
>
> **Text and Labels:**
> *   **Header Text:** The top left corner contains the journal citation: "J. Neural Eng. 14 (2017) 01600." The top right corner contains the author attribution: "K Halupa et al."
> *   **Figure Caption:** The caption below the panels provides a detailed explanation: "Figure 2. Example electrical stimulation patterns used as oriented electrical stimuli. The weighting of each electrode is represented by a grayscale, with black being the strongest weighting on the array (and thus the biggest current amplitude). White represents zero current amplitude. Electrodes with cathodic-phase first stimuli are hatched in white. (a) Mixed-phase stimulus. (b) Anodic-phase first only stimuli. (c) Cathodic-phase first only stimuli."

<center>Figure 2. Example electrical stimulation patterns used as oriented electrical stimuli. The weighting of each electrode is represented by a grayscale, with black being the strongest weighting on the array (and thus the biggest current amplitude). White represents zero current amplitude. Electrodes with cathodic-phase first stimuli are hatched in white. (a) Mixed-phase stimulus. (b) Anodic-phase first only stimuli. (c) Cathodic-phase first only stimuli. </center>

stimulus- independent activity. For both measures, responses on each channel were normalized by the maximum response recorded on the array to any presented stimulus.

## LN model

We developed a model to explain activity in the visual cortex in response to simultaneous multi- electrode stimulation of the retina. Cortical responses to spatially white electrical stimulation of the retina were used to characterize the model. The model consisted of two parallel spatial linear filters that provided estimates of the spatial tuning properties of each cortical recording channel, followed by two parallel static nonlinearities that accounted for nonlinear characteristics of neurons such as response thresholds and saturation.

This model is similar to well- established Gaussian white noise models developed to describe light responses in the retina (Chichilnisky 2001, Pillow et al 2005, Schwartz and Rieke 2011) and RGC responses to simultaneous stimulation of the retina (Maturana et al 2016). However, several key adaptions have been made to the established model to accommodate the different stimulation method (i.e. electrical versus light stimulation). First, as opposite phase pulses produce a differential response (Jensen and Rizzo 2006), the effects of both anodic- first and cathodic- first biphasic pulses were included separately in the model. Specifically, two different linear filters ( \(V_{\mathrm{P}}\) for net anodic- first and \(V_{\mathrm{N}}\) for net cathodic- first stimuli) and their associated static nonlinearities \((g_{p}\) and \(g_{N}\) ) acted on the input (S) separately (figure 3).

Our model also accommodated the larger range of response amplitudes present in our data and adjusted to describe response amplitude rather than spike probability. Additionally, we recorded cortical responses at multiple sites (up to 120) concurrently during stimulation and, as such, a LN model was fitted independently for each channel; thus, the index for each channel is omitted from the equations below for clarity.

An estimate of the activity (spike count or EP power) at each time \(t\) \((t\in \{1,\ldots ,T\})\) , at a given site in the cortex, is given by

\[\pmb {R}_{\mathrm{est}} = g_{\mathrm{P}}(\pmb{S}^{tr}\pmb {V}_{\mathrm{P}}) + g_{\mathrm{N}}(\pmb{S}^{tr}\pmb {V}_{\mathrm{N}}). \quad (1)\]

Where \(tr\) is the matrix transpose. Each column of the stimulus matrix \(S\) contains the stimulation amplitude applied at time \(t\) with a row for each stimulating electrode \(j\) \((j\in \{1\ldots M\})\) , where \(T\) is the number of stimuli that resulted in a response. The stimulus vector at time \(t\) is thus given by

\[s_{t} = \left( \begin{array}{c}s_{1,t}\\ \vdots \\ s_{M,t} \end{array} \right). \quad (2)\]

The normalized stimulus vector is thus given by

\[\bar{s}_t = \left( \begin{array}{c}s_{1,t} / \sigma_1\\ \vdots \\ s_{M,t} / \sigma_M \end{array} \right), \quad (3)\]

where \(\sigma_{M}\) is the activation threshold of each stimulating electrode. Since more than one spike was sometimes recorded per stimulus, the spike triggered covariance is given by

\[C_{\mathrm{STC}} = \frac{1}{N}\sum_{t = 1}^{T}r_{i,t}\bar{s}_t\bar{s}_t^{tr}, \quad (4)\]

where \(r_{i,t}\) is the response on recording channel \(i\) \((i\in \{1\ldots C\})\) at time \(t\) and \(N\) is the sum of responses on that channel.

The combined effect of all stimulating electrodes on a response in a given cortical channel could be either net anodic- first or net cathodic- first. Therefore, the effects of both anodic- first and cathodic- first biphasic pulses were included separately in the model. Responses due to a net anodic- first stimulation \((R_{\mathrm{P}})\) were those where the projections of the stimulus onto the principal eigenvector of \(C_{\mathrm{STC}}\) (denoted \(u_{\mathrm{STC}}\) ) were positive. Stimuli for which this held true were denoted \(\bar{s}_{\mathrm{P}}\) , such that

\[\bar{s}_{\mathrm{P}}\cdot u_{\mathrm{STC}} > 0. \quad (5)\]

> **Image description.** A complex flow diagram titled "Model" illustrates the linear nonlinear cascade model of the pathway between the retina and the visual cortex. The diagram depicts a signal flow from a retinal input on the left to a predicted cortical response on the right, utilizing two parallel processing streams (positive and negative).
>
> The process begins on the far left with the input labeled "Biphasic current stimuli in retina." This input is visually represented by a grid of small, dark gray/black circles, labeled $t_1$.
>
> The signal then enters the central processing block, "Model," which is divided into two parallel paths: a positive path (P) and a negative path (N).
>
> 1.  **Positive Path (P):** This stream is color-coded in red/pink.
>     *   It first passes through "Linear filters," represented by a matrix of red circles, labeled $V_P$.
>     *   The output of the linear filters then enters "Static nonlinearities," represented by a red, S-shaped curve, labeled $g_P$.
>
> 2.  **Negative Path (N):** This stream is color-coded in blue/purple.
>     *   It first passes through "Linear filters," represented by a matrix of blue circles, labeled $V_N$.
>     *   The output of the linear filters then enters "Static nonlinearities," represented by a blue, S-shaped curve, labeled $g_N$.
>
> The outputs of both the positive ($g_P$) and negative ($g_N$) nonlinearities converge and feed into the final stage.
>
> The final stage on the right is labeled "Predicted visual cortex response." This is visually represented by a square heatmap or color gradient. The color scale on the right side of the output ranges from dark red (representing a response of 0) to bright yellow/white (representing a response of 1), indicating the magnitude of the predicted cortical response.
>
> Text visible in the image includes the journal citation "J. Neural Eng. 14 (2017) 016006" in the top left corner and the author name "K. Halupa" in the top right corner. The overall structure clearly demonstrates how the input stimulus is processed through linear and nonlinear transformations in two opposing pathways to generate a final predicted output.

<center>Figure 3. The linear nonlinear cascade model of the pathway illustrated between the retina and visual cortex. Shown here is the input signal, arranged in the form of multiple electrode stimulation of the suprachoroidal array. The input is split by the model into a positive' and a negative' path, each representing the cortical response to net anodic first and net cathodic first stimuli respectively. After the linear and the nonlinear filters act on either side, the outputs are summed. The summed output is the predicted cortical response to a particular input stimulus. A total of 3600 white noise patterns were presented to the retina, here \(t_1\) refers to a single stimulus and its resulting predicted response. </center>

Responses to a net cathodic- first stimulation \((R_{\mathrm{N}})\) were those for which the projections onto the principal eigenvector were negative,

\[\bar{s}_{\mathrm{N}}\cdot \pmb {u}_{\mathrm{STC}}< 0, \quad (6)\]

where \(\bar{s}_{\mathrm{N}}\) were the corresponding cathodic- first stimuli.

The linear filter estimates \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) were then calculated as the spike triggered average (Chichilnisky 2001) of response subsets \(r_{\mathrm{P}}\) and \(r_{\mathrm{N}}\) and their respective stimuli \((s_{\mathrm{P}}\) and \(s_{\mathrm{N}})\)

\[V_{\mathrm{P,est}} = \frac{r_{\mathrm{P}}^{tr}\bar{s}_{\mathrm{P}}}{N_{\mathrm{P}}} \quad (7)\]

and

\[V_{\mathrm{N,est}} = \frac{r_{\mathrm{N}}^{tr}\bar{s}_{\mathrm{N}}}{N_{\mathrm{N}}}, \quad (8)\]

where \(N_{\mathrm{P}}\) and \(N_{\mathrm{N}}\) are the sums of response subsets \(r_{\mathrm{P}}\) and \(r_{\mathrm{N}}\) respectively, such that \(N_{\mathrm{P}} + N_{\mathrm{N}} = N\) . Filters were then normalized by dividing by their L- 2 norm. These \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) vectors were considered to be weightings for the effect of the stimulating electrodes on a given cortical site.

The static nonlinearities \(g_{\mathrm{P}}\) and \(g_{\mathrm{N}}\) were approximated by sigmoids and parameterized by their saturation amplitudes \((y_{\mathrm{P}}\) and \(y_{\mathrm{N}})\) , thresholds \((a_{\mathrm{P}}\) and \(a_{\mathrm{N}})\) which are \(50\%\) of the saturation level, as well as the gain of the sigmoids \((b_{\mathrm{P}}\) and \(b_{\mathrm{N}}\) ). The equations for the static nonlinearities \(g_{\mathrm{P}}\) and \(g_{\mathrm{N}}\) are

\[g_{\mathrm{P}}(x_{\mathrm{P}}) = \frac{y_{\mathrm{P}}}{1 + \mathrm{e}^{(-b_{\mathrm{P}}(x_{\mathrm{P}} - a_{\mathrm{P}}))}}, \quad (9)\]

\[g_{\mathrm{N}}(x_{\mathrm{N}}) = y_{\mathrm{N}} - \frac{y_{\mathrm{N}}}{1 + \mathrm{e}^{(-b_{\mathrm{N}}(x_{\mathrm{N}} - a_{\mathrm{N}}))}}. \quad (10)\]

We used the distribution of the outputs of the linear filters, \(x_{\mathrm{P}} = \bar{s}_{\mathrm{P}}V_{\mathrm{P,est}}\) and \(x_{\mathrm{N}} = \bar{s}_{\mathrm{N}}V_{\mathrm{N,est}}\) (hereafter referred to as generator signals), and corresponding responses \(r_{\mathrm{P}}\) and \(r_{\mathrm{N}}\) , to provide an initial estimate for the parameters of nonlinear functions \(g_{\mathrm{P}}\) and \(g_{\mathrm{N}}\) , respectively. The threshold values \(a_{\mathrm{P}}\) and \(a_{\mathrm{N}}\) were estimated to be the mean values of their respective generator signals, while \(y_{\mathrm{P}}\) and \(y_{\mathrm{N}}\) were estimated as that maximum average response recorded on any channel (averaged over repeated trials). We used a Levenberg- Marquardt nonlinear least squares algorithm in MATLAB (Mathworks, Inc. USA) to find the optimal nonlinear parameters \((a_{\mathrm{P}}, a_{\mathrm{N}}, b_{\mathrm{P}}, b_{\mathrm{N}}, y_{\mathrm{P}},\) and \(y_{\mathrm{N}}\) ) and confirm that the optimal linear filters were \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) . The outcome of this process was a set of linear filters and static nonlinearities, each corresponding to a different recording channel (shown for one recording channel in figure 5). To test which electrodes significantly affected a recording channel's response, we randomly time- shifted the response vector 1000 times and repeated the above analysis (equations (1)–(8)) for each new response subset. This generated a distribution for \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) to which the true vectors could be compared. Electrodes from the true \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) that were larger than the root mean square of the randomly- generated distribution were considered significant. The spatial extent in the retina over which a cortical site is influenced by is given by

\[\begin{array}{l}{{D_{\mathrm{P}}=\frac{\sum_{j=1}^{M}\nu_{j}^{\mathrm{P}}d_{j}}{\sum_{j=1}^{M}\nu_{j}^{\mathrm{P}}}},\qquad(11)}\\ {{D_{\mathrm{N}}=\frac{\sum_{j=1}^{M}\nu_{j}^{\mathrm{N}}d_{j}}{\sum_{j=1}^{M}\nu_{j}^{\mathrm{N}}}},\qquad(12)}}\end{array} \quad (11)\]

where \(d_{j}\) is the distance of each electrode \(j\) to the center of mass of the significant electrodes and \(\nu_{j}^{\mathrm{P}}\) and \(\nu_{j}^{\mathrm{N}}\) are the weights given by \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) , respectively.

## Statistical analysis

To compare the sizes of \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) , we conducted a sign test to determine whether the results of subtracting the filters for each channel were significantly different to zero. False discovery rate correction (Benjamini and Hochberg 1995) was used to control for multiple comparisons to a level of \(p < 0.05\) . We used the same analysis to compare the sizes of \(V_{\mathrm{P,est}}\) and \(V_{\mathrm{N,est}}\) between the two model types (MUA model and EP power model).

To demonstrate the ability of the model to predict cortical responses to spatially white electrical retinal stimulation, we performed a 6- fold cross validation analysis on all eight experiments for models fitted to both MUA and evoked response power. For this, the model was fitted using only \(5 / 6\) of the white noise data and used to predict the remaining \(1 / 6\) of the data. Only recording sites that exhibited a monotonic increase of activity with current in response to single electrode stimulation of at least one stimulating electrode were included in model fitting and analysis. Cross- correlation analyses were performed to compare the predicted and recorded responses. The coefficient of determination and slope of the line of best fit (where the predicted response was the independent variable) were calculated for each of the cross- validation sets independently. Unless otherwise stated, all figures with error bars show the mean and standard error of the mean. Significant differences between the prediction abilities of the model fitted to MUA versus that fitted to evoked response power were tested using a Wilcoxon rank sum test \((p < 0.05)\) .

In order to rule out any correlations due to chance, we estimated the number of responses to white noise patterns in the trial set that could be accurately predicted by the model. A bootstrap test was performed (10 000 samples) comparing the absolute residual error of prediction for each white noise pattern in the trial set against a distribution composed of the absolute residual error of recorded responses versus time- shifted predictions, over all fitted channels. False Discovery Rate correction (Benjamini and Hochberg 1995) was used to control for multiple comparisons to a level of \(p < 0.05\) .

We then tested the ability of models trained with responses to white- noise stimuli to predict responses to the oriented pattern stimuli. Models used in these predictions were fitted to all of the responses to white- noise stimuli (rather than just \(5 / 6\) of the data). Here, the coefficient of determination and slope of the line of best fit was calculated for each of the five stimulation amplitudes separately for all

eight experiments. Further bootstrap analyses similar to those performed with the white noise data were also performed on the pattern stimuli data to rule out any correlations that may have occurred due to chance. The same analysis was performed to compare the predicted and measured responses to single electrode stimulation, using the data obtained to calculate single electrode thresholds. In addition to comparing the absolute residual error to the bootstrapped distribution, the coefficient of determination between the predicted and recorded responses to above- threshold single electrode stimulation was also compared in the same manner.

## Results

Across eight experiments, visual cortex responses to multielectrode stimulation of the retina were recorded and analyzed in the form of MUA and EP power on a total of 696 recording channels.

## Cortical responses to multi-electrode suprachoroidal stimulation

Figures 4(a) and (b) show raw recording traces from two recording sites following a stimulus pulse, indicating evoked responses, and the presence of spiking activity, respectively (to a white noise stimulus). Evoked responses typically consisted of two prominent peaks occurring a few milliseconds apart (figure 4(a)), sometimes followed by a third peak, resulting in a significant increase in power from the baseline response (figure 4(e)). Both response measures exhibited a characteristic, monotonically increasing sigmoidal relationship with current amplitude (figures 4(c) and (d)) (Cicione et al 2012, Shivdasani et al 2012, Dumm et al 2014). However, significantly more channels exhibited this effect for EP power than MUA (MUA versus EP power: \(66.6\% \pm 6.1\) versus \(92.4\% \pm 3.2\) , \(p = 0.0029\) ; rank sum test; \(N = 8\) ).

## Prediction of cortical responses

Models for the response on each channel were fitted independently and parametrized by two linear filters and two static nonlinearities (figure 5). The linear filters derived analytically (equations (2)–(8)) and the optimized linear filters were compared, showing that the filters were largely identical before and after optimization, with a median \(r^2\) correlation coefficient of 0.93. The optimized linear filters and nonlinearity parameters were used in all further analyses. Figure 5 shows the components of the model for one recording channel. As shown by the linear filters, which can be considered to be the electrical receptive fields (ERFs) for each cortical channel, this particular recording site was maximally activated by pulses on the top left edge of the stimulating array. The static nonlinearities are functions of the action of the linear filters on the stimulus vector. For this recording channel, the model prediction of the responses (figure 5(c)) was in close agreement with the recorded responses shown in gray

> **Image description.** This image is a multi-panel scientific figure (Figure 4) presenting electrophysiological data and subsequent analysis of a single electrode stimulus response. The figure is composed of five distinct panels, labeled (a) through (e), arranged in a 2x3 grid format.
>
> **Panels (a) and (b): Raw and Filtered Traces**
> Panels (a) and (b) are time-series traces showing voltage responses. Both panels share the same axes: a vertical scale of "0.1 mV" and a horizontal scale of "5 ms."
> *   **Panel (a)** displays the raw response, showing a complex, multi-peaked evoked potential (EP) waveform. A vertical dashed line marks the end of the stimulus artifact.
> *   **Panel (b)** displays a filtered trace, which clearly shows distinct, sharp upward spikes (action potentials). These spikes are marked with asterisks (*).
>
> **Panels (c) and (d): Transfer Functions**
> Panels (c) and (d) are line graphs illustrating the transfer functions of the measured responses against increasing stimulation amplitude. Both plots feature a sigmoidal (S-shaped) curve representing the relationship between stimulus current and response magnitude.
> *   **Panel (c)** plots "Norm. power" (Y-axis) versus "Stim. current ($\mu$A)" (X-axis). The data points show a rapid increase in power followed by saturation. A dashed horizontal line indicates a response threshold, and an arrow points to the average normalized power.
> *   **Panel (d)** plots "Spike count" (Y-axis) versus "Stim. current ($\mu$A)" (X-axis). Similar to panel (c), the data forms a sigmoidal curve. A dashed horizontal line marks the threshold, and an arrow points to the average spike count.
>
> **Panel (e): Power Spectrum**
> Panel (e) is a spectrogram (power spectrum) of the multi-peaked response shown in panel (a).
> *   The axes are "Freq. (kHz)" (Y-axis) and "Time (ms)" (X-axis).
> *   The power is represented by a color gradient, ranging from dark blue (low power) to bright yellow/white (high power), as indicated by the color bar labeled "Norm. power" (0 to 2).
> *   A prominent, bright yellow area indicates a significant increase in power. A white dashed box defines the specific time and frequency window used for calculating the EP power.
>
> **Text and Labels**
> The top of the figure includes publication information: "J. Neural Eng. 14 (2017) 01606" on the left and "K Halupa et al." on the right. The axes and data points in all panels are clearly labeled with technical units (mV, ms, $\mu$A, kHz).

<center>Figure 4. (a) Raw response on one recording channel from a single electrode stimulus at \(700\mu \mathrm{A}\) , showing a multi-peaked evoked potential; dashed line shows the end of the stimulus artefact. (b) Filtered trace on a different recording channel, showing spiking (indicated by asterisks) in response to single electrode stimulation. (c), (d) Transfer functions of the power in the multi-peaked evoked potential (c) and spike count (d) versus stimulation amplitude, with a sigmoidal line of best fit. Dashed lines show the thresholds of these particular stimulating electrodes at \(50\%\) of maximum response. The arrows show the average normalized power and spike count for responses shown in panels (a) and (b) respectively. (e) Power spectrum of the multi-peaked response shown in panel (a). The black outline indicates significant increase in power from the baseline response. White dashed box indicates the time and frequency window within which the EP power is calculated. </center>

(mean \(\pm\) SEM of the binned responses) (coefficient of determination \(r^2 = 0.865\) ).

## Validating model fit  

For the averaged responses to stimuli to be a reasonable metric to fit the model, the stimulus response variability must be minimal. Figure 6(a) shows the measured EP power (mean \(\pm\) SE) for all recording channels in response to 60 repetitions of a white noise stimulus pattern in one experiment. Only minor variation in responses was observed, and a clear and significant correlation was seen with the responses predicted by the model ( \(r^2 = 0.93\) , \(p < 0.0001\) , FDR corrected permutation test, 10 million permutations). The same metric, but for a single cortical channel in response to 30 different white noise stimuli each repeated 60 times, is shown in figure 6(b). Again, only minor variation in response was observed, with a clear and significant correlation ( \(r^2 = 0.92\) , \(p < 0.0001\) , FDR corrected permutation test, 10 million permutations).

The stimuli used to fit the model comprised 3600 different white noise patterns, averaged over eight repeats. For one such white noise stimulus (figure 7(a)), a comparison of the recorded and predicted responses (figure 7(b)) indicates that the model prediction of the response was very similar to the measured response, which was borne out by a coefficient

> **Image description.** A multi-panel scientific figure (Figure 5) illustrating the model components for a single recording channel, consisting of two spatial filter maps (a and b) and a line graph showing static nonlinearities (c).
>
> **Overall Layout and Legend:**
> The figure is divided into three main sections labeled (a), (b), and (c). A vertical color bar is positioned to the right of panels (a) and (b), serving as a legend for the "Weight" of the filters. This bar ranges from -0.4 (represented by dark blue) to 0.4 (represented by dark red). The journal citation "J. Neural Eng. 14 (2017) 01600" is visible in the top left corner.
>
> **Panel (a): Spatial Linear Filters $V_N$**
> Panel (a) is titled "$V_N$" and displays a 5x5 grid of 25 circles, representing stimulating electrodes on a retinal array. The color of each circle corresponds to its linear filter weight. The colors range from light blue/white to dark blue, indicating negative weights. The distribution of colors is non-uniform across the grid.
>
> **Panel (b): Spatial Linear Filters $V_P$**
> Panel (b) is titled "$V_P$" and also displays a 5x5 grid of 25 circles. Similar to panel (a), the color of each circle represents its linear filter weight. The colors range from light red/white to dark red, indicating positive weights. The distribution of colors is non-uniform across the grid.
>
> **Panel (c): Static Nonlinearities $g_N$ and $g_P$**
> Panel (c) is a line graph titled "Norm. power" on the y-axis, plotted against a numerical scale from -400 to 400 on the x-axis. This panel shows the static nonlinearities of the model:
> *   **Red Line ($g_P$):** Represents the static nonlinearity for $V_P$. This line exhibits a sharp, pronounced peak near the center (x=0) before decreasing.
> *   **Blue Line ($g_N$):** Represents the static nonlinearity for $V_N$. This line is generally lower and flatter compared to the red line.
> *   **Data Representation:** A dashed black line represents the average recorded response, labeled with a coefficient of determination: "$r^2 = 0.865$". This line is surrounded by a gray shaded area, which represents the mean $\pm$ SEM (Standard Error of the Mean).

<center>Figure 5. Model components for a single recording channel, as shown schematically in figure 3, fitted with EP power in response to \(5 / 6\mathrm{th}\) of the white noise stimuli in one experiment. (a) Spatial linear filters \(V_{\mathrm{N}}\) and (b) \(V_{\mathrm{P}}\) , where each circle represents a stimulating electrode on the retinal array, and color refers to the strength of the linear filter. (c) Static nonlinearities \(g_{\mathrm{N}}\) (blue line) and \(g_{\mathrm{P}}\) (red line). The \(y\) axis is normalized to the maximum average EP power recorded on any channel. Dashed black line shows the average recorded response to each of the binned generator signal levels (mean \(\pm\) SEM, shown in gray) \((r^2 = 0.865)\) </center>

of determination of \(r^2 = 0.936\) (figure 7(c)), with a strong overall correlation observed for this experiment \((r^2 = 0.819\) , figure 7(d)).

Similar correlations were found for all six cross- validated models for all eight experiments, with \(0.55 < r^2 < 0.89\) \((n = 48)\) . Models fitted to MUA displayed significantly higher correlation coefficients (MUA versus EP power: \(r^2 = 0.77 \pm 0.01\) versus \(0.69 \pm 0.02\) , \(p = 1.22 \times 10^{- 4}\) ; rank sum test) than those fitted to EP power. The average slope of the line of best fit for the models fitted to power was significantly closer to 1 (MUA versus EP power: \(0.88 \pm 0.018\) versus \(0.92 \pm 0.13\) , \(p = 2.13 \times 10^{- 4}\) ; rank sum test) than those fitted to MUA.

Both types of models were able to predict the responses to at least \(75\%\) of the test set significantly better than chance (via bootstrap analysis), with the MUA model predicting significantly more than the EP power model (MUA versus EP power: \(95.77\% \pm 0.57\%\) versus \(92.70\% \pm 0.90\%\) , \(p = 4.08 \times 10^{- 4}\) ; rank sum test).

## ERFs characterized by linear filter component  

The linear filters of the model provided an estimate of the ERFs of each recording channel for simultaneous retinal stimulation. Figure 8(a) shows the ERF for stimuli with a net cathodic- first effect, for the most rostro- medial recording site; this channel was most responsive to stimulation of the superior- nasal retinal electrodes. The interpolated color maps depicting the linear filters at all cortical sites \((n = 96)\) from this experiment (figure 8(b)) display a clear preference to stimulation of superior- nasal retinal electrodes for more rostral recording sites, while caudal recording sites showed a preference for stimulation of electrodes located towards the inferior retina. The gradual movement of the ERFs between these two extremes indicates topographic mapping, and is likely to be retinotopic. Using these ERFs in combination with the static nonlinearities, it is possible to link regions of high activity to stimulus features. For example, the high power in the rostral (rostral direction shown in figure 1(b)) sites in figure 7(b) can be attributed to high stimulation amplitude on superior- nasal retinal electrodes. Figure 8(c) more clearly illustrates the rostro- caudal movement of the linear filters, where contours represent the significant linear filter weights belonging to the most rostro- medial (green) and caudo- medial (purple) recording sites (circled in figure 8(b)). The recording sites in this example were separated by a distance of approximately \(7\mathrm{mm}\) in the cortex, which corresponds to approximately \(14^{\circ} - 23^{\circ}\) of visual angle using a cortical magnification factor of \(0.3 - 0.5\mathrm{mm / degree}\) (Tusa et al 1978). The peak weightings of the linear filters for these channels were separated by about \(4\mathrm{mm}\) in retinal space, which subtends a visual angle of approximately \(18^{\circ}\) , and thus corresponds well with the recording channel separation.

While significant differences did occur between the size of ERFs for stimuli with a net cathodic- first effect and those with a net anodic- first effect on a channel by channel basis when using the EP power based model (Sign test, 0.05 level of significance), these differences were not consistent across experiments. Two out of eight experiments had larger \(V_{\mathrm{N}}\) filters than \(V_{\mathrm{P}}\) filters; however, one experiment had significantly larger \(V_{\mathrm{P}}\) filters than \(V_{\mathrm{N}}\) filters. No differences occurred between MUA- based model ERFs. Similar inconsistent differences occurred when comparing the ERF size between the two model types (EP power based models: two experiments had larger \(V_{\mathrm{N}}\) filters, three had larger \(V_{\mathrm{P}}\) filters; MUA- based models: three experiments had larger \(V_{\mathrm{N}}\) filters, three had larger \(V_{\mathrm{P}}\) filters).

## Predicting responses to electrical pattern stimuli

To examine whether a model fitted using responses to white noise stimuli could predict responses to non- white stimuli, measured responses to oriented pattern stimuli and single electrode stimuli were compared to responses predicted by the model. Three types of patterned stimuli were used: mixed- phase, anodic- first and cathodic- first. Figure 9(a) shows the comparison between the recorded and predicted responses for the stimulus shown in figure 2(a), where the maximum current amplitude delivered was \(295\mu \mathrm{A}\) . The responses predicted by the model corresponded well to the measured responses (figure 9(b), \(r^2 = 0.89\) ) for this stimulus.

To assess whether this effect extended to the entire set of oriented pattern stimuli, we calculated a coefficient of determination for each of the three pattern types for all experiments (figure 10(a)). Coefficients corresponding to MUA models were significantly higher than those for EP power

> **Image description.** A composite image consisting of two side-by-side scatter plots, labeled (a) and (b), which illustrate the correlation between recorded and predicted neural responses. Both panels are graphs with a linear relationship between the two variables.
>
> **General Graph Features:**
> Both panels share identical axes and scales. The horizontal axis (x-axis) is labeled "Predicted response" and ranges from 0 to 1. The vertical axis (y-axis) is labeled "Recorded response" and also ranges from 0 to 1. In both plots, the data points are clustered around a dashed diagonal line, which represents the line of perfect correlation ($y=x$). The data points themselves are small, dark markers, and the overall distribution suggests a strong positive correlation.
>
> **Panel (a) Details:**
> *   **Label:** (a)
> *   **Correlation:** The top right corner displays an $r^2$ value of 0.93.
> *   **Data:** The plot shows a dense collection of data points, indicating a high degree of agreement between the recorded and predicted responses.
> *   **Context (from caption):** This panel represents responses recorded on 88 cortical channels in one experiment, measured over 60 repetitions of a single white noise stimulus.
>
> **Panel (b) Details:**
> *   **Label:** (b)
> *   **Correlation:** The top right corner displays an $r^2$ value of 0.92.
> *   **Data:** Similar to panel (a), the data points are tightly clustered around the dashed line, indicating a very strong correlation.
> *   **Context (from caption):** This panel represents responses recorded on a single recording channel in the same experiment, measured over 60 repetitions of 30 separate white noise stimuli.
>
> **Text and Metadata:**
> *   **Headers:** The top left corner contains the journal citation: "J. Neural Eng 14 (2017) 01606". The top right corner contains the author attribution: "K Halpa et al".
> *   **Figure Caption:** The caption below the graphs reads: "Figure 6. Mean and standard error of recorded responses (n = 60 repetitions of each stimulus) plotted against the responses predicted by the model. Response measure is power in the multi-peaked EP. (a) Responses on 88 cortical channels in one experiment to 60 repetitions of a single white noise stimulus. (b) Responses on a single recording channel in the same experiment as in panel (a), to 60 repetitions of 30 separate white noise stimuli."

<center>Figure 6. Mean and standard error of recorded responses \((n = 60\) repetitions of each stimulus) plotted against the responses predicted by the model. Response measure is power in the multi-peaked EP. (a) Responses on 88 cortical channels in one experiment to 60 repetitions of a single white noise stimulus. (b) Responses on a single recording channel in the same experiment as in panel (a), to 60 repetitions of 30 separate white noise stimuli. </center>

> **Image description.** A multi-panel scientific figure, labeled Figure 7, presenting data related to the modeling and correlation of neural responses to a white-noise stimulus. The figure is divided into four distinct panels: (a), (b), (c), and (d).
>
> Panel (a) displays a visualization of the white-noise stimulus. It consists of a grid of 64 circular elements, each filled with a varying shade of gray, representing current amplitude. A vertical color bar on the right side of the panel is labeled "Stimulus amp (uA)" and indicates a range from -750 to 750, signifying positive (anodic-first) and negative (cathodic-first) pulses.
>
> Panel (b) presents a comparison of the recorded and predicted responses. It features two square heatmaps placed side-by-side. The map on the left is labeled "Recorded," and the map on the right is labeled "Predicted." Both heatmaps use a color scale ranging from 0 to 1, with warmer colors (yellow/orange) indicating higher response power.
>
> Panel (c) is a scatter plot illustrating the correlation between the recorded and predicted responses for individual channels. The x-axis is labeled "Predicted" and the y-axis is labeled "Recorded," both ranging from 0 to 1. A dashed diagonal line representing $y = x$ is visible. The data points are black dots, and the panel includes the annotation "$r^2 = 0.936$," indicating a high correlation.
>
> Panel (d) is an aggregated scatter plot showing the correlation across a larger dataset of stimuli. The x-axis is labeled "Predicted response" and the y-axis is labeled "Recorded response," both ranging from 0 to 1. A dashed diagonal line is present. The data points are black dots, and the panel includes the annotation "$r^2 = 0.819$." Crucially, this panel incorporates a color scale on the right, labeled "Log of response freq," which ranges from 0 (dark blue) to 3 (yellow/white), indicating the frequency of the response magnitude.

<center>Figure 7. (a) Example of a white-noise stimulus in one experiment with positive currents indicating anodic-first pulses and negative currents indicating cathodic-first pulses. (b) Recorded and predicted EP power in the visual cortex across two recording arrays in response to the white noise stimulus shown in panel (a) (averaged over 8 repetitions). (c) Correlation between the recorded response to the stimulus and the response predicted by the model. Each point represents the response measured on a single recording channel. Dashed line is \(y = x\) . (d) Aggregated scatter plot for all 600 white-noise stimuli that were not used to fit the model for this experiment, with the log frequency of responses represented on the color scale. Black dots show the responses presented in panel (c). </center>

models for mixed- phase stimuli (MUA versus EP power: \(r^2 = 0.81 \pm 0.02\) versus \(0.69 \pm 0.03\) , \(p = 0.016\) ; rank sum test). There was no difference between the MUA model and EP power model for the other two stimulus types (MUA versus EP power with anodic- first pulses: \(r^2 = 0.65 \pm 0.07\) versus \(0.65 \pm 0.05\) , \(p = 0.558\) . MUA versus EP power with cathodic- first pulses: \(0.73 \pm 0.06\) versus \(0.73 \pm 0.04\) , \(p = 0.457\) ). However, for the mixed- phase and cathodic- first stimulus types, the slopes of the lines of best fit for the models fitted to MUA were significantly lower than those fitted to EP power (figure 10(b), MUA versus EP power with mixedphase pulses: \(0.76 \pm 0.05\) versus \(0.96 \pm 0.09\) , \(p = 0.02\) . MUA versus EP power with anodic- first pulses: \(0.75 \pm 0.04\) versus \(0.94 \pm 0.12\) , \(p = 0.08\) . MUA versus EP power with cathodic- first pulses: \(0.72 \pm 0.05\) versus \(0.93 \pm 0.10\) , \(p = 0.03\) ; rank sum test).

While the percentage of responses that were able to be predicted significantly above chance was generally high for both types of models and all types of stimuli (via bootstrap analysis, figure 10(c)), the model fitted to MUA was able to predict a significantly higher number of responses for both mixed- phase and anodic- first stimuli compared to the EP

> **Image description.** This image is a complex technical figure, Figure 8, illustrating linear filter maps and schematic representations of electrode arrays and cortical recording sites from a neuroscience experiment. The figure is divided into three distinct panels labeled (a), (b), and (c).
>
> **Panel (a): Electrode Array Schematic**
> Panel (a) displays a schematic of a rectangular grid representing the stimulating array. This grid contains 42 numbered circles, each representing an electrode location. The numbers range from 1 to 42. To the right of the grid, four letters are positioned, likely indicating retinal locations: S (superior retina), I (inferior retina), N (nasal retina), and T (temporal retina).
>
> **Panel (b): Recording Setup and Filter Maps**
> Panel (b) is divided into two sections. On the left, a schematic of the recording setup is shown, featuring two boxes labeled "1" and "2," connected by lines, suggesting two recording sites or channels. A coordinate system is visible, defining directions: R (rostral), C (caudal), M (medial), and L (lateral). On the right, a large matrix of color maps is presented. This matrix consists of numerous circular maps, each representing a linear filter for a specific recording site. The maps are predominantly colored in shades of red and pink, indicating a strong effect of the stimulating electrodes on the recorded activity. Some cells in the grid are blank or white. A prominent green circle is drawn around one specific circular map within this large grid.
>
> **Panel (c): Cortical Recording Site Schematic**
> Panel (c) shows a schematic of a stimulating array, similar in structure to panel (a). This panel highlights two specific recording sites using colored circles: one green circle and one purple circle. These circles are positioned on the grid structure, representing specific cortical recording sites (rostro-medial and caudo-medial, according to the context).
>
> **Text and Labels**
> Visible text and labels include:
> *   Panel labels: (a), (b), (c).
> *   Electrode numbers: 1 through 42.
> *   Retinal location labels: S, I, N, T.
> *   Coordinate labels: R, C, M, L.
> *   Text in panel (c): "95th percentile of circled filters".
> *   The overall figure caption text is partially visible at the top left: "Figure 8. Linear filter maps for each recording site in one experiment."

<center>Figure 8. Linear filter maps for each recording site in one experiment. (a) Linear filter of the most rostr-caudally located cortical site (marked with a green circle in panel (b) prior to interpolation, as described in figure 5. Only filters corresponding to anodic first stimulation (i.e. \(\nu_{p}\) ) are shown. Electrode numbers correspond to those indicated in figure 1(a). S: superior retina, I: inferior retina, N: nasal retina, T: temporal retina. (b) Interpolated color maps representing optimized linear filters for anodic first stimulation pulses ( \(\nu_{p}\) ) corresponding to each of the 96 recording sites. Schematic of cortical recording areas corresponding to each of the linear filter maps is also shown. Red indicates a strong effect of a particular stimulating electrode on the activity recorded on a given cortical site. Blank sites are those that did not record a monotonically increasing response to single electrode stimulation and were thus excluded from analyses. R: rostral, C: caudal, M: medial, L: lateral. (c) Schematic of stimulating array showing significant areas of the linear filter maps for two cortical recording sites marked with green and purple circles (corresponding to rostro-medial and caudo-medial recording sites respectively) in panel (b). The shift in the electrodes that have the strongest contributions to a channels activity with cortical channel position shows that the retinotopic organization of the visual cortex is preserved with responses to simultaneous electrical stimulation of the retina. </center>

> **Image description.** This image is a scientific figure, Figure 9, consisting of two panels, (a) and (b), which illustrate the comparison between recorded neural responses and model-predicted responses to a specific oriented pattern stimulus.
>
> **Panel (a): Response Maps**
> Panel (a) displays four square heatmaps arranged in a 2x2 grid, comparing recorded data with model predictions. A vertical color bar to the right of the maps indicates the normalized power, ranging from 0 (dark red/black) to 1 (bright yellow/white).
> *   The top row compares the "Recorded" response (left) and the "Predicted" response (right) for one stimulus orientation. Both maps show a bright, concentrated area of high power in the center-right region.
> *   The bottom row compares the "Recorded" response (left) and the "Predicted" response (right) for a second stimulus orientation. Both maps show a bright, concentrated area of high power in the center-left region.
> The visual similarity between the recorded and predicted maps in both rows suggests that the model accurately reproduces the observed neural activity.
>
> **Panel (b): Correlation Plot**
> Panel (b) is a scatter plot that quantifies the relationship between the recorded and predicted responses.
> *   The X-axis is labeled "Predicted" and ranges from 0 to 1.
> *   The Y-axis is labeled "Recorded" and also ranges from 0 to 1.
> *   Numerous black data points are plotted, representing 88 channels ($n=88$).
> *   A dashed diagonal line runs from the bottom-left corner (0,0) to the top-right corner (1,1), representing a perfect correlation.
> *   The correlation coefficient is displayed in the upper left corner of the plot as $r^2 = 0.892$.
>
> **Text and Metadata**
> The figure includes several pieces of text:
> *   **Top Left:** "Oral Eng. 14 (2017) 01606" (Journal citation).
> *   **Top Right:** "K Halupa" (Author name).
> *   **Caption (below the figure):** "Figure 9. Recorded response and model-predicted response to the oriented pattern stimulus shown in figure 2(a) (mixed phase first stimulus). Response is measured by the power in the EP, and shown over two recording arrays arranged as in figure 8. The color map is normalized to the maximum recorded power. (a) Recorded response (left), and predicted response (right). (b) Correlation between the recorded and predicted responses (n = 88 channels)."

<center>Figure 9. Recorded response and model-predicted response to the oriented pattern stimulus shown in figure 2(a) (mixed phase first stimulus). Response is measured by the power in the EP, and shown over two recording arrays arranged as in figure 8. The color map is normalized to the maximum recorded power. (a) Recorded response (left), and predicted response (right). (b) Correlation between the recorded and predicted responses ( \(n = 88\) channels). </center>

> **Image description.** A multi-panel bar chart, labeled Figure 10, which compares the predictive ability of two models—a spiking-based model (MUA, represented by gray bars) and a power-based model (represented by white bars)—when predicting responses to grating pattern stimuli. The figure is divided into three distinct panels: (a), (b), and (c).
>
> **General Structure and Elements:**
> The X-axis across all three panels represents three types of stimulation: "Mixed," "Anodic," and "Cathodic." The legend indicates that the gray bars represent the MUA (spiking-based) model, and the white bars represent the Power (power-based) model. Asterisks (*) are placed above each pair of bars, signifying a statistically significant difference ($p < 0.05$) between the two models for that specific stimulation type.
>
> **Panel (a): Coefficient of determination ($r^2$)**
> This panel plots the "Coefficient of determination ($r^2$)" on the Y-axis, ranging from 0 to 1. In all three categories (Mixed, Anodic, and Cathodic), the gray bars (MUA) are consistently higher than the white bars (Power). This indicates that the MUA model has a higher coefficient of determination, meaning it explains a greater proportion of the variance in the recorded responses compared to the Power model. An asterisk is present above each pair of bars.
>
> **Panel (b): Slope of line of best fit**
> This panel displays the "Slope of line of best fit" on the Y-axis, ranging from 0.6 to 1.2. Similar to panel (a), the gray bars (MUA) are consistently taller than the white bars (Power) across all three stimulation types. This suggests that the MUA model yields a steeper slope in the correlation between predicted and recorded responses. An asterisk is present above each pair of bars.
>
> **Panel (c): Percentage of responses predicted**
> This panel shows the "Responses Predicted (%)" on the Y-axis, ranging from 0 to 100. For all three stimulation types, the gray bars (MUA) are higher than the white bars (Power). This indicates that the MUA model is able to predict a higher percentage of the responses to the oriented pattern stimuli compared to the Power model. An asterisk is present above each pair of bars.
>
> Overall, the figure visually demonstrates that the spiking-based MUA model consistently outperforms the power-based model across all three tested stimulation types in terms of coefficient of determination, slope of best fit, and percentage of predicted responses.

<center>Figure 10. Comparison of the ability to predict responses to grating pattern stimuli between a spiking-based model (gray) and power-based model (white), averaged over all experiments and stimulation amplitudes (mean \(\pm \mathrm{SM}\) ) ( \(n = 40\) ). Asterisks represent a significant difference \((p < 0.05\) ; rank sum test). (a) Coefficient of determination between the model-predicted responses to oriented pattern stimuli and the recorded responses. (b) Slope of the line of best fit for the correlation described in panel (a). (c) Percentage of responses to oriented pattern stimuli that were able to be predicted significantly using bootstrapping analyses. </center>

power model (MUA versus EP power with mixed- phase pulses: \(94\% \pm 2.1\%\) versus \(77\% \pm 5.2\%\) , \(p = 0.0024\) . MUA versus EP power with anodic- first pulses: \(85\% \pm 5.4\%\) versus \(70\% \pm 7.0\%\) , \(p = 0.129\) . MUA versus EP power with cathodic- first pulses: \(70\% \pm 5.8\%\) versus \(77\% \pm 6.1\%\) , \(p = 0.326\) ; rank sum test).  

When predicting responses to single electrode stimulation, coefficients of determination corresponding to EP power models were significantly higher than those corresponding to MUA models. However, both were lower than those for multi- electrode stimulation (MUA versus EP power: \(r^2 = 0.26 \pm 0.02\) versus \(0.37 \pm 0.02\) , \(p = 0.016\) ; rank sum test). Despite being low, the majority of both MUA and EP responses to stimuli above threshold had \(r^2\) values significantly higher than those of the corresponding bootstrapped distributions (MUA versus EP power: \(90.6\% \pm 1.20\%\) versus \(92.76\% \pm 0.75\%\) , averaged over above- threshold stimulus amplitudes and experiments). The slopes of the lines of best fit for the models fitted to MUA were significantly greater than those fitted to EP power (MUA versus EP power: \(0.40 \pm 0.03\) versus \(0.12 \pm 0.01\) , \(p \ll 0.001\) ; rank sum test). The percentages of responses able to be predicted accurately

by either model were also relatively low, and not significantly different between the model types (MUA versus EP power: \(53\% \pm 3.0\%\) versus \(45\% \pm 1.5\%\) , \(p = 0.208\) ; rank sum test).

## Discussion

We have demonstrated that cortical responses to simultaneous stimulation of the retina are repeatable and can be predicted by a simple LN model. We have shown that the model can be optimized using either multi- unit activity (MUA) or power in the multi- peaked evoked potential (EP), and can be used to predict responses to types of stimulation that were not used to fit it. The optimized model also provides information about ERFs, including the relative effects of each stimulating electrode on every recording site. These ERFs show that the topographic mapping of cortical responses to single electrode stimulation (Elfar et al 2009, Shivdasani et al 2012, Wong et al 2016) is maintained for simultaneous stimulation.

## Comparison with previous studies

Studies have shown that simultaneous multi- electrode stimulation can extend the range of cortical responses possible from retinal implants beyond what is available with interleaved single electrode stimulation (Cicione et al 2012, Matteucci et al 2013, Dumm et al 2014). These studies have characterized the responses of neurons to particular forms of simultaneous stimulation; however, these observations cannot be generalized to patterns for which the system has not been exposed. Response models recovered by white noise electrical stimulation go some way towards solving this issue, since white noise covers a wide range of possible inputs (Chichilnisky 2001).

In terms of visual prostheses, these investigations have been limited to in vitro preparations (Jepson et al 2014, Maturana et al 2016). Jepson et al (2014) showed that a piecewise linear model could predict the activation of a target cell in the retina, however the method was limited to stimulation of small numbers of electrodes at fixed stimulation amplitudes. Maturana et al (2016) successfully showed that a LN model, mathematically similar to our model, captured the responses of RGCs to simultaneous white noise stimulation of 20 electrodes. While the success of these models aligns with that of our LN model, several important distinctions should be made. In the present study, we have demonstrated successful prediction of activity at multiple concurrent sites in the visual cortex (up to 120 recording channels) in response to stimulation, as opposed to one or two cells at a time (Maturana et al and Jepson et al, respectively). Additionally, neither study investigated whether the suggested model performed equally well for stimulation that was non- white, as was shown for our model. Also, activation of the visual cortex more closely approximates perception elicited by electrical stimulation of the human retina than activity recorded in vitro (von der Heydt and Peterhans 1989, Gilbert and Wiesel 1990, Salzman et al 1990, Knierim et al 1992, van Wezel et al 1997), and finally we made use of the same clinical grade electrode array

for stimulation as has been trailed in patients (Ayton et al 2014, Shivdasani et al 2014).

## Comparison of MUA-based and EP power-based models

Two activity measures in the visual cortex were used to fit separate LN models: MUA and EP power. These activity measures correspond to two different types of cortical processing: MUA reflects the spiking activity of multiple neurons within a radius of \(150 - 300 \mu \mathrm{m}\) from the electrode tip (Gray et al 1995, Henze et al 2000); the EP contains both suprathreshold and sub- threshold components, the latter of which extends out over a larger area (Fregnac et al 1996). The electrically evoked potentials seen in our study were found to be in a relatively high frequency band compared to traditional local field potentials, and they exhibited a characteristic, positive- going, multi- peaked shape. A number of studies have investigated the origins of these EPs and the factor that influence them (Chang 1950, Malis and Kruger 1956, Schoolman and Evarts 1959, Doty and Grimm 1962, Burke et al 1985, Mitzdorf 1985). Burke et al (1985) suggested that the first two peaks of this multi- peaked response are due to conduction from Y and X type RGCs, respectively (Enroth- Cugell and Robson 1966, Stone 1983). Mitzdorf (1985) found that the polarity of the peaks was dependent on the cortical depth of their recording electrode. Thus, the constant polarity of the peaks in our study may be attributed to the fact that all recording electrodes on the penetrating array were the same length (1 mm) and were thus likely to be recording from the same cortical layer. More recently, the EP has been shown to be a viable alternative to MUA when comparing percepts from visual prostheses to those from light stimulation, since a similar EP is present in photic stimulation, albeit with delayed peak latencies due to retinal processing (Nakauchi et al 2005, Sun et al 2011). Our findings expand on this, to show that both measures of activity can be the basis of a model for characterizing cortical responses to simultaneous stimulation of the retina. Both model types were able to predict the vast majority of white noise stimuli that were presented in all experiments. In addition, both models displayed high correlation coefficients between recorded and predicted cortical responses to retinal stimuli that were not white, and were able to predict the majority of responses to these stimuli. No consistent differences were found between different receptive field sizes. However, given that we have recorded MUA as opposed to activity from single neurons, it is difficult to make any conclusions regarding the significance of this finding.

Some differences were present between the models, however. The MUA model performed significantly better than the EP power model at predicting responses to white noise, mixed- phase first stimuli and anodic- phase first stimuli. This may be due to a greater signal to noise ratio for the MUA responses than EP power, which suggests that, for a model based on EP power, the number of repetitions for each stimulus should be increased.

Neither model performed well in predicting responses to single electrode stimulation. This may be attributed to the lower thresholds observed when stimulating across several

electrodes simultaneously (Shivdasani et al 2012), such as during white- noise stimulation, causing the model to underestimate the current required to match responses to single electrode stimulation. However, both models could predict responses to above- threshold single electrode stimulation better than chance, suggesting that the retinotopic organization is preserved. From a clinical stand- point it is, therefore, possible that if the highest safe amplitude of single electrode stimulation is unable to elicit a percept, simultaneous stimulation of nearby electrodes could elicit a response in the required area.

During the present study, recording channels were only considered for analyses if they exhibited a monotonic increase in response with increasing stimulation current on any single retinal electrode. As a result, a significantly greater number of sites were excluded from the MUA analyses than from EP power analyses. This likely reflects the requirement that, for recording MUA, the recording site be in close proximity to spiking cells, whereas estimating EP power does not require direct proximity to cells to register an increase. Thus, while the MUA model predicted cortical responses more accurately than the EP power model, the latter had the advantage of characterizing a greater number of recording channels. This suggests that the activity measure on which to train the model could be altered dependent on the requirements of the application, and time available to record responses.

Clinically, the EP power would be a more attractive cortical measure as currently it is possible to record these EPs with less invasive methods than those required to record MUA; i.e., penetrating electrodes for MUA versus scalp electrodes. Additionally, EPs have been shown to be more robust for the long term, retaining information even when spikes are lost on the same electrode (Flint et al 2012). Thus, the EP power is an attractive measure for use with human patients, since it would eliminate the need for a further, invasive procedure, and remain informative in the long term.

## Considerations for future applications

The model described in this study is purely spatial in nature owing to the sparse timing used between stimulus pulses. A similar model has been employed previously to model the spatio- temporal dynamics of neurons responding to visual stimulation of the retina (DeAngelis et al 1993). We expect that by modifying our model to include a temporal dimension in our linear filters, as by Chichilnisky (2001) and Kameneva et al (2015), the model could be extended to predict temporal dynamics of cortical responses during repetitive, high- rate stimulation, such as perceptual fading. While there is strong evidence suggesting that perceptual fading could be attributed to desensitization observed in RGCs (Freeman and Fried 2011), it could also be attributed to neural mechanisms within central visual structures. In human trials, pulse rates for a suprachoroidal prosthesis have ranged between 50 and 500 pulses per second (pps) (Ayton et al 2014, Shivdasani et al 2014) and in other neural systems stimulation rates may be even higher (e.g., stimulation at up to 2000 pps has been studied in cochlear implants Galvin and Fu 2005). Therefore

further investigation of the characteristics of adaptation would be of particular interest. However, in pursuit of this goal, one would have to overcome the hurdle of the stimulation artefact present in the recordings. Our stimulus pulses were 1 ms per phase and biphasic, evoking cortical responses lasting approximately 20 ms. The use of stimulus rates higher than 50 pps would not allow analysis of activity with each pulse in the stimulus train without contamination by the stimulus artifact of subsequent stimulus pulses. However, evidence suggests that desensitization of RGCs and perceptual fading can also occur at rates lower than 50 pps (Freeman and Fried 2011, Fornos et al 2012). At such rates, it would be possible to remove artefacts with the same technique that we have used (Heffer and Fallon 2008) and analyze the responses between pulses. The model we propose could then be adjusted to incorporate spatiotemporal ERFs (Chichilnisky 2001).

Our model also provides an intriguing option for investigation of the effect of photoreceptor degeneration on responses to electrical retinal stimulation. Photoreceptor degeneration in a rat model has been shown to be accompanied by an increased activation threshold to electrical stimulation (Suzuki et al 2004, O'Hearn et al 2006) as well as an increase in baseline spiking (Pu et al 2006, Stasheff 2008). This may be a contributing factor to the inconsistencies found in the clinical results of simultaneous stimulation. Photoreceptor degeneration also leads to retinal remodeling (Jones et al 2003, Marc et al 2003). Thus, it is likely that the ERFs of cortical neurons would be different in appearance to those described here.

Another factor that should be considered in future applications of this method is the effect of anesthesia on cortical activity. Given that anesthesia has been found to reduce the signal- to- noise ratio of visual responses in the cat visual cortex (Livingstone and Hubel 1981) and preserve the main tuning characteristics of V1 neurons in monkeys (Lamme et al 1998) and mice (Niell and Stryker 2010), we expect that the responses to electrical stimulation in an awake cat would be stronger but have similar tuning properties and, therefore, be well suited for application of this method.

The model we have presented provides novel insights into the effects of interactions between electrodes during simultaneous electrical retinal stimulation. It is expected that with some adjustments, this model could provide a potential approach for choosing optimal stimulation patterns for eliciting specific neural activity (for example, activity more akin to that elicited by visual stimulation). This would entail first fitting the model to responses of the system in question to spatial white noise stimulation. Then, a second optimization algorithm would be used to compute stimulation patterns that would be likely to produce a desired cortical response. In this way, the model could be used to ultimately increase the resolution of the implant.

## Conclusion

In this study, we have shown that cortical responses to simultaneous stimulation of the retina are consistent and repeatable. We investigated the effects of electrode

interactions of retinal stimulation by creating a linear- nonlinear model of visual cortex responses. We showed that the model could accurately predict spiking neural responses to both white- noise stimulation and patterned stimulation. The model could also be based on an alternative measure of cortical activity, namely power in the evoked potentials, suggesting that, for clinical applications, a less invasive measure could be applicable. The model we describe provides an effective means of understanding the spatial interactions of retinal stimulation at the level of the cortex, showing that they are predominantly linear and the electrical receptive fields of cortical recording channels are topographically organized. The predictive success of our model shows promise for efficiently determining optimal stimulation paradigms for shaping neural activity with a neural prosthesis.

## Acknowledgments

The authors thank Penny Allen, Jonathan Yeoh, and Chi Luu for surgeries; Carla Abbott, Alice Brandli, Alexia Saunders, Michelle McPhedran, Alison Neil, Dimitra Stathopoulos, Stephanie Epp, and Ceara McGowan for experimental assistance and animal handling; Owen Burns and Vanessa Maxim for manufacturing of the electrodes; Evgeni Sergeev for technical assistance with stimulation software; and Thomas Spencer, Faith Lamont, Ali Almasi, Felix Aplin, Rosemary Cicione, and Ronald Leung for assistance with data collection. This research was supported by the Australian Research Council through its Special Research Initiative in Bionic Vision Science and Technology awarded to Bionic Vision Australia, the Bertalli Family Foundation to the Bionics Institute, and a project grant from the National Health and Medical Research Council, Australia (GNT#1063093). The Bionics Institute acknowledges the support it receives from the Victorian Government through its Operational Infrastructure Program. KJH was supported by an Australian Postgraduate Award through the Australian Government, and a postgraduate scholarship from the National Information and Communication Technology Australia (NICTA—www.nicta.com.au/). NICTA is funded by the Australian Government as represented by the Department of Broadband, Communications and the Digital Economy (www.communications.gov.au/) and the Australian Research Council through the ICT Centre of Excellence program. ANB and YTW acknowledge support under the Australian Research Council's Discovery Projects funding scheme (Project DP140104533).

## References

Auner G W, You R, Siy P, McAllister J P, Talukder M and Abrams G W 2007 Development of a wireless high- frequency microarray implant for retinal stimulation Artificial Sight (New York: Springer) pp 169- 86  
Ayton L N et al 2014 First- in- human trial of a novel suprachoroidal retinal prosthesis PLoS One 9 e115239  
Barry M P, Dagnelie G and Group A I S 2012 Use of the Argus II retinal prosthesis to improve visual guidance of fine hand movements Investigative Ophthalmology Vis. Sci. 53 5095  
Benjamin Y and Hochberg Y 1995 Controlling the false discovery rate: a practical and powerful approach to multiple testing J. R. Stat. Soc. B 57 289- 300  
Boinagrov D, Pangratz- Fuehrer S, Goetz G and Palanker D 2014 Selectivity of direct and network- mediated stimulation of the retinal ganglion cells with epi- , sub- and intraretinal electrodes J. Neural Eng. 11 026008  
Burke W, Burne J and Martin P 1985 Selective block of Y optic nerve fibres in the cat and the occurrence of inhibition in the lateral geniculate nucleus J. Physiol. 364 81- 92  
Chang H- T 1950 The repetitive discharges of corticothalamic reverberating circuit J. Neurophysiol. 13 235- 57  
Chichilnisky E 2001 A simple white noise analysis of neuronal light responses Neww. Comput. Neural Syst. 12 199- 213  
Cicione R, Shvidasani M N, Fallon J B, Luu C D, Allen P J, Rathbone G D, Shepherd R K and Williams C E 2012 Visual cortex responses to suprachoroidal electrical stimulation of the retina: effects of electrode return configuration J. Neural Eng. 9 036009  
da Cruz L, Coley B F, Dorn J, Merlini F, Filley E, Christopher P, Chen F K, Wuyuyuru V, Sahel J and Stanga P 2013 The Argus II epiretinal prosthesis system allows letter and word reading and long- term function in patients with profound vision loss Br. J. Ophthalmol. 0 1- 5  
DeAngelis G C, Ohzawa I and Freeman R 1993 Spatiotemporal organization of simple- cell receptive fields in the cat's striate cortex. II. Linearity of temporal and spatial summation J. Neurophysiol. 69 1118- 35  
Doty R W and Grimm F R 1962 Cortical responses to local electrical stimulation of retina Exp. Neurol. 5 319- 34  
Dumm G, Fallon J, Williams C and Shvidasani M 2014 Virtual electrodes by current steering in retinal prostheses Investigative Ophthalmology Vis. Sci. 55 8077- 85  
Elfar S D, Cottaris N P, Iezzi R and Abrams G W 2009 A cortical (V1) neurophysiological recording model for assessing the efficacy of retinal visual prostheses J. Neurosci. Methods 180 195- 207  
Enroth- Cugell C and Robson J G 1966 The contrast sensitivity of retinal ganglion cells of the cat J. Physiol. 187 517- 52  
Flint R D, Lindberg E W, Jordan L R, Miller L E and Slutzky M W 2012 Accurate decoding of reaching movements from field potentials in the absence of spikes J. Neural Eng. 9 046006  
Fornos A P, Sommerhalder J, da Cruz L, Sahel J A, Mohand- Said S, Hafezi F and Pelizzone M 2012 Temporal properties of visual perception on electrical stimulation of the retinapercetion upon electrical stimulation of the retina Investigative Ophthalmology Vis. Sci. 53 2720- 31  
Freeman D K and Fried S I 2011 Multiple components of ganglion cell desensitization in response to prosthetic stimulation J. Neural Eng. 8 016008  
Fregnac Y, Bringuier V and Chavane F 1996 Synaptic integration fields and associative plasticity of visual cortical cells in vivo J. Physiol. 90 367- 72  
Galvin J J III and Fu Q- J 2005 Effects of stimulation rate, mode and level on modulation detection by cochlear implant users J. Assoc. Res. Otolaryngology 6 269- 79  
Gilbert C D and Wiesel T N 1990 The influence of contextual stimuli on the orientation selectivity of cells in primary visual cortex of the cat Vis. Res. 30 1689- 701  
Gray C M, Maldonado P E, Wilson M and McNaughton B 1995 Tetrodes markedly improve the reliability and yield of multiple single- unit isolation from multi- unit recordings in cat striate cortex J. Neurosci. Methods 63 43- 54  
Habib A G, Cameron M A, Suaning G J, Lovell N H and Morley J W 2013 Spatially restricted electrical activation of retinal ganglion cells in the rabbit retina by hexapolar electrode return configuration J. Neural Eng. 10 036013  
Heffer L F and Fallon J B 2008 A novel stimulus artifact removal technique for high- rate electrical stimulation J. Neurosci. Methods 170 277- 84  
Henze D A, Borhegyi Z, Csiszvari J, Mamiya A, Harris K D and Buzsaki G 2000 Intracellular features predicted by extracellular recordings in the hippocampus in vivo J. Neurophysiol. 84 390- 400  
Horsager A, Greenberg R J and Fine I 2010 Spatiotemporal interactions in retinal prosthesis subjects Investigative Ophthalmology Vis. Sci. 51 1223- 33  
Humayun M S, de Juan E Jr, Weiland J D, Dagnelie G, Katona S, Greenberg R J and Suzuki S 1999 Pattern electrical stimulation of the human retina Vis. Res. 39 2569- 76  
Jensen R J and Rizzo J F 2006 Thresholds for activation of rabbit retinal ganglion cells with a subretinal electrode Exp. Eye Res. 83 367- 73  
Jepson L, Hottovy P, Gunning D, Mathieson K, Dabrowski W, Litke A and Chichilnisky E 2014 Spatially patterned electrical stimulation to enhance resolution of retinal prostheses J. Neurosci. 34 4871- 81  
Jones B W, Watt C B, Frederick J M, Baehr W, Chen C K, Levine E M, Milam A H, Lavail M M and Marc R E 2003 Retinal remodeling triggered by photoreceptor degenerations J. Comparative Neurology 464 1- 16  
Kameneva T, Abramian M, Zarelli D, Nesic D, Burkitt A N, Meffin H and Grayden D B 2015 Spike history neural response model J. Comput. Neurosci. 38 463- 81  
Knierim J J and Van Essen D C 1992 Neuronal responses to static texture patterns in area V1 of the alert macaque monkey J. Neurophysiol. 67 961- 80  
Kotecha A, Zhong J, Stewart D and da Cruz L 2014 The argus II prosthesis facilitates reaching and grasping tasks: a case series BMC Ophthalmology 14 71  
Lamme V A, Zipser K and Spekreijse H 1998 Figure- ground activity in primary visual cortex is suppressed by anesthesia Proc. Natl Acad. Sci. 95 3263- 8  
Livingstone M S and Hubel D H 1981 Effects of sleep and arousal on the processing of visual information in the cat Nature 291 554- 61  
Mails I and Kruger L 1956 Multiple response and excitability of cat's visual cortex J. Neurophysiol. 19 172- 86  
Marc R E, Jones B W, Watt C B and Strettoi E 2003 Neural remodeling in retinal degeneration Prog. Retinal Eye Res. 22 607- 55  
Matteucci P B, Chen S C, Tsai D, Dodds C W D, Dokos S, Morley J W, Lovell N H and Suaning G J 2013 Current steering in retinal stimulation via a quasimonopolar stimulation paradigm Investigative Ophthalmology Vis. Sci. 54 4307- 20  
Maturana M I, Apollo N V, Hadjinicolaou A E, Garrett D J, Cloherty S L, Kameneva T, Grayden D B, Ibbotson M R and Meffin H 2016 A simple and accurate model to predict responses to multi- electrode stimulation in the retina PLoS Comput. Biol. 12 e1004849  
Mitra P P and Pesaran B 1999 Analysis of dynamic brain imaging data Biophys. J. 76 691- 708  
Mitzdorf U 1985 Current source- density method and application in cat cerebral cortex: investigation of evoked potentials and EEG phenomena Physiol. Rev. 65 37- 100  
Nakauchi K, Fujikado T, Kanda H, Morimoto T, Choi J S, Ikuno Y, Sakaguchi H, Kamei M, Ohji M and Yagi T 2005 Transretinal electrical stimulation by an intrascleral multichannel electrode array in rabbit eyes Graefe's Arch. Clin. Exp. Ophthalmology 243 169- 74  
Niell C M and Stryker M P 2010 Modulation of visual responses by behavioral state in mouse visual cortex Neuron 65 472- 9  
O'Hearn T M, Sadda S R, Weiland J D, Maia M, Margalit E and Humayun M S 2006 Electrical stimulation in normal and retinal degeneration (rd1) isolated mouse retina Vis. Res. 46 3198- 204  
Pillow J W, Paninski L, Uzzell V J, Simoncelli E P and Chichilnisky E 2005 Prediction and decoding of retinal ganglion cell responses with a probabilistic spiking model J. Neurosci. 25 11003- 13  
Pu M, Xu L and Zhang H 2006 Visual response properties of retinal ganglion cells in the royal college of surgeons dystrophic rat Investigative Ophthalmology Vis. Sci. 47 3579- 85  
Rizzo J F, Wyatt J, Loewenstein J, Kelly S and Shire D 2003 Perceptual efficacy of electrical stimulation of human retina with a microelectrode array during short- term surgical trials Investigative Ophthalmology Vis. Sci. 44 5362- 9  
Salzman C D, Britten K H and Newsome W T 1990 Cortical microstimulation influences perceptual judgements of motion direction Nature 346 174- 7  
Schoolman A and Evarts E V 1959 Responses to lateral geniculate radiation stimulation in cats with implanted electrodes J. Neurophysiol. 22 112- 29  
Schwartz G and Rieke F 2011 Nonlinear spatial encoding by retinal ganglion cells: when \(1 + 1 = 2\) J. Gen. Physiol. 138 283- 90  
Shivdasani M N, Fallon J B, Luu C D, Cicione R, Allen P J, Morley J W and Williams C E 2012 Visual cortex responses to single- and simultaneous multiple- electrode stimulation of the retina: implications for retinal prostheses Investigative Ophthalmology Vis. Sci. 53 6291- 300  
Shivdasani M N, Sinclair N C, Dimitrov P N, Varsamidis M, Ayton L N, Luu C D, Perera T, McDermott H J and Blamey P J 2014 Factors affecting perceptual thresholds in a suprachoroidal retinal prosthesisfactors affecting retinal prosthesis thresholds Investigative Ophthalmology Vis. Sci. 55 6467- 81  
Stasheff S F 2008 Emergence of sustained spontaneous hyperactivity and temporary preservation of OFF responses in ganglion cells of the retinal degeneration (rd1) mouse J. Neurophysiol. 99 1408- 21  
Stingl K, Bartz- Schmidt K U, Besch D, Braun A, Bruckmann A, Gekeler F, Greppmaier U, Hipp S, Hördorfer G and Kernstock C 2013 Artificial vision with wirelessly powered subretinal electronic implant alpha- IMS Proc. R. Soc. B 280 20130077  
Stingl K, Bartz- Schmidt K U, Besch D, Chee C K, Cottriall C L, Gekeler F, Groppe M, Jackson T L, MacLaren R E and Koitschev A 2015 Subretinal visual implant alpha IMS- clinical trial interim report Vis. Res. 111 149- 60  
Stone J 1983 On the understanding of visual processing in the diencephalon Parallel Processing in the Visual System (New York: Springer) pp 149- 93  
Sun J, Lu Y, Cao P, Li X, Cai C, Chai X, Ren Q and Li L 2011 Spatiotemporal properties of multipeaked electrically evoked potentials elicited by penetrative optic nerve stimulation in rabbits Investigative Ophthalmology Vis. Sci. 52 146- 54  
Suzuki S, Humayun M S, Weiland J D, Chen S- J, Margalit E, Piyathaisere D V and de Juan J E 2004 Comparison of electrical stimulation thresholds in normal and retinal degenerated mouse retina Japan. J. Ophthalmology 48 345- 9  
Thomson D J 1982 Spectrum estimation and harmonic analysis Proc. IEEE 70 1055- 96  
Tusa R, Palmer L and Rosenquist A 1978 The retinotopic organization of area 17 (striate cortex) in the cat J. Comparative Neurology 177 213- 35  
van Wezel R J, Lankheet M J, Fredericksen R, Verstraten F A and van de Grind W 1997 Responses of complex cells in cat area 17 to apparent motion of random pixel arrays Vis. Res. 37 839- 52  
Villalobos J, Allen P J, McCombe M F, Ulaganathan M, Zamir E, Ng D C, Shepherd R K and Williams C E 2012 Development of a surgical approach for a wide- view suprachoroidal retinal prosthesis: evaluation of implantation trauma Graefe's Arch. Clin. Exp. Ophthalmology 250 399- 407  
von der Heydt R and Peterhans E 1989 Mechanisms of contour perception in monkey visual cortex. I. Lines of pattern discontinuity J. Neurosci. 9 1731- 48  
Wilke R, Gabel V- P, Sachs H, Schmidt K- U B, Gekeler F, Besch D, Szurman P, Stett A, Wilhelm B and Peters T 2011 Spatial resolution and perception of patterns mediated by a subretinal 16- electrode array in patients blinded by hereditary retinal dystrophies Investigative Ophthalmology Vis. Sci. 52 5995- 6003  
Wong Y T, Halupka K, Kameneva T, Cloherty S L, Grayden D B, Burkitt A N, Meflin H and Shivdasani M N 2016 Spectral distribution of local field potential responses to electrical stimulation of the retina J. Neural Eng. 13 036003

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
