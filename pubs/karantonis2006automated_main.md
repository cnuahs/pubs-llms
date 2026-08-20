```
@article{karantonis2006automated,
  title={Automated Non-invasive Detection of Pumping States in an Implantable Rotary Blood Pump},
  author={Dean M. Karantonis and Shaun L. Cloherty and David G. Mason and Robert F. Salamonsen and Peter J. Ayre and Nigel H. Lovell},
  journal={28th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2006},
  pages={5386-5389},
  doi={10.1109/iembs.2006.259725},
  url={https://ieeexplore.ieee.org/document/4463021}
}
```

---

# Automated Non-invasive Detection of Pumping States in an Implantable Rotary Blood Pump

Dean M. Karantonis, Student Member, IEEE, Shaun L. Cloherty, Member, IEEE, David G. Mason, Robert F. Salamonsen, Peter J. Ayre, Member, IEEE, Nigel H. Lovell, Senior Member, IEEE

Abstract- With respect to rotary blood pumps used as left ventricular assist devices (LVADs), it is clinically important to control pump flow to avoid complications associated with over- or under- pumping of the native heart. By employing only the non- invasive observer of instantaneous pump impeller speed to assess flow dynamics, a number of physiologically significant pumping states may be detected. Based on a number of acute animal experiments, five such states were identified: regurgitant pump flow (PR), ventricular ejection (VE), non- opening of the aortic valve (ANO), and partial collapse (intermittent and continuous) of the ventricle wall (PVC- I and PVC- C). Two broader states, normal (corresponding to VE, ANO) and suction (corresponding to PVC- I, PVC- C) were readily discernable in clinical data from human patients implanted with LVADs. Based on data from both the animal experiments \((\mathrm{N} = 6)\) and the human patients \((\mathrm{N} = 10)\) , a strategy for the automated non- invasive detection of significant pumping states has been developed and validated. Employing a classification and regression tree (CART), this system detects pumping states with a high degree of accuracy: state VE - \(87.5 / 100.0\%\) (sensitivity/specificity); state ANO - \(98.1 / 92.5\%\) ; state PVC- I - \(90.0 / 90.2\%\) ; state PVC- C - \(61.2 / 98.0\%\) . With a simplified binary scheme differentiating suction and normal states, both states were detected without error in data from the animal experiments, and with a sensitivity/specificity, for detecting suction, of \(99.2 / 98.3\%\) in the human patient data.

## I. INTRODUCTION

IMPLANTABLE rotary blood pumps (iRBPs) have proven to be a promising means of supporting the circulatory function in patients suffering heart failure. This is most often achieved by configuring the pump in parallel with the patient's native heart, as a left ventricular assist device (LVAD). However, the full potential of such devices may only be realized through the use of an effective control strategy such that an ambulant patient's metabolic demand for blood flow is met. A key requirement in realizing such a control strategy is the ability to discern with great accuracy, and indeed avoid, those pumping states which are potentially harmful to the patient. Such states include collapse of the ventricle due to over- pumping (ventricular suction), or pump back flow (regurgitation) as a result of under- pumping [1].

The identification of pumping states in iRBPs has received considerable attention in the scientific literature [2- 10]. Despite the use of implanted sensors by various

research groups [7], it is imperative that their use be avoided due to cost and reliability issues. Therefore, efforts to identify pumping states by a number of investigators [3- 6,8- 10] have focused on waveform analysis of the pump motor feedback signals (electric current or rotor speed), with a range of indices having been derived from these signals as indicators of either over- or under- pumping. Despite the success in deriving such indices, this research has, by and large, failed to deliver on the key challenge: the development of robust automated algorithms for detection of physiologically significant pumping states.

In this paper, we present an automated approach to the classification of significant pumping states, based on analysis of the non- invasive pump feedback signals. The approach, employing a classification and regression tree (CART), is developed and validated on data obtained from both animal and human recipients of the VentrAssist™ iRBP (Ventracer Ltd., Chatswood, Sydney, Australia). The technique described is shown to be accurate and robust in both scenarios and is therefore likely to be suitable for use in a sophisticated pump control strategy.

## II. METHODS

### A. Acute Animal Experiments

