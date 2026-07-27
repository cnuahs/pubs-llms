# Parameter-Optimized Model of Cardiovascular-Rotary Blood Pump Interactions - Appendix

---

## APPENDIX

## DESCRIPTION OF HEART CHAMBER EQUATIONS

The ESPVR for the left and right atria is given by

\[P_{e,s_i} = E_{e,s_i}(V_{e,s_i} - V_{d,i}) \quad (16)\]

where \(i\) represents either the left or right atrial (RA) free walls (laf or raf), \(P_{e,s,i}\) denotes end systolic pressure, \(E_{e,s,i}\) is the slope of the ESPVR, \(V_{e,s,i}\) denotes end systolic volume, and \(V_{d,i}\) denotes volume at zero pressure. The ESPVR for the left and right ventricles was given by

\[P_{e,s,i} = \frac{1}{\alpha_i + \beta_iV_{e,s,i}}\ln \frac{V_{e,s,i}}{V_{d,i}} \quad (17)\]

where \(i\) represents either the left or RV free walls (lvf or rvf), \(\alpha_i\) and \(\beta_i\) combine the myocardial stiffness, chamber geometry, and other empiric properties [9], and \(V_{d,i}\) denotes the volume at zero pressure. The end diastolic PVR (EDPVR) for all heart chambers was given by

\[P_{e,d,i} = P_{0,i}(e^{\lambda_i(V_{e,d,i} - V_{0,i})} - 1) \quad (18)\]

where \(i\) represents each of the heart chamber, \(P_{e,d,i}\) denotes the end diastolic pressure, \(P_{0,i}\) and \(\lambda_i\) characterize the stiffness of the corresponding heart chamber at end diastole, \(V_{e,d,i}\) denotes end diastolic volume, and \(V_{0,i}\) denotes the volume at zero pressure. The time- varying elastance function \(e(t)\) was given by

