```
@article{karantonis2006identification,
  title={Identification and classification of physiologically significant pumping states in an implantable rotary blood pump.},
  author={Dean M. Karantonis and Nigel H. Lovell and Peter J. Ayre and David G. Mason and Shaun L. Cloherty},
  journal={Artificial organs},
  year={2006},
  volume={30},
  number={9},
  pages={671-679},
  doi={10.1111/j.1525-1594.2006.00283.x},
  url={https://onlinelibrary.wiley.com/doi/10.1111/j.1525-1594.2006.00283.x}
}
```

---

# Identification and Classification of Physiologically Significant Pumping States in an Implantable Rotary Blood Pump

\*†Dean M. Karantonis, \*‡Nigel H. Lovell, §Peter J. Ayre, §David G. Mason, and \*Shaun L. Cloherty

\*Graduate School of Biomedical Engineering, University of New South Wales, Sydney NSW; †School of Electrical Engineering and Telecommunications, University of New South Wales, Sydney NSW; ‡National Information and Communications Technology Australia, Eveleigh NSW; and §Ventracor Limited, Chatswood, Sydney NSW, Australia

Abstract: In a clinical setting it is necessary to control the speed of rotary blood pumps used as left ventricular assist devices to prevent possible severe complications associated with over- or underpumping. The hypothesis is that by using only the noninvasive measure of instantaneous pump impeller speed to assess flow dynamics, it is possible to detect physiologically significant pumping states (without the need for additional implantable sensors). By varying pump speed in an animal model, five such states were identified: regurgitant pump flow, ventricular ejection (VE), nonopening of the aortic valve over the cardiac cycle (ANO), and partial collapse (intermittent and continuous) of the ventricle wall (PVC- I and PVC- C). These

states are described in detail and a strategy for their noninvasive detection has been developed and validated using \((n = 6)\) ex vivo porcine experiments. Employing a classification and regression tree, the strategy was able to detect pumping states with a high degree of sensitivity and specificity: state VE- 99.2/100.0% (sensitivity/specificity); state ANO- 100.0/100.0%; state PVC- I- 95.7/91.2%; state PVC- C- 69.7/98.7%. With a simplified binary scheme differentiating suction (PVC- I, PVC- C) and nonsuction (VE, ANO) states, both such states were detected with \(100\%\) sensitivity. Key Words: Implantable rotary blood pump- Pumping states- Control strategy- Left ventricular assist device.

Current commercially used implantable rotary blood pumps (iRBPs) make little or no attempt to automatically control pump speed to optimize ventricular assistance. In order to achieve such a control strategy, a major design goal for iRBPs is the ability to reliably and accurately detect pumping states that cause such deleterious effects as ventricular collapse due to overpumping, or pump backflow (regurgitation) as a result of underpumping (1). Naturally, the ideal control set point is where left ventricular (LV) ejection is occurring and there is a net positive flow through both the aortic valve (AV) and the pump.

A state that would be of long- term concern to a patient would occur at higher relative pump speeds when there is insufficient blood in the ventricle to

A state that would be of long- term concern to a patient would occur at higher relative pump speeds when there is insufficient blood in the ventricle to sustain normal LV ejection and the AV remains closed throughout the entire cardiac cycle. In this instance there is no flow through the AV and the possibility of blood stasis distal to the AV, which could lead to significant patient complications due to clotting. However, it has been recognized (2,3) that the aim of ensuring AV opening is often infeasible in patients with LV failure. The lack of native heart contractility in such patients means that in order to attain a level of pump flow which adequately perfuses the body, a pump speed which produces the state of full AV closure is often required. Even higher speeds would result in partial or total ventricular collapse as the volume of blood drawn from the ventricle chamber is increased to a level at which pulmonary supply cannot meet pump demand. Deleterious outcomes could also occur at lower relative pump speeds where there is regurgitant flow through the pump.

Experimentation in the transition of pumping states has previously been investigated by a number

of groups (4- 12). Various groups (9) employ invasive sensors to aid in this process (e.g., to measure the pump flow signal). However, it is desirable to avoid their use due to a considerable reduction in system reliability and increased cost. Research efforts have thus predominantly involved waveform analysis of the noninvasive pump motor feedback signals (current or speed), from which a number of useful indices have been derived by various authors (5- 8,10- 12) as indicators of either over- or underpumping of the heart. For example, Yuhki et al. (5) considered a waveform deformation index (WDI) based on a spectral analysis of the speed signal; Endo et al. (6,7) investigated the symmetry in the current amplitude; and Voigt et al. (12) used the amplified, differentiated current signal as a suction indicator. Most groups, however, fall short of developing algorithms to automate the detection of these abnormal pumping states, and thus do not provide a statistical assessment of the success of their methods (5- 8). The studies that have presented numerical results (4,11,12), however, provide a valuable platform against which a comparison with the current study can be made.

