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