(commands-image-processing)=
# Image processing

Image processing commands work on [image planes](image-planes) manipulating the input image plane and forwarding the newly image to the command output.
ImageC provides a set of image processing algorithm for different use cases.

In general, image preprocessing serves to minimize the image noise as far as possible (maximizing the signal-to-noise ratio) in order to enable separation between the background and the signal.
An [object detection command](commands-object-detection) is issued after the image preprocessing.

:::{hint}
Image processing commands get an image as input and have a manipulated image as output.
:::

## Color filter

```{figure} images/screenshot_command_color_filter.png
:class: small-image
```
:::

If the input image is an RGB 8-bit color image, the color image must first be converted to a grey scale image.
This conversion is done by the color filter command.
With this filter it is possible to define the color range containing the region of interests.
For each region of interest in a different color to extract a separate pipeline with a separate color filter must be created.

The resulting image is a gray scale image showing only the image regions filtered by the selected color range.
In a next step further image processing steps can be applied.


## Blur

## Intensity

## Rolling ball

## Median subtraction

## Edge detection