```
@article{lim2008noninvasive,
  title={Noninvasive Average Flow and Differential Pressure Estimation for an Implantable Rotary Blood Pump Using Dimensional Analysis},
  author={Emily Lim and Dean M. Karantonis and John A. Reizes and Shaun L. Cloherty and David G. Mason and Nigel H. Lovell},
  journal={IEEE Transactions on Biomedical Engineering},
  year={2008},
  volume={55},
  number={8},
  pages={2094-2101},
  doi={10.1109/tbme.2008.919723},
  url={https://ieeexplore.ieee.org/document/4463646}
}
```

---

# Noninvasive Average Flow and Differential Pressure Estimation for an Implantable Rotary Blood Pump Using Dimensional Analysis

Emily Lim, Dean M. Karantonis, Student Member, IEEE, John A. Reizes, Shaun L. Cloherty, Member, IEEE, David G. Mason, and Nigel H. Lovell\*, Senior Member, IEEE

Abstract—Accurate noninvasive average flow and differential pressure estimation of implantable rotary blood pumps (IRBPs) is an important practical element for their physiological control. While most attempts at developing flow and differential pressure estimate models have involved purely empirical techniques, dimensional analysis utilizes theoretical principles of fluid mechanics that provides valuable insights into parameter relationships. Based on data obtained from a steady flow mock loop under a wide range of pump operating points and fluid viscosities, flow and differential pressure estimate models were thus obtained using dimensional analysis. The algorithm was then validated using data from two other VentrAssist IRBPs. Linear correlations between estimated and measured pump flow over a flow range of \(0.5 \pm 0.8 \mathrm{~L} / \mathrm{min}\) resulted in a slope of \(0.98 (R^2 = 0.9848)\) . The average flow error was \(0.20 \pm 0.14 \mathrm{~L} / \mathrm{min}\) (mean \(\pm\) standard deviation) and the average percentage error was \(5.79\%\) . Similarly, linear correlations between estimated and measured pump differential pressure resulted in a slope of \(1.027 (R^2 = 0.997)\) over a pressure range of \(60 \pm 180 \mathrm{~mmHg}\) . The average differential pressure error was \(1.84 \pm 1.54 \mathrm{~mmHg}\) and the average percentage error was \(1.51\%\) .

Index Terms—Dimensional analysis, flow estimation, implantable rotary blood pump (IRBP), left ventricular assist device (LVAD).

## I. INTRODUCTION

HE VentrAssist (Ventracor, Ltd., Sydney, Australia) is a centrifugal implantable rotary blood pump (IRBP) with a hydrodynamic bearing that is used as a left ventricular assist device (LVAD) for long- term implant recipients [1]. Due to the insensitivity of IRBPs to preload, overpumping or underpumping conditions that endanger implant recipients might potentially occur if pump control is not properly implemented. This situation is further complicated by residual ventricular function, dependent on the amount of residual contractility and venous return [2], which causes pump head pressure to vary with each heart beat.

Manuscript received May 25, 2007; revised December 23, 2007. Asterisk indicates corresponding author.

E. Lim, S. L. Cloherty, and D. M. Karantonis are with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, New South Wales 2052, Australia.

\(^* \mathrm{N. H.}\) Lovell is with the Graduate School of Biomedical Engineering, University of New South Wales, Sydney, New South Wales 2052, Australia (e-mail: n.lovell@unsw.edu.au).

J. A. Reizes is with the School of Mechanical and Manufacturing Engineering, University of New South Wales, Sydney, New South Wales 2052, Australia.

D. G. Mason is with the Department of Surgery, Monash University, Victoria 3800, Australia, and also with the Department of Cardiothoracic Surgery, Alfred Hospital, Victoria 3181, Australia.

Digital Object Identifier 10.1109/TBME.2008.919723

Various pump control algorithms have been designed by different research groups. The traditional control strategy, which maintains a constant pump speed, demonstrates a limited degree of adaptability to cardiac demand and clinical conditions of the heart. Giridharan and Skliar [3] proposed that maintaining a constant average pressure difference (75 mmHg) between the left ventricle and the aorta provided sufficient physiological perfusion to the body over a wide range of physical activities and clinical cardiac conditions. On the contrary, Smith et al. [2] suggested that flow is a more physiologically relevant parameter than pump differential pressure since pump differential pressure by itself has no inherent physiological significance. Using a similar approach to Giridharan and Skliar [3], Wu et al. [4] based their algorithms on the control of aortic pressure rather than pump differential pressure. A state- space model of the human circulatory system as well as measurements of pump differential pressure was used to estimate the aortic pressure. The performance of all the aforementioned control algorithms (except speed control) requires accurate measurements of either pump flow or pump differential pressure. However, implantation of flow or pressure sensors in the body result in an attendant risk of thrombus formation, and the reliability of the measurements is affected by measurement drift, and thus, the need for in situ calibration.

Therefore, one design goal of an IRBP is to be able to reliably and accurately estimate pump flow as well as differential pressure without the need for additional implantable sensors. Extensive studies have reported that satisfactory algorithms for sensorless flow and differential pressure estimation through empirical process of pump variables (flow or differential pressure) mapping had been developed [5]–[8]. However, the performance and design characteristics of different pumps cause the proposed algorithms to be substantially different from each other [9]. In addition, to a large extent, the algorithms have failed to adequately model changes in fluid viscosity, and hence, blood hematocrit (HCT).

