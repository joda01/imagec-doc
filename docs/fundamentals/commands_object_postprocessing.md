(commands-object-post-processing)=
# Object post processing


## Object filtering

:::{sidebar} Circularity
Circularity describes the roundness of an object, with a perfect circle having a circularity of `1`. 
The circularity of an object is calculated as follows:

```{math}
c = \frac{4 \cdot pi \cdot AreaSize}{perimeter^2}
```
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

```{figure} images/threshold_histogram_filter.drawio.svg
:class: full-image
```

:::

To get comparable results in one experiment, it is common to use the same manual threshold value for all images.
Nevertheless, given the considerable range of exposure times for images, it is possible that the selected threshold value may prove insufficient for some images.
This leads to a kind of overexposed image after the threshold, in which the background is erroneously recognized as a signal.

To filter out images that are affected by this problem, ImageC offers a  {guilabel}`Histogram threshold factor` filter.
In the event that the selected threshold value is less than the value observed at the maximum of the image histogram, multiplied by the aforementioned factor, the filter is applied.

(cross-channel-measurement)=
## Cross channel measurement

ImageC offers the capability to utilize the object areas (regions of interest) from one channel and perform measurements in a different channel based on these regions.
Two cross channel measurement options are available: {guilabel}`Cross channel intensity` and {guilabel}`Cross channel count`.

To perform a cross-channel measurement, enter one or more comma-separated channel or slot indexes in the text box.
Allowed pattern is: {regexp}`[0-9][A-F]`.

### Cross channel intensity

Takes the ROIs from the source and measures the intensity value of this source in an other channel.
One potential application of this methodology is to utilize the identified cell regions to quantify the mean intensity of these regions within an EV channel.

### Cross channel count

Takes the ROIs from the source and counts how many ROIs within that source ROI are found in another channel.
One potential application of this approach would be to utilize the detected cell areas to enumerate the number of identified EVs (spots) within these regions.
