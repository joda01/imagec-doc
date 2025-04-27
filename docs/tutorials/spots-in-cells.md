(tutorials-count-spots-in-cells)=
# Count spots in cells

This tutorial shows you how to setup a pipeline which can count the number of spots within a detected cell area.

First of all we define two classes using the classification tab. 
Let's call them `spots` and `cell-area`.

```{image} images/spots-in-cell-01.png
:class: full-image
```

Now switch to the pipeline tab and add the pipeline template `EV in cell`.


```{image} images/spots-in-cell-02.png
:class: full-image
```


Double click to the newly added pipeline and select `spots` as output class.
All objects detected in the selected image channel are now classified as `spots`.


```{image} images/spots-in-cell-02.png
:class: full-image
```