# Inhomogeneity of Action Potential Waveshape Assists Frequency Entrainment of Cardiac Pacemaker Cells - Appendix

---

## APPENDIX MODEL PARAMETERS AND INITIAL CONDITIONS

The model used in this study is based on that previously published by Dokos et al. [7], with two modifications described below. Table III lists the model parameters which we have mod

ified to reproduce the observed regional variation in action- potential characteristics. Table IV lists the stable initial values for the state variables of both the central and peripheral cell models.

### A. \(L\) - and \(T\) -Type Calcium Currents

The new formulations for these currents are

\[\begin{array}{r}i_{\mathrm{Ca,L}} = g_{\mathrm{Ca,L}}dLf_{\mathrm{L}}f_{\mathrm{2,L}}(E - E_{\mathrm{Ca,rev}}) \\ i_{\mathrm{Ca,T}} = g_{\mathrm{Ca,T}}d_{\mathrm{T}}f_{\mathrm{T}}(E - E_{\mathrm{Ca,rev}}). \end{array} \quad (4)\]

where \(E_{\mathrm{Ca,rev}}\) is a constant (see Table III). For details regarding the other parameters, refer to Dokos et al. [7].

### B. Delayed Rectifying Potassium Current

The delayed rectifying potassium current \(i_{\mathrm{k}}\) was replaced by a rapid and slow component, \(i_{\mathrm{K,r}}\) and \(i_{\mathrm{K,s}}\) respectively. A modified version of the equations of Courtemanche et al. [19] were used as a starting point and the parameters were then adjusted to produce the central- peripheral variation in action- potential characteristics. The resulting formulations exhibit a reasonable

TABLE IV STABLE INITIAL CONDITIONS

| Description | Symbol | Units | Central | Peripheral |
| :--- | :--- | :--- | :--- | :--- |
| Membrane potential | $E_m$ | mV | $-6.176931\text{e} + 01$ | $-6.928550\text{e} + 01$ |
| Intracellular Ca$^{2+}$ conc. | $[Ca]_{im}$ | mM | $6.512300\text{e} - 05$ | $2.373596\text{e} - 05$ |
| SR Ca$^{2+}$ Uptake conc. | $[Ca]_{up}$ | mM | $7.023436\text{e} - 01$ | $7.093992\text{e} - 01$ |
| SR Ca$^{2+}$ Release conc. | $[Ca]_{relm}$ | mM | $2.266218\text{e} - 01$ | $1.425973\text{e} - 01$ |
| Extracellular Ca$^{2+}$ conc. | $[Ca]_{om}$ | mM | $1.999668\text{e} + 00$ | $2.000538\text{e} + 00$ |
| Intracellular Na$^+$ conc. | $[Na]_{im}$ | mM | $7.487890\text{e} + 00$ | $7.214087\text{e} + 00$ |
| Extracellular Na$^+$ conc. | $[Na]_{om}$ | mM | $1.400150\text{e} + 02$ | $1.400090\text{e} + 02$ |
| Intracellular K$^+$ conc. | $[K]_{im}$ | mM | $1.401183\text{e} + 02$ | $1.403920\text{e} + 02$ |
| Extracellular K$^+$ conc. | $[K]_{om}$ | mM | $5.397060\text{e} + 00$ | $1.400090\text{e} + 02$ |
| $i_{c\alpha,L}$ activation variable | $d_L$ | | $3.134970\text{e} - 03$ | $9.848848\text{e} - 05$ |
| $i_{c\alpha,L}$ inactivation variable | $f_L$ | | $1.524224\text{e} - 01$ | $4.915431\text{e} - 02$ |
| $i_{c\alpha,L}$ inactivation variable | $f_{2L}$ | | $6.365893\text{e} - 02$ | $7.984697\text{e} - 01$ |
| $i_{c\alpha,T}$ activation variable | $d_T$ | | $1.736530\text{e} - 03$ | $5.101402\text{e} - 04$ |
| $i_{c\alpha,T}$ inactivation variable | $f_T$ | | $1.059040\text{e} - 01$ | $1.957187\text{e} - 01$ |
| $i_{K,r}$ activation variable | $x_r$ | | $1.163904\text{e} - 01$ | $1.274298\text{e} - 01$ |
| $i_{K,s}$ activation variable | $x_s$ | | $5.744252\text{e} - 02$ | $2.816889\text{e} - 01$ |
| $i_{N,a}$ activation variable | $m$ | | $2.671965\text{e} - 02$ | $5.477534\text{e} - 03$ |
| $i_{N,a}$ inactivation variable | $h$ | | $5.806926\text{e} - 03$ | $1.655310\text{e} - 02$ |
| $i_F$ activation variable | $y$ | | $2.481893\text{e} - 02$ | $2.148954\text{e} - 02$ |

