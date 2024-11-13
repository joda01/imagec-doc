(commands-object-post-processing)=
# Object post processing


## Object filtering



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
