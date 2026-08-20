# TECHNICAL REPORT - Appendix

---

## Appendix

## Mapping the Dynamic Phase Response Curve data to the Phase-Phase Plot

Given the following measurements of timing in the input and output cycles;

\(CL[n] =\) cycle length of cycle number \(n\) \(CL[n + 1] =\) cycle length of the next cycle. \(ASI[n] =\) time from start of cycle n to inhibitory stimulus. \(SIA[n] =\) time from inhibitory stimulus to end of cycle n. \(T =\) period of stimulation.

From these definitions the following sums hold

\[CL[n] = ASI[n] + SIA[n]\] \[T = SIA[n] + ASI[n + 1]\]

Therefore

\[ASI[n + 1] = T - SIA[n] = T - CL[n] + ASI[n]\]

The dynamic phase response curve gives the result for cycle length as a function of stimulus timing

\[CL[n] = CL(ASI[n])\]

and thus, the succeeding stimulus delay is a function of the preceding stimulus delay

\[ASI[n + 1] = T - CL(ASI[n]) + ASI[n]\]

where \(ASI[n]\) is the stimulus delay in the \(\mathbf{n}^{\mathrm{th}}\) cycle, and \(\mathrm{CL}(\) is the cycle length, a function of the stimulus delay. Equation (4) gives the mapping from the phase response plane to the phase- phase plane.

## Stability of a point of 1:1 entrainment

A point of 1:1 entrainment may only be found on the PPP where a curve crosses the diagonal. For each point at which this occurs, there is the potential for entrainment, but only certain points will be stable. Whether the entrainment is stable will depend on the slope of the PPP as it passes through the diagonal.

Consider a section of PPP small enough to approximate a straight line as it passes through the diagonal, with intercept of the y- axis at \(c\) and slope \(b\)

\[a[n + 1] = b a[n] + c\]

where \(\mathbf{a[n]}\) is the stimulus delay for the \(n^{th}\) output cycle. The point of 1:1 entrainment will occur at

\[a[n + 1] = a[n]\]

Solving by substitution gives this point

\[a[n] = \frac{c}{1 - b} = a_{1:1}\]

Now consider a stimulus falling just beyond this point, with small offset d.

\[a[n] = a_{1:1} + d\] \[a[n + 1] = b a[n] + c\] \[a[n + 1] = \frac{bc}{1 - b} +bd + c = \frac{c}{1 - b} +bd = a_{1:1} + bd\]

For stability, \(a[n + 1]\) must be closer to a 1:1 than \(a[n]\) . Clearly, this will be the case if the magnitude of b is less than 1. Therefore, the requirement for stability of the PRC is that the 1:1 entrainment point is stable only if \(\left|b\right|< 1\) Consider the reverse mapping to the dynamic PRC plane, in the region near a 1:1 entrainment point.

\[CL(ASI[n]) = T - ASI[n + 1] + ASI[n]\] \[= T + (1 - b)ASI[n] + c\]

The constants are \(T\) and \(c\) so the slope of the PRC is \((l - b)\) . By substitution of the stability criterion from above for \(b\) , a 1:1 entrainment point is stable only if the slope of the PRC is positive, but not greater than 2.

## References

1. Jalife, J. and Michaels, D.C. Neural control of sinoatrial pacemaker activity. In: Vagal control of the heart: experimental basis and clinical implications, edited by Levy, M.N. and Schwartz, P.J., Armonk, New York: Futura Publishing Company, Inc., 173-206, 1994.  
2. Levy, M.N., Iano, T. and Zieske, H., Effects of repetitive bursts of vagal activity on heart rate, Circ Res. Vol:30, No:2, 186-95, 1972.  
3. Brown, G.L. and Eccles, J.C., The action of a single vagal volley on the rhythm of the heart beat, J Physiol (Lond). Vol:82, 211-40, 1934.  
4. Brown, G.L. and Eccles, J.C., Further experiments on vagal inhibition of the heart beat, J Physiol (Lond). Vol:82, 242-57, 1934.  
5. Levy, M.N., Martin, P.J., Lano, T. and Zieske, H., Paradoxical effect of vagus nerve stimulation on heart rate in dogs, Circ Res. Vol:25, No:3, 303-14, 1969.  
6. Jalife, J., Fraccola, P. and Moe, G.K. Entrainment of the SA nodal pacemaker by brief vagal bursts in relation to AV conduction. In: Cardiac rate and rhythm, edited by Bouman, L.N. and Jongsma, H.J.: Martinus Nijhoff Publishers, 577-603, 1982.  
7. Yang, T. and Levy, M.N., The phase-dependency of the cardiac chronotropic responses to vagal stimulation as a factor in sympathetic-vagal interactions, Circ Res. Vol:54, No:6, 703-10, 1984.  
8. Yang, T.E., Cheng, J. and Levy, M.N., Effects of the spatial dispersion of acetylcholine release on the chronotropic responses to vagal stimulation in dogs, Circ Res. Vol:67, No:4,844- 51,1990.  
9. Hariman, R.J. and Hoffman, B.F., Effects of ouabain and vagal stimulation on sinus nodal function in conscious dogs, Circ Res. Vol:51, No:6,760- 8,1982.  
10. Moore, E.N., Spear, J.F. and Kronhaus, K.D. The effects of brief vagal and sympathetic stimulation on rate and rhythm changes in the sinus node. In: Cardiac rate and rhythm, edited by Bouman, L.N. and Jongsma, H.J.: Martinus Nijhoff Publishers, 543- 61, 1982.  
11. Jailife, J., Slenter, V.A., Salata, J.J. and Michaels, D.C., Dynamic vagal control of pacemaker activity in the mammalian sinoatrial node, Circ Res. Vol:52, No:6, 642- 56, 1983.  
12. Shumaker, J.M., Clark, J.W. and Giles, W.R., A model of the phase- sensitivity of the pacemaking cell in the bullfrog heart, J Theor Biol. Vol:151, No:2, 193- 230, 1991.  
13. Dexter, F., Levy, M.N. and Rudy, Y., Mathematical model of the changes in heart rate elicited by vagal stimulation, Circ Res. Vol:65, No:5, 1330- 9, 1989.  
14. Dexter, F., Saidel, G.M., Levy, M.N. and Rudy, Y., Mathematical model of dependence of heart rate on tissue concentration of acetylcholine, Am J Physiol. Vol:256, No:2 Pt 2, H520- 6, 1989.  
15. Michaels, D.C., Slenter, V.A., Salata, J.J. and Jailife, J., A model of dynamic vagus- sinoatrial node interactions, Am J Physiol. Vol:245, No:6, H1043- 53, 1983.  
16. Michaels, D.C., Matyas, E.P. and Jailife, J., A mathematical model of the effects of acetylcholine pulses on sinoatrial pacemaker activity, Circ Res. Vol:55, No:1, 89- 101, 1984.  
17. Murphey, C.R. and Clark, J.W. Parasympathetic control of the SA node cell in rabbit heart - a model. In: Activation, metabolism and perfusion of the heart, edited by Sideman, S. and Beyar, R.: Martinus Nijhoff Publishers, 44- 60, 1987.  
18. Noble, D. and Noble, S.J., A model of sino- atrial node electrical activity based on a modification of the DiFrancesco- Noble (1984) equations, Proc R Soc Lond B Biol Sci. Vol:222, No:1228, 295- 304, 1984.  
19. Dokos, S., Celler, B.G. and Lovell, N.H., Vagal control of sinoatrial rhythm: a mathematical model, J Theor Biol. Vol:182, No:1, 21- 44, 1996.  
20. Demir, S.S., Clark, J.W. and Giles, W.R., Parasympathetic modulation of sinoatrial node pacemaker activity in rabbit heart: a unifying model, Am J Physiol. Vol:276, No:6 Pt 2, H2221- 44, 1999.  
21. Dokos, S., Lovell, N.H. and Celler, B.G., Review of ionic models of vagal- cardiac pacemaker control, J Theor Biol. Vol:192, No:3, 265- 74, 1998.  
22. Ikeda, N., Tsuruta, H. and Sato, T., Difference equation model of the entrainment of myocardial pacemaker cells based on the phase response curve, Biol Cybern. Vol:42, No:2, 117- 28, 1981.  
23. Glass, L. and Mackey, M. From clocks to chaos: the rhythms of life, Princeton, New Jersey: Princeton University Press, 1988.  
24. Winfree, A.T. When time breaks down: the three- dimensional dynamics of electrochemical waves and cardiac arrhythmias. Princeton, New Jersey: Princeton University Press, 1987.  
25. Perkel, D.H., Schulman, J.H., Bullock, T.H., Moore, G.P. and Segundo, J.P., Pacemaker neurons: effects of regularly spaced synaptic input, Science. Vol:145, 61, 1964.  
26. Hodgkin, A.L. and Huxley, A.F., A quantitative description of membrane current and its application to conduction and excitation in nerve, J Physiol (Lond). Vol:117, 500- 44, 1952.  
27. Dokos, S., Celler, B. and Lovell, N., Ion currents underlying sinoatrial node pacemaker activity: a new single cell mathematical model, J Theor Biol. Vol:181, No:3, 245- 72, 1996.  
28. Henning, R.J., Masuda, Y., Yang, T.N. and Levy, M.N., Rate of acetylcholine hydrolysis affects the phase dependency of cardiac responses to vagal stimulation, Cardiovasc Res. Vol:21, No:3, 169- 76, 1987.  
29. Loffelholz, K. and Pappano, A.J., The parasympathetic neuroeffector junction of the heart, Pharmacol. Rev. Vol:37, 1- 24, 1985.  
30. Celler, B.G., Characteristics of cardiac period responses to prolonged vagal stimulation in dogs, Med Biol Eng Comput. Vol:27, 595- 602, 1989.  
31. Celler, B.G. and Lovell, N.H., Dynamics of cardiac period responses after prolonged vagal stimulation in the dog, Ann Biomed Eng. Vol:19, No:3, 273- 89, 1991.

---

*Transcribed with OCR; text and equations may contain mistakes.*
