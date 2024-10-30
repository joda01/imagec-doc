(classification)=
# Classification

The concept behind ImageC is to run pipelines containing image pre-processing and object detection steps with the goal of extracting regions of interest from the input images.
For each extracted object the origin information: image, image channel, z-stack and t-stack are stored.
In Advanced, objects need to be classified for object statistics calculation and later quantification.

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

However ImageC also allows to create own presets which can be shared with others using the {{icon_bookmark}} menu.

:::{note}
It is recommended to use pre-defined classification presets to allow later comparison of results from different runs by different people.
:::

## Class hierarchy

For the future it is planned to allow class hierarchies.
Class hierarchies should address the need of a more fine granular classification of objects without loosing the scope.
Statistical questions like: Give me the number of found cells! or Give me the number of found hec cells! are possible then.