```
@article{bath2001vagal,
  title={Vagal entrainment of heart rate is simulated by an integrator with feedback},
  author={Andrew R. Bath and Shaun L. Cloherty and Socrates Dokos and Branko G. Celler and Nigel H. Lovell},
  journal={Australasian Physics \& Engineering Sciences in Medicine},
  year={2001},
  volume={24},
  pages={86-94},
  doi={10.1007/bf03178351},
  url={https://link.springer.com/article/10.1007/BF03178351}
}
```

---

# TECHNICAL REPORT

# Vagal entrainment of heart rate is simulated by an integrator with feedback

Andrew R. Bath \(^{1}\) , Shaun L. Cloherty \(^{2}\) , Socrates Dokos \(^{2}\) , Branko G. Celler \(^{1}\) , and Nigel H. Lovell \(^{2}\) .

\(^{1}\) Biomedical Systems Laboratory, School of Electrical Engineering, University of New South Wales, Sydney, NSW \(^{2}\) Graduate School of Biomedical Engineering, University of New South Wales, Sydney NSW

## Abstract

Paradoxical stable entrainment of heart rate to inhibitory vagal impulses can be simulated with two distinct mathematical models; a complex ionic current model of sinoatrial node pacemaker activity, as well as a simple integrator with nonlinear feedback. We show that both models exhibit similar entrainment characteristics to repetitive vagal stimuli. By applying a sharp disturbance to each model whilst entrained, the subsequent path of cycle length recovery can be described by dynamic phase response curves and phase- phase plots, the properties of which dictate whether stable entrainment is possible.

Key words sinoatrial node, entrainment, vagal stimulus, modelling.

## Introduction

In the physiological laboratory, it is possible to denervate or isolate the heart from all neural inputs except the vagus nerve. When the vagus is stimulated at relatively slow rates, close to that of the heart rate, the heart beats may lock in phase with the vagal impulses, despite the normal inhibitory action of the vagus on the heart. Thus, small changes in the stimulation rate are followed by concomitant changes in the heart rate: a phenomenon known as entrainment \(^{1}\) . Entrainment of the cardiac pacemaker has also been hypothesised to occur in vivo since vagal efferent activity is known to occur in discrete bursts coinciding with the systolic arterial pressure wave via the baroreceptor reflex \(^{2}\) . Elucidating the mechanisms underlying entrainment will lead to a greater understanding of neural control of the heart.

The observation that the negative chronotropic response of the heart to a brief vagal stimulus depends on its timing in the cardiac cycle was first described in the now classic work by Brown and Eccles \(^{3,4}\) . Levy et al. \(^{2,5}\) observed that over a range of stimulus frequencies, heart rate would match vagal stimulus rate. This is 1:1 entrainment (output cycles: input cycles), because there is one output pulse for each input pulse. This form of

entrainment is characterised by a range of matched stimulus rates through which entrainment is sustained, rather than a single point of 1:1 correspondence. Levy et al. named this a "paradoxical" response, because over the range of entrainment, an increase in stimulus rate produces an increase in heart rate. This is at odds with the general effect of vagal stimulation, which is to slow the heart.

Observations of entrainment have been reported in many experimental preparations, including anaesthetised dogs \(^{6,8}\) , conscious dogs \(^{9}\) and anaesthetised rabbits \(^{10}\) . Jalife et al. \(^{11}\) demonstrated entrainment in isolated sinus node preparations of rabbit, cat and sheep. Thus it has been established that entrainment is a property of the sinus node oscillator, and this property is shared by the active heart in vivo.

A useful tool in examining the phenomenon of entrainment is the phase response curve (PRC), which plots sinus cycle length (SCL) as a function of the phase of the inhibitory vagal stimulus within the cycle. In sinoatrial studies, the PRC has a characteristic shape with an initial positive linear slope, a sharp fall- off, followed by a relative "no- effect" region, until the stimulus phase reaches the cycle length. Two types of PRC have been traditionally used by investigators: the transient PRC arising from a one- off single vagal stimulus, or the steady- state PRC arising from stable behaviour during a train of repetitive vagal stimuli \(^{12}\) . Both types of PRC exhibit the characteristic shape described above.

Mathematical models of the sinoatrial node (SAN) have been formulated in varying orders of complexity, all capable of simulating vagal entrainment. Dexter et al. \(^{13,14}\) modelled SAN pacemaker activity using six ion channels, including an acetylcholine- activated potassium current activated by vagal stimulation. Michaels et al. \(^{15,16}\) extended this model to predict phase response curves from triphasic responses to vagal stimulation of isolated cat and rabbit

sinoatrial node tissue preparations. Murphey and Clark 17 used mathematical equations based on the Noble and Noble 18 model of rabbit sinoatrial node activity to also examine parasympathetic control of the heart. More recently, highly complex models of single rabbit SAN cells have been described, having an order of 100 or so parameters and 20- 30 state variables describing membrane currents, active transporters and ion concentrations 19,20. An analogous model of vagal control of a single amphibian sinus venous pacemaker cell has also been reported 12. A review of these and other models can be found in Dokos et al. 21.

Despite considerable differences in their mathematical complexity and physiological accuracy, each model was able to demonstrate entrainment. Ikeda et al. 22 argued from a difference equation model of the cardiac pacemaker that any system with the characteristic PRC will exhibit a pattern of entrainment. This is in agreement with studies in a wide variety of biological systems which suggest that a positive linear slope region of the PRC is sufficient to allow entrainment by periodic inhibitory stimulation 23,24. However, the source of the PRC in the intricacies of nonlinear ionic equations of the cardiac pacemaker has not been determined.

## A Control Hypothesis for Entrainment

From their observations, Levy et al.5 proposed a control theory based on the steady- state PRC, to account for the entrainment observed in animal experiments. They proposed that entrainment may be observed at a point where the steady- state PRC produces a sinus cycle length equal to the stimulus period, with the stability of this point attributable to the slope of the PRC. In regions of positive slope, a slight lengthening of the sinus cycle would result in the inhibitory stimulus falling early in the subsequent cycle. This causes a shortening of the cycle in a form of negative feedback, to stabilise the entrainment point. Where the PRC has negative slope, this feedback would push the system away from the potential entrainment point, so entrainment is not observed. Thus, the steady- state PRC predicts the range of stimulus periods for which entrainment is observed, from the beginning to the end of the positive slope region.