The present work involved an analysis of data obtained under steady flow conditions for a wide range of pump operating points and fluid viscosities, and employed a nondimensional analytical approach. By reducing the test data on a pump into nondimensional form, it is possible to extrapolate the performance of the pump with revised physical pump characteristics, different pump speeds, and different operating conditions [2]. Compared with purely empirical methods of flow or differential pressure mapping (where curve fitting is applied to the test

variables), the Buckingham \(\pi\) theorem [10], [11], which groups the test variables into fewer independent dimensionless groups, provides a better physical insight into the effects of different parameters on pump performance.

## II. METHODS

### A. Mock Loop Experiments

The mock circulatory loop, consisting of a small reservoir bag \((200\mathrm{mL})\) , the VentrAssist pump, a variable resistance clamp, and two segments of silicone tubing \((1.5\mathrm{m}\) total length, \(3 / 8\) in inner diameter, \(3 / 32\) - in thickness): one connecting the pump outlet to the reservoir and the other connecting the reservoir back to the pump inlet, provided a test environment for steady flow conditions. The pump flow rate, pump differential pressure, impeller speed and electrical input power were recorded at each operating point during the experiment at a sampling rate of \(4\mathrm{kHz}\) . The fluid employed in the experiment was an aqueous glycerol solution at concentrations of \(30\%\) wt (2.323 mPas), \(39\%\) wt (3.394 mPas), and \(45\%\) wt (4.823 mPas). In each case, a resistance clamp mounted on the loop was adjusted so as to vary the circuit resistance. The circuit resistance was defined by adjusting the resistance clamp to achieve a certain flow level, e.g., 1, 3, 5, 7, 9 L/min at a fixed speed, i.e., \(2300\mathrm{r / min}\) . At each resistance level, pump speed was adjusted in increments of \(100\mathrm{r / min}\) within a range of \(1800 - 3000\mathrm{r / min}\) . Once the desired speed had been set and the pump speed controller showed a steady pumping condition, values of pump power, speed, differential pressure, and flow rate averaged over a \(20\mathrm{- s}\) period were recorded. Since the viscosity of aqueous glycerol is highly sensitive to temperature, a thermistor transducer was attached to the loop to measure and control the temperature of the solution. The temperature was maintained at \(25^{\circ}\mathrm{C}\) . Three versions of nominally the same VentrAssist pumps were used to obtain the data, one set for each pump. The dataset from the first pump was used in the derivation of the correlation, while the other two datasets were used as validation. The raw data from pump 1 for an aqueous glycerol solution with a concentration of \(39\%\) wt is shown in Figs. 1 and 2. It can be seen that once the speed and power is known, the flow and differential pressure across the pump can be immediately determined. Unfortunately, if the fluid is changed, the curves are also changed; therefore, a more general approach needs to be provided.

### B. Theoretical Framework  

The objective was to use the viscosity of the aqueous glycerol solution (as a blood analogue at known HCT), pump input power, and impeller speed as indicators of pump flow rate and differential pressure. Ideally, the electromagnetic energy supplied by the external power source is converted into the fluid energy for the pump as well as the inertial energy used to accelerate or decelerate the impeller. However, in a practical situation, various losses occur along the flow passage path in the pump. The energy losses in a general pump include mechanical losses caused by mechanical contact at the shaft sealing section, disk friction losses consumed with friction torque in the gap between the impeller shroud disk and the pump housing wall, fluid leakage losses caused by recirculation of the fluid, and hydraulic losses in the impeller and in the diffuser (such as flow separation) [12].

> **Image description.** A line graph titled "Fig. 1. Graph of differential flow of pump..." (partially visible) that illustrates the relationship between pump flow rate and differential pressure across various impeller speeds.
>
> The graph features two primary axes:
> *   The Y-axis, labeled "Differential pressure (mmHg)," ranges from 0 to 200, with major grid lines marked every 50 units.
> *   The X-axis, labeled "Pump flow (L/min)," ranges from 0 to 9, with major tick marks every 1 unit.
>
> Six distinct data series are plotted, each representing a different impeller speed (RPM), as detailed in the legend located in the upper right corner. The data points are connected by lines, showing a positive correlation between flow and pressure for all speeds.
>
> The data series and their corresponding symbols are:
> *   1800 rpm: Represented by a diamond symbol.
> *   2000 rpm: Represented by an upward-pointing triangle.
> *   2200 rpm: Represented by a plus (+) symbol.
> *   2400 rpm: Represented by a downward-pointing triangle.
> *   2600 rpm: Represented by a dash/hyphen symbol.
> *   3000 rpm: Represented by an 'X' symbol.
>
> Visually, the curves demonstrate that as the pump flow increases from 0 to 9 L/min, the differential pressure increases for every speed. Furthermore, the curves are clearly separated by speed; the 3000 rpm series (X) consistently maintains the highest differential pressure across the entire flow range, while the 1800 rpm series (diamond) consistently maintains the lowest differential pressure. The curves appear relatively flat at low flow rates (0-2 L/min) before showing a steeper upward trajectory as the flow rate increases.

