```
@article{hallum2006rendering,
  title={Psychophysics of Prosthetic Vision: III. Stochastic Rendering, the Phosphene Image, and Perception},
  author={Luke E. Hallum and Shaun L. Cloherty and David S. Taubman and Gregg J. Suaning and Nigel H. Lovell},
  journal={28th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2006},
  pages={1169-1172},
  doi={10.1109/iembs.2006.259956},
  url={https://ieeexplore.ieee.org/document/4461965}
}
```

---

# Psychophysics of Prosthetic Vision: III. Stochastic Rendering, the Phosphene Image, and Perception

Luke E. Hallum, Shaun L. Cloherty, David S. Taubman, Gregg J. Suaning, and Nigel H. Lovell

Abstract—This paper examines the rendering of luminous spots ("phosphenes") in the visual field, and their stochastic positioning as a means of anti- aliasing the resulting spotty image ("phosphene image"). We derive an equation concerning the correlations of pairs of phosphenes comprising the phosphene image, and show the relationship to the statistics governing the stochastic positioning. We present some examples where stochastic rendering assists the veridical perception of textures, and argue for its superiority as cf. ordered rendering. Our preliminary results suggest that it may be perceptually effective to manufacture disordered arrays of stimulating electrodes for intraocular implantation.

## I. INTRODUCTION

N the primate retina, cones are arranged in a slightly disordered mosaic [1]. Therefore, the light sourced and reflected by real- world objects is rendered on to the visual sense organ in a disordered fashion. Some workers hypothesize that the disordered nature of the retinal image is a central mechanism in the remarkable quality of human vision [2], specifically, its release from aliasing, which one would expect when a fine mosaic (like the cone mosaic) samples an even finer signal (for more discussion, including the role of eye optics, see [3]).

The retinal image and the phosphene image (see Fig. 1) bear similarity, albeit they operate at vastly different scales - seconds of visual arc versus degrees. This latter image is presently of interest to a number of vision researchers (e.g., [4], [5], [6]) as it serves as a visual model of electrical stimulation of the retina, a technique that may restore vision to those profoundly blinded through diseases affecting photoreceptors (for review see [7]). Studies involving the phosphene image have examined the recognition of (phosphenized) faces, reading speeds of (phosphenized) text, and the acuity that the phosphene image affords observers. This approach is analogous to the acoustic modeling of the cochlear implant, wherein mixed bands of colored noise are played to normally hearing listeners as a means of investigating speech processing strategies and implant candidacy criteria (e.g., see [8]). As shown in Fig. 1, the phosphene image is typically

L. E. Hallum and 
S. L. Cloherty are with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, NSW, Australia, 2052. 
D. S. Taubman is with the School of Electrical Engineering and Telecommunications, University of New South Wales, Sydney, NSW, Australia, 2052. 
G. J. Suaning is with the School of Engineering, University of Newcastle, Callaghan, NSW, Australia, 2308. 
N. H. Lovell is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, NSW, Australia, 2052, and National Information and Communications Technology Australia (NICTA), Eveleigh, NSW, Australia, 1430.

comprised of relatively few phosphenes (usually on the order of 100), and is therefore subject to aliasing. Put differently, fine real- world detail is prone to manifest in the phosphene image as spurious low- frequency detail.

With the above in mind, the present authors have become interested in stochastic rendering and its use as an anti- aliasing mechanism, the aim being to improve perceptual outcomes concerning the phosphene image. In the next section, we derive an expression showing that correlations between phosphene pairs comprising the phosphene image tend to be cancelled by stochastic rendering. This, of course, depends on the statistics governing the rendering positions of phosphenes, and is generally more pronounced for high spatial- frequencies of the real- world scene being represented. In the Discussion, we take up the ramifications of all this for the perception of textures.

## II. STATISTICAL ANALYSIS OF THE DISORDERED PHOSPHENE IMAGE

The covariance of any two phosphenes contained in the phosphene image is given by

\[\operatorname {cov}(X,Y) = E(XY) - E(X)E(Y), \quad (1)\]

