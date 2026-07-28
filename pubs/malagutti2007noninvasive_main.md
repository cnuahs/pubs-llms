```
@article{malagutti2007noninvasive,
  title={Noninvasive average flow estimation for an implantable rotary blood pump: a new algorithm incorporating the role of blood viscosity.},
  author={Nicol{\`o} Malagutti and Dean M. Karantonis and Shaun L. Cloherty and Peter J. Ayre and David G. Mason and Robert F. Salamonsen and Nigel H. Lovell},
  journal={Artificial organs},
  year={2007},
  volume={31},
  number={1},
  pages={45-52},
  doi={10.1111/j.1525-1594.2007.00339.x},
  url={https://onlinelibrary.wiley.com/doi/10.1111/j.1525-1594.2007.00339.x}
}
```

---

# Noninvasive Average Flow Estimation for an Implantable Rotary Blood Pump: A New Algorithm Incorporating the Role of Blood Viscosity

\*\*\*Nicolò Malagutti, \*†Dean M. Karantonis, \*Shaun L. Cloherty, §Peter J. Ayre, §David G. Mason, ¶Robert F. Salamonsen, and \*†Nigel H. Lovell

\*Graduate School of Biomedical Engineering and †School of Electrical Engineering and Telecommunications, University of New South Wales (NSW), Sydney; ‡National Information and Communications Technology Australia (NICTA), Eveleigh, NSW; §Ventracor Limited, Chatswood, Sydney, NSW; ¶Alfred Hospital, Prahran, Victoria, Australia; and **Politecnico di Milano, Milan, Italy

Abstract: The effect of blood hematocrit (HCT) on a noninvasive flow estimation algorithm was examined in a centrifugal implantable rotary blood pump (iRBP) used for ventricular assistance. An average flow estimator, based on three parameters, input electrical power, pump speed, and HCT, was developed. Data were collected in a mock loop under steady flow conditions for a variety of pump operating points and for various HCT levels. Analysis was performed using three- dimensional polynomial surfaces to fit the collected data for each different HCT level. The polynomial coefficients of the surfaces were then analyzed as a

function of HCT. Linear correlations between estimated and measured pump flow over a flow range from 1.0 to 7.5 L/min resulted in a slope of \(1.024\mathrm{L} / \mathrm{min}\) ( \(R^2 = 0.9805\) ). Early patient data tested against the estimator have shown promising consistency, suggesting that consideration of HCT can improve the accuracy of existing flow estimation algorithms. Key Words: Implantable rotary blood pump—Noninvasive flow estimation—Control strategy—Left ventricular assist device—Hematocrit—Rotary blood pump.

Implantable rotary blood pumps (iRBPs) are emerging as a possible technological solution for the construction of left ventricular assist devices (LVADs). When compared to their pulsatile counterparts, rotary pumps have the advantage of being lighter, more compact, and more easily implantable devices. Due to the insensitivity of iRBPs to preload, flow control is an essential aspect of their performance as LVADs, as overpumping or underpumping conditions can result in uncomfortable or even dangerous situations for the recipient. Moreover, if long- term ventricular assistance is to be achieved (if the device is to be used as a bridge to heart transplant or, ideally, as a destination therapy), adaptation of the

pump's operating point to the body's metabolic demand is essential to ensure a good quality of life in ambulant patients.

The need for sensorless device operation is a further challenging aspect of iRBP flow estimation, and many researchers have recently increased their efforts in this field. The presence of permanent, invasive flow and/or pressure probes is not desirable in LVADs, as it leads to higher implantation complexity, shortened battery life, and need for periodic recalibration, while also decreasing the general reliability of the device (1). Many research groups claim to have developed satisfactory algorithms for sensorless flow estimation (for a review, see [2]). However, it is evident upon closer inspection of the reported equations that the design characteristics of different pumps cause the proposed algorithms, which have been obtained through an empiric process of pump flow mapping, to be substantially different from each other, and possibly unique to every individual pump design (3- 5). A clear example of the extreme variability of algorithms is also outlined by Ayre et al.

> **Image description.** A schematic diagram illustrating the experimental setup used for flow mapping experiments, featuring a pump immersed in a controlled environment.
>
> The central element is a large, transparent, rectangular container representing a water bath, which is labeled "Water bath maintained at 37°C." Inside this bath, the VentrAssist iRBP pump is positioned.
>
> The pump is connected to external components via a dark gray cable, labeled "VentrAssist iRBP connection to power supply and speed controller." The pump is integrated into a mock loop system designed to simulate circulatory flow. This system includes:
>
> *   **Silicone Bladder:** A small, rounded, dark gray reservoir located on the right side of the setup.
> *   **Silicone Tubing:** A flexible, dark gray loop of tubing that connects the pump to the bladder and forms the main circuit.
> *   **Flow Control and Measurement:** Along the silicone tubing, there are two specific components:
>     *   An "Adjustable clamp to modify outflow resistance," which is positioned on the tubing.
>     *   An "Ultrasonic flow probe," a sensor located near the tubing, used for measuring flow.
>
> The diagram uses clear labels and lines to identify the function and location of each component within the experimental apparatus. The overall arrangement depicts a closed, nonpulsatile loop system designed to test the performance of the VentrAssist iRBP pump under controlled thermal conditions.

