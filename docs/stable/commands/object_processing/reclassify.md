---
layout: docu
redirect_from:
- /docs/commands/reclassify
title: Reclassify
---

<a href="{{ site.baseurl }}/images/commands/reclassify-screenshot.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/reclassify-screenshot.png" style="width: 30%" alt="Loading ..."/></a>


The reclassify command can be used to change the class of an object that has been formally classified using the [classifier]({% link docs/stable/commands/classification/classifier.md %}) or [ai-classifier]({% link docs/stable/commands/classification/classifier_ai.md %}) command and build up an object hierarchy tree based on some filter criteria.
This allows to create further fine granular object populations.

Typical use case for instance are the separation of spots in cell and outside a cell, which can be managed using the intersection filter.
Or the separation of bright and less bright spots.

The reclassify command provides a couple of filter functions which are described below.

## Filters

### Intersection filter

The intersecting filter checks each object from the input class to see if it overlaps with an object from the intersecting class.
ImageC creates an object hierarchy by setting the parent object ID of the input object to the object ID of the intersecting object (see section [parent object id]({% link docs/stable/fundamentals/objects.md %}#parent-object-id)).

<a href="{{ site.baseurl }}/images/commands/object-hierarchy.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/object-hierarchy.drawio.svg" style="width: 80%" alt="Loading ..."/></a>


> Tip The object hierarchy allows to answer the questions: Which objects are contained within another object and how many objects intersect another object!

ImageC allows you to specify whether or not to create a hierarchy for intersecting objects by specifying the hierarchy mode.


#### Create hierarchy

This option stores the parent information for intersecting objects.
Existing hierarchy information is retained which allows to build up a full hierarchy tree.
E.g. parent of nucleus is cell, parent of spot is nucleus, which allows to answer the questions: Give me the spots within a Cell and give me the spots within a cell in the nucleus of this cell.

#### Keep existing

This option does not change the hierarchy information of the intersecting object.

#### Remove hierarchy information

This option removes the parent object ID from the intersecting objects.


### Intensity filter

This filter allows to specify a min and max intensity measured in the defined image channel.
If the measured object intensity is within this intensity range the filter is applied.

Intensity filter and intersection filter can both be activated.
Only if both filters match the filter for the object is applied.

## Match handling

Once the filter matches, one of the `Move` or `Copy` operations will be applied to the objects that match the filter.

The move operator applies a new object class to the object.
Object ID keeps the same as before.

The copy operator creates a new object and assigns the new object class only to the new object.
A new object ID is generated and the origin object ID of the newly created object is set to the object ID of the origin object.
The origin object keeps untouched.