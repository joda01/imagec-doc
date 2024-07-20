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

:::{note}
In the actual ImageC version it is not possible to change the order of the preprocessing pipeline steps.
However in further releases this will be possible.
:::

When changing some parameters of the preprocessing steps the preview image on the right-hand side is refreshed with the new settings applied.

The objective of the preprocessing stage is to eliminate noise from the image and position the objects of interest in a manner that facilitates their detection using the available object detection algorithms.
As the most prevalent approach to object segmentation, aside from artificial intelligence (AI), employs the use of thresholds, it is imperative to ascertain that the objects of interest exhibit a higher intensity value than the background subsequent to the implementation of the preprocessing steps.


## Detection

Following the application of the selected image processing algorithms from the preprocessing stage, ImageC then proceeds with the execution of an object detection and segmentation process.

:::{sidebar} Thresholding
Thresholding is a technique that aims to achieve an intensity value that is higher than the highest intensity value of the background noise and low enough to achieve the lowest intensity value of the regions of interest (ROIs).
Image preprocessing helps in advanced to reduce the background noise to get a sharp intensity border between background and foreground.

:::{figure} images/threshold.drawio.svg
:class: full-image

:::

:::

ImageC provides two object segmentation options: {guilabel}`Thresholds` and {guilabel}`Artificial intelligence`.

### Thresholding

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

### Artificial intelligence