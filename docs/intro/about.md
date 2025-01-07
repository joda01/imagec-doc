(about-imagec)=
# About ImageC?

**ImageC a open source software for high throughput bioimage analysis**

```{figure} images/screenshot_open_pipeline.png
:class: full-image
```

ImageC as a direct successor of [EVAnalyzer](https://github.com/joda01/evanalyzer) {{icon_eva}} provides an **easy to use graphical user interphase (GUI)** enabling the compilation of image processing pipelines for **Object detection and Quantification** from various types of microscopic images, particularly Brightfield images, fluorescence images and Histological images. 
It was optimized within a group focused on nanovesicles and therefore offers a powerful set of templates optimized for **single vesicle quantification** in diverse in vitro and in vivo settings. 


## Is ImageC suitable for me?

There are diverse commercial or open access image processing applications.
What is special about ImageC? 
Is it the best program to help me to quantify my imaging data?

### High throughput analysis of biological images

````{grid} 3
:gutter: 2

:::{grid-item-card} 🚀 Fast processing pipelines for big data sets
:columns 4

ImageC is implemented in C++, one of the fastest programming languages and efficiently uses all available CPU resources (multi threading support).
With the focus on hight throughput analyzes, ImageC allows processing times down to 0.2 seconds per image, allowing the analysis of thousands of images in a reasonable time.
:::


:::{grid-item-card} 🚀 Analysis of fluorescence and brightfield images
:columns 4

ImageC enables object detection and quantification in fluorescence images.
Analysis and cross channel quantification can be applied to any number of channels.
e.g. Measurement of fluorescence intensity per cell.
:::


:::{grid-item-card} 🚀 Analysis of histological images
:columns 4

ImageC enables the analysis of huge histological images, taken by fluorescence and light microscopy.
e.g.: Color picker enables to distinguish cellular compartments based on color.
:::


:::{grid-item-card} 🚀 BioFormats support
:columns 4

All common image formats used by different microscope manufacturers are supported thanks to BioFormats integration.
:::

:::{grid-item-card} 🚀 OME-XML support
:columns 4

ImageC automatically extracts underlying image infos (e.g. channel infos, Z-stack infos, etc. ) which allows to directly use multi channel (c, t and z-stack) images.
:::

````

### Big data processing / organization

````{grid} 3
:gutter: 2

:::{grid-item-card} 🚀 Big data organization
:columns 4

ImageC stores all the pipeline results into an integrated in-process SQL database (DuckDb) using a predefined data structure.
The flexibility of the database matched with an easy to use GUI enables basic data postprocessing and comparison.
:::

:::{grid-item-card} 🚀 Data export
:columns 4

The data are stored as an compressed database file and can be exported for further processing to R or Excel.
Custom export templates can be used for the creation of individual data sets.
:::


:::{grid-item-card} 🚀 Image/Data grouping
:columns 4

Automated image grouping based on well formats, image names using regex or directory structure can help to organize data output. 
AVG, MEDIAN, MAX, MIN, STDEV, SUM and CNT are automatically calculated from multiple images within a group.
:::

:::{grid-item-card} 🚀 Image/Data Filtering
:columns 4


ImageC allows to define data filters, removing images from the report based on customized criteria.
e.g. remove Images without cells
:::


:::{grid-item-card} 🚀 Heatmaps
:columns 4

ImageC can generate heatmaps of images or image groups (e.g. plates. wells), enabling a quick assessment of the data. 
:::


````

### Flexible / easy creation of image processing pipelines with inclusion of AI

````{grid} 3
:gutter: 2


:::{grid-item-card} 🚀 Pipeline creation 
:columns 4

ImageC enables the creation of individual image processing pipelines for object detection.
A set of widely used image processing algorithms ported from ImageJ, including background subtraction algorithms, filtering, edge detection and manual as well as auto-threshold are implemented and can be used for pipeline creation.
:::

:::{grid-item-card} 🚀 Live preview
:columns 4

ImageC offers a live preview enabling to monitor the impact of all image processing steps within the pipelines and thereby provides transparent and understandable object detection. 
:::


:::{grid-item-card} 🚀 AI driven object detection
:columns 4

In addition to classical image processing and thresholding algorithms ImageC supports object detection and classification based on AI.
ImageC supports the ONNX container format with net hight and with of 640 x 640 and a stride size of 3.
:::


:::{grid-item-card} 🚀 Reuseable and sharable pipelines
:columns 4

ImageC is designed for reproducible image analysis.
:::


:::{grid-item-card} 🚀 Generation of control images
:columns 4

ImageC generates user defined control images, for documentation and internal control.
:::

:::{grid-item-card} 🚀 Pipeline templates
:columns 4

[EVAnalyzer](https://github.com/joda01/evanalyzer) {{icon_eva}} and its successor ImageC where created within a research group focused on extracellular vesicles.
ImageC provides powerful pipelines especially for single vesicle imaging applications.
:::


````

### Work in progress and future perspective

````{grid} 3
:gutter: 2


:::{grid-item-card} 🔧 Analysis of videos
:columns 4

ImageC is prepared for multi channel image processing.
In future releases the support for time stack analysis (videos) including object tracing will be supported.
:::

:::{grid-item-card} 🔧 Distance calculator
:columns 4

It is planned to implement a distance calculator algorithm which allows to calculate the distance between multiple objects.
:::


:::{grid-item-card} 🔧 Extend preprocessing algorithms
:columns 4

The set of supported preprocessing algorithms will be extended in future releases based on the user needs.
:::


:::{grid-item-card} 🔧 Formula in report viewer
:columns 4

In future releases it is planned to add basic mathematic operations in the data report viewer.
:::

````

