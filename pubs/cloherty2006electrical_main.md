```
@inbook{cloherty2006electrical,
  author = {Shaun L. Cloherty and Socrates Dokos and Nigel H. Lovell},
  title = {Electrical Activity in Cardiac Tissue, Modeling of},
  booktitle = {Wiley Encyclopedia of Biomedical Engineering},
  year = {2006},
  publisher = {John Wiley & Sons, Ltd},
  isbn = {9780471740360},
  chapter = {},
  pages = {},
  doi = {10.1002/9780471740360.ebs1577},
  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/9780471740360.ebs1577}
}
```

---

## ELECTRICAL ACTIVITY IN CARDIAC TISSUE, MODELING OF

S.L. CLOHERTY  University of New South Wales  Sydney, Australia  and  University of Newcastle  Callaghan, Australia  S. DOKOS  University of New South Wales  Sydney, Australia  N.H. LOVELL  University of New South Wales  Sydney, Australia  and  Australian Technology Park  Eveleigh, Australia

## 1. INTRODUCTION

Mathematical modeling has proven to be a powerful tool for improving our understanding of electrical activation in the heart, including the ionic mechanisms underlying cardiac action potentials, the generation and propagation of both normal and abnormal rhythms, the termination of abnormal rhythms by external electric shocks, and the effect of various drugs on cardiac electrical activity (1). Fueled by an ever expanding pool of experimental data and the commoditization of computing technology, models of cardiac electrical activity continue to evolve, becoming increasingly more complex in an attempt to faithfully embody new experimental observations. To a large extent, these models are a result of the reductionist approach in the physical sciences, in which complex systems are decomposed into smaller, more manageable components that may be studied and characterized independently. This approach has been incredibly successful. However, in many biological systems, including the heart, it is becoming increasingly evident that much observed behavior is a result of the complex interaction of many systems ranging from the subcellular to the cellular and ultimately the tissue or whole organ scale. Understanding of such emergent behavior may be achieved through the development of so- called integrative models, which attempt to combine detailed and accurate models across a range of scales, into complex models of cardiac tissue and even the whole heart.

The goal of this article is to present an overview of the techniques routinely employed in modeling the electrical activity of cardiac myocytes and the propagation of electrical activation in cardiac tissue. Specifically, this article describes the modeling of cardiac activation at the cellular scale, using single cell models, and at the tissue scale, using spatially distributed multicellular models. Models of cardiac activation formulated using the techniques described here provide a basis for modeling other aspects of heart function such as the excitation- contraction process or the generation of body surface potentials recorded in the electrocardiogram.

## 2. HISTORICAL BACKGROUND

The foundation for contemporary models of cardiac activation lies in the pioneering work of Hodgkin and Huxley, who in the late 1940s, employed the voltage- clamp amplifier to characterize the membrane current- voltage relationships of the squid giant axon. Their technical and experimental achievement aside, Hodgkin and Huxley went further still, formulating the first mathematical description of membrane activation (2). This mathematical model could reproduce known experimental observations including membrane refractoriness, strengthening characteristics of the electrical stimulus threshold, the effects of specific ion channel blockade, as well as electrical propagation along a one- dimensional cable (3).

In their original work, Hodgkin and Huxley solved their model equations in an arduous fashion by hand. However, the advent of the digital computer saw a proliferation of models, based on Hodgkin and Huxley's formulations, describing the electrical properties of many excitable cells, including those of the central and peripheral nervous system and smooth and skeletal muscle.

Ionic models of cardiac electrical activity, based on Hodgkin- Huxley formulations, began to appear in 1962 with the publication of Noble's (4) model of Purkinje fiber activity. Over the next 10 years, this simple model provided a basis for numerous models of electrical activity in other regions of the heart. The 1970s saw the development of more sophisticated models of Purkinje and ventricular fiber activity by McAllister et al. (5) and Beeler and Reuter (6), respectively. These new models in turn spawned a second generation of models reproducing electrical activity in other regions of the heart (7,8), a pattern that entered its third cycle with the DiFrancesco and Noble (9) model of Purkinje fiber activity in 1985. In addition to membrane currents based on Hodgkin- Huxley formulations, the DiFrancesco and Noble equations modeled active transport mechanisms and employed compartment modeling to describe changes in intra- and extracellular ionic concentrations. More recent models attempt to couple together the wide range processes involved in normal cell activity by including stretch- activated membrane currents and the regulating effects of metabolites and neurotransmitters (10- 12).

## 3. SINGLE CELL MODELS

Single cell models describe electrical activity at the individual cell level, without taking into account the propagation of excitation from one cell to the next. Thus, single cell models can reproduce basic features of the cardiac action potential intrinsic to a single cell.

In general, single cell models may be classified as either simple empirical models or detailed biophysical models. Rather than attempting to model the complex ionic mechanisms underlying electrical activity in cardiac myocytes, simple empirical models capture the key characteristics of the intrinsic dynamics in a compact form. In contrast, biophysically detailed models attempt

to model the activation process based on the underlying physics of the cell membrane, and often they include complex formulations for each ionic membrane current.

Due to their simple mathematical formulations, empirical models are relatively cheap to solve and are therefore often used as a basis for formulating large- scale multicellular tissue models. Such models have proven useful in the qualitative investigation of many aspects of cardiac electrical activation (see, for example, the bidomain model simulations and associated discussion below). However, because the empirical models are somewhat divorced from the underlying physiology, such models are limited in their applicability. For example, empirical models are largely unsuitable for quantitative investigation of the effects of pharmacological agents or pathological conditions that may directly influence specific ionic currents or alter the cellular environment; for such studies, detailed and accurate ionic models are preferred.

### 3.1. Simple Empirical Models

Several relatively simple empirical models have been proposed to describe electrical activity in the heart. The first such model widely used was that formulated by FitzHugh (13), as a generalization of the Bonhoeffervan der Pol (BVP) equations for a relaxation oscillator. This simple model consisted of only two state variables, the dynamics of which were determined by a pair of first- order ordinary differential equations. As FitzHugh demonstrated, this simple model was essentially a simplification of the Hodgkin- Huxley equations for activation of the squid nerve under space clamped conditions. With appropriate selection of parameters, the BVP equations can also reproduce the spontaneous activity characteristic of the specialized pacemaker of the heart, the sinoatrial node. Such a simple model of pacemaker activity was formulated by Sato et al. (14), to investigate autonomic modulation of the pacemaking rate.

The BVP model was subsequently generalized by Nagumo et al. (15) to model propagation of the action potential in a pulse transmission line representing the nerve axon. This generalized form of the equations, referred to as the FitzHugh- Nagumo (FHN) equations, are often employed in multicellular models of cardiac activation.

The FHN equations can reproduce, in at least a qualitative sense, the excitable nature of cardiac myocytes, including the presence of a refractory period. Several investigators have modified the FHN equations in an attempt to improve their agreement with experimental observations. One such modification widely employed in cardiac activation modeling is that by Rogers and McCulloch (16); i.e.,

