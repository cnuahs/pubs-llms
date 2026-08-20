```
@article{tsafnat2004afl,
  title={AFL and FRL: abstraction and representation for field interchange},
  author={G. Tsafnat and S. L. Cloherty and T. D. Lambert},
  journal={26th Annual International Conference of the IEEE Engineering in Medicine and Biology Society},
  year={2004},
  volume={2},
  pages={5419-5422},
  doi={10.1109/iembs.2004.1404514},
  url={https://ieeexplore.ieee.org/document/1404514}
}
```

---

# AFL and FRL: Abstraction and Representation for Field Interchange

Guy Tsafnat \(^{1}\) , Shaun L. Cloherty \(^{2}\) and Tim D. Lambert \(^{1}\)

\(^{1}\) School of Computer Science & Engineering \(^{2}\) Graduate School of Biomedical Engineering University of New South Wales Sydney, Australia 2052

Abstract—The holy grail of biomedical modelling is an integrated model of the entire human body. To this end, research groups around the world need to interchange experimental data, models and model results. A good interchange will have an efficient representation for storage and sharing and will have tools for modelling, data verification, authoring, data conversions and so on.

A field is a spatially varying property. In this paper we present the Abstract Field Layer (AFL) and the Field Representation Language (FRL). The AFL provides the field abstraction together with a set of common field operations. The FRL provides an efficient means for field representation and storage. We show how fields can be used to interchange information between modelling systems and between modelling and visualisation systems. We are currently developing a software system that composes multiple single cell solvers to create a tissue solver.

Keywords—Field Description, Field Representation, Field Visualisation, Data Interchange, Model Integration

## I. INTRODUCTION

TODAY'S computer models are extensively used to investigate biological systems at scales from the molecular to the whole organism [1]. Many of these systems can be described in terms of fields—spatially and temporally varying scalar, vector and tensor properties. For example, the spatial variation of muscle fibers is a vector field, the spatial and temporal variation in temperature of an organ is a scalar field, and the distribution of stress across muscle tissue is a tensor field. Fields can come from experimental measurements, results of models or mathematical functions. The uses of fields are numerous and include interchange between model solvers and visualisation systems, interchange between solvers, representation of experimental data, and as a convenient abstraction within solvers for mesh generation and refinement.

The results of a solver are fields that can be read and then displayed by a visualisation system such as Visiome [2]. Visiome maps fields to vertex properties such as colour, texture and position. An advantage of this method is that the visualisation system is decoupled from the model solver. We can change visualisation systems without having to change the solver.  

Many kinds of models and solvers need to interchange information when simulating complex biomedical systems. Models are chained together by making the output from one model the input to another model. Using a common field representation for both and input and output of solvers simplifies model chaining.

Fields based on experimental data can be compared to output fields from a solver to assess the fidelity of a model. They can also be used as parameters to a model.

Dynamic mesh refinement can be facilitated by using fields internally in a solver. The mesh can be made finer by adding nodes or coarser by dropping nodes. The time axis is treated as any other axis allowing adjustment of time step interval for durations and regions of interest.

In this paper we present a method to represent fields of both analytical and numerical nature, along with several applications where we have used fields.

## II. FIELD DEFINITION

A field is a mathematical function that describes the variation of a property over space and time.

\[f(x_{1}\ldots x_{n}) = U(x_{1}\ldots x_{n})\in D\subseteq \mathbb{R}^{n}\]

where \(n\) is the dimension of the field, \(U\) can be a scalar, a vector or a tensor and \(D\) is the domain of the field. For example, for a model of the sinoatrial node (SAN) that has two spatial dimensions \((x\in [0\ldots 3]\mathrm{mm}\) and \(y = [0\ldots 6]\mathrm{mm})\) and a temporal dimension \((t\in [0\ldots 15]\mathrm{sec})\) , we use a three dimensional scalar field to describe the variation in \(Ca^{2 + }\) concentration over the domain of the model.

## III. FIELD DESCRIPTION

There are two common ways to describe a field: analytically and numerically. For example, a simple one dimensional field can be described analytically as

\[f(x) = x^{2}\quad x\in [0\ldots 3]\]

An analytic description of a field is commonly used for the description of model behavior. A numerical description of a field is useful when working with experimental results or results from numerical models. A numerical description

of a field is a set of points in the domain of the field and the associated value of the field at those points. Elsewhere, the field is approximated using some interpolation method. Figure 1a shows a set of points in a two dimensional space (the XY plane) and the associated values of the field in the Z axis. These points and values are used to define the field shown in figure 1b along with a linear interpolation method over a Delaunay triangulation [3]. The field's domain is defined by the convex hull of the set of points.