Another important factor in this research topic involves accounting for intersubject variation. Heart failure patients exhibit a large range of severity in their condition, with residual contractility, blood pressure level, and other cardiovascular characteristics influencing the interaction of the iRBP with their native heart. In turn these will affect the nature of the indices associated with different pumping states. Ideally, a classification system should have the ability to operate independently of the patient—that is, a calibration task based on each patient's condition should not be required. In order to ensure a robust classification system is developed, these issues must be suitably resolved.

Our hypothesis is that by using only the noninvasive measure of instantaneous pump impeller speed to assess flow dynamics, it is possible to detect a range of pump states including: regurgitant pump flow (state PR), ventricular ejection (state VE), AV not opening over the entire cardiac cycle (state ANO), and partial collapse (intermittent and continuous) of the ventricle wall during the cardiac cycle (states PVC- I and PVC- C). In this study, a classification and regression tree (CART) is used to detect pumping states for the VentrAssist Left Ventricular Assist System (LVAS) (Ventracor Ltd, Chatswood, Sydney, Australia) based on a series of acute animal experiments. The VentrAssist LVAS employs an iRBP with a hydrodynamic bearing, and is intended for implantation in patients for a period of greater than two years.

## METHODS

## Ex vivo experiments

Six porcine experiments were conducted in which the VentrAssist iRBP was acutely implanted. A sternotomy was performed and the inflow cannula was inserted at the apex of the left ventricle while the outflow cannula was anastomosed to the ascending aorta. The pump was connected to a controller via a percutaneous lead. The controller used hardware- based back- EMF commutation, while the speed control was implemented on the controller's microprocessor firmware.

The animal's native heart was instrumented to record: left ventricular (LVP), left atrial (LAP), aortic (AoP), and pump inlet \(\mathrm{(P_{in})}\) pressures using indwelling catheters (DwellCath; Tuta Laboratories, Lane Cove, NSW, Australia) and pressure transducers (Datex- Ohmeda, Homebush, NSW, Australia); aortic \(\mathrm{(Q_a)}\) and pump \(\mathrm{(Q_p)}\) flows by means of ultrasonic flow probes (Transonics Systems Inc., Ithaca, NY, USA); and a single lead electrocardiogram via needle electrodes. Aortic pressures and flows were measured downstream of the outlet cannula. The LVP sensor was placed in the center of the ventricle (between the pump inlet cannula tip and the mitral valve).

The noninvasive observers of instantaneous pump impeller speed, motor current, and supply voltage were monitored from the pump controller and were also recorded for analysis. A Powerlab data acquisition system (ADInstruments, Castle Hill, NSW, Australia) was employed to record all the aforementioned signals, with all pressure signals preconditioned using a Datex monitor (Datex- Ohmeda, Homebush, NSW, Australia). The experimental data were sampled at \(200\mathrm{Hz}\) .

In the ex vivo experiments, the transition between states was induced by changes in pump speed set point. Pump speed was adjusted in variable increments and within variable ranges, depending on the cardiovascular response given by each animal, in order to produce the full range of state transitions. Typically, each pig underwent several speed ramp tests in which impeller speed was increased from \(1050\mathrm{rpm}\) (at slowest) to \(3000\mathrm{rpm}\) (at greatest) in varying increments, with the recorded signals being allowed to settle for approximately \(30\mathrm{s}\) at each speed set point.

## Pumping state definitions

An initial inspection of the invasive observers of LVP, AoP, Pin, \(\mathrm{Q_a}\) and \(\mathrm{Q_p}\) indicate the presence of five physiologically significant pumping states (PR, ANO, VE, PVC- I, and PVC- C; see Fig. 1). State PR

> **Image description.** A multi-panel time-series line graph, Figure 1, illustrating the temporal evolution of various physiological and mechanical signals across five distinct pump states (PR, VE, ANO, PVC-I, and PVC-C) over a 20-second period. The graph is organized into three horizontal rows (panels) and five vertical columns, with the X-axis representing Time (s) from 0 to 20.
>
> The three rows represent different measured parameters:
> 1.  **Top Panel (Pressure):** Measures pressure in mmHg, with a Y-axis ranging from -100 to 100. It displays three signals: AoP (Aortic Pressure), LVP (Left Ventricular Pressure), and P_in (Inflow Pressure).
> 2.  **Middle Panel (Flow):** Measures flow in l/min, with a Y-axis ranging from -20 to 20. It displays two signals: Aortic flow and Pump flow.
> 3.  **Bottom Panel (Current):** Measures Pump current in Amperes (A), with a Y-axis ranging from 0 to 3000. It displays a single signal: Pump current.
>
> The five vertical columns represent the different pump states, labeled at the top: PR, VE, ANO, PVC-I, and PVC-C.
>
> **Visual Analysis of Pump States:**
>
> *   **PR (Pre-Regurgitant):** This state shows high-amplitude, rhythmic fluctuations across all three panels. The pressure signals (AoP, LVP, P_in) exhibit strong, synchronized oscillations. The flow signals (Aortic flow, Pump flow) are also highly oscillatory. The Pump current shows significant, rhythmic variation, peaking around 1000-2000 A.
> *   **VE (Ventricular Ejection):** Similar to PR, this state displays strong, rhythmic oscillations in pressure and flow. Visually, the LVP signal appears to maintain a higher peak than the AoP signal during the systolic phase, consistent with net forward flow. The Pump current remains high and rhythmic.
> *   **ANO (Anomalous):** The oscillations in this state are present but appear slightly dampened compared to PR and VE. The pressure and flow signals show rhythmic activity, but the amplitude of the fluctuations is visibly reduced.
> *   **PVC-I (Premature Ventricular Contraction - Initial):** The rhythmic oscillations begin to decrease in amplitude. The pressure and flow signals are still visible but less pronounced than in the previous states. The Pump current also shows a reduction in peak amplitude.
> *   **PVC-C (Premature Ventricular Contraction - Complete):** This state is characterized by a significant reduction in signal amplitude. The pressure, flow, and pump current signals are relatively low and appear much flatter and less oscillatory than in the preceding states, indicating a near-cessation of the rhythmic pumping action.
>
> Overall, the graph visually demonstrates a clear trend where the amplitude and intensity of all measured signals (pressure, flow, and current) decrease progressively as the pump state transitions from the highly active PR/VE states toward the low-activity PVC-C state. The labels on the right side of the graph provide the technical identification for each line plotted in the respective panels.

