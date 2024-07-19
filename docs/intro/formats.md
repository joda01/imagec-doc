(supported-image-formats)=
# Supported image formats

## Image files

ImageC can be used with a wide range of image formats, thanks to two essential open source libraries:

- **Bio-formats**: <https://docs.openmicroscopy.org/bio-formats>
- **libTIFF**: <https://gitlab.com/libtiff/libtiff>


:::{important}
ImageC is actually designed to read only greyscale images in either 8-bit or 16-bit format.
:::

:::{sidebar} BigTIFF
In the event that exceptionally large images are to be processed in the manner that is typically required for the analysis of histological images, the ImageC software is equipped with the capability to support the bigTIFF format. 
</br>
The big tiff file format breaks the the 4 gigabyte size limit in comparison to the normal tiff format.
</br>
BigTIFF images are usually split into tiles whereby a typical tile size is `256x256 px`.
When analyzing, ImageC opens `36` tiles at once and analyses one such composite tile after another.
This is necessary because when working with such large images, the entire image cannot be loaded into RAM at once.

```{image} images/tiles.png
```
:::

Based on the file extension, ImageC decides whether to use BioFormats or the built-in tiff loader to open the image.
Images using the extension `.tif, .tiff, .btif, .btiff, .btf` are loaded using the built-in tiff loader.
For all other image file extensions (`.vsi, .ics, .czi`) the BioFormats plugin is used.

Pictures with a resolution greater than `8466x8466 px` will not be loaded all at once, but will be attempted to be loaded tile by tile.

Tile based image loading is only supported for bigTIFF images with file extension `.btif, .btiff, .btf`.

BioFormats [command line tools](https://www.openmicroscopy.org/bio-formats/downloads/) can be used to convert your imaged to tiled bigTiff if necessary.

- Download bftools from <https://www.openmicroscopy.org/bio-formats/downloads/>
- Execute `bfconvert -pyramid-scale 4 -tilex 512 -tiley 512 <input_image> <output_image>.btf`

In addition many microscopy malefactors support big tiff export out of the box using the microscopy software itself.

:::{caution}
It should be noted that support for pyramid-scaled images is not yet available in ImageC, although this is currently being developed. To ensure compatibility with future versions, it is recommended that all images with pyramid scaling be converted.
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