> **Image description.** A technical diagram consisting of two stacked panels, (a) and (b), illustrating the representation of a two-dimensional numerical field using data points and subsequent interpolation. Both panels utilize a 3D coordinate system with labeled axes.
>
> Panel (a) displays the raw data points defining the field. This panel shows numerous vertical black lines, or "spikes," scattered across the base plane (XY plane). Each spike represents a data point, where the height of the spike corresponds to the value of the field along the Z-axis. The X, Y, and Z axes are clearly labeled, establishing the spatial domain. The caption below this panel reads: "(a) The defining points in the field represented as spikes emanating from the XY plane."
>
> Panel (b) shows the resulting field after interpolation. This panel depicts a continuous, irregular surface rendered in shades of gray. This surface is constructed from a mesh of interconnected triangular facets, which the caption identifies as a Delaunay triangulation. The surface follows the general shape defined by the spikes in panel (a). The X, Y, and Z axes are maintained and labeled identically to panel (a). The caption below this panel reads: "(b) The field with Delaunay triangulation of the surface and linear interpolation forms the surface."
>
> Overall, the image visually demonstrates the process of taking discrete, scattered data points (spikes) and using linear interpolation over a Delaunay triangulation to create a continuous, smooth surface representation of a numerical field.

<center>Fig. 1. A two dimensional numerical field described using a 2D linear interpolation and randomly scattered data. </center>

Domains can be described as intervals, rectangles, convex hulls or giving the boundary as arbitrary closed curves or surfaces. An arbitrary 2D curve can be described by a 1D field of 2D vectors giving the mapping from parameter space to 2D space. Similarly, a 3D surface is described by a 2D field

of 3D vectors. For example, the domain

\[D = \{(x,y)|x^{2} + y^{2}\leq 1\}\]

(the unit disc) can be described by the field giving its boundary:

\[f(\theta) = (\cos \theta ,\sin \theta)\quad \theta \in [0\ldots 2\pi ]\]

## IV. ABSTRACTION AND REPRESENTATION OF FIELDS

We propose the layered architecture illustrated in figure 2. At the top level, the Abstract Field Layer (AFL) provides the field abstraction together with a set of common field operations. The next level is the concrete representation of the field for storage and interchange. Our architecture allows different formats to be used for this layer such as the Field Representation Language (FRL) (see section IV- B) or FieldML [4]. This approach provides an abstraction of the field concept, independent of the underlying field representation.

> **Image description.** A block diagram illustrating a two-layered architectural structure designed for unified field interchange. The diagram is composed of two primary horizontal layers, representing an abstraction hierarchy.
>
> The top layer is a large, light-colored rectangular block labeled "Abstract Field Layer." This layer represents the high-level abstraction, providing a unified interface for field operations.
>
> The bottom layer is a second, equally large rectangular block that contains several smaller, distinct blocks representing concrete field representations. These concrete formats are arranged horizontally within the lower layer. The specific representations visible are:
> *   "FRL" (Field Representation Language)
> *   "XML"
> *   "FieldML"
> *   "Other Field Rep." (Other Field Representations)
>
> The visual arrangement suggests that the concrete representations in the bottom layer serve as the underlying implementation details for the abstract concepts defined in the Abstract Field Layer above them, creating a clear separation between the abstract field concept and its specific storage or interchange formats. The entire diagram is labeled "Fig. 2. A two layered architecture for unified field interchange."

<center>Fig. 2. A two layered architecture for unified field interchange. </center>

### A. The Abstract Field Layer (AFL)

The AFL provides a set of common field operations such as the storage and retrieval of fields from disk, the specification of the fields, and the retrieval of the value of a field at a given point.

Our implementation of AFL provides a library of common interpolation methods which should prove sufficient for most applications involving fields of up to 4 dimensions. We do not attempt to provide implementations of all conceivable interpolation methods, but do provide an interface for extensions.

Our implementation of the AFL provides for the storage and retrieval of fields using the FRL described in the next section. The AFL provides an interface for the addition of other field representation formats.

### B. The Field Representation Language (FRL)

In keeping with the layered architecture described above, we have developed the FRL as an efficient means for field representation and storage. The FRL easily accommodates

> **Image description.** A monochromatic, three-dimensional computational visualization representing scalar fields from a simulated sinoatrial node (SAN) model. The image displays an irregular, organic shape, suggesting a cross-section of biological tissue.
>
> The overall structure is characterized by an asymmetrical, flattened domain with a complex, uneven boundary. The visualization is rendered in shades of gray, utilizing shading and highlights to convey depth and a 3D perspective.
>
> The visual content is dominated by two distinct regions:
> 1.  **Central Feature:** A prominent, roughly spherical or dome-shaped structure is positioned near the center of the domain. This central mass is rendered in a smoother, medium gray tone, appearing relatively solid and uniform compared to the surrounding tissue.
> 2.  **Surrounding Tissue:** The area surrounding the central feature is highly textured and irregular. This outer tissue is depicted in darker shades of gray, with a rough, granular, or "textured" surface that suggests a complex internal structure or field variation.
>
> Based on the provided context, this visualization represents three scalar fields:
> *   The overall shape and contours represent the membrane potential field (Z-axis).
> *   The distinct textures visible on the surface of the tissue represent the cell type field.
> *   The central, smoother region likely represents a specific cluster or region of interest within the SAN model.
>
> The image is a technical representation of numerical simulation results, designed to visually map complex data fields onto visual properties like shape, texture, and shading.

