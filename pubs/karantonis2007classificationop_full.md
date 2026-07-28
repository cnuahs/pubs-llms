```
@article{karantonis2026classificationop,
  title={Classification of physiologically significant pumping states in an implantable rotary blood pump: effects of cardiac rhythm disturbances.},
  author={Dean M. Karantonis and Nigel H. Lovell and Peter J. Ayre and David G. Mason and Shaun L. Cloherty},
  journal={Artificial organs},
  year={2007},
  volume={31},
  number={6},
  pages={476-479},
  doi={10.1111/j.1525-1594.2007.00409.x},
  url={https://onlinelibrary.wiley.com/doi/10.1111/j.1525-1594.2007.00409.x}
}
```

---

# Classification of Physiologically Significant Pumping States in an Implantable Rotary Blood Pump: Effects of Cardiac Rhythm Disturbances

\*†Dean M. Karantonis, \*‡Nigel H. Lovell, §Peter J. Ayre, §David G. Mason, and \*Shaun L. Cloherty \*Graduate School of Biomedical Engineering; †School of Electrical Engineering and Telecommunications, University of New South Wales, Sydney; ‡National Information and Communications Technology Australia, Eveleigh; and §Ventracor Limited, Chatswood, Sydney, New South Wales, Australia

Abstract: Methods of speed control for implantable rotary blood pumps (iRBPs) are vital for providing implant recipients with sufficient blood flow to cater for their physiological requirements. The detection of pumping states that reflect the physiological state of the native heart forms a major component of such a control method. Employing data from a number of acute animal experiments, five such pumping states have been previously identified: regurgitant pump flow, ventricular ejection (VE), nonopening of the aortic valve (ANO), and partial collapse (intermittent [PVC- I] and continuous [PVC- C]) of the ventricle wall. An automated approach that noninvasively detects such pumping states, employing a classification and regression tree (CART), has also been developed. An extension to this technique, involving an investigation into the effects of cardiac rhythm disturbances on the state detection process, is discussed. When incorporating animal data containing arrhythmic events into the CART model, the strategy showed a marked improvement in detecting pumping states as compared to the model devoid of arrhythmic data: state VE—57.4/91.7% (sensitivity/specificity) improved to 97.1/100.0%; state PVC—66.7/83.1% improved to 100.0/88.3%, and state PVC—11.1/66.2% changed to 0.0/100%. With a simplified binary scheme differentiating suction (PVC- I, PVC- C) and nonsuction (VE, ANO) states, suction was initially detected with 100/98.5% sensitivity/specificity, whereas with the subsequent improved model, both these states were detected with 100% sensitivity. The accuracy achieved demonstrates the robustness of the technique presented, and substantiates its inclusion into any iRBP control methodology. Key Words: Implantable rotary blood pump—Pumping states—Control strategy—Left ventricular assist device—Arrhythmias.

Implantable rotary blood pumps (iRBPs) acting as left ventricular assist devices are proving to be an

effective method of support for patients with a failing heart. Achieving an effective control strategy for iRBPs, such that a recipient's metabolic demand for blood flow is optimized, is crucial to improving the quality of life for these individuals. In order to achieve such a control strategy, a major design goal for iRBPs is the ability to reliably and accurately detect pumping states that cause such deleterious effects as ventricular collapse due to overpumping (ventricular suction), or pump back flow (regurgitation) as a result of underpumping (1). The ability to detect these undesirable pumping states will allow a control system to effectively avoid their occurrence and thus ensure the patient's safety and comfort.

A previous study by the authors (2)—in which a discussion of prior studies may be found—has demonstrated that by using only the noninvasive measure of instantaneous pump impeller speed to assess flow dynamics, it is possible to detect a range of pump states including regurgitant pump flow (PR) (state PR), ventricular ejection (VE) (state VE), aortic valve not opening (ANO) over the entire cardiac cycle (state ANO), and partial collapse (intermittent [PVC- I] and continuous [PVC- C]) of the ventricle wall during the cardiac cycle (states PVC- I and PVC- C). The work herein extends this approach to evaluate the effects of cardiac rhythm disturbances on the classification of pumping states. A classification and regression tree (CART) is used to detect pumping states for the VentrAssist left ventricular assist system (Ventracor Ltd., Sydney, Australia) based on a series of acute animal experiments.

## METHODS

## Animal experiments