correlation with published kinetics in rabbit sinoatrial node [20], [21].

1) Rapid Component:

\[\begin{array}{rl} & {\dot{i}_{\mathrm{K},r} = i_{\mathrm{K},r},n_{\mathrm{a}} + i_{\mathrm{K},r},n_{\mathrm{K}}}\\ & {\dot{i}_{\mathrm{K},r},n_{\mathrm{a}} = g_{\mathrm{K},r}x_{r}P_{\mathrm{KNa},r} = \frac{E - E_{\mathrm{Na}}}{1.0 + \exp\left(\frac{E - E_{\mathrm{K},r},\mathrm{half}}{E_{\mathrm{K},r},\mathrm{skope}}\right)}}\\ & {\dot{i}_{\mathrm{K},r},n_{\mathrm{K}} = g_{\mathrm{K},r}x_{r}\frac{E - E_{\mathrm{K}}}{1.0 + \exp\left(\frac{E - E_{\mathrm{K},r},\mathrm{half}}{E_{\mathrm{K},r},\mathrm{skope}}\right)}}\\ & {\frac{dx_{r}}{dt} = \alpha_{x_{r}}(1.0 - x_{r}) - \beta_{x_{r}}x_{r}}\\ & {\alpha_{x_{r}}r = a_{1,r}\frac{E + a_{2,r}}{1.0 - \exp\left(-\frac{E + a_{2,r}}{a_{3,r}}\right)}}\\ & {\beta_{x_{r}}r = b_{1,r}\frac{E + b_{2,r}}{\exp\left(\frac{E + b_{2,r}}{b_{3,r}}\right)} -1.0} \end{array} \quad (6)\]

2) Slow Component:

