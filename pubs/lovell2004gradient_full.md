```
@article{lovell2004gradient,
  title={A gradient model of cardiac pacemaker myocytes.},
  author={Nigel Hamilton Lovell and Shaun Liam Cloherty and Branko G. Celler and Socrates Dokos},
  journal={Progress in biophysics and molecular biology},
  year={2004},
  volume={85},
  number={2-3},
  pages={301-323},
  doi={10.1016/j.pbiomolbio.2003.12.001},
  url={https://www.sciencedirect.com/science/article/pii/S0079610703001123}
}
```

---

# A gradient model of cardiac pacemaker myocytes

Nigel H. Lovell \(^{a}\) , Shaun L. Cloherty \(^{a}\) , Branko G. Celler \(^{b}\) , Socrates Dokos \(^{a,\ast}\)

\(^{a}\) Graduate School of Biomedical Engineering, University of New South Wales, Sydney, 2052, NSW, Australia \(^{b}\) School of Electrical Engineering and Telecommunications, University of New South Wales, Sydney, 2052, NSW, Australia

## Abstract

We have formulated a spatial- gradient model of action potential heterogeneity within the rabbit sinoatrial node (SAN), based on cell- specific ionic models of electrical activity from its central and peripheral regions. The ionic models are derived from a generic cell model, incorporating five background and exchange currents, and seven time- dependent currents based on three- or four- state Markov schemes. State transition rates are given by non- linear sigmoid functions of membrane potential.

By appropriate selection of parameters, the generic model is able to accurately reproduce a wide range of action potential waveforms observed experimentally. Specifically, the model can fit recordings from central and peripheral regions of the SAN with RMS errors of 0.3987 and 0.7628 mV, respectively. Using a custom least squares parameter optimisation routine, we have constructed a spatially- varying gradient model that exhibits a smooth transition in action potential characteristics from the central to the peripheral region, whilst ensuring individual membrane currents remain physiologically accurate. Smooth transition action potential characteristics include maximum diastolic potential, overshoot potential, upstroke velocity, action potential duration and cycle length. The gradient model is suitable for developing higher dimensional models of the right atrium, in which action potential heterogeneity within nodal tissue may be readily incorporated.

\(①\) 2004 Elsevier Ltd. All rights reserved.

Keywords: Sinoatrial node; Gradient model; Markov- state kinetics; Ionic model; Pacemaker

## 1. Introduction

Normal electrical activity of the mammalian heart is initiated by a small region of specialised pacemaker cells located in the wall of the right atrium near the opening of the superior vena cava, known as the sinoatrial node (SAN). These cells are spontaneously active, exhibiting a slow

depolarisation to threshold (pacemaker potential) rather than a stable resting potential. The SAN is known to consist of a large number of heterogeneous cells with some degree of functional electrotonic interconnection (Bleeker et al., 1980; Michaels et al., 1987). Microelectrode recordings from the intact SAN reveal a marked change in action potential (AP) characteristics from the centre to the periphery, including an increase (hyperpolarisation) in the maximum diastolic potential (MDP), an increase in overshoot potential (OS), upstroke velocity (UV) and a decrease in intrinsic cycle length (CL) (Kodama et al., 1997). Despite this variation in AP characteristics, cells of the SAN are able to synchronise their firing rate and drive contraction of the entire atrial myocardium. Such synchronisation of cells, despite differences in intrinsic CL, is due to electrotonic coupling of neighbouring cells via gap junctions; a hypothesis supported both experimentally and via simulation studies (Michaels et al., 1986; Kirchhof et al., 1987; Cai et al., 1994; Verheule et al., 2001).

To date, two alternative theories have been put forward to account for this observed spatial heterogeneity in AP characteristics within the SAN. The first, known as the gradient model, suggests that the heterogeneity arises intrinsically from a spatial gradient in underlying cellular electrophysiological properties (Boyett et al., 2000). Experimental evidence for such a gradient model lies in the fact that similar variation in AP characteristics can be observed in small balls of excised SAN tissue (approximately \(0.3\mathrm{mm}\) in diameter) (Kodama and Boyett, 1985); increases in levels of immunocytochemical labelling of SAN myocytes towards the periphery in the intact node (Musa et al., 2002), as well as the observed increase in myocyte size towards the SAN periphery (Bleeker et al., 1980), and correlated changes in AP characteristics with cell size in isolated SAN myocytes (Honjo et al., 1996). The second theory is the mosaic model, in which atrial myocytes are peppered throughout the SAN region, increasing in density towards the periphery. AP heterogeneity arises from extensive electrotonic coupling between atrial and pacemaker myocytes. Evidence for the mosaic hypothesis is that on enzymatic digestion of the SAN region, only atrial and pacemaker cells are isolated, with the electrophysiological characteristics of the latter remaining uniform across all pacemaker cells (Verheijck et al., 1998). This suggests that the source of spatial AP heterogeneity must lie in differences between the relative density of the two cell types within the SAN.

In order to resolve between the two hypothesis of SAN myocyte structure and organisation, computer simulations of electrotonically coupled ionic models may offer useful insights. Biophysically- detailed mathematical models of single cell SAN electrical activity have been extensively published (Noble and Noble, 1984; Wilders et al., 1991; Demir et al., 1994; Dokos et al., 1996; Zhang et al., 2000; Kurata et al., 2002), all to date have been based on Hodgkin- Huxley- type (1952) formalism to model underlying ionic membrane currents. Although yielding generic action potential waveforms crudely similar to those recorded in the laboratory, none of the models were able to accurately reproduce AP waveforms from any specific SAN cell (see Fig. 6 from Zhang et al., 2000 as well as Figs. 6 and 7 from Kurata et al., 2002 for recent examples). This limits the usefulness of such models to quantitatively assess the factors underlying AP heterogeneity in coupled systems of pacemaker cells, as well as elucidating specific ionic mechanisms underlying AP heterogeneity within the SAN. There is a need therefore, for a cell- specific approach in modelling SAN pacemaker activity, which can accurately simulate AP waveforms recorded in the laboratory.

In this study, we present a generic single cell ionic model of rabbit SAN cells based on Markovstate kinetics, capable of highly accurate reproduction of AP waveforms recorded from specific SAN myocytes. Parameters for this model are fitted to cell specific recordings from central and peripheral regions of the SAN using a custom least squares optimisation approach. We then propose a gradient model of the SAN by employing the same optimisation approach to fit a smooth transition in ionic model parameters to achieve a desired variation in AP characteristics. Although crude gradient models of the SAN region have been previously proposed (Cai et al., 1994; Zhang et al., 2002), these are not based on fits to experimental data which show a smooth variation across multiple AP characteristics such as CL, OS, UV, MDP and action potential duration. One advantage of a realistic gradient model is that it allows a specific cell CL, MDP or UV for example, to be chosen through selection of three parameter vectors. Such models can be used to study entrainment phenomena between multiple cells. The suitability of the resulting gradient model for the development of higher dimensional models of the SAN is also briefly discussed.

## 2. Methods

### 2.1. A generic Markov-state sinoatrial node cell ionic model

The SAN cell model developed in this study consists of 12 membrane currents, acting in parallel across a capacitive cell membrane, with transmembrane potential \(E_{\mathrm{m}}\) given by

\[\frac{\mathrm{d}E_{\mathrm{m}}}{\mathrm{d}t} = \frac{-i_{\mathrm{tot}}}{C_{\mathrm{m}}} \quad (1)\]

with total membrane current \(i_{\mathrm{tot}}\) given by the algebraic sum of its 12 constituents:

\[i_{\mathrm{tot}} = i_{\mathrm{f}} + i_{\mathrm{K},r} + i_{\mathrm{K},s} + i_{\mathrm{b},\mathrm{Na}} + i_{\mathrm{Na}} + i_{\mathrm{Na},\mathrm{K}} + i_{\mathrm{NaCa}} + i_{\mathrm{to}} + i_{\mathrm{Ca,L}} + i_{\mathrm{Ca,T}} + i_{\mathrm{b,K}} + i_{\mathrm{b,Cl}}. \quad (2)\]

The kinetic schemes of the currents in (2) is summarised in Table 1. A brief description of the underlying equations for the ionic currents is given in Appendix A. All time- dependent currents were described using three- or four- state Markov kinetic schemes. These kinetic schemes represent conformational changes in membrane- spanning proteins controlling the flow of ions across the cell membrane. With reference to Table 1, transient states of the underlying channel are denoted by \(A\) (activated or open), and \(I_{1}\) , \(I_{2}\) , \(I_{3}\) (inactivated or closed). Forward and reverse state transition rates are functions of membrane potential \(E_{\mathrm{m}}\) according to

\[k = k_{\infty} + \frac{k_{0} - k_{\infty}}{1 + \exp\left[\frac{E_{\mathrm{m}} - E_{50}}{E_{\mathrm{slope}}}\right]}. \quad (3)\]

