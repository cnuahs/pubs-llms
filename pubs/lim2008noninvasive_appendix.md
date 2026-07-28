# Noninvasive Average Flow and Differential Pressure Estimation for an Implantable Rotary Blood Pump Using Dimensional Analysis - Appendix

---

## APPENDIX A

The performance of a turbomachine depends on a number of variables, including pump differential pressure \((\Delta p)\) , input power \((P)\) , and efficiency. Since the present work aims to estimate flow and differential pressure across the pump from the pump input power, fluid viscosity, and impeller speed, we need at least two equations, one for the total pressure rise across the pump, \(\Delta p\) , and another for power required to drive the pump, \(P\) . \(\Delta p\) and \(P\) depend on the speed of the impeller \((\omega)\) , flow across the pump \((Q)\) , viscosity of the fluid \((\mu)\) , as well as the geometric parameters of the pump, which include pump impeller diameter \((D)\) , lengths \((l)\) , and angles \((\alpha)\) required to fully describe the

pump body and rotor.

\[\Delta p = f_{1}(\omega ,Q,\mu ,\rho ,D,l_{1},\ldots ,l_{m},\alpha_{1},\ldots ,\alpha_{n}) \quad (12)\]

\[P = f_{2}(\omega ,Q,\mu ,\rho ,D,l_{1},\ldots ,l_{m},\alpha_{1},\ldots ,\alpha_{n}). \quad (13)\]

Buckingham's \(\pi\) theorem was used to reduce the number of variables in (12) and (13) into a smaller number of nondimensional groupings [10], [11]. The theorem states that: Given a relation among \(j\) parameters of the form

\[q_{1} = f_{1}(q_{2},q_{3},\ldots ,q_{j})\]

the \(j\) parameters may be grouped into \(j\) - \(r\) independent dimensionless parameters in the form of

\[\Pi_{1} = F_{1}(\Pi_{2},\Pi_{3},\ldots ,\Pi_{j - r})\]

where \(r\) is usually equal to the minimum number of independent dimensions, called repeating variables, required to specify the dimensions of all the parameters.

In the first step of the derivation, \(\rho\) (dimension \(= ML^{- 3}\) ), \(\omega\) (dimension \(= T^{- 1}\) ), and \(D\) (dimension \(= L\) ) were selected as a set of repeating variables since it includes all the primary dimensions, i.e., MLT. Equations (12) and (13) were then transformed into nondimensional forms, i.e., (14) and (15), by dividing each dimensional term in the equations by a combination of the repeating variables taken to appropriate powers

\[\frac{\Delta p}{\rho\omega^2D^2} = F_1\left(\frac{Q}{\omega D^3},\frac{\rho\omega D^2}{\mu},\frac{l_1}{D},\ldots ,\frac{l_m}{D},\alpha_1,\ldots ,\alpha_n\right) \quad (14)\]

\[\frac{P}{\rho\omega^3D^5} = F_2\left(\frac{Q}{\omega D^3},\frac{\rho\omega D^2}{\mu},\frac{l_1}{D},\ldots ,\frac{l_m}{D},\alpha_1,\ldots ,\alpha_n\right). \quad (15)\]

Since attention is limited to a single model of a rotary centrifugal blood pump, the geometrical parameters are in principle the same for all copies of the pump, so (14) and (15) reduce to

\[\frac{\Delta p}{\rho\omega^2D^2} = F_3\left(\frac{Q}{\omega D^3},\frac{\rho\omega D^2}{\mu}\right) \quad (16)\]

\[\frac{P}{\rho\omega^3D^5} = F_4\left(\frac{Q}{\omega D^3},\frac{\rho\omega D^2}{\mu}\right). \quad (17)\]

Thus, complete similarity in pump performance tests would require identical flow coefficients and Reynolds numbers. Since the flow through the clearances is controlled by different physical phenomena to those involved in pumping, it has been suggested that a number of Reynolds numbers may be needed to fully describe the flow in a pump.

In practice, the viscous effects (Reynolds numbers) are unimportant for fully turbulent flow. The conventional laminar- to- turbulent flow transition value for the pump Reynolds number is approximately 2 000 000 (scaled from 500 000 to account for difference in Reynolds number definition) [20]. However, since blood pumps usually operate in or near the laminar flow region [2], with a relatively low Reynolds number (65 000- 220 000 for our test data), viscosity effects have to be taken into account.

Furthermore, since the measured input power is the power supplied by the controller to the motor coils, electromechanical power consumption, which largely depends on the motor speed, needs to be considered.

## REFERENCES