Six porcine experiments were conducted in which the VentrAssist (Ventracor Ltd.) iRBP was acutely implanted, as described previously (2). Briefly, the animal's native heart was instrumented to record left ventricular, left atrial, aortic, and pump inlet \((P_{\mathrm{in}})\) pressures; aortic \((Q_{\mathrm{a}})\) and pump \((Q_{\mathrm{p}})\) flows; and a three- lead electrocardiogram (ECG) via needle electrodes. The noninvasive observers of instantaneous pump impeller speed, motor current, and supply voltage were monitored from the pump controller and were also recorded for analysis. In each experiment, the various pumping states were induced by varying the pump speed set point—pump speed was systematically varied between upper and lower limits determined by the cardiovascular response of each animal.

> **Image description.** A composite figure consisting of four panels (a, b, c, d) arranged in a 2x2 grid, illustrating various physiological waveforms (ECG and Flow) under different cardiac conditions: nonarrhythmic (Normal/Heartbeat) and arrhythmic. Each panel contains two line graphs, one for the ECG signal and one for the Flow signal, plotted against time (x-axis) over a 5-second duration.
>
> The panels are organized as follows:
>
> *   **Panel (a) - Normal (Non-Suction):**
>     *   The top graph, labeled "ECG," displays a regular, rhythmic waveform, indicating a normal heart beat. The y-axis ranges from 0.0 to 0.1.
>     *   The bottom graph, labeled "Flow," shows a smooth, periodic waveform with no significant dips toward zero, indicating steady flow. The y-axis ranges from 0 to 8 L/min.
>
> *   **Panel (b) - Normal (Suction):**
>     *   The top graph, labeled "ECG," shows a regular, rhythmic waveform, similar to Panel (a). The y-axis ranges from 0.0 to 0.1.
>     *   The bottom graph, labeled "Flow," displays a periodic waveform that includes a sharp, transient dip toward zero (or slightly negative values) in the middle of the time axis, visually representing a suction event. The y-axis ranges from 0 to 3000 L/min.
>
> *   **Panel (c) - Heartbeat (Non-Suction):**
>     *   The top graph, labeled "ECG," shows a regular, rhythmic waveform. The y-axis ranges from 0.0 to 0.1.
>     *   The bottom graph, labeled "Flow," shows a smooth, periodic waveform with no significant dips, indicating steady flow. The y-axis ranges from 0 to 1900 L/min.
>
> *   **Panel (d) - Arrhythmic (Suction):**
>     *   The top graph, labeled "ECG," displays an irregular and erratic waveform, characteristic of an arrhythmia. The y-axis ranges from 0.0 to 0.2.
>     *   The bottom graph, labeled "Flow," shows a periodic waveform that includes a sharp, transient dip toward zero, indicating a suction event. The y-axis ranges from 2100 to 2300 L/min.
>
> In summary, the figure visually contrasts the regular ECG patterns of normal and heartbeat conditions with the irregular ECG pattern of the arrhythmic condition. It also contrasts the smooth, steady flow waveforms (non-suction) with the waveforms exhibiting sharp dips toward zero (suction) in both normal and arrhythmic contexts. The x-axis for all graphs represents time in seconds, and the y-axes represent electrical activity (ECG) or volumetric flow rate (L/min).

<center>FIG. 1. Example of speed and flow waveforms exhibiting both (c,d) arrhythmic and (a,b) nonarrhythmic events that (a,c) do not induce suction and (b,d) induce suction. In (b), it should be noted that the suction event in the presence of a normal heart beat was induced by an elevated target speed (roughly 2800 rpm), whereas the suction event in (d) was caused by an arrhythmic beat at a relatively lower speed. </center>

## Identifying rhythm disturbances

Arrhythmic cardiac events are caused by a disturbance of the normal electrical conduction system of the heart, and present a further challenge to the task of pumping state detection. The irregular pumping behavior of the native heart under this condition can produce pumping states that generally fall into two categories: arrhythmic events causing suction of the left ventricular myocardium, and those that do not induce suction. A summary of the effects of rhythm disturbances in relation to pumping states is illustrated in Fig. 1, using data from the animal studies undertaken.  

Irrespective of whether suction events are caused by arrhythmias or not, the pump flow and speed signals demonstrate the same fundamental characteristics in both cases (compare Fig. 1b and d). The speed waveform displays transient upward spikes, while the flow waveform shows a concurrent drop toward zero or even negative values. Furthermore, the ECG signal often exhibits similar "arrhythmic" properties, which poses the problem of how to correctly distinguish between these two cases. At lower speeds, it is typical to see a speed waveform of normal appearance (Fig. 1a), interspersed with relatively brief periods of suction. These suction events are induced by arrhythmias originating naturally in the heart itself. At higher speeds, suction may be induced by an excessive withdrawal of blood from the left ventricle by the pump. The resulting mechanical disturbance to the cardiac tissue, which occurs as the walls collapse and strike each other, causes disruption to its electrical activity. This action results in an ECG signal with arrhythmic features, and generally results in prolonged (or indefinite) periods of suction (until the pump speed is lowered). Thus, there is interplay between ventricular suction and cardiac arrhythmia. Nevertheless, it should be noted that any type of suction event, whether induced by arrhythmia or elevated pump speed, should be classified in the same category. It is reasonable to expect that a classifier trained without arrhythmic event data would still classify suction due to arrhythmia correctly.

