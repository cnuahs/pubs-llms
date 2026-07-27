```
@article{lim2010parameteroptimized,
  title={Parameter-Optimized Model of Cardiovascular–Rotary Blood Pump Interactions},
  author={Emily Lim and Socrates Dokos and Shaun L. Cloherty and Robert F. Salamonsen and David G. Mason and John A. Reizes and Nigel H. Lovell},
  journal={IEEE Transactions on Biomedical Engineering},
  year={2010},
  volume={57},
  pages={254-266},
  doi={10.1109/tbme.2009.2031629},
  url={https://ieeexplore.ieee.org/document/5247098}
}
```

---

# Parameter-Optimized Model of Cardiovascular-Rotary Blood Pump Interactions

Einly Lim, Socrates Dokos, Shaun L. Cloherty, Member, IEEE, Robert F. Salamonsen, David G. Mason, John A. Reizes, and Nigel H. Lovell\*, Senior Member, IEEE

Abstract—A lumped parameter model of human cardiovascular- implantable rotary blood pump (iRBP) interaction has been developed based on experimental data recorded in two healthy pigs with the iRBP in situ. The model includes descriptions of the left and right heart, direct ventricular interaction through the septum and pericardium, the systemic and pulmonary circulations, as well as the iRBP. A subset of parameters was optimized in a least squares sense to faithfully reproduce the experimental measurements (pressures, flows and pump variables). Our fitted model compares favorably with our experimental measurements at a range of pump operating points. Furthermore, we have also suggested the importance of various model features, such as the curvilinearity of the end systolic pressure- volume relationship, the Starling resistance, the suction resistance, the effect of respiration, as well as the influence of the pump inflow and outflow cannulae. Alterations of model parameters were done to investigate the circulatory response to rotary blood pump assistance under heart failure conditions. The present model provides a valuable tool for experiment designs, as well as a platform to aid in the development and evaluation of robust physiological pump control algorithms.

Index Terms—Heart failure, heart- pump interaction model, implantable rotary blood pump (iRBP), ventricular assist devices.

## I. INTRODUCTION

I. INTRODUCTIONMPLANTABLE rotary blood pumps (iRBP) have potential as bridge-to-transplantation and destination therapy devices for end-stage heart failure patients. However, insensitivity of iRBP's to preload, overpumping, or underpumping may endanger implant recipients if pump control is not properly implemented. This is further complicated by the remaining intrinsic ventricular function, which is dependent on residual contractil

Manuscript received February 19, 2009; revised May 12, 2009. First published September 18, 2009; current version published January 20, 2010. Asterisk indicates corresponding author.

E. Lim and S. Dokos are with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, 
N.S.W. 2052, Australia (e-mail: z3179719@student.unsw.edu.au; s.dokos@unsw.edu.au).

S. L. Cloherty is with the Research School of Biology, Australian National University, Canberra, 
A.C.T., Australia (e-mail: shaun.cloherty@anu.edu.au).

R. F. Salamonsen is with the Cardiothoracic Intensive Care, Alfred Hospital, Melbourne, 
Vic., Australia, and also with Monash University, Melbourne, 
Vic. 3800, Australia (e-mail: r.salamonsen@alfred.org.au).

D. G. Mason is with the School of Information Technology and Electrical Engineering, University of Queensland, Brisbane, Qld., Australia (e-mail: mason@itee.uq.edu.au).

J. A. Reizes is with the School of Mechanical and Manufacturing Engineering, University of New South Wales, Sydney, 
N.S.W. 2052, Australia, and also with the Faculty of Engineering, University of Technology Sydney, Sydney, 
N.S.W. 2000, Australia.

\(^{*}\) N. H. Lovell is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, 
N.S.W. 2052, Australia (e-mail: n.lovell@unsw.edu.au).

Digital Object Identifier 10.1109/TBME.2009.2031629

ity and venous return, causing the pump differential pressure (head) to vary with each heart beat.

Interaction between iRBP and the cardiovascular system (CVS) may be partially explored through in vivo animal studies. However, such studies are inconclusive at present due to limitations in animal models of heart failure and complexity of the experimental procedures [1]. Numerical models, able to simulate the response of the human CVS in the presence of an iRBP, can provide additional insights into the dynamics of the assisted circulation. Such models also offer an excellent platform for the development and evaluation of robust physiological pump control algorithms by easily allowing reproducible numerical experiments under identical conditions.

Various heart- pump interaction computational models have been described in the literature, with varying degrees of complexity depending on their purpose [1]–[3]. However, previous work has not focused on fitting the entire waveforms (the mean and complete dynamics of the waveforms) to actual experimental measurements and examining the dynamics of the responses during various pumping state transitions in a quantitative sense. This is despite the fact that dangerous pump operating conditions, including suction/ventricular collapse and back flow are closely related to the transient dynamics rather than mean hemodynamic values [4]. In recent experiments, a number of commonly accepted phenomena have been challenged. These include the insufficiency of the widely used time- varying elastance theory [5], the question of the interpretability of the well- established end systolic pressure- volume relationship (ESPVR) under left ventricular (LV) assist device (LVAD) assist [6], and the significant increase of mean aortic pressure with progressive LVAD unloading [7].

The aim of the present study is to develop a heart- pump interaction model, taking into careful consideration various discrepancies between experimental findings and model simulation results. A number of important features, including curvilinearity of the ESPVR, the Starling resistance, respiration effect, and suction and pump cannulae have been included and tested for their significance. Our model is validated using data collected from in vivo animal experiments, mock- loop experiments as well as other published data.

## II. METHODS

### A. Animal Experiments

The VentrAssist iRBP (Ventracor Ltd., Sydney, Australia) was acutely implanted in two healthy, anaesthetized, open- chest pigs supported by mechanical ventilation. The inflow cannula

> **Image description.** A complex technical schematic diagram illustrating the electrical equivalent circuit analogue of a heart-pump interaction model. The diagram uses standard electrical circuit symbols (resistors, inductors, capacitors, and diodes) to represent physiological components of the cardiovascular system (CVS) and a Left Ventricular Assist Device (LVAD).
>
> The diagram is organized horizontally, showing the flow of pressure and flow from left to right, connecting the systemic circulation to the pump and then to the pulmonary circuit.
>
> **Central Pump Model:**
> At the center of the diagram is a dashed box labeled "Pump model." This box contains three differential equations that define the pump's dynamic behavior:
> *   $\Delta P_{pump} = f_1(Q_p, \omega)$
> *   $\frac{d\omega}{dt} = f_2(I, \omega)$
> *   $\frac{dI}{dt} = f_3(V, \omega)$
>
> **Left Side (Systemic Circulation/CVS):**
> The left side of the circuit represents the systemic circulation leading into the pump. Components are arranged in series, representing different vascular beds:
> *   The circuit begins with $L_{out}$ (outflow inertance) and $R_{out}$ (outflow resistance).
> *   $P_{ao}$ (aortic pressure) is shown.
> *   The flow passes through sections labeled $R_{ao}$, $L_{ao}$, and $E_{ao}$ (representing the aorta).
> *   This continues through $R_{sa}$, $L_{sa}$, and $E_{sa}$ (systemic arteries).
> *   The flow then moves through $R_{sv}$, $L_{sv}$, and $E_{sv}$ (systemic veins).
>
> **Right Side (LVAD/Pulmonary Circuit):**
> The right side of the diagram represents the pump's interaction with the left ventricle and the pulmonary circulation.
> *   The pump model connects to the inlet side, showing $P_{in}$ (pump inlet pressure).
> *   The flow passes through $L_{in}$ (inlet inertance) and $R_{in}$ (inlet resistance).
> *   $P_{lv}$ (left ventricle pressure) is shown.
> *   The left ventricle is represented by $R_{lv}$, $L_{lv}$, and $E_{lv}$.
> *   The circuit continues through $R_{pa}$, $L_{pa}$, and $E_{pa}$ (pulmonary arteries).
> *   Finally, the flow passes through $R_{pu}$, $L_{pu}$, and $E_{pu}$ (pulmonary veins) before exiting as $Q_{out}$ (output flow) and encountering $R_{ax}$ (aortic resistance).
>
> **Pressure and Boundary Conditions:**
> Two pressure points, $P_{thor1}$ and $P_{thor2}$, are shown at the far left and far right of the circuit, respectively, representing intrathoracic pressures.
>
> **Legend/Labels:**
> The diagram uses standard electrical symbols:
> *   Resistors ($R$) represent resistance.
> *   Inductors ($L$) represent inertance.
> *   Capacitors ($E$) represent elastance (defined in the context as $1/\text{compliance}$).
> *   $P$ denotes pressure, $Q$ denotes flow, $\omega$ denotes angular velocity, $I$ denotes current, and $V$ denotes voltage.