Six healthy pigs were instrumented and implanted with the VentrAssist iRBP. In each animal, the pump's inflow cannula was inserted at the apex of the left ventricle (LV) while the outflow cannula was anastomosed to the ascending aorta. Various cardiovascular parameters were recorded via invasive measurement (Fig.1). The non- invasive signals of pump impeller speed, motor current and supply voltage were also recorded for analysis. The transition between pumping states was induced by changes in pump target speed, which was adjusted in variable increments and within variable ranges - depending on the cardiovascular response of each animal - in order to produce the full range of pumping states.

### B. Pumping State Definitions

Examination of the invasive observers (aortic pressure (AoP), left ventricular pressure (LVP), pump inlet pressure \((\mathrm{P_{in}})\) , aortic flow \((\mathrm{Q_{a}})\) and pump flow \((\mathrm{Q_{p}})\) ) indicated the presence of five physiologically significant pumping states: regurgitant pump flow (PR), ventricular ejection (VE), aortic valve non- opening (ANO), and partial collapse (intermittent and continuous) of the ventricle wall during the cardiac cycle (PVC- I and PVC- C). These pumping states are illustrated in Fig. 1 - for detailed descriptions see [11]. Briefly, state PR is typified by negative (or regurgitant) \(\mathrm{Q_{p}}\) during diastole. The most desirable pumping state appeared

to be VE, where left ventricular ejection via the aortic valve occurred in systole and \(\mathrm{Q}_9\) remained positive throughout the cardiac cycle. State ANO occurs when the aortic valve remains closed over the cardiac cycle, and may occur due to decreased myocardial contractility, a relative increase in pump speed, or a decrease in left ventricular preload.

Partial collapse of the left ventricle is evidenced at relatively high pump speeds, and is characterised by transient obstruction of the pump inlet cannula as the volume of blood drawn from the LV exceeds that delivered to the heart from the pulmonary circulation. The effects of the respiration on cardiac behavior often cause partial collapse of the ventricle to occur intermittently (state PVC- I), that is, not every heartbeat but over a fraction of the respiratory cycle (when intrathoracic pressure exceeds LVP). State PVC- C is exhibited when a suction event occurs every cardiac cycle.

### C. Human Patient Data

Clinical data were obtained from 10 recipients of the VentrAssistTM iRBP, Surgery and monitoring was performed at The Alfred Hospital (Melbourne, Australia). As for the animal studies, the normal and suction states correlated roughly with pump speed set point. Typically, lower speed set points exhibited the normal pumping state and produced a relatively high level of pulsatility in the speed waveform - residual contractility of the native heart creates an oscillatory flow. As target speed is increased, the influence of the native heart declines and the speed pulsatility is generally reduced. At even higher speeds the suction state is induced.

### D. Identifying Pumping States

In the human patients it was not feasible to measure invasive parameters as in the acute animal experiments. As a result, the non- invasive parameter of speed was itself used to classify the human patient data into three states: normal, suction and equivocal. The equivocal state was assigned to data segments where the pumping state was uncertain, and was excluded in the subsequent analysis. Classification of data into these three states was aided by trans- oesophageal echocardiographic images of the aortic valve and by recording as assessed by an expert clinician experienced in pumping state identification.

### E. Non-invasive Observers of Flow Dynamics

Efforts to automate the classification of pumping states focused on waveform analysis of the speed feedback signal. This signal exhibits much of the flow dynamics present within the iRBP, which are in turn was affected by the behavior of the native heart. A number of indices derived from the speed waveform were employed to classify the pumping state, and have been described previously [11]. Briefly, these indices involved features such as amplitude, amplitude symmetry, temporal symmetry, and temporal rates of change in various parameters (Fig. 2). Analysis of the human patient data employed two additional indices: the proportion of speed samples in a given interval exceeding the midpoint of the maximum and either the minimum or mean speed values.

### F. The CART Statistical Method

The Classification and Regression Tree (CART) method is a binary decision tree algorithm [12] used to predict the