where \(E(\cdot)\) denotes the expectation operator, and \(X\) and \(Y\) are random variables denoting the levels of activation of the two phosphenes. Then, consider a one- dimensional phosphene image, that is, a colinear array of phosphenes that, as opposed to assuming regular mosaic positions (that occur periodically with frequency \(1 / T_{p}\) ), are slightly (colinearly) displaced according to the probability density function (p.d.f.) denoted as \(w(x)\) . Then, the separation of any near neighboring phosphenes is governed by the sum of two independent random variables (see [10, p. 189]), that is, the p.d.f.

\[w^{\prime}(x) = w(x)*w(x - T_{p}), \quad (2)\]

where the asterisk denotes convolution. If the one- dimensional phosphene image were driven by a cosinusoid with frequency \(f_{s}\) (it is convenient to think of the cosinusoid as an "underlying" texture for representation in the phosphene image), then by way of Eqs. (1) and (2) above, the covariance of near neighbors in the phosphene image is given by

\[\operatorname {cov}(X,Y) = 1 / 8\int_{-\infty}^{\infty}w^{\prime}(x)\cos (2\pi f_{s}x)dx, \quad (3)\]

where \(\cos (2\pi f_{s}x) / 8\) is the mean- removed autocorrelation function of all arbitrarily shifted cosinusoids with frequency

> **Image description.** A technical figure consisting of two side-by-side panels that compare a real-world visual scene with a simulated phosphene image generated by electrical stimulation.
>
> The figure is divided into two distinct panels:
>
> 1.  **Left Panel (Real-World Scene):** This panel contains a photograph of a man's face. The man has dark, somewhat tousled hair and is looking slightly off-camera. The lighting is focused on his face, while the background is uniformly dark or black. This panel represents the "real-world scene" that the retinal prosthesis is intended to process.
>
> 2.  **Right Panel (Phosphene Image):** This panel displays a pattern of luminous spots (phosphenes) against a solid black background. The phosphenes are represented by small, bright white dots. These dots are not randomly distributed; they form a concentrated, roughly circular or elliptical cluster. The density of the dots is highest in the center of the cluster and gradually decreases towards the periphery, suggesting a localized field of stimulation. This panel represents the "phosphene image," which is a visual model of electrical stimulation of the retina.
>
> Below the image, a caption provides context for the visual elements: "le phosphene image (right panel) - a visual model of electrical stimulation of the retina - representing a real-world scene (left panel). Microelectronic retinal prosthesis proposes to render luminous spots (so-called phosphenes), that may be modulated, in the visual field of the implant recipient. Together, phosphenes comprise the phosphene image. (Left panel image source: [9].)"

<center>Fig. 1. An example phosphene image (right panel) - a visual model of electrical stimulation of the retina - representing a real-world scene (left panel). Microelectronic retinal prosthesis proposes to render luminous spots (so-called phosphenes), that may be modulated, in the visual field of the implant recipient. Together, phosphenes comprise the phosphene image. (Left panel image source: [9].) </center>

\(f_{s}\) . Then, \(f_{s}\) in Eq. (3) may be varied, giving a function in frequency, \(f\) , that describes the covariance of near neighbors at various driving frequencies,

\[K(f) = \frac{1}{8}\int_{0}^{\infty}w^{\prime}(x)\cos (2\pi f x)d x. \quad (4)\]

The reader will appreciate that \(K(f)\) is one- sixteenth the cosine transform of \(w^{\prime}(x)\) , that is,

\[\begin{array}{rcl}{K(f)} & = & {\frac{1}{16}\mathcal{F}_c\{w^{\prime}(x)\}}\\ {} & = & {\frac{1}{16}\mathcal{F}\{w^{\prime}(x) + w^{\prime}(-x)\} ,} \end{array} \quad (5)\]

where \(\mathcal{F}_c\{\cdot \}\) and \(\mathcal{F}\{\cdot \}\) denote the cosine and Fourier transforms (FTs) respectively. The parameters for \(K(f)\) are, firstly, \(k\) , the adjacency of the phosphenes in question ( \(k = 1\) for near neighbors, \(k = 2\) for near neighbors but one, etc.), and, secondly, \(w(x)\) , the p.d.f. that governs the stochastic rendering. Since the variance of a sinusoid with amplitude \(A\) is given by \(A^{2} / 2\) , then multiplication by a factor of eight for Eq. (5) yields the correlation coefficient (see [11, pp. 129- 133]), which we will denote \(\rho (f;k,w(x))\) , on the range \(\pm 1\) .

