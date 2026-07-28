```
@article{hallum2008image,
  title={Image Analysis for Microelectronic Retinal Prosthesis},
  author={Luke E. Hallum and Shaun L. Cloherty and Nigel H. Lovell},
  journal={IEEE Transactions on Biomedical Engineering},
  year={2008},
  volume={55},
  pages={344-346},
  doi={10.1109/tbme.2007.903713},
  url={https://ieeexplore.ieee.org/document/4360111}
}
```

---

# Image Analysis for Microelectronic Retinal Prosthesis

L. E. Hallum\*, S. L. Cloherty, and N. H. Lovell

Abstract—By way of extracellular, stimulating electrodes, a microelectronic retinal prosthesis aims to render discrete, luminous spots—90- called phosphenes—in the visual field, thereby providing a phosphene image (PI) as a rudimentary remediation of profound blindness. As part thereof, a digital camera, or some other photosensitive array, captures frames, frames are analyzed, and phosphenes are actuated accordingly by way of modulated charge injections. Here, we present a method that allows the assessment of image analysis schemes for integration with a prosthetic device, that is, the means of converting the captured image (high resolution) to modulated charge injections (low resolution). We use the mutual- information function to quantify the amount of information conveyed to the PI observer (device implantee), while accounting for the statistics of visual stimuli. We demonstrate an effective scheme involving overlapping, Gaussian kernels, and discuss extensions of the method to account for short- term visual memory in observers, and their perceptual errors of omission and commission.

Index Terms—Computational vision, functional electrical stimulation (FES), image processing, information theory, low vision, signal processing, vision prosthesis.

## I. INTRODUCTION

There exists a number of studies that have sought to quantify the usefulness of prosthetic vision for performing daily tasks, e.g., reading [1] and face recognition [2]. However, there is scarce treatment amongst this literature as to what constitutes effective image analysis for integration with a prosthetic device. In the same way that speech processing in the cochlear implant assists speech recognition (improved clinical outcomes in recent years are one- third attributed to speech processing improvements [3]), a well designed image analysis scheme should improve the prosthetic vision afforded retinal implantee. In a previous study, we assessed the visual fixation and pursuit capabilities of subjects afforded simulated prosthetic vision [4]. There, subjects were required to track a small, high- contrast target, at times stationary and at times moving, with the central phosphene of a phosphene array. The data showed that subjects used some areas of the phosphene array in preference to others. That is to say, by way of analogy, subjects developed an "artificial" preferred retinal locus (APRL). Further, we found that a nontrivial image analysis scheme (overlapping Gaussian kernels) afforded subjects improved object tracking as compared with regional averaging (uniform- intensity kernels)—the trivial scheme that is used extensively in the existing literature.

Manuscript received December 17, 2006; revised May 15, 2007. Asterisk indicates corresponding author.

\*L. E. Hallum is with the Graduate School of Biomedical Engineering, University of New South Wales, Anzac Parade, Sydney 2052, Australia, and also with the Department of Psychology and Center for Neural Science, New York University, New York, NY 10003 USA (e- mail: hallum@cns.nyu.edu).

S. L. Cloherty is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney 2052, Australia and also with the Research School of Biological Sciences, The Australian National University, Canberra 2601, Australia.

N. H. Lovell is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney 2052, Australia and also with the National ICT Australia, Eveleigh 1430, Australia.

Digital Object Identifier 10.1109/TBME.2007.903713

\*Sufferers of central scotoma likewise develop (new) preferred retinal loci in the vicinity of the fovea [5].

> **Image description.** A layered diagram illustrating a numerical setup for image processing, depicting the flow of information from a raw input image to a resulting phosphene image. The diagram consists of three stacked rectangular panels, each representing a stage in the visual processing model.
>
> The layers are arranged vertically, with the information flow moving upward, indicated by an arrow between the bottom and middle layers.
>
> 1.  **Raw image, R (Bottom Layer):** This is the largest, lightest gray rectangle at the base of the diagram. It is currently blank, representing the initial input stimulus.
> 2.  **Image analysis scheme (Middle Layer):** Positioned above the raw image, this layer is a medium gray rectangle. It contains a pattern of overlapping, concentric, white/light gray circular outlines, which visually represent the image analysis filters (context suggests these are nonoverlapping Gaussian kernels).
> 3.  **Phosphene image (PI) (Top Layer):** This is the smallest, darkest rectangle at the top. It displays a grid of distinct, white/light gray circular outlines arranged in a hexagonal mosaic pattern, representing the final output of the processing scheme.
>
> An upward-pointing arrow is placed between the "Raw image, R" and the "Image analysis scheme," signifying the direction of data processing.
>
> The visible text labels are:
> *   "Phosphene image (PI)" (Top layer)
> *   "Image analysis scheme" (Middle layer)
> *   "Raw image, R" (Bottom layer)