<center>Fig. 1. Electrical equivalent circuit analogue of heart-pump interaction model. \(P\) , pressures; \(R\) , resistances; \(E\) , elastances \((= 1 / \mathrm{compliances})\) ; \(L\) , inertances; \(D\) , diodes; \(M\) , rotary blood pump. The model consists of two main components: (1) the CVS, which is further divided into ten compartments (la, left atrium; Iv, left ventricle, ao, aorta; sa, systemic peripheral vessels, including the arteries and capillaries; sv, systemic veins, including small and large veins; vc, vena cava; ra, right atrium; rv, right ventricle; pa, pulmonary peripheral vessels, including pulmonary arteries and capillaries; pu, pulmonary veins and (2) the LV assist device (LVAD), which includes the rotary blood pump and the cannulae \((R_{\mathrm{in}}\) and \(R_{\mathrm{out}}\) , inlet and outlet cannulae resistances; \(L_{\mathrm{in}}\) and \(L_{\mathrm{out}}\) , inlet and outlet cannulae inertances; \(R_{\mathrm{su c}}\) , suction resistance). The intrathoracic pressure, \(P_{\mathrm{thor1}}\) and \(P_{\mathrm{thor2}}\) were assigned the same values \((-4\mathrm{mmHg})\) during closed-chest simulated conditions. During open chest simulation conditions, \(P_{\mathrm{thor1}} =\) atmospheric pressure \(= 0\) , while \(P_{\mathrm{thor2}} = P_{\mathrm{resp}}\) (defined in the text). </center>

was inserted at the apex of the left ventricle and the outflow cannula anastomosed to the ascending aorta. The pigs were instrumented with indwelling catheters and pressure transducers connected to the S/5 Light Monitor (Datex Ohmeda, Inc.) to record the LV pressure \((P_{\mathrm{LV}})\) , left atrial (LA) pressure \((P_{\mathrm{IA}})\) , aortic pressure \((P_{\mathrm{ao}})\) , vena cava pressure \((P_{\mathrm{vc}})\) , and pump inlet pressure \((P_{\mathrm{in}})\) . \(P_{\mathrm{LV}}\) was measured at the proximal part of the left ventricle (below the mitral valve) while \(P_{\mathrm{in}}\) was measured at the pump inflow cannula (near the inlet of the pump). Ultrasonic flow probes interfaced with a T106 flowmeter (Transonic Systems, Inc.) were used to record flow rate across the aortic valve \((Q_{\mathrm{av}})\) (with the perivascular flow probe placed around the ascending aorta, upstream of the anastomosis) and pump flow rate \((Q_{p})\) . In addition, instantaneous pump impeller speed \((\omega)\) , motor current \((I)\) , and supply voltage \((V)\) were also monitored and recorded from the pump controller. All signals were sampled at \(200\mathrm{Hz}\) . In each experiment, the pump outflow cannula was first occluded to record the baseline hemodynamic variables. The occlusion was then released and the impeller speed set point was increased from \(1050\) to \(3000\mathrm{r / min}\) in varying increments to cover the full range of pumping state transitions (from regurgitant pump flow to partial collapse of the ventricular wall).

### B. Model Description

Our model consists of two main components: the CVS and the LVAD. An electrical equivalent circuit analogue is illustrated in Fig. 1.

1) CVS Component: The lumped parameter CVS component includes ten compartments consisting of the pulmonary and systemic circulations as well as the left and right sides of the heart. These are described shortly.  

a) Heart chambers: Each of the four heart chambers is characterized by an assumed pressure-volume (PV) relationship, which varies from exponential during diastole, to either linear or curvilinear during systole depending on the time-varying elastance function, \(e(t)\) [8]. A linear ESPVR [8] was adopted for the left and right atrium, while the curvilinear relation proposed by Kass et al. [9] was used for the left and right ventricles. The duration of the systolic periods were assumed to vary linearly with heart rate [10]. Detailed description of the heart chamber equations are given in the Appendix.

LV/right ventricular (RV) interaction via the interventricular septum and the pericardium was modeled using the threeelement system described by Maughan et al. [11], and implemented by Smith et al. [12]. Detailed description of the ventricular interaction equations can be found in [12].

Heart valves were modeled using a resistance \(R\) in series with a diode, allowing flow only when the pressure gradient across them was positive

\[Q = \left\{ \begin{array}{ll}\frac{P_1 - P_2}{R}, & P_1 > P_2\\ 0, & P_1\leq 0 \end{array} \right. \quad (1)\]

where \(Q\) is the blood flow through the valve, and \(P_{1}\) and \(P_{2}\) are the upstream and downstream pressures of the valve, respectively.

b) Circulatory model: Our circulatory model consisted of both systemic and pulmonary circulations. The systemic circulation was further divided into the aorta, the systemic peripheral vessels (including arteries and capillaries), the systemic veins (including small and large veins), and the vena cava. Similarly, the pulmonary circulation was divided into the pulmonary peripheral vessels (including pulmonary arteries and capillaries) and the pulmonary veins. The pressure in the \(i\) th compartment \(P_{i}\) depended on the extravascular pressure \(P_{e,i}\) , the volume of the compartment \(V_{i}\) , the elastance of the compartment \(E_{i}\) , and the unstressed volume of the compartment \(V_{0,i}\) , through the linear PV relationship

\[P_{i} = E_{i}(V_{i} - V_{0,i}) + P_{e,i}. \quad (2)\]

In a closed chest situation, the external pressures surrounding the systemic peripheral vessels and systemic veins were assumed to be zero, while those surrounding the aorta, vena cava, the heart chambers, pulmonary peripheral vessels, and pulmonary veins were given by the intrathoracic pressure \((P_{\mathrm{thor}})\) , which may vary between \(- 4\mathrm{mmHg}\) at end expiration to \(- 9\mathrm{mmHg}\) at end inspiration. However, in the present study under open chest condition, the external pressures surrounding the aorta, vena cava, and the heart chambers were assumed to be zero (i.e., atmospheric pressure).

In regards to flow, the inertance effect was included only in the larger vessels in which blood acceleration was significant, i.e., between the aorta (ao) and the systemic peripheral (sa) compartments, as well as between the pulmonary peripheral vessels (pa) and the pulmonary venous (pu) compartments. Rate of change in flow \(\dot{Q}_i\) between these compartments depended on their pressure difference, \(P_{i} - P_{i + 1}\) , the resistance between them \(R_{i}\) , and the fluid inertance \(L_{i}\)

\[\dot{Q}_i = \frac{P_i - P_{i + 1} - R_iQ_i}{L_i} \quad (3)\]

where \(R_{i}\) and \(L_{i}\) values were assumed to be constants.

On the other hand, flows in other compartments \(Q_{i}\) were modeled as

\[Q_{i} = \frac{P_{i} - P_{i + 1}}{R_{i}} \quad (4)\]

where \(R_{i}\) values were assumed to be constant for all compartments except for the easily collapsible vessels, including those in the immediate vicinity of the pulmonary veins \((R_{\mathrm{pa}}\) and \(R_{\mathrm{la}}\) ), which were modeled using the Starling resistance concept adopted from Magosso and Ursino [13]. In these vessels, if the intravascular pressure downstream of the vessel was lower than the corresponding extravascular pressure \(P_{e,i}\) , the resistance \(R_{i}\) , between the upstream pressure \(P_{u,i}\) , and the downstream pressure \(P_{d,i}\) , became a function of this pressure difference

\[R_{i} = \left\{ \begin{array}{ll}R_{n,i}, & P_{d,i}\geq P_{e,i}\\ R_{n,i}\frac{P_{u,i} - P_{d,i}}{P_{u,i} - P_{e,i}}, & P_{d,i}< P_{e,i} \end{array} \right. \quad (5)\]

where the \(R_{n,i}\) 's were constants. The Starling resistance concept is particularly important for the pulmonary circulation, since continuous LVAD pumping potentially reduces the LA pressure or pulmonary venous pressure to below their external pressures.

c) Respiration effect: A respiration effect was observed in both the pressure and flow data of our animal experiments. During positive mechanical ventilation under open chest conditions, the degree of lung inflation (10-15 cmH2O in our experiments) affected the resistance and transmural pressure of the pulmonary vessels surrounding the alveoli [14], leading to respiration induced pressure and flow variations. In order to reproduce this effect, we modeled the external pressures surrounding the pulmonary vessels, \(P_{\mathrm{resp}}\) , as a time-dependent function given by the general form

\[P_{\mathrm{resp}} = a_{\mathrm{resp}}\frac{\sin\left(2\pi t / T_{\mathrm{resp}}\right)}{\sin\left(2\pi t / T_{\mathrm{resp}}\right) + b_{\mathrm{resp}}} + c_{\mathrm{resp}} \quad (6)\]

where \(T_{\mathrm{resp}}\) was the period of the respiration cycle, while \(a_{\mathrm{resp}}\) , \(b_{\mathrm{resp}}\) , and \(c_{\mathrm{resp}}\) were constants.

2) LVAD Component: The VentrAssist iRBP is a centrifugal blood pump having a hydrodynamic bearing. The pump was modeled using three differential equations: the motor windings electrical equation, the electromagnetic torque transfer equation, and the pump hydraulic equation. Models for differential pressure and flow estimation of the iRBP, previously validated against in vitro mock-loop data under both continuous and pulsatile flow conditions [15], [16], were used in the present simulation to represent the pump model. An addition to the previous model is the inclusion of inflow and outflow cannulae, each modeled in terms of flow-dependent resistances, \(R_{\mathrm{in}}\) and \(R_{\mathrm{out}}\) , producing a pressure drop given by

\[R_{\mathrm{in}} + R_{\mathrm{out}} = k_RQ_p \quad (7)\]

where \(k_{R}\) is a constant (see Table I), as well as constant series inductances \(L_{\mathrm{in}}\) and \(L_{\mathrm{out}}\) representing the inertia of blood in the cannulae. The rationale behind the flow-dependent resistance is the calculated Reynolds number \((Re)\) of the fluid flow in the cannulae, which falls in the transition region between laminar \((< 2300)\) and turbulent \((>4000)\) flow. The Reynolds number is defined by

\[Re = \frac{\rho VD}{\mu} \quad (8)\]

