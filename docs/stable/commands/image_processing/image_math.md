---
layout: docu
redirect_from:
- /docs/commands/image-math
title: Image math
---

<a href="/images/commands/image-math-screenshot.png" data-lightbox="image"><img src="/images/commands/image-math-screenshot.png" style="width: 30%" alt="Loading ..."/></a>

The image math command can be used to combine two images using one of the provided mathematical operations.
Input image one is the image from the last pipeline step, the second image is the image configured in the `Input image channel` settings.
For the second image either an image channel can be used or an image stored in the cache from a previous pipeline.
If `From cache` is not `None` the channel settings are ignored and the image from the selected cache slot is loaded.

The `Operating order` setting allows to define if the first operand of the selected function is the image from the last pipeline step or the selected input image.


> An image is represented as a matrix of pixel intensity values.
> When calculating with images a matrix operation is performed which uses the pixel value at `(n,m)` from both matrixes and applying the operator on that.
> The resulting matrix after applying the operator on all elements of the matrix is the resulting image.
> 
> <a href="/images/commands/image-math.drawio.svg" data-lightbox="image"><img src="/images/commands/image-math.drawio.svg" style="width: 30%" alt="Loading ..."/></a>