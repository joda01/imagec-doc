(objects)=
# Objects

:::{sidebar} Circularity
Circularity describes the roundness of an object, with a perfect circle having a circularity of `1`. 
The circularity of an object is calculated as follows:

```{math}
c = \frac{4 \cdot pi \cdot AreaSize}{perimeter^2}
```
:::

Objects are the final part of each ImageC pipeline and represents the quantified image data.

For each object following metrics are measured:
- Confidence
- Area size
- Perimeter
- Circularity
- Center of mass (x, y)
- Bounding box (x, y, width, height) 
- Contour
- Mask matrix


