```
@article{karantonis2007classification,
  title={Classification of Physiologically Significant Pumping States in an Implantable Rotary Blood Pump: Patient Trial Results},
  author={Dean M. Karantonis and David G. Mason and Robert F. Salamonsen and Peter J. Ayre and Shaun L. Cloherty and Nigel H. Lovell},
  journal={ASAIO Journal},
  year={2007},
  volume={53},
  number={5},
  pages={617-622},
  doi={10.1097/mat.0b013e318147e6a9},
  url={https://www.ovid.com/jnls/asaiojournal/abstract/10.1097/mat.0b013e318147e6a9~classification-of-physiologically-significant-pumping-states}
}
```

---

# Classification of Physiologically Significant Pumping States in an Implantable Rotary Blood Pump: Patient Trial Results

Dean M. Karantonis,\\*+ David G. Mason, Robert F. Salamonsen, Peter J. Ayre, Shaun L. Cloherty, \\* and Nigel H. Lovell\\*

An integral component in the development of a control strategy for implantable rotary blood pumps is the task of reliably detecting the occurrence of left ventricular collapse due to overpumping of the native heart. Using the noninvasive pump feedback signal of impeller speed, an approach to distinguish between overpumping (or ventricular collapse) and the normal pumping state has been developed. Noninvasive pump signals from 10 human pump recipients were collected, and the pumping state was categorized as either normal or suction, based on expert opinion aided by transesophageal echocardiographic images. A number of indices derived from the pump speed waveform were incorporated into a classification and regression tree model, which acted as the pumping state classifier. When validating the model on 12,990 segments of unseen data, this methodology yielded a peak sensitivity/ specificity for detecting suction of \(99.11\% /98.76\%\) . After performing a 10- fold cross- validation on all of the available data, a minimum estimated error of \(0.53\%\) was achieved. The results presented suggest that techniques for pumping state detection, previously investigated in preliminary in vivo studies, are applicable and sufficient for use in the clinical environment. ASAIO Journal 2007; 53:617- 622.

Implantable rotary blood pumps (iRBPs) acting as left ventricular assist devices are proving to be an effective method of supporting the circulatory function in patients with heart failure. Achieving an effective control strategy for iRBPs, such that a recipient's metabolic demand for blood flow is optimized, is crucial to improving the quality of life for these individuals. To achieve such a control strategy, one of the necessary requirements is the ability to discern with great accuracy those pumping states that are potentially harmful to the recipient, such as collapse of the ventricle due to overpumping (ventricular suction) or pump backflow (regurgitation) as a result of underpumping. The noninvasive detection of ventricular suction is examined in the present study.

A number of research teams are currently engaged in activities relating to the identification of pumping states in iRBPs.2- 12 These efforts have predominantly involved waveform analysis of noninvasive pump feedback signals (electrical current or impeller speed), whereas some groups.12 have used invasive sensors to aid in this process. Various authors have derived a number of useful indices from the noninvasive pump signals that serve as indicators of either overpumping or underpumping of the heart.3- 8,10 Most groups, however, fall short of developing automated state detection algorithms and thus do not provide a statistical assessment of their experimental results.5- 7,10

Interpatient variation is another significant issue requiring consideration. Individuals with heart failure exhibit a wide range of severity in their condition, with residual contractility, blood pressure level, cardiac filling pressures and other cardiovascular characteristics influencing the interaction of the iRBP with their native heart. As a result, the nature of any indices associated with different pumping states will differ to varying degrees according to each patient. Ideally, a classification system should have the ability to operate independently of the patient—that is, patient- specific calibration tasks should not be required.

A previous study by the present authors, using data from healthy animals,13 demonstrated that by using only the noninvasive measure of instantaneous pump impeller speed to assess flow dynamics, it is possible to detect a range of pump states, including ventricular ejection, aortic valve not opening over the entire cardiac cycle, and partial collapse of the ventricle wall during the cardiac cycle. The work herein describes the application of a Classification And Regression Tree (CART) to distinguish between normal and suction pumping states, based on data acquired from human recipients of the VentrAssist Left Ventricular Assist System (LVAS) (Ventracor Ltd., Chatswood, Sydney, Australia).