<center>FIG. 1. A schematic drawing illustrating the experimental setup used in the flow mapping experiments. The pump under test is inserted into a simple nonpulsatile mock loop comprising a loop of silicone tubing and a silicone reservoir. The entire assembly is immersed in a water bath set at \(37^{\circ}\mathrm{C}\) . </center>

(6), where it is evident that, even when using the same pump, a small change in impeller shape can introduce significant modifications in the relationship between power, speed, and flow.

The VentrAssist (Ventracor Ltd., Sydney, Australia), the focus of this study, is a centrifugal iRBP with a hydrodynamic bearing system, which allows continual operation with virtually no wear and low hemolysis values. This makes the device suitable for long- term ventricular assistance, a function for which it is currently undergoing clinical trials (7). When implanted, the pump inlet cannula is placed directly inside the left ventricle by coring the apex of the heart, while the outlet cannula is anastomosed to the ascending aorta, just above the sinus of Valsalva.

The fluid- dynamic design of the VentrAssist is different from other centrifugal rotary pumps as the device features a particularly flat head- flow (HF) curve (cf. 1,6). This distinctive characteristic would suggest that algorithms developed for other devices would not be applicable to the VentrAssist iRBP, thus advocating the need for a specific analysis. Coherent with the most recent flow estimation study carried out on the VentrAssist (5), which has returned very promising results, the present study focused on identifying a polynomial relationship between flow and the signals of pump speed and electrical input power in order to obtain an accurate, noninvasive estimate of average output flow rate. While Ayre et al. (5) have addressed the problem of estimating average flow, no systematic attempt has been made to date on the VentrAssist pump to incorporate the effect of blood viscosity variation into the estimator equations. The present work analyzed data obtained in a mock loop for a wide range of different pump operating points and blood hematocrit (HCT) values, so as to delineate a comprehensive, four- dimensional (4D) relationship between HCT, pump power, pump speed, and output flow rate. The resulting algorithm was then tested against a validation data set as well as data from patient trials, to verify that the accuracy of the model lay within a clinically acceptable range.

## MATERIALS AND METHODS

## Data collection

A mock loop for steady flow conditions was prepared as shown in Fig. 1. The experimental setup consisted of a silicone tubing loop (approximately \(1.5\mathrm{m}\) in length) connected to a silicone bladder reservoir and to the iRBP. The circuit was submerged, for the whole duration of the experiment, in a water bath maintained at \(37^{\circ}\mathrm{C}\) with a Thermoline (Thermoline Scientific, Smithfield, Australia) bath heater.

The loop was filled with human red blood cells resuspended in a plasma volume expander (Gelofusine, B. Braun Australia Pty Ltd., Bella Vista, Australia), and air bubbles were carefully removed. Pump speed was then set at a constant value. The loop resistance was then adjusted by way of an occluding clamp so as to obtain the desired flow through the loop. Once steady state was reached, readings for pump speed, power, and flow were recorded. Flow was measured with a Transonics (Transonics Systems, Inc., Ithaca, NY, USA) flow probe, calibrated for blood. Additional readings were also recorded for pressure values at the pump inlet and outlet. Such values are not relevant for the scope of this article, and therefore will not be discussed here.

The experiment was performed six times to create a training data set. HCT levels for the training data were \(24.0, 27.0, 34.0, 39.0, 41.0,\) and \(47.5\%\) (HCT was determined by averaging the readings obtained by centrifuging four to six blood samples collected at the beginning of each experiment). In each case, pump speed was initially set at \(3000\mathrm{rpm}\) , and was then decreased in steps of \(100\mathrm{rpm}\) to a minimum speed of \(1800\mathrm{rpm}\) . At each speed set point, the clamp was adjusted to obtain flow values between \(0.0\mathrm{L} / \mathrm{min}\) and the maximum achievable flow rate, at intervals of approximately \(0.5\mathrm{L} / \mathrm{min}\) . Maximum flow rates ranged between \(9.0\) and \(5.5\mathrm{L} / \mathrm{min}\) depending on pump speed. Once the desired flow rate was set and the pump speed controller showed a steady pumping

