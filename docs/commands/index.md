# Commands

## Image processing

Image processing commands work on [image planes](image-planes) manipulating the input image plane and forwarding the newly image to the command output.
ImageC provides a set of image processing algorithm for different use cases.

In general, image preprocessing serves to minimize the image noise as far as possible (maximizing the signal-to-noise ratio) in order to enable separation between the background and the signal.
An [object segmentation command](commands-object-segmentation) is issued after the image preprocessing.

:::{hint}
Image processing commands get an image as input and have a manipulated image as output.
:::

:::{toctree}
:maxdepth: 2

command_color_filter
command_rolling_ball
command_blur
:::

(commands-object-segmentation)=
## Object segmentation

The aim of object segmentation is to convert a grey-scale image into a binary image in such a way that all background areas are converted to black and all areas of interest are converted to a value other than black.

:::{toctree}
:maxdepth: 2

command_threshold
command_watershed
command_threshold_filter
:::


(commands-object-classification)=
## Object classification

Once objects are segmented, the resulting region of interests have to be classified.
Classification in ImageC is the process of converting regions of interest into objects, assigning each object to a class and cluster, and calculating object metrics.

ImageC provides an object classifier based on segmented images (e.g. after applying a threshold) and an AI classifier which can directly be applied to an image without the need of segmentation before.

:::{hint}
See chapter [classification](classification) for understanding the fundamentals.
:::

:::{toctree}
:maxdepth: 2

command_classifier
command_classifier_ai
:::