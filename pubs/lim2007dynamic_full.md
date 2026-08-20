```
@article{lim2007dynamic,
  title={A Dynamic Lumped Parameter Model of the Left Ventricular Assisted Circulation},
  author={Einly Lim and Shaun L. Cloherty and John A. Reizes and David G. Mason and Robert F. Salamonsen and Dean M. Karantonis and Nigel H. Lovell},
  journal={29th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2007},
  pages={3990-3993},
  doi={10.1109/iembs.2007.4353208},
  url={https://ieeexplore.ieee.org/document/4353208}
}
```

---

# A Dynamic Lumped Parameter Model of the Left Ventricular Assisted Circulation

Einly Lim, Shaun L. Cloherty, Member, IEEE, John A. Reizes, David G. Mason, Robert F. Salamonsen, Dean M. Karantonis, Student Member, IEEE, Nigel H. Lovell, Senior Member, IEEE

Abstract—A lumped parameter model of the cardiovascular system (CVS) and its interaction with an implantable rotary blood pump (iRBP) is presented. The CVS model consists of the heart, the systemic and the pulmonary circulations. The pump model is made up of three differential equations, i.e. the motor equation, the torque equation and the hydraulic equation. Qualitative comparison with data from ex vivo porcine experiments suggests that the model is able to simulate different physiologically significant pumping states with varying pump speed set points. The combined CVS- iRBP model is suitable for use as a tool for investigating changes in the circulatory system parameters in the presence of the pump, and for testing control algorithms.

## I. INTRODUCTION

I. INTRODUCTIONIimplantable rotary blood pumps (iRBPs) have a potential as bridge-to-transplantation and destination therapy devices for end-stage heart failure patients [1]. However, due to the insensitivity of iRBPs to preload, and variation in pump and circulatory system parameters such as resistance of the blood vessels or ventricular contractility, dangerous pumping states may arise (e.g. insufficient perfusion, ventricular collapse etc.) [2]. For the most part, interaction between iRBPs and the cardiovascular system may be only partially explored through in vivo animal studies due to limitations of available animal models of heart failure and complexity in the experimental procedures [3]. Numerical models, able to simulate the response of the human cardiovascular system in the presence of an iRBP, can provide additional insight into the dynamics of assisted circulation. Such models may also provide an ideal platform for the development and evaluation of robust physiological pump control algorithms by easily allowing reproducible experiments under identical conditions.

In this paper we describe a lumped parameter model of the healthy human cardiovascular system (CVS) augmented by an iRBP. Model parameters for the CVS are derived from the literature while those for the pump are based on pump characteristic curves obtained in mock loop experiments. The simulated response of the

combined CVS- iRBP model at a range of pump operating points is qualitatively compared to experimental data recorded during acute implantation of iRBPs in healthy pigs.

## II. METHODS

### A. Model Description

A. 1 The Human Cardiovascular System Model

The lumped parameter CVS model is adapted from that formulated by Blaxland [4]. An electrical equivalent circuit analogue of the CVS model is illustrated in Fig. 1. The model includes 12 compartments comprising the left and right sides of the heart and both the pulmonary and systemic circulations. In addition, the model also includes formulations for ventricular interaction via the interventricular septum and pericardium. Ventricular interaction via the inter-ventricular septum is modelled according to the three- element system described by Maughan et al. [5], where the two ventricles are divided into three parts, i.e. the right ventricle wall, the left ventricle wall and the septum wall. The luminal volumes of the left and right ventricles are enclosed by the left and right ventricular free- walls and separated by the interventricular septum. The entire heart is enclosed within the compliant pericardium, which constrains the diastolic filling capacity of the heart chambers. Baroreflex regulation of the aortic pressure, as presented in [4], is not included in the present model. The CVS model was validated using data obtained from the literature. For a more detailed description of the model formulations, see Blaxland [4].

### A.2 The VentrAssistTM iRBP Model

