# A gradient model of cardiac pacemaker myocytes - Appendix

---

## Appendix A

The equations of the generic Markov- state sinoatrial node cell ionic model appear below. Table 2 lists the components of the central and peripheral state vectors ( \(P_{\mathrm{C}}\) and \(P_{\mathrm{P}}\) ) together with the corresponding components of the interpolation parameter vector ( \(X\) ). Table 3 lists stable initial conditions for the central and peripheral sinoatrial node cell models.

1. \(L\) -Type calcium current

\[i_{\mathrm{Ca,L}} = g_{\mathrm{Ca,L}}A_{\mathrm{Ca,L}}(E_{\mathrm{m}} - E_{\mathrm{Ca,rev}}),\]

2. \(T\) -Type calcium current

\[i_{\mathrm{Ca,T}} = g_{\mathrm{Ca,T}}A_{\mathrm{Ca,T}}(E_{\mathrm{m}} - E_{\mathrm{Ca,rev}}).\]

3. Delayed rectifier potassium current

\[i_{\mathrm{K}} = i_{\mathrm{K},\tau} + i_{\mathrm{K},\mathrm{s}},\] \[i_{\mathrm{K},\tau} = i_{\mathrm{K},\mathrm{r}_{\mathrm{Na}} + i_{\mathrm{K},\mathrm{r}_{\mathrm{K}}}},\] \[i_{\mathrm{K},\mathrm{r}_{\mathrm{Na}}} = g_{\mathrm{K},\tau}A_{\mathrm{K},\tau}P_{\mathrm{KNa},\tau}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{K},\mathrm{r}_{\mathrm{K}}} = g_{\mathrm{K},\tau}A_{\mathrm{K},\tau}(E_{\mathrm{m}} - E_{\mathrm{K}}),\] \[i_{\mathrm{K},\mathrm{s}} = i_{\mathrm{K},\mathrm{s}_{\mathrm{Na}}} + i_{\mathrm{K},\mathrm{s}_{\mathrm{K}}},\] \[i_{\mathrm{K},\mathrm{s}_{\mathrm{Na}}} = g_{\mathrm{K},\mathrm{s}}A_{\mathrm{K},\mathrm{s}}P_{\mathrm{KNa},\mathrm{s}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{K},\mathrm{s}_{\mathrm{K}}} = g_{\mathrm{K},\mathrm{s}}A_{\mathrm{K},\mathrm{s}}(E_{\mathrm{m}} - E_{\mathrm{K}}).\]

4. \(TTX\) sensitive sodium current