## Methods

## Data Acquisition

Pump and physiological parameters were recorded in 10 patients implanted with the VentrAssist iRBP (Figure 1). Patients were located in the Intensive Care Unit of The Alfred Hospital, Melbourne, Australia, and were closely monitored by medical staff at all times to ensure their safety during this procedure. An institutional ethics committee was consulted to obtain the necessary ethical regulatory approval (ethics application 89/06: Exercise hemodynamics in patients with left ventricular assist devices and the need for a physiological controller). For each patient, the noninvasive observer of instantaneous pump impeller speed was monitored via interro

> **Image description.** A technical diagram illustrating the connection of a left ventricular assist device (LVAD) to a stylized human torso. The figure is shown from the front, depicting the placement of various medical components and tubing.
>
> The diagram is titled "Figure 1. Diagram of the left ventricular assist device connection to the patient's native heart." Below the main illustration, a detailed caption explains the function of each numbered component.
>
> The central illustration shows a simplified human figure with several components attached:
>
> *   **Native Heart (1):** Located in the upper chest area, this represents the patient's native heart, which is not removed during the procedure.
> *   **Inflow Cannula (2):** A short tube is shown attached to the left ventricle (near the heart), representing the inflow cannula that draws blood from the failing heart into the assist device.
> *   **Outflow Cannula (3):** Another tube is shown exiting the chest area, representing the outflow cannula that returns the blood to the ascending aorta.
> *   **Percutaneous Lead (4):** A lead is shown exiting the right side of the abdomen below the ribs, indicating the percutaneous connection.
> *   **External Controller/Pump (5):** A gray, box-like device is positioned in the lower abdomen, representing the pump unit that connects to the external controller and batteries.
>
> The accompanying text provides a detailed breakdown of these elements:
> *   (1) The native heart is not removed.
> *   (2) A short inflow cannula is attached to the left ventricle, which delivers blood from the failing heart into the VentrAssist iRBP.
> *   (3) The outflow cannula returns blood to the ascending aorta.
> *   (4) The percutaneous lead exits from the right side of the abdomen below the ribs.
> *   (5) This connects the pump to the external controller and batteries.

<center>Figure 1. Diagram of the left ventricular assist device connection to the patient's native heart. (1) The native heart is not removed. (2) A short inflow cannula is attached to the left ventricle, which delivers blood from the failing heart into the VentrAssist iRBP. (3) The outflow cannula returns blood to the ascending aorta. (4) The percutaneous lead exits from the right side of the abdomen below the ribs. (5) This connects the pump to the external controller and batteries. </center>

gation of the percutaneous controller lead and recorded for analysis. A Powerlab data acquisition system (AD Instruments, Castle Hill, NSW, Australia) was used to record all the aforementioned signals at a sampling rate of \(400\mathrm{Hz}\) .

In each patient, the transition between normal and suction states was induced by changes in set point for average pump speed. Pump speed was adjusted in variable increments and within variable ranges, depending on the cardiovascular response given by each patient, to generate the full range of pumping states. Typically, lower- speed set points lend themselves to the normal state and produce a relatively higher level of pulsatility in the speed waveform as the native heartbeat creates an oscillatory flow. As speed increases and the pump's level of assistance rises, left ventricular preload is reduced. The Starling mechanism then dictates that the contractility of the native heartbeat declines and hence the pulsatility in the speed waveform decreases. Further speed rises will eventually induce a state of suction in the left ventricle as the volume of blood drawn from the ventricular chamber is increased to a level at which pulmonary supply cannot meet pump demand. Suction is most likely to occur at end- systole, the point in the cardiac cycle at which the left ventricle chamber is of minimum size. When the pump's demand for flow induces a negative left ventricular pressure sufficiently below the intrathoracic pressure, the ventricle is forced to collapse. Due to the potentially negative consequences of ventricular suction, the pump speed was promptly reduced once suction was observed.