The VentrAssistTM iRBP (Ventracor Ltd, Sydney, Australia) is a centrifugal blood pump with a hydrodynamic bearing [6]. The magnetic interaction between the permanent magnets in the impeller blades and the oscillating current in the stator windings (encapsulated in the pump housing) provide the driving torque to turn the impeller. Commutation of the driving coils uses a three- phase, six- stepped switching principle. When the impeller (rotor) rotates at a constant speed, the back electromotive force (BEMF) will be induced in the stator windings. In order to produce the maximum torque production efficiency, synchronization between the phase currents and the induced BEMF is important and is achieved through a sensorless hardware scheme [7]. A proportional- integral control algorithm is used to track the desired average pump speed by modulating the pulse width of the driving voltage signal.

> **Image description.** A complex technical schematic diagram illustrating the electrical equivalent circuit analogue of the human cardiovascular system, integrated with a lumped parameter model of a pump and cannulae. The diagram is composed of numerous interconnected electrical circuit symbols, including voltage sources (represented by circles with arrows), resistors (rectangles), and inductors (coils), arranged in a flow path from left to right.
>
> The circuit can be divided into three main sections: the input system (left), the pump/motor model (center), and the output system (right).
>
> **Input System (Left Side):**
> The input section models the initial pressure and resistance of the pulmonary system. It consists of a series of components:
> *   $E_{pu}$ and $R_{pu}$
> *   $E_{pc}$ and $R_{pc}$
> *   $E_{pa}$ and $R_{pa}$
> These elements are arranged sequentially, representing the initial resistance and pressure sources before the flow enters the pump.
>
> **Pump and Motor Model (Center):**
> This central section represents the active pump mechanism and its associated electrical dynamics.
> *   **Motor Windings:** The top portion features the motor windings, including components $E_{la}$, $R_{la}$, $L_{la}$, $E_{lm}$, $R_{lm}$, and $L_{lm}$. These are connected in a complex configuration, likely representing the electrical characteristics of the motor.
> *   **Pump/Flow Path:** The bottom portion of the center section includes components $E_{tc}$, $R_{tc}$, $L_{tc}$, $E_{rc}$, $R_{rc}$, and $L_{rc}$, modeling the hydraulic properties of the pump itself.
> *   **Cannulae and External Connections:** The pump is connected to external flow elements:
>     *   $R_{in}$ and $L_{in}$ are shown in series, representing the inflow cannula.
>     *   $R_{inc}$ is shown prior to the inflow cannula, noted as simulating suction events, with its magnitude being a function of left ventricular pressure.
>     *   $E_{lv}$ is a voltage source connected to the pump system.
>
> **Output System (Right Side):**
> The output section models the systemic circulation (aorta and subsequent vessels). It is a long series of components:
> *   $E_{av}$ and $R_{av}$
> *   $L_{av}$
> *   $E_{co}$ and $R_{co}$
> *   $L_{co}$
> *   $E_{sa}$ and $R_{sa}$
> *   $E_{sc}$ and $R_{sc}$
> *   $E_{sv}$ and $R_{sv}$
> These elements are arranged sequentially, representing the resistance and pressure characteristics of the outflow.
>
> **Overall Arrangement:**
> The entire diagram is a single, continuous schematic. The flow path begins at the input components on the far left, passes through the central pump/motor assembly, and terminates at the output components on the far right. The use of standard electrical symbols allows the complex biological system to be modeled using electrical principles, where pressure corresponds to voltage and flow corresponds to current.

<center>Fig. 1. Electrical equivalent circuit analogue of the human cardiovascular system model combined with the lumped parameter model of the pump and cannulae. For clarity, the capacitive elements \((C_{i} = 1 / E_{i})\) representing the compliance of the various compartments are not shown, nor are the resistive elements representing the viscoelastic properties of the pulmonary artery and the aorta. For a description of each compartment see Blaxland [4]. </center>

The pump is modeled using three differential equations; the motor windings electrical equation (2), the electromagnetic torque transfer equation (3), and the pump hydraulic equation (4). In addition, the inflow and outflow cannulae are each modeled in terms of a constant flow resistance \((R_{in}\) & \(R_{out})\) which causes pressure drop, and a series inductance \((L_{in}\) & \(L_{out})\) which resists changes in flow rate. A third resistance \((R_{inc})\) is included prior to the inflow cannula to simulate suction events [8]. The magnitude of this variable resistance is a function of left ventricular pressure.

(i) Motor windings electrical equation

\[V = I(R + jX) + E \quad (1)\]

