
(command-rank-filter)=
# Rank filter

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

With ranking filters, the grey values of the pixels in a defined area around a pixel are collected, sorted by size and ranked. 
A grey value is then selected from this sorted list to replace the grey value of the current pixel.

The {guilabel}`Radius` setting defines the size of the area to collect the pixels gray values in.