where \(\rho\) denotes the blood density, \(V\) denotes the blood velocity, \(D\) denotes the diameter of the pump cannulae, and \(\mu\) denotes the blood viscosity. The calculated Reynolds number in our experimental data is approximately between 2000 and 6000, depending on the value of \(Q_{p}\) .

A third resistance \(R_{\mathrm{suc}}\) was inserted upstream of the inflow cannula to simulate suction events. Collapse of the ventricle was evident from observation of the pump inlet pressure \((P_{\mathrm{in}})\) waveforms, which showed a sharp fall when the ventricular walls suck together (normally near the point of end systole), causing a large pressure difference between \(P_{\mathrm{iv}}\) and \(P_{\mathrm{in}}\) . The model for \(R_{\mathrm{suc}}\) was first proposed by Schima et al. [17] and adopted by several research groups. Under normal operation, \(R_{\mathrm{suc}}\) is set to 0. When the LV pressure is less than a threshold pressure, \(R_{\mathrm{suc}}\) increases proportionally to this pressure difference. Although this model can explain the occurrence of suction relatively well, it has not been able to generate the observed phase difference between \(P_{\mathrm{iv}}\) , \(P_{\mathrm{in}}\) , and \(Q_{p}\) during suction in our experimental data, possibly due to the fact that the present study used LV instead of LA cannulation. One observation from preliminary experiments was that although there is a high variability in terms of the pressure and flow waveforms during suction, ventricular collapse (indirectly indicated by a sharp fall in pump flow and pump inlet pressure) always occurred near the point of end systole, i.e., shortly after LV pressure reached its maximum value in the cardiac cycle. This could not be achieved by Schima's model, which produced an increase in \(R_{\mathrm{suc}}\) at minimum LV pressure. In order to better reproduce this phenomenon, we have modeled the steady-state suction resistance \(R_{\mathrm{suc},\infty}\) as a function of LV volume \((V_{\mathrm{iv}})\) , which reached its minimum value during end systole. Under normal operation, \(R_{\mathrm{suc},\infty}\) is set to 0. When \(V_{\mathrm{iv}}\) fell

TABLEI VALUES OF MODEL PARAMETERS IN HEALTHY CIRCULATION ALONG WITH OPTIMIZED VALUES TO REPRODUCE PIG EXPERIMENTAL DATA

| Parameter | Description | Healthy | Pig 1 | Pig 2 |
| :--- | :--- | :--- | :--- | :--- |
| T (s)* | Heart period | 0.8 | 0.54 | 0.52 |
| Tresp (s)* | Respiration period | - | 3.8 | 3.8 |
| aresp (mmHg)* | Respiration waveform amplitude | - | 0.45 | 0.45 |
| bresp (s)* | Respiration waveform denominator coefficient | - | 1.21 | 1.21 |
| cresp (mmHg)* | Respiration waveform offset term | - | 3 | 3 |
| Vtotal (mL) | Total blood volume | 5300 | 4628 | 4198 |
| kR (mmHg.s2.mL-2) | Cannula resistance flow coefficient | -0.006 | 0.006 | 0.006 |
| cLvf (mmHg-1) | LV end systolic stiffness denominator term | 0.004 | 0.006 | 0.007 |
| Rsa (mmHg.s.mL-1) | Systemic peripheral resistance | 0.74 | 0.38 | 0.48 |
| 11βLvf (mL-1.mmHg-1) | LV end systolic stiffness denominator coefficient | 2.20E-05 | 1.69E-08 | 3.76E-08 |
| Rna,pa (mmHg.s.mL-1) | Pulmonary peripheral resistance | 0.12 | 0.12 | 0.12 |
| V0,Lvf (mL) | LV end diastolic volume at zero pressure | 40.0 | 38.8 | 33.2 |
| V0,rvf (mL) | RV end diastolic volume at zero pressure | 50.0 | 54.7 | 58.1 |
| Esa (mmHg.mL-1) | Systemic arterial elastance | 0.37 | 0.26 | 0.26 |
| Vd,rvf (mL) | RV end diastolic volume at zero pressure | 41.0 | 44.6 | 40.0 |
| Vd,Lvf (mL) | LV end systolic volume at zero pressure | 27.7 | 26.8 | 32.6 |
| αrvf (mmHg-1) | RV end systolic stiffness denominator term | 0.008 | 0.013 | 0.012 |
| P0,rvf (mmHg) | RV end diastolic stiffness scaling term | 0.91 | 0.93 | 0.84 |
| Ra0 (mmHg.s.mL-1) | Aortic resistance | 0.2 | 0.19 | 0.21 |
| P0,Lvf (mmHg) | LV end diastolic stiffness scaling term | 0.98 | 2.03 | 2.03 |
| Ea0 (mmHg.mL-1) | Aortic elastance | 0.82 | 0.05 | 2.05 |
| Evc (mmHg.mL-1) | Vena cava elastance | 0.03 | 0.11 | 0.11 |
| Lf(=Lvin+Lout) (mmHg.s2.mL-1) | Cannula inertance | -0.05 | 0.05 | 0.05 |
| k81 (s.mL-1) | Suction resistance coefficient 1 | -0.5 | 0.5 | - |
| k82 (s.mL-1) | Suction resistance coefficient 2 | - | 1.3 | -1.3 |
| TRsuc (s.mL-1) | Suction resistance time constant | -0.05 | 0.05 | - |
| Ees,lvf (mmHg.mL-1)** | LV end systolic elastance | 3.54 | 3.70 | 3.14 |
| Vd,Lvf (mL)** | LV end systolic volume at zero pressure | 16.77 | 26.00 | 31.55 |
| Ees,rvf (mmHg.mL-1)** | RV end systolic elastance | 1.75 | 0.92 | 1.00 |
| Vd,rvf (mL)** | RV end systolic volume at zero pressure | 40.80 | 38.08 | 33.37 |

