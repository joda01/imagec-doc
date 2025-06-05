---
layout: docu
redirect_from:
- /docs/commands/rank-filter
title: Rank filter
---

<a href="{{ site.baseurl }}/images/commands/screenshot-rank-filter.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/screenshot-rank-filter.png" style="width: 30%" alt="Loading ..."/></a>


With ranking filters, the grey values of the pixels in a defined area around a pixel are collected, sorted by size and ranked. 
A grey value is then selected from this sorted list to replace the grey value of the current pixel.

The `Radius` setting defines the size of the area to collect the pixels gray values in.

> Tip Bigger filter kernels removes more noise and details from the image.


> Rank-order filters belong to the class of non-linear filters in digital image processing. 
> These are filters that cannot be described by a convolution.
> 
> With ranking filters, the gray values of the pixels in a defined area around a pixel are collected, sorted by size and ranked. 
> A gray value is then selected from this sorted list to replace the gray value of the current pixel.
> 
> The choice of position determines the type of ranking filter. With ascending sorting, you get the:
> 
> - Minimum filter, for the minimum gray value, first position in the list
> - Median filter, for the gray value in the middle of the list
> - Maximum filter, for the maximum gray value, last position in the list.
> 
> <a href="{{ site.baseurl }}/images/commands/rank-filter.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/rank-filter.drawio.svg" style="width: 30%" alt="Loading ..."/></a>