> **Image description.** A three-dimensional (3D) surface plot illustrating the relationship between flow rate, pump speed, and pump power, representing a fitted model of experimental data.
>
> The graph is a volumetric visualization with three distinct axes:
>
> *   **Vertical Axis (Z-axis):** Labeled "Flow rate (L/min)," this axis ranges from 0 to 9, representing the dependent variable (estimated flow rate).
> *   **Horizontal Axis (Y-axis):** Labeled "Pump speed (rev/min)," this axis runs along the front-to-back dimension and ranges from 0 to 3000, representing the pump rotational speed.
> *   **Horizontal Axis (X-axis):** Labeled "Pump power (mW)," this axis runs along the left-to-right dimension and ranges from 0 to 12500, representing the input electrical power.
>
> The visual content consists of two primary elements:
>
> 1.  **Fitted Surface:** A continuous, smooth, undulating surface rendered in shades of gray. This surface represents the mathematical model (a polynomial fit) used to estimate the flow rate based on the input speed and power. The surface shows a complex, non-linear relationship, generally rising as both pump speed and pump power increase.
> 2.  **Experimental Data Points:** Numerous discrete black dots are scattered across the 3D space, lying directly on or very near the fitted surface. These points represent the actual experimental measurements taken during the study.
>
> The overall visual pattern demonstrates a high degree of correlation, as the fitted surface closely follows the distribution of the scattered data points, indicating a strong predictive model for the flow rate across the tested range of pump speeds and powers. The caption visible at the top of the image identifies this figure as "FIG. 2. An example of the 3D surface fitting..."

<center>FIG. 2. An example of the 3D surface fitting (for an HCT of \(47.5\%\) ) of estimated flow rate for various pump speeds and pump powers. The surface is given by Eq. 1, with \(a = 9.703\) , \(b = 4.331\) , \(c = 0.294 \times 10^{-5}\) , \(d = 8.501 \times 10^{-3}\) , \(e = -0.0111\) and \(f = 6.283 \times 10^{-7}\) . The \(R^2\) value is 0.9916. The experimental data points are shown along with the fitted surface. </center>

condition, values for power, speed, and flow were recorded. Each experiment lasted approximately \(5\mathrm{h}\) with HCT readings taken upon completion of the experiment to verify that no changes had occurred throughout the procedure.

The experiment was repeated at a later date using the same procedure to create a validation data set. HCT values in this set were \(20.5, 27.0, 32.5, 36.5, 41.0\) , and \(47.0\%\) .

## Data analysis

Using a three- dimensional (3D) interpolation tool (TableCurve 3D, Systat Software Inc., Richmond, CA, USA), numerous polynomial surfaces were fitted to the experimental data to identify a general equation able to produce a satisfactory fit to all six data sets. Polynomial surfaces were chosen not only to keep consistency with the model by Ayre et al. (5), but also due to their computational simplicity and their advantageous mathematical properties of continuity and differentiability (a potentially useful attribute for future applications). The chosen surface was of the type illustrated in Fig. 2, corresponding to the polynomial form

\[Q = a + b(VI) + c(VI)^2 +d(VI)^3 +e\omega +f\omega^2 \quad (1)\]

where \(Q\) denotes estimated flow rate (L/min); \(\omega\) denotes pump rotational speed (rpm), and \(VI\) represents input electrical power (W).

The equation was then fitted to the flow data for each HCT value in the training data set. The six values obtained for each of the six parameters \((a, b, c, d, e, \text{and} f)\) were then plotted against HCT, in order to identify a way to incorporate HCT in a comprehensive relationship.

## Estimator validation

The new algorithm for average flow estimation was then tested on the validation data. Over a wide range of flow rates (between 1.0 and \(7.5\mathrm{L} / \mathrm{min}\) ), measured and estimated flow were plotted against each other to evaluate the accuracy of the estimation algorithm. Results were deemed acceptable if either the difference (residual) between measured and estimated flow was less than \(0.5\mathrm{L} / \mathrm{min}\) or percentage error was below \(10\%\) . The variability of residuals and percentage error was also analyzed over the range of HCT values to verify that the accuracy of flow estimates was independent of blood viscosity.

A small data set of de- identified, clinical flow data from a number of patients currently trialing the VentrAssist pump was also used for algorithm validation. These data included average pump speed and input electrical power as reported by the pump controller, as well as a measure of systemic blood flow obtained with a Swan- Ganz catheter. Thirteen different operating points from two different patients were available. Medical imaging confirmed that the patients' aortic valve remained continuously closed throughout the cardiac cycle during such measurements, thus ensuring the equivalence between measured systemic flow and pump flow.

## RESULTS

## Data collection

The experiment produced a training and a validation data set. Each of these contained six subsets corresponding to six different HCT values. Each subset was made up of approximately 190 different pump operating points. The HCT readings taken after each experiment showed that no changes had occurred throughout the procedure.

## Investigating a 4D relationship