<center>Fig. 1. Numerical setup. The raw image (bottom layer), consisting of an impulsive stimulus, is analyzed by the image analysis scheme (middle layer) which, in turn, generates the phosphene image (upper layer). Thus, we are considering the response of a seven-phosphene array to a single spatial impulse somewhere in the field covered by their input sensitivity profiles. Note that phosphenes are arranged in a hexagonal mosaic, and the example shown involves a scheme of nonoverlapping Gaussian kernels. </center>

What follows provides an information theoretic explanation for the fixation and pursuit results in [4]. Further, it suggests improvements to the Gaussian analysis scheme used there, plus a means of designing an image analysis scheme in post- implantation device fitting.

## II. METHOD

The flow of information from the raw image \(R\) to the phosphene image (PI) is modelled as shown in Fig. 1. A crude means of assessing the efficacy of an image analysis scheme would be to move the impulse through very many locations in \(R\) , and tally the number of unique PIs generated. However, this does not account for a subject's use of an APRL, the relative frequencies of PIs, nor subjective, perceptual errors of omission and commission. Therefore, the present method proposes to assess the image processing scheme based on the mutual- information function [6]

\[\begin{array}{rl} & I(p;Q) = H(Y) - H(Y\mid X)\\ & \qquad = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}p(x)Q(y\mid x)\\ & \qquad \times \log_2\left\{\frac{Q(y\mid x)}{\int_{-\infty}^{\infty}p(x)Q(y\mid x)dx}\right\} dy dx \mathrm{bits} \end{array} \quad (1)\]  

where \(X\) is the input vector, dimensionality two, that describes the location of the impulse; \(Y\) is the output vector, dimensionality \(n_p\) (number of phosphenes), that describes the activations of phosphenes comprising the PI; \(H(\cdot)\) denotes entropy; \(p(x)\) is a first- order probability density function (p.d.f.) that models the APRL, that is, the probability of an impulse taking a particular location relative to the PI; and, \(Q(y\mid x)\) is the forward transition matrix (FTM), that is, the probability of \(Y\) being the output when \(X\) is the input. The mutual- information function effectively measures the degree to which seeing the PI reduces the uncertainty as to the location of the impulse, or, to rephrase, how well an ideal observer may fixate and pursue a small, high- contrast target.

In detail, the parameters involved are these: the number of phosphenes, \(n_p\) ( \(n_p = 7\) in Fig. 1), and their locations within the region, \(R\) ; the bivariate p.d.f., \(p(x)\) , that serves as the APRL model; the number of levels to which phosphene activations are quantized, \(n_q\) ; and the image analysis scheme for assessment.

Each mutual- information measurement was generated as follows using Octave [7]. The impulse was moved through 100000 locations generated by a continuous, bivariate p.d.f., uniform on \(R\) . At each location, \(R\) was analyzed by the scheme in question (each kernel operated on a finite support and was normalized such that the integral on that support was 1.0), and the resulting \(n_p\) outputs were quantized to \(n_q\) levels, clipped at 1.0, thus generating a PI. Each unique PI was assigned a key; keys were stored in a matrix along with the locations of all impulses that generated that key (or PI), and the probability of occurrence of each of these impulses according to \(p(x)\) . From this matrix, the FTM was generated, and all of the matrix operations of (1) implemented. The advantage of this statistical approach is that only those PIs that arise (on the order of 1000 images for a system of seven phosphenes) factor in to computations, as opposed to all possible PIs (on the order of 100000 for a system of seven phosphenes), which would be computationally prohibitive. The FTM is therefore conveniently thought of as a continuous, bivariate function (the variables being impulse location and PI) that comprises Dirac functions where an impulse generates a PI, and is zero elsewhere. The Octave code is available upon request from the corresponding author.

## III. RESULTS AND DISCUSSION

