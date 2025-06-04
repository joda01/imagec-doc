---
layout: docu
redirect_from:
- /docs/commands/blur
title: Blur
---

<img src="/images/commands/blur-screenshot.png" alt="Screenshot" style="width: 30%; height: auto;">


Blur algorithms are used to reduce image noise and details.

ImageC provides two different blur algorithms, "normal" blur and Gaussian blur.
For both the filter kernel size can be set.
The larger the kernel, the more details are removed from the image.

Gaussian blur uses a Gaussian function to blur the image.
Compared to the normal blur gaussian blur tends to preserve edges slightly better and avoids sharp transitions between blurred regions.

> Tip Bigger filter kernels removes more noise and details from the image. Use gaussian blur to preserve edges in a better way than normal blur.



> In image processing, a kernel, convolution matrix, or mask is a small matrix used for blurring, sharpening, embossing, edge detection, and more. 
> This is accomplished by doing a convolution between the kernel and an image. 
> Or more simply, when each pixel in the output image is a function of the nearby pixels (including itself) in the input image, the kernel is that function.
> 
> <img src="/images/commands/blur-kernel.drawio.svg" alt="Screenshot" style="width: 30%; height: auto;">
> ```
> https://en.wikipedia.org/wiki/Kernel_(image_processing)