where \(\mathbf{V}\) is the motor terminal voltage vector, \(I\) is the motor current vector, \(R\) is motor winding resistance and \(X\) is the motor winding reactance. \(E\) is the BEMF given by,

\[E = k_{e}\omega_{e} \quad (2)\]

where \(k_{e} = 8.48\mathrm{e - 3V / rads^{- 1}}\) is the BEMF constant and \(\omega_{e}\) is the electrical speed \((\omega_{e} = 2\omega\) , where \(\omega\) is the impeller speed in rad/s).

Since the phase current is synchronized with the BEMF voltage to produce maximum torque efficiency, equation (1) can be written as a scalar equation,

\[V = k_{e}\omega_{e} + RI + L\frac{dI}{dt}, \quad (2)\]

where \(V\) is motor terminal voltage (V), \(I\) is the motor phase current (A), \(R = 1.38\Omega\) is the motor winding resistance and \(L = 0.439\mathrm{mH}\) is the motor winding inductance. \(V\) was adjusted by the proportional- integral controller to track the desired average pump speed.

(ii) Electromagnetic torque transfer equation

The electromagnetic torque produced by the interaction between the permanent magnets in the blades of the impeller and the phase currents of the three coil

windings is proportional to the BEMF constant and the phase current [9]. The resulting electromechanical energy is converted into the inertial energy used to accelerate or decelerate the impeller, the fluid energy for the pump, as well as various losses. Since theoretical derivation of the load/friction torque on the impeller is complicated by the various losses, dimensional analysis [10] is used to formulate a relationship between the input torque (proportional to the current) and the load/friction torque (depending on the flow and the pump speed) under steady flow conditions, i.e.,

\[\begin{array}{l}{T_{e} = 3k_{e}I = J\frac{d\omega}{dt} +f(Q,\omega)}\\ {f(Q,\omega) = a\vec{Q}^{\prime}\omega +bQ\omega^{2} + c\omega +d\omega^{3}} \end{array} \quad (3)\]

where \(T_{e}\) is the input electromagnetic torque \((\mathrm{kg.m^2 / s^2})\) , \(Q\) is the pump flow rate (L/min) and \(J = 7.74\mathrm{e - 6kg.m^2}\) is the moment of inertia of the impeller. The moment of inertia of the fluid within the pump (i.e., around the impeller) is neglected since it is small compared to that of the impeller. Polynomial coefficients; \(a = 4.38\mathrm{e - 7}\) , \(b = 1.19\mathrm{e - 8}\) , \(c = 1.92\mathrm{e - 5}\) and \(d = 3.14\mathrm{e - 10}\) were obtained by least squares fitting of the experimental data obtained under steady flow conditions.

(iii) Pump hydraulic equation

The hydraulic equation is derived through empirical fitting of the pump characteristic curve obtained from experiments carried out under steady flow conditions,

\[\Delta P = e + fQ^{3} + g\omega^{2} \quad (4)\]

where \(\Delta P\) is the differential pressure across the pump \((\mathrm{mmHg})\) , \(e = - 6\) , \(f = - 0.0524\) , and \(g = 0.0019\) . The intersection between the pump characteristic curve and the cardiovascular system resistance curve determines the pump flow and differential pressure across the pump.

> **Image description.** A multi-panel line graph displaying physiological and pump performance data over a 3-second period, representing measurements taken during the acute implantation of a VentraAssist iRBP in a pig. The graph is composed of four stacked panels, each tracking a different set of variables, all sharing a common horizontal time axis labeled from 0 to 3 sec.
>
> The panels are organized as follows:
>
> 1.  **Flow Panel (Top):** This panel plots flow rate in L/min (Y-axis scale 0 to 15). It contains two red lines representing Qav (aortic flow rate) and Qp (pump flow rate). Both lines exhibit highly oscillatory waveforms, showing distinct peaks and troughs that correspond to the labeled physiological states below.
> 2.  **Pressure Panel (Second from Top):** This panel plots pressure in mmHg (Y-axis scale 0 to 80). It also features two red lines, representing Pao (aortic pressure) and Piv (left ventricular pressure). These lines show synchronized oscillatory patterns, mirroring the flow dynamics in the panel above.
> 3.  **Speed Panel (Third from Top):** This panel plots pump speed in rpm (Y-axis scale 0 to 3000). It contains a single black line that displays step-like changes in speed, indicating transitions between the different operational states.
> 4.  **Current Panel (Bottom):** This panel plots current in Amperes (A) (Y-axis scale 0 to 1). It features a single black line showing oscillatory waveforms, which fluctuate in response to the changes in pump speed.
>
> The entire graph is annotated with four vertical markers labeled PR, VE, ANO, and VC, which denote specific physiological pumping states: PR (pump regurgitation), VE (ventricular ejection), ANO (aortic valve not opening), and VC (ventricular collapse). A legend on the right side of the graph identifies the variables: Qav, Qp, Pao, Piv, Speed, and Current. The data visually demonstrates the relationship between pump operation (speed and current) and the resulting physiological measurements (flow and pressure) across the different cardiac phases.

