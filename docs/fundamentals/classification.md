(classification)=
# Classification

The concept behind ImageC is to run pipelines containing image pre-processing and object segmentation steps with the goal of extracting regions of interest from the input images.
For each extracted [object](objects) the origin information: image, image channel, z-stack and t-stack are stored.
In Advanced, [objects](objects) need to be classified for object statistics calculation and later quantification.

For classification ImageC provides the annotations {guilabel}`Class`.
Every object is annotated with exact one class.


(classes)=
## Classes

The first step before creating pipelines or starting the analysis is to define which classes are needed for object classification in your application.
Use the {guilabel}`Classification` tab to make the classification settings.

```{figure} images/screenshot_classification.png
:class: full-image
Classification tab
```

Double-clicking on a {guilabel}`Class` cell opens a dialog. 
In addition to the color, the name for the class can be specified.
Using the `@` symbol allows to group classes for a better reading in the selection tab.

Instead of manually specifying all required classes, ImageC provides the ability to populate the classification settings from the image channel information.
Open the menu {{icon_menu}} and use the {guilabel}`Populate classes from image channel` option to let ImageC try to extract the classification settings from an image. 

(classification-presets)=
## Presets

ImageC also allows to create classification presets by selecting a preset from the drop down in the {guilabel}`Classification` tab.
A classification preset is a set of predefined classes which can be loaded and shared with others.
The idea behind a preset is making results easier comparable by using the same nomenclator for each analysis.
For that reason the editing of class names is locked when a preset is selected.

Using the {guilabel}`Save as template` option within the menu {{icon_menu}} allows to create a new preset from an existing (removing the lock) and saving new presets based on the actual taken settings.  

Each preset provided by ImageC is identified by an unique identifier which is stored together with the preset.
This UID allows to reload the correct preset when settings are loaded.

:::{note}
It is recommended to use pre-defined classification presets to allow later comparison of results from different runs by different people.
:::