<center>Fig. 1. Graph of differential pressure versus flow for various speeds at a constant viscosity ( \(39\%\) wt aqueous glycerol). </center>

> **Image description.** A line graph titled "Fig. 2. Graph of input power versus flow for various speeds at a constant viscosity (39% wt aqueous glycerol)" illustrates the relationship between electrical input power and pump flow rate across several operating speeds.
>
> The graph features two primary axes:
> *   The Y-axis, labeled "Power (W)," represents the input power and ranges from 0 to 20 Watts, marked in increments of 5.
> *   The X-axis, labeled "Pump flow (L/min)," represents the flow rate and ranges from 0 to 9 Liters per minute, marked in increments of 1.
>
> The data is presented as seven distinct lines, each corresponding to a specific impeller speed (RPM), as detailed in the legend located in the bottom right corner. Each speed is represented by a unique geometric marker:
> *   1800 rpm: Black diamond
> *   2000 rpm: Black square
> *   2200 rpm: Black upward-pointing triangle
> *   2400 rpm: Black 'x'
> *   2600 rpm: Black circle
> *   2800 rpm: Black plus sign (+)
> *   3000 rpm: Black cross/plus sign
>
> The visual pattern across all data series shows a strong positive correlation: as the Pump flow (L/min) increases, the Power (W) required also increases. The lines are generally parallel, indicating that for a given flow rate, increasing the pump speed results in a higher power consumption. The highest speeds (2800 rpm and 3000 rpm) consistently occupy the upper portion of the graph, demonstrating the highest power output for any given flow rate compared to the lower speeds. The lines begin near the origin (0,0) and rise steadily toward the upper right corner of the graph.
>
> The caption at the top of the figure is partially visible and reads: "Fig. 2. Graph of input power versus flow for various speeds at a constant viscosity (39% wt aqueous glycerol)." The legend clearly lists the seven speeds and their corresponding markers.

<center>Fig. 2. Graph of input power versus flow for various speeds at a constant viscosity ( \(39\%\) wt aqueous glycerol). </center>

Due to the complexity in the analysis of the pump characteristics caused by various operating losses and imperfections involved in the design, the theoretical relationship between power, flow, and differential pressure derived for an ideal centrifugal pump is not applicable when studying their practical performance. Thus, the current approach aims to use a systematic nondimensional approach that is applicable to any pump design to derive the relationship between pump power, speed, fluid viscosity, flow, and differential pressure.

The performance of a turbomachine depends on a number of variables, including pump differential pressure \((\Delta p)\) , input power \((P)\) , and efficiency

\[\Delta p = f_{1}(\omega ,Q,\mu ,\rho ,D,l_{1},\ldots ,l_{m},\alpha_{1},\ldots ,\alpha_{n}) \quad (1)\]

\[P = f_{2}(\omega ,Q,\mu ,\rho ,D,l_{1},\ldots ,l_{m},\alpha_{1},\ldots ,\alpha_{n}). \quad (2)\]

As shown in (1) and (2), \(\Delta p\) and \(P\) depend on the speed of the impeller \((\omega)\) , flow rate through the pump \((Q)\) , viscosity \((\mu)\) ,

TABLEI DEFINITION OF THE NONDIMENSIONAL GROUPS THAT ARE SPECIFICALLY APPLICABLE TO PUMPS

| Symbol | Definition |
| :--- | :--- |
| $\psi$ | pressure coefficient |
| $\phi$ | flow coefficient |
| $\Pi$ | power coefficient |
| $Re$ | Reynolds number |

and density \((\rho)\) of the fluid, as well as the geometric parameters of the pump, which include the characteristic dimension of the pump represented by the impeller diameter \((D)\) , lengths \((l)\) , and angles \((\alpha)\) required to fully describe the pump body and rotor. The Buckingham \(\pi\) theorem can be used to reduce the number of variables involved in determining the performance of the pump to a smaller number of nondimensional groupings.

Using dimensional analysis as explained in Appendix A, together with justified assumptions, (1) and (2) can be rewritten as the pump affinity laws

\[\frac{\Delta p}{\rho\omega^2D^2} = F_3\left(\frac{Q}{\omega D^3},\frac{\rho\omega D^2}{\mu}\right) \quad (3)\]

and

\[\frac{P}{\rho\omega^3D^5} = F_4\left(\frac{Q}{\omega D^3},\frac{\rho\omega D^2}{\mu}\right). \quad (4)\]

The nondimensional groups are listed in Table I, which are specifically applicable to the types of pumps discussed in this paper. Table II lists the units and corresponding constants leading to truly nondimensional coefficients.

### C. Data Analysis

1) Flow estimate model: In the first step of the dimensional analysis, a graph of power coefficient versus flow coefficient was plotted for various speeds at a constant viscosity (39%wt aqueous glycerol) (see Fig. 3). Dynamic viscosity of 39%wt aqueous glycerol solution at \(25^{\circ}\mathrm{C}\) , 3.4 mPa, is very close to that of the average viscosity of whole human blood, 3.2 mPa, with hematocrit level of 38% at \(37^{\circ}\mathrm{C}\) [13]. Instead of collapsing onto a single curve, it was observed that the power coefficient values spread was more than \(\pm 25\%\) from the mean for the speeds plotted. This was due to the fact that the coil winding and other friction losses did not follow the same pattern as the power required to move the fluid, and that the Reynolds number changed as the speed was altered. Thus, power coefficients needed to be corrected for varying speed (since viscosity did not vary in the training dataset used).