<center>Fig. 2. Invasive flow rate (Qav and Qp) and pressure (Piv and Pao) measurements, and non-invasive pump speed and supply current waveforms obtained during acute implantation of the VentraAssist iRBP in healthy pigs. Four pump speed set points (1250, 1800, 2400 and \(2700\mathrm{rpm}\) ) are shown, corresponding to four physiologically significant pumping states: PR, pump regurgitation; VE, ventricular ejection; ANO, aortic valve not opening; and VC, ventricular collapse. (Qav, aortic flow rate; Qp, pump flow rate; Pao, aortic pressure; Piv, left ventricular pressure) </center>

> **Image description.** A multi-panel time-series line graph displaying various physiological and pump performance metrics over a 3-second period, representing data obtained during the acute implantation of a VentraAssist iRBP in a pig. The graph is composed of four stacked panels, each tracking a different variable against a shared horizontal time axis (0 to 3 seconds).
>
> The top of the graph features annotations marking four distinct physiological states: PR (pump regurgitation), VE (ventricular ejection), ANO (aortic valve not opening), and VC (ventricular collapse). A legend in the upper right corner identifies the variables: Qav (aortic flow rate), Qp (pump flow rate), Pao (aortic pressure), and Piv (left ventricular pressure).
>
> The four panels are detailed as follows:
>
> 1.  **Flow (L/min):** This top panel plots flow rate. The red line, representing Qav (aortic flow rate), shows sharp, high-amplitude pulsatile peaks. The black line, representing Qp (pump flow rate), shows a generally higher, smoother flow rate with less pronounced pulsatility compared to Qav.
> 2.  **Pressure (mmHg):** The second panel plots pressure. The red line, representing Pao (aortic pressure), exhibits sharp, high-magnitude pulsatile spikes. The black line, representing Piv (left ventricular pressure), shows lower, rounded pulsatile peaks.
> 3.  **Speed (rpm):** The third panel plots pump speed. A single black line shows the speed maintaining a relatively high and stable level (approximately 2700 rpm) throughout the 3-second duration, with minor fluctuations.
> 4.  **Current (A):** The bottom panel plots motor current. A single black line shows rapid, distinct fluctuations and spikes in current, which appear synchronized with the pulsatile events observed in the flow and pressure panels above.
>
> The overall visual pattern demonstrates the relationship between the pump's mechanical operation (speed and current) and the resulting physiological outputs (flow and pressure) across different cardiac phases.

<center>Fig. 3. Simulated flow rates (Qav and Qp), pressures (Piv and Pao) and pump speed and current waveforms obtained from the combined CVS-iRBP model. Four pump speed set points (1800, 2200, 2700 and 3000 rpm) are shown, corresponding to the same four physiological significant pumping states as in Fig. 2, namely, PR, pump regurgitation; VE, ventricular ejection; ANO, aortic valve not opening; and VC, ventricular collapse. (Qav, aortic flow rate; Qp, pump flow rate; Pao, aortic pressure; Piv, left ventricular pressure) </center>

## A.3 Model Implementation

The model is implemented in MATLAB (The Mathworks, Inc., Natick, MA, USA) using an Ordinary Differential Equation (ODE) solver. The algorithm is run on a PC running Windows XP.

### B. Ex vivo Porcine Experiments

