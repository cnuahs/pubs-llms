```
@article{karantonis2007noninvasive,
  title={Noninvasive Pulsatile Flow Estimation for an Implantable Rotary Blood Pump},
  author={Dean M. Karantonis and Shaun L. Cloherty and David G. Mason and Peter J. Ayre and Nigel H. Lovell},
  journal={29th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2007},
  pages={1018-1021},
  doi={10.1109/iembs.2007.4352467},
  url={https://ieeexplore.ieee.org/document/43524677}
}
```

---

# Noninvasive Pulsatile Flow Estimation for an Implantable Rotary Blood Pump

Dean M. Karantonis, Graduate Student Member, IEEE, Shaun L. Cloherty, Member, IEEE, David G. Mason, Peter J. Ayre, Member, IEEE, Nigel H. Lovell, Senior Member, IEEE

Abstract—A noninvasive approach to the task of pulsatile flow estimation in an implantable rotary blood pump (iRBP) has been proposed. Employing six fluid solutions representing a range of viscosities equivalent to \(20 - 50\%\) blood hematocrit (HCT), pulsatile flow data was acquired from an in vitro mock circulatory loop. The entire operating range of the pump was examined, including flows from \(- 2\) to \(12 \mathrm{L} / \mathrm{min}\) . Taking the pump feedback signals of speed and power, together with the HCT level, as input parameters, several flow estimate models were developed via system identification methods. Three autoregressive with exogenous input (ARX) model structures were evaluated: structures I and II used the input parameters directly; structure II incorporated additional terms for HCT; and the third structure employed as input a non- pulsatile flow estimate equation. Optimal model orders were determined, and the associated models yielded minimum mean flow errors of \(5.49\%\) and \(0.258 \mathrm{L} / \mathrm{min}\) for structure II, and \(5.77\%\) and \(0.270 \mathrm{L} / \mathrm{min}\) for structure III, when validated on unseen data. The models developed in this study present a practical method of accurately estimating iRBP flow in a pulsatile environment.

## I. INTRODUCTION

IMPLANTABLE rotary blood pumps (iRBPs) are emerging as a viable long- term treatment option for end- stage heart failure patients. Indeed the so- called third generation iRBPs are proving their worth as both bridge- to- transplant and destination therapy devices [2]. Developing an effective pump control method, in which blood flow actively responds to meet physiological demand, remains a vital objective for the operation of such devices.

Estimating the blood flow rate through an iRBP is essential if a pump control strategy based on flow is to be implemented. While some groups [4] have incorporated an implanted flow sensor into their left ventricular assist devices (LVADs), a noninvasive approach for flow estimation is desirable. Employing the feedback signals of pump impeller speed and motor current (or power), as well as information regarding the hematocrit (HCT) level (or viscosity) of the implant recipient, it has been demonstrated [9- 16] that an estimate of flow rate under non- pulsatile or steady- flow conditions may be attained.

In a pulsatile environment however, the effects of impeller inertia, speed control mechanisms, native heart interaction and other fluid dynamic behavior must be considered. The aim of the present study is the realization of a noninvasive estimate of pulsatile pump flow that is accurate across a range of fluid

D.M. Karantonis (email: z2272629@student.unsw.edu.au), S.L. Cloherty and N.H. Lovell are with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney NSW 2052, Australia. N.H. Lovell is also with National Information and Communications Technology Australia (NICTA), Eveleigh NSW 1308, Australia. D. G. Mason is with the Dept Surgery, Monash University, Melbourne, Australia. P.J. Ayre is with Ventracor Limited, Chatswood NSW 2067, Australia. This work was supported in part by an Australian Research Council Linkage Grant.

viscosities, and is based on pump feedback signals and a value for fluid viscosity. Information about the system, available to such an estimation algorithm, is highly constrained; for example, the magnitude of native cardiac contractions and the flow resistance encountered by the pump are unknown. Thus, rather than attempting to derive a flow estimate from a theoretical pump model, the more empirical approach of system identification was favored. In this paper we describe a pulsatile flow rate estimation algorithm based on an autoregressive with exogenous input (ARX) model and measurements of pump speed, power and HCT obtained in a mock circulatory loop.

## II. METHODS

### A. Mock Loop Experiments