\[i_{\mathrm{Na}} = g_{\mathrm{Na}}A_{\mathrm{Na}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\]

Table 3 List of initial conditions for all state variables in the generic SAN model, for both central and peripheral versions

| Variable | Central SAN cell | Peripheral SAN cell |
| :--- | :--- | :--- |
| $E_m$ | $-6.39512\mathrm{e}+1$ | $-7.663138\mathrm{e}+1$ |
| $[Ca]_i$ | $1.275323\mathrm{e}-4$ | $6.623230\mathrm{e}-5$ |
| $[Ca]_{up}$ | $1.035010$ | $7.506109\mathrm{e}-1$ |
| $[Ca]_{ef}$ | $2.447983\mathrm{e}-1$ | $1.365436\mathrm{e}-1$ |
| $[Ca]_s$ | $1.999744$ | $2.000020$ |
| $[Na]_i$ | $8.003895$ | $1.359578\mathrm{e}+1$ |
| $[Na]_s$ | $1.400235\mathrm{e}+2$ | $1.399803\mathrm{e}+2$ |
| $[K]_i$ | $1.498639\mathrm{e}+2$ | $2.121477\mathrm{e}+2$ |
| $[K]_s$ | $5.389262$ | $5.442564$ |
| $[Cl]_i$ | $2.606581\mathrm{e}+1$ | $2.489672\mathrm{e}+1$ |
| $[Cl]_s$ | $1.400001\mathrm{e}+2$ | $1.399971\mathrm{e}+2$ |
| $A_{Ca,L}$ | $4.563555\mathrm{e}-4$ | $6.736841\mathrm{e}-4$ |
| $I_{1-Ca,L}$ | $9.601208\mathrm{e}-1$ | $9.764172\mathrm{e}-1$ |
| $I_{2-Ca,L}$ | $5.260367\mathrm{e}-3$ | $3.012387\mathrm{e}-3$ |
| $A_{Ca,T}$ | $1.561896\mathrm{e}-5$ | $2.070065\mathrm{e}-10$ |
| $I_{1-Ca,T}$ | $9.985167\mathrm{e}-1$ | $9.961892\mathrm{e}-1$ |
| $A_{K,r}$ | $1.209480\mathrm{e}-1$ | $9.958786\mathrm{e}-2$ |
| $I_{1-K,r}$ | $1.991481\mathrm{e}-3$ | $1.243415\mathrm{e}-1$ |
| $I_{2-K,r}$ | $5.616591\mathrm{e}-2$ | $2.453342\mathrm{e}-4$ |
| $A_{K,s}$ | $5.048523\mathrm{e}-3$ | $1.733389\mathrm{e}-3$ |
| $I_{1-K,s}$ | $9.920536\mathrm{e}-1$ | $9.945393\mathrm{e}-1$ |
| $A_{Na}$ | $5.586372\mathrm{e}-4$ | $6.111398\mathrm{e}-8$ |
| $I_{1-Na}$ | $3.749674\mathrm{e}-1$ | $4.104663\mathrm{e}-1$ |
| $I_{2-Na}$ | $1.038603\mathrm{e}-1$ | $1.134436\mathrm{e}-1$ |
| $A_f$ | $3.715769\mathrm{e}-4$ | $8.742796\mathrm{e}-5$ |
| $I_{1-f}$ | $9.972171\mathrm{e}-1$ | $9.988556\mathrm{e}-1$ |
| $A_{to}$ | $1.219969\mathrm{e}-2$ | $1.479078\mathrm{e}-2$ |
| $I_{1-to}$ | $6.310187\mathrm{e}-1$ | $7.741232\mathrm{e}-1$ |
| $I_{2-to}$ | $2.696949\mathrm{e}-2$ | $2.586954\mathrm{e}-2$ |

# 5. Sodium-calcium exchange current

\[I_{\mathrm {NaCa}}=K_{\mathrm {NaCa}}\frac {x_{2}k_{21}-x_{1}k_{12}}{x_{1}+x_{2}+x_{3}+x_{4}},\]

\[x_{1}=(k_{23}+k_{21})k_{41}k_{34}+(k_{43}+k_{41})k_{21}k_{32},\]

\[x_{2}=(k_{14}+k_{12})k_{32}k_{43}+(k_{34}+k_{32})k_{12}k_{41},\]

\[x_{3}=(k_{23}+k_{21})k_{14}k_{43}+(k_{43}+k_{41})k_{12}k_{23},\]

\[x_{4}=(k_{14}+k_{12})k_{23}k_{34}+(k_{34}+k_{32})k_{14}k_{21},\]

\[D_{1}=1.0+\frac {[\mathrm {Ca}]_{\mathrm {i}}}{K_{\mathrm {C,i}}}\left(1.0+\exp \left(-\frac {E_{\mathrm {m}}Q_{\mathrm {C,i}}F}{RT}\right)\right)\frac {[\mathrm {Ca}][\mathrm {Na}]}{K_{\mathrm {C,i}}K_{\mathrm {C,Ni}}}+\frac {[\mathrm {Na}]}{K_{\mathrm {1,Ni}}}\left(1.0+\frac {[\mathrm {Na}]}{K_{\mathrm {2,Ni}}}\right)\right),\]

\[k_{43} = \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{Ni}}[\mathrm{Na}]_{i}},\] \[k_{12} = \frac{[\mathrm{Ca}]_{i}\mathrm{exp}\left(-\frac{E_{\mathrm{m}}Q_{\mathrm{C},i}F}{RT}\right)}{K_{\mathrm{C},i}D_{1}},\] \[k_{14} = \frac{[\mathrm{Na}]_{i}^{2}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{Ni}}}\right)\mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right)}{K_{1,\mathrm{Ni}}K_{2,\mathrm{Ni}}D_{1}},\] \[k_{41} = \mathrm{exp}\left(-\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right),\] \[D_{2} = 1.0 + \frac{[\mathrm{Ca}]_{i}}{K_{\mathrm{C},0}}\left(1.0 + \mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{C},0}F}{RT}\right)\right) + \frac{[\mathrm{Na}]_{i}}{K_{1,\mathrm{No}}}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{2,\mathrm{No}}}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{No}}}\right)\right),\] \[k_{34} = \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{No}}[\mathrm{Na}]_{i}},\] \[k_{21} = \frac{[\mathrm{Ca}]_{i}\mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{C},0}F}{RT}\right)}{K_{\mathrm{C},0}D_{2}},\] \[k_{23} = \frac{[\mathrm{Na}]_{i}^{2}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{No}}}\right)\mathrm{exp}\left(-\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right)}{K_{1,\mathrm{No}}K_{2,\mathrm{No}}D_{2}},\] \[k_{32} = \mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right).\]