This equation defines a sigmoidal variation of rate \(k\) as a function of membrane potential defined by four parameters: \(k_{\infty}\) , \(k_{0}\) (the values of \(k\) at \(E_{\mathrm{m}} = \pm \infty\) ), \(E_{50}\) (the value of \(E_{\mathrm{m}}\) at \(50\%\) of \(k\) 's range) and \(E_{\mathrm{slope}}\) (related to the slope at \(E_{\mathrm{m}} = E_{50}\) ). This formulation is largely empirical, similar to descriptions used in previous studies (Liu and Rasmussen, 1997), with the exception that an offset term has been added to the present description (\(k_{\infty}\) ) to account for the additional possibility

Table 1 List of all the membrane currents in the SAN Markov-state model and their corresponding kinetic scheme   

<table>SymbolNameKinetic schemeiCa,LL-type Ca2+ currentA<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>A<br>a</table>

that rates do not vanish at extreme values of voltage. Each rate in the kinetic schemes of Table 1 is given by (3), each having its own set of four parameters. The general form for all time- dependent currents was given by

\[i = gA(E_{\mathrm{m}} - E_{\mathrm{rev}}), \quad (4)\]

given by the set of two equations (refer to Table 1):

\[\begin{array}{l}\frac{\mathrm{d}A_{\mathrm{f}}}{\mathrm{d}t} = -(x_{1} + x_{2} + \beta_{1})A_{\mathrm{f}} - x_{1}I_{\mathrm{1f}} + x_{1},\\ \displaystyle \frac{\mathrm{d}I_{\mathrm{1f}}}{\mathrm{d}t} = (x_{2} - \beta_{3})A_{\mathrm{f}} - (x_{3} + \beta_{3})I_{\mathrm{1f}} + \beta_{3}, \end{array} \quad (5)\]

where the remaining state, \(I_{2\mathrm{f}}\) has been eliminated using the conservation relationship

\[I_{2\mathrm{f}} = 1 - A_{\mathrm{f}} - I_{1\mathrm{f}}.\]

Similar formulations hold for the remaining time- dependent currents. For four- state Markov schemes, 3 sets of equations are used.

Default conductances and rate parameters in (3)- (5) were chosen to fit published voltage- clamp data for each ion current using a custom least squares optimisation routine (Dokos and Lovell, 2003). The same optimisation process, described briefly in the following section, was used to estimate the cell specific model parameters to fit AP data from central and peripheral myocytes.

### 2.2. Central and peripheral sinoatrial node cell models

Using the default values of all model parameters as a starting point, a subset of 173 parameters (170 model parameters plus an additional three parameters denoting the initial values of concentration state variables [K], [Na], [Cl]) was adjusted to fit two experimental recordings of the transmembrane potential obtained at \(32^{\circ}\mathrm{C}\) , as reported by Kodama et al. (1999). These two recordings represented pacemaker activity from the central and peripheral regions of the same SAN preparation from a rabbit. Free parameters were chosen largely on the basis of those which modulated ion channel conductances and kinetics. Parameters not included in the optimisation process included those describing intracellular calcium handling by the SR (thought to be insignificant in non- working SAN myocytes), as well as basic cellular parameters such as compartment volumes, bulk buffer concentrations etc. The latter were assumed to be fixed properties of all SAN myocytes. Model parameter vectors for central and peripheral pacemaker activity were obtained by separately fitting the general Markov- state model with default parameters to each recording using a curvilinear gradient optimisation routine developed for this purpose (Dokos et al., 2001; Dokos and Lovell, 2003). In brief, the fitting process involved, a "data clamp" between the general Markov- state model and the experimental data by injection of a compensatory current ( \(i_{\mathrm{comp}}\) ) calculated at each instant as

\[i_{\mathrm{comp}} = g_{\mathrm{clamp}}(E_{\mathrm{model}} - E_{\mathrm{cell}}) \quad (6)\]

where \(E_{\mathrm{model}}\) is the calculated transmembrane potential returned by the model at any instant \(t\) , \(E_{\mathrm{cell}}\) is the recorded transmembrane potential at the same instant and \(g_{\mathrm{clamp}}\) is an arbitrary conductance which is set high enough such that \(E_{\mathrm{model}}\) approaches \(E_{\mathrm{cell}}\) at every instant. The calculated compensatory current ( \(i_{\mathrm{comp}}\) ) represents the true discrepancy in total membrane current between the ionic model and the actual recording. In the search for a global minimum, the optimisation process involved a random perturbation of the parameter space followed by a number of iterations involving a reweighting of the parameters at each iteration. If there was a limited improvement of an objective function based on the mean square difference between model

and experimental data then the parameter space would once again be randomly perturbed and the process repeated.

During the optimisation process the model parameters were subject to tight constraints designed to ensure reasonable correlation with the default values. All rate parameters and ion current peaks were constrained to lie within physiological limits, to ensure that the contribution of all membrane currents to pacemaker activity was in accordance with commonly reported experimental values. A final constraint was that all ionic species \(\mathbf{K}^{+}\) , \(\mathrm{Na}^{+}\) , \(\mathrm{Ca}^{2 + }\) and \(\mathrm{Cl}^{- }\) should exhibit no cycle- cycle drift. None of the 173 free parameters at optimality for either the central or peripheral AP was found to lie on the upper or lower constraint boundaries.

### 2.3. Gradient model of the sinoatrial node

The central and peripheral SAN cell model parameter sets were used as a basis for formulating the gradient model of the SAN. The "gradient" formulation of cell parameters was handled as a separate optimisation task from the AP fits to central and peripheral data. Thus, there were a total of three separate optimisations runs performed, each having approximately 170 free parameters; two for both central and peripheral AP waveforms and a third run to optimise the interpolation parameter \(X\) which governs the shape of the interpolation function between the two AP extremes. The task of formulating a gradient model is equivalent to determining a suitable interpolation function for the ionic model parameters in the intermediate region between the central and peripheral type cells. Initially a simple linear interpolation for each of the 170 model parameters was investigated, however it was found that with this approach that the cells from the intermediate region did not generate action potentials nor individual ion currents that were physiologically realistic. Thus it was necessary to construct a third parameter vector of 170 values that represented a more complex interpolating function. Consider

\[P(\phi) = [1 - W(\phi)]P_{C} + W(\phi)P_{\mathrm{P}} \quad (7)\]

where \(\phi\) is a dimensionless variable \((0< \phi < 1)\) , analogous to a spatial location within the SAN region, denoting an interpolation point between the central \((\phi = 0)\) and peripheral \((\phi = 1)\) type cells, \(P(\phi)\) denotes the interpolated ionic model parameter vector, \(P_{C}\) and \(P_{\mathrm{P}}\) denote the cell- specific central and peripheral SAN cell model parameter vectors, and \(W(\phi)\) denotes an interpolation weight function which varies from 0.0 in the centre of the SAN to 1.0 in the periphery. We assume the interpolation weight \(W(\phi)\) varies exponentially with \(\phi\) as follows

\[W(\phi) = \left\{ \begin{array}{ll}\frac{1 - \exp(\phi X)}{1 - \exp(X)} & X\neq 0,\\ \phi & X = 0, \end{array} \right. \quad (8)\]

where \(X\) denotes an unknown parameter vector which determines the shape of the interpolation weight function. Experimental evidence for a simple monotonic interpolation function is implied by the observed linear variation in ionic current magnitudes from centre to periphery, using cell size as an indicator of SAN location (Zhang et al., 2002). In the present study, the interpolation weight parameter vector \(X\) was adjusted to produce a linear variation in AP characteristics with respect to \(\phi\) using the same non- linear least squares optimisation technique employed in determining the cell- specific ionic model parameters above. These AP characteristics included a

> **Image description.** A line graph titled "Interpolation Weight $W(\phi)$" illustrates the relationship between the interpolating weight function and the position $\phi$ for various values of an interpolation parameter $X$.
>
> The graph features two primary axes:
> *   The horizontal X-axis is labeled "Position $\phi$" and ranges from 0 to 1.
> *   The vertical Y-axis is labeled "Interpolation Weight $W(\phi)$" and ranges from 0.0 to 1.0.
>
> Multiple curves are plotted, all of which originate at the point (0, 0) and terminate at the point (1, 1). These curves represent the function $W(\phi)$ for different values of the parameter $X$, which is listed in a legend on the right side of the plot.
>
> The visual patterns of the curves demonstrate how the parameter $X$ modulates the shape of the function:
> *   **Linear Case:** The curve corresponding to $X=0$ (implied by the context, though not explicitly listed in the legend) is a straight line connecting (0, 0) and (1, 1).
> *   **Concave Up (Convex):** Curves with negative values of $X$ (e.g., $X=-8, X=-6, X=-4, X=-2$) exhibit a concave up shape, bowing upwards between the start and end points.
> *   **Concave Down (Concave):** Curves with positive values of $X$ (e.g., $X=2, X=4, X=6, X=8$) exhibit a concave down shape, bowing downwards between the start and end points.
>
> The legend lists the specific values of the interpolation parameter $X$ corresponding to the plotted curves:
> *   $X = -8$
> *   $X = -6$
> *   $X = -4$
> *   $X = -2$
> *   $X = 2$
> *   $X = 4$
> *   $X = 6$
> *   $X = 8$
>
> The overall visual effect is a progression of shapes, showing how a single parameter $X$ can transition the weight function from a concave up curve to a linear function, and finally to a concave down curve.

<center>Fig. 1. The interpolating weight function \(W(\phi)\) can assume a variety of shapes transitioning from 0.0 at the central site to 1.0 at the peripheral site, dependent on the value of a single interpolation parameter, \(X\) (see Eq. (8)). When the parameter is near zero the shape is approximately linear. A change in sign of the parameter yields a change in concavity of the weight function. </center>

linear variation in MDP, OS, UV, CL and action potential duration (APD). Thus, the fitting process involved a large- scale parameter optimisation of the parameter vector \(X\) , which describes how each of the 170 parameters which are different in \(P_{\mathrm{C}}\) and \(P_{\mathrm{P}}\) vary in the intermediate region. Fig. 1 plots the shape of the interpolating function \(W(\phi)\) for various values of the interpolation parameter \(X\) , illustrating how this single parameter can modulate the shape of the interpolating weight function from concave up, to linear, to concave down.

### 2.4. Computational methods

Fits of individual ion currents to voltage clamp data (in order to establish default model parameters), as well as the large- scale least squares parameter optimisation for the central and peripheral cell models were carried out on a standard Pentium PC using Matlab (v6.5, The Mathworks, inc). The simulation code for the gradient model was implemented in C and GNU Octave (http://www.octave.org/), on a dual CPU Dell workstation running the GNU/Linux operating system. The ordinary differential equations of the underlying ionic models were evolved using the CVODE solver for stiff systems (Cohen and Hindmarsh, 1996) with a relative error tolerance of \(10^{- 4}\) .

## 3. Results

### 3.1. Central and peripheral sinoatrial node cell models

The parameters of the Markov- state model with default values determined by the individual ion channel fits were optimised to fit central and peripheral AP experimental SAN data of

> **Image description.** A line graph illustrating the membrane potential over time, comparing experimentally recorded action potentials (solid lines) with theoretical fits derived from a Markov-state model (dashed lines).
>
> The graph features two primary data sets, labeled "Central" and "Peripheral," both showing the characteristic shape of an action potential.
>
> **Axes and Scale:**
> *   **Y-axis:** Labeled "Membrane Potential $E_m$ (mV)," ranging from approximately -80 mV to 40 mV.
> *   **X-axis:** Labeled "Time (s)," ranging from 0 to 1 second.
>
> **Data Representation:**
> The figure displays four distinct action potential traces, grouped by region:
> 1.  **Central AP:** This trace shows a rapid depolarization from a resting potential near -80 mV, reaching a peak of approximately 20-30 mV around 0.3 seconds, followed by a sharp repolarization. The solid line (experimental data) and the dashed line (Markov-state model fit) for the central AP are closely aligned, indicating a high degree of correlation between the model and the experimental data.
> 2.  **Peripheral AP:** This trace also begins near -80 mV. Its peak is slightly lower and occurs slightly later than the central AP, reaching a maximum potential of around 20 mV. Similar to the central AP, the solid and dashed lines for the peripheral AP are tightly overlaid, demonstrating a strong fit by the model.
>
> The overall visual pattern confirms that the Markov-state model successfully replicates the temporal dynamics and shape of the action potentials recorded in both the central and peripheral regions of the tissue. The use of solid lines for experimental data and dashed lines for the model fit is consistent across both regions.

<center>Fig. 2. Action potential fits obtained with generic versions of the Markov-state model (dashed lines) to the experimentally recorded transmembrane potentials (solid lines) of Kodama et al. (1999). Generic model parameters for each fit are given in Table 2. </center>

Kodama et al., 1999. Results of model fits to these two regions of SAN tissue are shown in Fig. 2, where a high correlation is evident between experimental AP data and model APs for both central and peripheral cells. Individual model parameters, corresponding to central and peripheral APs, are given in Table 2. The optimisation process took approximately \(20\mathrm{h}\) to complete for each data set. For the fits shown in Fig. 2, the RMS error between model and data was \(0.3987\) and \(0.7628\mathrm{mV}\) for central and peripheral cells, respectively. The good fits obtained to these two sets of experimental data demonstrate the suitability of the optimisation technique for large- scale model systems.

### 3.2. Gradient model of the sinoatrial node

Fig. 3 illustrates simulated APs corresponding to several values of the position parameter \(\phi\) in Eq. (7) following optimisation of the interpolation weight parameter vector \((X)\) in Eq. (8) to produce smooth transitions in AP characteristics. A linear variation in five AP characteristics, MDP, OS, UV, AP duration at \(90\%\) repolarisation \((\mathrm{APD}_{90})\) and CL, from central to peripheral AP was fitted, based on the results of Kodama et al. (1997), who mapped the spatial variation in these AP characteristics within the SAN using small isolated tissue- ball preparations. The objective function was a weighted least squares sum of linear variations in the five AP characteristics noted above, shown with solid lines in Fig. 7. In Fig. 3, the first AP in each case is shown aligned at the moment of maximum UV to illustrate the variation in APD and CL. As is evident, the action potential waveshape follows a smoothly varying profile from central to peripheral cell types. The last column of Table 2 lists the interpolation weight parameter vector \(X\) , which describes the shape of the interpolating function between central and peripheral parameter values.

Figs. 4- 6 show respectively the spatial variation of the total membrane current \(i_{\mathrm{tot}}\) , and the ion currents \(i_{\mathrm{Ca,L}}\) and \(i_{\mathrm{K,r}}\) with respect to the position \(\phi\) . It can be seen from these figures that the ion

Table 2

List of generic SAN model parameters, a brief description, and numerical values obtained after fitting the model to central and peripheral AP waveforms. Also shown is the interpolation parameter (see Eq. (8)) for each of the 170 model parameters fitted to the central and peripheral waveforms. Those model parameters that were not fitted to the AP waveforms, but held constant, are indicated with the-N/A-notation in the interpolation column

| Parameter | Description | Central SAN value | Peripheral SAN value | Interpolation parameter, X |
| :--- | :--- | :--- | :--- | :--- |
| **Basic cellular parameters** | | | | |
| $C_m$ | Membrane capacitance (nF) | 3.200000e-2 | 3.200000e-2 | -N/A |
| $V_i$ | Cytosolic volume (pl) | 2.500000 | 2.500000 | -N/A |
| $V_{up}$ | SR uptake store volume (pl) | 3.500000e-2 | 3.500000e-2 | -N/A |
| $V_{rel}$ | SR release store volume (pl) | 1.500000e-2 | 1.500000e-2 | -N/A |
| $V_c$ | Extracellular cleft space volume (pl) | 5.000000e-1 | 5.000000e-1 | -N/A |
| $[Ca]_b$ | Bulk buffer Ca concentration (mM) | 2.000000 | 2.000000 | -N/A |
| $[Na]_b$ | Bulk buffer Na concentration (mM) | 1.400000e+2 | 1.400000e+2 | -N/A |
| $[K]_b$ | Bulk buffer K concentration (mM) | 5.400000 | 5.400000 | -N/A |
| $[Cl]_b$ | Bulk buffer Cl concentration (mM) | 1.400000e+2 | 1.400000e+2 | -N/A |
| $\tau_b$ | Transfer time constant between extracellular bulk and cleft spaces (s) | 1.000000e-1 | 1.000000e-1 | -N/A |
| **$i_{CaL}$ parameters** | | | | |
| $E_{Ca,rev}$ | Reversal potential of $i_{CaL}$ $i_{Ca,T}$ (mV) | 4.971562e+1 | 9.164335e+1 | -1.558778e-1 |
| $g_{CaL}$ | Membrane conductance of $i_{CaL}$ (nS) | 1.603617e+2 | 1.011347e+2 | 5.690001e-1 |
| $z_{1-CaL-0}$ | $k_0$ value for $z_{1-CaL}$ (s-1) | 1.114652e+2 | 2.345724e+2 | 9.996308e-1 |
| $z_{1-CaL-x}$ | $k_x$ value for $z_{1-CaL}$ (s-1) | 2.450796e+3 | 2.125409e+3 | -7.129458e-1 |
| $z_{1-CaL-E50}$ | $E_{50}$ value for $z_{1-CaL}$ (mV) | -3.115890e+1 | -5.801693e+1 | 1.413512 |
| $z_{1-CaL-Eslope}$ | $E_{slope}$ value for $z_{1-CaL}$ (mV) | 8.814804 | 2.006287e+1 | 1.962094 |
| $\beta_{1-CaL-0}$ | $k_0$ value for $\beta_{1-CaL}$ (s-1) | 1.283314e+4 | 2.331374e+4 | -1.032397 |
| $\beta_{1-CaL-x}$ | $k_x$ value for $\beta_{1-CaL}$ (s-1) | 4.750897e+3 | 2.461750e+3 | 5.235631e-1 |
| $\beta_{1-CaL-E50}$ | $E_{50}$ value for $\beta_{1-CaL}$ (mV) | -2.448097e+1 | -5.220942e+1 | -3.348667 |
| $\beta_{1-CaL-Eslope}$ | $E_{slope}$ value for $\beta_{1-CaL}$ (mV) | 7.300448 | 5.244847 | -1.488186 |
| $z_{2-CaL-0}$ | $k_0$ value for $z_{2-CaL}$ (s-1) | 9.622261e+18 | 1.40028e+11 | 5.39481 |
| $z_{2-CaL-x}$ | $k_x$ value for $z_{2-CaL}$ (s-1) | 1.409285e+17 | 2.730711e+1 | 4.39904 |
| $z_{2-CaL-E50}$ | $E_{50}$ value for $z_{2-CaL}$ (mV) | 3.116335 | -1.108242e+1 | -4.282669 |
| $z_{2-CaL-Eslope}$ | $E_{slope}$ value for $z_{2-CaL}$ (mV) | 7.665513 | 1.117930e+12 | 0.009274 |
| $\beta_{2-CaL-0}$ | $k_0$ value for $\beta_{2-CaL}$ (s-1) | 1.949588e-12 | 8.89158e-11 | 7.91068 |
| $\beta_{2-CaL-x}$ | $k_x$ value for $\beta_{2-CaL}$ (s-1) | 5.983741e-24 | 9.21406e-22 | 0.47314 |
| $\beta_{2-CaL-E50}$ | $E_{50}$ value for $\beta_{2-CaL}$ (mV) | 5.935904 | 8.097958e+6 | 4.99617e-1 |
| $\beta_{2-CaL-Eslope}$ | $E_{slope}$ value for $\beta_{2-CaL}$ (mV) | 2.798249 | 1.701841 | 1.388802e-2 |
| $z_{3-CaL}$ | $z_{3-CaL}$ Ca inactivation rate (mM-2s-1) | 1.395187e+5 | 6.640197e+4 | 1.873741e-29 |
| $\beta_{3-CaL}$ | $\beta_{3-CaL}$ rate (s-1) | 7.648436 | 1.058248e+11 | 1.190150 |
| $z_{4-CaL}$ | $z_{4-CaL}$ rate (s-1) | 4.945259 | 2.759530e-1 | -1.00832e-28 |
| $\beta_{4-CaL}$ | $\beta_{4-CaL}$ Ca inactivation rate (mM-2s-1) | 4.051228e+6 | 4.995671e+6 | 6.012287e-1 |
| **$i_{Ca,T}$ parameters** | | | | |
| $g_{Ca,T}$ | Membrane conductance of $i_{Ca,T}$ (nS) | 6.815962e+2 | 1.128875e+3 | 1.145510 |
| $z_{1-CaL-T,0}$ | $k_0$ value for $z_{1-CaL}$ (s-1) | 0.000000 | 0.000000 | -N/A |

Table 2 (continued)

| Parameter | Central SAN value | Peripheral SAN value | Interpolation parameter, Xz |
| :--- | :--- | :--- | :--- |
| z1-Ca,T-xk_x value for z1-Ca,T (s-1) | 1.202709e+3 | 9.500944e+2 | -1.687644 |
| z1-Ca,T-E50E50 value for z1-Ca,T (mV) | -3.441689e+13 | 9.350843 | 3.700402 |
| z1-Ca,T-E50preE50 value for z1-Ca,T (mV) | 6.142925 | 4.716709 | 1.547989 |
| β1-Ca,T-0k0 value for β1-Ca,T (s-1) | 8.075249e+2 | 6.907857e+2 | 9.341123e-1 |
| β1-Ca,T-xk_x value for β1-Ca,T (s-1) | 9.663276 | 5.79118 | -7.477684e-1 |
| β1-Ca,T-E50E50 value for β1-Ca,T (mV) | -3.025368e+1 | -2.814034e+1 | -1.287440 |
| β1-Ca,T-E50preE50 value for β1-Ca,T (mV) | 2.580329e+12 | 6.03780e+12 | 9.29688e-3 |
| z2-Ca,T-0k0 value for z2-Ca,T (s-1) | 2.458529e+21 | 9.61793e+1 | -7.900263e-1 |
| z2-Ca,T-xk_x value for z2-Ca,T (s-1) | 1.304339e+3 | 1.300505e+3 | 1.905259 |
| z2-Ca,T-E50E50 value for z2-Ca,T (mV) | -1.978266e+1 | -2.734388e+1 | -7.841234e-25 |
| z2-Ca,T-E50preE50 value for z2-Ca,T (mV) | 1.260400e+11 | 3.76905e+12 | 2.212484e-2 |
| z3-Ca,T-0k0 value for z3-Ca,T (s-1) | 1.003146e-19 | 5.56218e-2 | -4.129985e-24 |
| z3-Ca,T-xk_x value for z3-Ca,T (s-1) | 1.157199e-22 | 8.9284e-2 | -6.488506e-8 |
| z3-Ca,T-E50E50 value for z3-Ca,T (mV) | 6.078672 | 1.913205e+17 | 8.24437e-1 |
| z3-Ca,T-E50preE50 value for z3-Ca,T (mV) | 4.938229e-16 | 3.10242e-12 | 2.98622 |
| β3-Ca,T-0k0 value for β3-Ca,T (s-1) | 1.914443 | 7.406713 | 5.643241e-6 |
| β3-Ca,T-xk_x value for β3-Ca,T (s-1) | 4.489695e+23 | 8.17564e+21 | 5.25742 |
| β3-Ca,T-E50E50 value for β3-Ca,T (mV) | -3.948439e+1 | -3.542704e+17 | 8.86973e-1 |
| β3-Ca,T-E50preE50 value for β3-Ca,T (mV) | 1.294915e+16 | 5.953063 | 4.54643e-1 |
| iKx, parameters | | | |
| gKx Membrane conductance of iKx (nS) | 4.714259 | 1.841966e+12 | 3.66955 |
| PK,Na,xNa permeability of iKx | 3.042202e-2 | 2.00117e-1 | -1.202245 |
| z1-K,x-0k0 value for z1-K,x (s-1) | 2.924086e-16 | 7.43210e-6 | 3.020873 |
| z1-K,x-0k_x value for z1-K,x (s-1) | 1.796444 | 4.309993 | 7.532305e-1 |
| z1-K,x-E50E50 value for z1-K,x (mV) | -2.820955e+1 | -5.119427e+1 | -9.816515e-1 |
| z1-K,x-E50preE50 value for z1-K,x (mV) | 1.591213e+13 | 3.138193 | 3.352268 |
| β1-K,x-0k0 value for β1-K,x (s-1) | 1.161054e-12 | 2.93830e+11 | 4.48136 |
| β1-K,x-0k_x value for β1-K,x (s-1) | 5.200598e+14 | 5.51792e+13 | -1.12525e-1 |
| β1-K,x-E50E50 value for β1-K,x (mV) | -6.476931 | 1.362863e+1 | -1.567446 |
| β1-K,x-E50preE50 value for β1-K,x (mV) | 1.149323e+18 | 1.03750e-1 | -1.061901e-23 |
| z2-K,x-0k0 value for z2-K,x (s-1) | 8.010861e-47 | 8.52355e-3 | -2.212620e-22 |
| z2-K,x-0k_x value for z2-K,x (s-1) | 2.814763e+13 | 3.71802e+1 | -6.299239e-1 |
| z2-K,x-E50E50 value for z2-K,x (mV) | 2.606564e+13 | 9.65989e-1 | -1.559115 |
| z2-K,x-E50preE50 value for z2-K,x (mV) | 4.849186 | 4.015363 | 1.193965 |
| z3-K,x-0k0 value for z3-K,x (s-1) | 0.000000 | 0.000000 | - N/A |
| z3-K,x-0k_x value for z3-K,x (s-1) | 1.382251e+11 | 2.69216e+1 | -3.734197e-1 |
| z3-K,x-E50E50 value for z3-K,x (mV) | -1.705602 | 7.281954 | 1.304021e-22 |
| z3-K,x-E50preE50 value for z3-K,x (mV) | 8.661117 | 6.989032 | -6.596451e-2 |
| z4-K,x-0k0 value for z4-K,x (s-1) | 8.525522e+18 | 8.089748e+1 | -3.429248e-1 |
| z4-K,x-0k_x value for z4-K,x (s-1) | 5.839639 | 3.905214 | 6.880624e-1 |
| z4-K,x-E50E50 value for z4-K,x (mV) | 1.662894e+11 | 6.62908e+1 | -4.674050e-24 |
| z4-K,x-E50preE50 value for z4-K,x (mV) | 1.905902e+11 | 7.38942e+1 | -7.455251e-1 |
| β4-K,x-0k0 value for β4-K,x (s-1) | 5.727687 | 9.161707e-9 | -3.529836e-4 |
| β4-K,x-0k_x value for β4-K,x (s-1) | 5.372182e+25 | 5.20903e+2 | -1.536715e-22 |

Table 2 (continued)

| Parameter | Description | Central SAN value | Peripheral SAN value | Interpolation parameter, X |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |
| β4-Kx-ES0 | ES0 value for β4-Kx (mV) | 4.593740e + 1 | 3.645415e + 1 | 4.613553e - 1 |
| β4-Kx-ELoop | ELoop value for β4-Kx (mV) | 4.646354 | 5.806056 | -1.323381 |
| ikx parameters | | | | |
| gKx | Membrane conductance of ikx (nS) | 1.327832e + 1 | 3.468586e + 1 | -1.030909 |
| Pk,Na,s | Na permeability of ikx | 3.052768e - 2 | 3.017770e - 2 | 6.405061e - 2 |
| z1-Kx,s-0 | 0k0 value for z1-Kx,s (s-1) | 1.454664 | 9.090594e - 3 | -1.763295 |
| z1-Kx,s-7 | 7kz value for z1-Kx,s (s-1) | 1.590468e + 1 | 1.653331e + 1 | 6.081533e - 1 |
| z1-Kx,s-ES0 | ES0 value for z1-Kx,s (mV) | 3.402938e + 1 | 3.342643e + 1 | 2.227579 |
| z1-Kx-ELoop | ELoop value for z1-Kx,s (mV) | 9.464062 | 9.513255 | 9.798004e - 1 |
| β1-Kx,s-0 | 0k0 value for β1-Kx,s (s-1) | 3.627997e - 3 | 4.077626e - 2 | -1.175893 |
| β1-Kx,s-7 | 7kz value for β1-Kx,s (s-1) | 4.191217 | 4.120203 | 1.468731 |
| β1-Kx,s-ES0 | ES0 value for β1-Kx,s (mV) | 2.231378e + 1 | 2.298681e + 1 | 5.877908e - 2 |
| β1-Kx-ELoop | ELoop value for β1-Kx,s (mV) | 1.062848e + 1 | 1.068728e + 1 | -2.985711e - 1 |
| z2-Kx,s-0 | 0k0 value for z2-Kx,s (s-1) | 7.618576e - 1 | 8.160037e - 1 | -1.614861e - 1 |
| z2-Kx,s-7 | 7kz value for z2-Kx,s (s-1) | 7.206725e - 2 | 7.041751e - 1 | 1.568980 |
| z2-Kx,s-ES0 | ES0 value for z2-Kx,s (mV) | 1.021183e + 1 | 9.611465e + 0 | -7.519027e - 1 |
| z2-Kx-ELoop | ELoop value for z2-Kx,s (mV) | 2.584433 | 2.572296 | 1.046865e - 2 |
| z3-Kx,s-0 | 0k0 value for z3-Kx,s (s-1) | 0.000000 | 0.000000 | - N/A - |
| z3-Kx,s-7 | 7kz value for z3-Kx,s (s-1) | 1.689683e + 1 | 1.606267e + 1 | 3.906250e - 3 |
| z3-Kx,s-ES0 | ES0 value for z3-Kx,s (mV) | 4.216442e + 1 | 5.013262e + 1 | 1.328355 |
| z3-Kx-ELoop | ELoop value for z3-Kx,s (mV) | 8.481221 | 5.364982 | 1.176500e - 5 |
| β3-Kx,s-0 | 0k0 value for β3-Kx,s (s-1) | 1.772049 | 1.789998 | 8.776377e - 1 |
| β3-Kx,s-7 | 7kz value for β3-Kx,s (s-1) | 4.140718e - 1 | 4.204860e - 1 | 9.214321e - 1 |
| β3-Kx,s-ES0 | ES0 value for β3-Kx,s (mV) | 9.821939 | 1.019651e + 1 | 1.002624 |
| β3-Kx-ELoop | ELoop value for β3-Kx,s (mV) | 1.280048e + 1 | 1.278048e + 1 | 3.261719e - 1 |
| h3,k parameter | Kb,k | Membrane permeability of h3,k (pA mM-1.41) | 1.128060e - 16 | 5.72237e - 27 | 4.86361e - 1 |
| i3,n parameters | | | | |
| gNa | Membrane conductance of i3,n (nS) | 2.889016 | 4.309453 | -2.182471e - 1 |
| z1-Na-0 | 0k0 value for z1-Na- (s-1) | 1.022328e - 3 | 1.022328e - 3 | - N/A - |
| z1-Na-7 | 7kz value for z1-Na- (s-1) | 4.354541e + 5 | 3.528015e + 5 | -7.576443e - 5 |
| z1-Na-ES0 | ES0 value for z1-Na- (mV) | -3.807510e + 1 | -3.261229e + 1 | 1.921310 |
| z1-Na-ELoop | ELoop value for z1-Na- (mV) | 4.402125 | 3.038592 | 1.211400 |
| β1-Na-0 | 0k0 value for β1-Na- (s-1) | 1.133128e + 6 | 1.403191e + 6 | 7.406851e - 1 |
| β1-Na-7 | 7kz value for β1-Na- (s-1) | 4.104474e + 5 | 3.020463e + 4 | -1.09932 |
| β1-Na-ES0 | ES0 value for β1-Na- (mV) | -2.238794 | -2.170274e + 1 | 3.026832 |
| β1-Na-ELoop | ELoop value for β1-Na- (mV) | 1.650912 | 1.588363 | 4.477430e - 1 |
| z3-Na-0 | 0k0 value for z3-Na- (s-1) | 2.949648e + 1 | 2.544195e + 1 | 1.067521 |
| z3-Na-7 | 7kz value for z3-Na- (s-1) | 1.710387e + 2 | 1.636786e + 2 | -1.930406 |
| z3-Na-ES0 | ES0 value for z3-Na- (mV) | -1.840728e + 1 | -1.412021e + 1 | 1.120039 |
| z3-Na-ELoop | ELoop value for z3-Na- (mV) | 1.660660e + 1 | 1.445599e + 1 | -4.218539e - 1 |
| z3-Na-0 | 0k0 value for z3-Na- (s-1) | 0.000000 | 0.000000 | - N/A - |
| z3-Na-7 | 7kz value for z3-Na- (s-1) | 2.031228 | 2.303278 | -1.634235 |

Table 2 (continued)

| Parameter | Description | Central SAN value | Peripheral SAN value | Interpolation parameter, X |
| :--- | :--- | :--- | :--- | :--- |
| $z_{3\text{-Na}}$ | $E_{50}$ value for $z_{3\text{-Na}}$ (mV) | $-3.004184\mathrm {e}+1$ | $-2.966495\mathrm {e}+1$ | $-6.982675\mathrm {e}-2$ |
| $z_{3\text{-Na}}$ | $E_{50}$ value for $z_{3\text{-Na}}$ (mV) | $1.274548\mathrm {e}-1$ | $1.274591\mathrm {e}-1$ | $8.105469\mathrm {e}-2$ |
| $z_{4\text{-Na}}$ | $k_{0}$ value for $z_{4\text{-Na}}$ (s$^{-1}$) | $6.0001555\mathrm {e}+1$ | $6.341665\mathrm {e}+1$ | $-1.348839\mathrm {e}-3$ |
| $z_{4\text{-Na}}$ | $k_{x}$ value for $z_{4\text{-Na}}$ (s$^{-1}$) | $0.000000$ | $0.000000$ | - |
| $z_{4\text{-Na}}$ | $E_{50}$ value for $z_{4\text{-Na}}$ (mV) | $-5.555892\mathrm {e}+1$ | $-6.305623\mathrm {e}+1$ | $-2.480189$ |
| $z_{4\text{-Na}}$ | $E_{50}$ value for $z_{4\text{-Na}}$ (mV) | $4.849425$ | $2.740067$ | $9.118428\mathrm {e}-1$ |
| $\beta_{4\text{-Na}}$ | $k_{0}$ value for $\beta_{4\text{-Na}}$ (s$^{-1}$) | $1.830626\mathrm {e}-4$ | $6.460518$ | $6.849027$ |
| $\beta_{4\text{-Na}}$ | $k_{x}$ value for $\beta_{4\text{-Na}}$ (s$^{-1}$) | $1.903704\mathrm {e}+3$ | $1.911842\mathrm {e}+3$ | $1.145387$ |
| $\beta_{4\text{-Na}}$ | $E_{50}$ value for $\beta_{4\text{-Na}}$ (mV) | $1.821450\mathrm {e}+1$ | $1.619020\mathrm {e}+1$ | $8.849546\mathrm {e}-1$ |
| $\beta_{4\text{-Na}}$ | $E_{50}$ value for $\beta_{4\text{-Na}}$ (mV) | $1.465804\mathrm {e}+1$ | $1.428674\mathrm {e}+1$ | $-6.927059\mathrm {e}-2$ |
| $K_{\text{NaCa}}$ | Scaling factor for $i_{\text{NaCa}}$ (pA) | $2.294031\mathrm {e}+3$ | $5.088477\mathrm {e}+3$ | $1.040933$ |
| $K_{CJ}$ | Carrier binding constant (mM) | $6.509609\mathrm {e}-3$ | $2.671507\mathrm {e}-3$ | $-3.772723\mathrm {e}-1$ |
| $K_{C_o}$ | Carrier binding constant (mM) | $3.299484$ | $6.000595$ | $-3.486972\mathrm {e}-1$ |
| $K_{C\text{Ni}}$ | Carrier binding constant (mM) | $2.568215\mathrm {e}+1$ | $2.325160\mathrm {e}+1$ | $1.617863$ |
| $K_{1\text{Ni}}$ | Carrier binding constant (mM) | $3.938014\mathrm {e}+2$ | $4.945203\mathrm {e}+2$ | $-6.289877\mathrm {e}-1$ |
| $K_{1\text{No}}$ | Carrier binding constant (mM) | $2.199762\mathrm {e}+3$ | $2.059807\mathrm {e}+3$ | $4.391361\mathrm {e}-8$ |
| $K_{2\text{Ni}}$ | Carrier binding constant (mM) | $2.286485$ | $2.808650$ | $-7.958995\mathrm {e}-1$ |
| $K_{2\text{No}}$ | Carrier binding constant (mM) | $7.638536\mathrm {e}+2$ | $7.298272\mathrm {e}+2$ | $1.787050\mathrm {e}-1$ |
| $K_{3\text{Ni}}$ | Carrier binding constant (mM) | $2.490424\mathrm {e}+1$ | $2.936418\mathrm {e}+1$ | $-4.697630\mathrm {e}-1$ |
| $K_{3\text{No}}$ | Carrier binding constant (mM) | $6.324583$ | $6.099004$ | $-4.055719\mathrm {e}-1$ |
| $Q_{CJ}$ | Fractional charge movement | $1.420663\mathrm {e}-1$ | $1.121362\mathrm {e}-1$ | $2.128940$ |
| $Q_{C_o}$ | Fractional charge movement | $0.00000$ | $0.000000$ | - |
| $Q_{\text{N}}$ | Fractional charge movement | $2.650163\mathrm {e}-1$ | $1.464489\mathrm {e}-1$ | $8.432138\mathrm {e}-1$ |
| $g_{\text{b,Na}}$ | Membrane conductance of $i_{\text{b,Na}}$ (nS) | $2.692229\mathrm {e}-1$ | $2.061193\mathrm {e}-1$ | $-2.385927\mathrm {e}-8$ |
| $g_{\text{f,Na}}$ | Membrane Na conductance of $i_{\text{f}}$ (nS) | $5.031338\mathrm {e}+2$ | $8.806128\mathrm {e}+3$ | $1.398976$ |
| $P_{\text{f,K}}$ | K to Na permeability ratio of $i_{\text{f}}$ | $1.161545$ | $3.716073$ | $-2.672980$ |
| $K_{\text{m,f}}$ | $K_{\text{m}}$ for K+ activation of $i_{\text{f}}$ (mM) | $1.030000\mathrm {e}+1$ | $1.030000\mathrm {e}+1$ | - |
| $z_{1\text{-f,0}}$ | $k_{0}$ value for $z_{1\text{-f}}$ (s$^{-1}$) | $1.244335$ | $1.637239$ | $1.168162$ |
| $z_{1\text{-f,∞}}$ | $k_{\infty}$ value for $z_{1\text{-f}}$ (s$^{-1}$) | $2.157435$ | $2.387937$ | $6.259772\mathrm {e}-1$ |
| $z_{1\text{-f,E50}}$ | $E_{50}$ value for $z_{1\text{-f}}$ (mV) | $-4.972675\mathrm {e}+1$ | $-4.230842\mathrm {e}+1$ | $-7.277813\mathrm {e}-1$ |
| $z_{1\text{-f,E50e}}$ | $E_{50}$ value for $z_{1\text{-f}}$ (mV) | $9.458471$ | $6.404797$ | $2.262478$ |
| $\beta_{1\text{-f,0}}$ | $k_{0}$ value for $\beta_{1\text{-f}}$ (s$^{-1}$) | $9.583585\mathrm {e}-3$ | $1.385826$ | $7.529459\mathrm {e}-1$ |
| $\beta_{1\text{-f,∞}}$ | $k_{\infty}$ value for $\beta_{1\text{-f}}$ (s$^{-1}$) | $2.618719\mathrm {e}+1$ | $1.418487\mathrm {e}+1$ | $6.123084\mathrm {e}-2$ |
| $\beta_{1\text{-f,E50}}$ | $E_{50}$ value for $\beta_{1\text{-f}}$ (mV) | $-2.529536\mathrm {e}+1$ | $7.776829$ | $7.906976\mathrm {e}-1$ |
| $\beta_{1\text{-f,E50e}}$ | $E_{50}$ value for $\beta_{1\text{-f}}$ (mV) | $6.206317$ | $6.745904$ | $1.450049$ |
| $z_{2\text{-f,0}}$ | $k_{0}$ value for $z_{2\text{-f}}$ (s$^{-1}$) | $0.000000$ | $0.000000$ | - |
| $z_{2\text{-f,∞}}$ | $k_{\infty}$ value for $z_{2\text{-f}}$ (s$^{-1}$) | $6.950733$ | $1.479597\mathrm {e}+1$ | $-8.137004\mathrm {e}-3$ |
| $z_{2\text{-f,E50}}$ | $E_{50}$ value for $z_{2\text{-f}}$ (mV) | $-6.657809\mathrm {e}+1$ | $-7.882091\mathrm {e}+1$ | $-2.762134\mathrm {e}-1$ |
| $z_{2\text{-f,E50e}}$ | $E_{50}$ value for $z_{2\text{-f}}$ (mV) | $1.012870\mathrm {e}+1$ | $2.973097$ | $5.124117\mathrm {e}-5$ |
| $z_{3\text{-f,0}}$ | $k_{0}$ value for $z_{3\text{-f}}$ (s$^{-1}$) | $5.826125$ | $7.177844$ | $3.523743$ |
| $z_{3\text{-f,∞}}$ | $k_{\infty}$ value for $z_{3\text{-f}}$ (s$^{-1}$) | $0.000000$ | $0.00000$ | - |
| $z_{3\text{-f,E50}}$ | $E_{50}$ value for $z_{3\text{-f}}$ (mV) | $-1.235296\mathrm {e}+2$ | $-9.585455\mathrm {e}+1$ | $3.301268\mathrm {e}-1$ |

Table 2 (continued)

| Parameter | Description | Central SAN value | Peripheral SAN value | Interpolation parameter, X |
| :--- | :--- | :--- | :--- | :--- |
| z3-t-Eslope | Eslope value for z3-t (mV) | 1.035784e+1 | 3.448238 | -5.845339e-1 |
| β3-t-0k0 | k0 value for β3-t (s-1) | 0.000000 | 0.000000 | - N/A - |
| β3-t-∞k∞ | k∞ value for β3-t (s-1) | 1.507090e+1 | 1.449191e+1 | 3.69507 |
| β3-t-E50 | E50 value for β3-t (mV) | -7.442997 | 3.753349 | 2.021396e-1 |
| β3-t-Eslope | Eslope value for β3-t (mV) | 1.322687e+1 | 2.178209e+1 | 5.672875e-1 |
| hNak parameter | smax Maximum value of hNak (pA) | 2.462675e+2 | 3.389706e+2 | -1.479992e-7 |
| KmnAKmn | Kmn for Na activation of hNak (mM) | 4.000000e+1 | 4.000000e+1 | - N/A - |
| KmnKKmn | Kmn for K activation of hNak (mM) | 1.000000 | 1.000000 | - N/A - |
| i10 parameters | g10 Membrane conductance of i10 (nS) | 2.818095e-15 | 4.95184e-11 | 6.23029 |
| z1-t-0k∞ | k∞ value for z1-t0 (s-1) | 3.725721 | 4.067998e-1 | -1.507586 |
| z1-t-∞k∞ | k∞ value for z1-t0 (s-1) | 3.244315e+2 | 3.252458e+2 | -5.668968e-2 |
| z1-t-E50 | E50 value for z1-t0 (mV) | 2.695332e+1 | 1.235410e+1 | -9.780457e-1 |
| z1-t-Eslope | Eslope value for z1-t0 (mV) | 1.808426e+1 | 6.78441e+1 | -1.074617 |
| β1-t-0k0 | k0 value for β1-t0 (s-1) | 2.728781e-2 | 1.318252e-2 | 2.618186 |
| β1-t-∞k∞ | k∞ value for β1-t0 (s-1) | 1.450856e+2 | 1.631006e+2 | 8.025200e-1 |
| β1-t-E50 | E50 value for β1-t0 (mV) | -1.075136e+1 | -1.031465e+1 | -2.413464e-3 |
| β1-t-Eslope | Eslope value for β1-t0 (mV) | 5.012442 | 3.835739 | -8.919565e-1 |
| z2-t-0k0 | k0 value for z2-t0 (s-1) | 3.712539e+2 | 3.856476e+2 | 1.758458e-7 |
| z2-t-∞k∞ | k∞ value for z2-t0 (s-1) | 1.287828e+2 | 6.762189e+1 | -7.435590e-1 |
| z2-t-E50 | E50 value for z2-t0 (mV) | -9.952019e+1 | -9.558536e+1 | 2.062262 |
| z2-t-Eslope | Eslope value for z2-t0 (mV) | 1.706311e+1 | 7.14316e+1 | 5.766935e-1 |
| z3-t-0k0 | k0 value for z3-t0 (s-1) | 4.309102 | 4.109977 | 1.340224 |
| z3-t-∞k∞ | k∞ value for z3-t0 (s-1) | 3.371110e+1 | 3.388704e+1 | -5.430203e-1 |
| z3-t-E50 | E50 value for z3-t0 (mV) | 1.885799e+1 | 2.24718e+1 | 1.379036 |
| z3-t-Eslope | Eslope value for z3-t0 (mV) | 1.485452e+1 | 1.713317e+1 | 9.766973e-4 |
| z4-t-0k0 | k0 value for z4-t0 (s-1) | 1.166770e+2 | 1.169371e+2 | 2.758668 |
| z4-t-∞k∞ | k∞ value for z4-t0 (s-1) | 1.996661e+2 | 2.004894e+2 | 2.549862e-1 |
| z4-t-E50 | E50 value for z4-t0 (mV) | -8.893804e+1 | -8.902846e+1 | 1.295647 |
| z4-t-Eslope | Eslope value for z4-t0 (mV) | 8.432438e+1 | 8.393722e+1 | 5.61756 |
| β4-t-0k0 | k0 value for β4-t0 (s-1) | 2.804933e-1 | 2.801428e-1 | -2.072468e-1 |
| β4-t-∞k∞ | k∞ value for β4-t0 (s-1) | 7.776120 | 7.791389 | -8.581039e-1 |
| β4-t-E50 | E50 value for β4-t0 (mV) | -1.176010e+2 | -1.175799e+2 | 9.443624e-1 |
| β4-t-Eslope | Eslope value for β4-t0 (mV) | 1.031513e+2 | 1.030196e+2 | 4.630502e-1 |
| hNc1 parameter | gNc1 Membrane conductance of hNc1 (nS) | 8.691184e-2 | 1.675541e-1 | 0.000000 |
| SR uptake and release parameters | iimp,max Maximal value of iup (pA) | 2.120000e+1 | 2.120000e+1 | N/A - |
| SR uptake and release parameters | KmnC,u,up Kmn for Ca activation of iup (mM) | 5.000000e-4 | 5.000000e-4 | N/A - |
| SR uptake and release parameters | KmnC,u,rel Kmn for Ca activation of irel (mM) | 1.000000e-3 | 1.000000e-3 | N/A - |
| SR uptake and release parameters | τrel Time constant for Ca release (s) | 5.000000e-3 | 5.000000e-3 | N/A - |
| SR uptake and release parameters | τtr Transfer time constant between SR uptake and release (s) | 4.000000e-1 | 4.000000e-1 | N/A - |

> **Image description.** A multi-line graph titled "Fig. 3" (based on the context) that plots the membrane potential ($E_m$) of a cell over time for various values of a spatial position parameter, $\phi$.
>
> The graph displays the following visual elements:
>
> *   **Axes:**
>     *   The vertical Y-axis is labeled "Membrane Potential $E_m$" and ranges from -80 mV to 40 mV, marked with major increments of 20 mV.
>     *   The horizontal X-axis is labeled "Time (s)" and ranges from 0 to 1.0 seconds, marked with major increments of 0.2 seconds.
> *   **Data Curves:** The plot contains eleven distinct, overlapping curves, each representing the action potential (AP) of the cell at a specific value of $\phi$. These curves exhibit the characteristic shape of an action potential, including a rapid depolarization, a peak, and a subsequent repolarization phase.
> *   **Legend:** A legend is located in the upper right corner, listing the values of the parameter $\phi$ that correspond to the different curves: 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, and 1.0.
> *   **Visual Trend:** The primary visual observation is the gradual transition in the characteristics of the action potential as the value of $\phi$ increases. The curves corresponding to lower $\phi$ values (e.g., 0.0 and 0.1) show one set of AP characteristics, while the curves corresponding to higher $\phi$ values (e.g., 0.9 and 1.0) show a visibly different, though related, set of AP characteristics, demonstrating a smooth transition across the spatial gradient.

<center>Fig. 3. Plots of action potentials for the gradient model with the position \(\phi\) varying from 0.0 at the central site to 1.0 at the peripheral site. The gradual transition in AP characteristics can be readily observed. </center>

> **Image description.** A line graph titled "Plots of total membrane current as a function of time for all values of position $\phi$ varying from 0.0 at the central site to 1.0 at the peripheral site" (based on the context) displays the relationship between total membrane current and time for various spatial positions ($\phi$).
>
> The graph features two primary axes:
> *   **Y-axis:** Labeled "Total Membrane Current $i_{\text{tot}}$ (pA/pF)", with a numerical scale ranging from -12 to 4.
> *   **X-axis:** Labeled "Time (s)", with a numerical scale ranging from 0 to 1.
>
> The data is represented by a series of eleven distinct lines, each corresponding to a specific value of the parameter $\phi$. These values are listed in a legend located in the upper right corner: $\phi = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0$.
>
> Visually, all curves exhibit a similar transient pattern over the 1-second interval. They begin with a sharp, rapid decrease in current (a large negative inward current), reaching a minimum around 0.2 to 0.3 seconds. Following this initial peak, the current stabilizes briefly before gradually increasing towards a positive value as time approaches 1 second.
>
> The most notable visual feature is the smooth transition between the curves as $\phi$ increases. The curve for $\phi=0.0$ (the lowest value, represented by the darkest line) shows the most pronounced initial negative peak and a specific kinetic profile. As $\phi$ increases toward 1.0 (the highest value, represented by the lightest line), the overall shape of the current profile shifts, indicating a gradual change in the kinetics and amplitude of the membrane current across the spatial positions. The curves are ordered such that the profile for $\phi=0.0$ is distinct from the profile for $\phi=1.0$, demonstrating a continuous variation in the total membrane current as the position $\phi$ moves from the central site to the peripheral site.

<center>Fig. 4. Plots of total membrane current as a function of time for all values of position \(\phi\) varying from 0.0 at the central site to 1.0 at the peripheral site. </center>

currents exhibit smooth transitions in kinetics and amplitude with respect to the parameter \(\phi\) . Moreover, the variation in peak inward amplitude of \(i_{\mathrm{Ca,L}}\) and peak outward amplitude of \(i_{\mathrm{K,r}}\) with respect to spatial position is also in quantitative agreement with published experimental data in isolated SAN myocytes using cell size as an indicator of spatial SAN position (Lei et al., 2001; Musa et al., 2002). The trend in these peak currents is also indirectly suggested from the spatial variation in AP characteristics themselves. That is, UV is known to be greatest in the SAN periphery, therefore peak inward \(i_{\mathrm{Ca,L}}\) being the major determinant of UV in SAN pacemaker cells

> **Image description.** A multi-line graph titled "L-type Calcium Current $i_{\mathrm{Ca,L}}$" displays the transient behavior of the L-type calcium membrane current over time for various spatial positions, represented by the parameter $\phi$.
>
> The graph features two primary axes:
> *   **Y-axis:** L-type Calcium Current $i_{\mathrm{Ca,L}}$ (pA), ranging from 0 at the top to -14 at the bottom. The negative values indicate an inward current.
> *   **X-axis:** Time (s), ranging from 0 to 1.
>
> The data is presented as a series of overlapping curves, each corresponding to a specific value of the position parameter $\phi$. A legend on the right side of the plot lists all the values of $\phi$ tested: $\phi = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0$.
>
> All curves exhibit a similar transient pattern: they begin near zero at time $t=0$, rise rapidly to a peak negative value (representing the peak inward current), and then decay back toward zero as time approaches 1 second.
>
> A clear visual trend is observable: the curves corresponding to higher values of $\phi$ (moving from the center, $\phi=0.0$, to the periphery, $\phi=1.0$) reach a greater peak inward current magnitude. For instance, the curve for $\phi=1.0$ reaches the most negative peak, while the curve for $\phi=0.0$ reaches the least negative peak, demonstrating that the peak L-type calcium current is greatest at the peripheral site. The curves are tightly clustered but show a distinct separation based on the value of $\phi$.

<center>Fig. 5. Plots of L-type \(\mathrm{Ca}^{2 + }\) membrane current, \(i_{\mathrm{Ca,L}}\) for all values of position \(\phi\) varying from 0.0 at the central site to 1.0 at the peripheral site. Peak inward L-type current is seen to be the greatest at the SAN periphery. </center>

> **Image description.** A line graph titled "Delayed Rectifier Potassium Current $i_{K,r}$" that plots the transient current over time for various values of a position parameter $\phi$.
>
> The graph features two primary axes:
> 1.  **Y-axis (Vertical):** Labeled "Delayed Rectifier Potassium Current $i_{K,r}$ (pA/pF)," with a numerical scale ranging from -0.5 to 3.5.
> 2.  **X-axis (Horizontal):** Labeled "Time (s)," with a numerical scale ranging from 0 to 1.
>
> The main visual content consists of eleven distinct curves, each representing the delayed-rectifying current for a specific value of $\phi$. These curves are arranged in a cluster, showing a characteristic transient response: a rapid increase from zero, reaching a peak, and then decaying back toward zero.
>
> A legend in the upper right corner identifies each curve by its corresponding $\phi$ value, ranging from 0.0 to 1.0. The curves are color-coded or differentiated by line style, with $\phi=0.0$ represented by the lowest curve and $\phi=1.0$ represented by the highest curve.
>
> A clear visual trend is observable: as the value of $\phi$ increases (moving from the central site $\phi=0.0$ to the peripheral site $\phi=1.0$), the peak outward current ($i_{K,r}$) increases significantly. The curve corresponding to $\phi=1.0$ reaches the highest peak current, demonstrating the largest outward current in this region. All curves exhibit a similar temporal profile, peaking between 0.4 and 0.6 seconds before decaying.

<center>Fig. 6. Plots of rapid delayed-rectifying current, \(i_{\mathrm{K},r}\) for all values of position \(\phi\) varying from 0.0 at the central site to 1.0 at the peripheral site. Peak outward \(i_{\mathrm{K},r}\) is largest at the SAN periphery. </center>

should be greatest in this region. Similarly, APD is known to be smallest in the periphery, thereby \(i_{\mathrm{K},r}\) being the dominant repolarisation current in rabbit SAN cells should be larger in this region.

Fig. 7 demonstrates how the desired linear transition in AP characteristics have been achieved by plotting MDP, OS, UV, APD \(_{90}\) and CL as a function of the position parameter \(\phi\) . As mentioned above, linear transition in AP characteristics is suggested from the experimental data of Kodama et al. (1997), who used small tissue- ball preparations isolated from known spatial locations within the SAN. \(R^{2}\) correlation values for these fits obtained from linear regression

> **Image description.** A figure consisting of four line graphs arranged in a 2x2 grid, illustrating the linear interpolation fits of five action potential characteristics as a function of position ($\phi$). Each panel displays a solid line representing the least squares objective function (linear interpolation) and a series of solid square data points representing values produced by a gradient cell model.
>
> The common horizontal axis for all four panels is labeled "Position $\phi$," ranging from 0.0 (central) to 1.0 (peripheral). The vertical axes (y-axes) vary for each characteristic, representing different electrical properties measured in millivolts (mV) or milliseconds (ms).
>
> The four panels are detailed as follows:
>
> 1.  **Top Left Panel (MDP and OS):**
>     *   **Y-axis Label:** "MDP and OS (mV)".
>     *   **Trend:** The data shows a clear, positive, linear increase. The values start around -80 mV at $\phi=0.0$ and increase to approximately 20 mV at $\phi=1.0$.
>
> 2.  **Top Right Panel (UV):**
>     *   **Y-axis Label:** "UV (mV)".
>     *   **Trend:** The data shows a clear, positive, linear increase. The values start near 0 mV at $\phi=0.0$ and increase to approximately 12 mV at $\phi=1.0$.
>
> 3.  **Bottom Left Panel ($\mathrm{APD}_{90}$):**
>     *   **Y-axis Label:** "$\mathrm{APD}_{90}$ (ms)".
>     *   **Trend:** The data shows a clear, negative, linear decrease. The values start around 180 ms at $\phi=0.0$ and decrease to approximately 40 ms at $\phi=1.0$.
>
> 4.  **Bottom Right Panel (CL):**
>     *   **Y-axis Label:** "CL (ms)".
>     *   **Trend:** The data shows a clear, negative, linear decrease. The values start around 480 ms at $\phi=0.0$ and decrease to approximately 380 ms at $\phi=1.0$.
>
> In summary, the figure visually demonstrates that four key action potential characteristics (MDP, OS, UV, $\mathrm{APD}_{90}$, and CL) exhibit a linear gradient across the tissue, transitioning from central ($\phi=0.0$) to peripheral ($\phi=1.0$) locations. The solid lines represent the mathematical fit to the data points (solid squares) generated by the gradient cell model.

<center>Fig. 7. Linear interpolation fits as a function of position \(\phi\) obtained to five action potential characteristics. From left to right, top to bottom these are: MDP and OS (top left), UV, \(\mathrm{APD}_{90}\) , and CL. Solid lines depict the least squares objective function exhibiting linear interpolation between central and peripheral AP waveshape properties. Solid squares indicate corresponding values of AP waveshape properties produced by the gradient cell model, evaluated at discrete spatial locations separated by \(\Delta \phi = 0.05\) , where \(\phi = 0.0\) denotes central and \(\phi = 1.0\) peripheral. </center>

analysis were all close to unity. For the panels of Fig. 7, they are 0.9945 (OS), 0.9218 (MDP), 0.9828 (UV), 0.9832 (APD₉₀), and 0.9876 (CL).

## 4. Discussion

Based on their experimental recordings from small balls of isolated sinoatrial node tissue, Kodama and Boyett (1985) proposed the conventional gradient model of the SAN. This gradient model attributes the observed changes in AP waveshape to a genuine variation in cell membrane electrophysiological properties. More recently, Verheijck et al. (1998), identified three morphologically different types of SAN cells in addition to atrial myocytes in rabbit SAN tissue. After enzymatic isolation, these three cell types exhibited no significant differences in AP characteristics. Verheijck et al. therefore hypothesised that the observed variation in AP characteristics from the centre to the periphery of the SAN was due to a gradual increase in atrial cell numbers toward the periphery. This novel interpretation forms the basis of the mosaic model of the SAN.

The ability or otherwise of the mosaic model to explain the observed AP heterogeneity remains a contentious issue. Zhang and colleagues recently attempted to shed light on the problem, formulating mosaic models of central and peripheral SAN tissue using two dimensional network models including SAN and atrial cell types (Zhang et al., 2001, 2002). They assigned either SAN or atrial cell membrane properties to each node in the central and peripheral network models according to the proportions reported by Verheijck et al., 1998, and concluded that the mosaic model could not account for the observed heterogeneity in AP characteristics. Despite this, their studies did not implement a true gradient model of the SAN, in order to compare with their simulations using a mosaic model. Implementing a smooth transition in AP waveshape is non- trivial, even when parameters for central and peripheral cells are available. For example, we have found using the generic SAN model presented in this study that even a simple linear interpolation in all 170 model parameters from centre to periphery causes intermediate APs to become quiescent. Instead, we have used non- linear interpolation, coupled with a large degree of freedom in the fitting procedure arising from the large numbers of parameters employed, to fit a smooth transition in AP characteristics from the centre to the peripheral SAN. Thus, the availability of a suitable gradient SAN model, employing biophysically accurate reconstructions of underlying ionic mechanisms, should enable useful simulations to be carried out to compare gradient and mosaic models of SAN organisation.

Despite parameter constraints imposed, we note that the generic ionic model with 173 free parameters was likely to be an over- determined system of equations, particularly when fitting to a single experimental waveform. The issue of parameter identifiability in cardiac ionic models has been explored in a companion paper (Dokos and Lovell, 2004). The over- determined nature of the generic ionic model used here was implied from the numerically singular Hessian matrix that was generated during each iteration step of the non- linear optimisation routine. It should be noted that the generic model was developed to be used in conjunction with a larger variety of SAN AP records. At present, it remains unclear as to precisely how many degrees of freedom the model requires to fit such a broader range of experimental data. Nonetheless, the main aim of the present study was simply to describe a gradient SAN ionic model that yielded accurate reproduction of AP records, as well as a smooth transition in AP waveshape from central to peripheral cells. Parameter constraints ensured that the electrophysiological behaviour of ionic currents was preserved relative to published records. Future refinements to the parameter fitting process outlined in this study will involve improvements in identifiability through model reduction as well as appropriate experimental design through fits to multiple experimental records.

As an interesting aside, one of the reasons in employing Markov- state kinetics in this study is that such kinetic descriptions allowed for a greater degree of freedom in the fitting of ion current kinetics to AP experimental data, as well as fitting the smooth spatial waveshape transition across the SAN. We find from preliminary experience in fitting AP records that, in general, the extra degrees of freedom is required in order to obtain a generic model that can fit a wide variety of AP waveshapes encountered experimentally. The cyclic Markov- state models adopted were chosen in order to approximately mimic Hodgkin and Huxley (1952) kinetics in the first instance. On closer inspection, it can be readily seen that a 4- state cyclic Markov model can be made equivalent to classical Hodgkin- Huxley gating kinetics employing two gating terms, by ensuring that the parallel rates in the Markov scheme are equal. In this special case, the Markov rates are directly linked to the Hodgkin- Huxley equivalent rates. When viewed in this manner, the cyclic state

Markov- scheme represents a more generalised description of ion channel kinetics, of which classical Hodgkin- Huxley gating behaviour is but a special case.

## 5. Conclusions

Ionic mechanisms underlying pacemaker activity in SAN cells can be investigated using the central, peripheral and gradient models of cellular electrical activity developed in this study. A major improvement over existing models is that model parameters have been adjusted to accurately reproduce an action potential waveform recorded from specific experimental data in peripheral and central SAN tissue. This study represents the first stage in highly accurate modelling of ionic activity in any individual pacemaker cell. The gradient model presented could form the basis of higher dimensional models of coupling and propagation in the SAN and atrium.

## Appendix A

The equations of the generic Markov- state sinoatrial node cell ionic model appear below. Table 2 lists the components of the central and peripheral state vectors ( \(P_{\mathrm{C}}\) and \(P_{\mathrm{P}}\) ) together with the corresponding components of the interpolation parameter vector ( \(X\) ). Table 3 lists stable initial conditions for the central and peripheral sinoatrial node cell models.

1. \(L\) -Type calcium current

\[i_{\mathrm{Ca,L}} = g_{\mathrm{Ca,L}}A_{\mathrm{Ca,L}}(E_{\mathrm{m}} - E_{\mathrm{Ca,rev}}),\]

2. \(T\) -Type calcium current

\[i_{\mathrm{Ca,T}} = g_{\mathrm{Ca,T}}A_{\mathrm{Ca,T}}(E_{\mathrm{m}} - E_{\mathrm{Ca,rev}}).\]

3. Delayed rectifier potassium current

\[i_{\mathrm{K}} = i_{\mathrm{K},\tau} + i_{\mathrm{K},\mathrm{s}},\] \[i_{\mathrm{K},\tau} = i_{\mathrm{K},\mathrm{r}_{\mathrm{Na}} + i_{\mathrm{K},\mathrm{r}_{\mathrm{K}}}},\] \[i_{\mathrm{K},\mathrm{r}_{\mathrm{Na}}} = g_{\mathrm{K},\tau}A_{\mathrm{K},\tau}P_{\mathrm{KNa},\tau}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{K},\mathrm{r}_{\mathrm{K}}} = g_{\mathrm{K},\tau}A_{\mathrm{K},\tau}(E_{\mathrm{m}} - E_{\mathrm{K}}),\] \[i_{\mathrm{K},\mathrm{s}} = i_{\mathrm{K},\mathrm{s}_{\mathrm{Na}}} + i_{\mathrm{K},\mathrm{s}_{\mathrm{K}}},\] \[i_{\mathrm{K},\mathrm{s}_{\mathrm{Na}}} = g_{\mathrm{K},\mathrm{s}}A_{\mathrm{K},\mathrm{s}}P_{\mathrm{KNa},\mathrm{s}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{K},\mathrm{s}_{\mathrm{K}}} = g_{\mathrm{K},\mathrm{s}}A_{\mathrm{K},\mathrm{s}}(E_{\mathrm{m}} - E_{\mathrm{K}}).\]

4. \(TTX\) sensitive sodium current

\[i_{\mathrm{Na}} = g_{\mathrm{Na}}A_{\mathrm{Na}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\]

Table 3 List of initial conditions for all state variables in the generic SAN model, for both central and peripheral versions

| Variable | Central SAN cell | Peripheral SAN cell |
| :--- | :--- | :--- |
| $E_m$ | $-6.39512\mathrm{e}+1$ | $-7.663138\mathrm{e}+1$ |
| $[Ca]_i$ | $1.275323\mathrm{e}-4$ | $6.623230\mathrm{e}-5$ |
| $[Ca]_{up}$ | $1.035010$ | $7.506109\mathrm{e}-1$ |
| $[Ca]_{ef}$ | $2.447983\mathrm{e}-1$ | $1.365436\mathrm{e}-1$ |
| $[Ca]_s$ | $1.999744$ | $2.000020$ |
| $[Na]_i$ | $8.003895$ | $1.359578\mathrm{e}+1$ |
| $[Na]_s$ | $1.400235\mathrm{e}+2$ | $1.399803\mathrm{e}+2$ |
| $[K]_i$ | $1.498639\mathrm{e}+2$ | $2.121477\mathrm{e}+2$ |
| $[K]_s$ | $5.389262$ | $5.442564$ |
| $[Cl]_i$ | $2.606581\mathrm{e}+1$ | $2.489672\mathrm{e}+1$ |
| $[Cl]_s$ | $1.400001\mathrm{e}+2$ | $1.399971\mathrm{e}+2$ |
| $A_{Ca,L}$ | $4.563555\mathrm{e}-4$ | $6.736841\mathrm{e}-4$ |
| $I_{1-Ca,L}$ | $9.601208\mathrm{e}-1$ | $9.764172\mathrm{e}-1$ |
| $I_{2-Ca,L}$ | $5.260367\mathrm{e}-3$ | $3.012387\mathrm{e}-3$ |
| $A_{Ca,T}$ | $1.561896\mathrm{e}-5$ | $2.070065\mathrm{e}-10$ |
| $I_{1-Ca,T}$ | $9.985167\mathrm{e}-1$ | $9.961892\mathrm{e}-1$ |
| $A_{K,r}$ | $1.209480\mathrm{e}-1$ | $9.958786\mathrm{e}-2$ |
| $I_{1-K,r}$ | $1.991481\mathrm{e}-3$ | $1.243415\mathrm{e}-1$ |
| $I_{2-K,r}$ | $5.616591\mathrm{e}-2$ | $2.453342\mathrm{e}-4$ |
| $A_{K,s}$ | $5.048523\mathrm{e}-3$ | $1.733389\mathrm{e}-3$ |
| $I_{1-K,s}$ | $9.920536\mathrm{e}-1$ | $9.945393\mathrm{e}-1$ |
| $A_{Na}$ | $5.586372\mathrm{e}-4$ | $6.111398\mathrm{e}-8$ |
| $I_{1-Na}$ | $3.749674\mathrm{e}-1$ | $4.104663\mathrm{e}-1$ |
| $I_{2-Na}$ | $1.038603\mathrm{e}-1$ | $1.134436\mathrm{e}-1$ |
| $A_f$ | $3.715769\mathrm{e}-4$ | $8.742796\mathrm{e}-5$ |
| $I_{1-f}$ | $9.972171\mathrm{e}-1$ | $9.988556\mathrm{e}-1$ |
| $A_{to}$ | $1.219969\mathrm{e}-2$ | $1.479078\mathrm{e}-2$ |
| $I_{1-to}$ | $6.310187\mathrm{e}-1$ | $7.741232\mathrm{e}-1$ |
| $I_{2-to}$ | $2.696949\mathrm{e}-2$ | $2.586954\mathrm{e}-2$ |

# 5. Sodium-calcium exchange current

\[I_{\mathrm {NaCa}}=K_{\mathrm {NaCa}}\frac {x_{2}k_{21}-x_{1}k_{12}}{x_{1}+x_{2}+x_{3}+x_{4}},\]

\[x_{1}=(k_{23}+k_{21})k_{41}k_{34}+(k_{43}+k_{41})k_{21}k_{32},\]

\[x_{2}=(k_{14}+k_{12})k_{32}k_{43}+(k_{34}+k_{32})k_{12}k_{41},\]

\[x_{3}=(k_{23}+k_{21})k_{14}k_{43}+(k_{43}+k_{41})k_{12}k_{23},\]

\[x_{4}=(k_{14}+k_{12})k_{23}k_{34}+(k_{34}+k_{32})k_{14}k_{21},\]

\[D_{1}=1.0+\frac {[\mathrm {Ca}]_{\mathrm {i}}}{K_{\mathrm {C,i}}}\left(1.0+\exp \left(-\frac {E_{\mathrm {m}}Q_{\mathrm {C,i}}F}{RT}\right)\right)\frac {[\mathrm {Ca}][\mathrm {Na}]}{K_{\mathrm {C,i}}K_{\mathrm {C,Ni}}}+\frac {[\mathrm {Na}]}{K_{\mathrm {1,Ni}}}\left(1.0+\frac {[\mathrm {Na}]}{K_{\mathrm {2,Ni}}}\right)\right),\]

\[k_{43} = \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{Ni}}[\mathrm{Na}]_{i}},\] \[k_{12} = \frac{[\mathrm{Ca}]_{i}\mathrm{exp}\left(-\frac{E_{\mathrm{m}}Q_{\mathrm{C},i}F}{RT}\right)}{K_{\mathrm{C},i}D_{1}},\] \[k_{14} = \frac{[\mathrm{Na}]_{i}^{2}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{Ni}}}\right)\mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right)}{K_{1,\mathrm{Ni}}K_{2,\mathrm{Ni}}D_{1}},\] \[k_{41} = \mathrm{exp}\left(-\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right),\] \[D_{2} = 1.0 + \frac{[\mathrm{Ca}]_{i}}{K_{\mathrm{C},0}}\left(1.0 + \mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{C},0}F}{RT}\right)\right) + \frac{[\mathrm{Na}]_{i}}{K_{1,\mathrm{No}}}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{2,\mathrm{No}}}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{No}}}\right)\right),\] \[k_{34} = \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{No}}[\mathrm{Na}]_{i}},\] \[k_{21} = \frac{[\mathrm{Ca}]_{i}\mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{C},0}F}{RT}\right)}{K_{\mathrm{C},0}D_{2}},\] \[k_{23} = \frac{[\mathrm{Na}]_{i}^{2}\left(1.0 + \frac{[\mathrm{Na}]_{i}}{K_{3,\mathrm{No}}}\right)\mathrm{exp}\left(-\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right)}{K_{1,\mathrm{No}}K_{2,\mathrm{No}}D_{2}},\] \[k_{32} = \mathrm{exp}\left(\frac{E_{\mathrm{m}}Q_{\mathrm{N}}F}{2.0RT}\right).\]