A series of laboratory experiments were conducted with the VentrAssist™ (Ventracor Limited, Sydney, NSW, Australia) LVAD - a centrifugal iRBP - in a pulsatile mock circulatory loop (Fig. 1). The mock loop consisted of: a venous reservoir tank; an arterial reservoir tank; a silicone bag representing the left ventricle; the VentrAssist™ LVAD; and appropriate tubing inter- connections. Each compartment was designed to adhere to the appropriate physiological values (Table 1), ensuring that a valid simulation of the human cardiovascular system was performed.

Simulation of ventricular contraction was achieved by

> **Image description.** A schematic flow diagram illustrating a mock circulatory loop, designed to test the performance of an implantable rotary blood pump (LVAD). The diagram uses labeled components and connecting lines to represent the path of fluid flow.
>
> The system is organized as a closed loop, with the LVAD (1) serving as the central pump. The flow path begins at the LVAD and proceeds through the following sequence:
>
> 1.  **LVAD (1):** The pump component.
> 2.  **Arterial Reservoir:** A storage tank receiving flow from the pump.
> 3.  **Arterial Probe:** A measurement point located in the arterial side of the loop.
> 4.  **Systemic Resistance (3):** A component representing the resistance of the circulatory system.
> 5.  **Venous Reservoir (4):** A storage tank collecting flow after passing through the systemic resistance.
> 6.  **Left Ventricle Simulator:** A component that simulates the function of the heart's left ventricle.
> 7.  **Pump Flow Probe:** A measurement point located near the pump, completing the loop back to the LVAD.
>
> The diagram uses clear labels and numbers to identify each part:
> *   **LVAD (1):** The pump.
> *   **Arterial Reservoir:** The upper storage tank.
> *   **Arterial Probe:** A measurement point on the arterial line.
> *   **Systemic Resistance (3):** A component representing vascular resistance.
> *   **Venous Reservoir (4):** The lower storage tank.
> *   **Left Ventricle Simulator:** The component simulating the heart.
> *   **Pump Flow Probe:** A measurement point on the line leading into the pump.
>
> The caption below the figure reads: "Fig. 1. Schematic diagram of the mock circulatory loop employed in this". The overall visual style is that of a technical engineering schematic, using simple geometric shapes and lines to represent fluid dynamics and component connections.

<center>Fig. 1. Schematic diagram of the mock circulatory loop employed in this study. The diamonds indicate the location of each pressure transducer: (1) pump inlet; (2) pump outlet; (3) arterial pressure; and, (4) central venous pressure. </center>

TABLE I. COMPARISON OF VARIOUS PHYSIOLOGICAL PARAMETERS OCCURRING IN HEART FAILURE PATIENTS WITH THOSE EMPLOYED IN THE MOCK CIRCULATORY LOOP. (VALUES ARE MEAN \(\pm\) SD; DSC \(=\) DYNE.SEC.CM)

| Parameter | Human | Mock Loop |
| :--- | :--- | :--- |
| Arterial Compliance (mL/mmHg) | 1.38 ± 0.51 [1] | 0.91-1.25 |
| Venous Compliance (mL/mmHg) | 80 [3], 50 [5], 62.2 +/- 28.1 [6] | 49-50 |
| Peripheral Resistance (DSC) | 2085 ± 560 [1], 1800 [7], 2023 [8] | 100-6000 |
| Mean Circulatory Pressure (mmHg)* | 20 [7] | 20 |

\\* The mean circulatory pressure refers to the pressure within the mock loop compartments when the system is idle, and required for providing the initial preload (central venous) pressure.

periodically compressing the mock ventricle with pneumatic pistons mounted on adjustable stages. Both the in- stroke and out- stroke periods, as well as the stroke length of the pistons, could be independently set to predefined values, thus approximating the desired heart rate and cardiac contractile strength. Furthermore, the ventricle wall was open to air, allowing passive filling to occur.