## Identifying Pumping States  

A previous study by the present authors,13 involving acute porcine experiments, identified a range of significant pumping states via inspection of invasive cardiovascular parameters (e.g., left ventricular pressure, aortic flow). In the present study, however, it was infeasible to measure such invasive parameters due to the risk posed to patients by the necessary invasive instrumentation. Thus, the process of identifying pumping states was performed with the aid of transesophageal echocardiographic images of the aortic valve and left ventricle, together with an examination of the speed waveform. An expert clinician experienced in pumping state identification classified the data into three states: normal, suction, and equivocal. Whereas the normal and suction states have already been discussed, the equivocal state is simply used to assign data where the pumping state is uncertain. In the subsequent analysis, the equivocal data was excluded.

## Noninvasive Observers and CART Statistical Method

Classification and Regression Tree is a binary decision tree algorithm \(^{14}\) used to predict membership of cases in the classes of a categorical dependent variable from their measurements of one or more predictor variables. Considering the intersubject variation of the information extracted from the speed signal and the associated skew in its distribution, the CART approach provided the most appropriate method for dealing with the problem of classifying pumping state based on the noninvasive observers. Furthermore, the computational cost of implementing the CART algorithm is very low, especially in comparison to other approaches such as neural networks.

A number of indices derived from speed waveform features formed the basis for the predictor values used in the CART analysis, whereas the pumping state provided the categorical dependent variable. These indices have been described previously, thus precluding a thorough discussion here. \(^{13}\) In brief, these indices involved waveform features such as amplitude, amplitude symmetry about an average value, symmetry in the time domain, and rates of change in various parameters. Investigation of the clinical data involved the use of two additional indices: the proportion of speed samples in the speed cycle (roughly equivalent to a cardiac cycle) exceeding the midpoint of the maximum and minimum speed values; and the proportion of speed samples in the speed cycle exceeding the midpoint of the maximum and mean speed values. Subsequent to the recorded data being classified, it was further segmented to ensure the transition periods between target speed values were excluded. The CART predictor values were then calculated for each patient data set.

With respect to detecting suction, both types of misclassification (a false- negative occurring when a suction event is classified as normal, and a false- positive occurring when a nonsuction event is classified as suction) incur clinically significant consequences. Whereas false- negatives may result in myocardial damage, hemolysis, or lack of perfusion, false- positives may lead to an unnecessary speed reduction by a control facility aiming to alleviate the effect of suction. CART analysis allows the accuracies of both types of misclassification to be optimized via a differential cost structure, whereby variable costs can be individually imposed on the full range of misclassifications. Since there were more data points in the normal than the suction category, there is a statistical tendency to attribute greater importance to the correct classification of the normal state. During the analysis, greater cost was imposed

on the misclassification of suction events to ensure the sensitivities of classifying normal and suction states were comparable.

## Treatment of Data

Two different approaches were taken when developing the CART models. The first, more conventional approach, involved using data from half the total number of patients as a training set to construct the initial classification tree. As this initial tree tends to overfit the training sample, it was pruned such that the resultant tree had a depth of up to five levels. In this way, the tree attains a simplified structure with a greater ability to correctly classify new data. This pruned tree was then validated on the remainder of the data.

In the second approach, the entire data pool was used as a training set, and following a pruning procedure similar to that described above, the pruned tree was then validated on all the available data. Additionally, a 10- fold cross- validation \(^{15}\) was performed on the whole data pool to estimate the expected performance of the classifier on previously unseen data. Here the data were split into 10 subsamples of roughly equal size, with nine of these subsamples used for training and the remaining sample used for validation. This process of training and validating was repeated 10 times with different subsamples, after which the errors associated with each testing phase were averaged to determine an estimate of the error incurred when applying the classifier on new data.