Arrhythmias not inducing suction generally occur at relatively low pump speeds, and display a change from the normal symmetrical waveforms observed during nonsuction states. The speed and flow waveforms exhibit a decrease in pulsatility, a change in interbeat intervals, and asymmetries in the waveform profile (compare Fig. 1a and c). It is desired however, that such events are classified in the same way as the adjacent data is classified, and most importantly should not indicate suction. Worthy of note is that the various types of rhythm disturbances present in the recorded data (e.g., ectopic beats, atrioventricular block) were not individually scrutinized, but rather, the effect of arrhythmias on the nature of the speed signal waveform was carefully considered.

## Treatment of data

As described previously (2), a CART algorithm (3) was used to identify the pumping state based on a

TABLE 1. Results of the pumping state classification algorithm, for the case where the nonarrhythmic training data set was used in constructing a classification tree, and subsequent validation being performed on the arrhythmic validation set of data

| No. of initial states | Pump state | Correct | Total | Sensitivity (%) | Specificity (%) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 4 | VE | 39 | 68 | 57.4 | 91.7 |
| 4 | ANO | — | — | — | — |
| 4 | PVC-I | 2 | 3 | 66.7 | 83.1 |
| 4 | PVC-C | 1 | 9 | 11.1 | 66.2 |
| 4 | No suction | 46 | 68 | 67.7 | 91.7 |
| 4 | Suction | 1 | 1 | 12 | 91.7 |
| 3 | VE | 39 | 68 | 57.4 | 91.7 |
| 3 | ANO | — | — | — | — |
| 3 | No suction | 56 | 68 | 82.4 | 91.7 |
| 3 | Suction | 1 | 1 | 12 | 91.7 |
| 3 | No suction | 67 | 68 | 98.4 | 100.0 |
| 3 | Suction | 1 | 2 | 12 | 100.0 |
| 2 | VE | 39 | 68 | 57.4 | 91.7 |
| 2 | ANO | — | — | — | — |
| 2 | No suction | 11 | 68 | 82.4 | 91.7 |
| 2 | Suction | 12 | 12 | 91.7 | 82.4 |

number of predictor variables derived from the noninvasive pump speed waveform. These predictor variables, or indices, are described in detail in (2). Statistical analysis via tree building is particularly well suited to classification problems otherwise hampered by considerable variability in or skewed distribution of the predictor variables. Therefore, given the variability, both between subjects and within a single subject, in the indices derived from the pump speed waveform, the CART approach is a natural candidate for the classification of pumping states.

The available data was divided into two broad groups: those segments containing arrhythmias (139 segments in total, each being 6 s in length), and those without (690 segments); these groups were further divided into a training and validation set, of roughly equal proportions. Distinguishing arrhythmic from nonarrhythmic data was a process guided by the principles discussed in the previous section. In order to understand the impact of and account for the effects of arrhythmias on the classification process, a sizeable set of such data was incorporated into the CART analysis, and two separate studies were conducted. First, the nonarrhythmic training data set was used in constructing a classification tree, and this tree was validated with the arrhythmic validation set of data. The next study included both arrhythmic and nonarrhythmic training sets to build a CART model, and was subsequently validated on the same set of data as the first study. In this way, a comparison of classifier accuracy both with and without the effects of arrhythmias could be made.

## RESULTS  

Performance was assessed by comparing the state ascertained by the optimal tree and the "known" state as determined through invasive methods, and quantified by recording the sensitivity (true positive rate) and specificity (true negative rate) associated with each state. It should be noted that there was insufficient data in the arrhythmic validation set to classify state ANO as part of the CART analysis.

