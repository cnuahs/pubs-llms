```
@article{hallum2006sampling,
  title={Psychophysics of Prosthetic Vision: II. Stochastic Sampling, the Phosphene Image, and Noise},
  author={Luke E. Hallum and Spencer C. Chen and Shaun L. Cloherty and Nigel H. Lovell},
  journal={28th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2006},
  pages={1634-1637},
  doi={10.1109/iembs.2006.259957},
  url={https://ieeexplore.ieee.org/document/4462082}
}
```

---

# Psychophysics of Prosthetic Vision: II. Stochastic Sampling, the Phosphene Image, and Noise

Luke E. Hallum, Spencer C. Chen, Shaun L. Cloherty, and Nigel H. Lovell

Abstract—Stimulation of the diseased retina via an intraocular electrode array is a proposed means of restoring some vision to the profoundly blind. A prosthetic device to this end would involve post- implantation calibration (analogous to cochlear implant fitting), wherein the subject indicates those discrete positions in the visual field where luminous percepts are elicited. This procedure would be a source of noise, because the indicated positions would only approximate the actual positions in the visual field. Put differently, the procedure introduces sampling jitter, and would therefore affect clinical outcomes such as mobility and reading speeds. The nature of this noise is the concern of the present paper; we derive an expression for the noise power spectrum as it relates to the statistical nature of the sampling jitter. We show that, generally, jitter has greater effect on higher spatial- frequencies, that is, those areas of the implantee's visual perception that represent fine detail are more prone to noise. More specifically, the noise spectrum depends on the characteristic function of the random variable describing the sampling jitter. Our results signal the need for experimental work that characterizes sampling jitter in implantees, plus the need for simulations that allow a better understanding of perception and the noisy phosphene image.

## I. INTRODUCTION

THE microelectronic retinal prosthesis (for review see [1]) proposes, by way of an intraocular array of stimulating electrodes, to render luminous spots (so- called phosphenes which together comprise the phosphene image) in fixed locations of the visual field of the profoundly blind implantee. By way of analogy, in the cochlear implant, the implanted subject undergoes post- surgical, psychophysical calibration sessions wherein perceptual thresholds and maximum comfortable loudness are determined at each electrode. We envision a similar procedure for retinal implantees wherein, via psychophysical means, the locations in the visual field occupied by phosphenes are indicated. These locations inform the image processing that lies functionally intermediate to the intraocular electrode array and the digital camera (worn on the body) that acquires real- world scenes; specifically, the locations determine where the real- world scenes are sampled prior to the corresponding activations of electrodes. This calibration procedure would be necessarily inaccurate. That is to say, the phosphene locations as indicated by the subject only approximate the actual locations of phosphenes in the visual field. This introduces noise to

L. E. Hallum, S. C. Chen and S. L. Cloherty are with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, NSW, Australia, 2052. 
N. H. Lovell is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, NSW, Australia, 2052, and National Information and Communications Technology Australia (NICTA), Eveleigh, NSW, Australia, 1430.

the phosphene image that is more pronounced where high- spatial- frequency information (fine detail) in the real- world scene is concerned. This concept is depicted in Fig. 1. Note that, in the figure, phosphenes are arranged in an orderly fashion in the visual field (of the phosphene image observer). In practice we would expect irregularity in the phosphene layout due to the electrotonicity of the retina (e.g., see [2], [3]).

In the following section, we derive an expression (in one dimension) for the power contained in this noise as a function of spatial- frequency of real- world scenes, and the relationship between the noise and the statistics of the sampling jitter. In the Discussion, we take up the potential clinical significance of this result and signal the need for work concerning perception and the phosphene image in the presence of noise.

## II. STATISTICAL ANALYSIS OF SAMPLING JITTER