A number of window lengths—that is, the time interval over which the state classification was based—were examined, with a view toward optimizing both classification accuracy and temporal resolution. Temporal resolution directly relates to the responsiveness of the classifier and its ability to describe a given time interval (in terms of the sequence of states present) in greater detail. Both responsiveness and accuracy are clinically important attributes, especially when the classifier is to be used in a speed control facility.

## Results

As mentioned, the waveform features extracted from the speed signal form the basis of the CART input parameters. A sample of these indices for one patient, exhibiting both normal and suction pumping states, is given in Figure 2. \(^{13}\) using human patient data classified into the normal and suction states. The magnitude and nature of the deviations between states are clearly evident, and similar properties were observed in data samples of the remaining patients.

Performance of the classification scheme was evaluated by a comparison of the state ascertained by the CART analysis and the "known" state determined via expert opinion with the aid of transesophageal echocardiographic images. The sensitivity and specificity associated with each state were used to quantify the system's performance.

Results for the first approach—whereby a pruned classification tree, trained with half the available data, was validated on the remaining data—indicate a high level of accuracy was achieved in distinguishing normal and suction states (Table 1). Furthermore, the sensitivities across varying window lengths are also comparable. This suggests that the combination of indices used in the CART model is able to identify suction independent of the time interval over which the classification decision is made.

With respect to the second approach, in which a pruned classification tree, trained with all available data, was validated on the entire corpus of data, the results again indicate a high level of performance across all window lengths (Table 2). The estimated error rate (cross- validation error estimate in Table 2) in classifying new data with the classification tree trained on the complete data set is encouraging, with a maximum of \(1.76\%\) for a 2- second window and a minimum of \(0.53\%\) for a 5- second window length.

If the results of the two approaches are compared, it is evident that a significant increase in accuracy is given by the second approach, in which the entire data set is used for training and validation. However, considering the results are derived from a pruned tree that was trained on the same data set, rather than unseen data, this outcome is expected.

In light of these results, it is interesting to observe the interpatient variability encountered when compiling the set of CART predictor values. Figure 3 presents the statistical spread of each predictor variable across all patients, in the form of box- and- whisker plots. The fact that no single predictor clearly discriminates suction from the normal state serves to exemplify the ability of the CART model to accommodate such variation in its task of pumping state classification.

## Discussion

Research into the detection of pumping states is currently being investigated by a number of groups around the world. The majority of the reports in the literature to date have demonstrated the use of various state detection indices based on in vitro (mock circulatory loop) and in vivo animal experimentation. The team from Yamagata University \(^{10}\) was able to detect suction or regurgitation, based on the so- called waveform deformation index (WDI), given by the ratio of the fundamental component of the speed waveform power spectral density (PSD) to the higher frequency components. In both in vitro and animal studies, they were able to visually determine which of these two undesirable states was occurring by reference to a graph of WDI against speed. Oshikawa et al. \(^{6}\) and Endo et al., \(^{5}\) from Miyazaki Medical College, were able to identify the transition to total assist of the native heart (the "t- point") and the transition to suction (the "s- point") by using the index of current amplitude (ICA = \([(I_{\mathrm{max}} - I_{\mathrm{min}}) / I_{\mathrm{mean}}]\) ). In performing animal studies to ascertain the typical values of these critical points, the variation between subjects was found to be significant, and it was conceded that a per- patient calibration procedure would be required in the postoperative phase to ensure the validity of these points in detecting total assist and suction. Another valuable index of suction ( \(I_{\mathrm{s}} = \mathrm{LPF}[(I_{\mathrm{mean}} - I_{\mathrm{min}}) / (I_{\mathrm{max}} - I_{\mathrm{min}})]\) ; LPF = low- pass filter) was reported by Tanaka et al.; however, the in vivo study that was conducted made no discussion of interanimal variation in the index.

