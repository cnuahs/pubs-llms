```
@article{ramamoorthy2025prediction,
  title={Prediction of Delirium Risk in Mild Cognitive Impairment Using Time-Series Data, Machine Learning and Comorbidity Patterns -- A Retrospective Study},
  author={Santhakumar Ramamoorthy and Priya Rani and Glenna Matthews and Shaun L. Cloherty and Mahdi Babaei and James Mahon and Richard Kane and Christine Untario},
  journal={IEEE Journal of Biomedical and Health Informatics},
  year={2025},
  volume={29},
  pages={8791-8798},
  doi={10.1109/JBHI.2025.3609068},
  url={https://ieeexplore.ieee.org/document/11284685}
}
```

---

Prediction of Delirium Risk in Mild Cognitive Impairment Using Time-Series Data, Machine Learning and Comorbidity Patterns - A Retrospective Study

Santhakumar Ramamoorthy \(①\) , Priya Rani \(①\) , Senior Member, IEEE, Glenn Matthews \(①\) , Member, IEEE, Shaun L. Cloherty, Member, IEEE, Mahdi Babaei, James Mahon \(①\) , Richard Kane \(①\) , and Christine Untario \(①\)

Abstract- Delirium represents a significant clinical concern characterised by high morbidity and mortality rates, particularly in patients with mild cognitive impairment (MCI). This study investigates the associated risk factors for delirium by analysing the comorbidity patterns relevant to MCI and developing a longitudinal predictive model leveraging machine learning (ML) methodologies. A retrospective analysis utilising the MIMIC- IV v2.2 database was performed to evaluate comorbid conditions, survival probabilities, and predictive modelling outcomes. The examination of comorbidity patterns identified distinct risk profiles for the MCI population. Kaplan- Meier survival analysis demonstrated that individuals with MCI exhibit markedly reduced survival probabilities when developing delirium compared to their non- MCI counterparts, underscoring the heightened vulnerability within this cohort. For predictive modelling, a Long Short- Term Memory (LSTM) model was implemented utilising time- series data, demographic variables, Charlson Comorbidity Index (CCI) scores, and an array of comorbid conditions. The model demonstrated robust predictive capabilities with an Area Under the Receiver Operating Characteristic Curve (AUROC) of 0.92 and an Area Under the Precision- Recall Curve (AUPRC) of 0.91. This study underscores the critical role of comorbidities in evaluating delirium risk and highlights the efficacy of time- series predictive modeling in pinpointing patients at elevated risk for delirium development.

Index Terms- Delirium, mild cognitive impairment, Comorbidity analysis, kaplan- meier survival analysis, long short- term memory, electronic health records, clinical risk prediction, charlson comorbidity index.

## I. INTRODUCTION

ELIRIUM is a clinical condition characterised by acutely impaired attention and consciousness, commonly occurring in older patients in healthcare settings. Older age, comorbid medical conditions, higher burden of acute illness, and the use of sedative and analgesic medications are significant factors associated with an increased risk for delirium [1], [2]. Delirium is commonly observed in intensive care units (ICUs) and is associated with heightened mortality rates, prolonged hospitalisations, and long- term cognitive deficits [3], [4]. Among ICU patients worldwide, delirium is estimated to affect up to \(64\%\) during hospitalisation [5], [6]. The frequency and occurrence of delirium differ among various populations and age brackets, with data suggesting a prevalence of \(0.4\%\) in the overall population, rising to \(1\%\) in those aged 55 years and older [7]. The occurrence of postoperative delirium (POD) is a frequent complication after surgical procedures, with documented occurrence rates of \(40\%\) [8]. Alongside cognitive manifestations, delirium is linked to disturbances in sleep- wake cycles [9]. Individuals experiencing delirium suffer from increased morbidity and mortality rates, as well as heightened distress. The underlying causes of delirium are complex and poorly understood, which makes it both difficult to detect and prevent.

MCI is a transitional stage between normal age- related cognitive decline and more severe cognitive impairment associated with conditions such as Alzheimer's disease (AD). It is characterised by cognitive deficits that are noticeable but not severe enough to interfere significantly with daily activities [10]. The presence of MCI has been associated with an increased vulnerability to delirium, especially during periods of acute stress, such as hospitalisation or surgery [11]. Studies indicate that individuals with MCI may exhibit alterations in inflammatory processes that predispose them to delirium [12]. Furthermore, the cognitive deficits associated with MCI can lead to a higher likelihood of developing delirium when faced with relatively mild medical stressors [13]. Given the multifactorial nature of delirium, individualized, comprehensive strategies are essential to effectively prevent, identify, and manage this complex condition [14].

> **Image description.** A hierarchical flow diagram, titled "Study cohort selection flowchart from the MIMIC-IV v2.2 database," illustrates the process of selecting and stratifying a study population. The diagram uses rectangular boxes connected by vertical arrows to show the progression from a large initial database to four final study groups.
>
> The selection process begins at the top with the initial data source:
> *   **MIMIC-IV Database:** This box contains the initial counts of "431,231 Admissions" and "299,712 Patients."
>
> From this initial population, a filtering process is applied, indicated by an arrow pointing to an "Exclusion" box on the right. The exclusion criteria are listed as:
> 1.  "Patients who have any cognitive impairment other than mild-cognitive or delirium"
> 2.  "Patients with incomplete data"
>
> Following the exclusion of these patients, the cohort is reduced to the **Total Patients**, which is stated as "n = 45,534."
>
> The total patient group is then stratified into two primary categories:
> 1.  **Non-Cognitive Impairment:** n = 44,880
> 2.  **Mild-Cognitive Impairment:** n = 654
>
> Each of these two primary groups is further divided into two final sub-groups based on the presence or absence of delirium:
>
> *   **Under Non-Cognitive Impairment (n = 44,880):**
>     *   Non-Delirium Patients: n = 41,774
>     *   Delirium Patients: n = 3,106
> *   **Under Mild-Cognitive Impairment (n = 654):**
>     *   Non-Delirium Patients: n = 533
>     *   Delirium Patients: n = 121
>
> The flowchart clearly maps the reduction in patient numbers and the final stratification of the study cohort into four distinct groups: Non-Cognitive Impairment/Non-Delirium, Non-Cognitive Impairment/Delirium, Mild-Cognitive Impairment/Non-Delirium, and Mild-Cognitive Impairment/Delirium.