<center>FIG. 1. A summary of the invasive (LVP, AoP, \(\mathrm{P}_{in}\) , \(\mathrm{Q}_{in}\) and \(\mathrm{Q}_{b}\) ) and noninvasive (speed and current) signals as the iRBP operates at five different speed set points, demonstrating the five pump states from PR when underpumping to PVC-C when overpumping. </center>

is characterized by negative (or regurgitant) \(\mathrm{Q}_{\mathrm{p}}\) during diastole, caused as a result of the AoP surpassing the sum of LVP and the pump differential pressure. This condition usually occurs at relatively low pump speeds, but is otherwise quite similar to VE; LV ejection is maintained in systole and the amplitude of \(\mathrm{Q}_{\mathrm{p}}\) appears normal. PR is often associated with relatively strong native heart contractility, which is able to drive AoP sufficiently high to initiate the reverse flow.

The ideal pumping state appeared to be state VE, where blood flowed from both the ventricle and the pump. VE is typified by LV ejection in systole (i.e., maximum \(\mathrm{LVP} > \mathrm{AoP}\) and net aortic flow, \(\mathrm{Q}_{\mathrm{av}} > 0\) and a positive pump flow throughout the cardiac cycle. During systole and diastole, the contracting left ventricle modulated measured instantaneous pump speed and current—the speed control algorithm had a time constant which was sufficiently long (approximately 0.35 s) to allow impeller speed to be modulated by the cardiac cycle. Contraction of the ventricle caused the pump differential pressure to decrease and flow to rise. Torque at the shaft (which is virtual because of the hydrodynamic bearing) is proportional to input power for a constant coil drive voltage. This means that as torque at the "shaft" varies, so does motor current or input power. As flow increases, the increased blood inertia escalates the amount of force or torque on the impeller, temporarily causing impeller speed to fall and power to rise. During isovolumic relaxation, LVP decreased and the AV closed, causing a rise in differential pressure across the pump and pump flow to fall. The sudden deceleration of the blood during diastole applied less torque on the impeller causing speed to increase.

Thus, the speed waveform in VE exhibits a sinusoidal shape, fairly uniform with adjacent cardiac cycles, symmetric between systole and diastole, and inversely related to the flow waveform (i.e., as flow increases, speed decreases).

State ANO occurs when the AV remains closed and \(\mathrm{Q}_{\mathrm{av}}\) is near zero. This state is evidenced by a maximum LVP being less than the AoP and thus insufficient to open the AV, with the arterial pulse pressure much reduced. Increases in pump speed will eventually cause the ventricular contractions to cease and the mitral valve will remain open, at which point the flow will be nonpulsatile. The onset of this state can occur as a result of decreased myocardial contractility, increased pump speed, or a decrease in blood returning from the left atrium into the left ventricle. Noninvasively, the speed waveform exhibits a relatively sharp downward peak during systole, followed by a relatively high plateau during diastole. In state ANO, the level of native heart modulation on the speed signal is generally smaller as compared with VE, and is subject to greater variation in mean value due to a larger influence by the respiratory system. The long- term effects of this state might be stenosis of the AV due to lack of function.

Partial collapse of the ventricle is evidenced at relatively high pump speeds, and involves obstruction of the pump inlet cannula as the ventricle walls suck together. In this state, \(\mathrm{Q}_{\mathrm{p}}\) falls rapidly (often to near zero) at end- systole, with the AV closed at all times. In certain cases, suction of the ventricle walls occurs multiple times per cardiac cycle, indicating an increase in the stress placed on the native heart. In this suction state, the oscillatory nature of pump flow

TABLE 1. Summary of pumping state characteristics and observations, based on both invasive and noninvasive estimators

| State | Defining characteristic | AV flow | Pump flow | Pump speed waveform profile |
| :--- | :--- | :--- | :--- | :--- |
| PR | Pump flow is regurgitant in diastole | Normal | Negative during diastole | Near-sinusoidal |
| VE | Both pump flow and AV flow are positive | Normal | Positive and pulsatile | Near-sinusoidal |
| ANO | AV remains closed throughout cardiac cycle | Near-zero | Positive and less pulsatile | Downward peaks present |
| PVC-I | Ventricular suction occurs intermittently | Near-zero | Falls rapidly at end-systole | Upward peaks present |
| PVC-C | Ventricular suction occurs during every heart beat | Near-zero | Falls rapidly at end-systole | Upward peaks present |

waveforms are driven by the preload transiently volume loading an overpumped left ventricle. It is noted also that the flow collapse is coincident with a small decrease in arterial pressure. The arterial pressure is totally sustained by the pump flow alone. AV flow is near zero, which is explained by the steady near- zero LVP, suggesting that LV contractions have ceased. The ventricle walls being sucked together between the sensor and mitral valve may explain the static LVP and the appearance of the transients on \(\mathrm{P_{in}}\) . As the speed waveform is essentially a mirror image of flow, the sharp decreases in flow produce upward peaks in the speed signal.

The effects of the respiration on cardiac behavior often cause partial collapse of the ventricle to occur intermittently (state PVC- I), that is, not every heartbeat but over a fraction of the respiratory cycle. For the remainder of the respiratory cycle, there is nearzero pulsatility in \(\mathrm{Q_{p}}\) and the AV remains closed. State PVC- C is exhibited when a suction event occurs every cardiac cycle.

As pump speed increased there was a transition in states from the PR state at low pump speeds through VE, ANO, PVC- I, and PVC- C, where PVC- C is evidenced at the highest pump speed. Table 1 summarizes a number of observations regarding changes in various parameters with pumping states based on both invasive and noninvasive estimators.

## Noninvasive observers of flow dynamics

As the pump flow dynamics created by the interaction of the native heart and the left ventricular assist device (LVAD) are imprinted onto the noninvasive speed signal, attempts made to identify the pumping states concentrated on waveform analysis of this signal. This analysis was based largely on considering the relationship between the filtered speed and an average speed signal; a low- pass filter (3dB low- pass frequency cutoff \([F_{c}] \approx 11 \mathrm{~Hz}\) ) was applied to the raw signal to remove noise (providing the filtered speed), while mean filters of length 64 ( \(F_{c} \approx 1.4 \mathrm{~Hz}\) ), 128 ( \(F_{c} \approx 0.7 \mathrm{~Hz}\) ), and 256 ( \(F_{c} \approx 0.35 \mathrm{~Hz}\) ) were applied to produce the averaged signals.  

If we consider the filtered and averaged speed signals superimposed, then the points at which the filtered speed signal crosses its average from a higher to a lower value are known as "negative crossings," while crossings from a lower to a higher value are "positive crossings." A "speed cycle" will thus be defined as the time interval between successive negative crossings. In state VE, a speed cycle will correspond to the same interval as a cardiac cycle—with systole commencing with a negative crossing—thus establishing the native heart rate. When suction occurs, however, the speed cycle no longer sensibly relates to a cardiac cycle.

In all, seven indices derived from the speed waveform were used to classify pump state (see Fig. 2).

1 The speed pulsatility index \((\mathrm{N_{pp}})\) refers to the difference between the maximum and minimum speed over a speed cycle, indicating the amplitude of the speed signal.

\[\mathrm{N_{pp}[i]} = \mathrm{N_{max}[i]} - \mathrm{N_{min}[i]} \quad (1)\]

where: \(\mathrm{N_{max}}\) is the maximum speed value for the ith speed cycle and \(\mathrm{N_{min}}\) is the minimum speed value for the ith speed cycle.

2 The change in \(\mathrm{N_{pp}}\) \((\Delta N_{pp})\) was taken as the difference in consecutive \(\mathrm{N_{pp}}\) values, signifying the extent to which the speed pulsatility is changing.

\[\Delta N_{pp}[i] = \mathrm{N_{pp}[i]} - \mathrm{N_{pp}[i - 1]} \quad (2)\]

3 The change in \(\mathrm{N_{max}}\) \((\Delta N_{max})\) was taken as the difference in maximum speed values over consecutive speed cycles. This parameter serves to highlight the changes in speed maxima, where large values may be associated with suction states.

\[\Delta N_{max}[i] = \mathrm{N_{max}[i]} - \mathrm{N_{max}[i - 1]} \quad (3)\]

4 \(\mathrm{N_{profile}}\) essentially provides a measure of speed amplitude symmetry:

\[\mathrm{N_{profile}[i]} = (\mathrm{N_{av}[i]} - \mathrm{N_{min}[i]}) / \mathrm{N_{pp}[i]} \quad (4)\]

where: \(\mathrm{N_{av}[i]}\) average of the speed signal over ith speed cycle.

As the speed waveform demonstrates shorter downward peaks as seen in state ANO, \(\mathrm{N_{profile}}\) increases, while the sharp upward peaks evidenced in suction states produce relatively lower \(\mathrm{N_{profile}}\) values.

> **Image description.** A multi-panel time-series line graph illustrating five different noninvasive observers of flow dynamics derived from a pump speed signal across five distinct pump states. The graph is organized into a grid of five rows (representing different calculated indices) and five columns (representing the pump states: PR, VE, ANO, PVC-I, and PVC-C).
>
> The common horizontal axis (X-axis) for all panels is labeled "Time (s)" and spans from 0 to 20 seconds. Each row has its own vertical axis (Y-axis) with specific units and scales.
>
> The five rows, from top to bottom, represent the following signals:
>
> 1.  **Pump speed:** This top panel shows the raw speed signal, measured in RPM, with a scale from 0 to 3000. The signal is a periodic oscillation that varies in amplitude and frequency across the five states.
> 2.  **$\Delta N_{profile}$ (rpm):** This panel, also measured in RPM (scale 0 to 3000), displays a signal that is generally low but exhibits sharp, distinct spikes or steps, particularly noticeable during transitions between the pump states.
> 3.  **$N_{free}$ (rpm):** This panel, scaled from 0 to 200 RPM, shows a signal that is relatively stable and low during the PR and VE states. As the pump moves into the ANO, PVC-I, and PVC-C states, the signal increases and becomes more variable.
> 4.  **$\Delta N_{profile}$:** This panel is scaled from 0 to 1.0. It shows a signal that is mostly near zero, with sudden, sharp increases (spikes) occurring primarily during the transitions between the different pump states.
> 5.  **$d^2N/dt^2$ (rpm):** The bottom panel, scaled from 0 to 80 RPM, displays a highly fluctuating, noisy signal characterized by rapid, sharp peaks and troughs, representing the second time derivative of the speed signal.
>
> The five columns represent the following pump states:
> *   **PR**
> *   **VE**
> *   **ANO**
> *   **PVC-I**
> *   **PVC-C**
>
> The overall visual pattern demonstrates how the various derived indices change in response to the pump operating at different speed set points, transitioning through the five defined states. The raw pump speed signal (Row 1) serves as the input for the four derived indices shown below it.

<center>FIG. 2. The noninvasive observers of flow dynamics, derived from the pump speed signal, as the iRBP operates at five different speed set points, demonstrating the five pump states. </center>

5 The change in \(\mathrm{N}_{\mathrm{profile}}\) \((\Delta N_{\mathrm{profile}})\) was taken as the difference in consecutive \(\mathrm{N}_{\mathrm{profile}}\) values, thus showing the manner in which the speed profile is changing.

\[\Delta N_{profile}[\mathrm{i}] = \mathrm{N}_{\mathrm{profile}}[\mathrm{i}] - \mathrm{N}_{\mathrm{profile}}[\mathrm{i} - 1] \quad (5)\]

6 \(\mathrm{N}_{\mathrm{free}}\) refers to the number of samples between successive crossings of the filtered and averaged speed signal. During state VE where the speed signal is near- sinusoidal, the \(\mathrm{N}_{\mathrm{free}}\) values are reasonably constant over time. However, as the waveform becomes less symmetrical, consecutive \(\mathrm{N}_{\mathrm{free}}\) values will differ from each other. Now, if the change in \(\mathrm{N}_{\mathrm{free}}\) \((\Delta N_{\mathrm{free}})\) is considered, this parameter will be relatively low for states in which the speed cycle is symmetric about its central crossing point, while higher values will be obtained when such symmetry diminishes.

7 The second time derivative of the speed signal \((d^2 N / dt^2)\) was also noted to be a valuable index of suction detection, calculated as:

\[\begin{array}{r}d^2 N / dt^2 [\mathrm{k}] = (\mathrm{N}[\mathrm{k}] - \mathrm{N}[\mathrm{k} - 1]) - (\mathrm{N}[\mathrm{k} - 1]\\ -\mathrm{N}[\mathrm{k} - 2]) \end{array} \quad (6)\]

where: \(\mathrm{N}[\mathrm{k}] = k\mathrm{th}\) sample of the speed signal.

Subsequent to the experimental data being classified according to the defined pumping states using the invasive parameters, it was further segmented to ensure the transition periods between speed set points were excluded. The above indices were then calculated for each data set across all three average speed signals; the mean filter of length \(n = 128\) \((F_{\mathrm{c}} = 0.7\mathrm{Hz})\) was determined to be most effective, and a sample of the indices across five pumping states is given in Fig. 2.

## The CART statistical method

CART is a binary decision tree algorithm (13) used to predict membership of cases in the classes of a categorical dependent variable from their measurements on one or more predictor variables. CART is easier to interpret than a multivariate logistic model and is considerably more practical to implement in an embedded control system. Furthermore, it is inherently nonparametric, that is, no assumptions are made regarding the underlying distribution of values of the predictor variables. Thus, CART can handle numerical data that are highly skewed or multimodal. Considering the intersubject variation of the data extracted from the speed signal and the

associated skew in its distribution, the CART approach provided the most appropriate method for dealing with the problem of classifying pumping state based on the noninvasive observers.

The above seven indices formed the basis for the predictor values used in the CART analysis, while the pumping state provided the categorical dependent variable. In order to determine the optimal time interval over which to classify the data, a series of "window" lengths were considered (2, 4, 6, 8, 10, and 15 s intervals). As the data needed to be separated at the junction between speed cycles (because many of the indices are calculated for each speed cycle), the windows were actually taken to end at the first such junction past the stipulated window length. The predictor values were then calculated as either the average or the maximum value of the indices over the desired window length.

If we consider the two broad pumping states of suction (PVC- I and PVC- C) and no suction (VE and ANO), then the consequences of both types of misclassification (a false- negative occurring when a suction event is classified as normal, and a false- positive occurring when a nonsuction event is classified as suction) are clinically significant. In the case of false- negatives, suction events that are ignored can result in myocardial damage (as the LV walls collapse onto each other or are partially sucked into the pump inlet), red blood cell injury (hemolysis), and, because the peripheral blood flow is interrupted, the patient may collapse from lack of perfusion. If a nonsuction interval is identified as suction, then a speed controller may respond by decreasing the speed to alleviate the effect of suction. Should this misclassification persist, a relatively large reduction in pump speed may cause the patient's blood pressure to drop rapidly, and again may result in their collapse. However, it is envisaged that certain safeguards would have to be incorporated into any control mechanism to ensure such a situation is avoided. Another matter to consider here is that there will be a natural bias toward classifying the nonsuction state with higher sensitivity, simply because there are far more data points in the nonsuction category than in that of suction. In light of these issues, provisions were made in the CART analysis to ensure that the accuracies of both types of misclassification were optimized. CART facilitates this objective via a differential cost structure, whereby variable costs can be individually imposed on the full range of misclassifications.  

Data from three pig experiments were pooled for use as a training set, and the MATLAB Statistical Toolbox (The Mathworks, Inc., Natick, MA, USA) employed to build an initial tree. A 10- fold cross validation was then performed on this training set to estimate the true error for trees of various sizes. The optimal tree was determined to be the simplest tree (i.e., the tree of least size) that is within one standard error of the minimum. Using this optimal tree, verification was performed on the remaining three porcine data sets. It should also be noted that there were insufficient data to include state PR in the analysis (in only one pig was this state demonstrated).

## RESULTS

Performance was assessed by comparing the state ascertained by the optimal tree and the "known" state as determined through the invasive methods, and quantified by recording the sensitivity (true positive rate) and specificity (true negative rate) associated with each state. Such analysis was conducted for each window length under test; lengths of 6- 10 s produced the most accurate results overall. Considering the need for a classifier which is both highly accurate and highly responsive (i.e., one which requires a minimal amount of time for decision making), a window of 6 s was determined to be the most appropriate.

The ability to distinguish suction from nonsuction states is of primary importance in this study. Thus, in addition to forming classification trees based on four states, simpler trees were also formed based on more general classifications. The results for a 6 s window length are provided in Table 2. The first column refers to the number of pumping states used as part of the dependent variable for the CART analysis: all four states (VE, ANO, PVC- I, PVC- C) were used initially; the two suction states (PVC- I, PVC- C) were then combined to form the Suction state, thus providing three states for tree building; finally, states VE and ANO were combined to form the No Suction state, providing two states for the analysis. Statistics were also included for the Suction and No Suction states for every group of results (each group having the same number of initial states) after combining the appropriate set of state results. For example, the No Suction results with four initial states are found by treating VE and ANO as a single state when calculating the statistics. Similarly, the results for the Suction states are formed by treating PVC- I and PVC- C as one state. In this way we establish the tree's performance for more general classifications.

The statistical summary indicates that a high level of accuracy was achieved in detection of most pumping states. Perhaps the only exception was state PVC- C, with a sensitivity of 69.7%. However, when considered together with state PVC- I as one Suction state, the sensitivity increases to 99.5%, suggesting

TABLE 2. Results of pumping state classification algorithm

| No. of initial states | Pump state | Correct | Total | Sensitivity (%) | Specificity (%) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4 | VE | 131 | 132 | 99.2 | 100.0 |
| 4 | ANO | 53 | 53 | 100.0 | 100.0 |
| 4 | PVC-I | 45 | 47 | 95.7 | 91.2 |
| 4 | PVC-C | 53 | 76 | 69.7 | 98.7 |
| 4 | No suction | 184 | 185 | 99.5 | 100.0 |
| 4 | Suction | 123 | 123 | 100.0 | 99.5 |
| 3 | VE | 128 | 132 | 97.0 | 99.4 |
| 3 | ANO | 53 | 53 | 100.0 | 98.4 |
| 3 | No suction | 184 | 185 | 99.5 | 98.4 |
| 3 | Suction | 121 | 123 | 98.4 | 99.5 |
| 2 | No suction | 185 | 185 | 100.0 | 100.0 |
| 2 | Suction | 123 | 123 | 100.0 | 100.0 |

The first column refers to the number of pumping states used as part of the dependent variable for the CART analysis: all four states (VE, ANO, PVC-I, PVC-C) were used initially; the two suction states (PVC-I, PVC-C) were then combined to form the Suction state, thus providing three states for treebuilding; finally, states VE and ANO were combined to form the No Suction state, providing two states for the analysis. Statistics were also included for the Suction and No Suction states for every group of results (each group having the same number of initial states) after combining the appropriate set of state results. For example, the No Suction results with four initial states are found by treating VE and ANO as a single state when calculating the statistics.

that the lack of accuracy was due to misclassification between these two suction states (rather than the nonsuction states). Distinction between Suction and No Suction states was performed with great success; in the simplest binary state scheme (i.e., when two initial states were considered), sensitivities of \(100\%\) were attained for both states.

## DISCUSSION  

Extensive research in the area of pumping state detection has been conducted by a number of groups. Yuhki et al. (5) were able to establish the occurrence of suction or regurgitation based on a WDI- the ratio of the fundamental component of the speed waveform power spectral density (PSD) to the higher PSD components. While a WDI exceeding a calculated threshold indicated either suction or regurgitation, establishing which of these two states was actually occurring was done visually (with reference to a graph of WDI against speed) rather than as an automated process. Endo et al. (6,7) from Miyazaki Medical College investigated the index of current amplitude, taken as the difference in maximum and minimum value of the pump current waveform, divided by its simultaneous mean value. They were able to detect the transition between partial and total assist of the native heart (the t- point) as well as the transition between total assist and suction (the s- point). However, because the absolute value of these critical points varies between animals and is affected by changes in the cardiovascular system, it is stated that a coefficient peculiar to each individual would be required. This coefficient would be found by examining pump behavior in response to changes in the cardiovascular system during a postoperative calibration phase- an undesirable requirement. Tanaka et al. (8) propose a suction detection mechanism based on a single index \(\mathrm{(I_s = LPF(I_{mean} - I_{min}) / (I_{max} - I_{min})}}\) ; LPF \(=\) low- pass filter) similar to the Nprofile parameter employed here. However, no discussion is made with regard to interanimal variation in the index. The state detection indices proposed by these groups formed a platform for further research; however, these did not provide an automated system for classification and hence no statistical basis for comparison can be made.

