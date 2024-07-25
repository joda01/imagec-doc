(viewing-results)=
# Viewing results

To view the results go back to the start screen using the {guilabel}`House` button at the top left in the toolbar.
On the start screen use {guilabel}`Open Results` and navigate to the {file}`imagec` results folder selecting the {file}`results.duckdb` file.

## Plate view

ImageC opens the `Plate` view panel per default showing the results as heatmap.
Plate size can be selected in the {guilabel}`Heatmap` sidebar to the left.

```{figure} images/screenshot_plate_view.png
:class: full-image

Plate view
```

The plate view displays the Mean values and standard deviation as determined from all individual images taken in the respective well/ group. Image grouping is predefined in {guilabel}`Group by` settings.
If {guilabel}`Ungrouped` was selected as {guilabel}`Group by` method, all data are summarized to the well `A1`.

The left sidebar enables to select "Channel, measurement and statistics" that should be displayed in the well plate.

The right-hand sidebar shows information about the selected well.

Wells are coloured using a  heatmap calculated from all data displayed, with the mean value of all wells as the centre of the spectrum and the minimum and maximum as the outer left and outer right limits of the spectrum.

## Well view

A double click on a well will prompt the opening of a detailed view of the selected well.

```{figure} images/screenshot_well_view.png
:class: full-image

Well view
```

:::{sidebar} Well order matrix

A string formatted order matrix can be used to customize the order of images displayed in the well order matrix.
Per default the matrix is set to: `[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]`.
The numbers in the square brackets are the image indexes, where each comma-separated square block represents a row and the comma-separated numbers represent columns.
This results in the following screen sequence for the example above.

```{image} images/matrix_example.drawio.svg
``` 

:::

The {guilabel}`Well view` displays each image of the well ordered by the image index specified in the {guilabel}`Well order` matrix.
The image index was extracted from the filename during the analysis using the specified regex.
To reorder the image position displayed in the well view matrix use the {guilabel}`Well order` settings field.

If images are to be excluded from the statistics, this can be done via the menu item {guilabel}`Mark as invalid`.
As invalid marked images are crossed out and are not taken into account in all subsequent calculations.

## Image view

To go one step deeper, looking into detail information about a single image, double click on an image in the {guilabel}`Well view`.

The image view presents a density map of the image.
By default a are size of `200px 200px` is used to calculate the density map.
ImageC calculates the average value of the selected measurement of all valid objects within this `200px 200px` squares.

The square size can be changed using the left hand side panel.
Be careful though, if the square size is too small for large images, you may run out of RAM.

```{figure} images/screenshot_image_view.png
:class: full-image

Image view
```

ImageC allows you to inspect a selected density map square in the original image by double-clicking on these squares.
You are asked to enter a filename for the exported image, which is shown afterwards.
This exported image shows the selected area, making it easy to analyze the image in detail.

```{figure} images/screenshot_image_zoom.png
:class: small-image

Image details
```


