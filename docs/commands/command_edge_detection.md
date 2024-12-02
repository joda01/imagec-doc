
(command-edge-detection)=
# Edge detection

:::{sidebar} Edge detection

Edge detection is the process of finding edges in an image and converting them to a gradient representation.
Sharper changes in the intensity values lead to a higher gradient.

```{figure} images/edge_detection.drawio.svg
:class: full-image
```

:::

```{figure} images/edge_detection_screenshot.png
:class: tiny-image
```

Edge detection is a function used to highlight the edges within an image.
An edge is defined as a change in grey level.
Larger rates of change in the values lead to a larger output value in the algorithm.

ImageC provides {guilabel}`Sobel` and {guilabel}`Canny` edge detection.


The main advantages of the Sobel operator are that it is simple and time efficient but produces rough edges.
On the other hand, the Canny technique produces smoother edges due to the implementation of non-maxima suppression and thresholding. 
The disadvantage of the Canny algorithm is that it is more complex and less time efficient than Sobel.