Vollkron et al. (9) analyzed the pump flow signal obtained from patients whose implanted axial RBP includes a flow probe. With such invasive measurement, suction was detected with very high sensitivity and specificity. However, it is desirable to avoid the use of such invasive sensors, as they considerably reduce system reliability and increase cost. Therefore, many groups have attempted to exploit various noninvasive indices to produce a pumping state classifier based on the pump feedback signals.

Amin et al. (4) classified the motor- current waveform into one of the four physiologic regions (below, within, or above the optimal range, and ventricular suction), with reference waveforms using a matched filter. The reliability of their classification was over \(90\%\) , although only a very limited amount of data (42 data segments of 6 s each) were evaluated. Baloa and colleagues (10,11) have considered a number of indices derived from current and flow estimates, based on flow pulsatility, low flow values, changes in mean

flow with respect to changes in speed (known as "diminishing returns"), and waveform symmetry. The weakness of flow estimation when nearing suction, however, meant their best result was \(80\%\) correct detection of suction events. Voigt et al. (12) used the amplified, differentiated current signal to obtain a positive suction detection of \(79\%\) and false detection of \(6\%\) .

The ability of our classification tree to predict pumping states to a high degree of accuracy in the acute porcine experiments is promising. When comparing our approach with that of other researchers in the field, it appears this obtained accuracy can be attributed in part to using a combination of several indices, rather than focusing on a single speed- or current- derived parameter. The unique mechanical design of the VentrAssist iRBP (14)—which generates a particularly flat differential pressure versus pump flow (H- Q) curve—together with the response characteristic of the speed control system, results in a strong relationship between LV and pump impeller dynamics. The flat H- Q characteristic means that pump flow is particularly sensitive to differential pressure variation, and is the result of high impeller radial off- flow and relatively low impeller to housing clearances (<50 μm), which reduces flow leakage. Therefore, as evidenced by comparison with other studies (4,8,12), the shape of the speed waveform is inherently different and more informative than that obtained from other pumps. These waveform characteristics were exploited to detect a range of pumping states with a level of accuracy surpassing that of most previous work in this area. Furthermore, the indices were considered independently of the animal, so that no normalization or calibration was required to account for interanimal differences in physiological condition. The high sensitivities attained when classifying both suction and nonsuction states are also encouraging, given the issues associated with either type of misclassification at this broader level. Achievement of this goal was facilitated by a differential cost structure for misclassification, which the CART method provides.