The chosen polynomial surface template fitted the collected data well, with an average \(R^2\) value of 0.987. It represented a good compromise between polynomial order and goodness of fit, as shown in Table 1, with lower- order equations yielding lower \(R^2\) values and higher orders achieving only marginal improvements to the overall fit. A residual analysis of the plots is shown in Fig. 3. Residuals are defined as the

TABLE 1. Equations illustrating the goodness of fit of different polynomial surfaces

| Equation used for surface fitting | Average R² value (over the six data sets) |
| :--- | :--- |
| z = a + bx + cy | 0.955 |
| z = a + bx + cx² + dy | 0.968 |
| z = a + bx + cx² + dx³ + ey | 0.980 |
| z = a + bx + cx² + dx³ + ey + fy² | 0.987 |
| z = a + bx + cx² + dx³ + ex⁴ + fy + gy² | 0.988 |
| z = a + bx + cx² + dx³ + ex⁴ + fy + gy² + hy³ + iy⁴ + fy⁵ | 0.989 |

Variable \(\mathbf{x}\) refers to pump power; variable y to pump speed; variable z to estimated pump flow; and parameters a-j are constant coefficients.

difference between the measured value and the corresponding point on the fitted surface (i.e., estimated flow), and their plot is useful to visually identify areas of poor fit. The figure shows that the points deviating most significantly from the fitted surface are mostly located at very low (less than \(1.0\mathrm{L / min}\) ) flows. A few discrepancies are also located at very high flows (above \(7.0\mathrm{L / min}\) ). An analysis of residuals thus confirms the applicability of this type of surface fitting in a physiological range of flow rates.

Figure 4 shows the plots of the six fitted coefficients \(a,b,c,d,e,\) and \(f\) as a function of HCT. The three power coefficients \((b,c,\) and \(d\) in Eq.1) exhibited a linear relationship with HCT:

\[b = 5.82 - HCT\cdot 3.25\cdot 10^{-2} \quad (2)\]

\[c = -5.07\cdot 10^{-1} + HCT\cdot 4.67\cdot 10^{-3} \quad (3)\]

\[d = 1.87\cdot 10^{-2} - HCT\cdot 2.22\cdot 10^{-4} \quad (4)\]

However, no significant relationship could be identified between HCT and the speed coefficients \(e\) and \(f\) or the offset coefficient \(a\)

> **Image description.** A three-dimensional scatter plot, specifically a residual plot, illustrating the relationship between experimental data and a fitted surface for a pump system. The plot is rendered in a perspective view, showing the deviation of data points from a modeled surface.
>
> The plot is defined by three orthogonal axes:
> 1.  **Vertical Axis (Z-axis):** Labeled "Flow rate (L/min)," ranging from -0.75 to 0.75.
> 2.  **Horizontal Axis (X-axis):** Labeled "Pump speed (rev/min)," ranging from 1500 to 3000.
> 3.  **Depth Axis (Y-axis):** Labeled "Pump power (mW)," ranging from 0 to 12500.
>
> The data is represented by numerous small, dark circular points scattered throughout the volume defined by the axes. A faint, light-colored surface is visible, representing the fitted model. The points represent the residuals—the difference between the measured flow rate and the flow rate predicted by the fitted surface.
>
> The data points are densely clustered, particularly in the central region of the plot, indicating a strong correlation between the variables. The distribution of the points around the fitted surface suggests that the model provides a good fit across the measured range of pump speed and power.
>
> Below the plot, the figure is captioned: "FIG. 3. Plot of the residuals for the fitted surface and experimental data shown in Fig. 2 (HCT value of 47.5%)." The overall visual presentation is typical of technical data analysis used to validate the accuracy of a mathematical model against experimental measurements.

<center>FIG. 3. Plot of the residuals for the fitted surface and experimental data shown in Fig. 2 (HCT value of \(47.5\%\) ). </center>

Linear Eqs. 2- 4 were incorporated in general Eq. 1. The fitted values for parameters \(a,e,\) and \(f\) were averaged, and the results were also included in Eq. 1. The final equation was (numbers have been approximated to three significant figures to aid visualization)

\[\begin{array}{rl} & Q = 9.06 - 0.0105\cdot \omega +4.50\cdot 10^{-7}\omega^2 +(5.82 - \\ & \qquad HCT\cdot 3.25\cdot 10^{-2})\cdot (VI) + -(5.07\cdot 10^{-1} - \\ & \qquad HCT\cdot 4.67\cdot 10^{-3})\cdot (VI)^2 +(1.87\cdot 10^{-2} - HCT\cdot 2.22\cdot \\ & \qquad 10^{-4})\cdot (VI)^3 \end{array} \quad (5)\]

## Validation