We have formulated our approach as follows. Firstly, consider a zero- phase cosinusoid with frequency \(u_{a}\) on the range \([0,1]\) , that is, \((1 + \cos (2\pi u_{a}x)) / 2\) , sampled at \(x = 0\) . If the sample point is subject to a jitter, \(\chi\) , then the resulting amplitude error is given by \(\epsilon = (1 + \cos (2\pi u_{a}x)) / 2 - (1 + \cos (2\pi u_{a}(x + \chi)) / 2\) evaluated at \(x = 0\) . This expression for amplitude error may be generalised as,

\[\epsilon (x,u;A) = \frac{1}{2}\cos (2\pi A) - \frac{1}{2}\cos (2\pi u(x + A / u)), \quad (1)\]

where \(A\) , \(0 \leq A \leq 1\) , is a parameter that, for the meantime, takes the value \(A = 0\) , but will later be used to account for shifts, over a single period, of the original zero- phase cosinusoid. Therefore, the power contained in the error is related to

\[\epsilon^2 (x,u;A) = \frac{1}{4}\cos^2 (2\pi A)\\ -\frac{1}{2}\cos (2\pi A)\cos (2\pi u(x + A / u))\\ +\frac{1}{4}\cos^2 (2\pi u(x + A / u)).\]

The statistical average over \(x\) (see [5, p. 12]), then, of the power contained in the error is given by

\[\begin{array}{l}{E(\epsilon^2 (x,u;A)) = \frac{1}{4}\cos^2 (2\pi A)\int_{-\infty}^{\infty}w(x)dx}\\ {-\frac{1}{2}\cos (2\pi A)\int_{-\infty}^{\infty}w(x)\cos (2\pi u(x + A / u))dx}\\ {+\frac{1}{4}\int_{-\infty}^{\infty}w(x)\cos^2 (2\pi u(x + A / u))dx,} \end{array} \quad (2)\]

> **Image description.** A technical figure, labeled Figure 1, illustrating the effect of sampling jitter on a grayscale image of a face. The figure is composed of four distinct panels arranged in a 2x2 grid, demonstrating the process from the original image to the final rendered results using two different sampling methods.
>
> The panels are described as follows:
>
> *   **Top Left Panel (Source Image):** This panel displays the original grayscale photograph of a woman's face, which serves as the input image for the sampling process.
> *   **Top Right Panel (Sampling Mosaics):** This panel shows the two sampling grids (mosaics) used to extract data from the face image. The grid consists of small 'x' marks. According to the context, one grid represents an ordered sampling pattern, while the other represents a pattern subjected to a small amount of uniform jitter.
> *   **Bottom Left Panel (Ordered Sampling Result):** This panel shows the resulting phoneme image generated using the ordered sampling mosaic. It is characterized by a clean, structured pattern of small dots, accurately representing the features of the face image.
> *   **Bottom Right Panel (Jittered Sampling Result):** This panel shows the phoneme image generated using the jittered sampling mosaic. It also consists of small dots, but unlike the bottom-left panel, this image is visibly noisy, particularly in areas corresponding to fine details like the eyes and hairline, as explained in the accompanying text.
>
> The overall figure demonstrates that while the locations of the sampled features remain congruent between the two methods, the jittered sampling process introduces noise into the final rendered image.

<center>Fig. 1. The effect of sampling jitter on a phoneme image of a face. The face (top, left; image source [4]) is sampled by two mosaics, shown superimposed (top, right); one mosaic is ordered \((\times \mathrm{s})\) and the other is subject to a small amount of uniform jitter \((+ \mathrm{s})\) . The samples from each mosaic are then used to render a phoneme image (ordered sampling: bottom, left; jittered sampling: bottom right); note that locations of phonemes, which are congruent with the ordered sampling mosaic, do not differ between the two phoneme images. The bottom, right phoneme image is therefore noisy. This noise is most pronounced for fine detail, e.g., the eyes and eyebrows, and the hairline. </center>

where \(E(\cdot)\) denotes the expectation operator, and \(w(x)\) is the first- order probability density function (p.d.f.) that governs the sampling jitter. Of course, the first term in Eq. (2) simplifies to \(\cos^2 (2\pi A) / 4\) since the integral equates to 1. The second term relates to the Fourier transform (FT) of \(w(x)\) , that is, the characteristic function (c.f.) of the random variable (r.v.) jitter as follows (see [5, p. 13]):

\[\begin{array}{r l} & {\int_{-\infty}^{\infty}w(x)\cos (2\pi u(x + A / u))d x}\\ & {\qquad = \int_{-\infty}^{\infty}w(x^{\prime} - A / u)\cos (2\pi u x^{\prime})d x^{\prime}}\\ & {\qquad = \Re \{\mathcal{F}\{w(x^{\prime} - A / u)\} \}}\\ & {\qquad = \hat{w} (u)\cos (2\pi A)} \end{array} \quad (3)\]

where we have used a change of variable, \(x^{\prime} = x + A / u\) , \(\Re\) denotes 'the real part of', \(\mathcal{F}\) denotes 'the Fourier transform of', and the circumflex notation denotes a Fourier pair, \(w\leftrightarrow \hat{w}\) . These equations involve recognizing that, firstly, \(\int_{-\infty}^{\infty}f(x)\cos (2\pi u x)d x\) equates to the real part of the FT of \(f(x)\) , and that, secondly, shifting \(w\) affects the phase of the

FT, \(\hat{w}\) (see [6, pp. 111- 113]).

The third term in Eq. (2) relates to the constricted c.f. of r.v. jitter like so:

\[\begin{array}{l}{\int_{-\infty}^{\infty}w(x)\cos^{2}(2\pi u(x + A / u))d x}\\ {= \int_{-\infty}^{\infty}w(x^{\prime} - A / u)\cos^{2}(2\pi u x^{\prime})d x^{\prime}}\\ {= \frac{1}{2}\int_{-\infty}^{\infty}w(x^{\prime} - A / u)(\cos (4\pi u x^{\prime}) + 1)d x^{\prime}}\\ {= \frac{1}{2}\int_{-\infty}^{\infty}w(x^{\prime} - A / u)\cos (4\pi u x^{\prime})d x^{\prime} + \frac{1}{2}}\\ {= \frac{1}{2}\int_{-\infty}^{\infty}w(x^{\prime \prime} / 2 - A / u)\cos (2\pi u x^{\prime \prime})d x^{\prime \prime} + \frac{1}{2}}\\ {= \frac{1}{2}\Re \{\mathcal{F}\{w(x^{\prime \prime} / 2 - A / u)\} \} +\frac{1}{2}}\\ {= \frac{1}{2}\hat{w} (2u)\cos (2\pi A) + \frac{1}{2},} \end{array} \quad (4)\]

where the approach is much the same as in Eq. (3), and a second change of variable was used: \(x^{\prime} = x^{\prime \prime} / 2\) . Then,

Eq. (2) simplifies as follows,

\[E(\epsilon^{2}(x,u;A)) = \left(\frac{1}{4} -\frac{1}{2}\hat{w} (u)\right)\cos^{2}(2\pi A)\] \[\qquad +\frac{1}{8}\hat{w} (2u)\cos (2\pi A) + \frac{1}{8}\]

which, so as to account for all possible (and equally probable) phases of what was originally our zero- phase cosinusoid, we integrate on the interval \(A = [0,1]\) to get

\[E(\epsilon^{2}(x,u)) = \int_{0}^{1}\left\{\frac{1}{4} (1 - 2\hat{w} (u))\cos^{2}(2\pi A)\right.\] \[\qquad \left. + \frac{1}{8}\hat{w} (2u)\cos (2\pi A) + \frac{1}{8}\right\} dA\] \[\qquad = \frac{1}{4} (1 - \hat{w} (u)).\]

This equation (Eq. (5)) expresses the power spectrum of the noise. See Fig. 2. One critical observation to be made is the effect of the first- order p.d.f. that governs the sampling jitter, \(w(x)\) . The FT of \(w(x)\) , that is, the c.f. of the r.v. jitter, determines the rate of growth of the noise power. With the reciprocal relationship of \(w\) and \(\hat{w}\) in mind, as the p.d.f. \(w(x)\) narrows, noise power grows more slowly with frequency. In the limiting case, when sample positions are determined (subject to no jitter), then \(w(x) = \delta (x) \leftrightarrow 1\) , where \(\delta (x)\) denotes the Dirac delta function, and so \(E(\epsilon^{2}(x,u)) = (1 - 1) / 4 = 0\) . That is to say, as expected, in the absence of jitter, no noise is introduced to the phonosphere image. At the other extreme, when jitter is very broad, then all frequencies are noised except a d.c. offset.

> **Image description.** A line graph titled "Fig. 2. Growth of noise power with frequency for two classes of sampling jitter" illustrates the relationship between noise power and frequency for two different types of sampling jitter.
>
> The graph features a standard Cartesian coordinate system. The vertical axis (Y-axis) is labeled "Power" and ranges from 0 to 0.30, marked in increments of 0.05. The horizontal axis (X-axis) is labeled "Frequency $u$ ($^\circ$)" and ranges from 0 to 20, marked in increments of 5.
>
> Two distinct data series are plotted on the graph, both starting at the origin (0, 0) and exhibiting oscillatory behavior as frequency increases:
>
> 1.  **Solid Line:** This line represents "uniform jitter on $[-0.15^{\circ}, 0.15^{\circ}]$". It rises steeply from the origin, reaching its maximum power (approximately 0.28) around a frequency of $5^\circ$. After this peak, the line oscillates with a decreasing amplitude across the rest of the frequency range.
> 2.  **Dashed Line:** This line represents "normal jitter with standard deviation $\sigma = 0.1^{\circ}$". It also rises from the origin, but less steeply than the solid line, reaching a lower peak power (approximately 0.25) around $5^\circ$. Similar to the solid line, it continues to oscillate with decreasing amplitude.
>
> The figure caption provides the full context for the visual data: "Fig. 2. Growth of noise power with frequency for two classes of sampling jitter: uniform jitter on $[-0.15^{\circ}, 0.15^{\circ}]$ (solid line) and normal jitter with standard deviation $\sigma = 0.1^{\circ}$ (dashed line)." A partial phrase, "noise except d.c. offset," is visible at the top of the image, likely part of a preceding sentence.

<center>Fig. 2. Growth of noise power with frequency for two classes of sampling jitter: uniform jitter on \([-0.15^{\circ}, 0.15^{\circ}]\) (solid line) and normal jitter with standard deviation \(\sigma = 0.1^{\circ}\) (dashed line). </center>

A numerical simulation, using R [7], was undertaken. Analytical and numerical results agreed. At each frequency of a cosine wave on the range \([0,1]\) , and for purely random phase shifts thereof, we computed the mean \((n = 2000)\) of the square of the difference of the cosine sampled at \(x = 0\) , and the same cosine sampled at \(x = \chi\) . In the plot shown in Fig. 3, \(\chi\) was uniform on the interval \([- 0.15^{\circ}, 0.15^{\circ}]\) .

> **Image description.** A line graph titled "Fig. 3. Numerical simulation results" displays the relationship between "Power" and "Frequency $u$ ($^\circ$)" based on numerical simulation data.
>
> The graph features a Cartesian coordinate system with the following axes:
> *   **Y-axis (Vertical):** Labeled "Power," it ranges from 0 to 0.30, marked with increments of 0.05.
> *   **X-axis (Horizontal):** Labeled "Frequency $u$ ($^\circ$)," it ranges from 0 to 20, marked with major tick labels every 5 degrees (0, 5, 10, 15, 20).
>
> The data is represented by a single, continuous black line connecting numerous data points, each marked with a small black cross (+). The curve begins at the origin (0, 0). It rises sharply and rapidly, reaching its highest point (a peak) at approximately $u=5^\circ$, where the power is close to 0.28. Following this initial peak, the line exhibits a pattern of damped oscillations. The power fluctuates between approximately 0.20 and 0.28 as the frequency increases toward 20 degrees, showing several smaller peaks and troughs (e.g., a peak near $u=10^\circ$ and another near $u=15^\circ$).
>
> The visible text includes the figure caption: "Fig. 3. Numerical simulation results. See text for details. Note the..." (The caption is truncated). The axes are clearly labeled with the technical terms "Power" and "Frequency $u$ ($^\circ$)."

<center>Fig. 3. Numerical simulation results. See text for details. Note the agreement with Fig. 2. </center>

## III. DISCUSSION

There is a growing body of literature concerning the phosphene image and perception (e.g., [8], [9], [10]). These studies have involved the recognition of (phosphenized) faces, reading speeds of (phosphenized) text, and the acuity that the phosphene image affords observers. There is no study, however, that addresses the robustness of perception when faced with a noisy phosphene image. This work is underway in the present authors' lab, and is analogous to a study by Friesen et al. [11], which demonstrated declining speech recognition in both cochlear implant listeners and normally hearing listeners (afforded acoustic simulations) as the signal- to- noise ratio decreased from 15 dB to 0 dB. Similar trends are expected concerning perception of the phosphene image. A body of such data could specify the required accuracy of post- implantation visual calibration with a mind to keeping the adverse perceptual effects of sampling jitter to a minimum.

The foregoing, of course, assumes that the phosphene image observer does not, over the cause of practice, learn to compensate completely for sampling jitter. To rephrase, the observer may develop an internal model that effectively denoises the phosphene image. This is also an area of interest to the present authors.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
