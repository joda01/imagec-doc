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

(image-planes)=
## Image planes

Within a pipeline, select the image channel to be loaded as the starting point for this pipeline.
The channel is a number from 0 to x.
A separate pipeline must be created for each channel required for processing.

In a second step it is necessary to define how z-stacks and time stacks should be processed.
These settings can be taken in the {guilabel}`Project` tab of ImageC.
It is possible either to process each Z-stack image individually, using a projection algorithm to combine all the images of a Z-stack into a single stack image, or to analyze exactly one image of the Z-stack.
If a projection algorithm is to be used, the algorithm to be used must be defined within the individual pipeline.
For the time stack it is possible either to analyze one image of a time stack or to analyze the whole time series.

## Image formats

ImageC can be used with a wide range of image formats, thanks to the open source library **Bio-formats**: <https://docs.openmicroscopy.org/bio-formats> which is shipped together with application.


:::{note}
ImageC is actually designed to read greyscale images in either 8-bit or 16-bit format or RGB colored images.
:::


(formats-ome)=
## OME xml

ImageC supports reading OME XML meta data stored beside image files.
OME specifies a structure how image meta can be shared in a standardized way.
ImageC tries to parse this XML data if it is found in an image and displays the meta data in a sidebar on the start screen.

The OME metadata contains not only image metadata for the end user, but also information about the number of channels and the channel order.
Therefore, OME metadata is mandatory if multi-channel images are to be processed.

ImageC assumes that only one channel is available if no OME metadata is found.

:::{hint}
For a full specification OME see <https://ome-model.readthedocs.io/en/stable/ome-xml/index.html>
:::

(format-big-imaged)=
## Big images

:::{sidebar} BigTIFF
In the event that exceptionally large images are to be processed in the manner that is typically required for the analysis of histological images, the ImageC software is equipped with the capability to support the bigTIFF format. 
</br>
The big tiff file format breaks the the 4 gigabyte size limit in comparison to the normal tiff format.
</br>
BigTIFF images are usually split into tiles whereby a typical tile size is `512x512 px`.
When analyzing, ImageC opens in this example `64` tiles at once and analyses one such composite tile after another.
This is necessary because when working with such large images, the entire image cannot be loaded into RAM at once.

```{figure} images/tiles.drawio.svg
:class: full-image
```

:::

Pictures with a resolution greater than `8466x8466 px` will not be loaded all at once, but will be attempted to be loaded tile by tile.
ImageC loads more than one image tile at a time and builds composite tiles.
This is done to reduce the number of edges in a large image when it is sliced into tiles.

ImageC allows you to immediately see the pipeline settings that have been made by providing a live preview of the images.
However, it is not possible to preview a hole image that is larger than the available RAM, and it would also take a long time to generate the preview.
For this reason, ImageC only shows the preview of one composite tile at a time to reduce the amount of RAM required and to increase the preview generation time.
To allow navigation within such a large image, jumping from tile to tile, ImageC generates a map of the entire image showing the currently selected composite tile.

Using the pyramid image function, the navigation map is generated using an image with a lower resolution than the original image.
This means that the prerequisite for the preview generation of large images is that they are saved as a pyramid image.

:::{note}
When working with large images, be sure to save them as a pyramid image to take advantage of ImageC's full preview functionality.
:::