Figure 5a illustrates the linear correlation analysis between estimated flow given by Eq. 5 and measured flow rates in all collected points. Correlation between measured and estimated flow was highly significant, with \(R^2 = 0.9785\) . Only a small offset \((- 0.0874\mathrm{L / min})\) was present, and the slope of the linear regression line was very close to unity (1.024). A graph of residuals plotted against measured flow rate (Fig. 5b) shows that the flow estimation error lies within the required \(0.5\mathrm{L / min}\) or \(10\%\) range. The average value for residuals of flow estimation was \(0.25\pm 0.21\mathrm{L / min}\) (mean \(\pm \mathrm{SD}\) \(n = 1038\) ), and the average percentage error was \(7.2\pm 3.5\%\) (mean \(\pm \mathrm{SD}\) \(n = 1038\) ).

The errors in estimated flow for each HCT value in the validation data set are reported in Table 2. Results from validation on patient data are summarized in Table 3. For this data set, the average flow residual was \(0.20\pm 0.18\mathrm{L / min}\) (mean \(\pm \mathrm{SD}\) \(n = 12\) ), and average percentage error was \(4.3\pm 3.6\%\) (mean \(\pm \mathrm{SD}\) \(n = 12\) ).

## DISCUSSION

Noninvasive estimation of average pump flow, because of its clear clinical relevance, has been intensely investigated over the past decade. As Bertram (2) reports, the study by Wakisaka et al. (8) represented the first successful attempt at estimation. Using a NCVC- 2 (National Cardiovascular Center,

> **Image description.** A technical figure consisting of six line graphs arranged in a 2x3 grid, illustrating the relationship between various coefficient values (a, b, c, d, e, and f) and Hematocrit (HCT). All six plots share a common x-axis labeled "hematocrit," ranging from approximately 20% to 50%.
>
> The plots are organized into two columns: the left column displays coefficients a, e, and f, while the right column displays coefficients b, c, and d.
>
> **Left Column (Coefficients a, e, and f):**
> These three plots show data points that are scattered without a clear linear trend, suggesting no significant relationship between these coefficients and HCT.
> 1.  **Top Left (Coefficient 'a'):** The y-axis is labeled "a value" and ranges from 8.0 to 9.8. The data points are widely dispersed.
> 2.  **Middle Left (Coefficient 'e'):** The y-axis is labeled "e value (x 10^-2)" and ranges from -1.12 to -0.96. The data points are scattered.
> 3.  **Bottom Left (Coefficient 'f'):** The y-axis is labeled "f value (x 10^-7)" and ranges from 2.5 to 6.5. The data points are scattered.
>
> **Right Column (Coefficients b, c, and d):**
> These three plots show clear linear relationships between the coefficient values and HCT, each featuring a fitted regression line and an $R^2$ value.
> 1.  **Top Right (Coefficient 'b'):** The y-axis is labeled "b value" and ranges from 4.1 to 5.1. The data points follow a distinct downward sloping linear trend. The fitted line is accompanied by the text: "b = 5.82 - 3.25E-02 (HCT)" and "$R^2 = 0.976$".
> 2.  **Middle Right (Coefficient 'c'):** The y-axis is labeled "c value (x 10^-1)" and ranges from -3.7 to -2.5. The data points follow a distinct upward sloping linear trend. The fitted line is accompanied by the text: "c = -5.07E-01 + 4.67E-03 (HCT)" and "$R^2 = 0.976$".
> 3.  **Bottom Right (Coefficient 'd'):** The y-axis is labeled "d value (x 10^-2)" and ranges from 0.8 to 1.4. The data points follow a distinct downward sloping linear trend. The fitted line is accompanied by the text: "d = 1.87E-02 - 2.22E-04 (HCT)" and "$R^2 = 0.975$".

<center>FIG. 4. Plots of coefficient values (a, b, c, d, e, and f) versus HCT. Plots on the left-hand side from top to bottom are for coefficients a, e, and f. No significant relationship was found between these parameters and HCT. On the right-hand side from top to bottom are coefficients b, c, and d. A linear relationship can be seen between these parameters and HCT. </center>

Shiga, Japan) centrifugal pump, they analyzed flow maps obtained in a steady- state mock loop using whole goat blood for a range of HCT values (21.5- 42.0%) and identified the relationship \(Q = k_{1}x\) \(VI / \omega^{2} - k_{2}xHCT - k_{3}\) . Estimated output flow \((Q)\) was considered linearly proportional to a term called "normalized power" \((VI / \omega^{2})\) , while HCT introduced a variable offset. The method was reported as successful with an average \(R^{2}\) value between real and estimated flow of 0.988. However, residuals were still significant with a reported average of \(\pm 0.6 \mathrm{L} / \mathrm{min}\) . A noticeable drawback of this study is also that the effects of blood viscosity were investigated at only a