<center>Fig. 1. Study cohort selection flowchart from the MIMIC-IV v2.2 database. The flowchart outlines the inclusion and exclusion criteria used to identify the study population. The population was stratified into MCI and non-MCI cohorts, and each group was further divided based on the presence or absence of delirium. </center>

Despite growing interest in understanding the relationship between MCI and delirium, existing studies have largely focused on incidence rates or progression to dementia, without leveraging longitudinal, time- series data to assess survival outcomes or predict delirium risk over time. To address this critical gap, the present study proposes a comprehensive approach with three key objectives: (1) to identify key risk factors associated with the onset of delirium in individuals with MCI by analyzing comorbidity profiles; (2) to conduct a survival analysis comparing the incidence of delirium between MCI and non- MCI patient groups; and (3) to develop a time- series- based longitudinal predictive model capable of predicting delirium risk over time in both MCI and non- MCI patient populations. To our knowledge, no previous study has systematically applied time series modelling to comorbidity trajectories for delirium prediction in this population, making this study novel and timely. By improving our understanding and prediction of delirium risk among vulnerable patients with MCI, this study seeks to, in turn, facilitate early screening and targeted management strategies to reduce delirium- related complications and safeguard long- term cognitive health in clinical settings.

## II. METHODS

### A. Ethical Review

The data collected by the Medical Information Mart for Intensive Care IV (MIMIC- IV) version 2.2 database [15], [16]

follows recognised ethical guidelines and meets both institutional and federal compliance requirements. Due to its retrospective design, lack of direct patient involvement, and the use of a thorough de- identification process that aligns with Safe Harbor criteria outlined by the Health Insurance Portability and Accountability Act (HIPAA), the dataset does not require approval from an institutional review board (IRB). MIMIC- IV provides a modern electronic health record dataset that covers hospital admissions from 2008 to 2019, thus offering extensive and de- identified patient information for research purposes. The authors have completed the necessary coursework and personal training evaluations required by the Massachusetts Institute of Technology Affiliates (Record ID: 62569697), ensuring compliance with ethical standards for research involving de- identified health information.

### B. Study Population

The study population was derived from the MIMIC- IV version 2.2 database. After applying the selection criteria, a total of 45,534 patients were included in the analysis. This group excluded patients diagnosed with dementia and cognitive impairment other than MCI. The data was divided into two groups, Non- MCI Group: A total of 44,880 patients were classified as having no MCI, within the group, 3106 patients were identified with delirium using the International Classification of Diseases (ICD) codes F05, 293.0 and 292.81. MCI Group: The MCI group consisted of 654 patients identified based on the ICD- 9 code 331.83 and the ICD- 10 code G31.84. Among them, 121

TABLEI SUMMARY OF VARIABLES INCLUDED IN THE DELIRIUM PREDICTION MODELS

| Variable Category | Variables |
| :--- | :--- |
| Demographic data | Age, gender |
| Diseases diagnosis data | Total ICD-coded diagnoses (t_icds) per admission* |
| Comorbidity Condition data | Myocardial Infarction, Congestive Heart Failure, Peripheral Vascular Disease, Cerebrovascular Disease, Chronic Pulmonary Disease, Rheumatic Disease, Peptic Ulcer Disease, Mild Liver Disease, Diabetes without Comorbidities, Diabetes with Comorbidities, Paraplegia, Renal Disease, Malignant Cancer, Severe Liver Disease, Metastatic Solid Tumor, Charlson Comorbidity Index. |

Note. \* The variable t_icds per admission refers to the cumulative count of all unique ICD- coded diagnosed diseases per admission which varies for each patients

TABLE II CHARACTERISTICS OF MCI AND NON-MCI STUDY POPULATION   

<table>TotalNo MCIMCI45,534(100%)44,880(98.56%)654(1.44%)Age (IQR*), years79 (73-84)79 (73-84)80 (74-85)Male21,226 (46.62%)20,933 (46.64%)293 (44.80%)Female24,308 (53.38%)23,947 (53.36%)361 (55.20%)</table>

Note. \\*The age values are reported as medians with interquartile ranges (IQR).

patients were further classified into the delirium group, based on the same ICD codes F05, 293.0, and 292.81. Fig. 1 presents a comprehensive overview of the patient selection process. The complete list of ICD- 9 and ICD- 10 codes used to define inclusion and exclusion criteria is provided in Table IV.

The Table II summarizes the demographic characteristics of the study population. For the non- MCI cohort, there was a slightly higher proportion of females compared to males. Specifically, 20,933 patients (46.64%) were male, while 23,947 patients (53.36%) were female. The median age in this cohort was 79, with an IQR of (73 - 84) years, representing an older population overall. The MCI cohort has a slightly greater female representation. Among this group, 293 patients (44.8%) were male, and 361 patients (55.2%) were female. The median age of the MCI cohort was slightly higher at 80, with an IQR of (74 - 85) years. Furthermore, 50% of patients experienced multiple hospital admissions over the approximately 12- year study period, reflecting the sustained and recurring healthcare needs of this population, based on data availability in the MIMIC- IV database.

### C. Identification of Key Risk Factors Through Comorbidity Profiling  

text[[63, 832, 484, 954], [502, 475, 923, 654]]
To identify comorbidity risk factors for delirium in MCI patients, the study divided patients into MCI (654 patients) and non- MCI groups (44,880 patients). Each group was further split into delirium and non- delirium subgroups based on diagnostic codes, with 121 delirium cases in the MCI group and 3,106 in the non- MCI group. Comorbidity profiles were established for all groups. The specific comorbidities identified in this study are summarized in the Table III. Descriptive statistics were used to summarize the proportion of patients with each comorbid condition across groups (MCI vs. non- MCI and delirium vs. non- delirium). Group- wise differences were evaluated using Pearson's Chi- square test of independence, and False Discovery Rate (FDR) correction was applied to account for multiple testing across comorbidities. Adjusted p- values (adj- p) are reported, with a significance threshold of adj- p < 0.05. Confidence intervals (CIs) (95%) for proportions were calculated using the Wald method. This analysis aimed to highlight which comorbidities were more prevalent in patients with MCI who developed delirium, providing insights into potential risk factors for targeted prediction.

