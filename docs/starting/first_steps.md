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

## View Panels

### Overview

Once ImageC has been successfully launched and the new project wizard has been closed via the {guilabel}`Apply` button, the {guilabel}`Overview` panel is displayed.

:::{figure} images/screenshot_overview.png
:class:

ImageC overview panel
:::

## Channels

### Channel settings


### Voronoi settings


### Intersection settings