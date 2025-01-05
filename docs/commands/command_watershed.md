(command-watershed)=
# Watershed


:::{sidebar} Object segmentation using watershed

Based on peaks extracted from the intensity values the valleys between the peaks are the borders for splitting objects.

```{figure} images/watershed.drawio.svg
:class: full-image
```

:::

```{figure} images/watershed_screenshot.png
:class: tiny-image
```

The watershed algorithm employs a process of object segmentation/separation based on the intensity values of the objects in question. 
In this context, the intensity values are interpreted as altitude, with the objective of identifying the valleys between the peaks.

In applications with a high object density, it is no exception that two objects come very close or even touch each other.
When using threshold techniques for object segmentation, it is not possible to distinguish between two such near objects anymore.

Some algorithms have been developed with the specific aim of addressing this issue.
One of them is the Watershed algorithm which was ported from [ImageJ](https://imagej.net/imaging/watershed) to ImageC for that reason.

:::{hint}
Use the tolerance value to define on which percentage of the extracted intensity level an object border os detected.
:::

:::{warning}
It is recommended that the watershed be activated only when necessary, as it is a highly complex algorithm that significantly reduces analysis time when activated.
:::