> **Image description.** A multi-panel line graph displaying physiological and mechanical data over a 20-second period, illustrating various pumping states. The graph is composed of three stacked panels, each with its own vertical axis but sharing a common horizontal time axis.
>
> **Common Elements:**
> *   **X-axis:** Time (s), ranging from 0 to 20 seconds.
> *   **Overall Layout:** The data is segmented into distinct operational states across the top panel, labeled PR, VE, Normal, ANO, PVC-I, Suction, and PVC-C.
>
> **Top Panel: Pressure (mmHg)**
> *   **Y-axis:** Pressure (mmHg), ranging from approximately -100 to 100.
> *   **Legend:** Identifies four lines: AoP (Aortic Pressure), LVP (Left Ventricular Pressure), AoFlow (Aortic Flow), and Pin (Pump Inlet Pressure).
> *   **Visual Data:** This panel shows highly fluctuating pressure waveforms. The lines exhibit sharp peaks and troughs, characteristic of cardiac cycles. The different states (e.g., PR, VE, Normal) correspond to specific patterns of these pressure fluctuations.
>
> **Middle Panel: Flow (L/min)**
> *   **Y-axis:** Flow (L/min), ranging from 0 to 20.
> *   **Legend:** Identifies two lines: Aortic Flow and Pump Flow.
> *   **Visual Data:** This panel displays the flow rates over time. Both the Aortic Flow and Pump Flow lines show pulsatile patterns, indicating the movement of blood through the system.
>
> **Bottom Panel: Pump Speed (rpm)**
> *   **Y-axis:** Pump Speed (rpm), ranging from 0 to 3000.
> *   **Visual Data:** This panel shows the speed of the pump. The line is generally high, fluctuating around a set point, with some variations corresponding to the different states shown in the top panel.
>
> The graph provides a comprehensive view of the interaction between pressure, flow, and pump speed across different operational modes of the VentrAssistTM iRBP device.

