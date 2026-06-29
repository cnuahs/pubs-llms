```
@article{choy2022virtual,
  title={Virtual Reality Assisted Motor Imagery for Early Post-Stroke Recovery: A Review},
  author={Chi Sang Choy and Shaun L. Cloherty and Elena Pirogova and Qiang Fang},
  journal={IEEE Reviews in Biomedical Engineering},
  year={2022},
  volume={16},
  pages={487-498},
  doi={10.1109/rbme.2022.3165062},
  url={https://ieeexplore.ieee.org/document/9749920}
}
```

---

# Virtual Reality Assisted Motor Imagery for Early Post-Stroke Recovery: A Review

Chi Sang Choy \(①\) , Student Member, IEEE, Shaun L. Cloherty \(①\) , Member, IEEE, Elena Pirogova \(①\) , and Qiang Fang \(①\)

(Methodological Review)

Abstract—Stroke is a serious neurological disease that may lead to long- term disabilities and even death for stroke patients worldwide. The acute period, \((\leq 1\) mo post- stroke), is crucial for rehabilitation but the current standard clinical practice may be ineffective for patients with severe motor impairment, since most rehabilitation programs involve physical movement. Imagined movement — the so- called motor imagery (MI) — has been shown to activate motor areas of the brain without physical movement. MI therefore offers an opportunity for early rehabilitation of stroke patients. MI, however, is not widely employed in clinical practice due to a lack of evidence- based research. Here, we review MI- based approaches to rehabilitation of stroke patients and immersive virtual reality (VR) technologies to potentially assist MI and thus, promote recovery of motor function.

Index Terms—Stroke, motor imagery, virtual reality, EEG, rehabilitation, motor recovery, neuroplasticity.

## LIST OF ABBREVIATIONS

- BMRS: Brunnstrom motor recovery stages- BOLD: blood oxygen level-dependent- CID: clinically importance difference- CNN: convolutional neural network- CT: computerized tomography- 2D: 2 dimensional- 3D: 3 dimensional- DoC: disorder of consciousness- EEG: electroencephalogram- ERD: event-related desynchronisation- ErrP: error-related potential- ERS: event-related synchronisation