### D. Kaplan-Meier Survival Analysis for Delirium Onset

To identify relevant comorbidity- related risk factors for delirium in patients with MCI, a Kaplan- Meier survival analysis was conducted to compare the incidence and timing of delirium onset between MCI and non- MCI cohorts. Survival time was defined as the period (in months) from the index hospital admission to the first recorded diagnosis of delirium or censoring using ICD- coded diagnostic data at the last available follow- up. Patients without a recorded delirium diagnosis were treated as right- censored at the time of discharge, death, or the end of the study period. It is important to note that this analysis includes both delirium identified during the index admission as well as new- onset delirium diagnosed during subsequent hospital encounters within the follow- up window. It is acknowledged that this approach may have introduced immortal time bias, as survival and rehospitalisation were required for patients to be observed with incident delirium. Both the MCI and non- MCI groups were analysed independently, and survival curves were

TABLE III COMORBIDITY CHARACTERISTICS OF THE STUDY POPULATION

| Parameters | MCI Cohorts | Delirium Cohorts | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | with MCI | without MCI | with MCI | without MCI | adj-p | adj-p |
| Renal Disease | 0.292 (0.257-0.327) | 0.233 (0.229-0.237) | 0.005 | 0.405 (0.317-0.492) | 0.332 (0.315-0.348) | 0.356 |
| Diabetes With Comorbidities | 0.136 (0.110-0.162) | 0.090 (0.087-0.092) | 0.005 | 0.198 (0.127-0.269) | 0.120 (0.108-0.131) | 0.150 |
| Metastatic Solid Tumor | 0.035 (0.021-0.049) | 0.069 (0.066-0.071) | 0.005 | 0.025 (0.000-0.052) | 0.081 (0.072-0.091) | 0.180 |
| Peripheral Vascular Disease | 0.086 (0.064-0.107) | 0.114 (0.111-0.117) | 0.082 | 0.132 (0.072-0.193) | 0.154 (0.141-0.167) | 0.764 |
| Myocardial Infarction | 0.133 (0.107-0.159) | 0.147 (0.143-0.150) | 0.443 | 0.198 (0.127-0.269) | 0.175 (0.162-0.189) | 0.764 |
| Congestive Heart Failure | 0.271 (0.237-0.305) | 0.272 (0.268-0.276) | 0.946 | 0.405 (0.317-0.492) | 0.397 (0.380-0.415) | 0.945 |
| Cerebrovascular Disease | 0.139 (0.113-0.166) | 0.130 (0.127-0.133) | 0.513 | 0.149 (0.085-0.212) | 0.146 (0.134-0.159) | 0.945 |
| Chronic Pulmonary Disease | 0.206 (0.175-0.237) | 0.227 (0.223-0.231) | 0.182 | 0.256 (0.178-0.334) | 0.280 (0.265-0.296) | 0.764 |
| Rheumatic Disease | 0.057 (0.039-0.074) | 0.042 (0.040-0.044) | 0.513 | 0.066 (0.022-0.110) | 0.048 (0.040-0.055) | 0.756 |
| Peptic Ulcer Disease | 0.009 (0.002-0.016) | 0.018 (0.017-0.019) | 0.182 | 0.017 (0.000-0.039) | 0.024 (0.018-0.029) | 0.771 |
| Mild Liver Disease | 0.032 (0.019-0.046) | 0.040 (0.038-0.042) | 0.443 | 0.017 (0.000-0.039) | 0.044 (0.037-0.051) | 0.429 |
| Diabetes Without Comorbidities | 0.197 (0.167-0.228) | 0.215 (0.211-0.219) | 0.443 | 0.248 (0.171-0.325) | 0.242 (0.227-0.258) | 0.945 |
| Paraplegia | 0.034 (0.020-0.047) | 0.029 (0.027-0.030) | 0.513 | 0.017 (0.000-0.039) | 0.027 (0.021-0.032) | 0.764 |
| Malignant Cancer | 0.121 (0.096-0.146) | 0.145 (0.142-0.148) | 0.182 | 0.107 (0.052-0.163) | 0.169 (0.156-0.182) | 0.356 |
| Severe Liver Disease | 0.006 (0.000-0.012) | 0.012 (0.011-0.013) | 0.356 | 0.000 (0.000-0.000) | 0.012 (0.008-0.016) | 0.552 |

Note. Proportions are presented with \(95\%\) confidence intervals calculated using the Wald method. Reported adj- \(p\) values have been adjusted for multiple comparisons using the FDR method and are based on Pearson's Chi-square test of independence.

generated to visualise the cumulative probability of remaining delirium- free over time. Survival probabilities were estimated at defined monthly intervals, and the \(95\%\) CIs for each time point were calculated using Greenwood's formula. To statistically compare the survival distributions between the two groups, the log- rank test was applied. A p- value threshold of \(\mathrm{p}< 0.05\) was used to determine statistical significance in survival differences. The analysis aimed to evaluate whether individuals with MCI were at higher risk of developing delirium over time compared to those without MCI.

### E. Data Annotation for Predictive Modeling

For the purposes of training the time- series prediction model, delirium annotations were derived from structured diagnosis codes across all patient admissions in the MIMIC- IV v2.2 database. MCI status was assigned using ICD- 9 code 331.83 and ICD- 10 code G31.84, while delirium status was determined using ICD- 9 codes 293.0 and 292.81 and ICD- 10 code F05. To create the training labels, all diagnosis codes were aggregated longitudinally so that any occurrence of delirium during the observation period was treated as a positive outcome label. Each patient's time- series record consisted of sequential admissions and associated variables mentioned in the Table I, with the final delirium label indicating whether delirium was documented at any point during follow- up. This approach aligns with established practices in retrospective studies of MIMIC data.

### F. Data Preprocessing for Predictive Modeling