6. Hyperpolarisation activated inward current

\[i_{\mathrm{f}} = i_{\mathrm{f}_{\mathrm{Na}}} + i_{\mathrm{f}_{\mathrm{K}}},\] \[i_{\mathrm{f}_{\mathrm{Na}}} = A_{\mathrm{f}}\frac{[\mathrm{K}]_{\mathrm{o}}^{1.83}}{[\mathrm{K}]_{\mathrm{o}}^{1.83} + K_{\mathrm{m,f}}^{1.83}} g_{\mathrm{f},\mathrm{Na}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{f}_{\mathrm{K}}} = A_{\mathrm{f}}\frac{[\mathrm{K}]_{\mathrm{o}}^{1.83}}{[\mathrm{K}]_{\mathrm{o}}^{1.83} + K_{\mathrm{m,f}}^{1.83}} P_{\mathrm{f},\mathrm{K}}g_{\mathrm{f},\mathrm{Na}}(E_{\mathrm{m}} - E_{\mathrm{K}}).\]

7. Sodium-potassium pump current

\[i_{\mathrm{Na,K}} = I_{\mathrm{p,max}}\frac{[\mathrm{Na}]_{i}}{[\mathrm{Na}]_{i} + K_{\mathrm{m,Na}}[\mathrm{K}]_{\mathrm{o}} + K_{\mathrm{m,K}}}\left(1.0 - \left(\frac{E_{\mathrm{m}} - 40.0}{211.0}\right)^{2}\right).\]

8. 4-Aminopyridine (4-AP) sensitive outward current

\[i_{\mathrm{to}} = g_{\mathrm{to}}A_{\mathrm{to}}(E_{\mathrm{m}} - E_{\mathrm{K}}).\]

9. Background currents

