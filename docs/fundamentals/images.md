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


ImageC is able to process every channel of an image based on the settings taken in the {guilabel}`Project` tab and the pipeline.
However it is possible to either process each Z stack image individually or using a projection algorithm to combine all images of a Z stack to a single stack image.
For the time stack it is either possible to analyze exact one image of a T stack or to analyze the whole time series.

The image plane information is stored with each object extracted from that plane.
If a Z-projection is used, the Z-stack index is always assumed to be 0.