<center>Fig. 1. A summary of the invasive (aortic pressure (AoP), left ventricular pressure (LVP), pump inlet pressure \((\mathrm{P}_{\mathrm{in}})\) , aortic flow \((\mathrm{Q}_{\mathrm{a}})\) and pump flow \((\mathrm{Q}_{\mathrm{p}})\) and non-invasive (speed and current) signals recorded from one animal with the iRBP at five different average speed set points, demonstrating the five pumping states from PR when under-pumping to PVC-C when over-pumping. Aortic pressures and flows were measured downstream of the outlet cannula. </center>

> **Image description.** A multi-panel time-series line graph illustrating five non-invasive state detection indices derived from a pump speed signal, comparing data from a "Normal" state (0-6 seconds) and a "Suction" state (6-10 seconds).
>
> The overall figure is structured with five stacked subplots, all sharing a common horizontal X-axis labeled "Time (s)," which spans from 0 to 10 seconds. The data in each subplot represents a different derived index, with the transition from the Normal state to the Suction state occurring sharply at approximately 6 seconds.
>
> The five indices are presented from top to bottom:
>
> 1.  **$N_{pp}$ Pump Speed (rpm):** This top panel shows the raw pump speed. In the Normal state (0-6s), the speed fluctuates rhythmically around 2500 rpm. At 6 seconds, the speed drops significantly and becomes more erratic in the Suction state (6-10s).
> 2.  **$\Delta N_{pp}$ (rpm):** This panel tracks the change in pump speed. During the Normal state, the values fluctuate close to zero. In the Suction state, the values show a clear, sustained downward shift.
> 3.  **$N_{pp}$ Profile:** This index displays a processed version of the pump speed waveform. The waveform in the Normal state is characterized by a specific, high-amplitude pattern, which changes shape and amplitude dramatically when the Suction state begins at 6 seconds.
> 4.  **$\Delta N_{pp}$ Profile:** Similar to the previous panel, this index shows the change in the profile. It exhibits a distinct change in the shape and magnitude of the waveform at the 6-second mark.
> 5.  **$N_{sarp}$:** This final panel shows a derived index. In the Normal state, the values are relatively low and fluctuate. At 6 seconds, the $N_{sarp}$ index shows a sharp, sustained increase, indicating a significant change in the detected state.
>
> The visual evidence across all five indices consistently demonstrates a clear and abrupt transition at the 6-second mark, distinguishing the physiological characteristics of the Normal pumping state from the Suction state.

<center>Fig. 2. Example of the non-invasive state detection indices derived from the pump speed signal [11], using human patient data classified into the normal and suction states. </center>

class membership of a categorical dependent variable, based on one or more predictor variables. Given the variability of the indices extracted from the pump speed signal, and the associated skew in its distribution, the CART approach provides an appropriate method for solving the problem at hand. The indices described above formed the basis for the CART predictor variables used in the analysis, while the pumping state provided the categorical dependent variable.

With respect to discerning between normal and suction pumping states, both possible types of misclassification could precipitate clinically significant consequences. While false- negatives (suction events classified as normal) may result in myocardial damage, hemolysis, or lack of perfusion, false- positives may lead to an unnecessary speed reduction by a control system aiming to alleviate the effect of suction. The CART method allowed a symmetrical cost structure to be devised such that the sensitivities of classifying both normal and suction states were comparable.

## G. Treatment of Data

In the analysis of both the animal and human patient data, data from half the total number of subjects were pooled for use as a training set. The Matlab Statistical Toolbox (Mathworks, Inc., MA, USA) was then employed to build an initial classification tree from this training set. A ten- fold cross- validation was then performed on this set to estimate the true error for trees of various sizes. The optimal tree was determined to be the simplest tree (i.e., the tree of smallest size) whose estimated error lay within one standard error of the minimum estimated error. This optimal tree was then

validated on the remaining data sets. It should be noted that there was insufficient data corresponding to the PR state to allow inclusion of this state in the analysis.

## III. RESULTS

Performance of the state detection method was assessed by a comparison of the state ascertained by the optimal tree and the known' state determined via invasive measurement (for the animal experiments) or via expert opinion (for the human patients). The sensitivity and specificity associated with each state were used to quantify the system's performance. After analyzing a range of window lengths over which to classify the data, a length of 6s was deemed most suitable, considering the need to balance the tradeoff between accuracy and resolution.

Results based on data from the acute animal experiments (Table I) indicate the high level of accuracy achieved in correctly identifying most pumping states. Perhaps the only questionable state in this regard was PVC- C, with a sensitivity of \(61.2\%\) . However, when considered together with PVC- I as one suction state, the sensitivity increases to \(100\%\) , indicating that the lack of accuracy was due to misclassification between these two suction states (rather than the normal states). When a simplified binary scheme is evaluated (i.e., when only two initial states, suction and normal, are considered), sensitivities of \(100\%\) were attained for both the normal and suction states - an ideal result.

TABLE I. RESULTS OF PUMPING STATE CLASSIFICATION ALGORITHM FOR PORCINE DATA. THE FIRST COLUMN REFERS TO THE NUMBER OF PUMPING STATES USED AS PART OF THE DEPENDENT VARIABLE FOR THE CART ANALYSIS: ALL FOUR STATES (VE, ANO, PVC-I, PVC-C) WERE USED INITIALLY; STATES PVC-I AND PVC-C WERE THEN COMBINED TO FORM THE SUCTION STATE, THUS PROVIDING THREE STATES FOR TREE-BUILDING; FINALLY, STATES VE AND ANO WERE COMBINED TO FORM THE NORMAL STATE, PROVIDING TWO STATES FOR THE ANALYSIS. STATISTICS WERE ALSO INCLUDED FOR THE SUCTION AND NORMAL STATES FOR EVERY GROUP OF RESULTS (EACH GROUP HAVING THE SAME NUMBER OF INITIAL STATES). FOR EXAMPLE, THE NORMAL RESULTS WITH FOUR INITIAL STATES ARE FOUND BY TREATING VE AND ANO AS A SINGLE STATE.

| No. of Initial States | State | Correct | Total | Sensitivity (%) | Specificity (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4 | VE | 175 | 200 | 87.5 | 100.0 |
| 4 | ANO | 52 | 53 | 98.1 | 92.5 |
| 4 | PVC-I | 45 | 50 | 90.0 | 90.2 |
| 4 | PVC-C | 52 | 85 | 61.2 | 98.0 |
| 4 | Normal | 252 | 253 | 99.6 | 100.0 |
| 3 | Suction | 135 | 135 | 100.0 | 99.6 |
| 3 | VE | 184 | 200 | 92.0 | 100.0 |
| 3 | ANO | 52 | 53 | 98.1 | 95.2 |
| 2 | Normal | 252 | 253 | 99.6 | 100.0 |
| 2 | Suction | 135 | 135 | 100.0 | 99.6 |
| 2 | Normal | 253 | 253 | 100.0 | 100.0 |
| 2 | Suction | 135 | 135 | 100.0 | 100.0 |

TABLE II. STATISTICAL SUMMARY OF THE PUMPING STATE CLASSIFICATION ALGORITHM FOR CLINICAL DATA, ACROSS ALL 10 PATIENTS.

| State | Correct | Total | Sensitivity (%) | Specificity (%) |
| :--- | :--- | :--- | :--- | :--- |
| Normal | 11875 | 12081 | 98.3 | 99.2 |
| Suction | 959 | 967 | 99.2 | 98.3 |

Excellent results were also obtained based on clinical data from the human patients. Using a large corpus of patient data - 12081 records for the normal state, and 967 records for the suction state - suction events were classified with a sensitivity of \(99.2\%\) and specificity of \(98.3\%\) (Table II).

## IV. DISCUSSION

Variability between patients, and even within a single patient over time, presents a significant challenge to the development of robust pumping state detection algorithms. Individuals suffering heart failure typically exhibit a wide range of severity in their condition, often with unique cardiovascular characteristics such as: residual ventricular contractility, systemic resistance, and blood pressure level. These characteristics ultimately determine the nature of the interaction between the iRBP and the patient's native heart. As a result of this interaction and the inherent physiological variability, any indices derived from the non- invasive pump signals exhibit a concomitant level of variability in both their temporal dynamics and their global statistics. Any automated pumping state classification system must perform in the face of this variability and preferably, without the need for patient- specific calibration.

In this regard, the classification scheme described in this paper is particularly encouraging, achieving a high level of accuracy when classifying pumping states for both the animal and clinical data. This success is likely due to the use of a combination of speed- derived indices, and their integration into the CART model. It is also interesting to note that these indices were considered independently of the patient. As a result, the classifiers developed purport to be extremely robust, obviating the need for a patient- specific calibration procedure to account for physiological variation.

In comparison to other related studies, the present results indicate superior performance. Amin et al. [2] employed a match filter approach whereby the pump current signal was compared to reference waveforms. Accuracies of over \(90\%\) were achieved when classifying data into four physiological states (including suction), however these results were based on very limited data (42 data segments of 6s each). The University of Pittsburgh group have developed an array of suction indices based on current and flow estimates [8, 9]. Their highest reported accuracy is \(80\%\) correct detection of suction events, with this limited success due to a weakness in flow estimation when nearing suction. The only clinical study comparable to the present work was conducted by Voigt et al. [10], in which the current signal was used to classify suction with \(89\%\) sensitivity (16/18 snapshots, each 5s in length) and \(96\%\) specificity (136/141 snapshots).  

There exists an inherent difference in the behavior of the native heart when comparing animal and human subjects. While the animals possess relatively healthy cardiac function, human implant recipients are suffering with a failed LV. The ventricular dynamics exhibited by patients will thus produce pump signal waveforms with different features to the healthy animal subjects, and in turn will influence the non- invasive indices upon which the classification system is based. In light of this, the approach to pumping state classification described here is evidently rather robust.

In examining the results for detecting suction versus normal states, the superior performance in the animal data (as compared with the patient data) is perhaps largely due to the wide variation in cardiac condition and dynamics observed in the human patients, and the consequent disparity in suction detection indices. Furthermore, there was a larger corpus of data available relating to the human trials (10 patients; 13048 records) than was available for the acute animal studies (6 animals; 388 records). Nevertheless, the performance of the classifier, even in the face of significant variability inherent in the data from human patients, is impressive, testifying to the suitability of the approach and the robustness of the resulting algorithms.

## V. CONCLUSION

The ability to anticipate and detect the onset of ventricular collapse (suction) is a major objective in the area of iRBP control. In this paper we have described a system for automatically classifying physiologically significant pumping states in an iRBP configured as a LVAD. The presented results, obtained using this technique, in both acute animal experiments as well as human patient trials, demonstrated a high level of success in accomplishing this task.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