\[i_{\mathrm{b,Na}} = g_{\mathrm{b,Na}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{b,K}} = K_{\mathrm{b,K}}[\mathrm{K}]_{\mathrm{o}}^{0.41}\left([\mathrm{K}]_{\mathrm{i}} - \left([\mathrm{K}]_{\mathrm{o}}\mathrm{exp}\left(-\left(\frac{E_{\mathrm{m}}F}{RT}\right)\right)\right),\] \[i_{\mathrm{b,Cl}} = g_{\mathrm{b,Cl}}(E_{\mathrm{m}} - E_{\mathrm{Cl}}).\]

10. Calcium sequestration in the sarcoplasmic reticulum

\[i_{\mathrm{Ca,up}} = I_{\mathrm{up,max}}\frac{1.0}{1.0 + \left(\frac{K_{\mathrm{m,Caup}}}{[\mathrm{Ca}]_{\mathrm{i}}}\right)^{2}},\] \[i_{\mathrm{Ca,rel}} = \frac{2.0FV_{\mathrm{rel}}}{\tau_{\mathrm{rel}}} [\mathrm{Ca}]_{\mathrm{rel}}\frac{1.0}{1.0 + \left(\frac{K_{\mathrm{m,Ca_{rel}}}}{[\mathrm{Ca}]_{\mathrm{i}}}\right)^{2}},\] \[i_{\mathrm{Ca,tr}} = \frac{2.0FV_{\mathrm{rel}}}{\tau_{\mathrm{tr}}} [\mathrm{Ca}]_{\mathrm{up}}.\]

11. Compartment ion concentrations

\[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{i}}}{\mathrm{d}t} = -\frac{i_{\mathrm{Ca,L}} + i_{\mathrm{Ca,T}} - 2.0i_{\mathrm{NaCa}} + i_{\mathrm{Ca,up}} - i_{\mathrm{Ca,rel}}}{2.0FV_{\mathrm{i}}},\] \[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{up}}}{\mathrm{d}t} = \frac{i_{\mathrm{Ca,up}} - i_{\mathrm{Ca,tr}}}{2.0FV_{\mathrm{up}}},\] \[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{rel}}}{\mathrm{d}t} = \frac{i_{\mathrm{Ca,tr}} - i_{\mathrm{Ca,rel}}}{2.0FV_{\mathrm{rel}}},\] \[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{o}}}{\mathrm{d}t} = \frac{i_{\mathrm{Ca,L}} + i_{\mathrm{Ca,T}} - 2.0i_{\mathrm{NaCa}} + [\mathrm{Ca}]_{\mathrm{b}} - [\mathrm{Ca}]_{\mathrm{o}}}{2.0FV_{\mathrm{c}}},\] \[\frac{\mathrm{d}[\mathrm{Na}]_{\mathrm{i}}}{\mathrm{d}t} = -\frac{i_{\mathrm{K,Na}} + i_{\mathrm{K,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{NaCa}} + i_{\mathrm{b,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{p}}}{FV_{\mathrm{i}}},\] \[\frac{\mathrm{d}[\mathrm{Na}]_{\mathrm{o}}}{\mathrm{d}t} = \frac{i_{\mathrm{K,Na}} + i_{\mathrm{K,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{NaCa}} + i_{\mathrm{b,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{p}}}{FV_{\mathrm{c}}} +\frac{[\mathrm{Na}]_{\mathrm{b}} - [\mathrm{Na}]_{\mathrm{o}}}{i_{\mathrm{b}}},\] \[\frac{\mathrm{d}[\mathrm{K}]_{\mathrm{i}}}{\mathrm{d}t} = -\frac{i_{\mathrm{K,ri}} + i_{\mathrm{K,ri}} + i_{\mathrm{b,K}} + i_{\mathrm{K}} - 2.0i_{\mathrm{p}} + i_{\mathrm{io}}}{FV_{\mathrm{i}}},\] \[\frac{\mathrm{d}[\mathrm{K}]_{\mathrm{o}}}{\mathrm{d}t} = \frac{i_{\mathrm{K,ri}} + i_{\mathrm{K,ri}} + i_{\mathrm{b,K}} + i_{\mathrm{K}} - 2.0i_{\mathrm{p}} + i_{\mathrm{io}}}{FV_{\mathrm{c}}} +\frac{[\mathrm{K}]_{\mathrm{b}} - [\mathrm{K}]_{\mathrm{o}}}{i_{\mathrm{b}}},\]

\[\frac{\mathrm{d}[\mathrm{Cl}]_i}{\mathrm{d}t} = \frac{i_{\mathrm{b,Cl}}}{FV_i\] \[\frac{\mathrm{d}[\mathrm{Cl}]_o}{\mathrm{d}t} = -\frac{i_{\mathrm{b,Cl}}}{FV_{\mathrm{c}}} +\frac{[\mathrm{Cl}]_{\mathrm{b}} - [\mathrm{Cl}]_o}{\Gamma_{\mathrm{b}}}.\]

## References

Bleeker, W.K., MacKaay, A.J.C., Masson- Pevet, M., Bouman, L.N., Becker, A.E., 1980. Functional and morphological organization of the rabbit sinus node. Circ. Res. 46 (1), 11- 22.  
Boyett, M.R., Honjo, H., Kodama, I., 2000. The sinoatrial node, a heterogeneous pacemaker structure. Cardiovasc. Res. 47, 658- 687.  
Cai, D., Winslow, R.L., Noble, D., 1994. Effects of gap junction conductance on dynamics of sinoatrial node cells: two- cell and large- scale network models. IEEE Trans. Biomed. Eng. 41, 217- 231.  
Cohen, S., Hindmarsh, A., 1996. CVODE, a stiff/nonstiff ODE solver in C. Comput. Phys. 10 (2), 138- 143.  
Demir, S.S., Clark, J.W., Murphey, C.R., Giles, W.R., 1994. A mathematical model of a rabbit sinoatrial node cell. Am. J. Physiol. 266, C832- C852.  
Dokos, S., Lovell, N.H., 2003. A curvilinear gradient path method for optimization of biological systems models. In: Feng, D.D., Carson, E.R. (Eds.), Proceedings of the Fifth IFAC Symposium on Modelling and Control in Biomedical Systems 2003. Elsevier, Oxford, pp. 203- 208.  
Dokos, S., Lovell, N.H., 2004. Parameter estimation in cardiac ionic models. Progr. Biophys. Mol. Biol., doi:10.1016/j.pbiomolbio.2004.02.002.  
Dokos, S., Celler, B.G., Lovell, N.H., 1996. Ion currents underlying sinoatrial node pacemaker activity: a new single cell mathematical model. J. Theoret. Biol. 181, 245- 272.  
Dokos, S., Cloherty, S.L., Lovell, N.H., Zaza, A., 2001. Cell- specific ionic models of cardiac pacemaker activity. In: Proceedings of the 23rd Annual International Conference of the IEEE Engineering in Medicine and Biology Society, IEEE Press, Istanbul, Turkey.  
Hodgkin, A.L., Huxley, A.F., 1952. A quantitative description of membrane current and its application to conduction and excitation in nerve. J. Physiol. 117, 500- 544.  
Honjo, H., Boyett, M.R., Kodama, I., Toyama, J., 1996. Correlation between electrical activity and the size of rabbit sino- atrial node cells. J. Physiol. 496 (3), 795- 808.  
Kirchhof, C.J.H.J., Bonke, F.I.M., Allessie, M.A., Lammers, W.J.E.P., 1987. The influence of the atrial myocardium on impulse formation in the rabbit sinus node. Pflüger's Arch. 410, 198- 203.  
Kodama, I., Boyett, M.R., 1985. Regional differences in the electrical activity extended to include additional experimental recordings from the rabbit sinus node. Pflüger's Arch. 404, 214- 226.  
Kodama, I., Nikmaram, M.R., Boyett, M.R., Suzuki, R., Honjo, H., Owen, J.M., 1997. Regional differences in the role of the \(\mathrm{Ca^{2 + }}\) and \(\mathrm{Na^{+}}\) currents in pacemaker activity in the sinoatrial node. Am. J. Physiol. 272, H2793- H2806.  
Kodama, I., Boyett, M.R., Nikmaram, M.R., Yamamoto, M., Honjo, H., Niwa, R., 1999. Regional differences in effects of E- 4031 within the sinoatrial node. Am. J. Physiol. 276, H793- H802.  
Kurata, Y., Hisatome, I., Imanishi, S., Shibamoto, T., 2002. Dynamical description of sinoatrial node pacemaking: improved mathematical model of primary pacemaker cell. Am. J. Physiol. 283, H2074- H2101.  
Lei, M., Honjo, H., Kodama, I., Boyett, M.R., 2001. Heterogeneous expression of the delayed- rectifier \(\mathrm{K^{+}}\) currents \(i_{\mathrm{K},r}\) and \(i_{\mathrm{K},s}\) in rabbit sinoatrial node cells. J. Physiol. 535, 703- 714.  
Liu, S., Rasmussen, R.L., 1997. Hodgkin- Huxley and partially coupled inactivation models yield different voltage dependence of block. Am. J. Physiol. 272, H2013- H2022.  
Michaels, D.C., Matyas, E.P., Jalife, J., 1986. Dynamic interactions and mutual synchronization of sinoatrial node pacemaker cells. Circ. Res. 58, 706- 720.  
Michaels, D.C., Matyas, E.P., Jalife, J., 1987. Mechanisms of pacemaker synchronization: a new hypothesis. Circ. Res. 61, 704- 714.  
Musa, H., Lei, M., Honjo, H., Jones, S.A., Dobrzynski, H., Lancaster, M.K., Takagishi, Y., Henderson, Z., Kodama, I., Boyett, M.R., 2002. Heterogeneous expression of \(\mathrm{Ca^{2 + }}\) handling proteins in rabbit sinoatrial node. J. Histochem. Cytochem. 50, 311–324.  
Noble, D., Noble, S.J., 1984. A model of sino- atrial node electrical activity based on a modification of the DiFrancesco- Noble (1984) equations. Proc. Roy. Soc. London Ser. B 222, 295–304.  
Verheijck, E.E., Wessels, A., van Ginneken, A.C.G., Bourier, J., Markman, M.W.M., Vermeulen, J.L.M., de Bakker, J.M.T., Lamers, W.H., Opthof, T., Bouman, L.N., 1998. Distribution of atrial and nodal cells within the rabbit sinoatrial node: models of sinoatrial transition. Circulation 97, 1623–1631.  
Verheule, S., van Kempen, M.J.A., Postma, S., Rook, M.B., Jongsma, H.J., 2001. Gap junctions in the rabbit sinoatrial node. Am. J. Physiol. 280, H2103–H2115.  
Wilders, R., Jongsma, H.J., van Ginneken, A.C.G., 1991. Pacemaker activity of the rabbit sinoatrial node: a comparison of mathematical models. Biophys. J. 60, 1202–1216.  
Zhang, H., Holden, A.V., Kodama, I., Honjo, H., Lei, M., Varghese, T., Boyett, M.R., 2000. Mathematical models of action potentials in the periphery and center of the rabbit sinoatrial node. Am. J. Physiol. 279, H397–H421.  
Zhang, H., Holden, A.V., Boyett, M.R., 2001. Gradient model versus mosaic model of the sinoatrial node. Circulation 103, 584–588.  
Zhang, H., Holden, A.V., Boyett, M.R., 2002. Computational approaches to the ionic basis of pacemaker activity–from channel kinetics to the regional differences in rhythm. Chaos, Solitons and Fractals 13, 1631–1642.

---

*Transcribed with OCR and VLMs; text, equations, and tables may contain mistakes.*
