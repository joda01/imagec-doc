# Commands

## Image processing

Image processing commands work on [image planes](image-planes) manipulating the input image plane and forwarding the newly image to the command output.
ImageC provides a set of image processing algorithm for different use cases.

In general, image preprocessing serves to minimize the image noise as far as possible (maximizing the signal-to-noise ratio) in order to enable separation between the background and the signal.
An [object detection command](commands-object-detection) is issued after the image preprocessing.

:::{hint}
Image processing commands get an image as input and have a manipulated image as output.
:::

:::{toctree}
:maxdepth: 3

command_color_filter
:::