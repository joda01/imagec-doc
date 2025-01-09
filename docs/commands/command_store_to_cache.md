
(command-store-to-cache)=
# Store to cache

:::{sidebar} Cache

ImageC cache is reserved place in the RAM of the computer.
Storing an image to the cache stores the actual image to this place in RAM.
Other commands can load these images from the RAM in an efficient way and apply further processing steps on it.

```{figure} images/store_to_cache.drawio.svg
:class: full-image
```

:::

```{figure} images/image_math_screenshot.png
:class: tiny-image
```

The store image to cache command stores an actual image at any time to the cache.
Image cache allows using a preprocessed image as base for further preprocessing steps in an other pipeline or in the same pipeline in a future step.
Possible applications might be to preprocess a background for subtraction and use this preprocessed background together with the image math subtract command in other pipelines to remove it.

:::{note}
Cache scope is the processing step of an image. For each image a separate cache storage is created.
:::

:::{note}
Once an image is stored to the cache it is not edited any more. Loading from the cache creates a new local copy of the image and the pipeline is working on this local copy but not on the cached image.
:::