(command-classifier)=
# Classifier

:::{sidebar} Objects

Objects are extracted from a binary image representing thee regions of interest of the image.
For each extracted object a class is assigned and metrics are measured.
Objects are stored to the resulting database and can be used in further pipeline steps.

```{figure} images/classifier.drawio.svg
:class: full-image
```

:::


```{figure} images/classifier-screenshot.png
:class: small-image
```

The Classifier command is used to convert regions of interest, formally extracted from the image using a segmentation algorithm such as [Threshold](command-threshold), into objects, where each object is assigned to an object class, and metrics are calculated for each object.
[Classified](classification) objects are stored to the resulting database and can be used in further object-processing steps.


ImageC's classifier provides several filter methods which can be used to to filter out artefact.
All objects which match the filter criteria are assigned to the {guilabel}`match` class, objects not matching the filter criteria are assigned to the {guilabel}`no match`.
The filter can be set for each [threshold class](command-threshold-threshold-classes) individually.
This allows the classifier to assign each ROI of a [threshold class](command-threshold-threshold-classes) to a specific match and no match object class.
Use the {{icon_add}} button to add as many filters as needed.
As a rule, one filter for each threshold class is used.

:::{hint}
See section [Objects](objects) for more detailed information about object metrics.
:::
