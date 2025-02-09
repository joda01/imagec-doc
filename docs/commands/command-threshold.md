(command-threshold)=
# Threshold

:::{sidebar} Thresholding
Thresholding is a technique that aims to achieve an intensity value that is higher than the highest intensity value of the background noise and low enough to achieve the lowest intensity value of the regions of interest (ROIs).
Image preprocessing helps in advanced to reduce the background noise to get a sharp intensity border between background and foreground.

```{figure} images/threshold.drawio.svg
:class: full-image
```
:::

```{figure} images/threshold-screenshot.png
:class: tiny-image
```

Threshold is an object segmentation method with the goal to separate foreground objects from background objects.
Applying a threshold to an image converts the grey scale image to a binary image.
All pixels with an intensity value below the selected threshold value are converted to zero (black), the others are to 65535 (white).

Using the correct threshold will have a significant effect on the quality of the result.
The challenge is to find a threshold value that is high enough to suppress the background noise but not too high as to not remove objects of interest.
Looking on the histogram of an image can help to find a good starting point when using {guilabel}`Manual` threshold value.

Set the minimum threshold value to the smallest intensity value of the signal (most left value after the signal in the histogram).

:::{hint}
Using the {{icon_external_link}} button to open the advanced preview.
The histogram of the image is displayed in the left image pane.
:::

:::{note}
Set the minimum threshold value to the smallest intensity value of the signal (most left value after the signal in the histogram) as a good starting point.
:::

:::{hint}
See also section [threshold filter](command-threshold-filter).
:::

## Maximum threshold

Using a minimum thresholds sets the minimum signal intensity to segment an object.

However there may be use cases having different objects in an image with different signal intensity values.
Using a max threshold allows to limit the maximum signal intensity for segmenting an object too.
Together with the minimum threshold, the maximum threshold can be used either for more detailed object differentiation or, for example, to extract the background instead of the objects when the minimum threshold is set to zero.

:::{note}
A object is only segmented if the signal value is between minimum threshold value and maximum threshold value.
:::

(command-threshold-threshold-classes)=
## Threshold classes

In addition to only separating background and foreground using a minimum and maximum threshold, ImageC also allows more than one threshold to be applied to an image.

Use the {{icon_add}} button in the Threshold dialogue box to define additional thresholds for the image.
A threshold class must be selected for each defined threshold in order to distinguish between objects segmented with different threshold values.

Under the hood, ImageC assigns each threshold class to a well-defined pixel value in the binary image, starting from 65535 (full white) down to one.
Based on this value the later on classifier is able to distinguish the segmented objects.

:::{note}
Multiple thresholds are assigned to threshold classes, allowing different objects to be detected depending on their signal strength.
:::

## Auto threshold

Using a manual threshold applies the same threshold for all images of your set.

If the exposure ratios of the images are very different, it is possible that no uniform threshold value can be found for all images.
You can choose one of ImageC's provided auto-threshold algorithms for this.
The selected algorithm attempts to identify a minimum threshold value through the analysis of statistical properties inherent to the image in question. 
The precise methodology employed is contingent upon the specific algorithm utilized.  

### Minimum threshold in combination with auto threshold

Auto thresholds can be effective if the preprocessing steps are sufficiently robust in removing background noise.
However it is a common practice in research to include control images devoid of any objects as samples.
Since the auto threshold algorithms are designed to find an upper bound that separates background from signal, these algorithms will also find such a bound in an empty image due to noise.
Applying an auto threshold algorithm to an empty noise image will lead to the segmentation of noise.

It is therefore strongly advised that a minimum threshold value exceeding zero is set, even when an auto threshold method is employed.
ImageC will use the chosen minimum threshold as a lower bound.
If the auto threshold algorithm calculates a threshold value below the lower bound, ImageC will set it to the minimum value.

It is advisable to select an empty control image (an image without an object) from the list. 
By using the live preview and the histogram, it is possible to determine the intensity value of the background noise and set a suitable minimum value for the threshold.


:::{hint}
In the event that an auto threshold algorithm is employed, it is strongly recommended to establish a minimum threshold. 
This is to prevent the occurrence of false positive detection in images that lack objects, given that such images would otherwise be included in the analysis.
:::