\[\frac{dv}{dt} = c_1v(v - a)(1 - v) - c_2vu + i_{\mathrm{stim}}, \quad (1)\]

\[\frac{du}{dt} = b(v - du), \quad (2)\]

where \(a,b,c_1,c_2\) , and \(d\) are constants and \(i_{\mathrm{stim}}\) represents

an externally applied stimulus. The simulated action potential using this two- variable model with parameters \(a = 0.13\) , \(b = 0.013\) , \(c_1 = 0.26\) , \(c_2 = 0.1\) , and \(d = 1.0\) is shown in Fig. 1 ( \(v\) - trace). The \(u\) - trace is a measure of the refractoriness or inexcitability of the cell. The stimulus current \(i_{\mathrm{stim}}\) was a square pulse of amplitude 0.03 and duration 20 applied at time \(t = 100\) .

Several other simple models, slightly less empirical than the FHN models just described, have also been formulated to model cardiac electrical activity. van Capelle and Durrer (17) formulated a cell model consisting of two state variables, representing the transmembrane potential and a general excitability parameter. The dynamics of this simple model were determined by a weighted sum (with the excitability parameter serving as the weight) of two assumed current- voltage relationships: the first corresponding to a fully excitable state and the second to a fully activated or inexcitable state. Much like the FHN model, this simple model could also produce activity qualitatively similar to both quiescent and spontaneously active cardiac myocytes.

A relatively simple model of cardiac pacemaker activity was also proposed by Endresen (18). This model was derived from the underlying conservation relations of the cell membrane. It contained two state variables governed by a pair of ordinary differential equations, and it included simple formulations for three membrane currents. These were categorized according to their kinetics as either fast or slow, governed, respectively, by either a simple current voltage relationship or a single ordinary differential equation.

### 3.2. Detailed Biophysical (Ionic) Models

Biophysically detailed models attempt to model the activation process based on the underlying physics of the cell

> **Image description.** A line graph titled "Figure 1. Simulated action potential (v-trace) using the two-" displays the dynamics of three variables over time, likely representing components of a cardiac electrical model.
>
> The graph features a horizontal X-axis labeled "Time," ranging from 0 to 1000, with major tick marks every 100 units. The vertical Y-axis represents a normalized value, ranging from 0.0 to 1.0, with increments of 0.1.
>
> Three distinct data series are plotted:
>
> 1.  **v (Solid Line):** This line represents the primary action potential. It starts near zero, rises sharply to a peak value of approximately 0.9 around the 150-unit mark, and then decays rapidly back toward zero, completing the transient event by approximately 500 time units.
> 2.  **u (Dashed Line):** This line represents a secondary variable. It rises more gradually than 'v', reaching a peak value of approximately 0.6 around the 250-unit mark. It then decays more slowly than 'v', remaining above zero for a longer duration.
> 3.  **i_stim (Dotted Line):** This line represents a stimulus current. It remains relatively low and stable throughout the entire duration of the plot, starting near zero and peaking slightly below 0.1.
>
> The visible text includes the figure caption, which is partially cut off: "Figure 1. Simulated action potential (v-trace) using the two-". The axes are clearly labeled with numerical scales and the X-axis is labeled "Time."

<center>Figure 1. Simulated action potential ( \(v\) -trace) using the two-variable model by Rogers and McCulloch (16) (Equations 1 and 2) with parameters \(a = 0.13\) , \(b = 0.013\) , \(c_1 = 0.26\) , \(c_2 = 0.1\) , and \(d = 1.0\) . The stimulus current \(i_{\mathrm{stim}}\) was a square pulse of amplitude 0.03 and duration 20 applied at time \(t = 100\) . The \(u\) -trace is a measure of the refractoriness or inexcitability of the cell. </center>

membrane. Specifically, the cell membrane is modeled as a capacitor in parallel with several conductances representing the various ionic current systems. A typical example of such a "parallel conductance" model is illustrated by the equivalent circuit in Fig. 2. In this circuit, current flow across the membrane \((i_{\mathrm{m}})\) is equal to the sum of an ionic component \((i_{\mathrm{ion}})\) and a capacitive component \((i_{\mathrm{c}})\) , which models the effect of cell membrane capacitance as charge accumulates on either side of the cell membrane. Recent models extend the basic model of the cell membrane shown to the left in Fig. 2, adding formulations for active transport mechanisms \((i_{\mathrm{NaK}}\) and \(i_{\mathrm{NaCa}}\) depicted as current sources in Fig. 2) and autonomic modulation of various membrane currents \((i_{\mathrm{K,AcH}}\) in Fig. 2). In addition, these models often include formulations for dynamic changes in intra- and extracellular ion concentrations, including the uptake and release of calcium from the sarcoplasmic reticulum (SR) and buffering of calcium by the cytosolic proteins calmodulin and troponin.

Under space- clamped conditions, there is no net current flow across the cell membrane. The capacitive current \(i_{\mathrm{c}}\) is then equal and opposite to the ionic current \(i_{\mathrm{ion}}\) so that

\[\frac{dV_{\mathrm{m}}}{dt} = -\frac{i_{\mathrm{ion}}}{C_{\mathrm{m}}}, \quad (3)\]

where \(V_{\mathrm{m}}\) denotes the transmembrane potential, \(i_{\mathrm{ion}}\) denotes the sum of the membrane ionic currents \((i_{\mathrm{Na}}\) \(i_{\mathrm{Ca}}\) , \(i_{\mathrm{K}}\) , etc.), \(C_{\mathrm{m}}\) denotes the membrane capacitance, and \(t\) denotes time. Many ionic currents display complex time- and voltage- dependent activation and inactivation kinetics, as indicated by the variable conductance symbols in Fig. 2. Several schemes have been developed to model these kinetics (for a comprehensive review, see Bett and Rasmusson (19)). The first, and perhaps the simplest, being that pioneered by Hodgkin and Huxley in the squid giant axon (2). However, more recently, increased atten

