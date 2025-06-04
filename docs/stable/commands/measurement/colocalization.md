---
layout: docu
redirect_from:
- /docs/commands/colocalization
title: Colocalization
---

<a href="/images/commands/colocalization-screenshot.png" data-lightbox="image"><img src="/images/commands/colocalization-screenshot.png" style="width: 30%" alt="Loading ..."/></a>


The colocalization command is used to determine objects which intersect with each other.
Up to four object classes can be given as input, for those the colocalization is calculated.
A spot is defined as colocalizing if for each given input class a overlapping object is found.

The ImageC colocalization command allows to reclassify those objects which colocalizes for a further processing of the objects.


> Object tracking is the process of linking two objects, either from different time frames or channels, using the same tracking ID for all objects.
> This makes it possible to display objects from different sources that physically represent one object.
> 
> <a href="/images/commands/object-tracking.drawio.svg" data-lightbox="image"><img src="/images/commands/object-tracking.drawio.svg" style="width: 30%" alt="Loading ..."/></a>



## Colocalizing handling

Once an object colocalizes, one of the `Move` or `Copy` operations will be applied to that objects.

The move operator applies a new object class to the object.
Object ID keeps the same as before.

The copy operator creates a new object and assigns the new object class only to the new object.
A new object ID is generated and the origin object ID of the newly created object is set to the object ID of the origin object.
The origin object keeps untouched.

In addition a new object is generated which the overlapping area (colocalization area) of the overlapping objects.

All colocating objects, including the newly created Coloc Area object, are given a common tracking ID.
In the results, objects with the same Tracking ID are placed next to each other, allowing matching objects to be compared.


> If from each input class an object overlaps with an other object from the other input classes, the object is defined as colocalizing.
> The overlapping area is called the coloc area and a new object for further processing of this area is generated.
> In addition ech colocalizing object gets the same tracking ID assigned.
> 
> <a href="/images/commands/colocalization.drawio.svg" data-lightbox="image"><img src="/images/commands/colocalization.drawio.svg" style="width: 30%" alt="Loading ..."/></a>