The results presented here involve an hexagonal array of seven phosphenes, as shown in Fig. 1. Whilst the method is easily extended to arbitrary arrangements of many phosphenes, we concentrated on these parameters since our previous work involved hexagonal arrays and showed that practiced subjects can fixate and pursue a small target using only seven neighboring phosphenes (of a larger array, that is, \(p(x) \approx 0\) at eccentricity) [4]. Fig. 2(a) demonstrates the relative efficacy of two analysis schemes—one Gaussian based, and the other involving uniform- intensity kernels. For the former (filled circles), the abscissa ("kernel parameter") refers to the standard deviation (s.d.) of the kernels used, all seven of which were identical and isotropic. For the latter (filled squares), the abscissa refers to the diameters of the uniform kernels in question (again, identical and isotropic). As shown, for a bivariate, uniform APRL model, a scheme comprising Gaussian kernels, as compared to a scheme comprising uniform- intensity kernels, makes for more information in the PI. This beneficial effect is maximized when Gaussian kernels take on s.d. equal to 0.66 PP (the minimum phosphene spacing), which amounts to an information gain of approximately two- fold over the optimal uniform- intensity scheme (diameter 1.38 PP). The figure also demonstrates the effect of quantization—the two curves (filled and unfilled circles) compare identical Gaussian schemes, the outputs of which were quantized to \(n_q = 8\) and \(n_q = 4\) levels respectively, making for, approximately, a one- fifth reduction in information. Note that these two curves take similar forms, and thus the optimal analysis scheme (s.d. = 0.66 PP) is shown to be robust in the face of increasing quantization noise. The effect of quantization is an important consideration given that the prosthetic device, if the analogous cochlear implant serves as a guide [8], will likely involve limited intensity resolution.

Fig. 2(b) compares Gaussian and uniform- intensity schemes for a bivariate normal APRL model. This better approximates our experimental data [4], wherein the first- order statistics of subjects' deviations about the target were well fitted by bivariate normal distributions with s.d. equal

> **Image description.** A technical image consisting of two stacked line graphs, labeled (a) and (b), which compare the relationship between "mutual information (bits)" and "kernel parameter (PP)" for different image analysis schemes.
>
> **Common Features:**
> Both panels are line graphs with the Y-axis labeled "mutual information (bits)" ranging from 0 to 10, and the X-axis labeled "kernel parameter (PP)" ranging from 0 to 2.0. Each panel displays three distinct data series, differentiated by marker style: filled black circles, filled black squares, and unfilled white circles. All three series exhibit a similar unimodal pattern, starting at a low mutual information value, rising sharply to a peak around a kernel parameter of 1.0, and then gradually declining.
>
> **Panel (a) Details:**
> Panel (a) shows the performance of three schemes. The filled circles and filled squares generally achieve higher peak mutual information values compared to the unfilled circles. The curves for the filled circles and filled squares are closely aligned, peaking near 1.0 on the PP axis, reaching mutual information values between 8 and 10 bits. The unfilled circles also peak near 1.0 but achieve a lower maximum mutual information, around 7 bits.
>
> **Panel (b) Details:**
> Panel (b) displays a similar set of three data series (filled circles, filled squares, and unfilled circles). The overall shape and trend of the curves are consistent with Panel (a). However, Panel (b) includes two small black arrows pointing to specific data points on the curves, located between PP values of 0.5 and 1.0. These arrows indicate specific schemes or data points of interest, likely referencing external studies. The peak mutual information values in Panel (b) are generally comparable to those in Panel (a), with the filled markers achieving the highest peaks.
>
> The visual arrangement suggests a comparative study, where Panel (a) represents one set of conditions (e.g., a bivariate uniform APRL model) and Panel (b) represents a different set of conditions (e.g., a bivariate normal APRL model), with the different marker styles representing different kernel types (e.g., isotropic Gaussian kernels vs. uniform-intensity kernels) and quantization levels.

<center>Fig. 2. Comparison of effect of image analysis schemes on information conveyed to the phoneme image for an hexagonal array of seven phonemes. (a) For a bivariate uniform APRL model, a scheme comprising isotropic, identical Gaussian kernels (filled circles) and uniform-intensity kernels (filled squares) quantized to \(n_q = 8\) levels. Unfilled circles show Gaussian scheme quantized to \(n_q = 4\) levels. (b) As per (a) but a bivariate normal APRL model with s.d. \(= 0.25\) PP. Arrows refer to those schemes used in Hallum et al. [4]. (PP: the minimum phoneme spacing). </center>

to 0.14 PP for fixation and 0.27 PP for pursuit. Note that, as the APRL model narrows (uniform to normal), the optimal Gaussian kernels (0.66 PP versus 0.54 PP) and uniform- intensity kernels (1.38 PP versus 1.20 PP) likewise narrow. This makes intuitive sense; as target tracking accuracy increases, the image analysis scheme in question admits more high- frequency information (by way of narrower analysis kernels). The arrows in Fig. 2(b) indicate the schemes that best approximate those used in the Hallum et al. [4] study, wherein the Gaussian- based scheme, as compared to the uniform- intensity scheme, made for improved fixation and pursuit accuracies of \(35.8\%\) and \(6.8\%\) , respectively.  

Since the tightest packing of equi- sized circles on a plane is hexagonal, the mosaic arrangement of phonemes in Fig. 1 lends itself to the use of identical, isotropic kernels. While these may also be used for disordered phoneme arrangements likely to be experienced by implanctees (e.g., a recent clinical trial [9]), our preliminary work shows that further information gains may be achieved by geometric transfor mation of kernels based on the Voronoi cells formed about disordered phoneme locations [10]. The present method is readily extended to disordered phoneme arrangements and anisotropic kernels.