The mock loop was instrumented to measure: arterial (AP), central venous (CVP), pump inlet \(\mathrm{(P_{in})}\) and pump outlet \(\mathrm{(P_{out})}\) pressures using pressure transducers (ADInstruments, Castle Hill, NSW, Australia); and, pump flow \(\mathrm{(Q_p)}\) by means of an ultrasonic flow probe (Transonics Systems Inc., Ithaca, NY, USA). The noninvasive pump feedback signals of instantaneous pump impeller speed, motor current and supply voltage were monitored from the pump controller, filtered appropriately and also recorded for analysis. A Powerlab data acquisition system (ADInstruments) was employed to record all the aforementioned signals, with all pressure signals preconditioned using a Quad Bridge amplifier (ADInstruments). Six experiments were performed, each with an aqueous glycerol solution of different viscosity used to simulate human blood (2.05- 3.56 mPas). The range of viscosities was chosen to coincide roughly with a blood haematocrit (HCT) range of \(20 - 50\%\) , based on previous experiments by the authors. For each test fluid, a series of speed ramp tests was conducted, whereby the target pump speed setting was varied between \(1800 - 3000\mathrm{rpm}\) (in step increments of 100 rpm, with each speed setting lasting \(30\mathrm{s}\) ) at several systemic resistance settings, providing a range of flow rates from - 2 to \(12\mathrm{L} / \mathrm{min}\) . The level of contractility introduced via mock ventricle compression was also varied from no pulsatility to high pulsatility (at which the pump flow amplitude reached a maximum of \(3\mathrm{L} / \mathrm{min}\) ) for all operating points, with a fixed heart rate of \(72\mathrm{bpm}\) . The aortic valve was closed for all tests, consistent with clinical observations of implant recipients. The sampling rate was \(4\mathrm{kHz}\) for data acquisition, however subsequent analysis dealt with data at \(50\mathrm{Hz}\) .

### B. System Identification Methods

In approaching the problem of accurately estimating pump flow in a pulsatile environment, a number of system identification methods were examined. This methodology was chosen due to its ability to describe, in terms of an appropriate transfer function, discrete time- series data where the input(s) sufficiently describe the target output. The only inputs available are the noninvasive feedback signals of pump speed and power. It is also assumed that the patient's HCT level is known (within a range of \(5\%\) ).

There are a number of potential model structures that may be chosen, such as the ARX, output error (OE) or Box- Jenkins (BJ) types. Each of these treats the system dynamics and the disturbance dynamics in a different manner. Due to the excellent signal- to- noise ratio of our system, and the tight coupling between inputs and external disturbances, the ARX model structure was employed for this study. The generic form of an ARX model may be described by the difference equation:

\[\sum_{i = 0}^{N_s}a_iy(t - i) = \sum_{j = 1}^{N_k}b_ju(t - N_k - j + 1) \quad (1)\]

where: \(\mathrm{y(t)} =\) (vector of) output signal(s)

\(\mathrm{u(t)} =\) (vector of) input signal(s)

\(\mathrm{N_s} =\) output order \(=\) number of poles

\(\mathrm{N_b} =\) input order \(=\) number of zeroes

\(\mathrm{N_k} =\) input delay (samples)

Flow rate in the VentrAssist™ pump may be described, for the non- pulsatile case, by the polynomial relationship in (2) [9, 13].

\[Q = a + b\cdot VI + c\cdot VI^2 +d\cdot VI^3 +e\cdot N \quad (2)\]

where: \(Q =\) pump flow (L/min)

\(VI =\) pump power (W)

\(N =\) pump speed (rpm)

Thus, the initial approach involved developing separate models based on the data for each experiment (i.e., for each solution), according to the inputs of (2) and as depicted in Fig. 2a. The relationship between each of the ARX model coefficients and HCT was examined to determine whether a single model incorporating HCT as an input could be ascertained. However, unlike the four- dimensional nonpulsatile flow equation described in [13] which contained HCT as an input, no such useful relationship could be identified in the presence of pulsatile flow.

Since this first approach proved ineffective, a second structure which incorporated HCT directly was conceived and evaluated (Fig. 2b). In this case, the model assumes that each input term (VI, \(\mathrm{VI}^2\) , \(\mathrm{VI}^3\) and N) is linearly related with HCT.

A third model structure based on a non- pulsatile flow estimate equation developed previously in our laboratory [13] was also tested (Fig. 2c). In this case a static flow model is applied to dynamic (or pulsatile) data, via an ARX model. The advantage here is that the role of viscosity has already been accounted for, and with far fewer inputs than Structure II, computational complexity is reduced.

### C. Treatment of Data