Prior to modeling, all extracted variables underwent standardized preprocessing. The input dataset included demographic

F. Data Preprocessing for Predictive ModelingPrior to modeling, all extracted variables underwent standardized preprocessing. The input dataset included demographicvariables (age, gender), total ICD-coded diagnoses (t_icds) per admission, comorbidity indicators derived from the CCI [18], and CCI scores (Table I). For numerical variables, records with missing values were excluded to ensure data integrity. Categorical comorbidity indicators were encoded as binary features indicating presence or absence of each condition. All numerical variables were normalized to a 0–1 range using min–max scaling. For each patient, sequential time-series records of the features (Table I) were generated by chronologically ordering hospital admissions to represent the clinical trajectory over time, with each admission corresponding to a discrete timestep in the model input. To address class imbalance resulting from the relatively small proportion of delirium-positive cases, the Synthetic Minority Over-sampling Technique for Nominal and Continuous features (SMOTENC) [19] was applied to the flattened time-series data. SMOTENC was selected over simpler resampling methods (such as random oversampling or standard SMOTE) because it supports mixed data types, generating synthetic samples that preserve the distributions of both categorical and continuous variables. This approach was intended to create more realistic minority class representations and reduce potential bias in the model. However, SMOTENC can introduce limitations, including increased computational complexity and a higher risk of overfitting due to the introduction of synthetic records. To mitigate these issues, all oversampling and down-sampling were performed exclusively within each training fold of the cross-validation pipeline to avoid information leakage and to ensure unbiased performance estimates. Additionally, the majority (non-delirium) class was randomly downsampled to further balance the training data.

> **Image description.** A flow diagram illustrating the architecture of a lightweight LSTM-based neural network designed for predicting delirium onset. The diagram consists of five distinct, sequentially arranged rectangular blocks, each representing a layer or stage in the model, connected by an implied left-to-right data flow.
>
> The architecture is detailed as follows:
>
> 1.  **Input Layer:** The process begins with an orange rectangular block labeled "Input (Sequence)," indicating the sequential clinical data fed into the model.
> 2.  **LSTM Layer:** The data flows into a yellow/gold rectangular block, which represents the primary recurrent layer. This block is labeled "LSTM Layer / Units = 32 / Activation = tanh," specifying that the layer has 32 units and uses the hyperbolic tangent activation function.
> 3.  **Dropout Layer:** Following the LSTM layer is a teal/cyan rectangular block labeled "Dropout / rate = 0.3." This layer is intended to prevent overfitting by randomly setting 30% of the input units to zero during training.
> 4.  **Dense Layer:** The next component is a blue rectangular block labeled "Dense / Units = 1 / Activation = sigmoid." This fully connected layer has a single unit and uses the sigmoid activation function, which is typical for binary classification tasks.
> 5.  **Output Layer:** The final stage is an orange rectangular block labeled "Output (Probability)," representing the model's prediction of the probability of delirium onset.
>
> The overall visual structure is a linear pipeline, clearly defining the transformation of sequential input data through specialized layers (LSTM, Dropout, Dense) to produce a final probabilistic output.

<center>Fig. 2. A Lightweight LSTM-Based Architecture for Predicting Delirium Onset using Sequential Data. </center>

### G. Predictive Modeling of Delirium Onset

To model the temporal progression of clinical variables and predict delirium onset, a LSTM neural network was implemented as the primary time- series model [17]. The LSTM architecture was chosen for its ability to capture long- range dependencies in sequential clinical data. For comparison, two baseline models were developed: a Simple Recurrent Neural Network (SimpleRNN) to serve as a minimal sequence- based benchmark, and a logistic regression model trained on flattened input sequences to represent a conventional, non- temporal classifier. The model was designed to capture sequential patterns in patient data across hospital admissions and to estimate individualized delirium risk for patients diagnosed with MCI. The proposed architecture consist of a single LSTM layer to capture temporal dependencies from sequential clinical data, followed by a dropout layer to prevent overfitting. A dense layer with sigmoid activation is used for predicting delirium onset (Fig. 2). All models were trained and validated using a 10- fold cross- validation framework, with performance evaluated via AUROC, AUPRC, and Brier score to assess discrimination precision- recall balance, and calibration. To improve the interpretability of LSTM predictions, SHapley Additive exPlanations (SHAP) were applied to estimate the contribution of each input feature and timestep to individual risk scores. SHAP values quantify the impact of each variable on the predicted probability of delirium, thereby supporting transparency and clinical interpretability. Mean absolute SHAP values were visualized to highlight the most influential features and temporal patterns.

## III. RESULT

### A. Comorbidity Patterns Across MCI and Delirium Cohorts  

Table III summarizes the prevalence of comorbidities across MCI and delirium groups. After applying FDR correction, renal disease (29.2% vs. 23.3%, adj- \(p\) : 0.005) and diabetes with complications (13.6% vs. 9.0%, adj- \(p\) : 0.005) were significantly more prevalent among patients with MCI compared to those without MCI. In contrast, metastatic solid tumors were more common in the non- MCI group (6.9% vs. 3.5%, adj- \(p\) : 0.005). Some comorbidities, such as peripheral vascular disease (adj- \(p\) : 0.082), did not retain significance after multiple testing adjustment. Within both MCI and non- MCI cohorts, additional comparisons between delirium and non- delirium groups revealed similar trends; for example, diabetes with comorbidities appeared more frequent in delirium cases (adj- \(p\) : 0.150), and metastatic solid tumors less frequent (adj- \(p\) : 0.180), though neither reached significance post- adjustment. These results highlight distinct comorbidity profiles associated with MCI and suggest possible, though not statistically robust, patterns within delirium subgroups.