TABLE II UNITS AND CORRESPONDING CONSTANTS THAT RESULT IN TRULY NONDIMENSIONAL COEFFICIENTS   

<table>SymbolDefinitionUnit/ConstantΔppump differential pressure[mmHg]Qpump flow[L/min]Ppump input power[W]ωpump speed[rpm]μdynamic viscosity[kgm-1s-1]ρfluid density[kgm-3]Dpump impeller diameter[cm]l1,...,lmlengths required to fully describe the pump body and rotor angles required to fully describe the pump body and rotor[cm]α1,...,αndescribe the pump body and rotor pressure constant[rad]cπconstant1.2158 x 10-5constant[(Pa·l·m·m·H·g)cφflow coefficient constant159.161constant[(m3·s-1·L·min-1)cΠpower coefficient constant8.7082 x 10-6constant[(kgm-3·l·g·m-3)cReReynolds number constant0.01constant[(kgm-3·l·g·m-3)ωddesign speed2400 rpm</table>

> **Image description.** A line graph titled "Fig. 3. Graph of power coefficient ($\Pi_{39\%}$) versus flow coefficient ($\Phi_{39\%}$)" displays the relationship between the power coefficient and the flow coefficient for various rotational speeds (RPM).
>
> The graph features a standard Cartesian coordinate system. The horizontal X-axis is labeled "Flow coefficient, $\Phi_{39\%}$" and ranges from 0 to 0.007. The vertical Y-axis is labeled "Power coefficient, $\Pi_{39\%}$" and ranges from 0.0029 to 0.0069.
>
> The data is presented as seven distinct lines, each representing a different rotational speed, as detailed in the legend located in the upper right corner of the plot. The legend maps specific symbols to the following RPM values:
> *   1800 rpm (represented by a diamond symbol)
> *   2000 rpm (represented by a square symbol)
> *   2200 rpm (represented by a triangle symbol)
> *   2400 rpm (represented by an 'X' symbol)
> *   2600 rpm (represented by a circle symbol)
> *   2800 rpm (represented by a plus symbol)
> *   3000 rpm (represented by a cross/plus symbol)
>
> Visually, all lines exhibit a strong positive correlation, meaning that as the Flow coefficient ($\Phi_{39\%}$) increases, the Power coefficient ($\Pi_{39\%}$) also increases for every plotted speed. The curves are generally parallel, with the line corresponding to the highest speed (3000 rpm) consistently showing the highest Power coefficient for any given Flow coefficient, while the line for the lowest speed (1800 rpm) consistently shows the lowest Power coefficient. The lines appear to diverge slightly as the Flow coefficient increases.

<center>Fig. 3. Graph of power coefficient \((\Pi_{39\%})\) versus flow coefficient \((\Phi_{39\%})\) for various speeds at a constant viscosity (39%wt aqueous glycerol). It is observed that the power coefficient values are spread by more than \(\pm 25\%\) from the mean. </center>

As may be observed in Fig. 3, an empirically derived cubic relationship between power coefficients and flow coefficients was obtained at each speed, namely

\[\Pi_{39\%} = \alpha \Phi_{39\%}^3 +b\Phi_{39\%}^2 +c\Phi_{39\%} +d. \quad (5)\]

Since the speed generally causes an offset in the graph, \(a\) , \(b\) , and \(c\) are assumed to be constant, while \(d\) is a function of speed \((\omega)\) . A plot of \(d\) against \(\omega\) indicated that \(d\) is inversely

> **Image description.** A line graph titled "Fig. 4. Ratio of measured power coefficients to estimated power coefficients (m)" displays the relationship between the power coefficient ratio and the flow coefficient for three different concentrations of aqueous glycerol solution.
>
> The graph features two primary axes:
> *   **Y-axis:** Labeled "Ratio of measured power coefficient to estimated power coefficient," denoted by the variable $m$. The scale ranges from 0.0 to 1.4, with major tick marks every 0.2.
> *   **X-axis:** Labeled "Flow coefficient, $\Phi_{39}$." The scale ranges from 0 to 0.07, with major tick marks every 0.01.
>
> Three distinct data series are plotted, representing different viscosities (concentrations of aqueous glycerol, AG):
> 1.  **30% wt AG:** Represented by black squares (■).
> 2.  **39% wt AG:** Represented by black triangles (▲).
> 3.  **45% wt AG:** Represented by black crosses (x).
>
> All three data sets exhibit a generally increasing trend as the flow coefficient ($\Phi_{39}$) increases. The lines are relatively smooth, indicating a consistent functional relationship between the ratio $m$ and the flow coefficient.
>
> Visually, the data points for the three concentrations are distinct, demonstrating that the ratio $m$ does not collapse to a single value of 1.0 across all viscosities. The 30% wt AG data (squares) consistently shows the lowest ratio, while the 45% wt AG data (crosses) consistently shows the highest ratio across the entire range of the flow coefficient. The 39% wt AG data (triangles) falls between the other two.
>
> The overall visual pattern confirms the accompanying text's interpretation: as the viscosity increases (moving from 30% to 45% wt AG), the ratio of measured to estimated power coefficients increases, suggesting that higher power coefficients are required to achieve the same flow coefficients due to the effect of viscosity.

<center>Fig. 4. Ratio of measured power coefficients to estimated power coefficients \((m)\) versus flow coefficient \((\Phi)\) . As viscosity increases, higher power coefficients are needed to produce the same flow coefficients. </center>

proportional to \(\omega^2\) , so that the following relationship was obtained:

\[\begin{array}{rl} & {\Pi_{39\%} = -7148.9\Phi_{39\%}^3 +104.4\Phi_{39\%}^2 +0.057\Phi_{39\%}}\\ & {\qquad +0.0018 + \frac{0.001642}{(\omega_{39\%} / \omega_d)^2}.} \end{array} \quad (6)\]

To study the effect of viscosity, two other sets of training data (obtained using \(30\%\) wt and \(45\%\) wt aqueous glycerol solution) were used. Equation (6) was used to estimate power coefficients for each training data set. The ratio, \(m\) , of measured power coefficients to estimated power coefficients predicted by (6) was calculated from

\[m = \frac{\mathrm{Measured~power}}{\mathrm{Estimated~power}} = \frac{\Pi}{a\Phi^3 + b\Phi^2 + c\Phi + d}. \quad (7)\]

It is evident from Fig. 4 that the ratio did not collapse to the value of 1.0 when viscosity of the solution changed. The data for each viscosity showed a different and approximately constant power coefficient ratio. As viscosity increased, higher power coefficients were required to produce the same flow coefficient due to the effect of viscosity on the Reynolds number.

The relationship between the power coefficient ratio, \(m\) , and viscosity, \(\mu\) , is shown in Fig. 5 and given by

\[m = 0.5067\frac{\mu}{\mu_{39\%}} +0.4918. \quad (8)\]

In order to collapse the set of \(\Pi - \Phi\) curves in Fig. 3 onto a single curve for all viscosities and speeds, the power coefficient was corrected to

\[\Pi ' = \frac{\Pi}{m} -d. \quad (9)\]

Since the aim of this paper is the development of a method of estimating the flow rate from power and speed measurements, flow coefficients, \(\Phi\) , were plotted against corrected power coefficients, \(\Pi '\) , in Fig. 6, together with the line of best fit

\[\Phi = -241.19\Pi '^2 +3.556\Pi ' - 0.0049. \quad (10)\]

> **Image description.** A line graph titled "Fig. 5. Graph of power coefficient ratio (m) versus viscosity ($\mu/\mu_{39\%}$)" that illustrates the relationship between the power coefficient ratio and the relative viscosity of a solution.
>
> The graph features two primary axes:
> 1.  **Y-axis (Vertical):** Labeled "Measured power coefficient: Estimated power coefficient ratio," and represented by the variable $m$. The scale ranges from 0 to 1.4, with major tick marks every 0.2 units.
> 2.  **X-axis (Horizontal):** Labeled "Viscosity/Reference viscosity, $\mu/\mu_{39\%}$." The scale ranges from 0 to 1.6, with major tick marks every 0.2 units.
>
> The data is presented as a series of discrete data points, each marked by a small, filled circle. These points are connected by a solid line, indicating a positive correlation between the two variables. The trend shows that as the relative viscosity ($\mu/\mu_{39\%}$) increases along the X-axis, the power coefficient ratio ($m$) also increases along the Y-axis. The data points begin near the coordinates (0.7, 0.8) and extend to approximately (1.4, 1.2).
>
> The visual pattern suggests a linear or slightly convex relationship, consistent with the provided equation $m = 0.5067\frac{\mu}{\mu_{39\%}} +0.4918$. The graph visually confirms that the power coefficient ratio $m$ increases as the viscosity of the solution increases relative to the reference viscosity ($\mu_{39\%}$).

<center>Fig. 5. Graph of power coefficient ratio \((m)\) versus relative viscosity \((\mu /\mu_{39\%})\) shows a linear relationship between them. </center>

> **Image description.** A technical line graph, labeled Figure 6, illustrating the relationship between the flow coefficient ($\Phi$) and the corrected power coefficient ($\Pi'$). The graph displays a strong, positive, and nearly linear correlation between the two variables.
>
> The graph is structured with two primary axes:
> *   **X-axis (Horizontal):** Labeled "Corrected power coefficient, $\Pi'$". The scale ranges from 0.000 to 0.005, with major tick marks at intervals of 0.001.
> *   **Y-axis (Vertical):** Labeled "Flow coefficient, $\Phi$". The scale ranges from 0.000 to 0.007, with major tick marks at intervals of 0.001.
>
> The visual data consists of a dense cluster of small, dark circular data points. These points follow a clear upward trajectory, indicating that as the corrected power coefficient ($\Pi'$) increases, the flow coefficient ($\Phi$) also increases. A solid, dark line of best fit is drawn through the data points, confirming the stated linear relationship. The line originates near the lower left of the plotted area and slopes steadily upward toward the upper right.
>
> Visible text elements include:
> *   **Partial Caption:** "Fig. 6 Graph of flow coefficient ($\Phi$) versus corrected power coefficient ($\Pi'$)"
> *   **X-axis Label:** "Corrected power coefficient, $\Pi'$"
> *   **Y-axis Label:** "Flow coefficient, $\Phi$"
>
> The overall visual presentation is clean and academic, typical of scientific publications, emphasizing the strong correlation between the corrected power and flow coefficients.

<center>Fig. 6. Graph of flow coefficient \((\Phi)\) versus corrected power coefficient \((\Pi ')\) . Estimates of flow can be obtained from the equations relating the two variables. </center>

2) Differential pressure estimate model: As in Section II-C1, a graph of differential pressure coefficient versus flow coefficient was plotted for various speeds at a constant viscosity \((39\%\) wt aqueous glycerol) (see Fig. 7). It was observed that there was only a small spread of differential pressure coefficient values at the same value of flow coefficient. This indicates that there is negligible effect of the Reynolds number on the pump characteristic \((\Psi - \Phi)\) curve.

To study the effect of viscosity, two other sets of training data (obtained using \(30\%\) wt and \(45\%\) wt aqueous glycerol solution) were used. It is shown in Fig. 8 that the curves for various viscosities collapse onto a curve with only a small spread. A cubic relationship obtained between differential pressure coefficients and flow coefficients

\[\Psi = -170959\Phi^3 +1024\Phi^2 -1.7444\Phi +0.1528 \quad (11)\]

is also shown in Fig. 8.

## III. RESULTS

Flow and differential pressure estimate equations were developed by applying the methodology described before to a training data set. The performance of the estimation models

> **Image description.** A scatter plot titled "Fig. 7. Graph of pressure coefficient ($\Psi_{39\%}$) versus flow coefficient ($\Phi_{39\%}$)" illustrates the relationship between pressure and flow coefficients for various rotational speeds.
>
> The graph features two primary axes:
> *   **Y-axis:** Labeled "Pressure coefficient, $\Psi_{39\%}$," ranging from 0 to 0.18, with major tick marks every 0.02 units.
> *   **X-axis:** Labeled "Flow coefficient, $\Phi_{39\%}$," ranging from 0 to 0.07, with major tick marks every 0.01 units.
>
> The data is presented as a collection of black markers, each representing a specific rotational speed (RPM), as detailed in the legend located in the upper right corner:
> *   1800 RPM (Diamond symbol)
> *   2200 RPM (Triangle symbol)
> *   2400 RPM (Cross symbol)
> *   2600 RPM (Circle symbol)
> *   3000 RPM (Plus symbol)
>
> The visual pattern shows a strong positive correlation: as the flow coefficient ($\Phi_{39\%}$) increases along the X-axis, the pressure coefficient ($\Psi_{39\%}$) also increases along the Y-axis. A key observation is the extremely tight clustering of all data points. The curves corresponding to the different rotational speeds are nearly superimposed, indicating that the pressure coefficient remains highly consistent and shows only a small spread regardless of the rotational speed, provided the viscosity remains constant at 39%.

<center>Fig. 7. Graph of pressure coefficient \((\Psi_{39\%})\) versus flow coefficient \((\Phi_{39\%})\) for various speeds at a constant viscosity \((39\%\) wet aqueous glycerol). It was observed that there is only a small spread of differential pressure coefficient values at the same value of flow coefficient. </center>

> **Image description.** A scatter plot graph titled "Fig. 8" illustrating the relationship between the pressure coefficient ($\Psi$) and the flow coefficient ($\Phi$) for different viscosities of aqueous glycerol.
>
> The graph features two primary axes:
> *   **Y-axis:** Labeled "Pressure coefficient, $\Psi$," ranging from 0 to 0.18, with major tick marks every 0.02.
> *   **X-axis:** Labeled "Flow coefficient, $\Phi$," ranging from 0.000 to 0.007, with major tick marks every 0.001.
>
> A legend in the upper right corner identifies three data series based on viscosity:
> *   30% wt AG (represented by a black square)
> *   39% wt AG (represented by a black triangle)
> *   45% wt AG (represented by a black 'x')
>
> The data points for all three viscosity levels are plotted and show a strong positive correlation, meaning the pressure coefficient ($\Psi$) generally increases as the flow coefficient ($\Phi$) increases. Visually, the data points are extremely tightly clustered together across the entire range of the flow coefficient, suggesting that the variation in pressure coefficient is minimal regardless of the viscosity used.
>
> The figure caption, located below the graph, reads: "Fig. 8. Graph of pressure coefficient ($\Psi$) versus flow coefficient ($\Phi$) for various viscosities (30% wt, 39% wt and 45% wt aqueous glycerol). It was shown that viscosity has a negligible effect on the $\Psi - \Phi$ curves."

<center>Fig. 8. Graph of pressure coefficient \((\Psi)\) versus flow coefficient \((\Phi)\) for various viscosities \((30\%\) wt, \(39\%\) wt and \(45\%\) wt aqueous glycerol). It was shown that viscosity has a negligible effect on the \(\Psi - \Phi\) curves. </center>

was then validated against the remaining pool of data obtained using two other VentrAssist pumps, which cover the same viscosity levels as the training data. Fig. 9 illustrates the estimated flow corresponding to a range of measured flow rates \((0.5 - 8.0 \mathrm{L} / \mathrm{min})\) , while Fig. 10 illustrates the estimated differential pressures corresponding to a range of measured differential pressures \((60 - 180 \mathrm{mmHg})\) . Correlation between measured and estimated flow, as well as between measured and differential pressure was highly significant (flow: \(R^2 = 0.9848\) ; differential pressure: \(R^2 = 0.997\) ), and the slope of the linear regression line was very close to unity (flow: slope \(= 0.98\) ; differential pressure: slope \(= 1.027\) ). The residual error for flow estimation was in the range \(\pm 0.8 \mathrm{L} / \mathrm{min}\) , while for differential pressure lay within the range of \(\pm 8 \mathrm{mmHg}\) . The average flow error was \(0.20 \pm 0.14 \mathrm{L} / \mathrm{min}\) (mean \(\pm\) standard deviation), and the average differential pressure error was \(1.84 \pm 1.54 \mathrm{mmHg}\) .

## IV. DISCUSSION  

Noninvasive estimation of average pump flow and differential pressure has been investigated by many research groups as a means for physiological control of IRBPs. Most research groups have used surface fitting to map flow from the measurable quantities, e.g., power and speed. Bertram [5] reported that the first successful attempt at flow estimation was demonstrated by Wakisaka et al. [14] using pump power, speed, and HCT level. They derived their algorithm from the data obtained in a mock loop setup using whole goat blood, and successfully validated it in a healthy goat with an average error of \(0.5 \mathrm{L} / \mathrm{min}\) over a range of \(2.3 - 8.1 \mathrm{L} / \mathrm{min}\) . As Malagutti et al. [9] indicated, the limitation of their study was that the effects of viscosity were investigated at only a single target speed \((2800 \mathrm{r} / \mathrm{min})\) .

> **Image description.** A scatter plot graph illustrating the relationship between estimated flow and real flow, typical of a scientific validation study. The graph is presented in black and white with a dense cluster of data points forming a strong linear trend.
>
> The axes are clearly labeled:
> *   The horizontal X-axis is labeled "Real Flow (L/min)" and ranges from 0 to 9.
> *   The vertical Y-axis is labeled "Estimated Flow (L/min)" and ranges from 0 to 9.
>
> The data points, represented by small black dots, are tightly clustered around a straight line, indicating a high degree of correlation between the two variables. Overlaid on the graph are two key statistical annotations:
> 1.  A linear regression equation: "Estimated flow = 0.981 * Real flow + 0.176"
> 2.  The coefficient of determination: "R² = 0.9848"
>
> At the bottom of the image, a partial caption is visible, beginning: "Fig. 9. Graph of estimated flow versus real flow corresponding to a range..." The overall visual evidence suggests that the estimation model performs very accurately, as indicated by the high R² value and the slope of the regression line being close to unity (0.981).

<center>Fig. 9. Graph of estimated flow versus real flow corresponding to a range of measured flow rates \((0.5 - 8 \mathrm{L} / \mathrm{min})\) . The performance of the flow estimate equation derived using the training dataset was validated against the testing dataset obtained using two other VentrAssist pumps having similar hydraulic characteristics. </center>

> **Image description.** A technical line graph (scatter plot) illustrating the relationship between estimated and real differential pressure. The graph is titled "Fig. 10. Graph of estimated differential pressure versus real differential pressure."
>
> The visual elements are as follows:
>
> *   **Axes:**
>     *   The horizontal X-axis is labeled "Real pressure (mmHg)" and ranges from 0 to 200.
>     *   The vertical Y-axis is labeled "Estimated pressure (mmHg)" and also ranges from 0 to 200.
> *   **Data:** The graph displays a dense collection of small, dark circular data points. These points are tightly clustered, forming a clear, strong linear trend that slopes upward from the origin.
> *   **Trend Line and Equation:** A solid line of best fit is drawn through the data points. Overlaid on this line is the linear regression equation and the coefficient of determination:
>     *   "Estimated pressure = 1.02 * Real pressure - 2.115"
>     *   "R² = 0.997"
> *   **Text and Labels:**
>     *   The figure caption at the bottom reads: "Fig. 10. Graph of estimated differential pressure versus real differential pressure."
>     *   Partial text visible above the graph includes the word "characteristics."
>
> The visual evidence indicates a highly significant positive correlation between the real and estimated differential pressures, as evidenced by the tight clustering of data points and the high R² value of 0.997. The slope of the regression line (1.02) is very close to unity, suggesting that the estimated pressure closely tracks the real pressure.

<center>Fig. 10. Graph of estimated differential pressure versus real differential pressure corresponding to a range of measured differential pressure \((60 - 180 \mathrm{mmHg})\) . The performance of the differential pressure estimate equation derived using the training dataset was validated against the testing dataset obtained using two other VentrAssist pumps having similar hydraulic characteristics. </center>

On the other hand, Tsukiya et al. [12] included an extra step to estimate viscosity by occluding the pump outlet \((Q = 0)\) for \(< 10 \mathrm{s}\) , based on an inverse linear correlation between the Reynolds number and the speed- normalized current at zero flow. The algorithm achieved a maximum error of \(0.5 \mathrm{L} / \mathrm{min}\) between estimated and measured flow and \(15 \mathrm{mmHg}\) between estimated and measured differential pressure when tested in sheep. The

limitation of their study is the infeasibility of regular pump outlet occlusion in patients.

Tsukiya et al. [15] developed a technique for estimating the instantaneous flow rate in a pump implanted chronically in an animal. The technique took into account reverse flow, inlet cannula obstruction, and suction. They reported a mean flow rate error of \(1\mathrm{L} / \mathrm{min}\) . The main difference between their study and the present investigation is that they used a centrifugal pump rotor supported by a thrust bearing that contains the mechanical contacting surface, while the present study utilizes pumps that are hydraulically supported. Therefore, viscous friction losses have a much more significant influence in the present study as compared with their study, where the mechanical friction losses and the electromagnetic losses were dominant.

Previously, in our laboratory, we developed a steady- flowestimation model based on a VentrAssist pump, taking into account the effect of blood HCT [9]. We reported a residual error of \(0.25 \pm 0.2\mathrm{L} / \mathrm{min}\) . The current approach yields a slightly higher accuracy (with average flow estimation residuals of 0.21 \(\pm 0.15\mathrm{L} / \mathrm{min}\) ). Given the spread of the residuals, this difference is not statistically significant. More significantly, in the present paper, the model is validated against data obtained using two VentrAssist pumps, which are slightly different from each other due to inevitable variations in tolerances incurred in the manufacturing process. The advantage of the current approach is that we can obtain a more fundamental understanding of how different fluid mechanical parameters affect the pump performance, and, if required, ascertain the performance of the pump under modified operating conditions.

It is important to note that the performance of the pressure estimate model derived in the present paper degrades when the flow coefficient increases. This is due to the fact that at a higher speed (or higher Reynolds number), the curves shift to the right, indicating that the pump is able to deliver a higher flow rate at the same differential pressure. In order to collapse the \(\Psi - \Phi\) curves into a single curve, Wong et al. [16] proposed that the differential pressure be plotted against a modified flow coefficient. However, the method does not seem to improve the present pressure estimate model, probably due to the fact that the error in the pressure estimation is not only a function of Reynolds number, but also a function of flow coefficient [17]. As stated by Lorenz and Smith [17], the commonly used definition of the Reynolds number, which uses the impeller speed as the representative velocity, might not hold true at operating points far from the pump's optimal efficiency point. Since the spread of the differential pressure at the same flow coefficient is considered small in our flow range of interest (0.5- 8 L/min), no further effort has been taken to refine the equation by collapsing the curves.  

Several approaches [12], [18] have been proposed to estimate HCT level in the clinical setting, since variation in HCT level may cause differences in flow rates as high as \(2\mathrm{L} / \mathrm{min}\) at the same power and speed. Unfortunately, research to date has not been particularly successful. For example, Kitamura et al. used physical models of the motor, the centrifugal pump, and the Windkessel model of the systemic circulation to solve for viscosity, pump flow, and pressure [18]. The estimated viscos ity converged to the true value in vitro, but failed in vivo. The estimates vary between 8 and \(13\mathrm{cP}\) depending on the driving conditions, while the actual blood viscosity was about \(2.8\mathrm{cP}\) . The uncertainty in the estimation of viscosity in vivo was probably due to the oversimplification of the systemic circulation model. In our present study, it is assumed that in the clinical setting, the HCT level will be ascertained by prior measurement. Future studies shall examine the noninvasive estimation of HCT level in the patients' circulation using the implanted pump as a sensing device.

The present study uses aqueous glycerol solution instead of blood. Since blood is a non- Newtonian fluid, it is expected to complicate the estimate of flow using power. However, at the high shear rates experienced in the VentrAssist IRBP, i.e., \(>1000\mathrm{s}^{- 1}\) , the dynamic viscosity of blood can be considered to be independent of shear rate [7].

It should be noted that the present study focuses on the estimation of flow rate under steady flow conditions. In a pulsatile environment such as the cardiovascular system, the inertia of the fluid, the pump's rotating element, and the time constants of the speed controller need to be taken into account. The electrical input power will not only be used to provide the torque to the pump, but will also be used to accelerate or decelerate the impeller. Thus, a term that takes into account the moment inertia of the impeller has to be added. Furthermore, the time taken by the controller to sense and respond to load changes is important in developing the dynamic pump model. Experimentation on these aspects of instantaneous flow estimation is ongoing in our laboratory. Results from the experiments showed that average flow estimates are applicable to pulsatile flow environments, in the time- averaged sense [19]. This is in good agreement with the excellent results which are obtained in water hammer calculations when power supply is cut to very large pumps.

## V. CONCLUSION

The work herein introduces a systematic approach based on dimensional analysis to estimate average flow rate from average pump input power, average speed, and viscosity. In comparison with empirical model fitting, this approach proves to be more accurate, while also providing valuable insights into relationships between various fluid mechanics parameters that affect the pump flow estimated.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