The corpus of available data was divided into two pools: the first contained data from three experiments employing

> **Image description.** A technical block diagram illustrating three different model structures (Model Structure I, II, and III) used for evaluating ARX (AutoRegressive with eXogenous inputs) models, likely in the context of pump flow estimation. Each structure shows inputs feeding into one or more processing blocks, resulting in a specific output.
>
> The diagram is divided into three distinct panels, labeled (a), (b), and (c).
>
> **Model Structure I (Panel a):**
> This structure represents the simplest ARX model.
> *   **Inputs:** Four variables enter the system from the left: $VI$, $VI^2$, $N$, and $K_1$.
> *   **Processing:** These inputs feed into a single large gray rectangular block labeled "ARX model."
> *   **Output:** The output of this model is $Q_p$, which, according to the context, represents the measured pump flow.
>
> **Model Structure II (Panel b):**
> This structure modifies the inputs of the ARX model by incorporating the variable $HCT$ (blood hematocrit).
> *   **Inputs:** Four variables enter the system: $HCT \times VI$, $HCT \times VI^2$, $N$, and $K_2$.
> *   **Processing:** These inputs feed into a single large gray rectangular block labeled "ARX model."
> *   **Output:** The output of this model is $Q_p$, representing the measured pump flow.
>
> **Model Structure III (Panel c):**
> This structure utilizes a two-stage process to estimate non-pulsatile flow.
> *   **Inputs:** Four variables enter the system: $VI$, $VI^2$, $N$, and $HCT$.
> *   **Processing:** The inputs first feed into a gray rectangular block labeled "Non-Pulsatile Flow Estimator." The output of this estimator then feeds into a second large gray rectangular block labeled "ARX model."
> *   **Output:** The final output of this structure is $Q_{p,np,est}$, which represents the estimated non-pulsatile pump flow.
>
> In summary, the diagram visually compares how different combinations of input variables ($VI$, $VI^2$, $N$, $HCT$, and constants $K_1, K_2$) are processed by ARX models, either directly or through an intermediate flow estimator, to produce either the measured flow ($Q_p$) or an estimated non-pulsatile flow ($Q_{p,np,est}$).

<center>Fig. 2. Block representations of the structures used for each of the ARX models evaluated. \(\mathrm{Q}_p =\) measured pump flow; \(\mathrm{Q}_p,\mathrm{np},\mathrm{est} =\) non-pulsatile pump flow estimate; \(\mathrm{VI} =\) pump power; \(\mathrm{N} =\) pump speed; \(\mathrm{HCT} =\) blood hematocrit; \(\mathrm{K}_1\) \(\mathrm{K}_2 =\) constants. </center>

solutions of viscosity 2.05, 2.66, \(3.26\mathrm{mPa}\) , while the second pool contained data from the remaining three experiments (2.35, 2.96, \(3.56\mathrm{mPa}\) ). The pools acted as a training/validation pair, with a number of models being trained using one pool while the other pool was used to validate those models. Changes in pump target speed were included in the data, in order to ensure the transient response of the pump controller could also be identified.

For each model structure described, the model orders and delays were optimized: the number of poles \((\mathrm{N}_\mathrm{a})\) was varied between 0 and 8; the number of zeroes \((\mathrm{N}_\mathrm{b})\) was varied between 1 and 8; and the delay term \((\mathrm{N}_\mathrm{k})\) was determined via cross- correlation of the input and output signals, with a value of 2 used for all models. The modeling task was performed using the MATLAB System Identification Toolbox (The Mathworks, Inc., Natick, MA, USA).

## III. RESULTS

The central performance measure used in the data analysis was the normalized mean flow error \((\mathrm{Q}_{\mathrm{err,abs}})\) (3), while the absolute mean flow error \((\mathrm{Q}_{\mathrm{err,abs}})\) (4) provided an additional indicator of accuracy.

\[\begin{array}{r}Q_{err\_norm}[\% ] = \frac{100}{N}\sum_{k = 1}^{N}\left|\frac{Q_{est}[k] - Q_{max}[k]}{Q_{max}[k]}\right|\\ Q_{err\_abs}[L / \min ] = \frac{1}{N}\sum_{k = 1}^{N}\left|Q_{est}[k] - Q_{max}[k]\right| \end{array} \quad (4)\]