> **Image description.** A Kaplan-Meier survival plot titled "Survival Plot for Patients Developing Delirium," which compares the time until delirium onset between two patient groups.
>
> The graph features two primary axes:
> *   The Y-axis, labeled "Survival Probability," ranges from 0 to 100%.
> *   The X-axis, labeled "Time (months)," ranges from 0 to 140, with major tick marks every 20 months.
>
> Two distinct data series are plotted, representing the two patient cohorts:
> 1.  **MCI Patients:** Represented by a blue line.
> 2.  **Non-MCI Patients:** Represented by a green line.
>
> Both lines begin at a 100% survival probability at Time 0. The visual data demonstrates a clear difference in the rate of delirium onset between the two groups. The blue line (MCI Patients) shows a much steeper and more rapid decline in survival probability, indicating that this group develops delirium significantly faster. The green line (Non-MCI Patients) declines more gradually and remains consistently higher than the blue line throughout the entire 140-month observation period.
>
> A statistical finding is highlighted in the center of the graph: "p-value < 0.000," indicating a highly statistically significant difference in the survival curves between the MCI and Non-MCI patient groups. The overall visual pattern strongly suggests that patients with Mild Cognitive Impairment (MCI) have a significantly higher risk and earlier onset of delirium compared to those without MCI.

<center>Fig. 3. The Kaplan-Meier survival curves comparing the time to delirium onset between the MCI and Non-MCI cohorts. The plot shows a significantly lower survival probability (delirium-free duration) over time in the MCI cohort, indicating a higher risk of developing delirium compared to the Non-MCI group. </center>

### B. Kaplan-Meier Survival Analysis for Developing Delirium

The Kaplan- Meier survival analysis demonstrated notable differences in delirium- free survival probabilities for developing delirium between the MCI and non- MCI cohorts (log- rank test, \(p < 0.000\) ). In the MCI cohort, survival probabilities declined rapidly over time, starting at 96.97% (95% CI: 80.37- 99.57) at 6 months. By 12 months, the survival probability had dropped to 62.70% (95% CI: 43.74- 76.83), and at 24 months, it further declined to 31.35% (95% CI: 16.44- 47.46). In contrast, the non- MCI cohort exhibited higher survival probabilities throughout the same period. At 6 months, the survival probability was 97.96% (95% CI: 96.86- 98.68). By 12 months, the survival probability was 78.92% (95% CI: 76.19- 81.37), and by 24 months, it decreased to 59.72% (95% CI: 56.46- 62.82) as shown in (Fig. 3). These results highlight a steeper decline in survival probabilities within the MCI cohort, indicating a higher susceptibility to developing delirium over time compared to the non- MCI cohort.

### C. Model Performance

The LSTM model achieved strong predictive performance, with an AUROC of 0.92 (95% CI: 0.90- 0.93) and an AUPRC of 0.91 (95% CI: 0.90- 0.93) (Fig. 4), indicating high accuracy and reliability. To contextualize this performance, two baseline models were implemented using the same features and evaluation pipeline. A logistic regression model, trained on time- flattened inputs, yielded markedly lower performance

> **Image description.** A line graph titled "Receiver Operating Characteristic (ROC) Curve" displays multiple Receiver Operating Characteristic (ROC) curves, illustrating the performance of a model across ten different data folds.
>
> The graph features a standard Cartesian coordinate system:
> *   The Y-axis is labeled "True Positive Rate" and ranges from 0.0 to 1.0.
> *   The X-axis is labeled "False Positive Rate" and ranges from 0.0 to 1.0.
>
> A dashed black diagonal line runs from the origin (0.0, 0.0) to the top-right corner (1.0, 1.0), representing the performance of a random classifier (Area Under the Curve, or AUC, of 0.5).
>
> Ten distinct colored lines, representing different data folds, are plotted. These curves generally bow upwards and towards the top-left corner of the graph, indicating strong predictive performance. The curves are tightly clustered, with most lines positioned significantly above the diagonal line.
>
> A legend on the right side of the plot provides the specific AUROC (Area Under the Receiver Operating Characteristic Curve) value for each fold:
> *   Fold 1 AUROC: 0.94
> *   Fold 2 AUROC: 0.90
> *   Fold 3 AUROC: 0.91
> *   Fold 4 AUROC: 0.94
> *   Fold 5 AUROC: 0.92
> *   Fold 6 AUROC: 0.93
> *   Fold 7 AUROC: 0.92
> *   Fold 8 AUROC: 0.93
> *   Fold 9 AUROC: 0.93
> *   Fold 10 AUROC: 0.50
>
> The visual evidence suggests that the model performs very well across most folds, with AUROC values generally above 0.90, although Fold 10 shows a significantly lower performance (0.50), aligning with the random chance line.

<center>Fig. 4. The Receiver Operating Characteristic (ROC) curve for the validation cohort, illustrating the model's ability to discriminate between patients who developed delirium and those who did not. A high area under the curve (AUC) indicates strong predictive performance. </center>

(AUROC: 0.57, AUPRC: 0.22), highlighting the limitations of conventional static classifiers in capturing temporal dependencies. A SimpleRNN, trained with the same architecture and hyperparameters as the LSTM model, achieved an AUROC of 0.86 (95% CI: 0.77- 0.94) and an AUPRC of 0.85 (95% CI: 0.76- 0.93), reflecting moderate improvement over logistic regression but lower overall accuracy compared to the LSTM model. These results emphasize the importance of temporal modeling in clinical sequence data and demonstrate the added value of gated architectures like LSTM in enhancing predictive accuracy. Model interpretability was assessed using SHAP analysis (Fig. 5). The summary plot (Fig. 6) revealed that earlier hospital admissions — particularly timestep 3 — contributed most strongly to model predictions, while the influence of later timesteps progressively declined.

## IV. DISCUSSION

This study elucidates significant differences in comorbidity profiles, survival probabilities, and predictive modelling outcomes for delirium in patients with MCI and highlights the heterogeneity of this population compared to non- MCI counterparts. The findings underscore the interplay between cognitive impairment, comorbidities, and delirium risk, offering critical insights into clinical decision- making and risk stratification. Our results are similar to a recent study that indicates that adults who are experiencing MCI are at an increased risk of developing delirium [20], [21]. Also, patients with substantial comorbidities may have an elevated risk of developing delirium [22], [23].  

