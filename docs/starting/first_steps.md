(first-steps)=
# First steps

The following tutorial will provide an overview of the fundamental concepts and functions of ImageC, offering guidance on the initial steps required for effective utilization of the software.
The tutorial will demonstrate the following:

- Creating a new project
- Defining clusters and classes
- Adding pipelines
- Starting an analyzes
- Open analyzes results
- Export results


## Analyze images

:::{note}
If you have problems running ImageC see {doc}`here <../intro/installation>`.
:::

### Running ImageC

Once ImageC has been successfully launched, the user will be directed to the start page. 

```{figure} images/screenshot_start_screen.png
:class: full-image

ImageC start screen
```

The Settings tab on the left is divided into the following sections {guilabel}`Project`, {guilabel}`Classification`, {guilabel}`Pipeline`, {guilabel}`Images` and {guilabel}`Results`.

(project-settings)=
## Project tab

Starting with the project settings, basic information about the experiment and the scientist conducting the experiment needs to be collected.

:::{table}
|Title                   |Description                                                      | ...
|-------------           |-----------------------                                          |---------- |
|Working directory       |Storage Directory of the 'to be analyzed' images.                |Mandatory  |
|Experiment name         |Title of the experiment stored together with the results.        |Optional
|Scientist               |Name of the person who is responsible for this analysis.         |Optional   |
|Organization            |Organization responsible for the analysis.                       |Optional   |
|Experiment ID           |UUID of the experiment to globally identify this experiment.     |Optional   |
|Job name                |Name of the job to identify the run (auto generated if empty).   |Mandatory* |
|Group by                |Images may be left ungrouped, or can be grouped by Filename regex or Directory.|Mandatory |
|Filename regex          |If Images are grouped by filename, the regex should indicate the order of the images: Regex to extract plate row, plate column and image index from the image filename.|Mandatory
|Regex test              |Used to test the regex settings. Enter your Image Name and see if the wells are recognized. in the regex test result|   |
|Z-Stack                 |Define how to handle Z-stacks in the images                      |Mandatory  |
|T-Stack                 |Define how to handle T-stacks in the images                      |Mandatory  |
|Well order              |If images are taken from in a (6, 12, 24, 96, 384) well format, the order of the images position in the well can be determined here.|Optional |
|Plate size              |Size of the uses microscopy plate.                               |Optional|
|Notes                   |Some free text notes on the experiment.                          |Optional|
:::

:::{caution}
Make sure that the grouping options and regex settings are correct, as they are needed for valid image sorting and mean well infos.
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
Based on these settings, ImageC performs assignments of the results during a running analysis.
However, if the grouping settings are wrong, these statistics will also be calculated in a wrong way.

When grouping by {guilabel}`Foldername` or {guilabel}`Filename` is selected ImageC will calculate the statistics based on the determined group.
When opening a analysis result (see {doc}`dive into the tutorials <../starting/viewing>`) these calculated values are loaded for a fluid and fast view.

A change of the grouping settings after analysis is currently not supported by ImageC. 
If the grouping settings are changed the analysis has to be repeated.


The {guilabel}`Working Directory` should be set to the folder where the images to be analyzed are stored.
ImageC will perform a recursive folder search with the selected {guilabel}`Working Directory` as the base folder to find all supported image files.
All found files are listed in the {guilabel}`Images` panel.

(images-panel)=
## Images tab

Once a working directory has been selected and the folder scan is complete, all the images found will be listed in the table located in the {guilabel}`Images` tab.

```{figure} images/screenshot_images.png
:class: full-image

ImageC images tab
```

By clicking on an image the OME image information of the selected image is loaded and displayed in the properties table below.
The image selected in this tab is also the image used in the pipeline preview.

## Classification tab

Once a working directory has been selected and the folder scan is complete, all the images found will be listed in the table located in the {guilabel}`Images` tab.

```{figure} images/screenshot_classification.png
:class: full-image

ImageC classification tab
```

## Pipeline tab

By clicking {guilabel}`Add Image Channel` a new channel is added to the analysis settings.
Up to 10 channels can be added.
All predefined EVAnalyzer pipelines are included in this version. 
Select {guilabel}`EV channel` for loading a pipeline (preprocessing, object filtering, detection) optimized for EV quantification from single vesicle imaging images with low background. 
Select {guilabel}`Cell brightfield` for loading a pipeline (preprocessing, object filtering, detection) optimized for cell detection on brightfields images.
Select {guilabel}`Nucleus` for loading a pipeline (preprocessing, object filtering, detection) optimized for nucleus detection after fluorescent labelling of the nuclei (e.g. Hoechst, DAPI).
Select {guilabel}`EV in cell` for loading a pipeline (preprocessing, object filtering, detection) optimized for EV quantification in complex material like cells.
Select 

```{figure} images/screenshot_add_channel.png
:class: full-image

Setting with one added channel
```

When the analysis is started, each defined channels of all images found in the working directory are processed.Non defined channels are not processed.
The results for each channel are stored in a file based database with the extension {file}`.duckdb` for later reporting generation and statistics.

By clicking on a channel, the channel editor is opened.
The channel editor allows to specify channel meta data, preprocessing steps, detection settings as well as filters for objects and images.

```{figure} images/screenshot_channel_editor.png
:class: full-image

Channel editor
```


Defined template settings are stored as JSON template files and stored in the {file}`./templates` directory beside the ImageC binary.

At the right hand side a live preview is displayed.
It shows the resulting object detection after all applied preprocessing steps and filters.
Changing a parameter will directly change the preview, enabling a fast and easy adjustment and fine-tuning of the settings. A live object count is displayed at the bottom of the image.
Based on image size and the complexity of the selected preprocessing algorithms it could take a couple of seconds for refreshing the preview.
The preview can additionally be zoomed in and out and a second window with the original image and the processed image side by side further enables smooth detection setting. 

:::{hint}
See the section [Channels](channels-and-slots) for detailed information about the channel settings parameter.
:::

## Starting the analysis

With the back button on the top left the overview panel is displayed again.
After all channels are added and all needed channel settings are done, the analysis can be started by pressing the {{icon_play}} button on the top.

```{figure} images/screenshot_running.png
:class: small-image

Analysis running
```

A dialogue box informs you about the progress of the analysis.
At the bottom right of the dialog a {guilabel}`Open results folder` button is placed.
Press this button to open the file explorer showing the folder with results of the actual analysis run.

With {guilabel}`Stop` button a running analysis can be interrupted.
It may take a couple of minutes to stop a running analysis since all still in progress tasks have to be finished.

Press the {guilabel}`Close` button to close the dialog after a successful finished analysis run.

