(command-reclassifier)=
# Reclassifier

:::{sidebar} Object hierarchy
An object hierarchy is built up by storing a parent object ID together with each object.
This information can be used to draw a hierarchy graph of the objects, showing which objects are part of another.
Use the intersection filter of the [Reclassify](command-reclassifier) command to build up such a hierarchy.

```{image} images/object-hierarchy.drawio.svg
:class: full-image
```
:::


```{figure} images/reclassify-screenshot.png
:class: small-image
```

The reclassify command can be used to change the class of an object that has been formally classified using the [classifier](command-classifier) or [ai-classifier](command-classifier-ai) command, based on some filter criteria.
This allows to create further fine granular object populations.

Typical use case for instance are the separation of spots in cell and outside a cell, which can be managed using the intersection filter.
Or the separation of bright and less bright spots.

For that reason the ImageC reclassifier provides two filter options: {guilabel}`Intersection` and {guilabel}`Intensity`.

## Filters

### Intersection filter

The intersection filter takes an intersection object class as input and is applied to those objects of the input input class that intersect with any of these objects.
ImageC can create a object hierarchy (see section [parent object id](parent-object-id)) when using the intersection filter.
The object hierarchy allows to answer the questions: Which objects are contained within another object and how many objects intersect another object!?

The parent information is stored in the intersecting object from the input object input class whereby the parent object is the intersecting object from the intersecting object input class.

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

Once the filter matches, one of the {guilabel}`Move` or {guilabel}`Copy` operations will be applied to the objects that match the filter.

The move operator applies a new object class to the object.
Object ID keeps the same as before.

The copy operator creates a new object and assigns the new object class only to the new object.
A new object ID is generated and the origin object ID of the newly created object is set to the object ID of the origin object.
The origin object keeps untouched.