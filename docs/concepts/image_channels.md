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

This can be the case when calculating the colocalisation between objects in different channels if the channels are not 100% exactly on top of each other.
For such use cases a snap area can be activated.

A snap area is defined as a circle painted around an object, with the centre of mass of the object positioned at the centre of the circle.
It extends the object area with this circle in case of colocalisation calculation. 


## Object filtering

:::{sidebar} Circularity
Circularity describes the roundness of an object, with a perfect circle having a circularity of `1`. 
The circularity of an object is calculated as follows:

:::{math} c = \frac{4 \cdot pi \cdot AreaSize}{perimeter^2}

:::

Despite all efforts in pre-processing and detection scribing, unwanted objects or noise artifacts can still remain.
With the help of object filtering these objects can be removed.

ImageC provides size and circularity filter which are applied after the detection step.
Objects that do not match the applied filter criteria are marked as invalid and grey in the live preview.
Invalid objects are skipped for all statistical calculations.

(tetraspeck-removal)=
### Tetraspeck removal

A special object filter is the Reference spot removal filter.
To activate this filter select a channel with channel type {guilabel}`Reference spot` from the dropdown.
ImageC will mark as invalid all objects that overlap with the objects in the selected reference spot channel.

(image-filtering)=
## Image filtering

Given the extensive nature of the experiment, comprising thousands of images, it is possible that some of the images may be erroneous.

ImageC provides functions which try to find such erroneous images and can exclude them from the overall statistics.
In detail two heuristics are available: 

- Find noisy images
- Find overexposed threshold

The {guilabel}`Image filter mode` enables the user to select whether the entire image should be designated as invalid or merely the channel in which the filter is applied.


(filter-noisy-images)=
### Noisy images

The term "noise" is used to describe the presence of random, distributed pixels with varying intensity values across an image.
If noise is incorrectly recognized as an object, this manifests itself in the recognition of a large number of small objects.
With the {guilabel}`Max object` filter ImageC provides an setting which marks all images/channels as invalid where the number of detected objects is higher than this value. 

:::{hint}
Estimate what the largest number of valid objects in an image will be and set this value above it.
:::

### Overexposed threshold

:::{sidebar} Allowed threshold area
The intensity value at the maximum of the histogram of the image multiplied by the {guilabel}`Histogram threshold factor` defines the area of allowed threshold values for the image.
If the min. threshold value is lower than the lowe bound of this area, the image id filtered out.

:::{figure} images/threshold_histogram_filter.drawio.svg
:class: full-image


:::

To get comparable results in one experiment, it is common to use the same manual threshold value for all images.
Nevertheless, given the considerable range of exposure times for images, it is possible that the selected threshold value may prove insufficient for some images.
This leads to a kind of overexposed image after the threshold, in which the background is erroneously recognized as a signal.

To filter out images that are affected by this problem, ImageC offers a  {guilabel}`Histogram threshold factor` filter.
In the event that the selected threshold value is less than the value observed at the maximum of the image histogram, multiplied by the aforementioned factor, the filter is applied.

(cross-channel-measurement)=
## Cross channel measurement

ImageC offers the capability to utilize the object areas (regions of interest) from one channel and perform measurements in a different channel based on these regions.
In