---
layout: docu
redirect_from:
- /docs/commands/image-cache
title: Image Cache
---


<a href="{{ site.baseurl }}/images/commands/store-image-to-cache-screenshot.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/store-image-to-cache-screenshot.png" style="width: 30%" alt="Loading ..."/></a>


The store image to cache command stores an actual image at any time to the cache.
Image cache allows using a preprocessed image as base for further preprocessing steps in an other pipeline or in the same pipeline in a future step.
Possible applications might be to preprocess a background for subtraction and use this preprocessed background together with the image math subtract command in other pipelines to remove it.


### Storage scope

The storage scope defines either if the cached image is only available in the pipeline the command is used `Iteration` or if the stored image can also be used across different pipelines `Pipeline`.

The memory slots `M0` to `M10` can be used twice once for `Iteration` and once for `Pipeline` cache.


> Note Once an image is stored to the cache it is not edited any more. Loading from the cache creates a new local copy of the image and the pipeline is working on this local copy but not on the cached image.



> ImageC cache is reserved place in the RAM of the computer.
> Storing an image to the cache stores the actual image to this place in RAM.
> Other commands can load these images from the RAM in an efficient way and apply further processing steps on it.
> 
> <a href="{{ site.baseurl }}/images/commands/store-to-cache.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/store-to-cache.drawio.svg" style="width: 30%" alt="Loading ..."/></a>