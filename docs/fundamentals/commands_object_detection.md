(commands-object-detection)=
# Object detection

The aim of object detection is to convert a grey-scale image into a binary image in such a way that all background areas are converted to black and all areas of interest are converted to a value other than black.


## Threshold

:::{sidebar} Thresholding
Thresholding is a technique that aims to achieve an intensity value that is higher than the highest intensity value of the background noise and low enough to achieve the lowest intensity value of the regions of interest (ROIs).
Image preprocessing helps in advanced to reduce the background noise to get a sharp intensity border between background and foreground.

```{figure} images/threshold.drawio.svg
:class: full-image
```
:::

In case of using thresholds for object detection a threshold method must be chosen.
In most cases {guilabel}`Manual` with the appropriate minimum threshold is sufficient.
To find a good minimum value, the histogram of the preview image can be opened using the {{icon_externallink}} button.
Set the minimum threshold value to the smallest intensity value of the signal (most left value after the signal in the histogram).

Using a manual threshold applies the same threshold for all images of your set.

If the exposure ratios of the images are very different, it is possible that no uniform threshold value can be found for all images.
You can choose one of ImageC's auto-threshold algorithms for this.
The selected algorithm attempts to identify a minimum threshold value through the analysis of statistical properties inherent to the image in question. The precise methodology employed is contingent upon the specific algorithm utilized.  

### Handling control images without objects

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


## Fine tuning

Subsequent to the object detection stage, two fine-tuning options are available.

### Watershed algorithm

:::{sidebar} Object segmentation using watershed

Based on peaks extracted from the intensity values the valleys between the peaks are the borders for splitting the objects.

```{figure} images/watershed.drawio.svg
:class: full-image
```

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

### Overexposed threshold

:::{sidebar} Allowed threshold area
The intensity value at the maximum of the histogram of the image multiplied by the {guilabel}`Threshold filter` defines the area of allowed threshold values for the image.
If the min. threshold value is lower than the lowe bound of this area, the image id filtered out.

```{figure} images/threshold_histogram_filter.drawio.svg
:class: full-image
```

:::

To get comparable results in one experiment, it is common to use the same manual threshold value for all images.
Nevertheless, given the considerable range of exposure times for images, it is possible that the selected threshold value may prove insufficient for some images.
This leads to a kind of overexposed image after the threshold, in which the background is erroneously recognized as a signal.

To filter out images that are affected by this problem, ImageC offers a  {guilabel}`Threshold filter` filter.
In the event that the selected threshold value is less than the value observed at the maximum of the image histogram, multiplied by the aforementioned factor, the filter is applied.


%### Snap area

%This can be the case when calculating the colocalization between objects in different channels if the channels are not 100% exactly on top of each other.
%For such use cases a snap area can be activated.

%A snap area is defined as a circle painted around an object, with the centre of mass of the object positioned at the centre of the circle.
%It extends the object area with this circle in case of colocalization calculation. 