<center>Fig. 3. A visualisation of two-dimensional scalar fields from a SAN model. The Z-axis shows the membrane potential field and textures show the cell type field. </center>

both analytical and numerical field descriptions efficiently using XML and a binary data format.

In principal, it is possible to store all the information needed to represent a field in an XML based language. However, numerically defined fields can require the storage of millions of floating point numbers. XML would take an order of magnitude more space to store numerical information than a binary format. Therefore, FRL uses XML where possible, and the binary Dense Data Format (DDF) [5] to store the numerical data.

The IUPS Physiome Project [1][6] has proposed FieldML, an XML based language, to describe fields. When a complete FieldML specification becomes available, it will also be possible to use FieldML to represent fields, as shown in figure 2.

### V. USING FIELDS

### A. Visualising Model Results

Many numerical modelling systems provide basic visualisations at best. Researchers settle for such visualisations because of the problems involved in interchanging results with more powerful visualisation systems. Using field representations solves these problems. We have previously presented a powerful visualisation toolkit for biomedical models called Visiome [2]. Visiome can read and visualise fields using AFL. Other visualisation tools such as VTK [7] and OpenDX [8] could also be used to visualise fields.

Figure 3 shows a visualisation of three two- dimensional scalar fields from a simulation of the sinoatrial node (SAN) [9]. The Z- axis shows the membrane potential field, textures show the cell type field, and colour (not reproduced in this figure) shows the region of currently active tissue [10]. The fields displayed in the figure were read from an FRL file. The Visiome toolkit allows users to map fields to visualisation properties such as colour, opacity and texture. Several fields can be shown simultaneously by mapping them to different visualisation properties.

### B. Combining Different Models

We are developing a three dimensional fractal model of the arrangement of blood vessels in a liver tumour [11] (see figure 4a). This model is used to determine the spatial distribution of microspheres for Ferromagnetic Embolisation Hyperthermia (FEH) [12]. Simulated microspheres injected into the circulation are lodged in blood vessels narrower than themselves. These are accumulated in voxels to produce a three dimensional field of microsphere concentrations (see figure 4b). This field is the input to a heat- transfer model of FEH treatments [12].

> **Image description.** A complex three-dimensional scientific visualization, likely representing scalar fields from a biological simulation, set against a dark background.
>
> The composition is dominated by two main visual elements: a large, curved teal surface and a highly intricate, branching network.
>
> The background is uniformly dark, providing high contrast for the visualized data. Occupying the upper portion of the frame is a large, smooth, curved surface rendered in a deep teal or dark green color. This surface appears to define a boundary or a field upon which the primary data structure is projected.
>
> The central focus of the image is a dense, reddish-brown, filamentous structure. This structure is highly irregular and exhibits a complex, fractal-like branching pattern, resembling a vascular network or a biological tree. It is composed of numerous thin, interconnected lines that branch out from a central mass, spreading across the visualized space. The reddish-brown color and subtle shading give the network a strong sense of three-dimensional depth.
>
> Based on the provided context, this visualization represents two-dimensional scalar fields from a sinoatrial node (SAN) model. The reddish-brown, branching network represents the membrane potential field (the Z-axis), while the textures (though not explicitly detailed in the visual rendering, they are mentioned in the context) represent the cell type field. The overall arrangement illustrates the spatial distribution and complexity of these fields within the simulated biological model.

<center>(a) A 3D vasculature tree from a fractal model of a spherical liver tumour. </center>

> **Image description.** A three-dimensional scientific visualization depicting a complex, irregular scalar field, likely representing biological tissue from a computational model. The image is dominated by a textured, organic mass set against a dark background.
>
> The central element is a large, amorphous structure composed of varying shades of gray, ranging from light gray to near-white, interspersed with darker gray and black areas. This structure is highly textured, appearing granular, bumpy, and composed of numerous interconnected, irregular subunits, suggesting a cellular or tissue-like arrangement. The overall shape is non-uniform and sprawling, resembling a cluster of cells or a section of biological tissue.
>
> The visualization is presented in a dark, void-like environment. In the upper right quadrant, a curved, light-colored line is visible, suggesting a representation of a coordinate system or a plane within the 3D space. The varying shades of gray within the main structure represent the data of the scalar field, which, according to the context, corresponds to the membrane potential field of the simulated sinoatrial node (SAN) model.
>
> The image effectively uses grayscale to convey the distribution and intensity of the simulated data across the modeled tissue, with the texture providing a visual representation of the underlying cell type field. The overall aesthetic is characteristic of advanced biomedical modeling and visualization software, such as the Visiome toolkit mentioned in the context.