single target speed (2800 rpm). Due to the similarity in experimental procedures, the algorithm by Wakisaka et al. (8) was tested on the flow maps collected using the VentrAssist; however, results were unsatisfactory, as the constant offset term accounting for HCT failed to describe the difference in flow rates between flow maps.

Yoshizawa et al. (4), analyzing data collected in a mock loop using water and a \(37\%\) aqueous glycerol solution, proposed a new algorithm for a Kyocera C1E3 pump (Kyocera Corporation, Kyoto, Japan). Their model was summarized by the equation \(Q = K \cdot (b_{1} \omega^{2} \cdot VI + b_{2} \omega \cdot VI + b_{3} \cdot VI + b_{4} \cdot \omega^{2} + b_{5} \cdot \omega + b_{6})\) ,

> **Image description.** A technical figure consisting of two panels, (a) and (b), which are scatter plots used to analyze the relationship between estimated and measured pump flow.
>
> Panel (a) is a linear correlation plot titled (a). It displays the relationship between "Estimated flow (L/min)" on the vertical y-axis and "Measured flow (L/min)" on the horizontal x-axis. The y-axis ranges from 0 to 10 L/min, and the x-axis ranges from 0 to 8 L/min. A series of black data points are plotted, and a solid black line is fitted through these points, indicating a strong positive linear correlation. The plot includes the following statistical information displayed in the upper right corner:
> *   $y = 1.024x - 0.074$
> *   $R^2 = 0.9785$
>
> Panel (b) is a residual plot titled (b). It plots the "Residual (L/min)" on the vertical y-axis against "Measured flow (L/min)" on the horizontal x-axis. The y-axis ranges from -2 to 2 L/min, and the x-axis ranges from 0 to 8 L/min. The data points are scattered around the zero line, illustrating the magnitude of the error (residual) for each corresponding measured flow value. The scatter appears relatively consistent across the entire range of measured flow. Both panels utilize a white background with black axes, labels, and data points.

<center>FIG. 5. (a) Linear correlation plot between estimated and measured pump flow for the complete validation data set (six HCTs). (b) Plot of the residuals (difference between estimated and measured flow) against measured flow. The error bars indicate the SD at every half liter per minute interval. While calculating the SD, points whose actual flow did not fall exactly on a multiple of 0.5 L/min (several were present, especially at high flows) were assimilated to the closest 0.5-L/min interval. </center>

TABLE 2. Average residual value and average percentage error in estimated flow for each HCT value in the validation data set

| HCT of validation set (%) | Average residual (L/min) | Average (%) error |
| :--- | :--- | :--- |
| 47 | 0.20 ± 0.15 | 5.5 |
| 41 | 0.27 ± 0.21 | 9.4 |
| 37 | 0.28 ± 0.21 | 9.3 |
| 33 | 0.26 ± 0.21 | 6.1 |
| 27 | 0.24 ± 0.17 | 6.0 |
| 21 | 0.26 ± 0.25 | 6.3 |

where \(K\) , calculated through an autoregressive exogenous (ARX) model, represented a gain factor used to account for the effects of varying blood viscosity. They reported a much lower degree of accuracy than that of Wakisaka and colleagues (8), with an \(R^2\) value of 0.850 and an estimation error of \(1.66\mathrm{L / min}\) . However, it appears that these figures relate to the general outcome of their flow estimation experiments and not strictly to average flow estimation. It is therefore difficult to compare them to the results of the present study.

Both the previously described models were obtained through empiric flow mapping and featured sensibly different equations. An intrinsically different approach was employed by Kitamura et al. (9), where an attempt was made to identify a physical model of the interaction between the cardiovascular system and a Capiox (Terumo Corp., Tokyo, Japan) rotary pump. Successful results were reported for in vitro measurements using aqueous glycerol, with an \(R^2\) value of 0.994. Despite the interesting nature of the approach, the reported results only illustrate accuracy on flow rates up to \(2\mathrm{L / min}\) , whereas flow rates of up to \(7\mathrm{L / min}\) may be expected in a human adult. Early in vivo testing also

proved disappointing, as the necessarily simplified, windkessel- like nature of the model lacked robustness during animal trials.

The studies that provided most guidance for this article were the previous experiments carried out on the VentrAssist by Ayre et al. (5,6). Working on data from static and pulsatile mock loops containing ovine blood or aqueous glycerol solutions, as well as chronic and acute sheep experiments, Ayre and coworkers (5,6) proposed a flow estimate given by \(Q = a_0 - k_1\cdot \omega + k_2\cdot VI - k_3\cdot (VI)^2 + k_4\cdot (VI)^3\) , which performed well, with high \(R^2\) values both in vitro and in vivo. However, this flow estimate made no attempt to compensate for variations in blood viscosity.