The VentrAssist™ pump was acutely implanted in six healthy pigs, with the inflow cannula inserted at the apex of the ventricle and the outflow cannula anastomosed to the ascending aorta. The pigs were instrumented with indwelling catheters and pressure transducers to record the pressures (left ventricular pressure, Piv; left atrial pressure, Pia; aortic pressure, Pao; and pump inlet pressure, Pin), as well as with ultrasonic flow probes to record the flow rates (aortic flow rate, Qav; and pump flow rate, Qp). In addition to these physiological signals, instantaneous pump impeller speed \((\omega)\) , motor current \((I)\) and supply voltage \((V)\) were also monitored and recorded from the pump controller. All signals were sampled at \(200\mathrm{Hz}\) . In each experiment, the impeller speed set point was increased from \(1050\mathrm{rpm}\) to \(3000\mathrm{rpm}\) in varying increments in order to cover the full range of pumping state transitions (from regurgitant pump flow to partial collapse of the ventricular wall). For a more detailed description of the experimental procedure, see [11].

## III. RESULTS

Fig. 2 shows the waveforms obtained from a typical ex vivo porcine experiment. Four pump speed set points are illustrated, resulting in four physiologically significant pumping states, i.e., regurgitant pump flow (PR), ventricular ejection (VE), nonopening of the aortic valve over the whole cardiac cycle (ANO), and collapse of the ventricle wall (VC) [10]. Regurgitant pump flow occurs during diastole when the differential pressure generated by the pump is less than the pressure difference between the aorta and the left ventricle. This normally occurs at low pump speed. Transition from state PR to state VE occurs with increasing pump speed. State VE is where left ventricular ejection occurs during systole and pump flow is positive throughout the whole cardiac cycle. Further increase of the pump speed set point leads to state ANO, where the aortic valve remains closed (zero aortic flow). In this state, the maximum left ventricular pressure is less than the aortic pressure and thus unable to open the valve. It is also observed over these three states that the pulsatility of the left ventricular pressure, aortic pressure, pump flow, speed and current decreases with increasing speed. At relatively high pump speeds, state VC occurs. It can be observed that pump flow falls rapidly during end- systole due to the obstruction of the pump inlet cannula caused by the partial collapse of the ventricle walls.

Fig. 3 shows the simulated waveforms from the combined CVS-iRBP model, corresponding to those shown in Fig. 2. It is evident that the model is able to

faithfully reproduce, in at least a qualitative sense, the key features of the four physiologically significant pumping states described above.

## IV. DISCUSSION

The model described above is formulated so as to balance the tradeoff between fidelity and simplicity, with the aim of providing insight into the dynamics of heartpump interaction. For the most part, the model output is seen to simulate the experimental data reasonably well. One notable exception is the simulated aortic pressure (Pao) illustrated in Fig. 3. The experimental data in Fig. 2 reveals a relative constant mean aortic pressure with increasing pump speed set point. In contrast, the simulation results in Fig. 3 show a progressive increase in aortic pressure with increasing speed. The discrepancy may be attributed, in part, to regulation of arterial pressure by the baroreceptor reflex, which is not included in the present model formulation. Therefore, baroreceptor control of the arterial pressure is deemed essential to properly simulate the heart- pump interaction. Furthermore, quantitative differences in the actual pressures or flow rates observed experimentally and those observed in the model may reflect the fact that parameter values used in the model have been tuned to model the human cardiovascular system.

Various heart- pump interaction models have been described in the literature [3], [12]- [15]. However, none of these models include direct ventricular interaction, which is crucial in studying the effect of left ventricular assist device on the right heart. Reesink et al. suggested that insensitive left ventricular support could lead to right- sided circulatory failure [16]. The present model includes left and right ventricular interaction mechanism through the septum and pericardium. However, due to the limited amount of clinical data, the effect of the direct ventricular interaction onto the ventricular function and hemodynamics is not properly validated yet and therefore not included in this paper.

The pump model described above was developed based on experimental data collected under steady flow conditions, with the inclusion of inertia terms to account for the pump dynamics. Preliminary results obtained in our laboratory using a pulsatile mock circulatory loop suggests that the steady flow pump model described above also performs well in the pulsatile flow condition, however, further validation and refinement of the pump model under pulsatile flow conditions is required.

## V. CONCLUSION