\[\begin{array}{rl} & {\dot{i}_{\mathrm{K},s} = i_{\mathrm{K},s},n_{\mathrm{a}} + i_{\mathrm{K},s},n_{\mathrm{K}}}\\ & {\dot{i}_{\mathrm{K},s},n_{\mathrm{a}} = g_{\mathrm{K},s}x_{s}^{2}P_{\mathrm{KNa},s}(E - E_{\mathrm{Na}})}\\ & {\dot{i}_{\mathrm{K},s},n_{\mathrm{K}} = g_{\mathrm{K},s}x_{s}^{2}(E - E_{\mathrm{K}})\\ & {\frac{dx_{s}}{dt} = \alpha_{x_{s}}(1.0 - x_{s}) - \beta_{x_{s}}x_{s}}\\ & {\alpha_{x_{s}}s = a_{1,s}\frac{E + a_{2,s}}{1.0 - \exp\left(-\frac{E + a_{2,s}}{a_{3,s}}\right)}}\\ & {\beta_{x_{s}}s = b_{1,s}\frac{E + b_{2,s}}{\exp\left(\frac{E + b_{2,s}}{b_{3,s}}\right)} -1.0} \end{array} \quad (14)\]

## REFERENCES

[1] W. K. Bleeker, A. J. C. Mackaay, M. Masson- Pevet, L. N. Bouman, and A. E. Becker, "Functional and morphological organization of the rabbit sinus node," Circ. Res., vol. 46, pp. 11- 22, 1980.  
[2] H. Honjo, M. R. Boyett, I. Kodama, and J. Toyama, "Correlation between electrical activity and the size of rabbit sinoatrial node cells," J. Physiol. (Lond.), vol. 496, pp. 795- 808, 1996.  
[3] I. Kodama and M. R. Boyett, "Regional differences in the electrical activity of the rabbit sinus node," Pflugers Arch., vol. 404, pp. 214- 226, 1985.  
[4] C. J. H. J. Kirchhof, F. I. M. Bonke, M. A. Allessie, and W. J. E. P. Lammers, "The influence of the atrial myocardium on impulse formation in the rabbit sinus node," Pflugers Arch., vol. 410, pp. 198- 203, 1987.  
[5] D. C. Michaels, E. P. Matyas, and J. Jalife, "Dynamic interactions and mutual synchronization of sinoatrial node pacemaker cells," Circ. Res., vol. 58, pp. 706- 720, 1986.  
[6] D. Cai, R. L. Winslow, and D. Noble, "Effects of gap junction conductance on dynamics of sinoatrial node cells: Two- cell and large- scale network models," IEEE Trans. Biomed. Eng., vol. 41, pp. 217- 231, Mar. 1994.  
[7] S. Dokos, B. Celler, and N. Lovell, "Ion currents underlying sinoatrial node pacemaker activity: A new single cell mathematical model," J. Theor. Biol., vol. 181, pp. 245- 272, 1996.  
[8] I. Kodama, M. R. Boyett, M. R. Niknamar, M. Yamamoto, H. Honjo, and N. Niwa, "Regional differences in the effects of E- 4031 within the sinoatrial node," Amer. J. Physiol., vol. 276, pp. H793- H802, 1999.  
[9] H. Zhang, A. V. Holden, I. Kodama, H. Honjo, M. Lei, T. Varghese, and M. R. Boyett, "Mathematical models of action potentials in the periphery and center of the rabbit sinoatrial node," Amer. J. Physiol., vol. 279, pp. H397- H421, 2000.  
[10] D. J. Aidley, The Physiology of Excitable Cells, 2nd ed. Cambridge, U.K.: Cambridge Univ. Press, 1978.  
[11] S. R. Coppen, I. Kodama, M. Boyett, H. Dobrzynski, Y. Takagishi, H. Honjo, H. Yeh, and N. J. Severs, "Connexin45, a major connexin of the rabbit sinoatrial node, is coexpresses with connexin43 in a restricted zone at the nodal- crist terminals border," J. Histochem. Cytochem., pp. 907- 918, 1999.  
[12] A. P. Moreno, J. G. Laing, E. C. Beyer, and D. C. Spray, "Properties of gap junction channels formed of connexin 45 endogenously expressed in human heptoma (skhep1) cells," Amer. J. Physiol., pp. C356- C365, 1995.  
[13] R. D. Veenstra, H. Z. Wang, E. M. Westphal, and E. C. Beyer, "Multiple connexin confer distinct regulatory and conductance properties of gap junctions in developing heart," Circ. Res., pp. 1277- 1283, 1992.  
[14] J. M. B. Anumonwo, H. Z. Wang, E. Trabka- Janik, B. Dunham, R. D. Veenstra, M. Delmar, and J. Jalife, "Gap junction channels in adult mammalian sinus node cells," Circ. Res., vol. 71, pp. 229- 239, 1992.  
[15] D. E. Clapham, A. Shrier, and R. L. DeHaan, "Junctional resistance and action potential delay between embryonic heart cell aggregates," J. Gen. Physiol., pp. 633- 654, 1980.  
[16] R. W. Joyner and F. J. L. V. Capelle, "Propagation through electrically coupled cells: How a small sa node drives a large atrium," Biophys. J., vol. 50, pp. 1157- 1164, 1986.  
[17] R. Wilders, E. E. Verheijck, R. Kumar, W. N. Goolsby, A. C. G. Van Ginnenken, R. W. Joyner, and H. J. Jongsma, "Model clamp and its application to synchronization of rabbit sinoatrial node cells," Amer. J. Physiol., pp. H2168- H2182, 1996.  
[18] E. E. Verheijck, R. Wilders, R. W. Joyner, D. A. Golod, R. Kumar, H. J. Jongsma, L. N. Bouman, and A. C. G. vanGinnenken, "Pacemaker synchronization of electrically coupled rabbit sinoatrial node cells," J. Gen. Physiol., vol. 111, pp. 95- 112, 1998.  
[19] M. Courtemanche, R. J. Ramirez, and S. Nattel, "Ionic mechanisms underlying human atrial action potential properties: Insights from a mathematical model," Amer. J. Physiol., vol. 275, pp. H301- H321, 1998.  
[20] T. Shibasaki, "Conductance and kinetics of delayed rectifier potassium channels in nodal cells of the rabbit heart," J. Physiol. Lond., vol. 387, pp. 227- 250, 1987.  
[21] K. Ono and H. Ito, "Role of rapidly activating delayed rectifier \(k^{+}\) current in sinoatrial node pacemaker activity," Amer. J. Physiol., pp. H453- H462, 1995.  
[22] T. Opthof, B. De Jong, H. J. Jongsma, and L. N. Bouman, "Function morphology of the mammalian sinoatrial node," Eur. Heart J., pp. 1249- 1259, 1987.  
[23] H. Irisawa, H. F. Brown, and W. Giles, "Cardiac pacemaking in the sinoatrial node," Physiol. Rev., vol. 73, pp. 197- 227, 1993.

> **Image description.** A portrait photograph of a middle-aged man, likely a professional or academic, set against a plain, light background.
>
> The man has short, dark hair and a fair complexion. He is facing forward, looking directly at the viewer with a neutral expression. He is dressed in formal business attire, consisting of a dark suit jacket (appearing black or dark grey) worn over a light-colored collared shirt.
>
> Below the photograph, there is visible text that serves as a caption or title. The visible text reads: "Head of the School of Elec". The final word, "Elec," is truncated, suggesting the full title is "Head of the School of Electrical Engineering" or a similar department. The overall composition suggests this image is used to identify a person in an academic or institutional context.

Branko G. Celler (M'88) received the B.Sc. degree in computer science and physics, the B.E. (Hons) degree in electrical engineering, and the Ph.D. degree in biomedical engineering in 1969, 1972, and 1978, respectively, all from the University of New South Wales, Australia.

From 1977 to 1980 he was a Postdoctoral Fellow working at the John Hopkins School of Medicine, Baltimore, MD. He returned to UNSW in 1981 as a Lecturer, where he was appointed Associate Professor in 1991 and Professor in January 1997. He is

Head of the School of Electrical Engineering and Telecommunications, Director of the Biomedical Systems Laboratory, and Co- Director of the Centre for Health Informatics at UNSW. His research interests include biomedical instrumentation, signal processing and medical expert systems. Over the last 8- 10 years he has been actively involved in R&D on the application of information and communications technology in primary health care and he has a particular interest in home telecare and the remote monitoring of health status of the elderly at home.

Dr. Celler also serves on the editorial boards of the IEEE Transactions on Information Technology in Biomedicine and the International Journal of Telemedicine and Telecare.

> **Image description.** A portrait photograph of a man, likely a professional or academic figure, set against a plain, light background.
>
> The subject is a middle-aged man with dark, neatly styled hair. He is wearing rectangular-framed glasses and is dressed in a dark jacket or suit. He is positioned facing the camera directly, presenting a neutral and composed expression.
>
> The photograph is cropped to focus on the man from the chest up. The background is uniformly light, appearing white or very light gray, which isolates the subject and draws focus to his face.
>
> Fragmented text is visible immediately above the image, reading "...myocardium. He is curre," suggesting the image is embedded within a biographical or scientific text. The surrounding context indicates that this portrait is associated with the biography of Branko G. Celler.

Socrates Dokos (M'94) received the B.E. (Hons) degree in electrical engineering and the Ph.D. degree in biomedical engineering in 1987 and 1996, respectively, from the University of New South Wales (UNSW), Sydney, Australia. His thesis was in the area of mathematical modeling of cardiac pacemaker activity and its vagal control.

Until recently, he held a postdoctoral position in the Department of Physiology at Auckland University School of Medicine, New Zealand, where he investigated mechanical properties of mammalian

> **Image description.** A head-and-shoulders portrait photograph of a middle-aged man set against a plain white background.
>
> The subject is a man with a light skin tone, positioned centrally in the frame. He has very short, dark hair that appears to be receding slightly at the temples. His facial features are clear, and he has a neutral to slightly pleasant expression, with a subtle hint of a smile. He is wearing a dark, solid-colored collared shirt, which appears to be black or a very dark gray.
>
> The photograph is a close-up, focusing primarily on the man's head and shoulders. The background is uniformly white, providing high contrast and drawing full attention to the subject.
>
> On the right side of the image, there are fragmented pieces of black text visible, which appear to be part of the surrounding document content, including the letters "si," "i," "a," and "B."

Shaun L. Cloherty received the BE (Hons) degree in aerospace avionics from the Queensland University of Technology, Brisbane, Australia. He is currently working towards the Ph.D. degree in the Graduate School of Biomedical Engineering at the University of New South Wales, Sydney, Australia. His thesis lies in the area of cardiac electrophysiology and modeling of the mammalian sinoatrial node.

His research interests include biological signal processing, cardiac electrophysiology, and modeling.

myocardium. He is currently a Research Associate in the Graduate School of Biomedical Engineering, UNSW, where he is working on large scale parameter optimization techniques for the reconstruction of cardiac action potentials. He is interested in developing biophysically accurate models of the electrical and mechanical properties of myocardium.

> **Image description.** A portrait photograph of a middle-aged man, likely an academic or professional, set against a dark, indistinct background.
>
> The subject is positioned facing forward, captured from the chest up. He has short, dark hair and is wearing a light-colored collared shirt. He has a pleasant, slight smile and appears to be looking directly at the viewer. The lighting is focused on the subject, creating a high-contrast effect where the dark background recedes, emphasizing the man's features.
>
> Below the portrait, there is visible text and a stylized logo. The text reads:
> "Medicine and Biology Soc"
>
> Immediately following this text is a small, stylized graphic consisting of a letter 'A' followed by a hash symbol: "A#".

Nigel H. Lovell (M'90- SM'99) received the B.E. (Hons) and Ph.D. degrees from the University of New South Wales (UNSW), Sydney, Australia.

He is currently a Faculty member of the Graduate School of Biomedical Engineering and Deputy Director of the Centre for Health Informatics at UNSW. His research work has covered areas of expertise ranging from cardiac modeling, web- enabling technologies, biological signal processing, cardiac neurophysiology, and visual prosthesis design.

Medicine and Biology Society (EMBS) web- master and chairs the committee on Information Technology Infrastructure. He is a serving member on the Administrative Committee of the EMB Society (2000- 2002). Recently, he was awarded the IEEE Millennium Medal for services to the EMBS in relation to its Web- based infrastructure.

Dr. Lovell's is currently the IEEE Engineering in Medicine and Biology Society (EMBS) web- master and chairs the committee on Information Technology Infrastructure. He is a serving member on the Administrative Committee of the EMB Society (2000- 2002). Recently, he was awarded the IEEE Millennium Medal for services to the EMBS in relation to its Web- based infrastructure.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