Manuscript received 27 April 2021; revised 18 January 2022; accepted 19 March 2022. Date of publication 5 April 2022; date of current version 6 January 2023. This work was supported in part by the Li Ka Shing Foundation Cross- Disciplinary Research under Grant 2020LKSFG01C in part by the Australian Government (RTP Stipend Scholarship (RSS- SC)), and in part by the RMIT University (Engineering Top- up Scholarship (E&B). (Corresponding authors: Elena Pirogova; Qiang Fang.)

Chi Sang Choy, Shaun L. Cloherty, and Elena Pirogova are with the School of Engineering, RMIT University, Melbourne, VIC 3000, Australia (e- mail: s3835267@student.rmit.edu.au; s.cloherty@ieee.org; elena.pirogova@rmit.edu.au).

Qiang Fang is with the Department of Biomedical Engineering, Shantou University, Shantou 515063, China (e- mail: qiangfang@stu.edu.cn). Digital Object Identifier 10.1109/RBME.2022.3165062

- EMG: electromyography- FC: functional connectivity- FMA: Fugl-Meyer assessment- fMRI: functional magnetic resonance imaging- FMUE: Fugl-Meyer upper extremity scale- fNIRS: near-infrared spectroscopy- IAF: individual alpha frequency- KI: kinesthetic imagery- M1: primary motor cortex- MAS: modified Ashworth scale- MEG: magnetoencephalogram- MI: motor imagery- MRI: magnetic resonance imaging- NJIT: New Jersey Institute of Technology- OT: occupational therapy- OLED: organic light emitting diode- PET: positron emission tomography- PMC: premotor cortex- PPL: posterior parietal lobe- PT: physiotherapy- rPPL: right posterior parietal lobe- SIS: stroke impact scale- SMA: supplementary motor area- TMS: transcranial magnetic stimulation- VI: visual imagery- VR: virtual reality- WMFT: Wolf motor function test

## I. INTRODUCTION

S TROKE is a leading cause of disability and death around the world [1]–[3]. Among stroke induced disabilities, motor impairment – loss of function in muscle control or movement – is common and significantly affects stroke patients’ ability to perform activities of daily living and to live independently [4]. Recovery of motor function is therefore a key objective of current post-stroke rehabilitation strategies [4].

The significance of early rehabilitation for stroke patients should be emphasised [1], [2]. The progress of motor recovery can be classified by the Brunnstrom motor recovery stages (BMRS) which consists of six different levels of mobility [5]. Stroke patients in the acute period are often classified into stage 1 of the BMRS, when no voluntary movement of the paretic limbs

can be initiated [1], [5], [6]. Prolonged immobility after a stroke may cause adverse effects such as contractures, orthopedic complications, or pressure palsies [2]. The optimal commencement of rehabilitation varies between patients, but early intervention is generally more effective for recovery [1]- [3], [7].

Neurorecovery relies on neuroplasticity which is an ongoing process of reorganising the neuronal components of affected brain networks triggered by intrinsic or extrinsic stimuli [8]- [12]. Neuroplasticity is of utmost importance in the recovery of brain functions, rewiring the neurological components of the brain for restoring damaged neural networks and regaining lost functions [13]- [15]. The first month after stroke onset is the most critical time for neurorecovery as neuroplasticity is most active during the acute period [1], [13]- [15]. Consequently, the urgency of early post- stroke rehabilitation necessitates effective interventions to be implemented in the beginning of rehabilitation.

Stage 1 (Flaccidity) of the BMRs begins immediately after a stroke and is characterised by loss of voluntary motor function. The current general methods for motor rehabilitation include physiotherapy (PT), occupational therapy (OT), robot- therapy, electrical stimulation, optogenetics therapy, pharmacological therapy and virtual reality (VR) assisted motor imagery (MI) therapy [15]- [21]. During Stage 1, conventional physiotherapy and occupational therapy that rely on physical movement are often ineffective [5], [15], [16], [22]. It is important to develop strategies to allow motor rehabilitation to begin as early as possible, especially for stroke patients with severe physical impairment. The motor recovery rate of stroke patients depends on whether the activities performed during rehabilitation can effectively promote neuroplasticity of the lesioned brain. To ensure the quality of neurorehabilitation training, the tasks involved have to be continuously challenging, repetitive, individualised, motivating and intensive [16]. The exiting post- stroke interventions have demonstrated beneficial outcomes, but most are either still in clinical trials or not accessible worldwide due to associated costs [15]- [21]. MI and VR technology, however, are safe and relatively cost- effective; therefore, potentially accessible to a wider population [16], [17], [23].

MI is the ability to mentally perform a movement without moving the body [24], [25]. MI in rehabilitation aids to promote reorganisation of the lesioned brain areas by recruiting undamaged neurons and enhancing brain activity in other neuronal networks [26], [27]. MI abilities of stroke patients may be impaired initially, but this ability can be recovered in the first weeks of stroke onset [28]. Stroke patients with serious motor impairments, nevertheless, are likely not capable of participating in conventional physiotherapy and occupational therapy due to severely paretic limbs [15], [29]. MI only requires stroke patients to simulate a movement mentally which may activate the motor cortex and hence trigger neurorecovery [24], [25]. MI potentially allows stroke patients to rehearse motor tasks that are too difficult or dangerous to perform physically [13], [15]. Stroke patients may mentally activate their motor brain areas even when they are physically inactive [30]. MI ability may deteriorate with time following a stroke, so it could be too late to effectively restore motor functions after the acute period, especially for

stroke patients in Stage 1 of the BMRs [28], [31]. Some stroke patients may have difficulties in imagining movements; nevertheless, the implementation of a virtual environment may make it easier for stroke patients to perform a MI task [16], [17], [28], [31].

VR technology is non- invasive and may potentially accelerate motor recovery by assisting stroke patients to practice MI in an immersive virtual environment without any actual physical movement [17], [32]. Performing MI with VR technology may allow stroke patients to improve their MI capability by recruiting the sensory modality of vision while minimising distractions from the surroundings [25], [32]- [39]. VR technology has been shown to facilitate motor recovery even when stroke patients are in a minimally conscious state [22]. As a result, rehabilitation therapy involving VR assisted MI appears to be ideal for patients in stage 1 of the BMRs [24]- [26], [28].

Despite the fact that VR technology has been shown its benefits for assisting stroke patients to perform MI exercise, VR technology is not implemented in standard rehabilitation programs worldwide [16], [17], [33], [34]. This review aims to provide a general overview of the effectiveness of MI and applicability of VR technology in post- stroke rehabilitation programs.

## II. NEUROPLASTICITY DURING POST-STROKE RECOVERY

Rehabilitation relies on neuroplasticity to restore brain functions [13]- [15]. Neuroplasticity is an ongoing process of the human body that reorganises the neural components in the central nervous system of an individual in response to intrinsic or extrinsic stimuli [8]- [12]. Plasticity mechanisms initiate activity- dependent neural rewiring and synapse strengthening during post- stroke recovery [11], [40], [41]. Synaptic plasticity is a major mechanism that modifies synaptic transmission, thus, changing brain functions accordingly [11], [41]. Homeostatic plasticity regulates both the presynaptic release of and postsynaptic response to neurotransmitters, which is important in restoring an appropriate level of synaptic activity after stroke [40], [42]. Hebbian plasticity strengthens the synaptic connections between presynaptic and postsynaptic neurons that are coincidentally activated. Therefore, the circuitry of the brain that is spared after stroke may be refined to retain proper connections [40], [41], [43]. The cerebral cortex is able to activate spontaneous neuroplasticity after brain damage events such as stroke [8], [12], [44]. Substantial functional brain recovery can be achieved by neuroplasticity in the first weeks post- stroke [8], [12], [45], [46]. Neuroplasticity involves the contralateral hemisphere, subcortical, spinal regions and especially the perilesional tissue in the lesioned brain area [8], [47]. In rodent models, spontaneous neurorecovery peaks at 7 to 14 days following a stroke and is close to completion in 30 days which is within the acute period [1], [40]. Post- stroke recovery is most feasible during the acute period when neuroplasticity is most intense. Therefore, stroke intervention is required at the first instance of stroke onset to facilitate early neurorecovery and to prevent further deterioration of the lesioned brain [1], [8], [12], [40], [47].

> **Image description.** A flow diagram illustrating the typical clinical procedure for stroke management, presented as a sequence of five connected rectangular boxes. The diagram uses a clean, clinical aesthetic with black text on a white background, and the progression between steps is indicated by black arrows.
>
> The process begins with the first step:
> *   **Pre-hospital care (Ambulance services)**
>
> This leads to the second step, which involves diagnostic imaging:
> *   **CT or MRI brain scan (ideally within 1 hour of stroke onset)**
>
> The sequence continues to the third stage, focusing on treatment:
> *   **Medical and/or surgical intervention**
>
> The fourth step in the flow is the initial assessment and intervention phase:
> *   **Rehabilitation (within 48 hours)**
>
> The final step in the depicted clinical pathway is the long-term recovery phase:
> *   **Post-stroke rehabilitation (ideally within 24-48)**
>
> The overall arrangement is linear, moving from left to right, clearly defining the chronological progression of care from the moment of stroke onset through initial treatment and into post-acute recovery.

<center>Fig. 1. Flow chart of the typical clinical procedure for stroke management. </center>

## III. CURRENT CLINICAL PRACTICE FOR STROKE MANAGEMENT

Stroke management requires urgent attention to minimise complications and allow early motor rehabilitation [1]- [3], [6]. The United Kingdom National Clinical Guideline for Stroke is representative of the most up- to- date clinical practice for handling stroke patients worldwide [6]. Fig. 1 shows the general procedure of stroke management from pre- hospital care to post- stroke rehabilitation based on the United Kingdom National Clinical Guideline for Stroke. Firstly, a stroke patient is treated by ambulance services such as medications for controlling stroke [6], [48], [49]. Secondly, after the stroke patient arrives at the nearest hospital that has a stroke team, a computerized tomography (CT) or magnetic resonance imaging (MRI) brain scan of the stroke patient is taken for assessment immediately when facilities are available, ideally within 1h of stroke onset [6], [50], [51]. Thirdly, stroke patients are treated with medical and/or surgical interventions according to individual conditions [6], [52]- [58]. Finally, rehabilitation needs of the stroke patient is assessed and ideally mobilisation should begin within 24- 48 hours [6], [59]. Nevertheless, intensive out- of- bed activities within 24 hours of stroke onset are discouraged [1], [6], [7], [60] All the procedures of stroke management emphasise the necessity of early intervention [1], [3], [6].

### A. Stroke Condition Assessment  

text[[65, 622, 489, 938], [508, 215, 932, 291]]
The progress of post- stroke recovery needs to be frequently monitored in order to evaluate the effectiveness of rehabilitation [6], [33], [61]. Some common clinical guidelines for stroke management and assessing stroke patients include: modified Ashworth scale (MAS), Fugl- Meyer assessment (FMA), Stroke impact scale (SIS) and the Wolf motor function test (WMFT) score [33], [61], [62]. MAS measures the spasticity with a score range: 0, 1, 1+, 2, 3, and 4 [17]. SIS is based on questionnaires reported by stroke patients that evaluate their disability and well- being after stroke with a score range: 0 to 100 [17], [63], [64]. The upper extremity hemiparesis in particular is one of the most common consequence of stroke and the Fugl- Meyer upper extremity scale (FMUE) is a well- established measurement of post- stroke rehabilitation outcome with a 66- point scale [61], [65], [66]. The clinically importance difference (CID) of the FMUE scores has a range from 4.25 to 7.25 due to different aspects of upper extremity movement [61]. The WMFT is generally used for assessing mild to moderate upper extremity weakness in stroke patients [62]. Finally, functional magnetic resonance imaging (fMRI) scans can be used to assess stroke patients 48 hours after onset of motor impairment [47]. The voxels of the scans can be examined to determine any linear correlations between a recovery score and parameter estimates of a task [47]. An earlier rehabilitation ( \(< 30\) days post- stroke) correlates to a greater increase in task- related brain activation and also recovery score such as FMUE [47], [67].

### B. Existing Techniques for Post-Stroke Rehabilitation

Physiotherapy and occupational therapy are the most mainstream clinical practices for post- stroke rehabilitation worldwide, but conventional physical rehabilitation generally has limitations such as labour- and resource- intensive, also modest and delayed effects in some patients [15]- [17]. Other rehabilitation strategies are required to improve the quality of motor rehabilitation such as assisted robot- therapy, electrical stimulation, optogenetic approaches, pharmacological therapy and MI in a virtual environment.

Most existing motor rehabilitation techniques are either in clinical trials or not accessible worldwide due to cost [12], [17], [18], [20], [21], [32]. Assisted robot therapy may facilitate voluntary movement by using exoskeleton with neurofeedback to exert an amount of force that is just enough to help stroke patients to complete a certain movement task [18]. Robotic devices, nevertheless, by design restrict the degrees of movement and portability [18], [68]. Additionally, the high cost of mechatronic devices makes robot- therapy not an available option worldwide [18], [68]. Robot assisted therapy may be too intense for stroke patients at the beginning of rehabilitation when patients' health condition is often weak. Electrical stimulation is able to target specific brain areas to potentially initiate the rewiring of the damaged brain regions, but this technique still requires more risk assessment before it can be widely employed in clinical practice [19]. Optogenetic approaches use bioengineered light- sensitive proteins to stimulate or inhibit targeted cell type or neural circuits with temporal precision to potentially promote neuroplasticity, which cannot be achieved by exiting electrical stimulation techniques [20]. Applying optogenetics in clinical practice, however, needs further development in areas such as gene therapy and opto- electronics [20]. Pharmacological therapy may enhance motor recovery by altering the production of particular neurotransmitters; nevertheless, the potential side effects of drugs varies between different stroke patients, so more studies on pharmacological treatment for stroke patients are required before transitioning to clinical trials [12], [21]. On the contrary, MI is safe because it only relies on stroke patients' ability to mentally perform a movement [17], [24]. VR technology is non- invasive and relatively cost- effective that may accelerate motor recovery by assisting stroke patients to practice

> **Image description.** A technical diagram illustrating the schematic of a fuzzy inference system designed to detect motor imagery (MI) of the right foot by analyzing EEG patterns. The diagram flows from signal input on the left, through a fuzzy logic rule set in the center, to a frequency analysis and final output on the right.
>
> The input stage depicts a stylized human head, representing the source of the EEG signal. The raw signal is labeled "EEG" and is shown being acquired from specific measurement channels: C3, C4, P3, and C3. These channels feed into the fuzzy inference system.
>
> The central part of the diagram is the fuzzy logic engine, which operates based on a set of rules. These rules use linguistic variables ("High" and "Low") to define conditions for the input channels. Two rules are explicitly shown:
> 1. Rule 1: IF C3 is "High" AND C4 is "High" AND P3 is "High" AND C3 is "High" THEN Output is "High".
> 2. Rule 2: IF C3 is "Low" AND C4 is "Low" AND P3 is "Low" AND C3 is "Low" THEN Output is "Low".
>
> To the right of the rules, the system incorporates a frequency analysis component. This is represented by a line graph showing "EEG Power" on the vertical (Y) axis and "Frequency (Hz)" on the horizontal (X) axis. The graph displays a prominent peak (a bell-shaped curve) centered around 10-15 Hz, which is labeled "alpha band," indicating the identification of a specific motor-related frequency band.
>
> The final output of the system is presented below the frequency graph, showing two numerical results: "Output is 0.22" and "Output is 0.12." The overall structure clearly demonstrates how raw EEG data is processed through fuzzy logic and frequency analysis to yield a final classification or detection result.

<center>Fig. 2. Schematic of a fuzzy inference system that detects motor imagery of the right foot via identification of EEG patterns based on a set of rules regarding motor-related frequency bands and EEG power [78]. Figure courtesy of N. Saga et al. </center>

MI in a fully immersive virtual environment which minimises distractions [17], [32].

### C. Computational Intelligence for Stroke Rehabilitation

Artificial intelligence is useful for processing complex signals that are non- stationary and non- linear such as those obtained from stroke patients [69]- [73]. Non- invasive signal acquisition techniques are safe and preferred for stroke patients, especially within the first month of stroke onset [1], [2], [6], [74], [75]. Positron emission tomography (PET), functional magnetic resonance imaging, near- infrared spectroscopy (fNIRS), magnetoencephalography (MEG) and electroencephalography (EEG) are the commonly used non- invasive tools to record signals from the human body [44], [75], [76]. PET, fNIRS and fMRI all perform indirect measurement of brain activity and have a lower temporal resolution than EEG [75], [76]. The high cost and bulkiness of MEG cause difficulties in implementing into general usage for stroke patients [75]. EEG, however, is cost- effective and has a high temporal resolution which property is essential for assistive technology that is designed to provide instant feedback [17], [32], [44], [69], [72], [73].  

text[[71, 683, 500, 938], [520, 81, 939, 306]]
Artificial intelligence is widely applied in EEG- based assistive technology during post- stroke rehabilitation to accurately analyse complex signals [28], [69]- [73], [77]. Neural networks consists of layers of nodes, known as neurons, designed to estimate non- linear decision boundaries [72], [73]. Signals from all EEG channels have some level of correlation and the underlying patterns may be identified by passing through a neural network [69], [72], [77]. Convolutional neural network (CNN) in particular is a widely used method for MI EEG feature extraction and classification because CNN can extract EEG features while reducing the dimensions of input data to trivially identifiable outputs with minimal loss [69]- [71], [77]. The disadvantage of CNN is its requirement of a large data set for offline training and its high computational cost [69]- [71]. Deep transfer learning is applied with CNN to reduce preprocessing time by using a pretrained model which is fine- tuned by new data, then regularising the training process using labels [72]. Fig. 2 illustrates a fuzzy inference system that uses EEG spectral power as input from a person performing MI dorsiflexing of the right foot [78]. There are a set of rules based on the intensity of EEG powers in the motor- related frequency bands: \(\alpha\) and \(\beta\) [17], [36], [78]- [80]. Higher and lower power intensities respectively correspond to two fuzzy labels: High and Low [78]. After performing the required calculation, each rule outputs a value as shown by the numbers in the red rectangles at the bottom right of Fig. 2 [78]. Higher output values are associated with EEG patterns of MI [78]. Fuzzy models utilises rules based on information of neurophysiology and neuroscience to process EEG data; thus, the associated flexible boundary conditions make fuzzy models more suitable for intrinsic EEG feature extraction [72], [73]. Combining fuzzy models with neural networks can handle the rapidly varying EEG signals [72], [73].

## IV. MOTOR IMAGERY

MI is the ability to mentally rehearse a motor action in the working memory without physically movement [24], [25], [30]. This cognitive ability relates to motor planning and motor preparation, as well as suppression of motor execution [24]. The movement parameters involved in MI that need to be considered are repetitiveness, frequency and force level of movement [16], [24]. MI can be studied in four areas: motor control, explicitness, sensory modality and agency [24].

### A. Motor Control

Motor control consists of 3 stages: planning, preparation and execution [24]. MI should correspond to either motor planning or motor preparation [24]. The planning stage can be investigated by providing partial information to a patient to compute a motor command; whereas, in the preparation stage, the motor command is completed and the patient is ready for execution [24]. For instance, a patient is instructed to imagine a movement but not informed which limb should be used [24]. Several action plans may be available in the planning stage because the motor command is only uniquely defined in the preparation stage [24]. Only the execution stage of motor control accompanies muscle activity [24], [81], [82]. MI does not associate with overt muscle contractions; hence, motor inhibition is implemented to suppress physical movement during MI [24], [81], [82].

### B. Motor Imagery Modalities

The type of MI can be classified by the perspective and the sensory experience when imagining an action [24]. Feeling of agency or ownership over an imagined limb is in first person; whereas, mentally simulating a limb which does not belong to oneself is in third person [83]. Explicit and implicit motor imageries are intentionally and unintentionally generated motor imageries respectively [24], [74], [84]. Explicit MI is the internal rehearsal of a movement which accompanies the feeling of the movement consciously [74], [84]. Implicit MI relates to the first- person perspective mental rotation usually with one part of the body [84]. Explicit and implicit motor imageries are used in visual modality, but can also be used in other modalities

such as auditory [24]. Sensory stimuli are often associated with movement [24]. There are two types of MI for visual sensory experiences: kinesthetic and visual as confirmed by magnetoencephalographic (MEG) experiments [24]–[26], [85]. Muscular sensation is only associated with kinesthetic MI [24], [26], [85], [86]. MI recalls the sensory experiences corresponding to movements [24]. Different imagery strategies change the brain activity and corticomotor excitability; therefore, all sensory modalities need to be considered for determining the sensory types that should be focused on [24].

Different modalities of MI may share neural networks to facilitate motor learning [24], [74], [85]. There is an overlap in the premotor- parietal cortices between the brain activities which are explicit MI- related and that are instruction cue- induced [24]. A shared neural mechanism appears to exist between explicit MI and implicit MI during the planning stage of motor control [24], [74]. Even only observing actions performed by another person can increase the activity in the primary motor cortex (MI) and promote motor learning related processes to improve motor function [87], [88]. Mirror neurons are a type of neurons that are activated during movement and also observations of movement [24], [85]. The mirror neuron network allows an observer to mentally imitate the action performed by someone else; thus, the process of analysing the visual information of a movement overlaps with the execution of the movement [24], [85].

### C. Identification of Motor Imagery

The temporal patterns of the \(\alpha\) - band (8- 12 Hz) and the \(\beta\) - band (15- 30 Hz) brain rhythms desynchronise over the sensorimotor cortices when motor execution or MI is performed [17], [36], [79], [80]. The \(\mu\) - band (8- 30 Hz) rhythms correspond to the activity of the mirror neuron system and general sensorimotor functions [17]. The \(\beta\) - band (15- 30 Hz) rhythm is also measured along with the \(\mu\) rhythm as event- related desynchronisation (ERD) while a physical action is executed [17]. Event- related synchronisation/desynchronisation (ERS/ERD) are measured in the \(\mu\) and \(\beta\) frequency bands at the C3 and C4 locations of EEG electrodes for optimal detection of MI of the right and left limbs respectively [17], [79], [80], [89]. Different brain areas are activated or inhibited in motor- related \(\alpha\) (8- 12 Hz)- and \(\beta\) (15- 30 Hz)- frequency bands when performing kinesthetic and visual MI [25]. Kinesthetic imagery (KI) accompanies muscular sensation when performing an imagery task which results in event- related desynchronisation (ERD) of motor- related brain rhythms [25]. Visual imagery (VI) corresponds to the process of analysing the visual information of an imaginary action that leads to event- related synchronisation (ERS) of brain waves in the \(\alpha\) (8- 12 Hz) and \(\beta\) (15- 30 Hz) bands [25]. Typically, KI and VI respectively correspond to ERD and ERS distributions in \(\mu\) - band (8- 30 Hz) [25].

## V. NEURAL CORRELATES OF MOTOR IMAGERY  

text[[68, 878, 490, 938], [508, 321, 930, 380]]
MI activates many cortical and subcortical regions that significantly overlap with motor execution by employing the neurons within those regions of the brain, especially during KI [24]–[26], [85]. When a patient performs a MI task, the relevant brain areas on the side opposite to the imagined movement are expected to be activated [77], [90]. Motor control mainly involves the primary motor cortex (MI) and the secondary motor areas: the premotor cortex (PMC) and the supplementary motor area (SMA) [81].

> **Image description.** A conceptual diagram consisting of two panels, labeled (a) and (b), illustrating the anatomical relationship between specific brain regions and the body's motor control areas.
>
> Panel (a) is a stylized cross-section of a brain, highlighting various cortical regions involved in motor function. The brain structure is divided into several labeled areas:
> *   **Lobes:** The Frontal lobe, Temporal lobe, Occipital lobe, and Cerebellum are visible.
> *   **Motor Regions:** Specific motor areas are highlighted using color coding. The Primary motor cortex is prominently displayed in red. Surrounding motor areas, including the Supplementary motor area and Premotor cortex, are highlighted in blue.
>
> Panel (b) is a simplified, orange-colored outline of a human head and torso, representing the body. This panel illustrates the mapping of motor control to body parts. The labeled body parts include:
> *   Upper limb
> *   Lower limb
> *   Head
> *   Face
> *   Mouth
> A central label, "Motor area," is placed over the body outline, indicating the general region responsible for controlling these listed body parts.
>
> Overall, the two panels work together to conceptually link specific, anatomically defined motor regions in the brain (Panel a) to the corresponding physical body parts that are controlled by those regions (Panel b).

<center>Fig. 3. (a) A conceptual cross-sectional anatomy of the brain showing locations of the primary motor cortex (red), the supplementary motor area (purple) and the premotor cortex (blue). (b) The motor homunculus: a conceptual cross-sectional illustration showing different portions of the motor cortex and the regions of the body they control. </center>

Fig. 3(a) shows the approximate locations for the motor areas of the brain which includes M1, SMA and PMC in red, purple and blue colour respectively. Fig. 3(b) is the motor homunculus which conceptually shows that different areas of the motor cortex control a specific body part [91]. Some body parts involve a larger portion of the motor cortex depending on the complexity involved in the corresponding movement performed by those body parts [91]. For instance, the upper limb is controlled by a larger area of the motor cortex than the lower limb [91]. M1 is best corresponded to motor execution [24]. There are differences in the M1 definition between various studies which cause discrepancies. The best practice so far is to use a probabilistic map for anatomical nomenclature [24], [85]. Somatotopically organised MI- induced activity involves the premotor and supplementary motor areas which are most likely substrates for MI because these areas are mainly responsible for the planning and preparation stages of motor control [24]. The premotor cortex is the main node of MI as determined by a graph- theory analysis, which is in agreement that a part of the premotor cortex connects the cognitive and motor sectors of the brain [24]. MI, however, is more measurable with SMA [81].

Activity can also be observed in the posterior parietal cortex when performing MI tasks [24]. MI ability is functional for some patients with lesions of the parietal cortex [92]. Patients with impaired posterior parietal cortex, however, cannot accurately imagine movements and may unknowingly execute a movement while trying to imagine the movement [24]. If the damage is to the precentral motor cortex of the patient instead, then the patient's movement is impaired but MI abilities may be preserved [24].

The brain's functional connectivity (FC) of stroke patients' motor system is damaged after the occurrence of stroke [86], [93]. A healthy neuronal activity connection between different brain areas is associated with a high FC [86], [93]. FC corresponds to the synchrony of intrinsic blood oxygen level- dependent (BOLD) signal fluctuations of the brain which can be studied by fMRI [86]. Real- time fMRI can be used in MI

training which has illustrated that the right premotor area is important during MI [94], [95]. As reported in previous studies that the FC between motor- related regions and PMC may be altered by real- time fMRI MI training. Hence, facilitating MI practice of stroke patients by providing performance feedback based on specific target brain regions is beneficial [94]. MI, SMA, PMC, cerebellum, putaman, posterior parietal lobe (PPL), and thalamus are critical for motor sequence training [26], [94]. In particular, the FC between PMC and right posterior parietal lobe (rPPL) is found to attenuate significantly after real- time fMRI MI training, thus, indicating the corresponding function may be altered accordingly [94].

The stage of motor control in a MI task determines the extent of brain activity in the MI [24]. MI activity is likely to be more intense in the preparation stage than during the planning stage of motor control [24]. The main difference between VI and KI is observed in the frontal brain area [25]. The frontal cortex is active during VI and suppressed for KI [25]. VI mainly induces activities in the visually related brain regions and superior parietal lobule; whereas, KI mostly activates motor- related areas and the inferior parietal lobule, a crucial brain region during MI [24], [85]. Only the kinesthetic type of MI changes the corticomotor excitability [24]. The visual type of MI can have either a first or third person perspective (interior view and external view respectively) [25], [31]. The first person perspective influences the sensorimotor areas more significantly than the third person perspective [24]- [26], [85].

The "virtual hands" experiment shows that the motor cortex is activated during motor imagery [96]. The individual alpha frequency (IAF; \(9.45 \pm 0.54 \mathrm{~Hz}\) ) for each subject is used to account for between- subject variability of the alpha peak and define the frequency bands in the "virtual hands" experiment [90], [96]. The centroparietal areas of the ipsilesional hemisphere and the central midline in the \(\alpha\) band ( \(\mathrm{IAF} = - 2\) to \(2 \mathrm{~Hz}\) ) illustrate significant desynchronisation as detected at CP5, CP3 and Cz locations of EEG electrodes. At the \(\beta 1\) band ( \(\mathrm{IAF} = 2\) to \(11 \mathrm{~Hz}\) ), significant desynchronisation is mostly at the ipsilesional hemisphere (C1, CP1), but brain activity at C2 and Cz locations of EEG electrodes is also intense [96]. The C4 and FC2 locations of EEG electrodes at the contralesional hemisphere measure significant desynchronisation in the \(\alpha\) and \(\beta 1\) bands, respectively, post- intervention [96]. These results are consistent with previous studies that MI activates the motor brain areas: MI, PMC and SMA which are located around the central brain region and may promote neuroplasticity to restore motor functions.

The prefrontal cortex, anterior cingulate cortex, and premotor cortex are activated during MI [24]. The ventral prefrontal cortex and the anterior cingulate cortex correspond to the suppression of movement during the preparation stage of motor control [24]. During MI, the MI activity is suppressed by SMA [82]. There appears to be a relationship between MI and motor inhibition [24]. MI also uses subcortical motor areas such as basal ganglia and cerebellum, but is slowed by Parkinson's disease. Hence, the basal ganglia may change parameters that are not related to the contents of MI such as signal transmission speed [24], [26], [85]. The cerebellum may process efference copy from the motor cortex, thus, also assist in mental simulation [24].

## VI. MOTOR IMAGERY FOR POST-STROKE REHABILITATION

VI. MOTOR IMAGERY FOR POST-STROKE REHABILITATIONMI in rehabilitation aims to teach patients ways to promote reorganisation of the lesion areas by recruiting undamaged neurons and enhancing brain activity in other neuronal loops [26], [27]. Stroke patients with serious motor impairments are not capable to participate in conventional physiotherapy and occupational therapy due to severely paretic limbs, but stroke patients can activate their motor brain areas by MI even when they are physically inactive [15], [16], [30]. MI is a complex ability that requires practice and the brain's ability to activate certain areas of the motor cortex [8], [15], [17]. MI increases the repetitiveness of specific motor-related tasks. Hence, mental practice may significantly facilitate neuroplasticity and enhance motor recovery [30]. It is also found that stroke patients who have performed both mental and physical practice in rehabilitation illustrate better ability to learn skills in new environments than stroke patients who only participate in physical exercise [26], [30]. MI in combination with conventional physical practice for rehabilitation has a better outcome than only practising physical therapy [26], [27], [97]. MI combining with physical exercise of the same movement is most effective because it is easier for stroke patients to imagine skills that have been previously performed, also the same neural and muscular areas are simultaneously activated [30], [98].

### A. Motor Imagery Impairment

Certain mental practices are ineffective for patients whose ability to imagine movement is impaired. However, stroke patients may benefit from imaging movement by using different strategies over time [28]. Some stroke patients may be more visually inclined at the beginning of rehabilitation and their imagery abilities may gradually become more motor- based after first weeks of stroke onset [28]. MI allows stroke patients to rehearse motor tasks that are too difficult and dangerous to physically perform. Despite the potential benefits of MI, mental exercise may not be practical for all acute stroke patients with impaired imagery abilities at the start of rehabilitation.

Neuroplasticity may likely be an important factor in MI performance which is most active during the first month of poststroke recovery; thus, stroke patients' MI ability may deteriorate and motor rehabilitation may be ineffective over a certain period of time [8], [15], [29], [31]. VR technology may allow stroke patients to improve their MI capability by visually inducing an illusion of real movement while minimising distractions from the surroundings [16], [29], [35]- [39], [44]- [46]. Consequently, the implementation of VR technology to assist stroke patients to perform MI tasks is gaining popularity [15]- [17], [33].

## VII. VR ASSISTED MOTOR IMAGERY REHABILITATION

The main goal of VR technology in rehabilitation is to create an environment that is able to provide patients with multisensory feedback to simulate the real actions and motivate patients to participate in MI tasks for achieving the required level of repetitiveness and intensity of training [16], [99]. There are three important features of VR technology for MI performance:

TABLEI PROS & CONS OF DIFFERENT VR STUDIES WITH RESPECTIVE PARTICIPANTS' PROFILES AND TRAINING TIMEPRAMES

| Method | Time After Stroke | Sample Size | Frequency | Outcome | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1. REINVENT (2019) [33] | 59-186 months | 4 subjects | 8 sessions (1.5h each) over 3 weeks. | SIS: +10 to +50. No significant improvement in FMUE & MAS. | Purely Mental Control, Fully Immersive VR, Multisensory Stimuli. | Small Sample Size. |
| 2. NeuRow (2019) [17] | 10 months | 1 subject | 10 sessions (15min each) over 3 weeks. | FUME: +9 post-intervention, then +4 one-month follow-up. | Motion Observation, Fully Immersive VR, Multisensory Stimuli. | No Control Group Comparison. |
| 3. Unity3D + 3dsMax (2019) [99] | Healthy | 5 subjects | 20 feedback & 20 no feedback 8s-trials in 4 days. | MI accuracy significantly improved. | Purely Mental Control, Fully Immersive VR, Multisensory Stimuli. | No Stroke Patients. |
| 4. NJIT (2017) [101] | 6-92 days | 14 subjects | 8 sessions (1h each) over 6 months. | 12 subjects FUME: + > 10; 2 subjects similar FUME increase. | Robot-Assistance, Multisensory Stimuli. | No Neurofeedback, Partial immersive VR, Small Sample Size. |
| 5. Virtual Hands (2015) [96] | 1-6 months | VR & control: 14 subjects each. | 3 weekly sessions (30 9s-trials each, 1.5s interval) over 1 month. | VR FMA: +20.6. Control: no significant improvement | Purely Mental Control, Visual Stimuli. | Partial VR Immersion. |

immersion, interaction and imagination [99]. Stroke patients are more motivated in VR assisted MI rehabilitation if the visual environment is more complex [99]. VR allows patients to visualise the paralysed body part that facilitates the activation of the premotor cortex leading to faster motor learning [97]. The measured MI signals control the VR simulation [97]. The effectiveness of MI depends on the strategies of implementing MI into rehabilitation.  

text[[65, 578, 485, 923], [503, 456, 923, 547]]
It is important to evaluate MI performance. Online monitoring of MI performance based on neurofeedback can provide information for reviewing the usefulness of MI being incorporated in rehabilitation [24]. Sensorimotor rhythm is modulations of \(\alpha\) - or \(\beta\) - band EEG oscillations at central electrodes [24]. Sensorimotor rhythms are more intense at rest and decrease when executing and imagining a movement leading to event- related desynchronisation (ERD) [24]. The level of ERD indicates the extent of a patient's engagement in a MI task [24]. There are significant difficulties for using VR technology in rehabilitation such as the lengthy training time that leads to fatigue in patients, so the quality of VR technology needs to be evaluated [34]. Error- related potential (ErrP) is an event- related potential (ERP) component for correcting errors in VR devices [34]. If the response given by the VR device is different to a patient's intention to perform a certain task, then ErrP is induced [34], [100]. There are three phases in VR- based rehabilitation: pre- rehabilitation, rehabilitation training and post- rehabilitation [97]. In pre- rehabilitation, a pilot study involves the design and development of MI based VR systems by obtaining the MI rhythms for the required movements from patients [97]. Rehabilitation training involves testing of the developed VR- MI system, by having some patients in an experimental group and some in a control group to practise rehabilitation with the system and without the system, respectively [97]. In post- rehabilitation, clinical assessment scales such as FMA and MAS are used to evaluate the level and rate of motor recovery of both the experimental and control groups after rehabilitation training [17], [33], [61], [97].

### A. Typical VR Technology for Motor Rehabilitation

Table I shows the typical VR motor rehabilitation technologies that only require MI and do not rely on residual movement from stroke patients. The platform REINVENT allows chronic post- stroke patients to move a virtual avatar arm via their EEG signals, providing action observation neurofeedback generated by patients in a fully immersive VR environment [33]. In the REINVENT study, three of the four participants with a relatively greater mobility had no indication of significant motor function improvement after using the REINVENT VR platform [33]. Only the Stroke Impact Scale (SIS) is improved consistently for all four participants ranging from +10 to +50 in the REINVENT study (Table I) [33]. Social interaction with the therapy team may likely contribute to the SIS improvement [33]. The NeuRow study also involves a fully immersive VR, but there is no control group in the study to make a comparison with the VR users [17]. The positive outcomes from NeuRow need to be interpreted with caution [17]. The "virtual hands" technology positive outcomes are indicated by the corresponding stimulation of sensorimotor areas, not the MI area during MI. Hence, it is likely that compensatory changes in the brain are dominant in motor recovery when using the "virtual hands" [96], [102], [103]. The Unity3D + 3dsMax software (Table I) creates a 3D virtual environment

> **Image description.** A schematic flow diagram illustrating the REINVENT neurofeedback loop, detailing the three stages of a system designed to allow a user to control a virtual environment using brain signals.
>
> The diagram is divided into three main vertical sections: 1. Interfacing, 2. Processing, and 3. Interaction.
>
> **1. Interfacing (Left Section):**
> This stage depicts the user and the initial data acquisition. On the far left, a person is shown wearing a VR headset and what appears to be an EEG cap, representing the VR user. An arrow labeled "Evoked responses" points from the user to a box labeled "Acquisition Clients." This box represents the hardware responsible for receiving the raw brain signals.
>
> **2. Processing (Center Section):**
> This central section handles the analysis of the acquired data. It consists of two main functional boxes: "Feature Extraction" and "Signal Processing." Data flows from the "Acquisition Clients" into "Feature Extraction," and subsequently into "Signal Processing." A cylindrical icon, representing a data log, is labeled "LSL" (Low-Level Signal/Data Log). Arrows indicate that the "LSL" log receives data from both the "Feature Extraction" and "Signal Processing" stages, serving as a record of the extracted features.
>
> **3. Interaction (Right Section):**
> This final stage represents the output and feedback loop. The section shows a visual representation of a VR training environment, specifically a grassy outdoor scene resembling a volleyball court. An arrow labeled "Control Signal" originates from the "Signal Processing" box and points into the VR scene, indicating that the processed brain features are converted into commands for the virtual world. An arrow labeled "Visual and vibrotactile feedback" points from the VR scene back toward the user, completing the feedback loop.
>
> The overall flow demonstrates a continuous cycle: the user generates evoked responses (Interfacing), these are analyzed and recorded (Processing), and the resulting control signals drive the virtual environment, which then provides sensory feedback to the user (Interaction).

<center>Fig. 4. Schematic of REINVENT neurofeedback loop [33]. 1. Interfacing: the acquisition clients receive the evoked brain signals from the VR user. 2. Processing: the features of the evoked responses are extracted and recorded. 3. Interaction: the extracted patterns are output as control signals of the VR interface; visual feedback via the VR goggle; vibrotactile feedback via two Oculus touch controllers to the VR user. Figure courtesy of A. Vourvopoulos et al. </center>

that provides a range of daily living scenes such as volleyball court and garden to suit individual needs [99]. Some common clinical rehabilitation MI exercises involve grasping and limb rotation [99]. VR MI training can also include daily life tasks such as playing volleyball and catching a butterfly [99]. The results from Unity3D + 3dsMax shown in Table I, however, are based on only healthy participants; therefore, it is not clear whether the same level of beneficial outcome can be observed in stroke patients.

Fig. 4 illustrates how a stroke patient can control virtual avatar arms by MI alone using the REINVENT platform. The stroke patient wears an EEG cap to measure the brain signals corresponding to MI, meanwhile, electromyography (EMG) records the overt muscle activity and the neurophysiological data are transmitted to the interfacing layer. The evoked brain signals are then analysed in the processing layer, where certain signal features are extracted and recorded. Finally, the interaction layer converts the extracted EEG and EMG features to control signals of the VR system which provides visual and vibrotactile feedback to the stroke patient via the VR goggle (two OLED displays) and two oculus touch controllers with 6 degrees of freedom respectively [33]. Stroke patients, thus, can focus on MI tasks in a fully immersive virtual environment. The experimental procedure of the REINVENT VR study is representative of the process of a typical clinical trial. Stroke patients' motor functions are examined pre- intervention and post- intervention using clinical scales, Transcranial Magnetic Stimulation (TMS), MRI and questionnaires to demonstrate the effectiveness and feasibility of the REINVENT platform. The resting state of stroke patients provides the baseline data which are measured when stroke patients eyes are open and closed [33]. All 4 stroke patients in the REINVENT study had 8 sessions in 3 weeks, except for one patient who had 16 sessions in 6 weeks [33]. Each training session consists of 4 blocks each with 20 trials [33]. Each trial consists of the baseline with 10 seconds

and the MI task with 20 seconds [33]. All stroke patients show improvement in motor functions of upper limbs. Stroke patients with more severe motor impairment appear to illustrate better outcome with EEG- based neurofeedback; whereas, EMG- based neurofeedback may enhance motor recovery more for stroke patients with relatively milder motor disabilities [33].

The "virtual hands" are another type of EEG- based VR technology [96]. The hands of a stroke patient, who is wearing an EEG cap, are placed in an adjustable forearm orthosis covered with a white blanket on a desk. The white blanket provides visual feedback as a virtual representation of the stroke patients' actual hands. The movement of the "virtual hands" are controlled by the stroke patients' imagination of hand movements. A therapist is required to monitor and analyse the stroke patient's brain activity and muscle relaxation of the paretic hand and forearm by EEG and EMG respectively [96].

### B. Feasibility of VR-Based Technology for Motor Rehabilitation

The effect of MI on the motor areas of the brain is reproducible and a potentially feasible clinical intervention for rehabilitation [17], [26], [33], [96]. Virtual reality in combination with EEG has also demonstrated beneficial outcomes for patients with disorder of consciousness (DoC) which is often the initial state of many stroke patients [22]. 3D- VR devices have shown to be effective in providing patients a full immersion experience that helps patients to better engage in MI tasks in comparison to 2D- VR approaches which are only capable of partial immersion of VR [35]- [37]. VR helps patients in stage 1 of the BMRs to begin MI practice once their vitals have become stable even when no voluntary movement can be initiated; hence, rehabilitation is not delayed by physical difficulties. Haptic and auditory feedbacks can also be implemented in VR technology which provides vibrotactile feedback during MI tasks inducing an illusion of

performing a physical movement such as rowing a boat [17], [33]. VR technology with the integrated neurofeedback presents an innovative approach to facilitating neurorehabilitation of stroke patients in stage 1 of the BMRS. It can be an integral part of post- stroke rehabilitation programs around the world if there is substantial evidence to indicate its benefits.

## VIII. CONCLUSION

There is evidence showing the potential benefit of MI for post- stroke rehabilitation, even when conventional methods relying on residual movement such as physiotherapy are ineffective [15], [16], [22]. VR technology may assist MI performance in recovering motor functions after stroke as shown by the VR studies presented in Table I. There is barely any large- scale research incorporating MI in rehabilitation during the acute period \((< 1 \mathrm{~m o})\) , hence the opportunities and possibilities offered by MI in the acute period of post- stroke are not fully understood [28], [84]. Several existing studies indicate potential improvement in motor function after using VR technology for performing MI tasks [29], [33], [68], [96], [99], [101], [104]- [106]. Future experiments may focus on the improvement of VR technology and understanding of post- stroke motor recovery in order to produce cost- effective and user- friendly VR devices suitable for stroke patients with various medical backgrounds in different clinical settings. The effectiveness and applicability of MI and VR technology for acute stroke patients in post- stroke motor rehabilitation may be evaluated further by investigating whether MI induces neuronal responses, and confirming whether use of VR technology can enhance neural responses within the first month post- stroke. In addition, it is also important to confirm which specific locations of the motor cortex are activated, i.e. regions of the brain corresponding to particular MI tasks such as fingers flexion and shoulder rotation [107].

Stroke may affect different patients in various ways, hence certain MI tasks may be more suitable for different stroke patients [13], [15], [28], [31]. It is essential to accurately identify the type of suitable MI tasks which can satisfy the diverse needs of stroke patients. VR- assisted MI may soon be implemented in standard rehabilitation protocols to improve the quality of post- stroke motor recovery programs if there is substantial evidence of benefits from practising MI and using VR technology.  

text[[68, 713, 488, 937], [505, 81, 926, 140]]
VR- assisted MI may be a promising strategy for facilitating post- stroke recovery. MI activates the brain areas responsible for physical movement such as the M1, PMC and SMA; hence, MI appears to be an effective way to initiates neurorehabilitation as soon as stroke patients are in a stable condition. VR technology assists in engaging stroke patients with MI tasks in a fully immersive virtual environment that may enhance MI capability and potentially promote neurorecovery, especially during the early stage of post- stroke recovery when the patients cannot initiate any voluntary movement. VR technology is safe and may facilitate the effect of MI by providing constant multi- sensory feedback to simulate the real movement. Using VR- assisted MI, along with the conventional physical therapy and occupational therapy, may be a clinically feasible approach for early motor recovery, particularly during stage 1 of the BMRS. This review is an attempt to provide insights for developing future experiments and guide further investigation of the feasibility of applying MI combined with new immersive technologies such as VR for motor function recovery.

## IX. DECLARATIONS

Availability of data and materials: Not applicable.

Ethics approval and consent to participate: Not applicable.

Competing interests: The authors declare that they have no competing interests.

Consent for publication: Fig. 1 and Table I are authors' original work. The authors would like to thank N. Saga et al. and A. Vourvopoulos et al. for providing permission to publish Figs. 2 and 4, respectively. Fig. 3 is a modified version of figures from a copyleft source.

Authors' contributions: CSC performed the literature search and drafted the manuscript. SLC, EP and QF contributed concepts. All authors edited and revised the manuscript. All authors read and approved the manuscript.

## ACKNOWLEDGMENT

The authors would like to express their gratitude for a constructive discussion about EEG experiment and analysis with Dr Akshay Kumar, Mr Bingrui Ding and Mr Jiaming Li from the Department of Biomedical Engineering, Shantou University.

## REFERENCES

[1] E. R. Coleman et al., "Early rehabilitation after stroke: A narrative review," Curr. Atherosclerosis Rep., vol. 19, no. 12, pp. 1- 12, 2017.  
[2] E. C. Jauch et al., "Guidelines for the early management of patients with acute ischemic stroke: A guideline for healthcare professionals from the american heart association/american stroke association," Stroke, vol. 44, no. 3, pp. 870- 947, 2013.  
[3] L. B. Morgenstern et al., "Guidelines for the management of spontaneous intracerebral hemorrhage: A guideline for healthcare professionals from the american heart association/american stroke association," Stroke, vol. 41, no. 9, pp. 2108- 2129, 2010.  
[4] P. Langhorne, F. Coupar, and A. Pollock, "Motor recovery after stroke: A systematic review," Lancet Neurol., vol. 8, pp. 741- 754, 2009.  
[5] S. Brunnstrom, Movement Therapy in Hemiplegia: A Neurophysiological Approach. New York, NY, USA: Harper & Row, 1970, pp. 113- 122.  
[6] Intercollegiate Stroke, ICSWP, National Clinical Guideline for Stroke, A. Bowen, M. James, and G. Young, Eds. London, U.K.: Royal College Phys., 2016.  
[7] E. Lynch, S. Hillier, and D. Cadilhac, "When should physical rehabilitation commence after stroke: A systematic review," Int. J. Stroke, vol. 9, no. 4, pp. 468- 478, 2014.  
[8] C. Alia et al., "Neuroplastic changes following brain ischemia and their contribution to stroke recovery: Novel approaches in neurorehabilitation," Front. Cellular Neurosci., vol. 11, no. Mar., pp. 1- 22, 2017.  
[9] A. Sale, N. Berardi, and L. Maffei, "Enrich the environment to empower the brain," Trends Neurosciences, vol. 32, no. 4, pp. 233- 239, 2009.  
[10] M. Puderbaugh and P. D. Emmady, "Neuroplasticity," in StatPearls [Internet]. St. Petersburg, FL, USA: StatPearls Publishing, 2020.  
[11] P. M- Aparicio and A. R- Moreno, "The impact of studying brain plasticity," Front. Cellular Neurosci., vol. 13, no. Feb. pp. 1- 5, 2019.  
[12] S. C. Cramer et al., "Harnessing neuroplasticity for clinical applications," Brain, vol. 134, no. 6, pp. 1591- 1609, 2011.  
[13] S. C. Cramer, "Repairing the human brain after stroke: I. mechanisms of spontaneous recovery," Ann. Neurol., vol. 63, no. 3, pp. 272- 287, 2008.  
[14] S. C. Cramer, "Repairing the human brain after stroke. II. restorative therapies," Ann. Neurol., vol. 63, no. 5, pp. 549- 560, 2008.
[15] R. Mane, T. Chouhan, and C. Guan, "BCI for stroke rehabilitation: Motor and beyond," J. Neural Eng., vol. 17, no. 4, 2020, Art. no. 041001.  
[16] G. Saposnik and M. Levin, "Virtual reality in stroke rehabilitation: A meta-analysis and implications for clinicians," Stroke, vol. 42, no. 5, pp. 1380- 1386, 2011.  
[17] A. Vourvopoulos et al., "Efficacy and brain imaging correlates of an immersive motor imagery BCI- driven VR system for upper limb motor rehabilitation: A clinical case report," Front. Hum. Neurosci., vol. 13, no. Jul., pp. 1- 17, 2019.  
[18] C. Duret, A. G. Grosmaire, and H. I. Krebs, "Robot- assisted therapy in upper extremity hemiparesis: Overview of an evidence- based approach," Front. Neurol., vol. 10, no. APR, pp. 1- 8, 2019.  
[19] S. C. Bao, A. Khan, R. Song, and R. K. Y. Tong, "Rewiring the lesioned brain: Electrical stimulation for post- stroke motor restoration," J. Stroke, vol. 22, no. 1, pp. 47- 63, 2020.  
[20] M. Y. Cheng, M. Aswendt, and G. K. Steinberg, "Optogenetic approaches to target specific neural circuits in post- stroke recovery," Neurotherapeutics, vol. 13, no. 2, pp. 325- 340, 2016.  
[21] A. Kumar and T. Kitago, "Pharmacological enhancement of stroke rehabilitation," Curr. Neurol. Neurosci. Rep., vol. 19, no. 7, pp. 1- 11, 2019.  
[22] M. G. Maggio et al., "Virtual reality based cognitive rehabilitation in minimally conscious state: A case report with EEG findings and systematic literature review," Brain Sci., vol. 10, no. 7, pp. 1- 16, 2020.  
[23] A. Biaisucci, B. Franceschiello, and M. M. Murray, "Electroencephalography," Curr. Biol., vol. 29, no. 3, pp. R80- R85, 2019.  
[24] T. Hanakawa, "Organizing motor imagers," Neurosci. Res., vol. 104, pp. 56- 63, 2016. [Online]. Available: http://dx.doi.org/10.1016/j.neures. 2015.11.003  
[25] P. Chholak et al., "Visual and kinesthetic modes affect motor imagery classification in untrained subjects," Sci. Rep., vol. 9, no. 1, pp. 1- 12, 2019.  
[26] J. Munzert, B. Lorey, and K. Zentgraf, "Cognitive motor processes: The role of motor imagery in the study of motor representations," Brain Res. Rev., vol. 60, no. 2, pp. 306- 326, 2009.  
[27] K. B. Wilkins, J. P. Dewald, and J. Yao, "Intervention- induced changes in neural connectivity during motor preparation may affect cortical activity at motor execution," Sci. Rep., vol. 10, no. 1, pp. 1- 13, 2020.  
[28] S. de Vries, M. Tepper, B. Otten, and T. Mulder, "Recovery of motor imagery ability in stroke patients," Rehabil. Res. Pract., vol. 2011, pp. 1- 9, 2011.  
[29] G. Saposnik et al., "Effectiveness of virtual reality using wi gaming technology in stroke rehabilitation: A pilot randomized clinical trial and proof of principle," Stroke, vol. 41, no. 7, pp. 1477- 1484, 2010.  
[30] S. J. Page and H. Peters, "Mental practice: Applying motor PRACTICE and neuroplasticity principles to increase upper extremity function," Stroke, vol. 45, no. 11, pp. 3454- 3460, 2014.  
[31] E. Daprati, D. Nico, S. Duval, and F. Lacquaniti, "Different motor imagery modes following brain damage," Cortex, vol. 46, pp. 1016- 1030, 2010.  
[32] M. A. Cervera et al., "Brain- computer interfaces for post- stroke motor rehabilitation: A meta- analysis," Ann. Clin. Transl. Neurol., vol. 5, no. 5, pp. 651- 663, 2018.  
[33] A. Vourvopoulos et al., "Effects of a brain- computer interface with virtual reality (VR) neurofeedback: A pilot study in chronic stroke patients," Front. Hum. Neurosci., vol. 13, no. Jun., pp. 1- 17, 2019.  
[34] R. Abiri, S. Borhani, E. W. Sellers, Y. Jiang, and X. Zhao, "A comprehensive review of EEG- based brain- computer interface paradigms," J. Neural Eng., vol. 16, no. 1, 2019, Art. no. 011001.  
[35] K. Lafleur, K. Cassady, A. Doud, K. Shades, E. Rogin, and B. He, "Quadcopter control in three- dimensional space using a noninvasive motor imagery- based brain- computer interface," J. Neural Eng., vol. 10, no. 4, 2013, Art. no. 046003.  
[36] D. J. Mcfarland, W. A. Sarnacki, and J. R. Wolpaw, "Electroencephalographic (EEG) control of three- dimensional movement," J. Neural Eng., vol. 7, no. 3, pp. 1- 31, 2014.  
[37] Z. Cai et al., "Design & control of a 3D stroke rehabilitation platform," in Proc. IEEE Int. Conf. Rehabil. Robot., 2011, pp. 1- 6.  
[38] A. Abu- Rumble, E. Zakkay, L. Shmuelof, and O. Shriki, "Co- adaptive training improves efficacy of a multi- day EEG- based motor imagery BCI training," Front. Hum. Neurosci., vol. 13, no. Oct., pp. 1- 8, 2019.  
[39] O. Alkoby, A. Abu- Rumble, O. Shriki, and D. Todder, "Can we predict who will respond to neurofeedback? a review of the inefficacy problem and existing predictors for successful EEG neurofeedback learning," Neuroscience, vol. 378, pp. 155- 164, 2018.
[40] T. H. Murphy and D. Corbett, "Plasticity during stroke recovery: From synapse to behaviour," Nature Rev. Neurosci., vol. 10, no. 12, pp. 861- 872, 2009.  
[41] A. Citri and R. C. Malenka, "Synaptic plasticity: Multiple forms, functions, and mechanisms," Neuropsychopharmacol., vol. 33, no. 1, pp. 18- 41, 2008.  
[42] G. G. Turrigiano and S. B. Nelson, "Homeostatic plasticity in the developing nervous system," Nature Rev. Neurosci., vol. 5, no. 2, pp. 97- 107, 2004.  
[43] K. D. Miller, L. F. Abbott, and S. Song, "Competitive hebbian learning through spike- timing- dependent synaptic plasticity," Nature Neurosci., vol. 3, pp. 919- 926, 2000. [Online]. Available: http://neurosci.nature.com  
[44] C. Gerloff et al., "Multimodal imaging of brain reorganization in motor areas of the contralesional hemisphere of well recovered patients after capsular stroke," Brain, vol. 129, no. 3, pp. 791- 808, 2006.  
[45] C. Grefkes and G. R. Fink, "Connectivity- based approaches in stroke and recovery of function," Lancet Neurol., vol. 13, no. 2, pp. 206- 216, 2014.  
[46] N. Sharma and L. G. Cohen, "Recovery of motor function after stroke," Dev. Psychobiol., vol. 54, no. 3, pp. 254- 262, 2012.  
[47] N. S. Ward, M. M. Brown, A. J. Thompson, and R. S. Frackowiak, "Neural correlates of motor recovery after stroke: A longitudinal fMRI study," Brain, vol. 126, no. 11, pp. 2476- 2496, 2003.  
[48] P. Langhorne and S. Ramachandra, "Organised inpatient (stroke unit) care for stroke: Network meta- analysis," Cochrane Database Systematic Rev., no. 4, 2020. [Online]. Available: https://doi.org/10.1002/14651885.CD000197. pub  
[49] Y. Sun, D. Paulus, M. Eyssen, J. Maervoet, and O. Saka, "A systematic review and meta- analysis of acute stroke unit care: What's beyond the statistical significance," BMC Med. Res. Methodol., vol. 13, no. 1, pp. 1- 11, 2013.  
[50] G. Mair et al., "Sensitivity and specificity of the hyperdense artery sign for arterial obstruction in acute ischemic stroke," Stroke, vol. 46, no. 1, pp. 102- 107, 2015.  
[51] C. H. Riedel, J. Zoubie, S. Ulmer, J. Gierthmuellen, and O. Jansen, "Thin- slice reconstructions of nonenhanced CT images allow for detection of thrombus in acute stroke," Stroke, vol. 43, no. 9, pp. 2319- 2323, 2012.  
[52] S. Middleton et al., "Implementation of evidence- based treatment protocols to manage fever, hyperglycaemia, and swallowing dysfunction in acute stroke (QASC): A cluster randomised controlled trial," Lancet, vol. 378, no. 9804, pp. 1699- 1706, 2011.  
[53] K. Ali et al., "The stroke oxygen pilot study: A randomized controlled trial of the effects of routine oxygen supplementation early after acute stroke- effect on key outcomes at six months," PLoS One, vol. 8, no. 6, pp. 1- 8, 2013.  
[54] P. M. Rothwell, A. Algra, Z. Chen, H. C. Diener, B. Norrving, and Z. Mehta, "Effects of aspirin on risk and severity of early recurrent stroke after transient ischaemic attack and ischaemic stroke: Time- course analysis of randomised trials," Lancet, vol. 388, no. 10042, pp. 365- 375, 2016.  
[55] G. Gade et al., "Impact of an inpatient palliative care team: A randomized controlled trial," J. Palliat. Med., vol. 11, no. 2, pp. 180- 190, 2008.  
[56] M. Wardlaw, V. Murray, E. Berge, and G. J. del Zoppo, "Thrombolysis for acute ischaemic stroke," Cochrane Database Systematic Rev., Hoboken, NJ, USA: John Wiley, 2014. [Online]. Available: https://doi.org/10.1002/14651885.CD000213. pub3  
[57] L. H. Bath, PM and L. Everton, "Swallowing therapy for dysphagia in acute and subacute stroke," Cochrane Database Systematic Rev., 2018. [Online]. Available: https://doi.org/10.1002/14651885.CD000323. pub3  
[58] L. Back, V. Nagaraja, A. Kapur, and G. Eslick, "Role of decompressive hemicraniectomy in extensive middle cerebral artery strokes: A meta- analysis of randomised trials," Intern. Med. J., vol. 45, no. 7, pp. 711- 717, 2015.  
[59] P. Langhorne and S. Baylan, "Early supported discharge services for people with acute stroke," Cochrane Database Systematic Rev., 2017. [Online]. Available: https://doi.org/10.1002/14651885.CD000443. pub4  
[60] J. Bernhardt et al., "Efficacy and safety of very early mobilisation within 24H of stroke onset (AVERT): A randomised controlled trial," Lancet, vol. 386, no. 9988, pp. 46- 55, 2015.  
[61] S. J. Page, G. D. Fulk, and P. Boyne, "Clinically important differences for the upper- extremity fugl- meyer scale in people with minimal to moderate impairment due to chronic stroke," Phys. Ther., vol. 92, no. 6, pp. 791- 798, 2012.
[62] S. RBenjamim, "Wolf motor function test for characterizing moderate to severe hemiparesis in stroke patients," Arch. Phys. Med. Rehabil., vol. 23, no. 11, pp. 1963- 1967, 2012.  
[63] P. W. Duncan, D. Wallace, S. M. Lai, D. Johnson, S. Embretson, and L. J. Laster, "The stroke impact scale version 2.0," Stroke, vol. 30, no. 10, pp. 2131- 2140, 1999.  
[64] N. N. Ansari, S. Naghdi, T. K. Arab, and S. Jalaie, "The interrater and intrarater reliability of the modified ashtowr scale in the assessment of muscle spasticity: Limb and muscle group effect," NeuroRehabilitation, vol. 23, no. 3, pp. 231- 237, 2008.  
[65] D. Lloyd- Jones et al., "Heart disease and stroke statistics - 2010 update: A report from the american heart association," Circulation, vol. 121, no. 7, pp. 948- 954, 2010.  
[66] F- M. Ar, L. Jaasko, I. Leyman, S. Olsson, and S. Steglind, "The post- stroke hemiplegic patient. I. a method for evaluation of physical performance," Scand. J. Rehabil. Med., vol. 7, no. 1, pp. 13- 31, 1975.  
[67] C. Grefkes and G. R. Fink, "Recovery from stroke: Current concepts and future perspectives," Neurological Res. Pract., vol. 2, no. 1, pp. 1- 10, 2020.  
[68] L. Connelly, Y. Jia, M. L. Toro, M. E. Stoykov, R. V. Kenyon, and D. G. Kamper, "A pneumatic glove and immersive virtual reality environment for hand rehabilitative training after stroke," IEEE Trans. Neural Syst. Rehabil. Eng., vol. 18, no. 5, pp. 551- 559, Oct. 2010.  
[69] C. Zhang, C. Liu, X. Zhang, and G. Almpanidis, "An up- to- date comparison of state- of- the- art classification algorithms," Expert Syst. Appl., vol. 82, pp. 128- 150, 2017. [Online]. Available: http://dx.doi.org/10.1016/j.eswa.2017.04.003  
[70] A. Singh, A. A. Hussain, S. Lal, and H. W. Guesgen, "A comprehensive review on critical issues and possible solutions of motor imagery based electroencephalography brain- computer interface," Sensors, vol. 21, no. 6, pp. 1- 35, 2021.  
[71] M. Rashid et al., "Current status, challenges, and possible solutions of EEG- Based brain- computer interface: A comprehensive review," Front. Neurorob., vol. 14, no. Jun., pp. 1- 35, 2020.  
[72] X. Gu et al., "EEG- Based brain- computer interfaces (BCIs): A survey of recent studies on signal sensing technologies and computational intelligence approaches and their applications," IEEE/ACM Trans. Comput. Biol. Bioinf., vol. 18, no. 5, pp. 1645- 1666, Sep. 2021.  
[73] W. Y. Hsu, "EEG- based motor imagery classification using neuro- fuzzy prediction and wavelet fractal features," J. Neurosci. Methods, vol. 189, no. 2, pp. 295- 302, 2010. [Online]. Available: http://dx.doi.org/10.1016/j.jneumeth.2010.03.030  
[74] S. de Vries, M. Tepper, W. Feenstra, H. Oosterveld, A. M. Boonstra, and B. Otten, "Motor imagery ability in stroke patients: The relationship between implicit and explicit motor imagery measures," Front. Hum. Neurosci., vol. 7, no. NOV, pp. 1- 10, 2013.  
[75] G. Buzsaki, C. A. Anastassiou, and C. Koch, "The origin of extracellular fields and currents- EEG, ECoG, LFP and spikes," Nature Rev. Neurosci., vol. 13, no. 6, pp. 407- 420, 2012. [Online]. Available: http://dx.doi.org/10.1038/nrn3241  
[76] U. Chaudhary, N. Birbaumer, and A. Ramos- Murguialday, "Brain- computer interfaces for communication and rehabilitation," Nature Rev. Neurol., vol. 12, no. 9, pp. 513- 525, 2016.  
[77] X. Ma, S. Qiu, and H. He, "Multi- channel EEG recording during motor imagery of different joints from the same limb," Sci. Data, vol. 7, no. 1, pp. 1- 9, 2020. [Online]. Available: http://dx.doi.org/10.1038/s41597- 020- 0535- 2  
[78] N. Saga, A. Doi, T. Oda, and S. N. Kudoh, "Elucidation of EEG characteristics of fuzzy reasoning- based heuristic BCI and its application to patient with brain infarction," Front. Neurorob., vol. 14, 2021, doi: 10.3389/fnbot.2020.607706.  
[79] A. Suwannarat, S. Pan- ngum, and P. Israsena, "Comparison of EEG measurement of upper limb movement in motor imagery training system," BioMedical Eng. Online, vol. 17, no. 1, pp. 1- 22, 2018. [Online]. Available: https://doi.org/10.1186/s12938- 018- 0534- 0  
[80] H. Ramoser, J. Muller- Gerking, and G. Pfurtscheller, "Optimal spatial filtering of single trial EEG during imagined hand movement," IEEE Trans. Rehabil. Eng., vol. 8, no. 4, pp. 441- 446, Dec. 2000.  
[81] C. hyun Park et al., "Which motor cortical region best predicts imagined movement," NeuroImage, vol. 113, pp. 101- 110, 2013.  
[82] C. H. Kaess, C. Windischberger, R. Cunnington, R. Lanzenberger, L. Pezawas, and E. Moser, "The suppressive influence of SMA on M1 in motor imagery revealed by fMRI and dynamic causal modeling," NeuroImage, vol. 40, no. 2, pp. 828- 837, 2008.
[83] N. Braun et al., "The senses of agency and ownership: A review," Front. Psychol., vol. 9, no. APR, pp. 1- 17, 2018.  
[84] C. Kemlin, E. Moulton, Y. Samson, and C. Rosso, "Do motor imagery performances depend on the side of the lesion at the acute stage of stroke," Front. Hum. Neurosci., vol. 10, no. Jun., pp. 1- 10, 2016.  
[85] F. Melo, P. Passos, C. T. P. J. D. Brito, and J. Barreiros, "Brain activity during virtual and real dart throwing tasks in patients with stroke: A pilot study," Int. J. Bioelectromagnetism, vol. 18, no. 2, pp. 74- 78, Aug. 2016.  
[86] N. F. Chi et al., "Cerebral motor functional connectivity at the acute stage: An outcome predictor of ischemic stroke," Sci. Rep., vol. 8, no. 1, pp. 1- 11, 2018.  
[87] P. Celnik, B. Webster, D. M. Glasser, and L. G. Cohen, "Effects of action observation on physical training after stroke," Stroke, vol. 39, no. 6, pp. 1814- 1820, 2008.  
[88] S. Frenkel- Toledo, M. Einat, and Z. Kozol, "The effects of instruction manipulation on motor performance following action observation," Front. Hum. Neurosci., vol. 14, no. Mar., pp. 1- 13, 2020.  
[89] S. Hu, H. Wang, J. Zhang, W. Kong, and Y. Cao, "Causality from cz to C3/C4 or between C3 and C4 revealed by granger causality and new causality during motor imagery," Proc. Int. Joint Conf. Neural Netw., pp. 3178- 3185, 2014.  
[90] W. Kilmesh, "EEG alpha and beta oscillations reflect cognitive and memory performance: A review and analysis," Brain Res. Rev., vol. 29, no. 2/3, pp. 169- 195, 1999.  
[91] V. Singh, Textbook of Clinical Neuroanatomy. New York, NY, USA: Elsevier Health Sci., 2014.  
[92] S. H. Johnson, G. Sprehn, and A. J. Saykin, "Intact motor imagery in chronic upper limb hemiplegics: Evidence for activity- independent action representations," J. Cogn. Neurosci., vol. 14, no. 6, pp. 841- 852, 2002.  
[93] L. Wang et al., "Dynamic functional reorganization of the motor execution network after stroke," Brain, vol. 133, no. 4, pp. 1224- 1238, 2010.  
[94] F. Xie, L. Xu, Z. Long, L. Yao, and X. Wu, "Functional connectivity alteration after real- time fmri motor imagery training through self- regulation of activities of the right premotor cortex," BMC Neurosci., vol. 16, no. 1, pp. 1- 11, 2015.  
[95] C. Decharns, K. Christoff, G. H. Glover, J. M. Paulty, S. Whitfield, and D. E. Gabrieli, "Learned regulation of spatially localized brain activation usingreal- time fMRI.pdf," NeuroImage, vol. 21, pp. 436- 443, 2004.  
[96] F. Pichiorri et al., "Brain- computer interface boosts motor imagery practice during stroke recovery," Ann. Neurol., vol. 77, no. 5, pp. 851- 865, 2015.  
[97] M. A. Khan, R. Das, H. K. Iversen, and S. Puthusserypady, "Review on motor imagery based BCI systems for upper limb post- stroke neurorehabilitation: From designing to application," Comput. Biol. Med., vol. 123, no. May, 2020, Art. no. 103843. [Online]. Available: https://doi.org/10.1016/j.compbiomed.2020.103843  
[98] J. Decety, "Do imagined and executed actions share the same neural substrate," Cogn. Brain Res., vol. 3, no. 2, pp. 87- 93, 1996.  
[99] W. Wang, B. Yang, C. Guan, and B. Li, "A VR combined with MI- BCI application for upper limb rehabilitation of stroke," in Proc. IEEE MTT- S Int. Microw. Biomed. Conf., 2019, pp. 2- 5.  
[100] A. Kumar, Q. Fang, J. Fu, E. Pirogova, and X. Gu, "Error- related neural responses recorded by electroencephalography during post- stroke rehabilitation movements," Front. Neurorob., vol. 13, no. Dec., pp. 1- 11, 2019.  
[101] G. Fluet et al., "Early versus delayed V- based hand training in persons with acute stroke," in Proc. Int. Conf. Virtual Rehabil., 2017, pp. 1- 7.  
[102] N. Sharma, J.- C. Baron, and J. B. Rowe, "Europe PMC funders group motor imagery after stroke: Relating outcome to motor network connectivity," Ann. Neurol., vol. 66, no. 5, pp. 604- 616, 2009.  
[103] L. Dodakian, J. C. Stewart, and S. C. Cramer, "Motor imagery during movement activates the brain more than movement alone after stroke: A pilot study," J. Rehabil. Med., vol. 46, no. 9, pp. 843- 848, 2014.  
[104] M. C. Banina et al., "Exercise intensity is increased during upper limb movement training using a virtual rehabilitation system," in Proc. Int. Conf. Virtual Rehabil., 2019, pp. 1- 6.  
[105] J. Patel et al., "Virtual reality- augmented rehabilitation in the acute phase post- stroke for individuals with flaccid upper extremities: A feasibility study," in Proc. IEEE Int. Conf. Virtual Rehabil., 2015, pp. 215- 223.  
[106] M. S. Cameirao, S. B. I. Badia, E. D. Oller, and P. F. Verschure, "Using a multi- task adaptive VR system for upper limb rehabilitation in the acute phase of stroke," in Proc. IEEE Virtual Rehabil., 2008, pp. 2- 7.  
[107] P. L. Nunez et al., Electric Fields of the Brain: The Neurophysics of EEG. London, U.K.: Oxford Univ. Press, 2006.

> **Image description.** A grayscale portrait photograph of a young man, presented as a professional headshot.
>
> The subject is a man with dark, neatly styled hair, looking directly at the viewer with a neutral and serious expression. He is positioned centrally in the frame, shown from the chest up. He is wearing a light-colored, collared shirt, which contrasts with the dark, indistinct background. The lighting is focused on the subject, highlighting his facial features and creating a strong contrast against the deep shadows of the background.
>
> Below the photograph, the word "intelligence." is visible in a standard font, appearing to be part of the surrounding text or caption. The overall composition is typical of an academic or professional profile image, designed to present the individual clearly.

Chi Sang Choy (Student Member, IEEE) received the B.Sc. degree in physics and the M.Sc. degree in physics (experimental particle physics) from the University of Melbourne, Melbourne, VIC, Australia, in 2017 and 2019, respectively. He is currently working toward the Ph.D. degree in electrical and electronic engineering with RMIT University, Melbourne, VIC, Australia. His research interests include stroke rehabilitation via motor imagery and virtual reality, physiological signal processing, and artificial intelligence.

intelligence.

> **Image description.** A professional portrait or headshot of a man set against a plain, light-colored background.
>
> The subject is a middle-aged man with a fair complexion. He has short, dark hair on the sides and a neatly trimmed beard and stubble covering his jawline and chin. He is looking directly at the camera with a neutral, serious expression. He is wearing a light-colored, collared shirt, which appears to be light blue or white.
>
> The background is uniformly light, suggesting a studio setting, which keeps the focus entirely on the subject.
>
> At the bottom of the image, there is visible text that is partially cut off. The visible portion reads: "coding and information".

Shaun L. Cloherty (Member, IEEE) received the B.E. (Hons.) degree in aerospace avionics from the Queensland University of Technology, Brisbane, QLD, Australia, and the Ph.D. degree in biomedical engineering from the University of New South Wales, Sydney NSW, Australia. He is currently a Lecturer with the School of Engineering (Electrical and Biomedical Engineering). His primary research interests include systems neuroscience combine experimental and computational approaches to understand neural coding and information processing in the brain, and the neural basis of perception and behaviour.

> **Image description.** A portrait photograph of a woman, likely a professional headshot, set against a softly focused natural background.
>
> The subject is a woman with medium-length, light brown hair. She is wearing dark-rimmed glasses and has a pleasant, subtle smile. She is dressed in a dark, possibly black, collared top.
>
> The background is blurred, utilizing a shallow depth of field, which emphasizes the subject. The visible elements in the background include various shades of green foliage, suggesting an outdoor or garden setting, along with hints of lighter areas that could be sky or distant light.
>
> In the bottom right corner of the image, there is visible text that appears to be a continuation of the surrounding document content. The text reads:
> "tissue engineering, and
> intelligence."

Elena Pirogova received the B.Eng. (Hons.) degree in chemical engineering from the National Technical University of Ukraine, Kyiv, Ukraine, in 1991, and the Ph.D. degree in biomedical engineering from Monash University, Melbourne, VIC, Australia, in 2002. She is currently a Professor of biomedical engineering with the School of Engineering, RMIT University, Melbourne, VIC, Australia. Her research interests include biomedical signal analysis, bioelectronics, bioelectromagnetics, microfluidics, tissue engineering, and the novo design therapeutic peptides.

tissue engineering, and the novo design therapeutic peptides.

> **Image description.** A professional headshot of a middle-aged man, likely part of a faculty or staff biography within a document.
>
> The subject is a man with a shaved head, wearing rectangular-framed glasses. He is dressed in formal business attire, consisting of a dark suit jacket, a light-colored dress shirt, and a dark necktie. He is positioned facing forward, looking directly at the viewer with a neutral, professional expression.
>
> The image is set against a plain, light gray or off-white background.
>
> Fragmented text is visible surrounding the portrait, indicating that the image is embedded within a larger document. Visible text includes:
> *   To the top left: "d"
> *   Below the portrait: "with the specialties in"
> *   Along the far left edge, several vertical letters are visible: "e", "f", "t", "i", "o", "n", "g".

Qiang Fang received the B.S. degree in applied physics from Tsinghua University, Beijing, China, in 1991, and the Ph.D. degree in biomedical engineering from Monash University, Melbourne, VIC, Australia, in 2000. He is the Founding Chair of the new Department of Biomedical Engineering, Shantou University, Shantou, China. From 2002- 2017, he played a key role in forging the new biomedical engineering program with RMIT University, Melbourne, VIC, Australia, as a permanent Academic Staff

with the specialties in biomedical electronics. Prof. Fang's Neural Engineering and Rehabilitation Laboratory at Shantou University has the research interests on the automatic assessment of limb and speech function impairments caused by stroke and intelligent assistive devices supported by a brain- computer interface. His group also investigates the structural and functional connectivity for brain disorder patients.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