6. Hyperpolarisation activated inward current

\[i_{\mathrm{f}} = i_{\mathrm{f}_{\mathrm{Na}}} + i_{\mathrm{f}_{\mathrm{K}}},\] \[i_{\mathrm{f}_{\mathrm{Na}}} = A_{\mathrm{f}}\frac{[\mathrm{K}]_{\mathrm{o}}^{1.83}}{[\mathrm{K}]_{\mathrm{o}}^{1.83} + K_{\mathrm{m,f}}^{1.83}} g_{\mathrm{f},\mathrm{Na}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{f}_{\mathrm{K}}} = A_{\mathrm{f}}\frac{[\mathrm{K}]_{\mathrm{o}}^{1.83}}{[\mathrm{K}]_{\mathrm{o}}^{1.83} + K_{\mathrm{m,f}}^{1.83}} P_{\mathrm{f},\mathrm{K}}g_{\mathrm{f},\mathrm{Na}}(E_{\mathrm{m}} - E_{\mathrm{K}}).\]

7. Sodium-potassium pump current

\[i_{\mathrm{Na,K}} = I_{\mathrm{p,max}}\frac{[\mathrm{Na}]_{i}}{[\mathrm{Na}]_{i} + K_{\mathrm{m,Na}}[\mathrm{K}]_{\mathrm{o}} + K_{\mathrm{m,K}}}\left(1.0 - \left(\frac{E_{\mathrm{m}} - 40.0}{211.0}\right)^{2}\right).\]

