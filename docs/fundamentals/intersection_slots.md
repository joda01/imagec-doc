# Intersection slots

By click on {guilabel}`Add intersection channel` a new intersection channel is added to the processing list.

Intersection slots are used to calculate the intersection of two or more channels or slots.
Typical use case is the calculation of the colocalization of two or more channels.

```{figure} images/screenshot_intersection.png
:class: full-image
```


:::{sidebar} Intersection

An intersection is defined with: An region of interest (objects) intersects if it has an overlapping with an region of interest in all the given intersection channels.
The intersection factor in the range of $[0,1]$ is defined with:

```{math}
I_{factor} = \frac{A_{intersection}}{Min([A_{area_0}, A_{area_1}, ... A_{area_n}])}
```

The intersection factor $I_{factor}$ is defined by the area size of the intersection divided by the smallest of the areas the intersection was calculated with.
If 100% of the area is intersecting the factor is 1.

```{figure} images/intersection.drawio.svg
:class: full-image
```

:::

(intersection-meta)=
## Meta

Similar to the [image channels](pipelines) a user defined name can be set for the channel.

Using the {guilabel}`Channel index` the slot index `[A-F]` which should be associated with this channel can be selected.
Each slot channel index can only be used once and is needed for a unique identification of the channel.
Based on the slot channel index cross-channel measurements, for example, can be conducted on a specific slot channel.


## Intersection

The field {guilabel}`Cross channel intersection` is employed for the definition of comma-separated indexes of channels and slots. 
The intersection is calculated with the aforementioned indexes.

A region of interest (ROI) is defined as intersecting if the ROI in a given channel overlaps with an ROI in all the other defined channels, and the percentage of the specified minimum intersection is met. 


The minimum relative intersection area (Min. intersection area) is employed to delineate the minimal requisite area of intersection that must be present for two objects to be classified as intersecting. 
The value is expressed within the range [0,1], wherein 0 signifies that at least one pixel must intersect, and 1 denotes that 100% of the areas must intersect.


:::{caution}
The behavior is undefined when trying to calculate the intersection of an intersection slot.
:::