\[\begin{array}{r}e_{i}(t) = \left\{ \begin{array}{ll}\sin^{2}\left(\frac{\pi(t - t_{s h,i})}{2T_{r,i}}\right), & t_{s h,i}\leq t\\ & \mathrm{or}t< (t_{s h,i} + T_{r,i})\\ \cos^{2}\left(\frac{\pi(t - t_{s h,i} - T_{r,i})}{2(T_{s y s,i} - T_{r,i})}\right), & (t_{s h,i} + T_{r,i}\leq t\\ & \mathrm{or}t< (t_{s h,i} + T_{s y s,i})\\ 0, & (t_{s h,i} + T_{s y s,i})\leq t< T\\ & \mathrm{or}0\leq t< t_{s h,i} \end{array} \right. \end{array} \quad (19)\]

where \(i\) represents either atrium \(a\) , or ventricle \(v\) , \(T\) is the heart period, and \(T_{s y s,a}\) and \(T_{s y s,v}\) are the durations of the systolic periods for the atria and the ventricles, respectively. The latter were assumed to have a linear relationship with heart rate [10], given by

\[T_{s y s,v} = T_{s y s0} - \frac{k_{s y s}}{T} \quad (20)\]

and

\[T_{s y s,a} = \frac{T_{s y s,v}}{4} \quad (21)\]

where \(T_{s y s0}\) and \(k_{s y s}\) are constants, and \(t_{s h,a}\) and \(t_{s h,v}\) denote the time at the start of contraction for the atria and the ventricles respectively, with their relationship given by

\[t_{s h,v} = t_{s h,a} + T_{s y s,a}. \quad (22)\]

\(T_{r,a}\) and \(T_{r,v}\) denote the time intervals between the start of contraction and maximal contraction for the atria and the ventricles, respectively, and were assumed to be linear functions of \(T_{s y s,i}\)

\[T_{r,i} = k_{r,i}T_{s y s,i} \quad (23)\]

where \(k_{r,a}\) and \(k_{r,v}\) are constants. The overall time- varying PV relationships for the atria and the ventricles were given by

\[P = e_i(t)P_{e,s} + (1 - e_i(t))P_{e,d}. \quad (24)\]

## REFERENCES

[1] M. Vollkron, H. Schima, L. Huber, and G. Wieselthaler, "Interaction of the cardiovascular system with an implanted rotary assist device: Simulation study with a refined computer model," Artif. Organs, vol. 26, no. 4, pp. 349- 359, 2002.  
[2] T. Korakianitis and Y. Shi, "Numerical comparison of hemodynamics with atrium to aorta and ventricular apex to aorta vad support," ASJOA J., vol. 53, pp. 537- 548, 2007.  
[3] K. Reesink, A. Dekker, T. Van der Nagel, C. Beghi, F. Leonardi, P. Botti, G. De Cicco, R. Lorusso, F. Van der Veen, and J. Maessen, "Suction due to left ventricular assist: Implications for device control and management," Artif. Organs, vol. 31, no. 7, pp. 542- 549, 2007.  
[4] D. M. Karantonis, N. H. Lovell, P. J. Ayre, D. G. Mason, and S. L. Cloherty, "Identification and classification of physiologically significant pumping states in an implantable rotary blood pump," Artif. Organs, vol. 30, no. 9, pp. 671- 679, 2006.  
[5] S. Vandenberghe, P. Segers, P. Steendijk, B. Meyns, R. A. Dion, J. F. Antaki, and P. Verdonck, "Modeling ventricular function during cardiac assist: Does time- varying elastance work?" ASJOA J., vol. 52, no. 1, pp. 4- 8, 2006.  
[6] P. I. McConnell, C. L. Del Rio, P. Kwiatkowski, D. J. Farrar, and B. C. Sun, "Assessment of cardiac function during axial- flow left ventricular assist device support using a left ventricular pressure- derived relationship: Comparison with pre- load extractable stroke work," J. Heart Lung Transplant., vol. 26, no. 2, pp. 159- 166, 2007.  
[7] S. Vandenberghe, P. Segers, B. Meyns, and P. Verdonck, "Unloading effect of a rotary blood pump assessed by mathematical modeling," Artif. Organs, vol. 27, no. 12, pp. 1094- 1101, 2003.  
[8] K. Sagawa, L. Maughan, H. Suga, and K. Sunagawa, Cardiac Contraction and the Pressure- Volume Relationship. New York, Oxford: Oxford Univ. Press, 1988.  
[9] D. A. Kass, R. Beyar, E. Lankford, M. Heard, W. L. Maughan, and K. Sagawa, "Influence of contractile state on curvilinearity of in situ end- systolic pressure- volume relations," Circulation, vol. 79, pp. 167- 178, 1989.  
[10] M. Ursino, "Interaction between carotid baroregulation and the pulsating heart: A mathematical model," Amer. J. Physiol., vol. 275, no. 5, pp. H1733- H1747, 1998.  
[11] W. L. Maughan, K. Sunagawa, and K. Sagawa, "Ventricular systolic interdependence: Volume elastance model in isolated canine hearts," Amer. J. Physiol., vol. 253, no. 6, pp. H1381- H1390, 1987.  
[12] B. W. Smith, J. G. Chase, G. M. Shaw, and R. I. Nokes, "Simulating transient ventricular interaction using a minimal cardiovascular system model," Physiol. Meas., vol. 27, no. 2, pp. 165- 179, 2006.  
[13] E. Magosso and M. Ursino, "Cardiovascular response to dynamic aerobic exercise: A mathematical model," Med. Biol. Eng. Comput., vol. 40, no. 6, pp. 660- 674, 2002.  
[14] J. F. Nunn, Applied Respiratory Physiology. Boston, MA: Butterworth- Heinemann, 1993.  
[15] E. Lim, D. M. Karantonis, J. A. Reizes, S. L. Cloherty, D. G. Mason, and N. H. Lovell, "Noninvasive average flow and differential pressure estimation for an implantable rotary blood pump using dimensional analysis," IEEE Trans. Biomed. Eng., vol. 55, no. 8, pp. 2094- 2101, Aug. 2008.  
[16] E. Lim, S. L. Cloherty, J. A. Reizes, D. G. Mason, R. F. Salamonsen, D. M. Karantonis, and N. H. Lovell, "A dynamic lumped parameter model of the left ventricular assisted circulation," in Proc. 29th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc., Lyon, France, Aug. 22- 26, 2007, pp. 3990- 3993.  
[17] H. Schima, J. Honigschnebel, W. Trubel, and H. Thoma, "Computer simulation of the circulatory system during support with a rotary blood pump," ASJOA Trans., vol. 36, no. 3, pp. M252- M254, 1990.  
[18] I. G. Blaxland, "The effect of cap on the pulsatile dynamics of the heart," Master's thesis, Univ. New South Wales, Sydney, N.S.W., Australia, 2005.  
[19] A. C. Guyton and J. E. Hall, Textbook of Medical Physiology. Philadelphia, PA: Saunders, 1996.  
[20] A. Undar, C. M. Zapanta, J. D. Reibson, M. Souba, B. Lukic, W. J. Weiss, A. J. Snyder, A. R. Kunselman, W. S. Pierce, G. Rosenberg, and J. L. Myers, "Precise quantification of pressure flow waveforms of a pulsatile ventricular assist device," ASJOA J., vol. 51, no. 1, pp. 56- 59, 2005.  
[21] J. Lagarias, J. A. Reeds, M. H. Wright, and P. E. Wright, "Convergence properties of the Nelder- Mead simplex method in low dimensions," SIAM J. Optim., vol. 9, no. 1, pp. 112- 147, 1998.  
[22] S. Kono, K. Nishimura, T. Nishina, S. Yuasa, K. Ueyama, C. Hamada, T. Akamatsu, and M. Komeda, "Autosynchronized systolic unloading during left ventricular assist with a centrifugal pump," J. Thorac. Cardiovasc. Surg., vol. 125, no. 2, pp. 353- 360, 2003.  
[23] A. H. Goldstein, G. Monreal, A. Kambara, A. J. Spiwak, M. L. Schlossberg, A. R. A. Brishamchian, and M. A. Gerhardt, "Partial support with a centrifugal left ventricular assist device reduces myocardial oxygen consumption in chronic, ischemia heart failure," J. Cardiac Failure, vol. 11, no. 2, pp. 142- 151, 2005.  
[24] D. Morley, K. Litwak, P. Ferber, P. Spence, R. Dowling, B. Meyns, B. Griffith, and D. Burkhoff, "Hemodynamic effects of partial ventricular support in chronic heart failure: results of simulation validated with in vivo data," J. Thorac. Cardiovasc. Surg., vol. 133, no. 1, pp. 21- 28, 2007.  
[25] B. Meyns, T. Siess, Y. Nishimura, R. Racz, H. Reul, G. Rau, V. Leunens, and W. Flameng, "Miniaturized implantable rotary blood pump in atrial- aortic position support and unloads the failing heart," Cardiovasc. Surg., vol. 6, no. 3, pp. 288- 295, 1998.  
[26] D. J. Farrar, "Physiology of ventricular interactions during ventricular assistance," in Cardiac Assist Devices, D. J. Goldstein and M. C. Oz, Eds. Armonck, New York: Futura, 2000, pp. 15- 26.  
[27] A. C. Guyton, Cardiac Output and Its Regulation (Circulatory Physiology). Philadelphia, PA: Saunders, 1973.  
[28] K. Reesink, A. Dekker, T. van der Nagel, H. Blom, C. Soemers, G. Geskes, J. Maessen, and E. van der Veen, "Physiologic- insensitive left ventricular assist predisposes right- sided circulatory failure: A pilot simulation and validation study," Artif. Organs, vol. 28, no. 10, pp. 933- 939, 2004.  
[29] O. Tagwari, K. Yamazaki, P. Litwak, J. F. Antaki, M. Watach, L. M. Gordon, K. Kono, T. Mori, H. Koyanagi, B. P. Griffith, and R. L. Komos, "Effect of pressure- flow relationship of centrifugal pump on in vivo/hemodynamics: A consideration for design," Artif. Organs, vol. 22, no. 5, pp. 399- 404, 1998.  
[30] S. Choi, J. R. Boston, and J. F. Antaki, "Hemodynamic controller for left ventricular assist device based on pulsatility ratio," Artif. Organs, vol. 31, no. 2, pp. 114- 125, 2007.  
[31] T. Sakamoto, "Evaluation of native left ventricular function during mechanical circulatory support: Theoretical basis and clinical limitations," Ann. Thorac. Cardiovasc. Surg., vol. 8, pp. 1- 6, 2002.  
[32] D. L. Eckberg, P. Sleight, and B. Folkow, Human Baroreflexes in Health and Disease. Oxford, U.K.: Clarendon, 1992.  
[33] J. Linneweber, K. Nonaka, T. Takano, S. Kawahito, S. Schulte- Eistrup, T. Motomura, S. Ichikawa, M. Mikami, S. Stevens, H. Schima, E. Wolner, and Y. Nose, "Hemodynamic exercise response in calves with an implantable biventricular centrifugal blood pump," Artif. Organs, vol. 25, no. 12, pp. 1018- 1021, 2001.  
[34] H. Suga, Y. Tsumura, T. Nozawa, S. Futaki, and N. Tanaka, "Pressure- volume relation around zero transmural pressure in excised cross- circulated dog left ventricle," Circ. Res., vol. 63, pp. 361- 372, 1988.

Emily Lim received the BiomedE (Hons.) and M.Eng.Sc. degrees from the University of Malaya, Kuala Lumpur, Malaysia, 2003 and 2006, respectively. She is currently working toward the Ph.D. degree at the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, N.S.W., Australia.

Her current research interests include modeling and control of an implantable rotary blood pump.

> **Image description.** A portrait photograph of a middle-aged man, likely an author or researcher, set against a plain, light-colored background.
>
> The man has dark, neatly styled hair and is wearing rectangular-framed glasses. He is dressed professionally in a dark suit jacket or blazer over a light-colored collared shirt. He is positioned facing forward, looking directly at the viewer with a subtle, pleasant expression.
>
> The photograph is a head-and-shoulders shot, focusing entirely on the subject. The background is uniformly light, providing high contrast that makes the subject stand out.
>
> At the bottom of the image, there is a line of text that is partially visible and appears to be part of a caption or article excerpt. The visible text reads: "in nature involving techn".

Socrates Dokos received the Ph.D. degree in biomedical engineering from the University of New South Wales (UNSW), Sydney, N.S.W., Australia, in 1996.

He is currently a Senior Lecturer in the Graduate School of Biomedical Engineering, UNSW. His research interests include electrical and mechanical properties of cardiac and other excitable tissues using experimental and mathematical modeling techniques. He has authored or coauthored more than 40 papers and abstracts in international journals and meetings. This research has been multidisciplinary in nature, involving techniques ranging from electrophysiological recording to mechanical testing, as well as finite- element modeling and large- scale systems identification.

> **Image description.** A professional portrait photograph of a man, positioned against a plain white background, with a partial line of text visible at the bottom.
>
> The subject is a middle-aged man with a light complexion and short, dark hair that is receding. He is looking directly at the camera with a slight, pleasant expression. He is wearing a dark, likely black or navy, zip-up jacket or hoodie. The lighting is bright and even, typical of a studio portrait, highlighting the subject while keeping the background uniformly white.
>
> At the bottom of the image, a fragment of text is visible, appearing to be a title or a description of research. The visible text reads: "modeling and flow estimation". Based on the provided context, this phrase relates to the subject's academic and research work, specifically concerning the modeling and flow estimation for control of an implantable rotary blood pump. The text is positioned in the lower right corner of the frame.

Shaun L. Cloherty (M'00) received the B.E. (Hons.) degree in aerospace avionics from the Queensland University of Technology, Brisbane, Qld., Australia, and the Ph.D. degree in biomedical engineering from the University of New South Wales, Sydney, N.S.W., Australia.

From 2005 to 2007, he was a Research Associate in the Graduate School of Biomedical Engineering, University of New South Wales, where he was engaged in cardiac electrophysiology and modeling of functional heterogeneity in the cardiac pacemaker,

modeling and flow estimation for control of an implantable rotary blood pump, and modeling of electrical stimulation strategies for a retinal vision prosthesis. He is currently with the Visual Sciences Group, Research School of Biology, Australian National University, Canberra, A.C.T., Australia. His current research interests include aspects of development and organization of the mammalian visual cortex, information processing in the visual system, and the functional assessment of electrical stimulation strategies and the development of novel neural interfaces for a retinal vision prosthesis.

Dr. Cloherty is a Founding Officer of the New South Wales Chapter of the IEEE Engineering in Medicine and Biology Society, Sydney, Australia, and is a representative for the Asia Pacific region on the IEEE Engineering in Medicine and Biology Society's Administrative Committee (2010- 2012).

> **Image description.** A portrait photograph of an older man, likely a professional headshot, set against a plain, light gray background.
>
> The subject is a man with gray and white hair, which is relatively full and slightly wavy. He has a neatly trimmed beard that is also predominantly gray and white. He is wearing rectangular, dark-rimmed glasses. His expression is pleasant, featuring a slight, gentle smile.
>
> He is dressed in professional attire, consisting of a dark jacket (appearing black or very dark navy) worn over a lighter collared shirt, which is visible at the neck.
>
> The lighting is soft and even, illuminating the subject clearly and creating a neutral, professional aesthetic. The background is uniformly light gray, ensuring the focus remains entirely on the man.

Robert F. Salamonsen is currently an Emeritus Consultant in intensive care at the Alfred Hospital, Melbourne, Vic., Australia, where he is an Intensivist and has pioneered the introduction of ventricular assist devices and extracorporeal membrane oxygenation (ECMO) in Australia focussing, in particular, on applied physiology and medical management. He is an Associate Professor of surgery at Monash University, Melbourne. His current research interests include the development of physiological control for rotary blood pumps.

> **Image description.** A portrait photograph of a middle-aged man, set against a plain, light gray background, with partial text visible beneath the image.
>
> The man, who has dark, neatly styled hair, is shown from the chest up. He is wearing a collared shirt that appears to be a light blue or gray color. He is looking slightly off-camera to the viewer's right, presenting a neutral and professional expression. The lighting is soft and even, highlighting his features without harsh shadows.
>
> Below the photograph, there is a line of text that is partially visible and appears to be cut off. The visible text reads:
> "applied research of medic"
> "a"
> "# Task"

David G. Mason received the B.E. (Hons.), M.Eng.Sc., and Ph.D. degrees in biomedical engineering from the University of Melbourne, Melbourne, Vic., Australia. He is currently a Senior Research Fellow in the School of Information Technology and Electrical Engineering, University of Queensland, Brisbane, Qld., Australia. He has authored or coauthored more than 100 refereed journals, conference proceedings, book chapters, and patents. He has held U.K. and Australian university appointments and was involved in

applied research of medical device companies. His current research interests include physiological control and clinical advisory systems related to circulatory management, including rotary blood pumps and drug infusion systems, and also include biosignal processing for clinical diagnostic systems, including for remote sleep monitoring. He continues to foster university and industry linkages that improve the quality of patient care through the research and development of novel medical devices.

> **Image description.** A grayscale portrait photograph of an older man, accompanied by biographical text below the image.
>
> The photograph is a head-and-shoulders portrait of a man with short, receding gray hair. He is looking slightly off-camera to the viewer's left and has a gentle, slight smile. He is formally dressed in a dark suit jacket over a light-colored collared shirt. The lighting is soft, highlighting the contours of his face.
>
> Below the portrait, there is visible text. The first line of text reads: "Dr. Reizes was a Past Ed". Following this line, there is a small, seemingly unrelated string of characters: "गाय# Task". The text appears to be part of a biographical entry, though the full context is not visible.

John A. Reizes received the B.E., M.E., and Ph.D. degrees from the University of New South Wales (UNSW), Sydney, N.S.W., Australia, in 1960, 1965, and 1975, respectively.

He is currently an Adjunct Professor in the School of Mechanical and Manufacturing Engineering, UNSW, and the Faculty of Engineering, University of Technology Sydney, Sydney, N.S.W. He is the author or coauthor of more than 170 papers. He was the Chairman of the College of Mechanical Engineers.

Dr. Reizes was a Past Editor of the Mechanical Transaction of the Institution of Engineers Australia, and currently, the Chairman of the Australasian Fluids and Thermal Engineering Society. He was on the Engineering 2 Panel of the Australian Research Council (ARC), and on the ARC Collaborative Grants Committee. He was the recipient of the 2006 AGM Mitchell Medal, the highest honor, by the College of Mechanical Engineers of the Institution of Engineers Australia, for his contribution to the profession, sustained leadership in the development of mechanical engineering, and for his contribution to the art and science of mechanical engineering.

> **Image description.** A portrait photograph of a man, likely a professional headshot, set against a plain white background.
>
> The subject is a middle-aged man with a shaved or very closely cropped head. He is looking directly at the camera with a slight, pleasant smile. He is wearing a dark, solid-colored collared shirt, which appears to be black or dark gray. The lighting is bright and even, highlighting his features and creating a clean, professional appearance.
>
> To the right of the subject, there are fragments of text visible, suggesting this image is part of a larger document or biography. The visible text includes:
> *   "I"
> *   "t"
> *   "ing"
> *   "t"
> *   "interests include cardiac mod"
>
> The overall composition is a close-up portrait, focusing entirely on the man's upper body and face, with the text positioned in the margin to the right.

Nigel H. Lovell (M'91- SM'99) received the B.E. (Hons.) and Ph.D. degrees from the University of New South Wales (UNSW), Sydney, N.S.W., Australia.

He is currently a Professor of biomedical engineering with the Graduate School of Biomedical Engineering, UNSW, where he is an Adjunct Professor in the School of Electrical Engineering and Telecommunications. He has authored or coauthored more than 300 refereed journals, conference proceedings, book chapters, and patents. His current research interests include cardiac modeling, telehealth technologies, biological signal processing, and visual prosthesis design.

terests include cardiac modeling, telehealth technologies, biological signal processing, and visual prosthesis design.

Dr. Lovell was the IEEE Engineering in Medicine and Biology Society (EMBS) Vice President (VP) for Conferences (2004/2005 and 2010/2011) and VP for Member and Student Activities (2002/2003), and the program cochair for the Annual IEEE EMBS Conference in Lyon, France, in 2007. In 2000, he was awarded the IEEE Millennium Medal for services to the IEEE EMBS and the profession.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