This study examined comorbidity patterns across MCI and delirium cohorts. Specifically, the MCI group had a significantly higher prevalence of renal disease (29.2%, 95% CI: 25.7- 32.7 vs. 23.3%, 95% CI: 22.9- 23.7; adj- p: 0.005) and diabetes with comorbidities (13.6%, 95% CI: 11.0- 16.2 vs. 9.0%, 95% CI: 8.7- 9.2; adj- p: 0.005). In contrast, metastatic solid tumors were more common in the non- MCI group (6.9%, 95% CI: 6.6- 7.1 vs. 3.5%, 95% CI: 2.1- 4.9; adj- p: 0.005). Although some trends were observed in delirium subgroups—such as a higher rate of diabetes with comorbidities in patients with delirium (19.8% vs. 12.0%)—none of these differences reached statistical significance after FDR correction. These results underscore specific comorbidities, particularly renal disease and complex diabetes, as disproportionately affecting patients with MCI [24]. However, the findings likely indicate that the patients included had clinically recognized cognitive decline, as the identification of MCI was based solely on ICD- coded diagnoses. Consequently, subtle or undocumented cases may have been underrepresented.

> **Image description.** A SHAP summary plot, labeled "Fig. 5," which is a type of scatter plot used to visualize the contribution of individual features to a machine learning model's output. The plot displays the relationship between the SHAP value (the impact on the model output) and the feature values for various clinical and demographic variables.
>
> The plot is structured with the features listed vertically on the Y-axis and the SHAP value on the horizontal X-axis.
>
> **Axes and Scales:**
> *   **Y-axis (Features):** Lists 19 distinct features, including clinical conditions and demographics. The features listed are: cci, tcds, congestive heart failure, myocardial infarct, renal disease, age, cerebrovascular disease, chronic pulmonary disease, paraplegia, peripheral vascular disease, diabetes with cc, rheumatic disease, peptic ulcer disease, metastatic solid tumor, malignant cancer, mild liver disease, severe liver disease, and gender.
> *   **X-axis (SHAP value):** Labeled "SHAP value (impact on model output)," this axis ranges from approximately -0.06 on the left to 0.08 on the right, indicating the magnitude and direction of the feature's influence on the model's prediction.
>
> **Data Representation and Color Coding:**
> *   The data points are represented by small dots, which are colored either red or blue.
> *   A vertical color bar on the right side of the plot, labeled "Feature value," serves as the legend. The top of the bar is red and labeled "High," while the bottom is blue and labeled "Low."
> *   Therefore, red dots indicate instances where the corresponding feature had a high value, and blue dots indicate instances where the feature had a low value.
>
> **Visual Patterns:**
> *   The data points for most features are clustered relatively close to the zero line on the X-axis, suggesting that the majority of these features have a moderate or small impact on the model's output.
> *   The distribution of red and blue points varies across the features, indicating that the impact of a feature (positive or negative) is dependent on whether the feature's value was high or low. For example, some features show a slight tendency for red dots to be shifted to the right (positive impact) while blue dots are shifted to the left (negative impact), though this effect is subtle across the board.

<center>Fig. 5. SHAP summary plot showing the contribution of each feature to predicted delirium risk. Higher SHAP values indicate greater impact on model output. Feature importance is ranked by the mean absolute SHAP value across all samples. The cci, t_cids, and several specific comorbidities were the most influential features. </center>

> **Image description.** A column chart titled "Fig. 6. Mean absolute SHAP values across timesteps illustrating the..." displays the mean absolute SHAP values for 19 different timesteps, illustrating the predictive importance of each timestep in a delirium prediction model.
>
> The chart features two primary axes:
> *   **X-axis (Horizontal):** Labeled "Timesteps," it represents the sequence of time points and is marked with integers from 1 to 19.
> *   **Y-axis (Vertical):** Labeled "Mean Absolute SHAP Value," it measures the magnitude of influence and ranges from 0.0000 to 0.0030, with major grid lines marked every 0.0010.
>
> The data is presented as 19 vertical bars, each corresponding to a specific timestep. The visual pattern shows a clear trend of decreasing influence over time:
> *   **Peak Influence:** The highest mean absolute SHAP values are observed at the beginning of the sequence. Timestep 1 exhibits the highest value, reaching approximately 0.0022. Timestep 3 also shows a significant peak, with a value around 0.0018.
> *   **General Trend:** Following the initial peaks, the mean absolute SHAP values for the subsequent timesteps (4 through 19) progressively decline.
> *   **Later Timesteps:** The bars for timesteps 4 through 19 are substantially lower than the initial peaks, generally clustering between 0.0005 and 0.0012, indicating a diminishing contribution to the model's prediction as the sequence progresses.
>
> Overall, the chart visually confirms that the model places the greatest predictive weight on the earliest timesteps, particularly Timestep 1 and Timestep 3, while the influence of later timesteps is significantly reduced.

<center>Fig. 6. Mean absolute SHAP values across timesteps, illustrating the temporal importance of hospital admissions for predicting delirium. Each timestep represents a prior hospital admission, ordered chronologically from the most recent (timestep 1) to the least recent. The analysis shows that earlier admissions — particularly timestep 3 — contributed most strongly to the model's risk estimation. </center>

Kaplan- Meier survival analysis revealed a significantly steeper decline in survival probabilities for developing delirium among MCI patients compared to non- MCI patients. At 24

TABLE IV ICD CODES AND CONDITIONS USED FOR STUDY INCLUSION AND EXCLUSION (ICD-9 AND ICD-10)

| ICD Code (Version) | Condition Name |
| :--- | :--- |
| 290.0–290.9 (ICD-9) | Senile and presenile dementias |
| 291.1, 291.2 (ICD-9) | Alcohol-induced persisting amnestic disorder / dementia |
| 292.81 (ICD-9) | Drug-induced delirium |
| 292.82 (ICD-9) | Drug-induced persisting dementia |
| 293.0 (ICD-9) | Delirium, not otherwise specified (NOS) |
| 294.0–294.20 (ICD-9) | Persistent mental disorders due to other conditions |
| 331.0 (ICD-9) | Alzheimer's disease |
| 331.11, 331.19 (ICD-9) | Pick's disease / Frontotemporal dementia |
| 331.82 (ICD-9) | Dementia with Lewy bodies |
| 331.83 (ICD-9) | Mild Cognitive Impairment |
| A81.00 (ICD-10) | Creutzfeldt–Jakob disease |
| E71.0, E75.2, E75.23, E75.29 (ICD-10) | Metabolic and genetic neurodegenerative disorders |
| F01–F04 (ICD-10) | Vascular and unspecified dementias |
| F10.26–F18.97 (ICD-10) | Substance-induced persisting dementia and amnestic disorders |
| G10 (ICD-10) | Huntington's disease |
| G20 (ICD-10) | Parkinson's disease |
| G30 (ICD-10) | Alzheimer's disease |
| G23.1, G31, G31.85 (ICD-10) | Other degenerative diseases of the nervous system |
| G31.84 (ICD-10) | Mild Cognitive Impairment |
| R41 (ICD-10) | Symptoms involving cognitive function and awareness |
| F05 (ICD-10) | Delirium due to known physiological condition |

