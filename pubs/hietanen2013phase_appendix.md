# PHASE SENSITIVITY OF COMPLEX CELLS IN PRIMARY VISUAL CORTEX - Appendix

---

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

*Transcribed with OCR; text and equations may contain mistakes.*
