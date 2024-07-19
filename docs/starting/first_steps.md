(first-steps)=
# First steps

The following tutorial will provide an overview of the fundamental concepts and functions of ImageC, offering guidance on the initial steps required for effective utilization of the software.
The tutorial will demonstrate the following:

- ImageC Welcome window
- Creating a new project
- Adding channels
- Starting an analyzes
- Open analyzes results
- Export results to XLSX


## Getting started

:::{note}
If you have problems running ImageC see {doc}`here <../intro/installation>`.
:::

### Running ImageC

Once ImageC has been successfully launched, the user will be directed to the start wizard. 
At this point three options are available: create a new project, open an existing project, open the results of a previous run.


:::{figure} images/screenshot_start_screen.png
:class:  full-image

ImageC start screen
:::

By clicking the {guilabel}`New project` button a project wizard is opened.
You are asked for some basic experiment information:


:::{figure} images/screenshot_start_wizard.png
:class:

ImageC new project wizard
:::



```{eval-rst}
.. csv-table::
  :header: "Title", "Description", ""
  :align: center

  "Scientist name", "Name of the person who is responsible for this analysis", "Optional"
  "Organization", "Organization responsible for the analysis", "Optional"
  "Working directory", "Directory where the images to analyze are stored in", "Mandatory"
  "Images in well order", Describes in which order the images are placed in the well. The number is the image index in well.,"Mandatory"
  "Group by", "Group images either by Filename regex or Directory.","Mandatory"
  "Filename regex", "Regex to extract plate row, plate column and image index from the image filename.","Mandatory"
  "Regex test", "Used to test the regex settings.",""
  "Regex test result", "Result of the regex applied on the text given in the regex test field.",""
  "Notes", "Some free text notes on the experiment.",""


```

:::{caution}
Make sure that the grouping options and regex settings are correct, as they are needed for valid statistics calculations.
:::

:::{sidebar} Regex

Filename grouping uses regex (regular expressions) to extract the position on the plate and the position of the image in the well from the image filename.
Extracted are: plate `row` and `column` position and the image `index` in the well.

```{image} images/regex_example.drawio.svg
``` 

It es expected that the row position is a character in the range of `[A-Z]` and the column and index a decimal number.
A typical series of file names for the regex {regexp}`_((.)([0-9]+))_([0-9]+)` might look something like the following:

`name_A1_1.tif`
`name_A1_2.tif`
`name_A1_3.tif`
`name_A1_4.tif`
`name_A2_1.tif`
`name_A2_2.tif`
`name_A2_3.tif`
`name_A2_4.tif`

To experiment with regular expressions, have a look at [regex101](https://regex101.com/).

:::

It is important to set the correct grouping options in combination with the correct filename regular expression.
Based on these settings, ImageC performs some statistical calculations of the results during a running analysis.
This dramatically improves the speed of report generation.
However, if the grouping settings are wrong, these statistics will also be calculated in a wrong way.

When grouping by {guilabel}`Foldername` or {guilabel}`Filename` is selected ImageC will pre-calculate the statistics based on the determined group.
Average, Median, Min, Max, Standard deviation, Sum and Count are calculated for each group in advanced
When opening a analysis result (see {doc}`dive into the tutorials <../starting/results>`) these pre-calculated values are loaded for a fluid and fast view.

It is not possible to modify the grouping settings subsequently, as this would necessitate the repetition of the precalculation, which is not currently supported by ImageC.


The {guilabel}`Working Directory` should be set to the folder where the images to be analyzed are stored.
ImageC will perform a recursive folder search with the selected {guilabel}`Working Directory` as the base folder to find all supported image files.
All found files are listed in the {guilabel}`Overview` panel.


## Overview Panel

Once ImageC has been successfully launched and the new project wizard has been closed via the {guilabel}`Apply` button, the {guilabel}`Overview` panel is displayed.

:::{figure} images/screenshot_overview.png
:class:

ImageC overview panel
:::

The overview panel displays the actual for analysis created channels in the middle of the screen.
With the {guilabel}`Add` buttons in the button box new channels can be added.

On the right hand side the parsed [OME](formats-ome) meta data from the selected image is shown.

A list of all images found in the selected working directory is displayed in the bottom toolbar.

## Adding a channel

By clicking {guilabel}`Add Image Channel` a new channel is added to the analysis settings.
Up to 10 channels can be added.

:::{figure} images/screenshot_add_channel.png
:class:

Setting with one added channel
:::

When the analysis is started, each channel of all images found in the working directory is processed.
The results for each channel are stored in a file based database with the extension {file}`.duckdb` for later reporting generation and statistics.

By clicking on a channel, the channel editor is opened.
The channel editor allows to specify channel meta data, preprocessing steps, detection settings as well as filters for objects and images.

:::{figure} images/screenshot_channel_editor.png
:class:

Channel editor
:::

For a fast start select add an {guilabel}`EV channel` by selecting the {guilabel}`EV channel` entry from the template dropdown and click {guilabel}`Add Image Channel`.
Channel templates are useful if same settings for a channel are used more often.
Template files are JSON files and stored in the {file}`./templates` directory beside the ImageC binary.

At the right hand side a live preview is displayed.
It shows the resulting image after all applied preprocessing steps and filters.
Changing a parameter will directly affect the preview.
Based on image size and the complexity of the selected preprocessing algorithms it could take a couple of seconds for refreshing the preview.

:::{hint}
See the section [Channels](channels) for detailed information about the channel settings parameter.
:::

## Starting the analysis

With the back button on the top left the overview panel is displayed again.
After all channels are added and all needed channel settings are done, the analysis can be started by pressing the {guilabel}`Run` button on the top.

:::{figure} images/screenshot_running.png
:class:

Analysis running
:::

A dialogue box informs you about the progress of the analysis.
At the bottom right of the dialog a {guilabel}`Open results folder` button is placed.
Press this button to open the file explorer showing the folder with results of the actual analysis run.

With {guilabel}`Stop` button a running analysis can be interrupted.
It may take a couple of minutes to stop a running analysis since all still in progress tasks have to be finished.

Press the {guilabel}`Close` button to close the dialog after a successful finished analysis run.

## Viewing results

To view the results go back to the start screen using the {guilabel}`House` button at the top left in the toolbar.
On the start screen use {guilabel}`Open Results` and navigate to the {file}`imagec` results folder selecting the {file}`results.duckdb` file.

ImageC opens the `Plate` view panel per default showing the results as heatmap.
Plate size can be selected in the {guilabel}`Heatmap` sidebar to the left.

:::{figure} images/screenshot_plate_view.png
:class:

Plate view
:::

The plate view displays the statistics per well based on the {guilabel}`Group by` settings of the analysis.
If {guilabel}`Ungrouped` was selected as {guilabel}`Group by` method, all data ara summarized to the well `A1`.

The left sidebar lets you view channel, measurement and statistic selections.

The right-hand sidebar shows information about the selected well.

The coloring of the wells is done using a color map with the mean value of all wells as the centre of the spectrum and the minimum and maximum as the outer left and outer right limits of the spectrum.

A double click on a well will prompt the opening of a detailed view of the selected well.

:::{figure} images/screenshot_well_view.png
:class:

Well view
:::

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

## Export to XLSX