Note. The table above outlines the ICD-9 and ICD-10 codes used to define inclusion and exclusion criteria for this study. These codes represent various cognitive impairment and neurodegenerative conditions [25].

months, the survival probability for the MCI cohort dropped to \(31.35\%\) , compared to \(59.72\%\) in the non- MCI cohort (log- rank test, \(p < 0.000\) ). This underscores the heightened vulnerability of cognitively impaired patients to delirium, which may be driven by their distinct comorbid profiles and underlying pathophysiological processes. Although higher delirium incidence among MCI patients was demonstrated, these findings should be viewed cautiously due to potential immortal time bias and methodological limitations of retrospective data. Importantly, a logistic regression model using the same feature set yielded substantially lower discrimination performance (AUROC: 0.57; AUPRC: 0.22), demonstrating that traditional linear classifiers may be inadequate for capturing the temporal dependencies and complex interactions embedded in sequential clinical data. While the SimpleRNN provided moderate performance gains (AUROC: 0.86), the LSTM prediction model (AUROC: 0.92; AUPRC: 0.91) consistently outperformed the simpler models, validating the integration of time- series health records, including demographic data, CCI scores, and detailed comorbidity profiles, as critical components for accurate delirium risk stratification. The model's ability to effectively capture temporal and clinical patterns in high- risk populations represents a significant advancement in predictive analysis for complex patient cohorts.  

In practice, this model could be integrated into EHR platforms to provide real- time risk scores for patients with MCI, triggering early interventions to prevent delirium onset. Prospective validation and workflow integration will be essential to ensure clinical utility and adoption. Although LSTM models are often criticized for limited inherent interpretability, SHAP was applied to provide transparency into the influence of each variable and timestep on delirium risk predictions. This approach supports clinical trust and facilitates understanding how specific comorbidity patterns and temporal information contribute to the model's output. These findings underscore that the cumulative comorbidity burden, as captured by the CCI and the total number of coded diagnoses, is a key driver of model predictions. Additionally, early timepoints in the patient trajectory provided the most salient information for risk stratification, suggesting that initial clinical presentations have a critical impact on delirium risk assessment.

## V. LIMITATIONS

This study has several limitations. The retrospective design and use of structured EHR data limit generalizability, as key variables like medication use and cognitive testing were unavailable. MCI identification based only on ICD codes likely led to underreporting (1.44% prevalence), reflecting more severe or clinically obvious cases. Lack of neuropsychological validation and exclusion of dementia codes may also affect case accuracy. Delirium classification may be incomplete due to inconsistent documentation. Including both total CCI and its components may introduce collinearity but was done to reflect both overall and specific comorbidity effects. Differences in comorbidity rates may reflect surveillance bias, where sicker patients are more likely to be assessed for cognitive issues. Additionally,

survival analysis may be affected by immortal time bias and unmodeled competing risks, so results should be interpreted descriptively. While the LSTM model performed well, overfitting is still possible, especially when compared to simpler models. To reduce this risk, we included logistic regression and SimpleRNN as benchmarks. SMOTENC oversampling was limited to training data, but synthetic samples may still introduce some bias. The small MCI group limits statistical strength, and the retrospective design without detailed clinical data may result in unmeasured confounding. Future studies should use larger, multi- site datasets with clinical validation to improve accuracy and generalizability.

## VI. CONCLUSION

In this study, the interplay between MCI, comorbidities, and the risk of delirium was systematically evaluated, along with the development of a time- series predictive model. Analysis in this study revealed that distinct comorbidity profiles significantly influenced delirium risk in MCI patients. Furthermore, a LSTM model was implemented, confirming the utility of time- series data and machine learning in predicting delirium risk. The model demonstrated robust performance in identifying high- risk patients, thereby supporting the integration of advanced analytics into clinical workflows to enable earlier detection and intervention for delirium risk. Future studies should validate the model externally and explore the incorporation of additional data types to further improve predictive performance.

# Untitled_Paper - Appendix

---

## APPENDIX

### A. Inclusion and Exclusion Criteria

This appendix provides a summary of the ICD- 9 and ICD- 10 codes used to define the inclusion and exclusion criteria for study participants. These codes, as detailed in Table IV, were selected to identify cases of MCI and delirium while excluding other cognitive and neurodegenerative conditions that may confound the analysis.

## REFERENCES

[1] J. E. Wilson et al., "Delirium," Nature Rev. Dis. Primers, vol. 6, no. 1, 2020, Art. no. 90, doi: 10.1038/s41572- 020- 00223- 4. [2] M. Kanova, P. Sklienka, R. Kula, M. Burda, and J. Janoutova, "Incidence and risk factors for delirium development in ICU patients - a prospective observational study," Biomed. Papers, vol. 161, no. 2, pp. 187- 196, 2017, doi: 10.5507/bp.2017.004. [3] J. L. Stollings, K. Kotfis, G. Chanques, B. T. Pun, P. P. Pandharipande, and E. W. Ely, "Delirium in critical illness: Clinical manifestations, outcomes, and management," Intensive Care Med., vol. 47, no. 10, pp. 1089- 1103, 2021, doi: 10.1007/s00134- 021- 06503- 1. [4] C. Xu, Z. Chen, L. Zhang, and H. Guo, "Systematic review and meta- analysis on the incidence of delirium in intensive care unit inpatients after cognitive exercise intervention," Ann. Palliat. Med., vol. 11, no. 2, pp. 66372- 66672, 2022. [Online]. Available: https://apm.amegroups.org/article/view/89970 [5] S. Bose, L. Kelly, Z. Shahn, L. Novack, V. Banner- Goodspeed, and B. Subramaniam, "Sedative polypharmacy mediates the effect of mechanical ventilation on delirium in critically ill COVID- 19 patients: A retrospective cohort study," Acta Anaesthesiologica Scandinavica, vol. 66, no. 9, pp. 1099- 1106, 2022, doi: 10.1111/aas.14119.