\\* These values were either estimated or determined directly from the pig experimental measurements, and not via least-squares optimization. \\*\\* Parameter values of the linearized ESPVR (at \(V_{o} =\) 60 mL). The superscript number before each parameter (e.g., \(V_{\mathrm{max}}^{\prime}\) corresponds to their ranking according to the degree of sensitivity on the objective function.

below a predefined threshold volume \((V_{\mathrm{th}})\) (chosen in this study as \(V_{\mathrm{lv}}\) corresponding to \(P_{\mathrm{levs}} = 5\mathrm{mmHg}\) \(R_{\mathrm{suic},\infty}\) increased exponentially as a function of this volume difference

\[R_{\mathrm{suic},\infty} = \left\{ \begin{array}{ll}k_{\mathrm{s1}}(e^{k_{\mathrm{s2}}(V_{\mathrm{lv}} - V_{\mathrm{th}})}) & V_{\mathrm{lv}}< V_{\mathrm{th}}\\ 0 & V_{\mathrm{lv}}\geq V_{\mathrm{th}} \end{array} \right. \quad (9)\]

where \(k_{\mathrm{s1}}\) and \(k_{\mathrm{s2}}\) are constants. We have also added a time constant term \((\tau_{R_{\mathrm{suic}}})\) to simulate a first- order response on the suction resistance to a change in the volume difference

\[\frac{dR_{\mathrm{suic}}}{dt} = \frac{-R_{\mathrm{suic}} + R_{\mathrm{suic},\infty}}{\tau_{R_{\mathrm{suic}}}}. \quad (10)\]

The overall relationship between \(Q_{p}\) , \(P_{\mathrm{lv}}\) , \(P_{\mathrm{ao}}\) , and the differential pressure across the pump \(\Delta P_{\mathrm{pump}}\) was given by

\[\dot{Q}_p = \frac{\Delta P_{\mathrm{pump}} - (P_{\mathrm{ao}} - P_{\mathrm{lv}}) - (R_{\mathrm{in}} + R_{\mathrm{out}} + R_{\mathrm{suic}})Q_p}{L_{\mathrm{in}} + L_{\mathrm{out}}} \quad (11)\]

where \(\dot{Q}_p\) was the first derivative of \(Q_p\) .

### C. Simulation Protocols

The heart- pump interaction model contained 87 parameters, including 64 parameters for the CVS, 18 parameters for the

iRBP, and five parameters for the pump cannulae. Initial parameter estimates for the CVS were obtained from [10] and [18]. These parameters were then fitted to reproduce pressure, flow, and volume distributions in a healthy human circulation (parameter values are listed in Tables I and II). Resulting- model- simulated key hemodynamic variables are listed in Table III, where the values are seen to agree with published results [19].

The CVS model was then coupled to the LVAD model and selected parameters were tuned to reproduce experimental measurements using weighted least squares optimization. Parameters for the iRBP were obtained from previous in vitro mock- loop experiments described in Section II- B.2.

In order to investigate the efficiency of LVAD assist under heart failure conditions, we have simulated two different biventricular failure scenarios with similar baseline cardiac output. This was achieved by modifying the optimized parameters from pig 1 that characterized the left and RV ESPVR (parameter values listed in Table IV). The first simulated biventricular failure scenario (HF1) has a lower LV contractility compared to the second simulated biventricular failure scenario (HF2). On the contrary, HF2 has a lower RV contractility compared to HF1.

Surplus hemodynamic energy (SHE) was derived from the experimental and simulation results as a means of assessing

TABLE II VALUES OF NONOPTIMIZED MODEL PARAMETERS FOR BOTH HEALTHY HUMAN CIRCULATION AND PIG DATA SIMULATIONS

| Parameter | Description | Value |
| :--- | :--- | :--- |
| Tsys0 (s) | Maximum systolic heart period | 0.5 |
| ksys (s2) | Systolic heart period-inverse heart period slope | 0.075 |
| kr,v (-) | Proportion of ventricular systolic time to reach maximal contraction | 0.5 |
| kr,a (-) | Proportion of atrial systolic time to reach maximal contraction | 0.5 |
| P0,pcd (mmHg)* | Pericardial end diastolic stiffness scaling term | 0.52 |
| V0,sv (mL) | Systemic vein unstressed volume | 1976.103 |
| V0,ao (mL) | Aortic unstressed volume | 201.754 |
| Esv (mmHg.mL-1) | Systemic vein elastance | 0.0135 |
| V0,vc (mL) | Vena cava unstressed volume | 136.176 |
| Rn,sv (mmHg.s.mL-1) | Systemic vein resistance | 0.127 |
| V0,sa (mL) | Systemic arterial unstressed volume | 231.0418 |
| V0,pu (mL) | Pulmonary veins unstressed volume | 132.3921 |
| V0,pa (mL) | Pulmonary arterial unstressed volume | 91.6726 |
| Rmt (mmHg.s.mL-1) | Mitral valve resistance | 0.0127 |
| βrv,f (mL-1.mmHg-1) | RV end systolic stiffness denominator coefficient | 0.00004828 |
| Rn,ra (mmHg.s.mL-1) | Vena cava resistance | 0.01229 |
| λtuf (mL-1) | LV end diastolic stiffness coefficient | 0.02830 |
| Epu (mmHg.mL-1) | Pulmonary vein elastance | 0.0431 |
| λrv,f (mL-1) | RV end diastolic stiffness coefficient | 0.02832 |
| Epα (mmHg.mL-1) | Pulmonary arterial elastance | 0.1533 |
| Rtc (mmHg.s.mL-1) | Tricuspid valve resistance | 0.0134 |
| Ees,ra (mmHg.mL-1) | RA end systolic elastance | 0.2035 |
| λla (mL-1) | LA end diastolic stiffness coefficient | 0.025 |
| Ees,la (mmHg.mL-1) | LA end systolic elastance | 0.203 |
| Ra0 (mmHg.s.mL-1) | Aortic valve resistance | 0.025 |
| V0,ra (mL) | RA end diastolic volume at zero pressure | 203 |
| Rn,la (mmHg.s.mL-1) | Pulmonary vein resistance | 0.00640 |
| P0,la (mmHg) | LA end diastolic stiffness scaling term | 0.50 |
| Lao (mmHg.s2.mL-1) | aortic inertance | 0.002242 |
| Vd,la (mL) | LA end systolic volume at zero pressure | 1043 |
| λra (mL-1) | RA end diastolic stiffness coefficient | 0.025 |
| P0,ra (mmHg) | RA end diastolic stiffness scaling term | 0.50 |
| V0,pcd (mL) | Pericardial end diastolic volume at zero pressure | 200 |
| V0,la (mL) | LA end diastolic volume at zero pressure | 2048 |
| V0,spt (mL) | Septal end diastolic volume at zero pressure | 849 |
| Vd,spt (mL) | Septal end systolic volume at zero pressure | 850 |
| Vd,ra (mL) | RA end systolic volume at zero pressure | 105 |
| Ees,spt (mmHg.mL-1) | Septal end systolic elastance | 19.55 |
| Rpv (mmHg.s.mL-1) | Pulmonary valve resistance | 0.025 |
| λpcd (mL-1) | Pericardial end diastolic stiffness coefficient | 0.005 |
| Lpa (mmHg.s2.mL-1) | Pulmonary arterial inertance | 0.00185 |
| λspt (mL-1) | Septal end diastolic stiffness coefficient | 0.175 |
| P0,spt (mmHg) | Septal end diastolic stiffness scaling term | 0.46 |

\((\mathrm{P}_{0,\mathrm{pd}}\) is set to 0.01 mmHg in the pig model simulations to remove the pericardium effects under open chest condition. The superscripted number before each parameter (e.g., \(\overline{V}_{0,\mathrm{os}}\) ) corresponds to their ranking according to the degree of sensitivity on the objective function.

pulsatility [20], and it was defined as

SHE (in erg per milliliter)

\[= 1332\left(\frac{\int(Q_{p} + Q_{\mathrm{av}})P_{\mathrm{ao}}dt}{\int(Q_{p} + Q_{\mathrm{av}})dt} -\overline{P_{\mathrm{ao}}}\right). \quad (12)\]

On the other hand, pulmonary vascular resistance (PVR) (in millimeters of mercury- second per milliliter) was derived from the simulation results, as follows:

\[\mathrm{PVR} = \frac{\overline{P_{\mathrm{pa}}} - \overline{P_{\mathrm{la}}}}{\overline{Q_{\mathrm{pa}}}} \quad (13)\]

where \(\overline{P_{\mathrm{pa}}}\) denotes the mean pulmonary arterial pressure, \(\overline{P_{\mathrm{la}}}\) denotes the mean LA pressure, while \(Q_{\mathrm{pa}}\) denotes the mean pulmonary blood flow.

The complete model was implemented in MATLAB (The Mathworks, Inc., Natick, MA) using its inbuilt ordinary differential equation (ODE) solver suite. The algorithm was run on a PC running Windows XP.

### D. Parameter Estimation

Least squares- parameter- estimation methods were utilized to fit the parameters for the CVS and the pump cannulae in order to achieve better agreement with the experimental data. Due to

TABLE III MODEL-SIMULATED HEMODYNAMIC DATA FOR HEALTHY SUBJECT: LV PEAK SYSTEMIC AND END DIAGSTOLIC PRESSURES, \(P_{1\mathrm{Ves}}\) AND \(P_{1\mathrm{Vcd}}\) ; PEAK SYSTEMIC AND END DIAGSTOLIC AORTIC PRESSURES, \(P_{\mathrm{asres}}\) AND \(P_{\mathrm{ascd}}\) ; MEAN AORTIC PRESSURE \(\overline{P_{\mathrm{asd}}}\) ; RV PEAK SYSTEMIC AND END DIAGSTOLIC PRESSURES, \(P_{\mathrm{res}}\) AND \(P_{\mathrm{revd}}\) ; PERCENTAGE VOLUME IN SYSTEMIC AND PULMONARY CIRCULATION; LV END SYSTEMIC AND END DIAGSTOLIC VOLUMES, \(V_{\mathrm{1ves}}\) AND \(V_{\mathrm{1vcd}}\) ; STROKE VOLUME SV; AND MEAN CARDIAC OUTPUT, \(\overline{\mathrm{CO}}\) (REFERENCE VALUES FOR HEALTHY SUBJECT WERE TAKEN FROM [19])

| Variable | Healthy | Reference [19] |
| :--- | :--- | :--- |
| $P_{1\mathrm{ves}}$ (mmHg) | 123.3 | 130 |
| $P_{1\mathrm{vcd}}$ (mmHg) | 6.5 | 10 |
| $P_{\mathrm{aoes}}$ (mmHg) | 119.4 | 130 |
| $P_{\mathrm{aoed}}$ (mmHg) | 78.9 | 80 |
| $P_{\mathrm{ao}}$ (mmHg) | 97.8 | 95 |
| $P_{\mathrm{res}}$ (mmHg) | 35 | 30 |
| $P_{\mathrm{revd}}$ (mmHg) | 5.2 | 6 |
| % volume in the systemic circulation | 82.3 | 84 |
| % volume in the pulmonary circulation | 9.6 | 8.8 |
| $V_{1\mathrm{vcd}}$ (mL) | 127.2 | 120 |
| $V_{1\mathrm{ves}}$ (mL) | 57.8 | 50 |
| SV (mL) | 69.4 | 70 |
| CO (L.min$^{-1}$) | 5.2 | 5 |

the limited availability of measurements from the animal experiments as well as restrictions imposed by the model structure, all 87 model parameters could not be uniquely determined. Thus, we reduced the number of parameters to be estimated by first determining their relative effects on a weighted least squares objective function given by

\[F = \Sigma_{i}w_{i}(\mathbf{y}_{\mathrm{model},i}(\theta) - \mathbf{y}_{\mathrm{meas},i})^{2} \quad (14)\]

where \(w_{i}\) denotes the weight corresponding to the \(i\) th experimental dataset, including \(P_{1\mathrm{v}}\) \(P_{1\mathrm{a}}\) \(P_{\mathrm{ao}}\) \(P_{\mathrm{vc}}\) \(Q_{\mathrm{av}}\) \(Q_{p}\) \(\omega\) ,and \(I\) .Term \(w_{i}\) was determined so that each experimental dataset initially contributed equally to the least- squares objective, \(\theta\) represents model parameters, \(y_{\mathrm{model},i}\) denotes the \(i\) th model output, while \(y_{\mathrm{meas},i}\) denotes the \(i\) th experimental measurement corresponding to the \(i\) th model output. Each parameter \(\theta_{j}\) was perturbed from its baseline value by \(5\%\) , one at a time, and the change in the corresponding objective function was calculated. The dimensionless parameter sensitivity coefficient \(S_{j}\) was evaluated using

\[S_{j} = \frac{\theta_{j}}{F_{0}}\frac{\Delta F}{\Delta\theta_{j}} \quad (15)\]

where \(F_{0}\) is initial nominal value of the objective function corresponding to default model parameters.

The sensitivity analysis revealed that the 25 most sensitive parameters (i.e., those having the highest \(S_{j}\) values) include the total blood volume as well as the unstressed volumes in the circulation \([V_{\mathrm{total}}]\) and \(V_{0}\) 's], the systemic veins, systemic peripheral vessels, aortic and vena cava elastances \((E_{\mathrm{sv}}\) \(E_{\mathrm{sa}}\) \(E_{\mathrm{ao}}\) , and \(E_{\mathrm{vc}}\) ), the systemic veins, systemic peripheral vessels, pulmonary peripheral, and aortic resistance \((R_{\mathrm{sv}}\) \(R_{\mathrm{sa}}\) \(R_{\mathrm{pa}}\) and \(R_{\mathrm{ao}}\) ), the cannula resistance flow coefficient \((k_{R})\) , the parameters, which describe the contractility of the left and right ventricles \((\alpha_{\mathrm{1vcf}}\) \(\beta_{\mathrm{1vcf}}\) , and \(\alpha_{\mathrm{rvf}}\) ), LV and RV end diastolic volumes at zero pressure \((V_{0,\mathrm{1vf}}\) and \(V_{0,\mathrm{rvf}}\) ), LV and RV end systolic volumes at zero pressure \((V_{d,\mathrm{1vf}}\) and \(V_{d,\mathrm{rvf}}\) ), and the LV and RV end diastolic stiffness scaling term \((P_{0,\mathrm{1vf}}\) and \(P_{0,\mathrm{rvf}}\) ). Based on

this analysis, 19 out of the 25 most sensitive parameters were included in the nonlinear least squares- parameter- estimation algorithm (the simplex search method [21]), starting at initially estimated values described in Section II- C. Some of the parameters, including \(V_{0}\) 's, \(E_{\mathrm{sv}}\) , and \(R_{\mathrm{sv}}\) , were not chosen to be optimized due to their obvious dependencies with \(V_{\mathrm{total}}\) with respect to their effect on the eight measurements used in the fitting process.

All the eight waveform measurements from two speed settings (1960 and 2360 r/min for pig 1; 1760 and 2160 r/min for pig 2) in each of the two pig experiments (with 10- s segments sampled at \(200\mathrm{Hz}\) extracted for each speed setting) were used in the optimization process to search for parameter values that minimized the objective function. Data from other speed settings (1760 and 2160 r/min for pig 1; 1460 and 1960 r/min for pig 2) as well as pump occlusion data were used to test the predictability of the model in describing data that were not used in the fitting process. A constant heart rate, estimated from the measurement of ECG during the experiments, was used to run the model. The other known input to the model that was varied during each speed variation is the measured pulswidth- modulated voltage (PWM) to the pump. Values for the optimized parameters for each pig (listed according to their degree of sensitivity) are given in Table I.

## III. RESULTS

Fig. 2 shows waveforms of one of the pig experiments (pig 1) superimposed on the model simulation using the optimized parameters for that pig. Pump occlusion and four pump speed settings are shown, corresponding to two cardiac pumping states: ventricular ejection (VE), i.e., when \(Q_{\mathrm{av}} > 0\) (mean pump speeds, \(\overline{\omega}\) of 1760, 1960, and 2160 r/min) and nonopening of the aortic valve over the whole cardiac cycle (ANO), i.e., when \(Q_{\mathrm{av}} = 0\) (mean pump speed of 2360 r/min). From the results shown in Fig. 2, there is a high degree of correlation between model and experimental data, including pressure, flow, and pump waveforms, both in terms of mean values and response dynamics. Table V shows the rms value of the error between the experimental data and the simulation results for both pigs, before and after optimization. It was shown that the modelling process produced a much better agreement in all variables between the experimental measurements and the model simulations (with an error of less than \(10\%\) , except for \(P_{\mathrm{la}}\) and \(P_{\mathrm{vc}}\) , which has an error of less than \(20\%\) ). The model was not able to accurately reproduced the corresponding dynamics in these two measurements, as the waveforms were corrupted by relatively higher levels of measurement noise, partly due to their lower absolute values. To illustrate the trend of hemodynamic and pump waveforms with increasing mean pump speed in both pig experiments, mean values of key variables from the experiments and/or model are plotted in Figs. 3 and 4. The range of pump speeds included both VE and ANO states. Both model simulation and experimental data showed a nonlinear decrease in LV end diastolic pressure \((P_{\mathrm{1vcd}})\) with increasing pump speed, with the least decrease during state VE and the greatest decrease during state ANO. The pump speed where significant LV end diastolic pressure reduction began to occur corresponded to that

TABLE IV VALUES OF MODEL PARAMETERS IN HEART FAILURE CONDITIONS

| Parameter | Description | Pig 1 | HF1 | HF2 |
| :--- | :--- | :--- | :--- | :--- |
| $\alpha_{\text{LVf}}$ ($\text{mmHg}^{-1}$) | LV end systolic stiffness denominator term | 0.0067 | 0.0147 | 0.0068 |
| $\beta_{\text{LVf}}$ ($\text{mL}^{-1}\text{mmHg}^{-1}$) | LV end systolic stiffness denominator coefficient | 1.69E-08 | 1.44E-07 | 1.30E-08 |
| $V_{\text{d,LVf}}$ (mL) | LV end systolic volume at zero pressure | 26.8 | 65.0 | 61.9 |
| $\alpha_{\text{RVf}}$ ($\text{mmHg}^{-1}$) | RV end systolic stiffness denominator term | 0.0130 | 0.0178 | 0.0377 |
| $\beta_{\text{RVf}}$ ($\text{mL}^{-1}\text{mmHg}^{-1}$) | RV end systolic stiffness denominator coefficient | 4.80E-05 | 2.07E-06 | 3.49E-8 |
| $V_{\text{d,RVf}}$ (mL) | RV end systolic volume at zero pressure | 44.6 | 57.0 | 64.0 |

> **Image description.** A multi-panel time-series line graph, Figure 2, which compares experimental measurements with model simulations of hemodynamic variables in a pig experiment. The graph is composed of four stacked subplots, all sharing a common horizontal time axis ranging from 0 to 1 second.
>
> The data is organized into four distinct panels, each representing a different physiological variable, and is segmented into four sections corresponding to four different pump speed settings ($\omega$): 1760 r/min, 1960 r/min, 2160 r/min, and 2360 r/min.
>
> The legend indicates that the solid black line represents the "Measurement" (experimental data), while the dashed black line represents the "Simulation" (model data).
>
> The four panels are labeled as follows:
> 1.  **Top Panel ($P_{\mathrm{LV}}$):** Displays Left Ventricular (LV) pressure in mmHg. The waveforms show a clear pulsatile pattern, with the measured and simulated pressures tracking each other closely across all four pump speeds.
> 2.  **Second Panel ($P_{\mathrm{ao}}$):** Displays aortic pressure in mmHg. Similar to the LV pressure, the solid and dashed lines exhibit highly correlated pulsatile waveforms.
> 3.  **Third Panel ($Q_{\mathrm{p}}$):** Displays pump flow in L/min. This panel shows sharp, pulsatile flow waveforms, indicating the operation of the rotary blood pump.
> 4.  **Bottom Panel ($Q_{\mathrm{av}}$):** Displays aortic valve flow in L/min. This panel also shows pulsatile flow patterns, representing the flow through the aortic valve.
>
> Overall, the visual evidence demonstrates a high degree of agreement between the experimental measurements and the model simulations for all four hemodynamic parameters across the tested range of pump speeds. The text at the top of the graph specifies the pump occlusion condition and the four corresponding rotational speeds ($\omega$).

<center>Fig. 2. Waveforms from an in vivo pig experiment (pig 1) implanted with rotary blood pump superimposed on model simulations with the rotary blood pump activated at pump occlusion and at four pump speed settings from left to right corresponding to 1760, 1960, 2160, and 2360 r/min. During pump occlusion, pump outflow cannula was occluded to record the baseline hemodynamic variables. This was reproduced in the model simulation by setting pump flow to zero. From top: LV pressure, \(P_{\mathrm{LV}}\) ; aortic pressure, \(P_{\mathrm{ao}}\) ; pump flow, \(Q_{\mathrm{p}}\) ; aortic valve flow, \(Q_{\mathrm{av}}\) . </center>  

when the PVR started to increase (see Fig. 4). On the other hand, LV peak systolic pressure \((P_{\mathrm{IVes}})\) remained relatively constant during state VE, but decreased significantly during state ANO. Mean aortic pressure \(\left(\overline{P_{\mathrm{no}}}\right)\) showed a very slight increase with increasing pump speed for both model and experiments, while mean central venous pressure \(\left(\overline{P_{\mathrm{vc}}}\right)\) was not significantly changed by pump speed. In terms of blood flow, both model simulation and experimental results showed a bilinear relationship between mean pump flow \(\left(\overline{Q_{\mathrm{p}}}\right)\) and pump speed, with higher increases during state VE compared with state ANO. Total mean cardiac output \(\overline{\mathrm{CO}}\) remained relatively constant in the experiments but increased slightly with increasing pump speed in the model. The increase in mean pump flow with pump speed is counteracted by the decrease in mean aortic valve flow \(\left(\overline{Q_{\mathrm{av}}}\right)\) caused by the decrease in LV preload. In terms of pulsatility, both experiments and model showed a nonlinear decrease in pulsatility with increasing pump speed, as indicated by the values of SHE (see Fig. 3). Simulated LV end diastolic volume \(\left(V_{\mathrm{IVed}}\right)\) and end systolic volume \(\left(V_{\mathrm{IVes}}\right)\) decreased with increasing pump speed, with a greater decrease for the end diastolic volume, leading to a decrease in stroke volume (SV) (see Fig. 4). To examine how well the model reproduced the effect of LV suction at excessive pump speeds, LV pressure \(\left(P_{\mathrm{IV}}\right)\) , pump inlet pressure \(\left(P_{\mathrm{in}}\right)\) , and pump flow \(\left(Q_{\mathrm{p}}\right)\) are plotted in Fig. 5. It can be seen that suction occurs intermittently over a fraction of the respiratory cycle. Partial collapse of the LV walls occurred when \(V_{\mathrm{IV}} < V_{\mathrm{th}}\) , creating a large resistance between the left ventricle and the pump inlet. As a result, pump flow and pump inlet pressure started to fall significantly at end systolic when the LV volume reached its minimum value. Model simulation showed an increase in the values of \(R_{\mathrm{pa}}\) , \(R_{\mathrm{la}}\) , and \(R_{\mathrm{suic}}\) during suction, with \(R_{\mathrm{pa}}\) increased by a factor of 1.9, \(R_{\mathrm{la}}\) by a factor of 3.9, while \(R_{\mathrm{suic}}\) increased from 0 to 1 mmHg·s/mL. The much higher increase in the resistance at the ventricle compared to the pulmonary vessels during suction was most probably due to the lower intravascular pressure (downstream) at the ventricle and the difference in the mechanical structure between the ventricle and the vessels (where the ventricle is a single chamber while the vessels are made up of many branches at various locations that may or may not collapse at the same time).

Table VI shows the effect of heart failure and pump speed on the circulatory system and pump variables. Compared to the healthy condition, baseline mean aortic pressure \(\left(\overline{P_{\mathrm{ao}}}\right)\) and mean cardiac output \(\overline{\mathrm{CO}}\) in both heart failure scenarios decreased, while mean LA pressure \(\left(\overline{P_{\mathrm{la}}}\right)\) , mean vena cava pressure \(\left(\overline{P_{\mathrm{vc}}}\right)\) , LV end diastolic volume \(\left(V_{\mathrm{IVed}}\right)\) , and RV end diastolic volume \(\left(V_{\mathrm{IVed}}\right)\) increased. Due to the more severe LV failing condition, HF1 demonstrated a more significant increase in \(V_{\mathrm{IVed}}\) and \(\overline{P_{\mathrm{la}}}\) compared to HF2. On the contrary, HF2 showed a more significant increase in \(V_{\mathrm{IVed}}\) and \(\overline{P_{\mathrm{vc}}}\) due to the more severe RV failing condition. Increasing pump speed shifted the blood volume in the pulmonary circulation \(\left(\overline{V_{\mathrm{pul}}}\right)\) into the systemic circulation \(\left(\overline{V_{\mathrm{sys}}}\right)\) , thus reducing \(\overline{P_{\mathrm{la}}}\) while increasing \(\overline{P_{\mathrm{vc}}}\) . In regards to blood flow, \(\overline{\mathrm{CO}}\) increased \(84\%\) in HF1 and \(52\%\) in HF2 from the same baseline value under LVAD assistance. On the other hand, pump flow pulsatility \(\left(Q_{\mathrm{p,pp}}\right)\) decreased in both heart failure scenarios and with increasing pump speeds. Compared to the healthy heart that continuously ejects blood out of the ventricle in the presence of an LVAD, blood flow to the circulation in both heart failure conditions was completely supported by the rotary pump, even at the lowest simulated pump speeds.

## IV. DISCUSSION

### A. Comparison With Experimental Observations

The model developed in this study reproduces the experimental data well, both in terms of mean values and steady- state

TABLE V RMS VALUE OF THE ERROR BETWEEN EXPERIMENTAL DATA AND SIMULATION RESULTS, BEFORE AND AFTER OPTIMIZATION

| Measurements | Range | rms error (before) | | rms error (after) | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | Pig 1 | Pig 2 | Pig 1 | Pig 2 |
| P1v (mmHg) | -3.15 – 98.06 | 32.34 | 41.01 | 9.82 | 9.46 |
| P1a (mmHg) | -2.56 – 16.26 | 3.43 | 3.80 | 3.34 | 3.50 |
| P1a0 (mmHg) | 35.16 – 95.08 | 46.29 | 47.09 | 3.68 | 3.61 |
| P1v (mmHg) | 0.49 – 6.76 | 1.33 | 2.56 | 1.29 | 0.93 |
| Qp (L.min-1) | 0.12 – 6.88 | 3.43 | 3.78 | 0.33 | 0.31 |
| Qav (L.min-1) | -3.78 – 25.44 | 10.83 | 12.67 | 1.97 | 2.16 |
| ω (rpm) | 1413.10 – 2382.50 | 121.37 | 203.42 | 13.37 | 17.34 |
| I (A) | 0.19 – 0.74 | 0.05 | 0.09 | 0.01 | 0.02 |

> **Image description.** A multi-panel line graph, labeled "Fig. 3," illustrating the effect of increasing mean pump speed ($\omega$) on several hemodynamic parameters. The graph consists of five stacked subplots, all sharing a common horizontal X-axis representing the mean pump speed ($\omega$) in revolutions per minute (rpm), ranging from 1400 to 2500.
>
> The legend at the top identifies four data series:
> *   Pig 1 (exp): Represented by black circles.
> *   Pig 1 (mod): Represented by black squares.
> *   Pig 2 (exp): Represented by black triangles.
> *   Pig 2 (mod): Represented by black inverted triangles.
>
> The five panels, from top to bottom, display the following variables:
>
> 1.  **Top Panel ($P_{1vcl}$):** This panel plots LV end diastolic pressure ($P_{1vcl}$) in mmHg. The data shows a slight, gradual increase in pressure as the pump speed increases. The experimental (exp) and modeled (mod) results for both Pig 1 and Pig 2 are closely aligned.
> 2.  **Second Panel ($P_{1vcs}$):** This panel plots LV peak systolic pressure ($P_{1vcs}$) in mmHg. A clear, steady upward trend is visible, indicating that peak systolic pressure increases significantly as the pump speed increases. The experimental and modeled data points track each other closely across the speed range.
> 3.  **Third Panel ($\overline{P_{ao}}$):** This panel plots mean aortic pressure ($\overline{P_{ao}}$) in mmHg. The data shows a slight, gradual increase in mean aortic pressure as the pump speed increases, with the lines for both pigs remaining tightly clustered.
> 4.  **Fourth Panel ($\overline{CO}$):** This panel plots mean total cardiac output ($\overline{CO}$) in Liters per minute (L/min). This panel shows the most dramatic change, with $\overline{CO}$ increasing sharply and non-linearly as the pump speed increases, particularly after 1800 rpm. The modeled and experimental data for both pigs show strong agreement in this trend.
> 5.  **Bottom Panel (SHE):** This panel plots Surplus Hemodynamic Energy (SHE) in ergs/mL. The data shows a steady, gradual increase in SHE as the pump speed increases, with the experimental and modeled lines remaining closely grouped.
>
> Overall, the graph demonstrates the relationship between increasing pump speed and various hemodynamic outcomes, showing that most parameters (pressure, cardiac output, and energy) tend to increase with higher pump speeds, with the model simulations closely matching the experimental data for both pigs.

<center>Fig. 3. Effect of increasing mean pump speed \(\overline{\omega}\) on LV end diastolic pressure \(P_{\mathrm{1vcl}}\) , LV peak systolic pressure \(P_{\mathrm{1vcs}}\) , mean aortic pressure \(\overline{P_{\mathrm{ao}}}\) , mean total cardiac output \(\overline{\mathrm{CO}}\) , and surplus hemodynamic energy SHE from both the in vivo pig experiments and model simulations using corresponding optimized parameters. ANO state occurred at \(\overline{\omega} >2100 \mathrm{r / min}\) in pig 1 and \(\overline{\omega} >1850 \mathrm{r / min}\) in pig 2. </center>

> **Image description.** A technical line graph consisting of two stacked panels, illustrating the relationship between mean pump speed ($\overline{\omega}$) and two hemodynamic parameters, PVR and SV, based on model simulations.
>
> The overall graph shares a common X-axis representing the mean pump speed ($\omega$) in revolutions per minute (rpm), ranging from 1400 to 2600. The legend, located at the top center, identifies the two data series: "Pig 1 (mod)" represented by solid circles (●) and "Pig 2 (mod)" represented by solid triangles (▲).
>
> The top panel displays the Pulmonary Vascular Resistance (PVR).
> *   **Y-axis:** Labeled "PVR (mmHg/s/ml)," ranging from 0.1 to 0.25.
> *   **Data Trend:** Both the Pig 1 and Pig 2 lines show an increasing trend in PVR as the pump speed ($\omega$) increases. The line for Pig 2 (triangles) consistently maintains a higher PVR value than the line for Pig 1 (circles) across the entire speed range.
>
> The bottom panel displays the Stroke Volume (SV).
> *   **Y-axis:** Labeled "SV (ml)," ranging from 0 to 40.
> *   **Data Trend:** Both the Pig 1 and Pig 2 lines show a decreasing trend in SV as the pump speed ($\omega$) increases. The line for Pig 1 (circles) consistently maintains a higher SV value than the line for Pig 2 (triangles) across the entire speed range.
>
> Below the two graphs, the figure caption is provided: "Fig. 4. Effect of increasing mean pump speed $\overline{\omega}$ on PVR and SV from model simulations using optimized parameters for both pigs. It was not possible to directly instrument the animals to record these parameters experimentally."

<center>Fig. 4. Effect of increasing mean pump speed \(\overline{\omega}\) on PVR and SV from model simulations using optimized parameters for both pigs. It was not possible to directly instrument the animals to record these parameters experimentally. </center>

> **Image description.** A multi-panel line graph displaying the time course of five different hemodynamic parameters over a period of 5 seconds. The graph consists of five stacked subplots, all sharing a common horizontal time axis labeled "$t$ (s)" ranging from 0 to 5.
>
> The data in each subplot is presented using two line styles: a dashed line representing "Simulation" and a solid line representing "Measurement," as indicated by the legend located in the bottom right corner.
>
> The five subplots, from top to bottom, are labeled and represent the following variables:
>
> 1.  **$V_{1v}$ (mL):** This top panel shows the Left Ventricular volume. The data exhibits sharp, periodic spikes, fluctuating between approximately 0 and 45 mL. Both the simulation and measurement lines track each other closely, showing similar oscillatory patterns.
> 2.  **$R_{1vct}$ (mmHg/s):** This second panel represents the suction resistance. The values are generally low, fluctuating between 0 and 30 mmHg/s, with distinct peaks corresponding to the cycles seen in the volume plot above.
> 3.  **$P_{1v}$ (mmHg):** This third panel displays the Left Ventricular pressure. The pressure cycles between approximately -40 and 30 mmHg. The solid measurement line and the dashed simulation line show a strong correlation in their cyclical behavior.
> 4.  **$P_{1n}$ (mmHg):** This fourth panel shows the pump inlet pressure. The values are relatively low, ranging roughly from -40 to 10 mmHg, and exhibit sharp, periodic fluctuations.
> 5.  **$Q_p$ (L/min):** The bottom panel represents the pump flow. The flow rate is positive and oscillatory, ranging from near 0 to approximately 6 L/min. The measurement and simulation lines are highly synchronized, demonstrating a strong agreement in the flow dynamics.
>
> Overall, the graph visually demonstrates the time-dependent relationship between various parameters (volume, resistance, pressure, and flow) during a cardiac cycle, comparing experimental data (Measurement) against a computational model (Simulation).

<center>Fig. 5. Time course of LV volume \(V_{\mathrm{1v}}\) , suction resistance \(R_{\mathrm{1vct}}\) , LV pressure \(P_{\mathrm{1v}}\) , pump inlet pressure \(P_{\mathrm{1n}}\) , and pump flow \(Q_{p}\) from an in vivo pig experiment (pig 1) implanted with rotary pump superimposed on model simulations during LV suction caused by an excessive pump speed setting (in this case, \(2560 \mathrm{r / min}\) ). </center>

waveforms (see Figs. 2 and 3). As reported in [6], [22], and [23], and observed in our animal experiments, LV peak systolic pressures produced by the model were maintained as pump speed was increased until the point where LV systolic pressure became insufficient to allow for aortic ejection (see Figs. 2 and 3). At this point, LV end diastolic volume became so small that LV peak systolic pressure fell dramatically and the left ventricle no longer needed to generate enough pressure to open the aortic valve. As a result, LV peak systolic pressure dropped rapidly with increasing pump speed.

On the other hand, LV end diastolic pressure decreased with increasing pump speed, as observed in our experimental data (see Figs. 2 and 3) and reported by others [22], [23]. This is due to a shift in blood volume from the pulmonary to the systemic circulation. LA pressure is, in turn, also reduced with increasing LVAD support. This aids pulmonary venous return up to the point where the pulmonary venous pressure is less than the intrathoracic pressure. At this point, pulmonary veins located at the entry to the left atrium collapse, causing an increase in PVR and preventing any further increase in pulmonary venous return. This phenomenon is clearly shown in Figs. 2 and 3, where the pump speeds at which significant reduction in LV end diastolic

TABLE VI EFFECT OF HEART FAILURE AND PUMP SPEEDS ON MEAN AORTIC PRESSURE \(\overline{P_{\mathrm{ao}}}\) , MEAN PULMONARY ARTERIAL PRESSURE \(\overline{P_{\mathrm{pa}}}\) , MEAN LA PRESSURE \(\overline{P_{\mathrm{la}}}\) MEAN VENA CAVA PRESSURE \(\overline{P_{\mathrm{vc}}}\) , PERCENTAGE VOLUME IN SYSTEMIC AND PULMONARY CIRCULATION \(V_{sys}\) AND \(V_{\mathrm{pu1}}\) , LEFT AND RV END DIAGSTIC VOLUMES \(V_{\mathrm{1vecl}}\) AND \(V_{\mathrm{revcl}}\) , MEAN PUMP FLOW \(Q_{p}\) , PEAK-TO-PEAK PUMP FLOW \(Q_{p,PP}\) , MEAN AORTIC VALVE FLOW \(\overline{Q_{\mathrm{av}}}\) , MEAN CARDIAC OUTPUT \(\overline{\mathrm{CO}}\) , AND PUMPING STATE (VE, VENTRICULAR EJECTION; ANO, NONOPENING OF AORTIC VALVE; SUC, VENTRICULAR SUCTION)

| Variable | Pig 1 | | | | HF1 | | | | HF2 | | | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | w (rpm) - 1700.0 | 1900.0 | 2100.0 | | w (rpm) - 1700.0 | 1900.0 | 2100.0 | | w (rpm) - 1700.0 | 1900.0 | 2100.0 |
| Pao (mmHg) | 62.4 | 65.7 | 66.6 | 67.4 | 35.3 | 49.6 | 53.9 | 58.7 | 36.7 | 47.6 | 51.5 | 48.0 |
| Ppa (mmHg) | 15.1 | 14.7 | 14.7 | 14.9 | 18.9 | 15.4 | 14.8 | 14.1 | 14.2 | 12.5 | 11.7 | 14.2 |
| Pla (mmHg) | 4.6 | 3.6 | 3.4 | 3.1 | 13.4 | 7.5 | 6.0 | 4.5 | 8.9 | 5.2 | 3.7 | 2.0 |
| Pvc (mmHg) | 4.8 | 4.7 | 4.7 | 4.7 | 5.5 | 5.5 | 5.4 | 5.3 | 7.3 | 7.0 | 7.0 | 8.1 |
| Vsys (%) | 84.9 | 86.0 | 86.3 | 86.5 | 76.5 | 81.5 | 82.8 | 84.3 | 79.8 | 83.0 | 84.5 | 85.1 |
| Vpu1 (%) | 7.6 | 7.0 | 6.9 | 6.8 | 12.9 | 9.2 | 8.3 | 7.4 | 9.7 | 7.5 | 6.5 | 6.0 |
| V1vecl (mL) | 116.0 | 95.8 | 88.7 | 82.5 | 170.3 | 136.6 | 122.7 | 105.2 | 127.1 | 96.1 | 85.1 | 70.0 |
| Vrevcl (mL) | 90.4 | 94.7 | 96.2 | 98.7 | 97.9 | 105.7 | 109.4 | 113.9 | 137.2 | 143.9 | 145.1 | 154.5 |
| Qp (L.min-1) | 0.0 | 3.3 | 4.1 | 4.9 | 0.0 | 3.8 | 4.2 | 4.6 | 0.0 | 3.5 | 3.8 | 3.5 |
| Qp,PP (L.min-1) | 0.0 | 3.5 | 2.9 | 2.5 | 0.0 | 1.5 | 1.1 | 0.7 | 0.0 | 1.3 | 0.6 | 3.3 |
| Qav (L.min-1) | 4.9 | 2.0 | 1.2 | 0.5 | 2.5 | 0.0 | 0.0 | 0.0 | 2.5 | 0.0 | 0.0 | 0.0 |
| CO (L.min-1) | 4.9 | 5.2 | 5.3 | 5.4 | 2.5 | 3.8 | 4.2 | 4.6 | 2.5 | 3.5 | 3.8 | 3.5 |
| Pumping state | VE | VE | VE | VE | VE | VE | VE | ANO | ANO | ANO | VE | ANO | SUC |

pressure first occur (see Fig. 3) coincided with pump speeds at which PVR began to increase (see Fig. 4). Since cardiac output equals venous return in the steady state, total flow out of the ventricle reaches a plateau during this phase. As a result, further increase in LVAD speed eventually leads to LV suction.

Our animal experiments were carried out under complete autonomic blockade and we did not observe any significant changes in aortic pressure, central venous pressure, heart rate or systemic vascular resistance during the LVAD unloading. Therefore, we did not include any baroreceptor components in our model. Despite this, the model was able to reproduce the relatively constant mean aortic pressure across the full range of pump speeds (see Figs. 2 and 3). Given the absence of baroreceptor components in our model, we believe that this may in part be attributable to hydraulic or mechanical effects, such as improper filling of the left ventricle at higher pump speeds.  

Conflicting findings have been reported in the literature regarding the change in mean aortic pressure and total cardiac output with increasing pump assistance levels [24], [25]. We observed that total cardiac output (aortic valve flow \(^+\) pump flow) remained relatively constant regardless of pump speed (see Figs. 2 and 3). This is consistent with published experimental findings in normal (i.e., nonfailing) hearts [25]. However, the efficiency of an LVAD in improving total cardiac output depends on metabolic demand as well as the condition of the patients [26]. Guyton suggested that under normal resting conditions, cardiac output is controlled almost entirely by peripheral factors governing return of blood to the heart, while the heart controls the permissible amount of output that can be pumped [27]. In the present paper, we studied the hemodynamic response of the CVS with varying degrees of LVAD assistance under various heart failure conditions. Our results (see Table VI) agreed with published experimental findings, which showed an increase in total cardiac output and mean aortic pressure with increasing pump speeds in the failing heart but insignificant change in the nonfailing heart [25]. However, the increase in the LA \((P_{\mathrm{la}})\) and pulmonary arterial pressure \((P_{\mathrm{pa}})\) in our simulation results for the heart failure conditions was not as high as that reported clinically. This may be due to the fact that we have not included the compensatory mechanisms involved in heart failure, such as peripheral vasoconstriction and fluid retention.

Furthermore, we demonstrated that the improvement in cardiac output with LVAD assist is most apparent in LVF patients with reasonable right heart contractility (i.e., HF1, as compared to HF2). It was reported that right- sided circulatory failure (RSCF) occurs in \(15\% - 30\%\) of the patients supported with LVAD [28] due to three reasons: existing RSCF, reduced RV contractility due to leftward shift of the interventricular septum, and functional mismatch between the LVAD and the native circulation [26]. It can be shown from Table VI that in the simulation of HF2 with severe RV failure, the baseline \(V_{\mathrm{revcl}}\) and \(P_{\mathrm{vc}}\) was significantly higher compared to that of the healthy condition. Increasing LVAD assistance helps reduce the LV end diastolic stress (indicated by the decrease in \(V_{\mathrm{revcl}}\) ) and increasing the total blood flow. However, this further increased \(V_{\mathrm{revcl}}\) and impaired the pressure generating capability of the overstretched, failing right ventricle, thus limiting venous return to the left ventricle (as indicated by the low \(\overline{P_{\mathrm{la}}}\) ). As a result of this mismatch between the LV and the RV output, the left ventricle experienced suction before the LVAD could generate sufficient blood flow required by the circulation system. Furthermore, this may further impair RV performance, through both series and direct interaction.

Both our experimental data and simulation results showed a decrease in pulsatility in aortic pressure, pump flow, speed, and current with increasing pump speed (see Fig. 2 and Table VI) until the point where suction occurred. This is consistent with published experimental findings [23]. Tagusari et al. [29] have suggested that flow pulsatility depended not only on the native cardiac output, but also on the slope of the pump head- flow \((H - Q)\) curve at which the pump was operating. Therefore, flow pulsatility varied with pump parameters and speed, contractility of the heart, as well as systemic vascular resistance, all of which altered the operating region of the pump on the \(H - Q\) curve.

The results of parameter sensitivity analysis and the parameter estimation procedure revealed that total circulatory volume

\((V_{\mathrm{total}})\) is the most relevant parameter that may cause a difference between the two pigs. The lower values for LV pressure, mean aortic pressure, vena cava pressure, and mean cardiac output, as well as the earlier suction speed in pig 2 may be related to its lower circulatory volume compared to pig 1. Decrease in total blood volume decreased preload (indicated by decreased vena cava pressure and LA pressure) to the heart, thus decreasing SV, cardiac output, mean aortic pressure, and pump flow pulsatility. On the other hand, the aortic and systemic peripheral resistance \((R_{\mathrm{ao}}\) and \(R_{\mathrm{sa}}\) ) that affect the afterload to the left ventricle are also highly responsible for determining the LV and aortic pressures (both mean values and pulse pressure). Increasing the systemic afterload decreased the SV and cardiac output, while shifting the LV PV loops to higher volume, resulting in an increase in LV and mean aortic pressure. Furthermore, pump flow pulsatility, which is largely determined by the difference between the pump differential pressure during systole and diastole, increased as a result of the significant increase in aortic pressure.

### B. Comparison With Previous Models

Previous work on heart- pump interaction studies has not focused on fitting the entire waveforms to actual experimental measurements nor has it targeted the dynamics of the responses during various pumping state transitions in a quantitative sense. In the present study, we have attempted to fit our model parameters to reproduce the steady- state hemodynamic waveforms of our animal experimental measurements (quantitatively) over a wide range of pump speeds to cover all the important pumping state transitions, from ventricular ejection to suction. Transient dynamics, such as pulsatility index, are known to provide important information for pump control development [30], and are also closely related to dangerous pump operating conditions, including suction/ventricular collapse [4]. Furthermore, we have also extended our effort to study the effect of increasing pump speed on some important hemodynamic variables under two different heart conditions with varying degrees of LV and RV ventricular contractility, and showed that the efficiency of LVAD assist in improving cardiac output depends on the conditions of the patients.  

One important feature that we have included is the Starling resistance effect for vessel collapse. Continuous LVAD pumping unloads the left ventricle and potentially reduces LA or pulmonary venous pressure to below the intrathoracic pressure. At this point, any further increase in flow or venous return is impeded. It is shown from our simulations that the Starling mechanism may be responsible for the significant decrease in LA pressure at high pump speeds (see Figs. 3 and 4), leading to suction (see Fig. 5). Moreover, Reesink et al. have suggested that suction- induced vessel collapse is responsible for the persistence of collapse after a suction event [3]. Although we were not able to determine the PVR experimentally for the two pigs, we have observed from our recent experiments (unpublished), which measured both pulmonary arterial and LA pressures that the increase in PVR near the region of suction is a genuine phenomena. We do not exclude other alternatives that may have caused this apart from the Starling mechanism, such as the dependencies of PVR on the pulmonary blood volume, which was decreased with increasing pump speeds.

Compared to most models that use a linear ESPVR for the ventricles [2], [3], we have adopted a curvilinear ESPVR as proposed by Kass et al. [9]. This is supported by the published data [31], which show that the end systolic points of LV PV loops obtained with different pump speeds do not fall on the same straight line as those obtained without pump assist. Furthermore, numerous studies have shown that there is a contractility- dependent curvilinearity and load dependence associated with the slope of ESPVR \((E_{\mathrm{max}}\) index) [8]. This implies that at extremes of LVAD unloading, where the LV end systolic pressure is less than the mean aortic pressure, end systolic points may lie out of the normally assumed linear ESPVR region into the curvilinear region. As a result, LV pressure has been shown to drop significantly with increasing pump speed in this state. A nonlinear ESPVR is also important under heart failure conditions, where the abnormally high end diastolic volumes reduce the strength of cardiac contraction [8] (which was highlighted in HF2 scenario).

In terms of the cannula resistance, our experimental data show a large pressure drop across the cannula that acts to dissipate the increased pump outlet pressure relative to the aortic pressure. In order to model this, we attempted to fit various cannulae formulations to the experimental data, including the LV pressure, pump inlet pressure, pump outlet pressure, aortic pressure, pump flow, and pump speed. We found that total cannula resistance is best described by a linear function of flow through it, instead of the commonly used constant resistance reported in the literature, while the total cannula inductance can be regarded as a constant. The flow- dependent resistance could be explained by a gradual transition of laminar flow into turbulence, altering the effective cannula resistance. This feature is also partly responsible for the nonlinear increase of pump flow with increasing pump speed (see Fig. 2), with lower increases at higher pump speeds.

### C. Model Limitations

The present paper uses experimental measurements from healthy pigs to assess the effect of various degrees of LVAD assistance on the CVS. Further experimental studies using animals with induced chronic heart failure should be carried out to study the effect of various perturbations, such as changes in heart contractility, systemic vascular resistance, and heart rate.

Furthermore, as inherent in all nonlinear modeling problems, results of our parameter fitting process may not be unique, i.e., we may have found a local minimum. Uniquely determining all the parameters would require isolated experiments for each compartment, measurements of different variables at many points in the circulation, as well as various well controlled and measurable perturbations such as preload, afterload, heart rate and heart contractility. However, given the goodness of fit between model and a large amount of data at various pump speeds, and that the model predicts data that was not used in the fitting process, we believe that the model is a valid representation of the system. In

order to ensure that the optimized parameters are within physiological limits, we have also set constraints for each parameter at a reasonable range, starting at initial estimates obtained from well established literature.

Reflex control as well as autoregulatory systems were also not included in the present model. The baroreceptor response has been shown to be important under conditions of heart failure [32] and exercise [33], suggesting that further extension of our model to incorporate the reflex control system is needed to simulate these pathological conditions.

Furthermore, we have not taken into account the nonlinearities in the vascular pressure- volume (PV) relationship. This may be important during simulations that significantly change the blood volume distribution in the circulation system. Also, we were not able to reproduce regurgitant flow through the aortic valve with the use of an ideal valve model. Accurate modeling of the heart valves may be important in various heart disease situations, such as aortic stenosis.

A final limitation of the present model is that we have not been able to accurately reproduce the LV pressure waveform during suction (see Fig. 5), e.g., the duration of the "positive cycle" of the LV pressure waveform from the model is much lower compared to that of the experimental results. However, we found that LV pressure waveforms are highly variable from one experiment to another, probably due to the complexity of the geometrical changes in the ventricle during a suction event. Furthermore, the ventricular model used in this study may be insufficient in describing end diastolic and end systolic LV PV relationship around zero transmural pressures [34]. Further modeling and experimental efforts that measure both the instantaneous pressure and volume in the ventricle are required to better describe the suction phenomenon. In addition, further measurement of the instantaneous respiration waveform is necessary during the experiments due to the fact that suction events are closely related to respiration.

### V. CONCLUSION

We have presented a dynamic heart- pump interaction model, validated against animal experimental data obtained with the rotary blood pump in place. A number of features that provide important insights into the dynamics of heart- pump interaction have been determined, such as Starling resistance, ESPVR curvilinearity, and suction and pump cannulae descriptions. Simulated responses of the model over a range of pump operating points were quantitatively compared to experimental data recorded during acute implantation of iRBPs in healthy pigs. Furthermore, the effect of pump speed on important hemodynamic variables under various heart conditions was also presented and was shown to agree with published findings.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