8. 4-Aminopyridine (4-AP) sensitive outward current

\[i_{\mathrm{to}} = g_{\mathrm{to}}A_{\mathrm{to}}(E_{\mathrm{m}} - E_{\mathrm{K}}).\]

9. Background currents

\[i_{\mathrm{b,Na}} = g_{\mathrm{b,Na}}(E_{\mathrm{m}} - E_{\mathrm{Na}}),\] \[i_{\mathrm{b,K}} = K_{\mathrm{b,K}}[\mathrm{K}]_{\mathrm{o}}^{0.41}\left([\mathrm{K}]_{\mathrm{i}} - \left([\mathrm{K}]_{\mathrm{o}}\mathrm{exp}\left(-\left(\frac{E_{\mathrm{m}}F}{RT}\right)\right)\right),\] \[i_{\mathrm{b,Cl}} = g_{\mathrm{b,Cl}}(E_{\mathrm{m}} - E_{\mathrm{Cl}}).\]

10. Calcium sequestration in the sarcoplasmic reticulum

\[i_{\mathrm{Ca,up}} = I_{\mathrm{up,max}}\frac{1.0}{1.0 + \left(\frac{K_{\mathrm{m,Caup}}}{[\mathrm{Ca}]_{\mathrm{i}}}\right)^{2}},\] \[i_{\mathrm{Ca,rel}} = \frac{2.0FV_{\mathrm{rel}}}{\tau_{\mathrm{rel}}} [\mathrm{Ca}]_{\mathrm{rel}}\frac{1.0}{1.0 + \left(\frac{K_{\mathrm{m,Ca_{rel}}}}{[\mathrm{Ca}]_{\mathrm{i}}}\right)^{2}},\] \[i_{\mathrm{Ca,tr}} = \frac{2.0FV_{\mathrm{rel}}}{\tau_{\mathrm{tr}}} [\mathrm{Ca}]_{\mathrm{up}}.\]

11. Compartment ion concentrations

\[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{i}}}{\mathrm{d}t} = -\frac{i_{\mathrm{Ca,L}} + i_{\mathrm{Ca,T}} - 2.0i_{\mathrm{NaCa}} + i_{\mathrm{Ca,up}} - i_{\mathrm{Ca,rel}}}{2.0FV_{\mathrm{i}}},\] \[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{up}}}{\mathrm{d}t} = \frac{i_{\mathrm{Ca,up}} - i_{\mathrm{Ca,tr}}}{2.0FV_{\mathrm{up}}},\] \[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{rel}}}{\mathrm{d}t} = \frac{i_{\mathrm{Ca,tr}} - i_{\mathrm{Ca,rel}}}{2.0FV_{\mathrm{rel}}},\] \[\frac{\mathrm{d}[\mathrm{Ca}]_{\mathrm{o}}}{\mathrm{d}t} = \frac{i_{\mathrm{Ca,L}} + i_{\mathrm{Ca,T}} - 2.0i_{\mathrm{NaCa}} + [\mathrm{Ca}]_{\mathrm{b}} - [\mathrm{Ca}]_{\mathrm{o}}}{2.0FV_{\mathrm{c}}},\] \[\frac{\mathrm{d}[\mathrm{Na}]_{\mathrm{i}}}{\mathrm{d}t} = -\frac{i_{\mathrm{K,Na}} + i_{\mathrm{K,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{NaCa}} + i_{\mathrm{b,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{p}}}{FV_{\mathrm{i}}},\] \[\frac{\mathrm{d}[\mathrm{Na}]_{\mathrm{o}}}{\mathrm{d}t} = \frac{i_{\mathrm{K,Na}} + i_{\mathrm{K,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{NaCa}} + i_{\mathrm{b,Na}} + i_{\mathrm{Na}} + 3.0i_{\mathrm{p}}}{FV_{\mathrm{c}}} +\frac{[\mathrm{Na}]_{\mathrm{b}} - [\mathrm{Na}]_{\mathrm{o}}}{i_{\mathrm{b}}},\] \[\frac{\mathrm{d}[\mathrm{K}]_{\mathrm{i}}}{\mathrm{d}t} = -\frac{i_{\mathrm{K,ri}} + i_{\mathrm{K,ri}} + i_{\mathrm{b,K}} + i_{\mathrm{K}} - 2.0i_{\mathrm{p}} + i_{\mathrm{io}}}{FV_{\mathrm{i}}},\] \[\frac{\mathrm{d}[\mathrm{K}]_{\mathrm{o}}}{\mathrm{d}t} = \frac{i_{\mathrm{K,ri}} + i_{\mathrm{K,ri}} + i_{\mathrm{b,K}} + i_{\mathrm{K}} - 2.0i_{\mathrm{p}} + i_{\mathrm{io}}}{FV_{\mathrm{c}}} +\frac{[\mathrm{K}]_{\mathrm{b}} - [\mathrm{K}]_{\mathrm{o}}}{i_{\mathrm{b}}},\]

\[\frac{\mathrm{d}[\mathrm{Cl}]_i}{\mathrm{d}t} = \frac{i_{\mathrm{b,Cl}}}{FV_i\] \[\frac{\mathrm{d}[\mathrm{Cl}]_o}{\mathrm{d}t} = -\frac{i_{\mathrm{b,Cl}}}{FV_{\mathrm{c}}} +\frac{[\mathrm{Cl}]_{\mathrm{b}} - [\mathrm{Cl}]_o}{\Gamma_{\mathrm{b}}}.\]

## References

Bleeker, W.K., MacKaay, A.J.C., Masson- Pevet, M., Bouman, L.N., Becker, A.E., 1980. Functional and morphological organization of the rabbit sinus node. Circ. Res. 46 (1), 11- 22.  
Boyett, M.R., Honjo, H., Kodama, I., 2000. The sinoatrial node, a heterogeneous pacemaker structure. Cardiovasc. Res. 47, 658- 687.  
Cai, D., Winslow, R.L., Noble, D., 1994. Effects of gap junction conductance on dynamics of sinoatrial node cells: two- cell and large- scale network models. IEEE Trans. Biomed. Eng. 41, 217- 231.  
Cohen, S., Hindmarsh, A., 1996. CVODE, a stiff/nonstiff ODE solver in C. Comput. Phys. 10 (2), 138- 143.  
Demir, S.S., Clark, J.W., Murphey, C.R., Giles, W.R., 1994. A mathematical model of a rabbit sinoatrial node cell. Am. J. Physiol. 266, C832- C852.  
Dokos, S., Lovell, N.H., 2003. A curvilinear gradient path method for optimization of biological systems models. In: Feng, D.D., Carson, E.R. (Eds.), Proceedings of the Fifth IFAC Symposium on Modelling and Control in Biomedical Systems 2003. Elsevier, Oxford, pp. 203- 208.  
Dokos, S., Lovell, N.H., 2004. Parameter estimation in cardiac ionic models. Progr. Biophys. Mol. Biol., doi:10.1016/j.pbiomolbio.2004.02.002.  
Dokos, S., Celler, B.G., Lovell, N.H., 1996. Ion currents underlying sinoatrial node pacemaker activity: a new single cell mathematical model. J. Theoret. Biol. 181, 245- 272.  
Dokos, S., Cloherty, S.L., Lovell, N.H., Zaza, A., 2001. Cell- specific ionic models of cardiac pacemaker activity. In: Proceedings of the 23rd Annual International Conference of the IEEE Engineering in Medicine and Biology Society, IEEE Press, Istanbul, Turkey.  
Hodgkin, A.L., Huxley, A.F., 1952. A quantitative description of membrane current and its application to conduction and excitation in nerve. J. Physiol. 117, 500- 544.  
Honjo, H., Boyett, M.R., Kodama, I., Toyama, J., 1996. Correlation between electrical activity and the size of rabbit sino- atrial node cells. J. Physiol. 496 (3), 795- 808.  
Kirchhof, C.J.H.J., Bonke, F.I.M., Allessie, M.A., Lammers, W.J.E.P., 1987. The influence of the atrial myocardium on impulse formation in the rabbit sinus node. Pflüger's Arch. 410, 198- 203.  
Kodama, I., Boyett, M.R., 1985. Regional differences in the electrical activity extended to include additional experimental recordings from the rabbit sinus node. Pflüger's Arch. 404, 214- 226.  
Kodama, I., Nikmaram, M.R., Boyett, M.R., Suzuki, R., Honjo, H., Owen, J.M., 1997. Regional differences in the role of the \(\mathrm{Ca^{2 + }}\) and \(\mathrm{Na^{+}}\) currents in pacemaker activity in the sinoatrial node. Am. J. Physiol. 272, H2793- H2806.  
Kodama, I., Boyett, M.R., Nikmaram, M.R., Yamamoto, M., Honjo, H., Niwa, R., 1999. Regional differences in effects of E- 4031 within the sinoatrial node. Am. J. Physiol. 276, H793- H802.  
Kurata, Y., Hisatome, I., Imanishi, S., Shibamoto, T., 2002. Dynamical description of sinoatrial node pacemaking: improved mathematical model of primary pacemaker cell. Am. J. Physiol. 283, H2074- H2101.  
Lei, M., Honjo, H., Kodama, I., Boyett, M.R., 2001. Heterogeneous expression of the delayed- rectifier \(\mathrm{K^{+}}\) currents \(i_{\mathrm{K},r}\) and \(i_{\mathrm{K},s}\) in rabbit sinoatrial node cells. J. Physiol. 535, 703- 714.  
Liu, S., Rasmussen, R.L., 1997. Hodgkin- Huxley and partially coupled inactivation models yield different voltage dependence of block. Am. J. Physiol. 272, H2013- H2022.  
Michaels, D.C., Matyas, E.P., Jalife, J., 1986. Dynamic interactions and mutual synchronization of sinoatrial node pacemaker cells. Circ. Res. 58, 706- 720.  
Michaels, D.C., Matyas, E.P., Jalife, J., 1987. Mechanisms of pacemaker synchronization: a new hypothesis. Circ. Res. 61, 704- 714.  
Musa, H., Lei, M., Honjo, H., Jones, S.A., Dobrzynski, H., Lancaster, M.K., Takagishi, Y., Henderson, Z., Kodama, I., Boyett, M.R., 2002. Heterogeneous expression of \(\mathrm{Ca^{2 + }}\) handling proteins in rabbit sinoatrial node. J. Histochem. Cytochem. 50, 311–324.  
Noble, D., Noble, S.J., 1984. A model of sino- atrial node electrical activity based on a modification of the DiFrancesco- Noble (1984) equations. Proc. Roy. Soc. London Ser. B 222, 295–304.  
Verheijck, E.E., Wessels, A., van Ginneken, A.C.G., Bourier, J., Markman, M.W.M., Vermeulen, J.L.M., de Bakker, J.M.T., Lamers, W.H., Opthof, T., Bouman, L.N., 1998. Distribution of atrial and nodal cells within the rabbit sinoatrial node: models of sinoatrial transition. Circulation 97, 1623–1631.  
Verheule, S., van Kempen, M.J.A., Postma, S., Rook, M.B., Jongsma, H.J., 2001. Gap junctions in the rabbit sinoatrial node. Am. J. Physiol. 280, H2103–H2115.  
Wilders, R., Jongsma, H.J., van Ginneken, A.C.G., 1991. Pacemaker activity of the rabbit sinoatrial node: a comparison of mathematical models. Biophys. J. 60, 1202–1216.  
Zhang, H., Holden, A.V., Kodama, I., Honjo, H., Lei, M., Varghese, T., Boyett, M.R., 2000. Mathematical models of action potentials in the periphery and center of the rabbit sinoatrial node. Am. J. Physiol. 279, H397–H421.  
Zhang, H., Holden, A.V., Boyett, M.R., 2001. Gradient model versus mosaic model of the sinoatrial node. Circulation 103, 584–588.  
Zhang, H., Holden, A.V., Boyett, M.R., 2002. Computational approaches to the ionic basis of pacemaker activity–from channel kinetics to the regional differences in rhythm. Chaos, Solitons and Fractals 13, 1631–1642.

---

*Transcribed with OCR and VLMs; text, equations, tables, and figure descriptions may contain mistakes.*