The lumped parameter model of interaction between the healthy cardiovascular system and an iRBP has been presented and shown to faithfully reproduce physiologically significant pumping states. This model represents an initial step in the development of a detailed and accurate model of the assisted circulation. Future work involves adapting and validating the model to simulate various types of heart failure, as well as being able to represent the response to postural changes and exercise.

## VI. ACKNOWLEDGMENT

The authors thank Tim Shadie of Ventracor Ltd., for assistance in the development of the pump model.

## REFERENCES

[1] H. Hoshi, T. Shinshi, and S. Takatani, "Third- generation blood pumps with mechanical noncontact magnetic bearings," Artif Organs, vol. 30, pp. 324- 38, 2006.  
[2] W. A. Smith, M. Goodwin, M. Fu, and L. Xu, System analysis of the flow/pressure response of rotydomanic blood pumps. Artificial Organs, vol. 23, pp. 947- 955, 1999.  
[3] M. Volkron, H. Schima, L. Huber, and G. Wieseltalher, "Interaction of the cardiovascular system with an implanted rotary assist device: simulation study with a refined computer model," Artificial Organs, vol. 30, pp. 349- 359, 2002.  
[4] I. G. Blaxland, "The effect of CPAP on the pulsatile dynamics of the heart," Master's thesis, University of New South Wales, 2005.  
[5] W. L. Maughan, K. Sunagawa, and K. Sagawa, "Ventricular systolic interdependence: Volume elastance model in isolated canine hearts," Am. J. Physiol., vol. 253, pp. H1381- H1390, 1987.  
[6] D. S. Esmore, D. Kaye, R. F. Salamonsen, M. Buckland, M. Rowland, J. Negri, Y. Rowley, J. C. Woodard, J. R. Begg, P. J. Ayre, and F. L. Rosenfeld, "First clinical implant of the VentrAssist left ventricular assist system as destination therapy for end- stage heart failure," J Heart Lung Transplant, vol. 24, pp. 1150- 1154, 2005.  
[7] P. A. Watterson, J. C. Woodard, V. S. Ramsden, and J. A. Reizes, "VentrAssist hydrodynamically suspended, open, centrifugal blood pump," Artificial Organs, vol. 24, pp. 475- 477, 2000.  
[8] H. Schima, J. Honigschmabel, W. Trubel, and H. Thoma, "Computer simulation of the circulatory system during support with a rotary blood pump," Trans Am Soc Artif Intern Org, vol. 36, pp. M252- M254, 1990.  
[9] P. A. Watterson, "Analysis of six- step 120 conduction permanent magnet motor drives," Australasian Universities Power Engineering Conference, pp. 13- 18, 1997.  
[10] R. W. Fox, and A. T. McDonald, "Introduction to fluid mechanics", 6th ed., New York: John Wiley and Sons, pp. 273- 300, 2004.  
[11] D. M. Karantonis, N. H. Lovell, P. J. Ayre, D. G. Mason, and S. L. Cloherty, "Identification and classification of physiologically significant pumping states in an implantable rotary blood pump," Artificial Organs, vol. 30, pp. 671- 679, 2006.  
[12] L. Xu, and M. Fu, "Computer modeling of interactions of an electric motor, circulatory system, and rotary blood pump," ASAIO Journal, pp. 604- 611, 2000.  
[13] A. Ferreira, S. Chen, M. A. Simaan, J. R. Boston, and J. F. Antaki, "A nonlinear state- space model of a combined cardiovascular system and a rotary pump," Proceedings of the 44th IEEE Conference on Decision and Control, pp. 897- 902, 2005.  
[14] S. Choi, "Modeling and control of left ventricular assist system," Ph. D. dissertation, University of Pittsburgh, 1998.  
[15] S. Vanderberghe, P. Segers, B. Meyns, and P. R. Verdonck, "Effect of rotary blood pump failure on left ventricular energetics assessed by mathematical modeling," Artificial Organs, vol. 26, pp. 1032- 1039, 2002.  
[16] K. Reesink, A. Dekker, T. Nagel, H. Blom, C. Soemers, G. Geskes, J. Maessen, and E. Veen, "Physiologic- insensitive left ventricular assist predisposes right- sided circulatory failure: a pilot simulation and validation study," Artificial Organs, vol. 28, pp. 933- 939, 2004.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
