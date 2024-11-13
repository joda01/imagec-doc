
(command-blur)=
# Blur

:::{sidebar} Filter kernel

In image processing, a kernel, convolution matrix, or mask is a small matrix used for blurring, sharpening, embossing, edge detection, and more. 
This is accomplished by doing a convolution between the kernel and an image. 
Or more simply, when each pixel in the output image is a function of the nearby pixels (including itself) in the input image, the kernel is that function.



```{figure} images/blur_kernel.drawio.svg
:class: full-image
```

https://en.wikipedia.org/wiki/Kernel_(image_processing)
:::

```{figure} images/blur_screenshot.png
:class: tiny-image
```

Blur algorithms are used to reduce image noise and details.

ImageC provides two different blur algorithms, "normal" blur and Gaussian blur.
For both the filter kernel size can be set.
The larger the kernel, the more details are removed from the image.

Gaussian blur uses a Gaussian function to blur the image.
Compared to the normal blur gaussian blur tends to preserve edges slightly better and avoids sharp transitions between blurred regions.

:::{hint}
Bigger filter kernels removes more noise and details from the image. Use gaussian blur to preserve edges in a better way than normal blur.
:::