The method proposed here may also be extended to account for perceptual errors and STVM limitations of the PI observer. For example, if a subject is wont to miss the activation of, say, a particular peripheral phoneme (error of omission), this can be accounted for in the FTM (the probability of the peripheral perception is reduced from 1.0 and that of no perception is increased); compensatory adjustments in the image analysis scheme may then be investigated. Similarly, the way in which an observer moves the phoneme array when scanning a scene or image (a dynamic APRL) may be accounted for in the analysis scheme (which then becomes adaptive) by extending \(p(x)\) in (1) to higher order statistics (informed by visuomotor data as in [4]).

There is previous work that frames retinal prosthesis in terms of information theory [11], [12]. Those studies sought to quantify the information capacity of a prosthesis, for comparison with an intact visual system, based on electrophysiological measurements in cat cortex. In contrast, the present approach aims to make more effective use, through image processing, of the electronical bottleneck [13, p. 405] that the device imposes. Overall, we hope to inform post- surgical device programming, wherein a clinician uses behavioral measures to determine parameters particular to a subject (e.g., phoneme locations and the intensity resolution of each), and then uses the present method to fit an image analysis scheme accordingly. This bears analogy to the post- surgical programming of a cochlear implant, and we hope will make for improved clinical outcomes.

## REFERENCES

[1] J. Sommerhalder, E. Oueghlani, M. Bagnoud, U. Leonards, A. B. Safran, and M. Pelizzone, "Simulation of artificial vision: I. Eccentric reading of isolated words, and perceptual learning," Vis. Res., vol. 43, pp. 269- 283, 2003.  
[2] R. W. Thompson, G. D. Barnett, M. S. Humayun, and G. Dangelie, "Facial recognition using simulated prosthetic pixelized vision," Invest. Ophthalmol. Vis. Sci, vol. 44, pp. 5035- 5042, 2003.  
[3] J. T. Rubinstein and C. A. Miller, "How do cochlear prostheses work?," Curr. Opin. Neurobiol., vol. 9, pp. 399- 404, 1999.  
[4] L. E. Hallum, G. J. Suaning, D. S. Taubman, and N. H. Lovell, "Simulated prosthetic visual fixation, saccade, and smooth pursuit," Vis. Res., vol. 45, pp. 775- 788, 2005.  
[5] G. T. Timberlake, M. A. Mainster, E. Peli, R. A. Augliere, E. A. Essock, and L. E. Arend, "Reading with a macular scotoma. I. retinal location of scotoma and fixation area," Invest. Ophthalmol. Vis. Sci., vol. 27, pp. 1137- 1147, 1986.  
[6] R. E. Blahut, Principles and Practice of Information Theory. Norwood, MA: Addison- Wesley, 1987.  
[7] J. W. Eaton, GNU Octave Manual. Bristol, U.K.: Network Theory Limited, 2002.  
[8] P. C. Loizou, M. Dorman, O. Poroy, and T. Spahr, "Speech recognition by normal- hearing and cochlear implant listeners as a function of intensity resolution," J. Acoust. Soc. Amer., vol. 108, pp. 2377- 2387, 2000.  
[9] M. S. Humayun, J. D. Weiland, G. Y. Fujii, R. Greenberg, R. Williamson, J. Little, B. Mech, V. Cimmarusti, G. V. Boemel, G. Dagenlie, and E. d. Juan, "Visual perception in a blind subject with a chronic microelectronic retinal prosthesis," Vis. Res., vol. 43, pp. 2573- 2581, 2003.  
[10] L. E. Hallum, G. J. Suaning, D. S. Taubman, and N. H. Lovell, "Towards photosensor movement- adaptive image analysis in an electronic retinal prosthesis," in Proc. 26th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBS), 2004, pp. 4165- 4168.  
[11] M. Eger, M. Wilms, R. Eckhorn, T. Schanze, and L. Hesse, "Retino- cortical information transmission achievable with a retina implant," Biosystems, vol. 79, pp. 133- 142, 2005.  
[12] R. Eckhorn, M. Wilms, T. Schanze, M. Eger, L. Hesse, U. T. Eysel, Z. F. Kisvarday, E. Zrenner, F. Gekeler, H. Schwahn, K. Shinoda, H. Sachs, and P. Walter, "Visual resolution with retinal implants estimated from recordings in cat visual cortex," Vis. Res., vol. 46, pp. 2675- 2690, 2006.  
[13] G. M. Clark, Cochlear Implants. New York: Springer, 2003.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