<center>(b) The 3D scalar field of microsphere concentration in the region of the vasculature model. </center>

The solvers for these two models are inherently different. The first is a fractal stochastic solver while the second is a finite element numerical solver. Combining the two solvers into one tool would sacrifice modularity and flexibility. Using fields we can develop each of the solvers separately, inter

changing the information easily between the models. We also visualise the intermediate microsphere concentration field. Since the input to the finite element solver is the microsphere concentration at the location of each node, without using the field abstraction, any changes to the finite element model would mean replicating those changes to the fractal solver.

## VI. DISCUSSION

Researchers can benefit from the use of fields as an interchange between modelling systems and between modelling and visualisation systems. The standardisation of a field description language is a necessary step in the development of an effective interchange. Together with the language, software tools to use with that language must also be developed. In this paper we discussed solvers and visualisation tools, but authoring tools and field verification tools will make any field standard more appealing to biomedical researchers. A standard field description will also enable the creation of a field repository which will let researchers share models, experimental results and any other data that is expressed as fields.

We are developing a software system that uses fields and cell models to create tissue models. Single cell solvers are created from a CellML document by a solver generator. Each instance of a cell solver represents a node in a tissue solver. A tissue solver connects all the nodes with a mesh and parameterises the nodes from fields via AFL. Each time step is computed via the cell solvers and the results are stored in a field. That field then serves as the input for the next time step. The result of repeating this process is a field that can be visualised and stored. Figure 5 shows how the subsystems of the tissue solver interact. Note that FRL is used for input of initial conditions and parameters and for output of results. We are also developing an interactive field visualisation tool that will show several fields simultaneously.

## VII. CONCLUSION

In any computational framework such as the IUPPS Physiome Project [1], which integrates models of different types and scales, a method for interchanging data is needed. Fields are already used in biomedical models even if only implicitly. There are already much experimental data and model results that can be expressed as fields. This makes fields a natural medium for interchange between models and various sources of data.  

text[[87, 820, 489, 862], [506, 128, 822, 142]]
Concurrent with the development of a concrete representation of fields (FRL), we are developing an abstract representation (AFL) that can be used independently of FRL. This allows us to use fields for a cornucopia of applications.

> **Image description.** A block diagram illustrating the interaction between various subsystems of a tissue solver, representing a computational architecture. The diagram is organized into two main vertical columns: data/input formats on the left, and processing/solver components on the right.
>
> The left column contains four rectangular blocks representing data formats and abstraction layers:
> 1.  `CellML Document` (Top)
> 2.  `FRL Document` (Middle)
> 3.  `AFL` (A large, central block, serving as the primary interface)
> 4.  `FRL Document` (Bottom)
>
> The right column contains three rectangular blocks representing the computational solvers:
> 1.  `Solver Generator` (Top)
> 2.  `Single Cell Solver` (Middle)
> 3.  `Tissue Solver` (Bottom)
>
> The interactions between these components are shown through arrows:
>
> *   **Solver Generation Flow:** An arrow points from the `CellML Document` to the `Solver Generator`. A subsequent downward arrow connects the `Solver Generator` to the `Single Cell Solver`, and another downward arrow connects the `Single Cell Solver` to the `Tissue Solver`, indicating a hierarchical construction or flow of components.
> *   **AFL as the Central Interface:** The `AFL` block acts as the central hub, interacting bidirectionally with all three solver components:
>     *   A bidirectional arrow connects `AFL` and the `Solver Generator`.
>     *   A bidirectional arrow connects `AFL` and the `Single Cell Solver`.
>     *   A bidirectional arrow connects `AFL` and the `Tissue Solver`.
> *   **Data Flow:** The `FRL Document` (middle) has an arrow pointing to `AFL`, and a downward arrow connects `AFL` to the `FRL Document` (bottom), suggesting that FRL is used for input parameters and output results managed through the AFL interface.
>
> Overall, the diagram visually represents how data formats (CellML, FRL) and the AFL abstraction layer are used to generate and connect the hierarchical computational solvers (Solver Generator, Single Cell Solver, Tissue Solver) to model tissue systems.

<center>Fig. 5. Interaction between subsystems of a tissue solver that uses CellML and FRL to describe tissue behaviour. </center>

---

*Transcribed with OCR and VLMs; text, equations, and figure descriptions may contain mistakes.*
