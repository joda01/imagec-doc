
(command-morphological-transform)=
# Morphological transform

:::{sidebar} Pixel operations

An image is represented as a matrix of pixel intensity values.
When applying a rank-filter the pixel values in the defined area size are observed and ranked by the selected algorithm.
All pixels in the observed area are set to the new calculated value.

```{figure} images/rank-filter.drawio.svg
:class: full-image
```

:::

```{figure} images/screenshot-rank-filter.png
:class: tiny-image
```

Morphological transformation is an operation applied to the image shape.
Usually, binary images are used as input for this operation but can also applied to gray scale images.
ImageC supports the basic operations: erosion, dilation, opening and closing beside a couple of experimental operations.


A structuring element is applied to the input image performing the selected operation getting the output image. 
The output image pixel values are calculated by an comparison of the corresponding input image pixels with its neighbors.

A "structural element" is a shape which is used to identify the pixel to be processed and the neighboring pixels used during the process.
The structuring element form is chosen according to the shape of the object which should be processed in the input image.

The centre of the structuring element is called the origin. 
It identifies the pixel being processed. 
The origin need not always be the centre but might be even outside of the structuring element.

ImageC provides following options which allows to define the structual element and the algorithm settings:

The {guilabel}`Shape` defines the form of the structural element to use.
Theoretically any form can be used.
ImageC actually supports: `Circle`, `Square` and `Cross` as predefined elements to select.


The {guilabel}`Kernel size` setting is used to define the size of the area looking for neighbour pixels.

With the {guilabel}`iteration` option the number of runs of the algorithm can be defined.
Default is one run.


## Erosion

:::{sidebar} Erosion


```{figure} images/rank-filter.drawio.svg
:class: full-image
```

:::

Erosion removes the boundaries of an object.
The core of the object remains as the result.

- In a binary image, a pixel is set to 1 if all of the neighboring pixels have the value 1.
- In a gray scale image, the value of the output pixel is the minimum value of all pixels in the neighborhood.

Erosion can be used to separate connected objects or remove noise from the image.

## Dilation

## Opening

## Closing