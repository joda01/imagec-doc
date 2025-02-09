
(command-median-subtract)=
# Median subtract

:::{sidebar} Rank filter

Rank-order filters belong to the class of non-linear filters in digital image processing. 
These are filters that cannot be described by a convolution.

With ranking filters, the gray values of the pixels in a defined area around a pixel are collected, sorted by size and ranked. 
A gray value is then selected from this sorted list to replace the gray value of the current pixel.

The choice of position determines the type of ranking filter. With ascending sorting, you get the:

- Minimum filter, for the minimum gray value, first position in the list
- Median filter, for the gray value in the middle of the list
- Maximum filter, for the maximum gray value, last position in the list.

:::

```{figure} images/median-subtract-screenshot.png
:class: tiny-image
```

Median subtraction is a sort of noise filtering which can be used to reduce background noise similar to the [rolling ball]() algorithm.
Behind the scenes a rank filter is used to calculate the median of the image intensity, which is subtracted afterwards from the original image.

The kernel size defines the window size used for the rank filter to calculate the median.
Bigger kernels reduces more details from the image than smaller ones.

:::{hint}
Bigger filter kernels removes more noise and details from the image.
:::