where: \(Q_{est} =\) estimated pump flow (L/min)

\(Q_{max} =\) measured pump flow (L/min)

When calculating \(\mathrm{Q}_{\mathrm{err,norm}}\) flows less than \(1\mathrm{L / min}\) were excluded in order to avoid the skew produced when normalizing errors for flows close to zero.

Results attained for Structure II (Fig. 2b) demonstrated a

TABLE II. PERFORMANCE SUMMARY OF THE FLOW ESTIMATION MODELS UNDER EVALUATION. RESULTS REFER TO THE CASE WHERE A SINGLE TRAINING SET IS VALIDATED AGAINST THE REMAINING DATA. A ROTATION OF THE TRAINING AND VALIDATION SETS PRODUCES SIMILAR RESULTS.

| Model Structure | $N_a$ | $N_b$ | Absolute Mean Error (L/min) | Normalised Mean Error (%) |
| :--- | :---: | :---: | :---: | :---: |
| II | 0 | 4 | 0.260 | 5.56 |
| II | 0 | 5 | 0.259 | 5.52 |
| II | 0 | 6 | 0.258 | 5.49 |
| III | 0 | 4 | 0.271 | 5.78 |
| III | 0 | 5 | 0.270 | 5.77 |
| III | 0 | 6 | 0.270 | 5.78 |

wide range of accuracy, depending on the selection of model orders. In general, orders of \(\mathrm{N}_\mathrm{a} = 0\) and \(\mathrm{N}_\mathrm{b} = 4 - 6\) provided the smallest \(\mathrm{Q}_{\mathrm{err,norm}}\) and \(\mathrm{Q}_{\mathrm{err,abs}}\) (see Table II), with minimum values of \(5.49\%\) and \(0.258\mathrm{L / min}\) respectively. Thus, the models purely dependent on previous inputs provided the best accuracy.

For the third approach, using the non- pulsatile flow estimate as an input to the ARX model, the best performance was also obtained with \(\mathrm{N}_\mathrm{a} = 0\) and \(\mathrm{N}_\mathrm{b} = 4 - 6\) (see Table II). For example, a \(\mathrm{Q}_{\mathrm{err,norm}}\) of \(5.77\%\) and \(\mathrm{Q}_{\mathrm{err,abs}}\) of \(0.270\mathrm{L / min}\) was achieved for \(\mathrm{N}_\mathrm{a} = 0\) and \(\mathrm{N}_\mathrm{b} = 5\)

In comparing approaches II and III, the results reveal that slightly superior performance was attained for the structure II. A visual comparison between these approaches is depicted in Fig. 3, for \(\mathrm{N}_\mathrm{a} = 0\) and \(\mathrm{N}_\mathrm{b} = 4\) . As shown, there is a high level of agreement between the simulated and measured flows, including the ability to accurately track the step change in target pump speed at time 3.7 s.

## IV. DISCUSSION

A limited number of research groups have addressed the problem of pulsatile flow estimation. Tsukiya et. al. [17] developed a non- pulsatile flow estimate equation and applied it to pulsatile data, with a mean flow rate error "almost within \(1\mathrm{L / min}\) ". The team headed by Tohoku University described the development of a pulsatile flow estimator (in a mock circulatory loop) via ARX modeling [18]. When incorporating a second ARX model to account for HCT variation, a mean error of \(1.66\mathrm{L / min}\) was obtained, with a correlation coefficient (r) of 0.85 between estimates and measured flows. For comparison, the current models resulted in an \(r\) value of 0.9926 (when using model II with \(\mathrm{N}_\mathrm{a} = 0\) and \(\mathrm{N}_\mathrm{b} = 6\) ). In light of these earlier results, the present study appears to have produced a highly accurate flow estimation model. Perhaps the only limitation of the approach presented above is the need for information regarding the HCT value. Further research into estimating this value online is being conducted.

Abnormal flow conditions, such as ventricular suction, pump inlet obstruction and regurgitant flow, met varied outcomes with the models tested. The relatively sharp downward flow peaks associated with suction or inlet obstruction were estimated to a high level of accuracy (not shown). Regurgitant (or negative) pump flows did not fair as well, with the flow estimates unable to follow the measured flow into the negative region beyond \(- 0.5\mathrm{L / min}\) . This is due