[6] E. Alzoubi, F. Shaheen, and K. Yousef, "Delirium incidence, predictors and outcomes in the intensive care unit: A prospective cohort study," Int. J. Nurs. Pract., vol. 30, no. 1, 2024, Art. no. e13154, doi: 10.1111/jnj.13154. [7] S. B. Proma et al., "Delirium on admission: Patterns in a medicine unit of a tertiary care hospital in Bangladesh," Bangladesh J. Med., vol. 35, no. 1, pp. 20- 25, 2024, doi: 10.3329/bjm.v35i1.69949. [8] Z.- J. Zhang, X.- X. Zheng, X.- Y. Zhang, Y. Zhang, B.- Y. Huang, and T. Luo, "Aging alters Hv1- mediated microglial polarization and enhances neuroinflammation after peripheral surgery," CNS Neurosci. Therapeutics, vol. 26, no. 3, pp. 374- 384, 2020, doi: 10.1111/cns.13271. [9] K. Hatta, "Prevention of delirium via melatonin and orexin neurotransmitter," Juntendo Med. J., vol. 68, no. 1, pp. 12- 16, 2022, doi: 10.14789/jmj.JM12- 0035. [10] R. C. Petersen et al., "Mild cognitive impairment: Clinical characterization and outcome," Arch. Neurol., vol. 56, no. 3, pp. 303- 308, 1999. [11] M. P. Carrasco, M. V. L. Fau- Andrade, J. A. M. Fau- Calderón, M. C. J. Faugonzález, and M. González, "Development and validation of a delirium predictive score in older people," Age Ageing, vol. 43, pp. 346- 351, 2014. [12] J. Kazmierski et al., "Mild cognitive impairment with associated inflammatory and cortisol alterations as independent risk factor for postoperative delirium," Dement. Geriatr. Cogn. Disord., vol. 38, pp. 65- 78, 2024. [13] S. K. Inouye and P. A. Charpentier, "Precipitating factors for delirium in hospitalized elderly persons. Predictive model and interrelationship with baseline vulnerability," J. Am. Geriatr. Soc., vol. 55, pp. 852- 857, 1996. [14] M. J. Kwak et al., "Optimizing delirium care in the era of Age- Friendly Health System," J. Amer. Geriatrics Soc., vol. 72, no. 1, pp. 14- 23, 2024, doi: 10.1111/jgs.18631. [15] A. Johnson, L. Bulgarelli, T. Pollard, S. Horng, L. A. Celi, and R. Mark, "MIMIC- IV (version 2.2). PhysioNet," 2023, doi: 10.13026/nm1- ek67. [16] A. E. W. Johnson et al., "MIMIC- IV, a freely accessible electronic health record dataset," Sci. Data, vol. 10, no. 1, 2023, Art. no. 1, doi: 10.1038/s41597- 022- 01899- x. [17] A. Sherstinsky, "Fundamentals of recurrent neural network (RNN) and long short- term memory (LSTM) network," Physica D: Nonlinear Phenomena, vol. 404, 2020, Art. no. 132306, doi: 10.1016/j.physd. 2019.132306. [18] V. Sundararajan, T. Henderson, C. L. Perry, A. Muggyan, H. Quan, and W. A. Ghali, "New ICD- 10 version of the clarkin comorbidity index predicted in- hospital mortality," J. Clin. Epidemiol., vol. 57, no. 12, pp. 1288- 1294, 2004, doi: 10.1016/j.jclinepi.2004.03.012. [19] M. Mukherjee and M. Khushi, "SMOTE- ENC: A novel SMOTE- based method to generate synthetic data for nominal and continuous features," Appl. Syst. Innov., vol. 4, no. 1, 2021, Art. no. 18, doi: 10.3390/asi4010018. [20] M. S. Haynes, K. D. Alder, C. Toombs, I. C. Amakiri, L. E. Rubin, and J. N. Grauer, "Predictors and sequelae of postoperative delirium in a geriatric patient population with hip fracture," JAOS Glob. Res. Rev., vol. 5, no. 5, 2021, Art. no. e20. [21] T. T. Hsieh, "One- year medicare costs associated with delirium in older hospitalized patients with and without Alzheimer's disease dementia and related disorders," Alzheimer's Dement., vol. 19, no. 5, pp. 1901- 1912, 2023, doi: 10.1002/alz.12826. [22] P. Kumar, T. Raman, M. M. Swain, R. Mishra, and A. Pal, "Hyperglycemia- induced oxidative- nitrosative stress induces inflammation and neurodegeneration via augmented tuberous sclerosis complex- 2 (TSC- 2) activation in neuronal cells," Mol. Neurobiol., vol. 54, no. 1, pp. 238- 254, 2017, doi: 10.1007/s12033- 015- 9667- 3. [23] J. Kang, J. H. An, H. J. Jeon, and Y. J. Park, "Association between ankle brachial index and development of postoperative intensive care unit delirium in patients with peripheral arterial disease," Sci. Rep., vol. 11, no. 1, 2021, Art. no. 12744, doi: 10.1038/s41598- 021- 91990- x. [24] K. V. Keulen et al., "Diabetes and glucose dysregulation and transition to delirium in ICU patients," Crit. Care Med., vol. 46, no. 9, pp. 1444- 1449, 2018, doi: 10.1097/ccm.0000000000003285. [25] World Health Organization, "International classification of diseases (ICD)," Health Organization, 2025, Accessed: Mar. 28, 2025. [Online]. Available: https://www.who.int/standards/classifications/classification- of- diseases

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
