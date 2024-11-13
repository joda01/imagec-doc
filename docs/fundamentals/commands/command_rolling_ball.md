
(command-rolling-ball)=
# Rolling ball

:::{sidebar} Thresholding


The rolling-ball algorithm was inspired by Stanley Sternberg’s article, “Biomedical Image Processing”, IEEE Computer, January 1983.

```{figure} images/rolling_ball_reseacrh_gate.jpeg
:class: full-image
```

:::

```{figure} images/rolling_ball_screenshot.png
:class: tiny-image
```

The rolling ball algorithm is a background subtraction algorithm, with the goal to remove most of the background noise.

This is achieved by creating a local background around a virtual ball.
Within the radius of the ball, the average intensity is calculated.
This is done for the entire image.
The result is subtracted from the original image.  

This port from ImageJ contains two ball types, a spheral ball and a paraboloid.
A paraboloid handles edges more gently, reducing the appearance of artifacts along boundaries. 
This is beneficial in applications such as microscopy, where accurate boundary representation is essential.

:::{hint}
The radius of the ball should be set to at least the size of the largest object that does not belong to the background.
:::

:::{note}
The implementation in ImageC was taken from the original ImageJ and ported to C++ based on the NIH Image Pascal version by Michael Castle and Janice Keller of the University of Michigan Mental Health Research Institute.
:::