A number of other studies \(^{2 - 4,12}\) have provided an indication of the performance of their methods in correctly identifying suction in in vivo animal data. Amin et al. \(^{2}\) used a matched filter approach in which the pump current waveform was compared with reference waveforms. This technique provided accuracies of over \(90\%\) when classifying data into four physiological states (including suction). However, this study was based on a limited corpus of data (42 data segments of 6 seconds each). The research group from the University of

> **Image description.** A complex figure consisting of two side-by-side panels, each containing a series of line graphs, illustrating noninvasive state detection indices derived from a pump speed signal. The figure is titled "Noninvasive Indices" and compares data from two distinct states: "Normal" (left panel) and "Suction" (right panel).
>
> The overall structure features a shared horizontal X-axis labeled "Time (s)," ranging from 0 to 5 seconds, spanning both panels. The Y-axis labels for each row represent various derived indices, primarily denoted by $\Delta N_{pp}$ (e.g., $\Delta N_{pp}$, $\Delta N_{pp}$, $\Delta N_{pp}$, etc.), with the top row specifically labeled "Pump Speed."
>
> **Normal State Panel (Left):**
> This panel displays signals characteristic of a stable, normal operating state.
> *   **Pump Speed:** The top graph shows a clear, consistent, periodic wave pattern, fluctuating smoothly between approximately 1900 and 2000 RPM.
> *   **Indices ($\Delta N_{pp}$):** The subsequent graphs show signals that are generally stable, exhibiting gentle oscillations or remaining relatively flat, indicating consistent, predictable behavior over the 5-second period.
>
> **Suction State Panel (Right):**
> This panel displays signals characteristic of the suction state, showing abrupt changes and instability.
> *   **Pump Speed:** The top graph shows a sudden shift in the signal pattern, fluctuating around 2700 to 2900 RPM, with less consistent periodicity compared to the Normal state.
> *   **Indices ($\Delta N_{pp}$):** The remaining graphs in this panel exhibit sharp, step-like changes or rapid, high-frequency fluctuations. Many of these indices show distinct vertical jumps (step functions) at specific points in time, indicating sudden transitions or erratic behavior associated with the suction event.
>
> In summary, the figure visually contrasts the smooth, periodic, and stable signals observed in the "Normal" state with the sharp, step-like, and erratic signals observed in the "Suction" state across multiple derived noninvasive indices.

<center>Figure 2. Example of the noninvasive state detection indices derived from the pump speed signal using human patient data classified into the normal and sunction states. </center>

Pittsburgh have reported on a number of studies \(^{3,4}\) in which an array of indices based on current and flow estimates were utilized in an effort to identify suction. The highest reported accuracy in these studies was \(80\%\) correct detection of suction

events, \(^{4}\) which was attributed to a weakness in flow estimation when nearing suction. A more recent study from the same group \(^{12}\) used a discriminant analysis model applied to various indices derived from the pump flow signal. In this study, data

Table 1. Statistical Summary of the First Approach to Pumping State Classification, Over a Series of Window Lengths

