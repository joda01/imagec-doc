# Intersection slots

By click on {guilabel}`Add intersection channel` a new intersection channel is added to the processing list.


:::{figure} images/screenshot_intersection.png
:class: full-image
:::

Intersection slots are used to calculate the intersection of two or more channels or slots.

Typical use case is the calculation of the colocalization of two or more channels.

The field {guilabel}`Cross channel intersection` is employed for the definition of comma-separated indexes of channels and slots. 
The intersection is calculated with the aforementioned indexes.

A region of interest (ROI) is defined as intersecting if the ROI in a given channel overlaps with an ROI in all the other defined channels, and the percentage of the specified minimum intersection is met. 

:::{warn}
The behavior is undefined when trying to calculate the intersection of an intersection slot.
:::