By way of example, we now consider a specific class of phosphene image wherein phosphenes are rendered in positions according to the uniform p.d.f. \(w(x) = \Pi (x / a) / a\) , for \(a\) such that no two phosphenes overlap, where \(\Pi (x)\) denotes a unit- area square pulse on support \([- 1 / 2,1 / 2]\) . Then, from Eq. (2),

\[\begin{array}{rcl}{w^{\prime}(x)} & = & {w(x)*w(x - kT_p)}\\ {} & = & {\frac{1}{a^2}\Pi (x / a)*\Pi (x / a - kT_p)}\\ {} & = & {\frac{1}{a^2}\Lambda (x / a - kT_p),} \end{array} \quad (6)\]

where \(\Lambda (x)\) denotes the triangle function of unity height on support \([- 1,1]\) . Then, the covariance function is the FT of \(\Lambda (x / a - kT_p) / a^2 + \Lambda (kT_p - x / a) / a^2\) .

This is depicted in Fig. 2. Note that as neighbor number, \(k\) , increases, that is, as replicas of \(w^{\prime}(x)\) are more divergent, the frequency of oscillation of \(\rho (f;k,w(x))\) increases. As \(a \to 0\) , where in the limiting case phosphenes take their mosaic positions and each replica of \(w^{\prime}(x)\) is in fact a Dirac function, \(\rho (f;k,w(x))\) oscillates indefinitely between \(\pm 1\) . This latter result indicates complete linear dependence arises between \(k\) - th neighbors when the phosphene image represents fine detail, that is, it indicates that the moire effect- [12] is manifest in the image. We take up this point in the Discussion.

> **Image description.** A line graph titled "Fig. 2" that plots a correlation coefficient against frequency. The graph is set against a white background and features two distinct oscillatory lines: a solid line and a dashed line.
>
> The vertical axis (Y-axis) is labeled $\rho(f; k, w(x))$ and represents the correlation coefficient, ranging from -1 to 1, with major tick marks at -1, 0, and 1. The horizontal axis (X-axis) is labeled "Frequency $f$ ($^\circ$)" and represents the frequency, spanning a range from 0 to approximately 100.
>
> Both the solid and dashed lines exhibit a highly oscillatory, sinusoidal pattern across the entire frequency range. Both lines begin near the value of 1 at the lowest frequencies, dip below the zero line, and then oscillate back toward positive values. The solid line and the dashed line track each other very closely, indicating a strong similarity in their correlation behavior across different frequencies.
>
> Visible text includes the section header "Discussion." at the top left, and the figure caption at the bottom left, which reads: "Fig. 2 The correlation $\rho$ of $k$-th neighboring phosphenes (solid line) in the..." (The caption is truncated). The labels on the axes are clearly defined, providing the context for the plotted data.

<center>Fig. 2. The correlation, \(\rho\) , of \(k\) -th neighboring phosphenes (solid line) in the (uniformly) disordered phosphene image as a function of frequency, \(f\) , of the underlying stimulus. This is effectively the product of the two (dashed) envelopes shown. As neighbor number, \(k\) , increases, the frequency of the cosinusoidal envelope increases. The first zero of the \(\sin c^2 (\cdot)\) envelope relates to the interval of the jitter, \(a\) ; as \(a\) increases, the zero decreases, and vice versa. </center>

## III. DISCUSSION

In the previous section, we derived an expression for the correlations between pairs of phosphenes as a function of \(f\) , the spatial- frequency component of the real- world scene being represented. We showed how this expression is affected

by the statistics that govern the jitter of phonemes, and by \(k\) , the adjacency of phonemes comprising the pair. This allows some predictions as to the appearance of the phoneme image. Firstly, the moire effect tends to be annihilated by stochastic rendering. Secondly, textures involving fine detail take on the qualitative appearance of noise, as opposed to spurious structures.

