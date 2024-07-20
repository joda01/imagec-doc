(image-channels)=
# Image channels

Clicking on an image channel in the {guilabel}`Overview panel` opens the Image Channel Settings panel.

:::{figure} images/screenshot_image_channel_settings.png
:class: full-image

:::

## Meta

The {guilabel}`Meta` section is used to specify some basic channel information.

The {guilabel}`Channel index` setting selects the image channel to process.
With {guilabel}`Channel type` the category of the channel is defined.
Nevertheless, the specific channel type has no impact on the analysis, with the exception of channels of the {guilabel}`Reference spot` type, which are analysed prior to the other channel types.

## Preprocessing

The {guilabel}`Preprocessing` section is used to specify the image processing algorithms which should be applied before object detection can be done.

All preprocessing steps are applied in the order displayed, from top to bottom, to the image.
In order to circumvent the algorithm, either select the option labelled "Off" or remove the value from the text field.

When changing some parameters of the preprocessing steps the preview image on the right-hand side is refreshed with the new settings applied.

The objective of the preprocessing stage is to eliminate noise from the image and position the objects of interest in a manner that facilitates their detection using the available object detection algorithms.
As the most prevalent approach to object segmentation, aside from artificial intelligence (AI), employs the use of thresholds, it is imperative to ascertain that the objects of interest exhibit a higher intensity value than the background subsequent to the implementation of the preprocessing steps.

:::{hint}
For a detailed description of the individual image processing steps navigate to the chapter [Advanced](advanced).
:::

:::{note}
In the actual ImageC version it is not possible to change the order of the preprocessing pipeline steps.
However in further releases this will be possible.
:::

## Detection

Following the application of the selected image processing algorithms from the preprocessing stage, ImageC then proceeds with the execution of an object detection and segmentation process.

ImageC provides two object segmentation options: {guilabel}`Threshold` and {guilabel}`Artificial intelligence`.

### Threshold

:::{sidebar} Thresholding
Thresholding is a technique that aims to achieve an intensity value that is higher than the highest intensity value of the background noise and low enough to achieve the lowest intensity value of the regions of interest (ROIs).
Image preprocessing helps in advanced to reduce the background noise to get a sharp intensity border between background and foreground.

:::{figure} images/threshold.drawio.svg
:class: full-image
:::

:::

In case of using thresholds for object detection a threshold method must be chosen.
In most cases {guilabel}`Manual` with the appropriate minimum threshold is sufficient.
To find a good minimum value, the histogram of the preview image can be opened using the {{icon_externallink}} button.
Set the minimum threshold value to the smallest intensity value of the signal (most left value after the signal in the histogram).

Using a manual threshold applies the same threshold for all images of your set.

If the exposure ratios of the images are very different, it is possible that no uniform threshold value can be found for all images.
You can choose one of ImageC's auto-threshold algorithms for this.
The selected algorithm attempts to identify a minimum threshold value through the analysis of statistical properties inherent to the image in question. The precise methodology employed is contingent upon the specific algorithm utilized.  

#### Handling control images without objects

Auto thresholds can be effective if the preprocessing steps are sufficiently robust in removing background noise.
However it is a common practice in research to include control images devoid of any objects as samples.
Since the auto threshold algorithms are designed to find an upper bound that separates background from signal, these algorithms will also find such a bound in an empty image due to noise.
Applying an auto threshold algorithm to an empty noise image will lead to the detection of noise.

It is therefore strongly advised that a minimum threshold value exceeding zero is set, even when an auto threshold method is employed.
ImageC will use the chosen minimum threshold as a lower bound.
If the auto threshold algorithm calculates a threshold value below the lower bound, ImageC will set it to the minimum value.

It is advisable to select an empty control image (an image without an object) from the list. 
By using the live preview and the histogram, it is possible to determine the intensity value of the background noise and set a suitable minimum value for the threshold.


:::{hint}
In the event that an auto threshold algorithm is employed, it is strongly recommended to establish a minimum threshold. 
This is to prevent the occurrence of false positive detection in images that lack objects, given that such images would otherwise be included in the analysis.
:::

(artificial-intelligence)=
### Artificial intelligence

In some cases, it may not be feasible to differentiate between the background and the signal based solely on intensity values.
Images of unlabeled brightfield cells may be such an example for difficult to detect objects using just thresholds.

:::{sidebar} AI models

ImageC supports AI models in ONNX format.
Compatible models can be downloaded from [imagec.org](https://imagec.org).
A manual how to train your own model can be found in the advanced chapter, section [AI training](ai-training).

:::
In such use cases, ImageC permits the utilization of artificial intelligence models for object segmentation as an alternative to thresholding techniques.

ImageC compatible models for object segmentation can be downloaded from [imagec.org](https://imagec.org) below the Download section.
Copy the downloaded model to the {file}`./path/to/ImageC/models` folder.
ImageC will load all models from this folder automatically on startup and provides them in the {guilabel}`AI model` dropdown for selection.

In contrast to the threshold, a minimum probability is now specified.
All detected object with a minimum probability higher than this value will be used.

:::{note}
AI based object segmentation is still in alpha phase.
It is safe to use but not feature complete yet.
:::

### Fine tuning

Subsequent to the object detection stage, two fine-tuning options are available.

#### Watershed algorithm

:::{sidebar} Object segmentation using watershed

Based on peaks extracted from the intensity values the valleys between the peaks are the borders for splitting the objects.

:::{figure} images/watershed.drawio.svg
:class: full-image
:::
:::

In applications with a high object density, it is no exception that two objects come very close or even touch each other.
When using threshold techniques for object segmentation, it is not possible to distinguish between two such near objects anymore.

Some algorithms have been developed with the specific aim of addressing this issue.
One of them is the Watershed algorithm which ported from [ImageJ](https://imagej.net/imaging/watershed) to ImageC for that reason.

The watershed algorithm employs a process of object segmentation based on the intensity values of the objects in question. 
In this context, the intensity values are interpreted as altitude, with the objective of identifying the valleys between the peaks.

When using AI as detection method, watershed algorithm is not usually required.

:::{note}
It is recommended that the watershed be activated only when necessary, as it is a highly complex algorithm that significantly reduces analysis time when activated.
:::

#### Snap area

:::{sidebar} Snap area

Two objects with snap area activated.

:::{figure} images/screenshot_snap_area.png
:class: small-image
:::
:::



This can be the case when calculating the colocalisation between objects in different channels if the channels are not 100% exactly on top of each other.
For such use cases a snap area can be activated.

A snap area is defined as a circle painted around an object, with the centre of mass of the object positioned at the centre of the circle.
It extends the object area with this circle in case of colocalisation calculation. 


## Object filtering

Despite all efforts in pre-processing and detection scribing, unwanted objects or noise artifacts can still remain.