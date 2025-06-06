---
layout: docu
redirect_from:
- /docs/commands/intensity
title: Intensity
---

<img src="{{ site.baseurl }}/images/commands/intensity-screenshot.png" alt="Screenshot" style="width: 25%; height: auto;">


The intensity command allows to change the image brightness, contrast and gamma.
The contrast value is a factor between one and three.
One means no change in contrast, three means a contrast increase by a factor of three.

For brightness a range of -32768 and +32768 can be specified.
By adding this value to each pixel value in the image, the brightness is increased by the specified value.

> Warning Gamma correction is not yet supported by ImageC.


In addition to setting manual image correction factors, an automatic correction mode can be selected.
Automatic contrast and brightness correction is done by calculating a histogram equalizing.





> Histogram equalizing is done in three steps:
> Step 1: Calculate the histogram (65536 bins for 16-bit range)
> Step 2: Calculate the cumulative distribution function (CDF)
> 
> $$
> cdf[i] = cdf[i - 1] + hist[i];
> $$
> 
> Step 3: Normalize the CDF to the range [0, 65535]
> 
> $$
> equalization_{map}[i] = \frac{65535.0 \cdot cdf[i]}{total_{pixels}}
> $$
> 
> Step 4: Map the pixel values from the equalization map