> **Image description.** A schematic diagram illustrating the equivalent circuit of a single cell ionic model, specifically designed to represent the electrical properties of a cardiac cell membrane. The diagram depicts a complex parallel circuit connecting intracellular and extracellular compartments.
>
> The circuit is fundamentally structured around a central capacitor, $C_m$, which represents the cell membrane capacitance. This capacitor is connected in parallel with several other components that model various ionic and active transport processes.
>
> The components are organized as follows:
>
> 1.  **Capacitance:**
>     *   $C_m$: A capacitor symbol (two parallel lines) is positioned centrally, representing the membrane capacitance.
>
> 2.  **Ionic Currents (Conductances):**
>     *   Several zigzag lines, representing conductances, are connected in parallel. These are labeled with the corresponding ionic currents: $i_{Na}$ (sodium), $i_{Ca}$ (calcium), $i_K$ (potassium), and $i_b$ (bicarbonate).
>     *   These conductances are connected across voltage sources representing the equilibrium potentials for each ion: $E_{Na}$, $E_{Ca}$, $E_K$, and $E_b$. These voltage sources are depicted as standard battery symbols (rectangles with positive and negative terminals).
>
> 3.  **Active Transport and Modulation (Current Sources):**
>     *   The model includes three current sources, represented by circles with arrows indicating the direction of current flow. These represent active transport mechanisms or autonomic modulation:
>         *   $i_{NaK}$: Sodium-potassium pump current.
>         *   $i_{NaCa}$: Sodium-calcium exchanger current.
>         *   $i_{K,AcH}$: Potassium current modulated by Acetylcholine.
>
> The entire circuit is labeled with the boundaries "Intracellular" at the bottom and "Extracellular" at the top, indicating the direction of current flow $i_m$ (membrane current) from the intracellular space to the extracellular space. The overall arrangement shows that the total membrane current ($i_m$) is the sum of the capacitive current and all the various ionic and active transport currents flowing in parallel across the membrane.
>
> The caption below the figure reads: "Figure 2. Equivalent circuit of a single cell ionic model of cardiac..." (The text is truncated).

<center>Figure 2. Equivalent circuit of a single cell ionic model of cardiac electrical activity. The cell membrane is modeled as a capacitance \((C_{\mathrm{m}})\) in parallel with several conductances representing the various ionic current systems \((i_{\mathrm{Na}}\) , \(i_{\mathrm{Ca}}\) , \(i_{\mathrm{K}}\) , and \(i_{\mathrm{b}}\) ). Active transport mechanisms \((i_{\mathrm{NaK}}\) and \(i_{\mathrm{NaCa}}\) ) and autonomic modulation \((i_{\mathrm{K,AcH}})\) found in more sophisticated models are shown shaded on the right. Total membrane current \((i_{\mathrm{m}})\) consists of a capacitive component \((i_{\mathrm{c}})\) and an ionic component \((i_{\mathrm{ion}})\) , the later being equal to the sum of the currents in each ionic conductance branch. By convention, a positive current denotes outward current flow to the extracellular space. </center>

tion has been focused on Markov state models of ion currents.

### 3.3. Hodgkin-Huxley Formalism

In Hodgkin- Huxley- type models, the time- dependent ion currents are modeled by equations of the form

\[i = gm^{p}h^{q}(V_{\mathrm{m}} - E_{\mathrm{eq}}), \quad (4)\]

where \(i\) is the membrane current, \(g\) is the maximum whole- cell conductance, \(m\) and \(h\) are dimensionless gating variables representing respectively the proportion of activation and inactivation gates in the open state, \(p\) and \(q\) represent the number of gates of each type required to model the observed kinetics, \(V_{\mathrm{m}}\) is the transmembrane potential, and \(E_{\mathrm{eq}}\) is the Nernst equilibrium potential of the ion species in question. The activation and inactivation gates are governed by first- order kinetics given by

\[\frac{dm}{dt} = z_{m}(1 - m) - \beta_{m}m \quad (5)\]