> **Image description.** A line graph titled "Fig. 3. A comparison between the flow estimates (simulated flow) produced by ARX models II and III, together with the measured flow signal," which plots flow rate over time. The graph illustrates the comparison between a measured flow signal and two simulated flow estimates derived from different models.
>
> The graph features two axes:
> *   **Y-axis (Vertical):** Labeled "Flow (L/min)," representing the flow rate. The scale ranges from 2.5 to 5.5, with major tick marks every 0.5 units (2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5).
> *   **X-axis (Horizontal):** Labeled "Time (s)," representing time in seconds. The scale ranges from 0 to 8, with major tick marks every 1 second.
>
> Three distinct data lines are plotted on the graph, representing different flow sources, as detailed in the legend:
> 1.  **Measured Flow:** Represented by a solid black line.
> 2.  **Simulated Flow (Model 2):** Represented by a gray dashed line.
> 3.  **Simulated Flow (Model 3):** Represented by a light gray dotted line.
>
> All three lines exhibit a highly periodic, pulsatile pattern, characteristic of cardiac flow. The flow rises sharply from a baseline, reaches a peak, and then drops sharply, repeating this cycle multiple times over the 8-second duration. The visual data demonstrates a high degree of correlation and agreement between the measured flow and both simulated flow models, as the three lines track each other very closely throughout the entire time series.
>
> The legend, located in the bottom right corner of the plot, clearly identifies the three data series:
> *   Measured Flow
> *   Simulated Flow (Model 2)
> *   Simulated Flow (Model 3)

<center>Fig. 3. A comparison between the flow estimates (simulated flow) produced by ARX models II and III, together with the measured flow signal. There is a target speed change at time 3.75. </center>

to the behavior of the pump power signal, which does not continue the trend of decline when the flow becomes negative, but rather reaches a minimum plateau value.

As mentioned in the results section, model structure II produced a marginally superior overall performance. However, considering that structure III is far less complex and considerably less computationally intensive, it may be beneficial to implement this simpler method in a real- time embedded application.

Since continuous flow measurements cannot be obtained in implant recipients due to the invasiveness of the required instrumentation, only an average flow estimate may be compared in this case. As such, in vivo animal experiments may be required to provide the appropriate real- time measurements and physiological environment necessary to validate these flow models.

Worthy of note is that the level of pulsatility in the simulated cardiac contractions had no effect on the pump flow- power- speed characteristic, in the time- averaged sense. It was hypothesized that added pulsatility might assist in the work done by the pump, thereby reducing the power requirement to produce a given average flow rate at a fixed speed. However the data demonstrated that this was not the case. This confirms the assertion made by Ayre et. al. [9], that non- pulsatile flow estimates are applicable to pulsatile flow environments when an average estimate is all that is required.

## V. CONCLUSION

A practical method of estimating pulsatile flow in an iRBP to a high degree of accuracy has been described. A reliable flow estimate is not only a clinically valuable parameter to be monitored by the relevant clinicians, but also serves as a fundamental variable for a pump control strategy.

## REFERENCES