The ability to distinguish suction from nonsuction states is of primary importance in this study. Thus, in addition to forming classification trees based on four states, simpler trees were also formed based on more general classifications. The results for a 6- s window length are provided in Tables 1 and 2. In each table, the first column refers to the number of pumping states used as the dependent variable for the CART analysis: all four states (VE, ANO, PVC- I, and PVC- C) were used initially; the two suction states (PVC- I and PVC- C) were then combined to form the suction state, thus providing three states for tree building; finally, states VE and ANO were combined to form the no suction state, providing two states for the analysis. Statistics were also included for the suction and no suction states for every group of results (each group having the same number of initial states) after combining the appropriate set of state results. For example, the suction results with four initial states are found by treating PVC- I and PVC- C as a single state when calculating the statistics. In this way, we establish the tree's performance for more general classifications.

The statistical summaries in Tables 1 and 2 indicate that, following the incorporation of arrhythmic data into the CART analysis, a significant improvement in accuracy was achieved in the detection of most pumping states. For example, if one examines the results for state VE, its classification sensitivity increased from 57.4 to 97.1% when four initial states

TABLE 2. Results of the pumping state classification algorithm, for the case where both arrhythmic and nonarrhythmic training sets were employed to build a classification tree, and subsequent validation being performed on the arrhythmic validation set of data

| No. of initial states | Pump state | Correct | Total | Sensitivity (%) | Specificity (%) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 4 | VE | 66 | 68 | 97.1 | 100.0 |
| 4 | ANO | — | — | — | — |
| 4 | PVC-I | 3 | 3 | 100.0 | 88.3 |
| 4 | PVC-C | 0 | 9 | 0.0 | 100.0 |
| 4 | No suction | 68 | 68 | 100.0 | 100.0 |
| 4 | Suction | 12 | 12 | 100.0 | 100.0 |
| 3 | VE | 63 | 68 | 92.7 | 100.0 |
| 3 | ANO | — | — | — | — |
| 3 | No suction | 68 | 68 | 100.0 | 100.0 |
| 3 | Suction | 12 | 12 | 100.0 | 100.0 |
| 2 | VE | 63 | 68 | 92.7 | 100.0 |
| 2 | ANO | — | — | — | — |
| 2 | No suction | — | — | — | — |
| 2 | Suction | — | — | — | — |

were considered, and from 57.4 to \(92.7\%\) when using three initial states. Similar improvements are evident when the no suction and suction states are employed, with no errors present in any result subgroups as reported in Table 2. Perhaps the only exception to the trend of improvement was state PVC- C, with a sensitivity of \(11.1\%\) (when excluding arrhythmias from the training set) and \(0.0\%\) (when including arrhythmias). However, when considered together with state PVC- I as one suction state, the sensitivity increases to 91.7 and \(100\%\) , respectively, suggesting that the lack of accuracy was due to misclassification between these two suction states (rather than the nonsuction states).

## DISCUSSION

Arrhythmias have been identified as having a significant impact on the ability of a classification tree to correctly identify pumping states. Vollkron et al. (4) acknowledged the complications introduced by arrhythmias, but did not present results specifically including or excluding them from the analysis, and hence no comparison may be made with the present results. Considering that heart failure patients often exhibit an arrhythmic heartbeat, it is imperative that these events be accounted for. As such, they were incorporated into the CART analysis to improve the robustness of the classifier. The statistical summaries given in Tables 1 and 2 demonstrate that including arrhythmic events lead to a significant increase in classification accuracy. The ability of the classifier to discern between normal and suction pumping states without error, after incorporating the data containing arrhythmic events, indicates that the application of the technique was successful.

While the animals used in this study possess relatively healthy cardiac function, human implant patients are suffering from varying degrees of left ventricle failure (and occasionally right heart failure as well), and thus exhibit a more diverse range of arrhythmic characteristics than may be presented from healthy animals. As such, it is anticipated that further research into the effects of arrhythmia when employing human patient data is required to validate the robustness of the methods presented herein.

## CONCLUSION

Incorporating the effects of cardiac rhythm disturbances in the development of a pumping state classifier has been shown to improve the robustness of such algorithms. An increase in the reliability of detecting critical pumping states can only serve to enhance the performance of a pump control strategy.

## REFERENCES

1. Hall AW, Soykan O, Harken AH. Physiologic control of cardiac assist devices. Artif Organs 1996;20:271-5.  
2. Karantonis DM, Lovell NH, Ayre PJ, Mason DM, Cloherty SL. Identification and classification of physiologically significant pumping states in an implantable rotary blood pump. Artif Organs 2006;30:671-9.  
3. Breiman L, Friedman JH, Olshen RA, Stone CJ. Classification and Regression Trees. Monterey, CA: Wadsworth and Brooks, 1984.  
4. Vollkron M, Schima H, Huber L, Benkowski RJ, Morello GF, Wieselthaler G. Development of a suction detection system for axial blood pumps. Artif Organs 2004;28:709-16.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