Ayre et al. (5) expressed concern regarding the "robustness of the flow estimation algorithms in case of more widely varying HCT." This concern was well founded, as demonstrated by the flow mapping data presented in this study. This article demonstrates that HCT plays a fundamental role in the relationship between power, speed, and output flow in the VentrAssist iRBP. For example, the flow maps contained in the validation data set indicate that at a speed of \(2600\mathrm{rpm}\) and an input power of \(8\mathrm{W}\) , output flow rate increases from \(5\mathrm{L / min}\) at \(47.5\%\) HCT to \(6.5\mathrm{L / min}\) at \(24\%\) HCT. Therefore, in order to obtain an accurate estimation of average flow, it is clearly important to take into account the effects of blood viscosity.

Strictly speaking, HCT and blood viscosity are not totally equivalent concepts. As Wakisaka et al. (8) note, the rheological properties of blood as a shear thinning fluid are such that its viscosity is not purely dependent on HCT, but it also varies according to shear rate, temperature, plasma viscosity, and fibrinogen content. However, in the clinical setting, except for cases of anomalous fibrinogen concentration, such as during thrombus formation (10), most

TABLE 3. Preliminary validation of flow estimation algorithm at different pump speeds in two implanted patients

| Speed (rpm) | Power (W) | Swan CO (L/min) | HCT (%) | Estimated flow (L/min) | Residual (L/min) | % Error |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1800 | 3.186 | 3.9 | 27 | 3.82 | 0.08 | 2.1 |
| 1900 | 3.617 | 3.8 | 27 | 4.14 | 0.34 | 9.0 |
| 2000 | 4.044 | 4.5 | 27 | 4.36 | 0.14 | 3.1 |
| 2100 | 4.505 | 4.7 | 27 | 4.60 | 0.10 | 2.1 |
| 2200 | 4.986 | 4.8 | 27 | 4.79 | 0.01 | 0.2 |
| 2300 | 5.559 | 5.2 | 27 | 5.08 | 0.12 | 2.3 |
| 2400 | 6.173 | 5.0 | 27 | 5.34 | 0.34 | 8.4 |
| 2500 | 6.816 | 5.1 | 27 | 5.53 | 0.43 | 1.6 |
| 2600 | 7.438 | 5.7 | 27 | 5.66 | 0.09 | 11.0 |
| 2700 | 8.094 | 5.1 | 27 | 5.68 | 0.28 | 5.2 |
| 2750 | 8.434 | 5.4 | 27 | 5.68 | 0.01 | 0.2 |
| 2050 | 4.081 | 4.3 | 23 | 4.31 | 0.01 | 4.3 |
| Average | | | | | | |
| | | | | 0.20 | | 4.3 |

of the mentioned parameters are considered reasonably stable, and HCT and shear rate are the two factors that mainly determine viscosity. Also, at the high shear rates experienced in the VentrAssist iRPB \(>1000 / s\) , the behavior of blood can be considered as almost Newtonian (5), indicating that dynamic viscosity may be regarded as independent of shear rate. This explains the interchangeable use of the terms "HCT" and "blood viscosity" within this article.

As previously described, a significant relationship between blood HCT and the coefficients for power \((b, c, \text{and} d)\) was identified. This was expected, as higher HCT values correspond to more viscous blood, and the necessary power to run any pump intuitively rises as the viscosity of the pumped fluid increases. In contrast, the coefficients of speed \((e \text{and} f)\) and the offset term \((a)\) indicated no apparent dependence on HCT. In order to establish a general equation including blood viscosity as a parameter, their values were deemed to be sufficiently uncorrelated with HCT that their average could be used in forming the general equation.

The identified polynomial relationship is ultimately similar to the one outlined by Ayre et al. (5), though a better surface fit was achieved in the present study by including a quadratic term for speed, which had not been previously reported. It is interesting to compare the form of the final equation with the findings of other empiric studies: unlike previous estimators, Eq. 5 does not feature HCT as an external gain factor (as in Yoshizawa et al. [4]) or as an additional linear term (as in Wakisaka et al. [8]). Blood viscosity was instead selectively incorporated in some of the parametric coefficients, specifically, those related to input electrical power. A key role was also attributed to the terms for \((VI)^2\) and \((VI)^3\) , whereas both Yoshizawa et al. (4) and Wakisaka et al. (8) had assumed a linear relationship between output flow rate and input electrical power. Figure 6 demonstrates that such a linear relationship is not applicable to the VentrAssist iRPB and that a cubic curve provides a much more accurate interpolation, especially at low and high flow rates. These significant differences highlight once again the fact that considerably different flow estimation equations may apply to different pump designs.

Estimated flow rates for the mock loop experiments generally fell within the acceptable \(0.5 \text{L} /\text{min}\) or \(10\%\) error range, validating our model for use under these circumstances. Consistent values for the residuals over a wide range of HCT values (see Table 2) confirm that the accuracy of the estimate is independent of blood viscosity. The highest discrep