Figure 3 provides two examples of the effect of stochastic rendering. In Fig. 3(a), a supra- Nyquist sinusoidal grating (top) is represented on an ordered phoneme mosaic (middle) and a disordered phoneme mosaic (bottom). Note that spurious structure is manifest (lower spatial- frequency and changed orientation) on the ordered mosaic (middle), whilst the entire disordered mosaic (bottom) takes on the appearance of noise. Despite the fact that a sine wave is an unlikely natural scene, it bears similarity to numerous features of the built environment which have important bearing on subject mobility, e.g., a flight of stairs. In Fig. 3(b), a Brodatz [13] texture (top) is similarly represented on both ordered (middle) and disordered (bottom) phoneme mosaics. Note how the ordered phoneme mosaic (middle) takes on the appearance of a composite surface (larger phonemes appear to clump together). The disordered phoneme mosaic (bottom), on the other hand, takes on the uniform appearance of noise, which allows it to be segmented by the human visual system as a textural whole.

All of the foregoing begs the question, Why not bandlimit (low- pass filter) the real- world scene prior to sampling so as to avoid aliasing? Work in our lab shows that phoneme image observers typically scan the phoneme mosaic over the real- world scene and integrate phoneme outputs over time (using visual memory) so as to effect an increased sampling density (e.g., see the companion paper in this volume by S. C. Chen et al.). This being the case, to bandlimit the scene would be at odds with subjects' visuomotor behaviors (scanning), effectively decreasing the capacity of the (already impaired) information channel that is the phoneme image. Therefore, anti- aliasing measures that avoid low- pass filtering are of interest.

These results suggest that if a retinal prosthesis renders phonemes in the visual field of the implantee in a disordered fashion then, all other things being equal, this is not perceptually disadvantageous. Rather, disorder affords perceptual benefits. It follows that, if an intraocular electrode array allows deterministic access to the visual field (that is, the layout of electrodes is faithfully reproduced by the layout of phonemes in the visual field), then disordered arrays should be manufactured for implantation, as opposed to the ordered arrays (rectangular and hexagonal) that appear in the literature [14][15][16].

> **Image description.** A scientific figure consisting of two main panels, labeled (a) and (b), which illustrate the effect of stochastic rendering on different visual stimuli when represented on ordered and disordered "phoneme mosaics." The image is organized into a 2x2 grid, with each panel containing three distinct rows representing different types of visual input or rendering.
>
> **Panel (a): Sinusoidal Grating**
> Panel (a) demonstrates the representation of a supra-Nyquist sinusoidal grating.
> *   **Top Row:** Displays the original sinusoidal grating, characterized by high-contrast, parallel, alternating light and dark lines.
> *   **Middle Row:** Shows the ordered phoneme mosaic. This pattern consists of white, elongated, slightly curved lines that maintain the general orientation and spacing of the original grating, but the individual elements are distinct and structured.
> *   **Bottom Row:** Shows the disordered phoneme mosaic. This pattern consists of randomly scattered white dots, representing a loss of structure compared to the ordered mosaic.
>
> **Panel (b): Brodatz Texture**
> Panel (b) demonstrates the representation of a Brodatz texture, a complex, mottled surface.
> *   **Top Row:** Displays the original Brodatz texture, which is a complex, multi-toned gray pattern with fine, irregular detail.
> *   **Middle Row:** Shows the ordered phoneme mosaic. This pattern consists of white, irregularly shaped elements that appear to clump together, giving the visual impression of a composite surface.
> *   **Bottom Row:** Shows the disordered phoneme mosaic. This pattern consists of randomly scattered white dots, similar to the bottom row of panel (a), resulting in a uniform appearance of noise.
>
> The panels are labeled (a) and (b) in the bottom right corner of their respective columns. The figure visually contrasts how structured input (top row) is rendered into structured (middle row) versus disordered (bottom row) phoneme mosaics, illustrating the transition from recognizable patterns to noise.

<center>Fig. 3. Two examples of the effect of stochastic rendering, (a) a supra-Nyquist sinusoidal grating, and (b) a Brodatz [13] texture. In both cases, the top panel shows the original image, the middle panel shows the image rendered on an ordered phoneme mosaic and the bottom panel shows the image rendered on a uniformly disordered phoneme mosaic. Note that the ordered representations (middle panels) manifest spurious structure, whereas the disordered representations appear like noise (correlations between phoneme pairs are cancelled). </center>

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
