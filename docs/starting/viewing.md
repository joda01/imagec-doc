(viewing-results)=
# Viewing results

To view the results, switch to the {guilabel}`Results` tab, the results of the most recent analyses will be displayed at the top of the list.
Results from a previous run can be opened by clicking the {guilabel}`Open` button on the toolbar.

## Plate view

ImageC opens the `Plate` view panel per default showing an empty table.
To add a column click the add column button {{icon_addcolumn}}.


```{figure} images/screenshot_add_column.png
:class: small-image

Add a new column
```

The add column dialog allows to specify which data should be shown within this column.
Repeat the process for each data you are interested in.
Finally the statistics of the selected data grouped by well is displayed.

```{figure} images/screenshot_plate_view_table.png
:class: full-image

Plate view as table
```

The plate view displays the Mean values as determined from all individual images taken in the respective well/ group. 
Image grouping is predefined in {guilabel}`Group by` settings.
If {guilabel}`Ungrouped` was selected as {guilabel}`Group by` method, the plate view is not shown and ImageC directly jumps to the image list view.

Using the heatmap button {{icon_heatmap}} the view can be switched from a table view to a heatmap view.

```{figure} images/screenshot_plate_view_heatmap.png
:class: full-image

Plate view as heatmap
```



Wells are coloured using a  heatmap calculated from all data displayed, with the mean value of all wells as the centre of the spectrum and the minimum and maximum as the outer left and outer right limits of the spectrum.
In heatmap view a dropdown in the toolbar allows to select which column of the table should be displayed as heatmap.

## Image view

A double click on a well in the heatmap view or a column in the table view will prompt the opening of a detailed view of the selected well.

```{figure} images/screenshot_well_view.png
:class: full-image

Image view
```

:::{sidebar} Well order matrix

A string formatted order matrix can be used to customize the order of images displayed in the well order matrix.
Per default the matrix is set to: `[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]`.
The numbers in the square brackets are the image indexes, where each comma-separated square block represents a row and the comma-separated numbers represent columns.
This results in the following screen sequence for the example above.

```{image} images/matrix_example.drawio.svg
``` 

:::

The {guilabel}`Image view` displays each image of the well ordered by the image index specified in the {guilabel}`Well order` matrix.
The image index was extracted from the filename during the analysis using the specified regex.
To reorder the image position displayed in the well view matrix use the {guilabel}`Well order` settings field.

If images are to be excluded from the statistics, this can be done via the exclude menu item {{icon_unavailable}}.
As invalid marked images are crossed out and are not taken into account in all subsequent calculations.

## Density map view

To go one step deeper, looking into detail information about a single image, double click on an image in the {guilabel}`Image view`.

The density view presents a density map of the image.
In the bottom left sidebar the are size to b used for calculate the density map can be chosen.
ImageC calculates the average value of the selected measurement of all valid objects within this squares.

The square size can be changed using the left hand side panel.
Be careful though, if the square size is too small for large images, you may run out of RAM.

```{figure} images/screenshot_density_view.png
:class: full-image

Image view
```

(data-export)=
## Data export

The Download button {{icon_download}} allows the current settings to be exported as either XLSX or R.
ImageC saves the actual table settings with the database file so that they are restored the next time the results are opened.