[1] D. Esmore, D. Kaye, R. Salamonsen, M. Buckland, M. Rowland, J. Negri, Y. Rowley, J. Woodard, J. Begg, and P. Ayre, "First clinical implant of the VentrAssist left ventricular assist system as destination therapy for end- stage heart failure," J. Heart Lung Transplant, vol. 24, pp. 1150- 1154, 2005.  
[2] W. A. Smith, M. Goodin, M. Fu, and L. Xu, "System analysis of the flow/pressure response of rotodynamic blood pumps," Artif. Organs, vol. 23, pp. 947- 955, 1999.  
[3] G. A. Giridharan and M. Skliar, "Control strategy for maintaining physiological perfusion with rotary blood pumps," Artif. Organs, vol. 27, pp. 639- 648, 2003.  
[4] Y. Wu, P. Allaire, G. Tao, and D. Olsen, "Study of pressure estimation for automated circulatory system with a LVAD," in Proc. 2006 Amer. Control Conf., pp. 713- 718.  
[5] C. Bertram, "Measurement for implantable rotary blood pumps," Physiol. Meas., vol. 26, pp. R99- R117, 2005.  
[6] M. Yoshizawa, T. Sato, A. Tanaka, K. Abe, H. Takeda, T. Yambe, S. Nitta, and Y. Nose, "Sensorless estimation of pressure head and flow of a continuous artificial heart based on input power and rotational speed," ASAIO J., vol. 48, pp. 443- 448, 2002.  
[7] P. J. Ayre, N. H. Lovell, and J. C. Woodard, "Non- invasive flow estimation in an implantable rotary blood pump: A study considering non- pulsatile and pulsatile flows," Physiol. Meas., vol. 24, pp. 179- 189, 2003.  
[8] A. Funakubo, S. Ahmed, I. Sakuma, and Y. Fukui, "Flow rate and pressure head estimation in a centrifugal blood pump," Artif. Organs, vol. 26, pp. 985- 990, 2002.  
[9] N. Malagutti, D. M. Karantonis, S. L. Cloherty, P. J. Ayre, D. G. Mason, R. F. Salamonsen, and N. H. Lovell, "Non- invasive average flow estimation for an implantable rotary blood pump: a new algorithm incorporating the role of blood viscosity," Artif. Organs, vol. 31, pp. 45- 52, 2007.  
[10] R. W. Fox and A. T. McDonald, Introduction to Fluid Mechanics, 6th ed. New York: Wiley, 2004, pp. 273- 300.  
[11] E. Buckingham, "On physically similar systems: Illustrations of the use of dimensional equations," Phys. Rev., vol. 4, no. 4, pp. 345- 376, Oct. 1914.  
[12] T. Tsukiya, T. Akamatsu, K. Nishimura, T. Yamada, and T. Nakazeki, "Use of motor current in flow rate measurement for the magnetically suspended centrifugal blood pump," Artif. Organs, vol. 21, pp. 396- 401, 1997.  
[13] A. C. Guyton and J. E. Hall, Textbook of Medical Physiology, 9th ed. Philadelphia, PA: Saunders, 1996, pp. 168.  
[14] Y. Wakisaka, Y. Okuzono, Y. Taenaka, K. Chikanari, T. Masuzawa, T. Nakatani, E. Tatsumi, T. Nishimura, Y. Takewa, T. Ohno, and H. Takano, "Noninvasive pump flow estimation of a centrifugal blood pump," Artif. Organs, vol. 21, pp. 651- 654, 1997.  
[15] T. Tsukiya, Y. Taenaka, T. Nishinaka, M. Oshikawa, H. Ohnishi, E. Tatsumi, H. Takano, Y. Konishi, K. Ito, and M. Shimada, "Application of indirect flow rate measurement using motor driving signals to a centrifugal blood pump with an integrated motor," Artif. Organs, vol. 25, pp. 692- 696, 2001.  
[16] Y. W. Wong, W. K. Chan, S. C. M. Yu, and L. P. Chua, "Effects of scaling on centrifugal blood pumps," Artif. Organs, vol. 26, pp. 998- 1001, 2002.  
[17] M. Lorenz and W. A. Smith, "Rotodynamic pump scaling," ASAIO J., vol. 48, pp. 419- 430, 2002.  
[18] T. Kitamura, Y. Matsushima, T. Tokuyama, S. Kono, K. Nishimura, M. Komeda, M. Yanai, T. Kijima, and C. Nojiri, "Physical model- based indirect measurements of blood pressure and flow using a centrifugal pump," Artif. Organs, vol. 24, pp. 589- 593, 2000.  
[19] D. M. Karantonis, S. L. Cloherty, D. G. Mason, P. J. Ayre, and N. H. Lovell, "Noninvasive pulsatile flow estimation for an implantable rotary blood pump," in Proc. 29th Annu. Int. Conf. IEEE Eng. Med. Biol., Lyon, France, Aug. 23- 26, pp. 1018- 1021.  
[20] R. H. Sabersky, A. J. Acosta, and E. G. Hauptmann, Fluid Flow, 2nd ed. New York: Macmillan, 1971, p. 423.

