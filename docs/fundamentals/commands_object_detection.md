(commands-object-segmentation)=
# Object segmentation

The aim of object segmentation is to convert a grey-scale image into a binary image in such a way that all background areas are converted to black and all areas of interest are converted to a value other than black.


## Threshold



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