Pump regurgitation is a state where blood flows backward through the pump, and has been observed to occur in the VentrAssist iRBP only for speeds significantly lower than the accepted minimum (1800 rpm) for normal operation. It has been observed rarely in clinical situations, and was obtained in only one of the porcine experiments—at a pump speed of 1250 rpm. As such, it was surmised that PR is not of critical importance, and that the focus should be placed on the boundary between normal and suction states.

Experiments conducted with healthy animal hearts present obvious concerns in terms of the applicability of data recorded, and considerably more work is needed in models more closely resembling the failing heart to ensure the robustness of the approach. These models will include perturbation of the animal's cardiovascular system (such as infusion of epinephrine to increase heart rate and contractility) and manipulation of hematocrit levels, in order to examine the effects of changes in various physiological parameters. The CART methodology has, however, proven to be an effective tool in solving this type of problem. It is anticipated that development of a noninvasive estimate of pump flow (15) will provide an additional parameter likely to enhance the performance of the CART- based state classifier.

Reliable detection of the various pumping states, particularly the approach of suction and the suction events themselves, has been recognized as a foundation upon which a pump control algorithm may be developed (8,11,16). If speed is set to a target value at which pump flow is at its near- maximal level without inducing suction, then this will provide a systemic flow rate which meets physiological demand. Development of a suitable pump controller for the VentrAssist LVAS, employing such a control methodology, is being investigated.