A study by Perkel et al. 25 observed a similar effect in the neural pacemaker cells of sea slugs and crayfish when subjected to inhibitory postsynaptic potentials. This study further observed that entrainment is stable for PRC slopes between zero and two (the dimensions are time/time, ie: dimensionless). For slopes less than one, stability is achieved by gradual progression along the PRC towards the stable point. For slopes between one and two, stability would be reached in a series of overcorrections of the cycle length, jumping from one side of the stable point to the other on the PRC but gradually converging to entrainment. In terms of vagal control of heart rate, many studies have reported entrainment and constructed phase response curves, but none have tested whether the SAN membrane obeys this control hypothesis when disturbed from states of stable entrainment.

## A Simple Model of Sinoatrial Cell Behaviour

Entrainment is observed across a sufficiently wide variety of models of differing complexity to suggest that some fundamental property shared by all the models might be the source of the phenomenon. It would be valuable to develop a very simple model which also has this property. A sufficiently simple model would be easily solved over many cycles, offering few complications to numerical simulation. Examining the behaviour of this model might contribute to understanding the nature of entrainment, particularly the mechanisms underlying the positive slope region of the PRC. Such a model is derived and analysed in this paper.

Almost all SAN models are modifications of Hodgkin and Huxley's 26 excitable membrane, modelled as a series of conductive ionic channels in parallel with a capacitance C. The membrane potential \(V\) is proportional to a time integration \(dt\) of the sum current \(i\) flowing

\[V = -\frac{1}{C}\int i\cdot dt \quad (1)\]

where \(V\) is the membrane potential, \(C\) is the constant capacitance, and \(i\) is the sum of currents flowing as a function of time \(t\) . These models are nonlinear because each current is a complex function of membrane potential, time- dependent gating variables and ion concentrations.

The capacitive structure may be modelled very simply by an integrator which has a mechanism for resetting when the membrane potential reaches a threshold value, to simulate an action potential. Such a model has a constant input, to generate a train of spontaneous resets, and a simple nonlinearity may be introduced by applying negative feedback to the input which is proportional to the output. This is appropriate, because each current is to some extent proportional to the membrane potential. When a threshold is reached, the action potential rises from a rush of ions generated by positive feedback, so the feedback function in the simple model includes a region of positive feedback above the first threshold, until a second threshold is reached - and the integrator output is reset to zero.

## Materials and Methods

## The Sinoatrial Node Model

A detailed biophysical model of electrical activity in single SAN cells has been derived from physiological principles and observations by Dokos et al. 19,27. This is a lumped parameter model, incorporating the movements of sodium, potassium and calcium ions across the cell membrane and sarcoplasmic reticulum, as well as nine sarcolemma currents governed by fourteen gating variables. Vagal stimulation is included as a three- compartment model for acetylcholine release and uptake. The acetylcholine acts primarily on an ACh- activated potassium channel, with secondary actions on other

currents. This model provides an excellent correlation to the behaviour of single SAN cells observed in the laboratory.

## The Integrator with Feedback Model

The integrator block has a threshold- triggered reset which returns the output to zero instantaneously when the threshold is reached. The threshold is set at 1.0, and all other magnitudes are scaled against it. The integrator block receives input from a summing block, which combines a constant input, an inhibitory input, and negative feedback which is proportional to the instantaneous integrator output. The feedback function is discontinuous at an intermediate threshold 0.75. This simulates the membrane potential at which the onset of an action potential occurs. The integrator with feedback is modelled as shown in Figure 1. Negative feedback is governed by the equation