> **Image description.** A professional head-and-shoulders portrait photograph of a young woman set against a plain, light background.
>
> The subject is positioned centrally and faces the viewer directly. She has dark, straight hair that falls past her shoulders. Her complexion is fair, and she has a subtle, pleasant expression with a slight smile. Her eyes are light-colored, and her features are well-defined. She appears to be wearing dark clothing, though only the upper portion of her shoulders and chest is visible.
>
> The background is uniformly light gray or white, providing a neutral contrast that keeps the focus entirely on the subject.
>
> On the right side of the image, there is a vertical column of text and symbols that appears to be part of the surrounding document layout. This column includes visible characters such as "H", "N", "a", and other non-Latin characters, suggesting it is a partial transcription or formatting artifact from the original source document. The text is oriented vertically and is partially cut off by the edge of the frame.

Emily Lim received the B. Biomed.E. (Hons.) and M.E. degrees from the University of Malaya (UM), Kuala Lumpur, Malaysia, in 2006. She is currently working toward the Ph.D. degree at the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, Australia.

Her current research interests include modeling and control of an implantable rotary blood pump.

> **Image description.** A head-and-shoulders photograph of a middle-aged man is displayed on the left side of the image, positioned next to a column of partially visible biographical text.
>
> The man has short, dark brown hair and is wearing dark-rimmed rectangular glasses. He is dressed in a dark, possibly black, collared shirt or jacket. He is looking directly at the camera with a slight, pleasant smile that reveals his teeth. The lighting is soft, highlighting his face, while the background is uniformly dark and indistinct, suggesting an indoor setting.
>
> To the right of the photograph, there is a column of text. The text is partially cut off at the top and bottom, but the visible fragments include:
> - "I"
> - "C"
> - "F"
> - "S"
> - "a"
>
> The overall composition suggests this image is part of a professional profile or faculty directory.

