(classification)=
# Classification

The concept behind ImageC is to run pipelines containing image pre-processing and object detection steps with the goal of extracting regions of interest from the input images.
For each extracted object the origin information: image, image channel, z-stack and t-stack are stored.
In Advanced, objects need to be classified for object statistics calculation and later quantification.

For classification ImageC provides the labels {guilabel}`Clusters` and  {guilabel}`Classes`.
Every object is assigned to exact one cluster and class.


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

(image-channels)=
## Image channels

:::{sidebar} Image plane

An image may comprise one or more C (channels), with each channel in turn consisting of a series of T (time) stacks, and these in turn consisting of a series of Z stacks.

The combination channel, Z stack (z) and time stack (t) is called image plane.
ImageC is able to process each image plane of an image, based on the taken project and pipeline settings.


```{image} images/image_channels.drawio.svg
:class: full-image
```

:::


ImageC is able to process every channel of an image based on the settings taken in the {guilabel}`Project` tab and the pipeline.
However it is possible to either process each Z stack image individually or using a projection algorithm to combine all images of a Z stack to a single stack image.
For the time stack it is either possible to analyze exact one image of a T stack or to analyze the whole time series.

The image plane information is stored with each object extracted from that plane.
If a Z-projection is used, the Z-stack index is always assumed to be 0.
