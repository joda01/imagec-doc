(objects)=
# Objects


Objects are the result of an image [classification step](commands-object-classification) and represents the quantified data of an formally extracted region of interest.
Objects are the final part of an ImageC pipeline and are those elements which are finally stored to the results database.

Each object is assigned to exact one object class (See [classification](Classification) section) to scope it.
Together with the classification labels some object metrics are calculated.
ImageC distinguishes between [image plane](image-planes) independent and [image plane](image-planes) dependent metrics.
Image plane independent metrics are globally valid for the object whereby image plane dependent metrics are calculated based on the image pixel data.
Following independent metrics are calculated for each object and are available in the results at the end of the analysis:

:::{note}
See section [Measurement](command-measurement) to get an overview of the image plane dependent object metrics.
:::

## Confidence

The confidence interpretation depends on the used segmentation mode.
For [threshold](command-threshold) segmentation the confidence value is the minimum threshold which was used to finally extract the object from the rest of the image.
The number range is from zero to 65535.

If [AI classifier](command-classifier-ai) is used the confidence value represents the output prediction probability of the used AI model.
The number range is from zero to one.

## Area size

:::{sidebar} Metrics
Red the centroid, gray the surrounding bounding box of the object.
Hatched the are size of the object.

```{image} images/metrics-example.drawio.svg
:class: full-image
```
:::

The area size is defined by the number of not black pixels within the shape of the extracted region of interest.
It's unit is px^2.

## Perimeter

The perimeter calculation has been ported from ImageJ to ImageC.

The algorithm counts pixels in straight edges as 1 and pixels in corners as sqrt(2).
It does this by calculating the total length of the ROI boundary and subtracting 2-sqrt(2) for each non-adjacent corner. 
For example, a 1x1 pixel ROI has a boundary length of 4 and 2 non-adjacent edges so the perimeter is 4-2*(2-sqrt(2)). 
A 2x2 pixel ROI has a boundary length of 8 and 4 non-adjacent edges so the perimeter is 8-4*(2-sqrt(2)).

## Circularity

Circularity defines the "roundness" of an object.
In other words, how similar the object is to a circle.
The value is in range of zero to one, whereby one stands for a perfect circle!
The circularity of an object is calculated as follows:


```{math}
c = \frac{4 \cdot pi \cdot AreaSize}{perimeter^2}
```


## Centroid

The centroid is the geometrical center of an object.
This is the average of the x and y coordinates of all of the pixels in an object.
It's coordinates are calculated by the first order spatial moments.

```{math}
c_x = \frac{m_{10}}{m_{00}}
c_y = \frac{m_{01}}{m_{00}}
```

## Bounding box

The bounding box is the smallest square which can be drawn to include all pixels of the object within the box.

## Object ID

During the object detection of a run, ImageC assigns an ID to each detected object, starting with `1` for the first detected object.
This object ID is unique throughout the entire run, i.e. an object can be uniquely identified by this object ID.

Using the {guilabel}`With object ID` option of the [Image save](command-image-save) allows to plot the ID beside the detected ROI in the image.
Together with the results table, which also allows the ID to be displayed, each region of interest within the image can be matched to its measurements.


(parent-object-id=)
### Parent Object ID

:::{sidebar} Object hierarchy
An object hierarchy is built up by storing a parent object ID together with each object.
This information can be used to draw a hierarchy graph of the objects, showing which objects are part of another.
Use the intersection filter of the [Reclassify](command-reclassifier) command to build up such a hierarchy.

```{image} images/object-hierarchy.drawio.svg
:class: full-image
```
:::

ImageC allows to build up a hierarchy of objects during a run using the [Reclassify](command-reclassifier) command.
Once an object has been discovered and assigned to an object class, the command can be used to change this class based on some criteria.

One of these criteria is the intersection of the object with an other one.
When this option is used, ImageC stores the object ID of the intersecting object (the parent) as the parent object ID together with the object with which the intersection is to be calculated. 
An object can have exact zero or one parent.

### Origin Object ID

Once an object is duplicated using the {guilabel}`Reclassify copy` option of the [Reclassify](command-reclassifier) command, the ID of the origin object is stored together with the duplicated object.
The origin object ID keeps the same even if a duplicated object is again duplicated.

## Tracking ID

:::{sidebar} Object tracking
Object tracking is the process of linking two objects, either from different time frames or channels, using the same tracking ID for all objects.
This makes it possible to display objects from different sources that physically represent one object.

```{image} images/object-tracking.drawio.svg
:class: full-image
```
:::

The Object ID identifies an object uniquely within a run and the parent object ID gives information about the hierarchy of the objects.
The tracking ID, on the other hand, is used to link recognized objects that represent the same physical instance.

Example for such "same physical instances" are colocalizing objects from different image channels or moving objects in two different time frames,
In the actual version of ImageC, the colocalizing tracking is supported by using the [Colocalization](command-colocalization) command.

When using the colocalizing command each object which colocalizes get the same tracking ID which allows later on to match those objects.