(for the activation gate \(m\) in (Equation 4), where \(z_{m}\) and \(\beta_{m}\) are the opening and closing rates and are, in general, empirical functions of the membrane potential \(V_{\mathrm{m}}\) . Equivalently, the gating kinetics may also be expressed in terms of the proportion of open gates under steady state conditions \((m_{\infty}\) for example) and the time constant of activation \((\tau_{m})\) ; i.e.,

\[\frac{dm}{dt} = \frac{m_{\infty} - m}{\tau_{m}}, \quad (6)\]

where

\[m_{\infty} = \frac{z_{m}}{z_{m} + \beta_{m}}, \tau_{m} = \frac{1}{z_{m} + \beta_{m}}.\]

### 3.4. Markov Models of Ion Channel Gating

Although Hodgkin- Huxley- type equations are adequate in reproducing a wide range of observable membrane current kinetics, recent advances in single channel recordings suggest that individual ion channels exhibit multiple states corresponding to voltage- dependent protein conformations and/or ligand binding (20). To be consistent with this new understanding of channel structure and function, Markov state models of ion channels have been increasingly used to describe membrane current kinetics (21). In general terms, the Hodgkin- Huxley form of membrane current (Equation 4) is replaced by

\[i = \left(\sum_{s = 1}^{N}g_{s}A_{s}\right)(V_{\mathrm{m}} - E_{\mathrm{eq}}), \quad (7)\]

where \(A_{s}\) is the proportion of membrane channels in state \(s\) , \(g_{s}\) is the membrane conductance associated with state \(s\) , and \(N\) is the total number of states. The kinetics governing

the \(A_{s}\) are given by

\[\frac{dA_{s}}{dt} = \sum_{r\neq s}(k_{rs}A_{r} - k_{sr}A_{s})r = 1,\ldots ,N - 1 \quad (8)\]

and

\[\sum_{r = 1}^{N}A_{r} = 1, \quad (9)\]

with \(k_{rs}\) and \(k_{sr}\) denoting the forward and reverse rate coefficients of transfer from state \(r\) to state \(s\) , respectively. These rates are typically empirical monotonic functions of transmembrane potential \(V_{\mathrm{m}}\) . Often, only one of the \(N\) states is regarded as corresponding to the open or conducting state of the channel; all other states having a conductivity \(g\) of zero. In this case, no summation is taken in (7), and only one \(g\) value is used corresponding to the single open state. Also, in (8), direct transition between all state pairs is not always allowed, equivalent to setting the relevant \(k\) terms to zero.

When all states are connected in a closed loop, as shown in Fig. 3, the thermodynamic principle of detailed balance (also known as microscopic reversibility) may be employed to further constrain the rate terms in Equation 8 (22). The principle states that in the absence of any external energy source to drive the state transitions, the product of rate constants in the clockwise direction around the loop is equal to the product in the counterclockwise direction. For the Markov state model of Fig. 3, this is equivalent to \(k_{1}k_{2}k_{3}k_{7} = k_{5}k_{6}k_{4}k_{8}k_{9}\) .

In some cases, Markov state models can be expressed in equivalent Hodgkin- Huxley form. For example, the trivial case of a two- state Markov model is analogous to an ion channel possessing a single Hodgkin- Huxley gating variable. For the four- state model of Fig. 3 with the single open state \(A_{1}\) , if \(k_{4} = k_{7} = z_{m}\) , \(k_{3} = k_{8} = \beta_{m}\) , \(k_{2} = k_{5} = z_{h}\) , and \(k_{1} = k_{6} = \beta_{h}\) , the Markov state description of the membrane current

\[i = gA_{1}(V_{\mathrm{m}} - E_{\mathrm{eq}}) \quad (10)\]

> **Image description.** A flow diagram illustrating a four-state Markov model, representing transitions between four distinct states ($A_1, A_2, A_3, A_4$) governed by various rate coefficients ($k_1$ through $k_9$). The diagram is structured with four vertical bars representing the states, and directed arrows connecting these states, each labeled with a specific rate constant.
>
> The four states are arranged as follows:
> *   $A_1$: Located at the bottom left.
> *   $A_2$: Located at the top left.
> *   $A_3$: Located at the top right.
> *   $A_4$: Located at the bottom right.
>
> The transitions between these states are represented by directed arrows and labeled with rate coefficients ($k_n$):
>
> **Transitions involving $A_1$ and $A_2$ (Left Column):**
> *   $k_1$: Transition from $A_1$ to $A_2$ (upward arrow).
> *   $k_2$: Transition from $A_2$ to $A_1$ (downward arrow).
>
> **Transitions involving $A_1$ and $A_3$ (Top Row):**
> *   $k_3$: Transition from $A_1$ to $A_3$ (rightward arrow).
> *   $k_4$: Transition from $A_3$ to $A_1$ (leftward arrow).
>
> **Transitions involving $A_2$ and $A_4$ (Right Column):**
> *   $k_5$: Transition from $A_2$ to $A_4$ (downward arrow).
> *   $k_6$: Transition from $A_4$ to $A_2$ (upward arrow).
>
> **Diagonal and Cross-State Transitions:**
> *   $k_7$: Transition from $A_1$ to $A_4$ (downward-right diagonal arrow).
> *   $k_8$: Transition from $A_4$ to $A_1$ (upward-left diagonal arrow).
> *   $k_9$: Transition from $A_2$ to $A_3$ (rightward arrow).
>
> The diagram visually represents a complex network of possible state changes, where the rate coefficients ($k_n$) quantify the speed or probability of moving from one state to another. The overall structure is characteristic of a Markov state model used in biological contexts, such as describing ion channel gating.

<center>Figure 3. Four-state Markov model with single open state \(A_{1}\) . State transition rates \(k_{1} - k_{8}\) are typically empirical functions of transmembrane potential \(V_{\mathrm{m}}\) . </center>

is equivalent to

\[i = g m h(V_{\mathrm{m}} - E_{\mathrm{eq}}), \quad (11)\]

with

\[\frac{dm}{dt} = z_{m}(1 - m) - \beta_{m}m,\] \[\displaystyle \frac{dh}{dt} = z_{h}(1 - h) - \beta_{h}h,\]

and

\[m = A_1 + A_2,\] \[h = A_1 + A_4.\]

Thus, Hodgkin- Huxley models may be regarded as specific cases of the more generalized Markov- state descriptions of ion channel kinetics.

### 3.5. Simulating Heterogeneous Cell Types

Detailed ionic models are currently available for many different regions of the heart including the specialized conduction systems of the sinoatrial node, the atrioventricular node, and the Purkinje fibers, as well as the working myocytes of the atria and ventricles. A comprehensive list may be found in the online model repository of the Physiome project (http://www.cellml.org/), which at the time of writing lists in excess of 30 detailed cardiac cell models.

Figure 4 illustrates simulated action potentials produced by detailed ionic models of electrical activity characteristic of four different regions of the heart: (1) sinoatrial node (23), (2) atria (24), (3) Purkinje fiber (9), and (4) ventricle (25).

The rabbit sinoatrial node cell model illustrated in Fig. 4a was developed by the authors with all time- dependent ionic currents governed by three- or four- state Markov models rather than conventional Hodgkin- Huxley gating models (23). The model consists of 12 membrane currents (including two active transport mechanisms) and includes formulations for dynamic changes in both intra- and extracellular ionic concentrations together with equations describing the sequestration of calcium in the SR. The remaining models illustrated in Fig. 4 all employ the conventional Hodgkin- Huxley gating model for their time- dependent membrane currents. The rabbit atrial cell model by Earm and Noble and Hilgemann and Noble (24,26) (Fig. 4b) contains nine membrane currents and incorporates dynamic changes in ionic concentrations including the sequestration of calcium in the SR and the buffering of calcium by calmodulin and troponin. The Purkinje fiber model of DiFrancesco and Noble (9) (Fig. 4c) includes active transport mechanisms and dynamic changes in ionic concentrations. The guinea pig ventricular cell model (Fig. 4d) by Faber and Rudy (25), based on the earlier model of Lou and Rudy (27), includes 15 ionic membrane currents in addition to formulations for ion

> **Image description.** This image is a scientific figure consisting of four separate line graphs arranged in a 2x2 grid, illustrating simulated action potentials from ionic cell models. The graphs are presented on a white background with black lines and text.
>
> **General Structure and Axes:**
> Each of the four panels (a, b, c, and d) is a time-series plot. The vertical axis (Y-axis) in all panels is labeled "Membrane Potential (mV)," and the horizontal axis (X-axis) is labeled "Time (s)." The scale and range of the axes vary across the panels to accommodate the specific characteristics of the simulated action potentials.
>
> **Detailed Panel Descriptions:**
>
> *   **Panel (a):** This graph shows a single, complex action potential. The Y-axis ranges from -100 mV to 50 mV, and the X-axis ranges from 0.0 to 1.0 s. The curve exhibits a gradual, spontaneous depolarization (pacemaker potential) before a sharp, rapid upward spike (depolarization) followed by a return toward a negative potential (repolarization).
> *   **Panel (b):** This graph displays a single, sharp, and rapid action potential spike. The Y-axis ranges from -100 mV to 50 mV, and the X-axis ranges from 0.0 to 1.0 s. The potential starts at a negative baseline and quickly rises to a peak before rapidly falling back down.
> *   **Panel (c):** This panel shows multiple, distinct action potentials spread over a much longer duration. The Y-axis ranges from -100 mV to 50 mV, and the X-axis is significantly extended, ranging from 0.0 to 4.0 s. The spikes are sharp and follow a pattern similar to Panel (a), illustrating a prolonged duration of the action potential.
> *   **Panel (d):** This graph shows a single, broad action potential. The Y-axis ranges from -100 mV to 100 mV, and the X-axis ranges from 0.0 to 1.0 s. The depolarization and repolarization phases are less sharply defined compared to the other panels, resulting in a more rounded spike.
>
> **Text and Labels:**
> The figure is titled "Figure 4. Simulated action potentials from ionic cell models representing four different regions of the heart, (a) sinoatrial node (23), (b) atria (24), (c) Purkinje fiber (9), and (d) ventricle (25)." The panel labels (a), (b), (c), and (d) are placed in the upper left corner of their respective graphs.
>
> The surrounding text provides context, noting that the time base in (c) was slowed to better illustrate the prolonged duration of the Purkinje fiber action potential, and mentions the spontaneous depolarization (pacemaker potential) exhibited in the sinoatrial node and Purkinje fiber.

<center>Figure 4. Simulated action potentials from ionic cell models representing four different regions of the heart, (a) sinoatrial node (23), (b) atria (24), (c) Purkinje fiber (9), and (d) ventricle (25). The time base in (c) has been slowed to better illustrate the prolonged duration of the Purkinje fiber action potential. Note the spontaneous depolarization (the pacemaker potential) exhibited in both the sinoatrial node and the Purkinje fiber. The action potentials shown are the result of the authors' simulations. </center>

concentration changes and the sequestration and buffering of calcium.

## 4. MULTICELLULAR MODELS

In general, single cell models describe the intrinsic dynamics of the cell membrane of their intended cell type. However, the membrane potentials observed in intact cardiac tissue are not simply a result of the intrinsic dynamics of the cell membranes. Rather, observed membrane potentials are a result of the interplay between the intrinsic dynamics of the cell membrane and the electrotonic interaction between neighboring myocytes. As a result, much behavior observed in cardiac tissue may be attributed in part to the complex spatial organization of the tissue and interaction between large populations of heterogeneous cells. This section describes several techniques often employed in formulating multicellular models of cardiac electrical activation. These techniques aim to model the mutual interaction of neighboring cells and may, in general, be classified as either discrete or continuous. In either case, multicellular models often incorpo

rate single cell models, such as those described above, to describe the intrinsic dynamics of the cells constituting the tissue being modeled.

## 5. DISCRETE MODELS

### 5.1. Cellular Automata Models

Cellular automata (CA) models discretize the geometry of the tissue into a regular array of cells, whose electrical activity is based on a set of rules, rather than systems of differential equations. These cells need bare no correlation to the cardiac myocytes forming the tissue and may instead be considered simply as building blocks, each occupying a finite volume of space with a defined relationship to its neighbors. At any time step, a given cell may exist in one of a finite number of states. The transition from one state to the next in successive time steps is governed by rules, based on the current state of the cell and the states of its neighbors.

Among the earliest applications of the CA approach to modeling cardiac activation was that of Moe et al. (28),

who constructed relatively simple two- dimensional arrangements representing sheets of atrial tissue. These models included spatial heterogeneity in refractory period and could sustain multiple wavefronts of activation, qualitatively similar in many respects to atrial fibrillation. Given their low cost in computational terms, CA models have since been widely employed in modeling activation of the whole heart to determine equivalent source distributions for the purposes of modeling the surface ECG—the so- called “forward problem” of electrocardiology (29,30).

### 5.2. Network Models

Network models of cardiac tissue consist of cell models (such as the simple empirical models or the detailed ionic models described above) resistively coupled together in a regular spatial lattice as illustrated schematically for a two- dimensional sheet of tissue in Fig. 5a. Each node represents a single cell or a small cluster of identical cells and is coupled to its immediate neighbors by ohmic conductances representing the cardiac gap junctions. The electrophysiological characteristics of the tissue being

> **Image description.** A technical diagram illustrating two schematic representations of two-dimensional network models used in electrocardiology, labeled (a) and (b). Both panels depict a grid-like arrangement of interconnected components, representing cardiac tissue.
>
> The overall visual style is a black-and-white schematic, using simple geometric shapes and lines to represent electrical components.
>
> **Panel (a): Simple Network Model**
> This panel shows a relatively simple, regular lattice structure.
> *   **Nodes:** The primary components are represented by small, vertical, cylindrical shapes, arranged in a 3x4 grid (three rows and four columns). These cylinders represent individual cells or small clusters of cells.
> *   **Connections:** Each node is connected to its immediate neighbors (up, down, left, and right) by straight lines, which represent ohmic conductances or gap junctions.
> *   **Grounding:** The bottom row of nodes is connected to a horizontal line at the base, which features a standard electrical ground symbol (three horizontal lines of decreasing length), indicating a common reference potential.
>
> **Panel (b): Complex Network Model**
> This panel illustrates a more intricate and complex network arrangement compared to Panel (a).
> *   **Nodes and Structure:** While the main cylindrical nodes are present, the overall structure is denser and more meshed. The connections are more numerous and complex, suggesting a higher level of detail in the model.
> *   **Complexity:** The visual complexity of Panel (b) is interpreted as representing a more advanced model that incorporates additional nodes. According to the accompanying text, these additional nodes represent both intra- and extracellular potentials for each cell, leading to a denser, more interconnected network than the simple lattice shown in Panel (a).
> *   **Grounding:** Similar to Panel (a), the bottom nodes are connected to a common ground reference line.
>
> The diagram serves as a visual comparison between a basic, regularly coupled cell network (a) and a more sophisticated, multi-potential network (b) used to model the electrical activity of cardiac tissue.

<center>Figure 5. Schematic representations of network models in two dimensions: (a) nodes representing individual cells or small groups of identical cells are coupled to their immediate neighbors via ohmic resistors representing gap junctions, and (b) a more complex network arrangement incorporating additional nodes representing both intra- and extracellular potentials for each cell (represented by small cylinders in the figure). </center>

modeled are embodied in the dynamics of the underlying single cell models and the coupling conductances.

The total membrane current for each cell in the network includes a contribution from each of its neighbors. This current is determined by Ohm's law as the product of the coupling conductance and the difference in membrane potentials. For a given cell

\[i_{n} = g_{n}(V_{\mathrm{m}} - V_{\mathrm{m},n}), \quad (12)\]

where \(i_{n}\) is the contribution to the membrane current due to its neighbor \(n\) , \(V_{\mathrm{m}}\) is the membrane potential of the cell in question, and \(V_{\mathrm{m},n}\) is the membrane potential of the neighboring cell. The total membrane current ( \(i_{\mathrm{m}}\) ) is therefore the algebraic sum of the cell's intrinsic ionic and capacitive currents ( \(i_{\mathrm{ion}} + i_{\mathrm{c}}\) ), and it is equal to the contribution from its \(N\) neighbors; i.e.,

\[i_{\mathrm{m}} = C_{\mathrm{m}}\frac{dV_{\mathrm{m}}}{dt} +i_{\mathrm{ion}} = \sum_{n = 1}^{N}g_{n}(V_{\mathrm{m}} - V_{\mathrm{m},n}). \quad (13)\]

Therefore,

\[C_{\mathrm{m}}\frac{dV_{\mathrm{m}}}{dt} = -i_{\mathrm{ion}} + \sum_{n = 1}^{N}g_{n}(V_{\mathrm{m}} - V_{\mathrm{m},n}) \quad (14)\]

Network models have the advantage of being simple to construct and solve. As a result, the earliest multicellular cardiac tissue models were one- and two- dimensional network models. Unfortunately, large- scale network models suitable for modeling extended regions of tissue or the whole heart remain computationally formidable. The network approach is also difficult to implement for irregular geometries with spatially varying material properties, as is the case for cardiac tissue.

More complex network structures may be developed by incorporating a layer of additional nodes to account for both the intracellular and the extracellular potentials, as shown in Fig. 5b. The governing equations for such a network are

\[\begin{array}{l}{i_{\mathrm{m}} = C_{\mathrm{m}}\frac{dV_{\mathrm{m}}}{dt} +i_{\mathrm{ion}} = \sum_{n = 1}^{N}g_{\mathrm{i},n}(\Phi_{\mathrm{i}} - \Phi_{\mathrm{i},n})}\\ {= -\sum_{n = 1}^{N}g_{\mathrm{e},n}(\Phi_{\mathrm{e}} - \Phi_{\mathrm{e},n}),} \end{array} \quad (15)\]

where \(\Phi_{\mathrm{i}}\) and \(\Phi_{\mathrm{e}}\) denote the intra- and extracellular potentials of the cell, \(\Phi_{\mathrm{i},n}\) and \(\Phi_{\mathrm{e},n}\) denote those potentials for the neighboring cell \(n\) , \(g_{\mathrm{i},n}\) and \(g_{\mathrm{e},n}\) denote the intra- and extracellular conductivities, and \(V_{\mathrm{m}} = \Phi_{\mathrm{i}} - \Phi_{\mathrm{e}}\) .

## 6. CONTINUUM MODELS

### 6.1. The Bidomain Model

Explicitly modeling the discrete nature of the myocardium at the cellular level is a computationally expensive task. A

significant reduction in computation cost may be achieved by employing a spatially averaged description of the tissue. By appropriate selection of the scale over which this averaging is performed, a suitable compromise between the fidelity of a true, cellular network model of the myocardium and the available computational resources may be achieved. One approach to achieving this goal has been formalized mathematically as the bidomain model, which represents a continuum description of the network structure illustrated in Fig. 5b. A comprehensive treatment of the bidomain model, from its roots in the pioneering work of Hodgkin and Huxley (2), may be found in Ref. 31. A less rigorous, although more intuitive summary of the mathematical basis of the bidomain model, is given below.

The bidomain model is founded on the premise that cardiac tissue consists of two interpenetrating domains, representing the volume- averaged properties of the intraand extracellular spaces (32). These two domains are separated by the cell membrane, so that current entering or leaving a domain does so only via the cell membrane and is therefore also volume- averaged. In the bidomain model, currents and potentials are described by continuous partial differential equations.

If the potential in the intra- and extracellular domains are denoted by \(\Phi_{\mathrm{i}}\) and \(\Phi_{\mathrm{e}}\) , respectively, then according to Ohm's law, the corresponding current densities \((J_{i}\) and \(J_{\mathrm{e}}\) \(\mathrm{A} / \mathrm{m}^2\) ) are given by

\[J_{\mathrm{i}} = -\sigma_{\mathrm{i}}\nabla \Phi_{\mathrm{i}} \quad (16)\]

and

\[J_{\mathrm{e}} = -\sigma_{\mathrm{e}}\nabla \Phi_{\mathrm{e}}, \quad (17)\]

where \(\sigma_{\mathrm{i}}\) and \(\sigma_{\mathrm{e}}\) are the volume- averaged conductivities of the intra- and extracellular domains, respectively. In general, \(\sigma_{\mathrm{i}}\) and \(\sigma_{\mathrm{e}}\) are tensor quantities and are diagonal when the global Cartesian coordinate system is aligned with the principle directions of conductivity of the tissue. If the tissue is "isotropic," then the diagonal elements are equal and the current densities in (Equations 16 and 17) are aligned with the potential gradients. If the tissue exhibits a direction of preferential conduction, that is, the tissue is "anisotropic," then the diagonal elements of the conductivity tensors are not equal. In cardiac tissue, preferential conduction occurs in the direction of muscle fiber orientation. In the anisotropic case, current densities in (Equations 16 and 17) are not aligned with the potential gradients.

The intra- and extracellular current densities are coupled by way of a conservation relationship. Current leaving one domain enters the other domain via the cell membrane in the form of the transmembrane current \((I_{\mathrm{m}})\) expressed as a volume current density \((\mathrm{A} / \mathrm{m}^3)\) ; i.e.,

\[-\nabla \cdot \boldsymbol {J}_{\mathrm{i}} = I_{\mathrm{m}} - I_{\mathrm{si}} \quad (18)\]

and

\[-\nabla \cdot \boldsymbol {J}_{\mathrm{e}} = -I_{\mathrm{m}} - I_{\mathrm{se}}, \quad (19)\]

where \(I_{\mathrm{si}}\) and \(I_{\mathrm{se}}\) represent the stimulus current volume densities \((\mathrm{A} / \mathrm{m}^3)\) applied to the intracellular and extracellular domains, respectively.

Substituting (Equations 16 and 17) into (Equations 18 and 19),

\[\nabla \cdot (\sigma_{\mathrm{i}}\nabla \Phi_{\mathrm{i}}) = I_{\mathrm{m}} - I_{\mathrm{si}} \quad (20)\]

and

\[\nabla \cdot (\sigma_{\mathrm{e}}\nabla \Phi_{\mathrm{e}}) = -I_{\mathrm{m}} - I_{\mathrm{se}}, \quad (21)\]

and therefore,

\[\nabla \cdot (\sigma_{\mathrm{i}}\nabla \Phi_{\mathrm{i}}) = -\nabla \cdot (\sigma_{\mathrm{e}}\nabla \Phi_{\mathrm{e}}) - I_{\mathrm{si}} - I_{\mathrm{se}}. \quad (22)\]

Equation 22 may be rewritten in terms of the transmembrane potential \(V_{\mathrm{m}} = \Phi_{\mathrm{i}} - \Phi_{\mathrm{e}}\)

\[\nabla \cdot (\sigma_{\mathrm{i}}\nabla V_{\mathrm{m}}) = -\nabla \cdot ((\sigma_{\mathrm{i}} + \sigma_{\mathrm{e}})\nabla \Phi_{\mathrm{e}}) - I_{\mathrm{si}} - I_{\mathrm{se}}. \quad (23)\]

Now, from the Hodgkin- Huxley theory, the transmembrane current is the sum of the membrane capacitive current and the total transmembrane ionic current; i.e.,

\[I_{\mathrm{m}} = A_{\mathrm{m}}i_{\mathrm{m}} = A_{\mathrm{m}}\left(C_{\mathrm{m}}\frac{\partial V_{\mathrm{m}}}{\partial t} +i_{\mathrm{ion}}\right), \quad (24)\]

where \(A_{\mathrm{m}}\) is the surface- to- volume ratio \((\mathrm{m}^{- 1})\) , effectively transforming the transmembrane current \((i_{\mathrm{m}}, \mathrm{A} / \mathrm{m}^2)\) into a source per unit volume \((I_{\mathrm{m}}, \mathrm{A} / \mathrm{m}^3)\) , \(C_{\mathrm{m}}\) is the specific membrane capacitance \((\mathrm{F} / \mathrm{m}^2)\) , and \(i_{\mathrm{ion}}\) is the sum of the transmembrane ionic currents \((\mathrm{A} / \mathrm{m}^2)\) .

From (Equation 21),

\[-\nabla \cdot (\sigma_{\mathrm{e}}\nabla \Phi_{\mathrm{e}}) = A_{\mathrm{m}}\left(C_{\mathrm{m}}\frac{\partial V_{\mathrm{m}}}{\partial t} +i_{\mathrm{ion}}\right) - I_{\mathrm{se}}. \quad (25)\]

Substituting into (Equation 23),

\[\nabla \cdot (\sigma_{\mathrm{i}}\nabla V_{\mathrm{m}}) + \nabla \cdot (\sigma_{\mathrm{i}}\nabla \Phi_{\mathrm{e}}) = A_{\mathrm{m}}\left(C_{\mathrm{m}}\frac{\partial V_{\mathrm{m}}}{\partial t} +i_{\mathrm{ion}}\right) - I_{\mathrm{si}}. \quad (26)\]

Equations 23 and 26 are referred to as the extracellular and transmembrane equations, respectively. Together they constitute the bidomain model.

At first glance, the spatial averaging or smoothing inherent in the bidomain equations represents something of a contradiction—cardiac tissue is known to posses a high level of structural organization at the microscopic scale. For example, myocytes in the ventricular wall are organized into parallel fibers, which are in turn organized into laminar sheets (33). Furthermore, ventricular fiber and sheet orientation is known to vary considerably across the thickness of the ventricular wall. This structural organization may be readily included, at a macroscopic

level, in the bidomain equations in the form of spatially varying conductivity tensors.

### 6.2. The Monodomain Equation

The bidomain equations are computationally expensive to solve. As a result, the elliptic and parabolic equations, (Equations 23 and 26), respectively, are often decoupled and solved sequentially by considering \(V_{\mathrm{m}}\) to be fixed in (Equation 23) and \(\Phi_{\mathrm{e}}\) to be fixed in (Equation 26). Acceptable accuracy may then be achieved at reduced computational cost by solving the elliptic equation, which dominates the solution time, on a coarser grid and with larger time steps than the parabolic equation (34). The solution of the elliptic equation may be avoided and the bidomain equations simplified, with a concomitant reduction in the cost of solving them, by assuming that either the extracellular domain is highly conductive (i.e., \(\sigma_{\mathrm{e}} \to \infty\) ) or that the intra and extracellular conductivity tensors are simply related by a constant scaling factor (i.e., \(\sigma_{\mathrm{i}} = k \sigma_{\mathrm{e}}\) ). This last assumption effectively constrains the intra- and extracellular domains to be equally anisotropic at all points. In making either of these assumptions, the extracellular potential \(\Phi_{\mathrm{e}}\) may be eliminated and the bidomain equations, (Equations 23 and 26), reduce to a single monodomain equation,

\[\nabla \cdot (\pmb {\sigma}\nabla V_{\mathrm{m}}) = A_{\mathrm{m}}\left(C_{\mathrm{m}}\frac{\partial V_{\mathrm{m}}}{\partial t} +i_{\mathrm{ion}}\right) - I_{\mathrm{s}}, \quad (27)\]

where \(I_{\mathrm{s}}\) represents the external stimulus current volume density (A/m3).

### 6.3. Boundary Conditions

In addition to specifying initial conditions for all state variables, the solution of the bidomain or monodomain equations requires careful attention to the boundary conditions imposed at the geometric boundaries of the solution domain. In general, such boundary conditions may be classified as either Dirichlet or Neumann.

At a Dirichlet boundary, the value of the solution is known and specified. Such situations are not often employed in cardiac activation modeling, although a Dirichlet condition may be employed in large domains where the solution near the boundary is not of interest.

The most widely employed boundary condition in cardiac activation modeling is the Neumann boundary condition, at which the derivative of the solution is specified, rather than the value of the solution itself. Typically, a zero- flux boundary condition is employed to simulate the effect of a sealed or insulated boundary at which no current can flow across the boundary.

In the bidomain model, the zero- flux boundary condition requires that at the boundary

\[(\sigma_{\mathrm{i}}\nabla \Phi_{\mathrm{i}})\cdot \hat{\pmb{n}} = 0 \quad (28)\]

and

\[(\sigma_{\mathrm{e}}\nabla \Phi_{\mathrm{e}})\cdot \hat{\pmb{n}} = 0, \quad (29)\]

where \(\hat{\pmb{n}}\) is the unit vector normal to the boundary. At the boundary between cardiac tissue and an adjoining extracellular volume conductor, such as a tissue bath, a zero- flux condition (28) is imposed on the intracellular domain only.

For the monodomain formulation, initial conditions and zero- flux boundary conditions are sufficient to solve (27). However, for the bidomain model, zero- flux boundary conditions are not sufficient to generate a unique solution. A Dirichlet boundary condition must also be imposed somewhere in the domain, typically at an extracellular point, to fix the solution at that point to some reference value (usually ground potential).

### 6.4. Simulating Electrical Propagation in Cardiac Tissue

Figure 6 shows the results of a bidomain model simulation on a square two dimensional spatial domain measuring \(100 \times 100\) spatial units (dimensionless). The model equations solved were

\[\nabla \cdot (\pmb {\sigma}_{\mathrm{i}}\upsilon_{\mathrm{i}}) = i_{\mathrm{m}}, \quad (30)\]

\[\nabla \cdot (\pmb {\sigma}_{\mathrm{e}}\upsilon_{\mathrm{e}}) = -i_{\mathrm{m}} - i_{\mathrm{stim}}, \quad (31)\]

with

\[i_{\mathrm{m}} = \frac{\partial v_{\mathrm{m}}}{\partial t} +c_{1}v_{\mathrm{m}}(v_{\mathrm{m}} - a)(v_{\mathrm{m}} - 1) + c_{2}v_{\mathrm{m}}u, \quad (32)\]

\[\frac{\partial u}{\partial t} = b(v_{\mathrm{m}} - du), \quad (33)\]

\[v_{\mathrm{m}} = v_{\mathrm{i}} - v_{\mathrm{e}}, \quad (34)\]

and all parameters as described previously (see Equations 1 and 2). The conductivity tensors were defined to be isotropic \((\sigma_{\mathrm{i}})\) and anisotropic \((\sigma_{\mathrm{e}})\) as follows:

\[\pmb{\sigma}_{\mathrm{i}} = \left( \begin{array}{cc}1 & 0\\ 0 & 1 \end{array} \right)\quad \mathrm{and}\quad \pmb{\sigma}_{\mathrm{e}} = \left( \begin{array}{cc}1 & 0\\ 0 & 4 \end{array} \right).\]

Zero- flux (Neumann) boundary conditions were imposed at the edges of the domain. Two circular extracellular electrodes were also defined as shown in the figure. The extracellular potential was fixed to 0 at the center of the right- most electrode. At the left- most electrode, a negative extracellular square pulse stimulus current of magnitude 0.08 was applied at \(t = 100\) for a duration of 20 time units, with a current of equal magnitude and opposite polarity applied at the right- most electrode. With these stimulus parameters, the left and right electrodes are cathodic and anodic, respectively.

The top four panels of the figure show the transmembrane potential at various times throughout the simulation and illustrate excitation at the cathode (left) and the outward propagation of the action potential. The action potential waveform at the center of the square domain is illustrated in the lower panel (the site is shown as a black dot in the upper four panels).

> **Image description.** This image is a composite figure illustrating the results of a two-dimensional bidomain simulation, showing the spatial distribution of electrical activity over time and the resulting action potential waveform. The figure is divided into four square panels displaying spatial maps and one line graph displaying temporal data.
>
> The upper portion of the image consists of four square panels, each representing a snapshot of the "Electrical Activity" within a square domain at different time points. A vertical color bar on the right side of these panels serves as a legend, indicating the range of electrical activity from -0.1 (dark/black) to 0.8 (light/white). Each panel features three circular electrode representations: one on the left (cathode), one in the center (where the potential is tracked), and one on the right (anode).
>
> The four spatial panels are labeled with time stamps and show the propagation of activation:
> 1.  **t = 150:** Activation is beginning near the left electrode.
> 2.  **t = 300:** The activation front has moved significantly toward the right.
> 3.  **t = 450:** The activation front is further right, and the central area shows a high degree of depolarization (lighter color).
> 4.  **t = 600:** The activation front is nearing the right electrode, and the central area remains highly depolarized.
>
> The lower panel is a line graph illustrating the transmembrane potential (Vm) over time at the central point of the domain.
> *   **Y-axis:** Labeled "Vm," ranging from 0.0 to 0.8.
> *   **X-axis:** Labeled "Time," ranging from 0 to 1000.
> *   **Data:** A single curve depicts a characteristic action potential. The potential starts low, rises sharply to a peak of approximately 0.7, and then gradually decays back toward baseline, illustrating the depolarization and subsequent repolarization of the cell.
>
> In summary, the figure visually demonstrates how an electrical stimulus delivered via the left electrode causes a wave of depolarization to propagate across the domain, and simultaneously shows the resulting action potential waveform at the center of the domain.

<center>Figure 6. Simulated transmembrane potential in a two-dimensional bidomain model at various times after stimulation via a pair of extracellular electrodes (indicated by circles). A cathodic ( \(- \mathrm{ve}\) ) stimulus current was delivered to the left-most electrode, whereas an anodic ( \(+ \mathrm{ve}\) ) current of equal magnitude was delivered to the right-most electrode. Activation is observed to occur at the cathode (left-most electrode) and to propagate outward across the sheet. The action potential waveform at the center of the square domain (indicated by the black dot in the upper four panels) is illustrated in the lower panel. </center>

The bidomain model represents a powerful example of the ability of mathematical modeling to identify and drive promising avenues for experimental investigation. One success of the bidomain model is its ability to model so- called "virtual electrodes"—regions of activation elicited in response to an electrical stimulus, at sites removed from the physical stimulating electrode. This phenomenon is illustrated in a two- dimensional bidomain simulation shown in Fig. 7. The model employed is the same as that described above with the exception that the magnitude of the stimulus current has been significantly increased, from 0.08 in Fig. 6, to 1. Figure 7 shows a snapshot of the transmembrane potential at \(t = 121\) (i.e., immediately

after termination of the stimulus). As can be observed, the transmembrane potential around the cathode (left) is highly depolarized (max \(\sim 1.3\) ) and that near the anode (right) is significantly hyperpolarized ( \(\sim - 0.7\) ). The presence of depolarized regions of excitation, the virtual electrodes, can be clearly seen above and below the anode. This classic "dog- bone" activation pattern has also been observed in experimental cardiac tissue preparations (35). The virtual electrodes are a result of differences in the anisotropy of the intra- and extracellular domains. As a result, models based on the monodomain equation cannot reproduce this phenomenon.

> **Image description.** This image is a scientific contour plot visualizing a simulated transmembrane potential within a two-dimensional computational model. The visualization uses a grayscale color map to represent the magnitude of the potential across a square domain, with overlaid white contour lines indicating specific isopotential levels.
>
> The main visual area displays a complex electrical field pattern. The potential is represented by shading, where lighter areas correspond to higher positive potential and darker areas correspond to lower or negative potential.
>
> Key features of the potential distribution include:
> *   **Left Region:** A large, roughly circular area on the left side of the domain exhibits a high, bright white potential, suggesting a localized area of maximum positive transmembrane potential.
> *   **Right Region:** On the right side, there is a more intricate, localized pattern of potential changes. This region features a complex arrangement of high and low potential areas, consistent with the "dog-bone" activation pattern mentioned in the accompanying text.
> *   **Contour Lines:** White lines are drawn across the domain, delineating the boundaries between different potential levels, providing a clear visualization of the field's gradients and propagation.
>
> To the right of the main plot, a vertical color bar (legend) provides the scale for the transmembrane potential. This scale ranges from -0.6 (represented by the darkest shade) to 1.2 (represented by the lightest shade), with major increments marked at intervals of 0.2 (e.g., -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2).
>
> Visible text includes the figure caption at the bottom left, which reads: "Figure 7. Simulated transmembrane potential in the two-di..." (the rest is cut off).

<center>Figure 7. Simulated transmembrane potential in the two-dimensional bidomain model of Fig. 6, immediately after delivery of a larger stimulus (magnitude 1.0). This classic "dog-bone" activation pattern, the so-called virtual electrodes, are clearly visible above and below the anode (right-most electrode). </center>

## 7. CURRENT AND FUTURE TRENDS

It is anticipated that detailed ionic models of excitable cardiac tissue will continue to evolve as more experimental data becomes available. Currently, there is a need to develop accurate models that can predict a range of experimentally observed behavior, including changes brought about by disease and drugs. Promising avenues of research include novel experimental designs for developing, optimizing, and validating cell- specific ionic models (36).

In many organ systems, there is increasing recognition that computational biology and mathematical modeling will contribute to the understanding of physiological processes. The models described in this article can span a range of scales from subcellular processes to cells, tissues, and the organ. Multiscale modeling is certainly gaining favor, particularly as the reductionist approach to modeling has provided key validated building blocks from which larger scale models can be assembled. Indeed several international initiatives are working toward providing a public domain framework for computational physiology, including the development of modeling standards, computational tools, and Web- accessible databases of structural and functional models at all spatial scales. A key example is the Physiome project (37), which aims to develop an infrastructure for linking models of biological structure and function in human and other eukaryotic physiology across multiple levels of spatial organization and multiple time scales. The levels of biological organization, from genes to the whole organism, includes gene regulatory networks, protein pathways, integrative cell function, tissue and whole organ structure- function relations, and finally the integrative function of the whole organism.

The heart is an extremely complex organ. Examining cardiac modeling since the early work of Hodgkin and Huxley, it is evident that the focus began at the level of the cell but has expanded upward in spatial scale to include cellular interactions and continuum models of tissue and the organ, as well as electrical activity on the surface of the body. More recently, with the increasing emphasis on genomics, there has been a focus downward in spatial scale to attempt to incorporate models of genetic and molecular information (38). However, the end goal of these modeling approaches, in terms of influencing clinical practice and decision making, is to build accurate integrative models of the entire heart that can predict the effects of disease, drugs, and electrical and mechanical stimulation, as well as shed light on normal and abnormal rhythms often encountered in clinical practice.

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
