---
layout: docu
redirect_from:
- /internals/tutorials/yest-cell-detection
title: Yest cell detection
---

ImageC is shipped with a predefined pipelines for Yest cell detection in brightfield images.
In this tutorial we will go step by step through this pipeline template.

<a href="{{ site.baseurl }}/images/tutorials/yest_cells_screenshot.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/tutorials/yest_cells_screenshot.png" style="width: 100%" alt="Loading ..."/></a>


Before you start creating the pipeline, look at your image and identify the metrics that distinguish your objects of interest from the rest of the image.
When we examine the yeast cells in bright field, a very strong characteristic is the cell membrane, which is shown as a bold, dark border.

So let's find a pipeline which finds this border:

1. **Intensity** First, we use the intensity command to adapt the brightness of the image based on the image exposure.
2. **Blur** To find the border we will use an edge detection algorithm. However such algorithms react on intensity changes in the image. Noise per definition generates a lot of small such sharp intensity changes in an image. Therefore we use a Gaussian Blur as our second step in the pipeline. The gaussian blur protects "real" edges in the image from being blured away but removed noise efficiently.
3. **Canny edge detection** The canny edge detection algorithm is now applied, converting the grayscale image into a binary image containing only the detected edges.
4. **Blur** the edges again to fill the are inside the circle with more contrast.
5. **Threshold** The background is removed when we reach the final threshold, which results in the cell body becoming more visible.
6. **Hough transformation** is used to find circles, which represents our cells in the image.
7. **Voronoi** The voronoi algorithm is used to separate the cells from each other.