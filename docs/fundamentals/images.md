(images)=
# Images

:::{sidebar} Image plane

An image may comprise one or more C (channels), with each channel in turn consisting of a series of T (time) stacks, and these in turn consisting of a series of Z stacks.

The combination channel, Z stack (z) and time stack (t) is called image plane.
ImageC is able to process each image plane of an image, based on the taken project and pipeline settings.


```{image} images/image_channels.drawio.svg
:class: full-image
```

:::

Microscope images usually consist of several individual images that are summarized in a common image file.
This individual images are named image planes.
Each plane is identified by its channel, z-stack and time stack.

ImageC is able to access each image plane of an image and process these planes individually based on the taken project and pipeline settings.

## Image plane processing

Within a pipeline, select the image channel to be loaded as the starting point for this pipeline.
The channel is a number from 0 to x.
A separate pipeline must be created for each channel required for processing.

In a second step it is necessary to define how z-stacks and time stacks should be processed.
These settings can be taken in the {guilabel}`Project` tab of ImageC.
It is possible either to process each Z-stack image individually, using a projection algorithm to combine all the images of a Z-stack into a single stack image, or to analyze exactly one image of the Z-stack.
If a projection algorithm is to be used, the algorithm to be used must be defined within the individual pipeline.
For the time stack it is possible either to analyze one image of a time stack or to analyze the whole time series.