| Window Length (s) | State | Correct | Total | Sensitivity (%) | Specificity (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2 | Normal | 12,366 | 12,566 | 98.41 | 98.67 |
| 2 | Suction | 813 | 824 | 98.67 | 98.41 |
| 3 | Normal | 12,309 | 12,440 | 98.95 | 97.99 |
| 3 | Suction | 732 | 747 | 97.99 | 98.95 |
| 4 | Normal | 12,161 | 12,316 | 98.76 | 99.11 |
| 4 | Suction | 668 | 674 | 99.11 | 98.76 |
| 5 | Normal | 12,024 | 12,213 | 98.45 | 98.87 |
| 5 | Suction | 611 | 618 | 98.87 | 98.45 |
| 6 | Normal | 11,875 | 12,081 | 98.29 | 99.17 |
| 6 | Suction | 959 | 967 | 99.17 | 98.29 |

These results were obtained after validating a pruned classification tree, trained with half the available data, on the remaining data.

Table 2. Statistical Summary of the Second Approach to Pumping State Classification, Over a Series of Window Lengths

| Window Length (s) | State | Correct | Total | Sensitivity (%) | Specificity (%) | CV Error Estimate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2 | Normal | 30,091 | 30,353 | 99.14 | 99.26 | 1.76 |
| 2 | Suction | 1619 | 1631 | 99.26 | 99.14 | 3 |
| 3 | Normal | 29,940 | 30,101 | 99.47 | 99.47 | 0.73 |
| 3 | Suction | 1515 | 1523 | 99.47 | 99.47 | 4 |
| 4 | Normal | 29,645 | 29,855 | 99.30 | 99.86 | 0.82 |
| 4 | Suction | 1420 | 1422 | 99.86 | 99.30 | 5 |
| 5 | Normal | 29,467 | 29,599 | 99.55 | 99.70 | 0.53 |
| 5 | Suction | 1332 | 1336 | 99.70 | 99.55 | 6 |
| 6 | Normal | 29,199 | 29,358 | 99.46 | 99.76 | 0.65 |
| 6 | Suction | 1672 | 1676 | 99.76 | 99.46 | |

These results were obtained after validating a pruned classification tree, trained with all available data, on the entire data set. The cross-validation (CV) error estimate refers to an estimate of the error incurred when applying the classifier on new data.

categorized as either "moderate" or "severe" suction were detected with sensitivity and specificity of \(94.0\%\) (591 of 629 samples, each 5 seconds in duration) and \(70.0\%\) (1193 of 1706 samples), respectively.  

The state detection indices proposed by the abovementioned groups form a platform for further research, being based on in vitro and in vivo animal experimentation. It is imperative, however, that any pumping state detection system for iRBP recipients must be based on clinical data from human patients with heart failure. The myocardial physiology and associated flow dynamics of a failing heart are difficult to simulate in in vitro mock loop setups or in in vivo animal experiments, since the animals in use generally have healthy cardiovascular systems and current animal models of heart failure have severe limitations. At the time of writing, the only clinical data analysis reported in the literature is that from the University of Vienna, in conjunction with MicroMed Technology (Houston, TX). This study used data from 100 recipients of an axial iRBP.9 Based on these data (ten 5- sond snapshots per patient), which, notably, included an invasive measurement of pump flow from an implanted flow sensor, the investigators developed a range of indices for suction detection. Their algorithm achieved sensitivity and specificity of \(95\%\) and \(99.5\%\) , respectively, for data classified by experts as "certainly" suction. In a more recent study using this same technique, Vollkron et al.11 reported results of 5 false- positives (from a group of 831 snapshots classified expertly as "certainly" or "most probably" no suction) and 18 false- negatives (from a group of 225 snapshots

> **Image description.** A complex, multi-panel technical figure titled "Figure 3," which presents an interpatient comparison of various CART predictor variables derived from a pump speed signal. The figure is structured as a grid of box plots, organized into three main columns representing different pumping states and six rows representing specific predictor variables.
>
> **Overall Structure and Layout:**
> The figure is divided into three vertical panels (columns) and six horizontal rows.
> 1.  **Columns (Pumping States):**
>     *   The leftmost column is labeled "Normal."
>     *   The middle column is labeled "Suction."
>     *   The rightmost column is labeled "Normal Suction."
> 2.  **Rows (CART Predictors):**
>     *   The six rows represent different CART Predictors, listed vertically on the left side of the figure.
> 3.  **X-Axis:**
>     *   The horizontal axis at the bottom is labeled "Patient Number," with numerical labels 1 through 10 visible beneath each of the three columns.
> 4.  **Y-Axis:**
>     *   The vertical axis on the left is labeled "CART Predictor." Each row has a specific label indicating the variable being measured.
>
> **Detailed Predictor Variables (Rows):**
> The six CART Predictors, listed from top to bottom, are:
> *   $\Delta N_{pp}$ (pp)
> *   $\Delta N_{max}$ (pp)
> *   $\Delta N_{profile}$ (pp)
> *   $\Delta N_{req}$ (pp)
> *   $\Delta N_{mean}$ (pp)
> *   $N_{mean}$
>
> **Data Visualization (Box Plots):**
> Each individual plot is a box plot, illustrating the distribution of a specific predictor for a given patient within a specific pumping state.
> *   The box within each plot represents the interquartile range (IQR).
> *   A horizontal line inside the box indicates the median value.
> *   Whiskers extend from the box to show the range of the data.
> *   Individual data points (outliers) are visible as small dots in several plots.
> *   The distributions vary significantly across patients and across the different predictor types. For instance, the range of $\Delta N_{pp}$ (top row) is generally much wider than the range of $N_{mean}$ (bottom row).
>
> **Text and Caption:**
> The caption at the bottom of the figure reads: "Figure 3. An interpatient comparison of the CART predictor variables derived from the pump speed signal. From left to right, there appears..." (The caption is truncated).
>
> The visual presentation is consistent across all three state columns, allowing for a direct comparison of how the distribution of each CART predictor changes between "Normal," "Suction," and "Normal Suction" states across ten different patients.

<center>Figure 3. An interpatient comparison of the CART predictor variables derived from the pump speed signal. From left to right, there appears data from the normal state, the suction state, and a comparison between these states for the full complement of data. Each plot is a box-and-whisker plot, with the whiskers extending to at most 1.5 times the interquartile range. All outliers have been omitted for the purpose of clarity. This figure illustrates the interpatient variability of the CART predictors and thus the ability of the CART methodology to accommodate such variation in its task of pumping state classification. </center>

classified expertly as "certainly" or "most probably" suction), equating to a sensitivity and specificity, for all suction events, of \(92\%\) and \(99.4\%\) , respectively. Although these results represent a considerable improvement in specificity, it is undesirable to incorporate invasive sensors such as the flow probe, used in the MicroMed pump, into the iRBP, as they considerably reduce system reliability and increase cost. In view of this, a clinical study by Voigt et al.8 used only the noninvasive pump current signal to classify suction with \(89\%\) sensitivity (16 of 18 snapshots) and \(96\%\) specificity (136 of 141 snapshots).

As noted above, interpatient and intrapatient variability presents a significant challenge to the development of robust pumping state detection algorithms. Patients with heart failure typically have a range of issues related to their compromised circulatory pumping capacity. Reduced residual contractility, increased filling pressures, and changes in blood pressure all affect the nature of the interaction between the iRBP and the patient's native heart. As a result of this interaction and the inherent physiological variability, any indices derived from the noninvasive pump signals exhibit a concomitant level of variability. Given this level of variability, the derivation of an automated pumping state classification system that does not require the need for patient- specific calibration is a nontrivial task. An interpatient comparison of the CART predictor variables used in this analysis indeed demonstrates such variation between patients (Figure 3). When comparing the normal and suction states for all patients, the spread of data for each variable is such that a clear separation cannot be made between pumping states. The accuracy of the final results then confirms that the CART methodology has the ability to accommodate for the observed variations in input variables when creating a suitable classification tree.

The high level of accuracy achieved in this study, when classifying pumping states based on clinical data, is greatly promising. Using a combination of indices derived from the noninvasive speed signal and integrating them into a CART model evidently results in an effective and robust state detection system. The success of the present study, relative to those of other groups, may be due, at least in part, to the nature of the speed waveform produced by the VentAssist iRBP. This waveform is inherently different and more informative than that produced by other pumps.2,7,8 Specifically, the unique mechanical design of the VentAssist iRBP,16 together with the response characteristic of the speed control system, results in a close relationship between left ventricular and pump impeller dynamics. The waveform produced by this interaction is exploited to develop a suction detection mechanism whose performance surpasses that of most prior studies. Furthermore, since the waveform parameters used in the present study were considered independent of the patients, there is no requirement for a calibration procedure to account for intersubject differences.  

A previous paper by the authors13 using data from acute animal studies presented results for correctly identifying the suction state with \(100\%\) sensitivity and specificity. This superior performance, as compared with that reported here, is perhaps largely due to the wide variation in cardiac condition and dynamics observed in the human patients and the consequent disparity in suction detection indices. Nevertheless, the performance of the classifier, even in the face of significant variability inherent in the data from human patients, is encouraging, testifying to the suitability of the approach and the robustness of the resulting algorithms.

## Conclusion

Dynamically adapting pump speed to achieve optimal systemic perfusion is the ultimate goal for iRBP development. Reliable detection of ventricular collapse, or the suction pumping state, is likely to form an integral component of any pump control algorithm devised to achieve this end. Therefore, the pumping state classification scheme described in this study, using the CART methodology and based on the noninvasive pump speed signal, represents a significant step toward achieving the full potential of iRBPs in a clinical setting.

## References

1. Hall AW, Soykan O, Harken AH: Physiologic control of cardiac assist devices. Artif Organs 20: 271-275, 1996.  
2. Amin DV, Antaki JF, Litwak P, et al: Controller for an axial-flow blood pump. Biomed Instrum Technol 31: 483-487, 1997.  
3. Baloa LA, Liu D, Boston JR, Simaan MA, Antaki JF: Control of rotary heart assist devices. Proceedings of the American Control Conference, Chicago, IL, 2000.  
4. Boston JR, Baloa LA, Liu D, Simaan MA, Choi S, Antaki JF: Combination of data approaches to heuristic control and fault detection. Conference on Control Applications, Anchorage, AK, 2000.  
5. Endo G, Araki K, Kojima K, Nakamura K, Matsuzaki Y, Onitsuka T: The index of motor current amplitude has feasibility in control for continuous flow pumps and evaluation of left ventricular function. Artif Organs 25: 697-702, 2001.  
6. Oshikawa M, Araki K, Endo G, Anai H, Sato M: Sensorless controlling method for a continuous flow left ventricular assist device. Artif Organs 24: 600-605, 2000.  
7. Tanaka A, Yoshizawa M, Olegario P, et al: Detection and avoiding ventricular suction of ventricular assist devices. Proceedings of the 2005 IEEE Engineering in Medicine and Biology 27th Annual Conference, Shanghai, China, 2005.  
8. Voigt O, Benkowski RJ, Morello GF: Suction detection for the MicroMed DeBakey Left Ventricular Assist Device. ASAIO J 51: 321-8, 2005.  
9. Vollkron M, Schima H, Huber L, Benkowski R, Morello G, Wieselthaler G: Development of a suction detection system for axial blood pumps. Artif Organs 28: 709-16, 2004.  
10. Yuhki A, Hato H, Nogawa M, Miura M, Shimazaki Y, Takatani S: Detection of suction and regurgitation of the implantable centrifugal pump based on the motor current waveform analysis and its application to optimization of pump flow. Artif Organs 23: 532-537, 1999.  
11. Vollkron M, Schima H, Huber L, Benkowski R, Morello G, Wieselthaler G: Advanced Suction Detection for an Axial Flow Pump. Artif Organs 30: 665-670, 2006.  
12. Ferreira A, Chen S, Simaan MA, Boston JR, Antaki JF: A discriminant-analysis-based suction detection system for rotary blood pumps. 28th Annual International Conference of the IEEE EMB5, New York City, NY, 2006.  
13. Karantonis DM, Lovell NH, Ayre PJ, Mason DG, Cloherty SL: Identification and classification of physiologically significant pumping states in an implantable rotary blood pump. Artif Organs 30: 671-679, 2006.  
14. Breiman L: Classification and Regression trees. Boca Raton, FL, Chapman and Hall/CRC Press, 1998.  
15. Nelles O: Nonlinear System Identification: From Classical Approaches to Neural Networks and Fuzzy Models. Berlin/New York, Springer, 2001.  
16. Tansley G, Vidakovic S, Reizes J: Fluid dynamic characteristics of the VentAssist rotary blood pump. Artif Organs 24: 483-487, 2000.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
