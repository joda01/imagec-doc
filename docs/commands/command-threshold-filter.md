(command-threshold-filter)=
# Threshold filter

:::{sidebar} Allowed threshold area
The intensity value at the maximum of the histogram of the image multiplied by the {guilabel}`Threshold filter` defines the area of allowed threshold values for the image.
If the min. threshold value is lower than the lowe bound of this area, the image id filtered out.

```{figure} images/threshold-filter.drawio.svg
:class: full-image
```

:::

```{figure} images/threshold-filter-screenshot.png
:class: tiny-image
```

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