> **Image description.** A line graph, labeled FIG. 6, illustrating the relationship between pump power and pump flow. The graph features a positive, non-linear correlation between the two variables.
>
> The axes are clearly defined:
> *   The vertical Y-axis is labeled "Pump flow (L/min)" and ranges from 0 to 8, with major tick marks at intervals of 1.
> *   The horizontal X-axis is labeled "Pump power (W)" and ranges from 3.0 to 8.0, with major tick marks at intervals of 1.0.
>
> The data is represented by a series of black circular data points scattered across the plot. These points are connected by a dashed black line, which represents the trend. The trend shows that as the "Pump power (W)" increases, the "Pump flow (L/min)" also increases. The curve is concave up, indicating that the rate of increase in pump flow accelerates as the pump power increases.
>
> The caption visible at the bottom of the image reads: "FIG. 6 A plot of power versus measured flow has been pre..." The overall visual presentation is typical of technical data analysis, demonstrating an empirical relationship between electrical input power and fluid output flow rate for a pump.

<center>FIG. 6. A plot of power versus measured flow has been produced; pump was operating at \(2500 \text{rpm}\) . HCT was \(27\%\) . A straight line \((R^2 = 0.979)\) and a cubic polynomial \((R^2 = 0.995)\) have been superimposed to highlight the nonlinear nature of the relationship between pump power and actual pump flow in the VentrAssist iRPB. The equation for the straight line was \(Q = 1.8(VI) - 6.61\) , whereas the equation for the cubic was \(Q = 2 \times 10^{-1}(VI)^3 - 4(VI)^2 + 20.7(VI) - 47.177\) . </center>

ancies, as shown in Fig. 5b, were observed at very high flow rates (above \(7.5 \text{L} /\text{min}\) ). Such average flow rates would not be expected during pump operation under physiological conditions.

Accuracy at low flows was also affected by a higher percentage error in the flow probe reading, while at high flows, eddy currents/turbulence or the presence of small, undetected air bubbles in the mock loop may have led to some incorrect flow rate measurements. At a number of operating points at high flows, in fact, an increase in output flow was recorded without a corresponding increase in input power. An even higher overall accuracy of the estimator is therefore likely to be achieved through multiple, averaged repetitions of the data acquisition process, so as to obtain larger and more accurate training and validation data sets.

The achieved correlation value of 0.981 does not represent an improvement from the accuracy previously reported by Ayre et al. (5), who reported an average value of 0.991 in relation to estimation of steady mock loop flow rates. However, the results from the new estimator fall within a clinically acceptable error range while covering a wide range of HCTs, whereas the model by Ayre et al. (5) was restricted to a constant, \(30\%\) ovine blood HCT value. This is an important advancement, given that patients

may experience HCT levels ranging between 20 and \(50\%\) (7). The value can also undergo substantial variations, especially during the early postoperative recovery period.

Preliminary validation of the flow estimator proposed here using clinical patient data also yielded very promising results. However, these should be considered very carefully, given the limited number of available case studies and that Swan- Ganz catheter flow measurements are well known for their limited accuracy (11). Also, they provide no information to assess the applicability of the model to situations where pump flow simply aids cardiac ejection, instead of completely substituting it, that is, in cases where pump speed and input power are modulated by the pulsatile action of the heart. Nevertheless, in all examined points but one, the results from the estimator matched or surpassed the accuracy of previous algorithms designed for the VentrAssist (5).

By identifying HCT as key parameter for flow estimation, the present work proposes an effective way to overcome estimation errors introduced by changes in blood viscosity. However, it also introduces a complementary issue, that is, the need to noninvasively and accurately determine a patient's HCT value. As mentioned, HCT is physiologically subject to variations, and while it is quite easy to monitor its value from blood samples taken directly from a mock loop or a hospitalized patient, such a procedure would be extremely impractical in discharged patients and would undermine the ultimate goal of long- term independence and quality of life for these individuals. Future work will necessarily involve the development of an effective blood viscosity estimation algorithm.

## CONCLUSIONS  

The work herein introduces a new, comprehensive relationship between blood HCT and average pump power, speed, and output flow rate. If implemented, this could lead to a simpler, more flexible pump speed control system for the VentrAssist iRPB. It is anticipated that further clinical data, as well as acute experiments in animals with models of cardiac failure, will confirm the early positive outcomes presented herein. The flow estimator described here may also represent an important starting point for the development of an algorithm for noninvasive instantaneous flow estimation, through, for example, an ARX model (4,12). Such an estimate of instantaneous flow is an essential tool for clinicians to gain further insight into the interactions between the body and the pump, and is a necessary development on the way to designing a totally implantable, long- term artificial heart.

Acknowledgement: This work was funded by an Australian Research Council Linkages Grant.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
