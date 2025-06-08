---
layout: docu
redirect_from:
- /docs/commands/measure-distance
title: Measure distance
---


The distance measure command can be used to measure the distance between all objects of two different object classes.
Five different distances are calculated for each object combination: center to center, center to surface min, center to surface max, surface to surface min, surface to surface. 
The euclid-distance is used for distance calculation.

<a href="{{ site.baseurl }}/images/commands/distance-measure.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/distance-measure.drawio.svg" style="width: 50%" alt="Loading ..."/></a>


ImageC calculates the distance between all objects within the two given classes.
In reality, however, often only a fraction of the calculated distances are required. 
Typically, for example, the distance between spots and the cell wall would be calculated, but only the distance between those spots and the cell wall where the spots are also located within the respective cell are of interest.

For that reason ImageC allows to specify a condition for the distance calculation.
Following conditions are supported:


Condition                   |Description
------------                |--------------
All                         |The distance between all objects of the given classes is calculated.
Intersecting                |Only those objects that intersect with each other have their distances calculated.
Same parent                 |If the "From" and "To" object have the same parent the distance is calculated.
To object is parent of From |If the "To" object ID is same to the "From" object parent ID.

## All

No condition is used for calculating the distance between the given object classes.



> Warning Be careful using the command without condition. The number of calculated distances may increase very fast.

The example below calculated the distance between the class of green objects and red objects without any condition.

<a href="{{ site.baseurl }}/images/commands/distance-measure-all.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/distance-measure-all.drawio.svg" style="width: 80%" alt="Loading ..."/></a>

## Intersecting

Only those objects that intersect with each other have their distances calculated.
This condition is typically used to calculate the distance between spots taken up by a cell and the cell's wand and centre.

This example shows the usage of the `Intersecting` condition to calculate the distance from the `spot` objects to the `cell` objects.

<a href="{{ site.baseurl }}/images/commands/distance-measure-intersect.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/distance-measure-intersect.drawio.svg" style="width: 80%" alt="Loading ..."/></a>


## Same parent

If the "From" and "To" object have the same parent the distance is calculated.
This condition is typically used to calculate the distance between objects within an other object, e.g. the distance between spots and nucleus within a cell.

> Warning To use this condition a `Reclassify` command using the intersecting filter has to be applied before using the distance measurement.
> Using the `Reclassify` using th intersecting filter sets the parent ID. If the command is not applied before no parent ID is set and the distance measurement with this condition will not work.

This example shows the usage of the `Same parent` condition to calculate the distance from the `spot` objects to the `nucleus` objects inside a cell

<a href="{{ site.baseurl }}/images/commands/distance-measure-same-parent.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/distance-measure-same-parent.drawio.svg" style="width: 80%" alt="Loading ..."/></a>



## To object is parent of From

If the "To" object ID is same to the "From" object parent ID.
This condition can be used after a `Reclassify` using the intersection filter to calc the distance between objects which are intersecting.
The result is similar than using the `Intersecting` condition but allows have more control of the intersecting properties.
In addition, the distance between two different object classes can be calculated from the intersection that was calculated a few pipeline steps earlier, which does not directly intersect with the distance measurement step.


> Warning To use this condition a `Reclassify` command using the intersecting filter has to be applied before using the distance measurement.
> Using the `Reclassify` using th intersecting filter sets the parent ID. If the command is not applied before no parent ID is set and the distance measurement with this condition will not work.