Dean M. Karantonis (S'05) received the B.E. (Hons.) degree in computer engineering and the M. Biomed.E. degree in biomedical engineering in 2005 from the University of New South Wales (UNSW), Sydney, Australia, where he is currently working toward the Ph.D. degree at the Graduate School of Biomedical Engineering.

His current research interests include simulation and control of an implantable rotary blood pump.

> **Image description.** A portrait photograph of an older man, accompanied by biographical text, likely from an academic or professional publication.
>
> The photograph features a middle-aged to elderly man, identified by the accompanying text as Dr. Reizes. He has short, light-colored hair and is wearing a dark suit jacket over a light-colored shirt. He is positioned facing slightly toward the viewer and has a gentle, pleasant expression, smiling slightly. The lighting is bright and even, highlighting his features.
>
> Below the photograph, there is a caption in black text. The visible portion of the text reads: "Dr. Reizes was a Past". To the right of the photograph, there are fragments of other text, including the letters "J", "n", "o", "w", and "T", which appear to be part of a larger, cut-off column of text.
>
> The overall composition is typical of a biographical entry, presenting a professional portrait alongside a brief description of the subject's career or achievements.

John A. Reizes received the B.E., M.E., and Ph.D. degrees from the University of New South Wales (UNSW), Sydney, Australia, in 1960, 1965, and 1975, respectively.

He is currently an Adjunct Professor at the School of Mechanical and Manufacturing Engineering, University of New South Wales (UNSW), Sydney, Australia, and the Faculty of Engineering, University of Technology Sydney (UTS), Sydney. He is the author or coauthor of more than 170 papers. He was a Chairman of the College of Mechanical Engineers.

Dr. Reizes was a Past Editor of the Mechanical Transaction of the Institution of Engineers Australia, and currently, the Chairman of the Australasian Fluids and Thermal Engineering Society. He was on the Engineering 2 Panel of the Australian Research Council (ARC), and on the ARC Collaborative Grants Committee. He was the recipient of the 2006 AGM Michell Medal by the College of Mechanical Engineers of the Institution of Engineers Australia, its highest honor, for his contribution to the profession, sustained leadership in the development of mechanical engineering, and for his contribution to the art and science of mechanical engineering.

> **Image description.** A grayscale portrait photograph of a middle-aged man, presented within a document layout that includes surrounding text fragments.
>
> The central image is a head-and-shoulders portrait of a man with dark, neatly combed hair. He is wearing a light-colored collared shirt and a dark necktie. He is looking directly toward the viewer with a neutral expression. The lighting is focused on the subject, creating a contrast against a dark, slightly textured background, which appears uniform and indistinct.
>
> The photograph is positioned on a page that contains several fragments of text. The visible text surrounding the portrait includes:
> *   In the upper left corner: "d, ye"
> *   Below that: "g"
> *   In the lower left corner: "with the University of Lon"
>
> The overall composition is typical of an academic or professional biography, featuring a formal portrait alongside biographical information.

David G. Mason was born Fremantle, Western Australia on December 7, 1962. He received the Graduate degree in electrical and electronic engineering from the University of Melbourne, Melbourne, Australia, in 1985, and the Ph.D. degree in expert systems for closed- loop drug infusion systems in intensive care from the Royal Melbourne Hospital, Melbourne, in 1990.

He was earlier with Telectronics, Ltd., Sydney, where he was engaged in research on rhythm discriminators for implantable defibrillators, and later,

with the University of London, London, U.K., where he developed endocardial electrodes for treatment of atrial flutter. During 2001, he was in Melbourne to develop an expert advisory system for circulatory management in intensive care. During 2004, he was engaged in research on feedback controller for a left ventricular assist device with Ventracor Limited. He is currently in the Department of Surgery, Monash University, Victoria, Australia, as a Senior Research Fellow.

> **Image description.** A portrait photograph of a man set against a plain white background.
>
> The subject is a middle-aged man with a shaved head or very short, dark hair. He is looking directly at the camera with a slight, pleasant smile. He is wearing a dark, collared shirt, which appears to be black or a very dark navy. The photograph is a head-and-shoulders shot, focusing primarily on his face and upper torso.
>
> The image is cropped from a larger document, as several fragments of text are visible around the subject.
>
> Visible text fragments include:
> *   Top left: "...o."
> *   Middle left: "s"
> *   Middle left: "5,"
> *   Bottom left: "ol"
> *   Bottom center/right: "ologies, biological signal"
> *   Bottom right: "a" (part of a word)

Nigel H. Lovell (M'90- SM'98) received the B.E. (Hons.) and Ph.D. degrees from the University of New South Wales (UNSW), Sydney, Australia.

He is currently a Professor of Biomedical Engineering at the Graduate School of Biomedical Engineering, UNSW, and an Adjunct Professor in the School of Electrical Engineering and Telecommunications, UNSW. He is the author or coauthor of more than 250 refereed journals, conference proceedings, book chapters, and patents. His current research interests include cardiac modeling, home telecare technologies, biological signal processing, and visual prosthesis design.

Dr. Lovell was the IEEE Engineering in Medicine and Biology Society (EMBS) Vice- President (VP) for Conferences (2004/2005) and VP for Member and Student Activities (2002/2003). He was the Program Co- Chair for the Annual IEEE Engineering in Medicine and Biology Society (EMBS) Conference 2007 that was held in Lyon, France.

> **Image description.** A professional headshot of a man, positioned on the left side of the frame, accompanied by fragmented text from a document.
>
> The subject is a man with light skin and short, dark hair that shows some recession at the temples. He is looking directly at the camera with a neutral, slight smile. He is wearing a dark, high-collared shirt, which appears to be black or a very dark gray. The background is uniformly plain and light gray or off-white, providing a neutral contrast to the subject.
>
> The image contains several fragments of text, suggesting it is part of a larger biographical or academic listing:
>
> *   **Top Right:** A vertical column of text is partially visible, starting with the letters "S", "U", "l", "i", "n", "a", "p", and "e".
> *   **Bottom Center/Left:** A horizontal line of text is visible below the subject, which reads: "pump, and modeling of elec".
>
> The overall composition suggests the image is used to introduce an individual, likely an academic or researcher, given the technical nature of the visible text fragments related to "modeling" and "pump."

Shaun L. Cloherty (M'00) received the B.E. (Hons.) degree in aerospace avionics from the Queensland University of Technology, Brisbane, Australia, and the Ph.D. degree in biomedical engineering from the University of New South Wales, Sydney, Australia.

During 2005- 2007, he was a Research Associate at the Graduate School of Biomedical Engineering, Sydney, where he was engaged in research on cardiac electrophysiology and modeling, flow estimation and modeling for control of an implantable rotary blood

pump, and modeling of electrical stimulation strategies for a retinal vision prosthesis. He is currently a Postdoctoral Fellow in the Research School of Biological Sciences, Australian National University, Canberra, Australia. His current research interests include mammalian visual cortex and functional assessment of electrical stimulation strategies for a retinal vision prosthesis.

Dr. Cloherty is a Founding Officer of the New South Wales Chapter of the IEEE Engineering in Medicine and Biology Society, Sydney, Australia.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