[1] G. F. Mitchell, J. C. Tardif, J. M. Arnold, G. Marchiori, T. X. O'Brien, M. E. Dunlap, and M. A. Pfeffer, "Pulsatile hemodynamics in congestive heart failure," Hypertension, vol. 38, pp. 1433- 9, 2001.  
[2] H. Hoshi, T. Shinshi, and S. Takatani, "Third- generation blood pumps with mechanical noncontact magnetic bearings," Artif Organs, vol. 30, pp. 324- 38, 2006.  
[3] F. M. Colacino, M. Arabia, G. A. Danieli, F. Moscato, S. Nicosia, F. Piedimonte, P. Valigi, and S. Pagnottelli, "Hybrid test bench for evaluation of any device related to mechanical cardiac assistance," Int J Artif Organs, vol. 28, pp. 817- 26, 2005.  
[4] O. Voigt, R. J. Benkowski, and G. F. Morello, "Suction detection for the MicroMed DeBakey Left Ventricular Assist Device," Asiao J, vol. 51, pp. 321- 8, 2005.  
[5] Y. Liu, P. Allaire, H. Wood, and D. Olsen, "Design and initial testing of a mock human circulatory loop for left ventricular assist device performance testing," Artif Organs, vol. 29, pp. 341- 5, 2005.  
[6] H. Takatsu, K. Gotoh, T. Suzuki, Y. Ohsumi, Y. Yagi, T. Tsukamoto, Y. Terashima, K. Nagashima, and S. Hirakawa, "Quantitative estimation of compliance of human systemic veins by occlusion plethysmography with radionuclide- methodology and the effect of nitroglycerin," Jpn Circ J, vol. 53, pp. 245- 54, 1989.  
[7] D. Timms, M. Hayne, K. McNeil, and A. Galbraith, "A complete mock circulation loop for the evaluation of left, right, and biventricular assist devices," Artif Organs, vol. 29, pp. 564- 72, 2005.  
[8] G. M. Pantalos, S. C. Koenig, K. J. Gillars, G. A. Giridharan, and D. L. Ewert, "Characterization of an adult mock circulation for testing cardiac support devices," Asiao J, vol. 50, pp. 37- 46, 2004.  
[9] P. J. Ayre, N. H. Lovell, and J. C. Woodard, "Non- invasive flow estimation in an implantable rotary blood pump: a study considering non- pulsatile and pulsatile flows," Physiol Meas, vol. 24, pp. 179- 89, 2003.  
[10] P. J. Ayre, S. S. Vidakovic, G. D. Tansley, P. A. Watterson, and N. H. Lovell, "Sensorless flow and head estimation in the VentArssist rotary blood pump," Artif Organs, vol. 24, pp. 585- 8, 2000.  
[11] A. Funakubo, S. Ahmed, I. Sakuma, and Y. Fukui, "Flow rate and pressure head estimation in a centrifugal blood pump," Artif Organs, vol. 26, pp. 985- 90, 2002.  
[12] T. Kitamura, Y. Matsushima, T. Tokuyama, S. Kono, K. Nishimura, M. Komeda, M. Yanai, T. Kijima, and C. Nojiri, "Physical model- based indirect measurements of blood pressure and flow using a centrifugal pump," Artif Organs, vol. 24, pp. 589- 593, 2000.  
[13] N. Malagutti, D. M. Karantonis, S. L. Cloherty, P. J. Ayre, D. G. Mason, R. F. Salamonsen, and N. H. Lovell, "Noninvasive average flow estimation for an implantable rotary blood pump: a new algorithm incorporating the role of blood viscosity," Artif Organs, vol. 31, pp. 45- 52, 2007.  
[14] K. Nakata, M. Yoshikawa, T. Takano, Y. Sankai, G. Ohtsuka, J. Glueck, A. Fujisawa, K. Makinouchi, M. Yokokawa, and Y. Nose, "Estimation of pump flow rate and abnormal condition of implantable rotary blood pumps during long- term in vivo study," Artif Organs, vol. 24, pp. 315- 9, 2000.  
[15] Y. Wakisaka, Y. Okuzono, Y. Taenaka, K. Chikanari, T. Masuzawa, T. Nakatani, E. Tatsumi, T. Nishimura, Y. Takewa, T. Ohno, and H. Takano, "Noninvasive pump flow estimation of a centrifugal blood pump," Artif Organs, vol. 21, pp. 651- 4, 1997.  
[16] Y. Wakisaka, Y. Okuzono, Y. Taenaka, K. Chikanari, T. Masuzawa, and H. Takano, "Establishment of flow estimation for an implantable centrifugal blood pump," Asiao J, vol. 43, pp. M659- 62, 1997.  
[17] T. Tsukiya, Y. Taenaka, T. Nishinaka, M. Oshikawa, H. Ohnishi, E. Tatsumi, H. Takano, Y. Konishi, K. Ito, and M. Shimada, "Application of indirect flow rate measurement using motor driving signals to a centrifugal blood pump with an integrated motor," Artif Organs, vol. 25, pp. 692- 6, 2001.  
[18] M. Yoshizawa, T. Sato, A. Tanaka, K. Abe, H. Takeda, T. Yambe, S. Nitta, and Y. Nose, "Sensorless estimation of pressure head and flow of a continuous flow artificial heart based on input power and rotational speed," Asiao J, vol. 48, pp. 443- 8, 2002.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
