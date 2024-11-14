(classification)=
# Classification

The concept behind ImageC is to run pipelines containing image pre-processing and object segmentation steps with the goal of extracting regions of interest from the input images.
For each extracted [object](objects) the origin information: image, image channel, z-stack and t-stack are stored.
In Advanced, [objects](objects) need to be classified for object statistics calculation and later quantification.

For classification ImageC provides the annotations {guilabel}`Cluster` and {guilabel}`Class`.
Every object is annotated with exact one cluster and one class.


(clusters-and-classes)=
## Clusters and Classes

The first step before creating pipelines or starting the analysis is to define which clusters and classes are needed for object classification in your application.
Both can be done at the {guilabel}`Classification` tab in the left sidebar.

```{figure} images/screenshot_classification.png
:class: full-image
Classification tab
```

As a best practice, clusters should represent the image channels plus the necessary object pre-processing pipelines such as coloc.
ImageC provides a preset functionality.
Predefined sets of commonly used classification settings can be loaded instead of defining the clusters and groups yourself.
Each pre-defined classification set supplied with ImageC contains a unique ID stored with the set.
Any run performed with a classification set using the same ID can be compared.

(classification-presets)=
## Presets

ImageC also allows to create classification presets by selecting a preset from the drop down in the {guilabel}`Classification` tab.
A classification preset is a set of predefined clusters and classes which can be loaded and shared with others.
The idea behind a preset is making results easier comparable by using the same nomenclator for each analysis.
For that reason the editing of class and cluster name is locked when a preset is selected.

Using the {{icon_bookmark}} menu allows to create a new preset from an existing (removing the lock) and saving new presets based on the actual taken settings.  

Each preset provided by ImageC is identified by an unique identifier which is stored together with the preset.
This UID allows to reload the correct preset when settings are loaded.

:::{note}
It is recommended to use pre-defined classification presets to allow later comparison of results from different runs by different people.
:::