\[g(r) = \left\{ \begin{array}{ll}c\cdot r(t), & 0< r(t)< 0.75\\ c\cdot (r(t) - 1), & 0.75< r(t)< 1 \end{array} \right. \quad (2)\]

where \(r(t)\) is the integrator output magnitude, and \(c\) is the feedback constant. The integrator model parameters used in this study are given in Table 1.

> **Image description.** A technical block diagram, labeled "Figure 1. Block diagram of the integrator with feedback model," illustrating a mathematical model used to simulate the behavior of a single SAN cell. The diagram shows several interconnected blocks representing inputs, processing units, and feedback loops.
>
> The model begins with two primary inputs feeding into a central summing block:
> 1.  **Constant Input B:** Represented by a block labeled "Constant Input B."
> 2.  **Inhibitory Input h(t):** Represented by a block labeled "Inhibitory Input h(t)."
>
> These two inputs converge at a circular summing block, which combines them to produce a signal that flows into the main processing unit, the **Integrator g(r)**.
>
> The Integrator block is the core of the system. Its output is labeled **Output r(t)**. This output signal is routed in two directions:
> 1.  It feeds into a **Reset** block, which, according to the context, triggers an instantaneous return of the output to zero when a threshold is reached.
> 2.  It feeds into a **Feedback** block.
>
> The signal from the Feedback block is then routed back to the summing block, creating a negative feedback loop. This feedback mechanism is governed by the function $g(r)$, which is described in the accompanying text as being discontinuous at an intermediate threshold of 0.75.
>
> In summary, the diagram depicts a closed-loop system where constant and inhibitory inputs are integrated, and the resulting output is modulated by a feedback mechanism that simulates the onset of an action potential, while also being subject to a reset mechanism.

<center>Figure 1. Block diagram of the integrator with feedback model. The output is reset each time the threshold \(r = 1.0\) is reached. Feedback is through the block with function \(g(r)\) . </center>

Table 1. Parameters used for integrator model.

| Parameter | Value |
| :--- | :--- |
| Constant input B | 4.88 |
| Threshold for reset | 1.00 |
| Feedback magnitude c | 5.50 |
| Fast rate constant $c_1$ | 14/s |
| Fast pulse magnitude $A_1$ | 3.90 |
| Slow rate constant $c_2$ | 1/s |
| Slow pulse magnitude $A_2$ | 0.49 |

## Vagal Stimulation of the SAN Model

A train of vagal bursts (three stimuli per burst, with an intra- burst stimulus interval of \(50~\mathrm{ms}\) ) was applied to the SAN model at a fixed period; ie. at regularly spaced intervals, similar to previous simulations of Dokos et al. 19. The number of stimuli per burst was held fixed for all simulations, however the inter- burst interval (referred to hereafter as stimulus period) was varied across a range of 0.56 to 0.84 s in steps of 0.02 s.

At each stimulus period, the model began in its free- running unstimulated condition. Vagal stimuli were then applied for \(25~\mathrm{s}\) . An approximate steady- state condition was judged to have been reached when the sinus cycle lengths were either occuring with constant duration, occuring in a repetitive constant pattern, or were scattered in a fixed bounded region for a period of at least five seconds.

## Inhibitory Stimulation of the Integrator Model

An equivalent stimulus to a vagal pulse as implemented by Dokos et al. 19 is an inhibitory pulse with second order exponential decay, as described by

\[v(t) = A_{1}e^{-c_{1}t} + A_{2}e^{-c_{2}t} \quad (3)\]

where \(\mathbf{A}_1\) is the magnitude and \(\mathbf{c}_1\) the time constant for the fast impulse component, and \(\mathbf{A}_2\) , \(\mathbf{c}_2\) correspond to the slow component. This structure has been proposed by other authors as superior to a first order model 28- 31. The time constants were chosen to be equivalent to the acetylcholine dynamics used in the SAN model.

The parameters for the integrator were chosen to produce behaviour similar to that observed in the SAN model. The constant input B and the feedback magnitude \(c\) were chosen so that the unstimulated integrator reset at a rate equivalent to the SAN model unstimulated rate. They were modified as a pair to preserve this relationship. A train of inhibitory pulses was applied to the integrator model at a range of periods similar to that applied to the SAN model. Cycle lengths were examined to determine the steady- state (as defined above) at each stimulus period.

## Plots Used to Examine Entrainment

The PRC plots sinus cycle length as a function of the timing of an inhibitory pulse in the cycle. It is the most common device used by authors to examine entrainment 5,6,8,13,15,17. Each frequency of stimulation which produces 1:1 entrainment generates a single point on the phase response plot. Connecting these points produces a steady- state PRC. The shape of the steady- state PRC is usually taken to indicate the stability of points of entrainment; a point of 1:1 entrainment is stable where the slope is positive. If, rather than connecting entrainment points, the lengths of successive cycles in the same simulation are plotted, then the curve formed is a dynamic PRC. At stable entrainment, the curve is a single point on the dynamic PRC plot, but where the cycle length is oscillating, a line drawn through the successive cycles shows the path of the oscillation. The dynamic PRC is more useful in our study, as it is a convenient method of depicting the path of recovery of each pacemaker model following perturbation from its stable 1:1 entrainment.

The phase- phase plot (PPP) is a device used in the study of nonlinear dynamics 23 which can be constructed from the dynamic PRC. The plot has the same independent variable as the PRC, but the dependent variable is the phase of the inhibitory stimulus in the subsequent output cycle.

For each point on the plane, the abscissa shows the pulse timing for cycle \(n\) , and the ordinate shows the pulse timing for cycle \(n + 1\) . It can readily be seen that a point of 1:1 entrainment will always appear on the unit diagonal of the plot. Furthermore, it can be shown that where a curve in the PPP crosses the diagonal, stable entrainment will occur if the slope is between minus and plus one (see appendix). If this slope is positive, the output will converge smoothly to entrainment, whereas if it is negative, the output will follow a series of converging overcorrections.

## Construction of Phase Response Curves and Phase-Phase Plots

For the SAN cell and integrator models, a steady- state PRC was constructed using each steady- state point of 1:1 entrainment and the points from the steady oscillation at the frequencies closest to each side of this range.

Dynamic PRC's were generated for both models by perturbing each oscillator from a stable point of 1:1 entrainment, whilst maintaining the periodic train of vagal stimuli. This perturbation generated a new sequence of points for construction of a dynamic PRC, until the pacemaker recovered its steady- state 1:1 entrainment. The SAN cell model was perturbed by instantaneously adding \(40 \mathrm{mV}\) to the membrane potential at a set delay after an action potential. This magnitude was sufficient to trigger a premature action potential, and thus disturb the steady- state activity without altering the acetylcholine concentration. The integrator model was perturbed by instantaneously setting its output to the intermediate threshold of 0.75, thereby eliciting a new action potential.

The points and curves from the dynamic PRC were mapped to phase- phase plots using the function (as derived in the appendix).

\[AS[t[n + 1] = T - CL(ASt[n]) + ASt[n] \quad (4)\]

where \(T\) is the period of stimulation, \(AS[t[n]\) is the stimulus delay in the \(\mathrm{n}^{\mathrm{th}}\) cycle, and \(CL(\mathrm{\Delta})\) is the cycle length, a function of the stimulus delay (as given by the phase response curve).

## Computational Methods

All computation was performed on a \(333\mathrm{MHz}\) Pentium PC. The SAN model was implemented from Dokos'19 equations using GNU \(C / C + +\) . The integrator model and all post- processing for plotting was performed in MATLAB. All values were stored as floating point numbers of eight bytes length, giving fifteen significant decimal digits. Numerical integration of the SAN cell equations was performed using a modified Adams- Bashforth multistep method, as described in a previous study27.

## Results  

The transient and steady- state PRC's of the integrator model are shown in the left hand panels of Figure 2. Entrainment (1:1) was observed over a range of stimulus periods spanning \(0.56 - 0.80\mathrm{s}\) . These values correspond to the minimum and maximum ordinate (SCL) values of the steady- state PRC (Figure 2). Representative time traces of the integrator model output at various points on each PRC are also shown (Figure 2(b) and 2(d)). For both types of PRC shown, it can be seen that if an inhibitory pulse occurs early in the cycle, the cycle is not greatly prolonged. For later pulses, the cycle is prolonged further and further up to the breakpoint, after which, the inhibitory stimulus does not arrive before the output exceeds the intermediate 0.75 threshold. Stimuli falling after the breakpoint have a greatly reduced effect on the cycle length.

> **Image description.** A technical figure consisting of four panels (a, b, c, and d) that illustrate Phase Response Curves (PRCs) and corresponding Phase-Phase Plots for an integrator model, comparing transient and steady-state behavior.
>
> The figure is organized into two rows, with two panels in each row.
>
> **Top Row (Transient Behavior):**
> *   **Panel (a):** This is a line graph titled "Transient." It plots "SCL (s)" (Stimulus Cycle Length in seconds) on the ordinate (Y-axis) against "Stimulus Phase (s)" on the abscissa (X-axis). The curve starts at a low SCL (approximately 0.5s) and increases as the stimulus phase progresses, reaching a peak SCL of around 0.75s near a stimulus phase of 0.4s. Several data points are labeled A, B, C, D, and E along the curve.
> *   **Panel (b):** This is a Phase-Phase Plot titled "Transient." It displays five distinct step functions, labeled A through E. Each function represents a phase shift between cycles. The functions show a sharp jump (representing the phase shift) followed by a plateau, with the magnitude of the shift generally increasing from curve A to curve E.
>
> **Bottom Row (Steady-State Behavior):**
> *   **Panel (c):** This is a line graph titled "Steady-State." It plots "SCL (s)" on the ordinate against "Stimulus Phase (s)" on the abscissa. The curve starts at a lower SCL (approximately 0.5s) and increases, reaching a peak SCL of approximately 0.85s near a stimulus phase of 0.6s. Six data points are labeled A, B, C, D, E, and F along this curve.
> *   **Panel (d):** This is a Phase-Phase Plot titled "Steady-State." Similar to Panel (b), it displays five step functions, labeled A through E. These functions also show phase shifts, but the overall shape and magnitude of the shifts differ from the transient functions in Panel (b).
>
> The figure is partially accompanied by text below the panels, which begins: "Figure 2. (a) Transient phase response curve for the integrator..." This confirms the technical nature of the graphs, where the SCL represents the output timing and the Stimulus Phase represents the input timing. The comparison between the top row (Transient) and the bottom row (Steady-State) illustrates how the system's response changes as it moves from an initial disturbed state to a stable, periodic oscillation.

<center>Figure 2. (a) Transient phase response curve for the integrator model. The integrator output cycle length is shown as a function of the phase of delivery of a single bi-exponential inhibitory pulse. The cycle lengths for the traces shown in (b) are indicated by the circles. The dashed horizontal line indicates the free running cycle length of 0.385s. (b) Transient phase response of the integrator model. The top trace is the integrator output with no inhibitory input. The remaining traces show the inhibitory pulse arriving at different points through the integrator output cycle (indicated by the arrows). The output cycle length is changed by the timing of the input pulse. The horizontal scale in the lower left corner indicates the free running cycle length of 0.385s. (c) Steady-State phase response curve for the integrator model. The integrator output cycle length, at 1:1 entrainment, is shown as a function of the phase of delivery of a periodic train of bi-exponential inhibitory pulses. The cycle lengths for the traces shown in (d) are indicate by the circles. (d) Steady-state phase response of the integrator model. Each trace shows a single cycle, at 1:1 entrainment, of the integrator output corresponding to a different stimulus period. Inhibitory pulses are indicated by the arrows. The horizontal scale in the lower left corner indicates the free running cycle length of 0.385s. </center>

Analogous behaviour for the SAN model is shown in Figure 3. In the SAN model, 1:1 entrainment was observed for stimulus periods ranging from 0.58 to 0.82s. Both transient and steady- state PRC's are similar in shape to those of the integrator model. Vagal pulses arriving later in the cycle (for both types of PRC), have a greater effect in prolonging the SCL, up until a breakpoint is encountered.

> **Image description.** A composite image consisting of two stacked line graphs, labeled (a) and (b), which illustrate phase response curves for a SAN model. Both graphs use a black line on a white background and share a common theme of plotting Sinus Cycle Length (SCL) against Stimulus Phase.
>
> **Panel (a): Transient Phase Response Curve**
> This upper graph is titled "Transient" and depicts the transient phase response.
> *   **Y-axis:** Labeled "SCL," with a scale ranging from 0.4 to 0.8, marked in increments of 0.1.
> *   **X-axis:** Labeled "Stimulus Phase (s)," with a scale ranging from 0 to 0.4, marked in increments of 0.1.
> *   **Data Curve:** A single, continuous black line. The curve begins at an SCL of approximately 0.45 at a phase of 0. It rises sharply, reaching a peak SCL of approximately 0.75 around a phase of 0.25. Following this peak, the line drops steeply and then flattens out, maintaining a relatively stable SCL of around 0.5 for the remainder of the plotted phase.
>
> **Panel (b): Steady-State Phase Response Curve**
> This lower graph is titled "Steady-State" and depicts the steady-state phase response.
> *   **Y-axis:** Labeled "SCL," with a scale ranging from 0.4 to 0.9, marked in increments of 0.1.
> *   **X-axis:** Labeled "Stimulus Phase (s)," with a scale ranging from 0 to 0.6, marked in increments of 0.1.
> *   **Data Curve:** A single, continuous black line. Unlike the transient curve, this line shows a consistent, nearly linear upward trend across the entire visible range. It starts at an SCL of approximately 0.65 at a phase of 0 and increases steadily to an SCL of approximately 0.85 at a phase of 0.6.
>
> **Caption and Context**
> Below the graphs, the figure is captioned: "Figure 3. (a) Transient phase response curve for the SAN model. Sinus cycle length is shown as a function of the phase of delivery of a single vagal stimulus burst. (b) Steady-State phase response curve for the SAN model. Sinus cycle length, at 1:1 entrainment, is shown as a function of the phase of delivery of a periodic train of vagal stimulus bursts."

<center>Figure 3. (a) Transient phase response curve for the SAN model. Sinus cycle length is shown as a function of the phase of delivery of a single vagal stimulus burst. (b) Steady-State phase response curve for the SAN model. Sinus cycle length, at 1:1 entrainment, is shown as a function of the phase of delivery of a periodic train of vagal stimulus bursts. </center>

At this point, the hyperpolarising \(\mathbf{K}^{+}\) current activated by ACh can no longer counterbalance the large depolarising currents underlying action potential upstroke 19. Thus, the action potential is not appreciably delayed, producing the "no- effect" region on each PRC.

When the entrained SAN model was perturbed by a 40 mV depolarisation, a series of cycles following the disturbance were plotted as a dynamic PRC moving back towards the point of 1:1 entrainment (Figure 4(a)). Stable 1:1 entrainment points occur at stimulus periods of 0.60, 0.70 and 0.80s, with the paths of recovery indicated by crosses. Other entrainment points between these are not shown, for clarity. At 0.84s the point is almost stable, but then falls out and follows a cycling path across the plane (circles) at points below those of 1:1 entrainment. At 0.56s, a cycle of points (squares) repeats across the plane at points above those of 1:1 entrainment. It can be seen that the points of stable 1:1 entrainment appear to fall on a line between the two oscillating cycles. Other authors have connected these points to form the steady- state PRC, but we believe that this is inappropriate, as we will demonstrate later.

For the integrator model, 1:1 entrainment is observed for stimulus periods of 0.56 to 0.80s. At 0.54s (squares) and 0.82s (circles), the cycle length is unstable and oscillates across the plane.  

For both models, the data of Figure 4 can be mapped onto the phase- phase plane, as shown in Figure 5. For the SAN cell model (Figure 5(a)), the points of 1:1 entrainment fall on the unit diagonal, as expected. At 0.84s, the points lie above the diagonal (circles), and travel to the right as each stimulus delay is longer than the one before it. Similarly, at 0.56s, the points lie below the diagonal (squares), and travel to the left. The closer a point lies toward the diagonal, the smaller the jump will be to the next point. This is seen especially at 0.56s for a large group of points lying very close together close to the diagonal. Where the SAN cell model was perturbed at steady- state, the points are pushed off the diagonal, and then follow a path between the two oscillating cycles until the diagonal is attained at the entrainment point. These trajectories are shown on Figure 5(a) as crosses. For the three entrainment points shown, the recovery paths lie parallel to each other.

> **Image description.** A technical figure consisting of two stacked line graphs, labeled (a) and (b), illustrating dynamic phase response curves (PRCs) for two different models: the SAN Cell and the Integrator.
>
> **Panel (a): SAN Cell Model**
> This upper graph is labeled "SAN Cell" and is titled "Figure 4. (a) Dynamic phase response curve for the SAN model."
> *   **Axes:** The vertical Y-axis is labeled "SCL (s)" (Sinus Cycle Length in seconds), ranging from 0.4 to 1.2. The horizontal X-axis is labeled "Stimulus Phase," ranging from 0 to 0.6.
> *   **Data Pattern:** A single, continuous line graph shows the relationship between SCL and Stimulus Phase. The curve begins at an SCL of approximately 0.6 at Phase 0. It rises steadily, reaching a peak SCL of approximately 1.1 around Phase 0.3. Following this peak, the curve drops sharply to an SCL of approximately 0.6 at Phase 0.4, and then continues to decline slightly toward the end of the plotted phase.
>
> **Panel (b): Integrator Model**
> This lower graph is labeled "Integrator" and is titled "Figure 4. (b) Dynamic phase response curve for the Integrator model."
> *   **Axes:** The vertical Y-axis is labeled "SCL (s)," ranging from 0.4 to 1.0. The horizontal X-axis is labeled "Stimulus Phase," ranging from 0 to 0.6.
> *   **Data Pattern:** A single, continuous line graph shows the relationship between SCL and Stimulus Phase. The curve starts at an SCL of approximately 0.6 at Phase 0. It rises steadily, reaching a peak SCL of approximately 0.9 around Phase 0.3. Similar to the upper graph, the curve drops sharply to an SCL of approximately 0.6 at Phase 0.4, before continuing to decline slightly.
>
> Both panels utilize the same axis labels and structure, comparing the dynamic response of two distinct mathematical models to a periodic stimulus. The SAN Cell model (a) exhibits a higher maximum SCL response compared to the Integrator model (b).

<center>Figure 4. (a) Dynamic phase response curve for the SAN model. The stable 1:1 entrainment points for stimulus periods of 0.60, 0.70 and 0.80s, are shown together with the paths taken to recover these points after perturbation (crosses). The PRC for stimulus periods of 0.56s (squares) and 0.84s (circles), just outside the 1:1 entrainment range, are also shown. Stable entrainment is observed where the points lie closely merged. (b): Dynamic phase response for the integrator model. Again, the stable 1:1 entrainment points for stimulus periods of 0.6, 0.7 and 0.8s (crosses) are shown, together with the paths taken to recover these points after perturbation. The upper and lower curves show the complete PRC for stimulus periods of 0.54s (squares) and 0.82s (circles), just outside the 1:1 entrainment region. </center>

When the corresponding data from the integrator model is mapped to a PPP (Figure 5(b)), more information is apparent. Each point of 1:1 entrainment lies where a PPP crosses the diagonal with slope less than one. Where the PPP crosses back with slope greater than one (at the breakpoint), the cycle length would be unstable, and so entrainment is not observed. At 0.54s (squares) and 0.82s (circles), the PPP does not cross the diagonal at all, and so entrainment is not possible.

## Discussion

Entrainment of the cardiac rhythm by vagal stimulus pulses has been observed experimentally, both in in vitro SAN tissue preparations and in the whole animal. There is no clear consensus on the aetiology of this anomalous behaviour, although many authors have demonstrated entrainment in SAN models of varying complexity and

physiological accuracy. In this study, we demonstrate that a simple idealized model of cardiac pacemaker activity exhibits similar patterns of entrainment to that of a highly complex model of single cell SAN activity.

> **Image description.** A scientific figure consisting of two panels, (a) and (b), which are phase-phase plots illustrating the dynamics of two different models: the SAN Cell and the Integrator. Both plots share identical axis scales and represent the relationship between stimulus phase at time N and stimulus phase at time N+1.
>
> **General Layout and Axes:**
> Both panels are line graphs with a coordinate system ranging from 0.0 to 0.6 on the horizontal axis (Stimulus Phase (N) s) and 0.0 to 0.8 on the vertical axis (Stimulus Phase (N+1) s). A dashed diagonal line, representing the unit diagonal, runs from the bottom-left corner to the top-right corner of both plots.
>
> **Panel (a): SAN Cell**
> This panel is labeled "SAN Cell" at the top center. It displays multiple trajectories and data points representing the dynamics of the SAN model.
> *   **Stable Entrainment:** Clusters of black crosses are visible, primarily lying directly on the dashed unit diagonal, indicating points of stable 1:1 entrainment.
> *   **Unstable Cycle Length (Above Diagonal):** A cluster of black circles is visible above the unit diagonal.
> *   **Unstable Cycle Length (Below Diagonal):** A cluster of black squares is visible below the unit diagonal.
> *   The data points are connected by various solid lines, showing the progression of successive cycle lengths across the phase plane.
>
> **Panel (b): Integrator**
> This panel is labeled "Integrator" at the top center. It mirrors the structure and data representation of Panel (a).
> *   **Stable Entrainment:** Similar to Panel (a), clusters of black crosses are visible on the dashed unit diagonal, indicating stable 1:1 entrainment.
> *   **Unstable Cycle Length (Above Diagonal):** A cluster of black circles is visible above the unit diagonal.
> *   **Unstable Cycle Length (Below Diagonal):** A cluster of black squares is visible below the unit diagonal.
> *   The trajectories in this panel also show the progression of cycle lengths, demonstrating a close visual similarity in entrainment behavior to the SAN Cell model.
>
> In summary, the figure visually compares the phase-phase plots of a complex SAN cell model and a simplified integrator model, using symbols (crosses, circles, squares) and their position relative to the unit diagonal to distinguish between stable and unstable entrainment states.

<center>Figure 5. (a) The phase-phase plot for the SAN model. Constructed using data mapped from the dynamic PRC of Figure 4(a). Points of stable 1:1 entrainment are indicated by clusters of crosses lying on the unit diagonal (dashed line). At 0.84s the cycle length is unstable and the points lie above the unit diagonal (circles). Similarly, at 0.56s the points lie below the unit diagonal (squares). (b) The phase-phase plot for the integrator model. Constructed using data mapped from the dynamic PRC of Figure 4(b). Again, points of stable 1:1 entrainment are indicated by clusters of crosses on the diagonal (dashed line). At stimulus periods of 0.82s and 0.54s, resulting in unstable cycle lengths, the trajectories lie above (circles) and below (squares) the unit diagonal respectively. </center>

## The Integrator Model Simulates Entrainment

There are many similarities between the SAN cell and integrator model PRCs. 1:1 entrainment is observed across a similar range of stimulus periods. Each PRC has a characteristic shape with a positive slope followed by a rapid drop- off and ending in a "no- effect" region (Figures 2 and 3). Successive cycle lengths travel across the plane above and below the steady- state points on each dynamic PRC (Figure 4). This creates an unstable oscillation in cycle length which may appear as a regular 'beating' pattern, or an irregular scattering of cycle lengths.

It would be expected that the complexity of the SAN model would modify the entrainment behaviour from the ideal integrator model. In fact, it was surprising to find such close agreement between the entrainment regions in these two models. The idealised features of the integrator model are probably the major cause of the discrepancies.

## Shape of the Phase Response Curves

The important features of the integrator dynamic PRC (Figure 4(b)) can be identified and explained with reference to the time traces in the right hand panels of Figure 2. In the positive- slope region of each PRC, the cycle length grows

as the stimulus falls later in the cycle. This region ends in the breakpoint, corresponding to the point at which the stimulus falls at the same time as the integrator output reaches the intermediate threshold of 0.75. Before this point, the inhibitory pulse has a maximal effect. In this positive slope region, what is the mechanism in which later stimuli have greater effect in prolonging cycle length? This can be seen from the integrator block diagram of Figure 1. Here, the inhibitory stimuli \(\mathrm{h(t)}\) are subtracted from the difference between a constant input level (B) and a signal that is proportional to the output (c.r(t)), before being integrated to produce the integrator output. That is, the following signal \(\mathrm{v(t)}\) is integrated to produce the output signal:

\[\mathrm{v}(t) = \{B - c.r(t)\} -h(t) \quad (5)\]

In the early phase of the cycle, the output is near 0, and the expression \(\{B - c.r(t)\}\) in (5) is large. Thus, the effect of an inhibitory stimulus at this time is strongly counter balanced. At later phases of the cycle however, \(r(t)\) is larger and \(\{B - c.r(t)\}\) is consequently reduced. Thus, inhibitory stimuli are able to have a greater effect on the cycle by virtue of the reduced opposing signal acting against the inhibitory input.

A similar mechanism acts in the case of the complex SAN cell model, as well as in all other ionic models of pacemaker activity. Here the dominant inhibitory stimulus acting on the membrane (integrator) is the ACh- activated outward \(\mathrm{K}^{+}\) current, whose fully- activated current- voltage relationship \(\overline{i_{K,ACB}}\) is given by

\[\overline{i_{K,ACB}} = g(E - E_K) \quad (6)\]

where \(g\) is the membrane conductance of this current, \(E\) is the transmembrane potential and \(E_K\) is the equilibrium potential for \(\mathrm{K}^{+}\) . During pacemaker depolarisation, the electrochemical driving force \((E - E_K)\) is positive, becoming more positive as \(E\) depolarises further. Thus, in later phases of the cycle where \(E\) has depolarised to more positive values, more \(\mathrm{i_{K,ACB}}\) can be activated at the same level of ACh concentration. This leads to a positive slope in the PRC characteristic, enabling stable entrainment to be attained.

The shape of the dynamic PRC for the SAN model is qualitatively similar to that of the integrator model (Figure 4). Furthermore, the integrator model suggests that curves for neighbouring stimulus periods should be parallel in this region, and that a perturbed membrane should follow the appropriate curve to recover stability. The paths of recovery for the SAN model are parallel, as predicted by the integrator. The oscillation paths above and below the entrainment region are also approximately parallel. Thus, the analogy between the SAN and integrator models explains the recovery behaviour.

## A Refinement of the Theory for Stability of Entrainment

Comparing the perturbation of the SAN model with the dynamic PRC's of the integrator model for steady- state

points of 1:1 entrainment provides an explanation for the stability of entrainment. For any given stimulus period, there is a dynamic PRC governing the cycle lengths. As the stimulus period decreases, the dynamic PRC moves up its plane to longer cycle lengths, probably due to an increase in the mean value of the inhibitory stimuli. Stable 1:1 entrainment will occur where a point on the dynamic PRC gives a cycle length corresponding to the stimulus period, and the slope is between zero and two. If the SAN model is disturbed from 1:1 entrainment, it follows this PRC to regain the stable state.

Notice that this differs from the control hypothesis of Levy \(^{5}\) not in principle, but in detail. The governing PRC is not formed by connecting the points of stable 1:1 entrainment. In fact, if such a steady- state PRC is mapped to the phase- phase plane, it falls exactly along the diagonal; the information about stability is lost. It has a slope of exactly one, which would imply that every point is marginally stable, and that if a point is perturbed, a new steady- state point is obtained. Clearly this implication is inappropriate and incorrect.

## Oscillation to entrainment

Perkel et al. \(^{25}\) observed that when the PRC had a slope between one and two, the stable entrainment point was achieved via a series of over corrections. This corresponds on the phase- phase plot to a curve crossing the diagonal with small negative slope \((- 1.0 < \text{slope} < 0.0)\) , for which an iterative mapping produces the same path of over corrections. For the SAN and integrator models, the phase- phase curve only has negative slope at the breakpoint, and it is very large, so there is no stable point which is reached by over corrections. Hence, an oscillating recovery back to stable entrainment is not observed.

## Limitations of the Integrator Model

In constructing the integrator model it was desired to reach the simplest possible configuration which would still exhibit entrainment. Many features of a SAN cell have been ignored, and some features of the integrator are clearly unrealistic. For example, the SAN action potential and repolarisation are modelled in the integrator by a region of positive feedback, followed by an instantaneous reset of output magnitude. The point at which this begins is the intermediate threshold, which has been set arbitrarily at 0.75. The feedback is not really positive after this point, just less negative, allowing an acceleration to the reset point. In the SAN cell model, repolarisation is not instantaneous, and the intermediate threshold is well established.

A criticism of the integrator model is the shape of its wave in the slow depolarisation phase. The feedback causes stronger inhibition as the integrator output rises, and so the output curve flattens as it approaches the onset of positive feedback. In contrast, the SAN cell model shows an increase in membrane potential whose derivative slightly increases with time during diastolic depolarisation. The feedback block is necessary for entrainment. If there is no feedback to the integrator, there is no phase dependence in

the system. That is, the length of the output cycle is not dependent on the timing of an inhibitory pulse in the cycle. Without this property, the PRC is flat, and there is no opportunity for entrainment. In the SAN cell model, negative feedback is effectively implemented by equation (1), where ignoring time- dependent kinetics, total membrane current \(i\) is a non- linear function of membrane potential \(V\) . It is possible to modify the feedback function \(g(r)\) of the integrator model so that the output more closely resembles that of the SAN cell model, however this was beyond the scope of the present study.

## Implications

There is clearly room for development of the integrator model to find a stronger analogy with the SAN cell. This may assist in the development of simpler models of the SAN, from which models of the heart and its control system may eventually develop.

In this study, a test has been performed which may be replicated in the animal laboratory. Perturbation of the membrane potential under steady- state vagal stimulation requires an artificial stimulation of the sinoatrial tissue directly, under suitably controlled conditions. Thus the conclusions derived here may be tested in living tissue.

A clearer understanding of this behaviour could assist in the development of theories for the control of the heart by the nervous system. The autonomic activity reaching the heart acts through a system which exhibits nonlinear behaviour. Is this an advantage to the control system, or a hurdle to be overcome? In disease, is this one source of the characteristic patterns which are seen in cardiac arrhythmias? These are topics which bear long- term investigation. The phase dependency of the SAN suggests that it would be advantageous for the position control of vagal impulses to be incorporated in baroreceptor reflex control of the heart rate, as has already been suggested \(^{2,16}\) by other investigators.

## Conclusions

The results presented should help to clarify the aetiology of an anomolous mechanism which has long been commented on in the literature. Entrainment occurs even in very simple models of the sinoatrial node electrical activity. By virtue of its integrating and negative feedback characteristics, the simple model used here is intrinsic to all of the more complex models established in the literature. As a result all of the complex models exhibit entrainment.

A distinction has been drawn amongst phase response curves developed under steady- state vagal stimulation. If the points of 1:1 entrainment are connected (steady- state PRC), then the stability information is lost. If small perturbations are applied to the membrane, then a dynamic phase response curve can be constructed, allowing stability information to be ascertained. This is also true of the phase- phase plots, which have been introduced in this study as a valuable tool for the examination of vagal entrainment of the heart rate.

## Acknowledgment

This research was supported by a grant from the Australian Research Council.

## Appendix

## Mapping the Dynamic Phase Response Curve data to the Phase-Phase Plot

Given the following measurements of timing in the input and output cycles;

\(CL[n] =\) cycle length of cycle number \(n\) \(CL[n + 1] =\) cycle length of the next cycle. \(ASI[n] =\) time from start of cycle n to inhibitory stimulus. \(SIA[n] =\) time from inhibitory stimulus to end of cycle n. \(T =\) period of stimulation.

From these definitions the following sums hold

\[CL[n] = ASI[n] + SIA[n]\] \[T = SIA[n] + ASI[n + 1]\]

Therefore

\[ASI[n + 1] = T - SIA[n] = T - CL[n] + ASI[n]\]

The dynamic phase response curve gives the result for cycle length as a function of stimulus timing

\[CL[n] = CL(ASI[n])\]

and thus, the succeeding stimulus delay is a function of the preceding stimulus delay

\[ASI[n + 1] = T - CL(ASI[n]) + ASI[n]\]

where \(ASI[n]\) is the stimulus delay in the \(\mathbf{n}^{\mathrm{th}}\) cycle, and \(\mathrm{CL}(\) is the cycle length, a function of the stimulus delay. Equation (4) gives the mapping from the phase response plane to the phase- phase plane.

## Stability of a point of 1:1 entrainment

A point of 1:1 entrainment may only be found on the PPP where a curve crosses the diagonal. For each point at which this occurs, there is the potential for entrainment, but only certain points will be stable. Whether the entrainment is stable will depend on the slope of the PPP as it passes through the diagonal.

Consider a section of PPP small enough to approximate a straight line as it passes through the diagonal, with intercept of the y- axis at \(c\) and slope \(b\)

\[a[n + 1] = b a[n] + c\]

where \(\mathbf{a[n]}\) is the stimulus delay for the \(n^{th}\) output cycle. The point of 1:1 entrainment will occur at

\[a[n + 1] = a[n]\]

Solving by substitution gives this point

\[a[n] = \frac{c}{1 - b} = a_{1:1}\]

Now consider a stimulus falling just beyond this point, with small offset d.

\[a[n] = a_{1:1} + d\] \[a[n + 1] = b a[n] + c\] \[a[n + 1] = \frac{bc}{1 - b} +bd + c = \frac{c}{1 - b} +bd = a_{1:1} + bd\]

For stability, \(a[n + 1]\) must be closer to a 1:1 than \(a[n]\) . Clearly, this will be the case if the magnitude of b is less than 1. Therefore, the requirement for stability of the PRC is that the 1:1 entrainment point is stable only if \(\left|b\right|< 1\) Consider the reverse mapping to the dynamic PRC plane, in the region near a 1:1 entrainment point.

\[CL(ASI[n]) = T - ASI[n + 1] + ASI[n]\] \[= T + (1 - b)ASI[n] + c\]

The constants are \(T\) and \(c\) so the slope of the PRC is \((l - b)\) . By substitution of the stability criterion from above for \(b\) , a 1:1 entrainment point is stable only if the slope of the PRC is positive, but not greater than 2.

## References

1. Jalife, J. and Michaels, D.C. Neural control of sinoatrial pacemaker activity. In: Vagal control of the heart: experimental basis and clinical implications, edited by Levy, M.N. and Schwartz, P.J., Armonk, New York: Futura Publishing Company, Inc., 173-206, 1994.  
2. Levy, M.N., Iano, T. and Zieske, H., Effects of repetitive bursts of vagal activity on heart rate, Circ Res. Vol:30, No:2, 186-95, 1972.  
3. Brown, G.L. and Eccles, J.C., The action of a single vagal volley on the rhythm of the heart beat, J Physiol (Lond). Vol:82, 211-40, 1934.  
4. Brown, G.L. and Eccles, J.C., Further experiments on vagal inhibition of the heart beat, J Physiol (Lond). Vol:82, 242-57, 1934.  
5. Levy, M.N., Martin, P.J., Lano, T. and Zieske, H., Paradoxical effect of vagus nerve stimulation on heart rate in dogs, Circ Res. Vol:25, No:3, 303-14, 1969.  
6. Jalife, J., Fraccola, P. and Moe, G.K. Entrainment of the SA nodal pacemaker by brief vagal bursts in relation to AV conduction. In: Cardiac rate and rhythm, edited by Bouman, L.N. and Jongsma, H.J.: Martinus Nijhoff Publishers, 577-603, 1982.  
7. Yang, T. and Levy, M.N., The phase-dependency of the cardiac chronotropic responses to vagal stimulation as a factor in sympathetic-vagal interactions, Circ Res. Vol:54, No:6, 703-10, 1984.  
8. Yang, T.E., Cheng, J. and Levy, M.N., Effects of the spatial dispersion of acetylcholine release on the chronotropic responses to vagal stimulation in dogs, Circ Res. Vol:67, No:4,844- 51,1990.  
9. Hariman, R.J. and Hoffman, B.F., Effects of ouabain and vagal stimulation on sinus nodal function in conscious dogs, Circ Res. Vol:51, No:6,760- 8,1982.  
10. Moore, E.N., Spear, J.F. and Kronhaus, K.D. The effects of brief vagal and sympathetic stimulation on rate and rhythm changes in the sinus node. In: Cardiac rate and rhythm, edited by Bouman, L.N. and Jongsma, H.J.: Martinus Nijhoff Publishers, 543- 61, 1982.  
11. Jailife, J., Slenter, V.A., Salata, J.J. and Michaels, D.C., Dynamic vagal control of pacemaker activity in the mammalian sinoatrial node, Circ Res. Vol:52, No:6, 642- 56, 1983.  
12. Shumaker, J.M., Clark, J.W. and Giles, W.R., A model of the phase- sensitivity of the pacemaking cell in the bullfrog heart, J Theor Biol. Vol:151, No:2, 193- 230, 1991.  
13. Dexter, F., Levy, M.N. and Rudy, Y., Mathematical model of the changes in heart rate elicited by vagal stimulation, Circ Res. Vol:65, No:5, 1330- 9, 1989.  
14. Dexter, F., Saidel, G.M., Levy, M.N. and Rudy, Y., Mathematical model of dependence of heart rate on tissue concentration of acetylcholine, Am J Physiol. Vol:256, No:2 Pt 2, H520- 6, 1989.  
15. Michaels, D.C., Slenter, V.A., Salata, J.J. and Jailife, J., A model of dynamic vagus- sinoatrial node interactions, Am J Physiol. Vol:245, No:6, H1043- 53, 1983.  
16. Michaels, D.C., Matyas, E.P. and Jailife, J., A mathematical model of the effects of acetylcholine pulses on sinoatrial pacemaker activity, Circ Res. Vol:55, No:1, 89- 101, 1984.  
17. Murphey, C.R. and Clark, J.W. Parasympathetic control of the SA node cell in rabbit heart - a model. In: Activation, metabolism and perfusion of the heart, edited by Sideman, S. and Beyar, R.: Martinus Nijhoff Publishers, 44- 60, 1987.  
18. Noble, D. and Noble, S.J., A model of sino- atrial node electrical activity based on a modification of the DiFrancesco- Noble (1984) equations, Proc R Soc Lond B Biol Sci. Vol:222, No:1228, 295- 304, 1984.  
19. Dokos, S., Celler, B.G. and Lovell, N.H., Vagal control of sinoatrial rhythm: a mathematical model, J Theor Biol. Vol:182, No:1, 21- 44, 1996.  
20. Demir, S.S., Clark, J.W. and Giles, W.R., Parasympathetic modulation of sinoatrial node pacemaker activity in rabbit heart: a unifying model, Am J Physiol. Vol:276, No:6 Pt 2, H2221- 44, 1999.  
21. Dokos, S., Lovell, N.H. and Celler, B.G., Review of ionic models of vagal- cardiac pacemaker control, J Theor Biol. Vol:192, No:3, 265- 74, 1998.  
22. Ikeda, N., Tsuruta, H. and Sato, T., Difference equation model of the entrainment of myocardial pacemaker cells based on the phase response curve, Biol Cybern. Vol:42, No:2, 117- 28, 1981.  
23. Glass, L. and Mackey, M. From clocks to chaos: the rhythms of life, Princeton, New Jersey: Princeton University Press, 1988.  
24. Winfree, A.T. When time breaks down: the three- dimensional dynamics of electrochemical waves and cardiac arrhythmias. Princeton, New Jersey: Princeton University Press, 1987.  
25. Perkel, D.H., Schulman, J.H., Bullock, T.H., Moore, G.P. and Segundo, J.P., Pacemaker neurons: effects of regularly spaced synaptic input, Science. Vol:145, 61, 1964.  
26. Hodgkin, A.L. and Huxley, A.F., A quantitative description of membrane current and its application to conduction and excitation in nerve, J Physiol (Lond). Vol:117, 500- 44, 1952.  
27. Dokos, S., Celler, B. and Lovell, N., Ion currents underlying sinoatrial node pacemaker activity: a new single cell mathematical model, J Theor Biol. Vol:181, No:3, 245- 72, 1996.  
28. Henning, R.J., Masuda, Y., Yang, T.N. and Levy, M.N., Rate of acetylcholine hydrolysis affects the phase dependency of cardiac responses to vagal stimulation, Cardiovasc Res. Vol:21, No:3, 169- 76, 1987.  
29. Loffelholz, K. and Pappano, A.J., The parasympathetic neuroeffector junction of the heart, Pharmacol. Rev. Vol:37, 1- 24, 1985.  
30. Celler, B.G., Characteristics of cardiac period responses to prolonged vagal stimulation in dogs, Med Biol Eng Comput. Vol:27, 595- 602, 1989.  
31. Celler, B.G. and Lovell, N.H., Dynamics of cardiac period responses after prolonged vagal stimulation in the dog, Ann Biomed Eng. Vol:19, No:3, 273- 89, 1991.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
