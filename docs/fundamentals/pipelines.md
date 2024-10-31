(pipelines)=
# Pipelines

Clicking on an pipeline in the {guilabel}`Pipelines` tab opens the pipeline settings panel.

```{figure} images/screenshot_open_pipeline.png
:class: full-image
```

(channels-meta)=
## Pipeline meta

The {guilabel}`Pipeline meta` section is used to specify some basic channel information.

The {guilabel}`Pipeline name` input allows you to give the pipeline a meaningful name.
It is recommended to not use the same name for two pipelines in the same project to make failure analyzes much more easier.

## Pipeline input

The {guilabel}`Pipeline input` defines the image plane which should be used as a starting point for this pipeline.
Mandatory field is the {guilabel}`Image channel`.

If the {guilabel}`Z-Stack` setting in the {guilabel}`Project` tab is set to {guilabel}`Intensity Projection`, it is necessary to select which intensity projection mode is to be used for the input channel of the images by selecting the {guilabel}`Z-Projection` mode.
If the the {guilabel}`Z-Stack` setting in the {guilabel}`Project` tab is set to {guilabel}`Each one`, not additional settings have to be taken for the z-stack. Each z-stack is processed individually.
If the {guilabel}`Z-Stack` setting in the {guilabel}`Project` tab is set to {guilabel}`Exact one`, it is necessary to specify which z-stack index to use for analysis, the default being zero (0).

Same settings have to be taken for the t-stack depending on taken {guilabel}`T-Stack` settings in the {guilabel}`Project` tab.

In addition to start with an image plane as input it is also possible to start with an {guilabel}`Empty` image.
Using a blank image is useful for use cases where you are working with objects from a previous pipeline without having to extract objects again.


## Pipeline output

Some of the processing steps are used to extract objects from the input images.
Each detected object is [classified](classification) by assigning to exact on cluster and class.
The settings in this section allow you to specify the default cluster and class that will be used for each detected object, unless specified otherwise within a pipeline step.


## Pipeline steps

The goal of each pipeline is to extract regions of interest from an image input plane and store these regions of interest as objects for further object processing.
For this purpose, ImageC provides a large number of commands that can be used for this purpose.

By clicking on the **--- + ---** button within the pipeline step section the command selection dialog is opened.
This dialog shows all commands that can be used at this point.
Double-click to insert the command at the specified position.


```{figure} images/screenshot_command_selection.png
:class: small-image
```

Commands are classified into four principal categories: image processing commands (gray), object detection commands (white), object classification commands and object post-processing commands (green).

1. First of all image processing commands are used to reduce the image noise as much as possible.
2. Object detection commands are used to separate foreground from background by using threshold algorithms and convert the grey scale image to a binary image.
3. In the next step an object classification command is used to extract region of interests from the grey scale image and classify them to objects.
4. Object postprocessing and filter commands can be used to do further processing or filtering on the detected objects.