## CONCLUSION

Employing the CART approach, we have described the successful noninvasive detection and classification of a range of physiologically significant pumping states. Invasive sensors were used to identify these states and seven easily derivable, noninvasive system observers were proposed as a means of realizing state detection. The detection method operated as an automated process, and no calibration was needed to account for interanimal differences. The next stage is to implement this algorithm in our LVAS controller and undertake testing in chronic animal models with induced heart failure.

## REFERENCES

1. Hall AW, Soykan O, Harken AH. Physiologic control of cardiac assist devices. Artif Organs 1996;20:271-5.  
2. Connelly JH, Abrams J, Klima T, Vaughn WK, Frazier OH. Acquired commissural fusion of aortic valves in patients with left ventricular assist devices. J Heart Lung Transplant 2003;22:1291-5.  
3. Rose AG, Park SJ, Bank AJ, Miller LW. Partial aortic valve fusion induced by left ventricular assist device. Ann Thorac Surg 2000;70:1270-4.  
4. Amin DV, Antaki JF, Litwak P, et al. Controller for an axial-flow blood pump. Biomed Instrum Technol 1997;31:483-7.  
5. Yuhki A, Hatoh E, Nogawa M, Miura M, Shimazaki Y, Takatani S. Detection of suction and regurgitation of the implantable centrifugal pump based on the motor current waveform analysis and its application to optimization of pump flow. Arif Organs 1999;23:532- 7.  
6. Oshikawa M, Araki K, Endo G, Anai H, Sato M. Sensorless controlling method for a continuous flow left ventricular assist device. Arif Organs 2000;24:600- 5.  
7. Endo G, Araki K, Kojima K, Nakamura K, Matsuzaki Y, Onitsuka T. The index of motor current amplitude has feasibility in control for continuous flow pumps and evaluation of left ventricular function. Arif Organs 2001;25:697- 702.  
8. Tanaka A, Yoshizawa M, Olegario P, et al. Detection and avoiding ventricular suction of ventricular assist devices. Proceedings of the 2005 IEEE Engineering in Medicine and Biology 27th Annual Conference, Shanghai, China, September 1- 4, 2005.  
9. Vollkron M, Schima H, Huber L, Benkowski RJ, Morello GF, Wieselthaler G. Development of a suction detection system for axial blood pumps. Arif Organs 2004;28:709- 16.  
10. Baloa LA, Liu D, Boston JR, Simaan MA, Antaki JF. Control of rotary heart assist devices. Proceedings of the American Control Conference, Chicago, Illinois. June 2000;2982- 6.  
11. Boston JR, Baloa LA, Liu D, Simaan MA, Choi S, Antaki JF. Combination of data approaches to heuristic control and fault detection. International Conference on Control Applications. Anchorage, Alaska, USA. September 25-27, 2000;98-103.  
12. Voigt O, Benkowski RJ, Morello GF. Suction detection for the MicroMed DeBakey left ventricular assist device. ASAIO J 2005;51:321-8.  
13. Breiman L, Friedman JH, Olshen RA, Stone CJ. Classification and Regression Trees. Monterey, CA: Wadsworth and Brooks, 1984.  
14. Tansley G, Vidakovic S, Reizes J. Fluid dynamic characteristics of the ventrassist rotary blood pump. Arif Organs 2000;24:483-7.  
15. Ayre PJ, Lovell NH, Woodard JC. Non-invasive flow estimation in an implantable rotary blood pump: a study considering non-pulsatile and pulsatile flows. Physiol Meas 2003;24:179-89.  
16. Bertram CD. Measurement for implantable rotary blood pumps. Physiol Meas 2005;26:R99-117.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
