(pipelines)=
# Pipelines

Clicking on an pipeline in the {guilabel}`Pipelines` tab opens the pipeline settings panel.

```{figure} images/screenshot-open-pipeline.png
:class: full-image
```

The final goal of a pipeline in ImageC is to get objects (see section [Classification](classification)).
Objects can either be extracted from an image plane based on a region of interest using image processing and classification algorithms, or constructed from an existing set of objects using object math.

A typical way to get the wanted objects from an image is first the define the image plane to process, set classification information for the extracted objects, add image preprocessing and classification steps, do some object math and filtering.

Finally, the extracted objects are stored in the resulting database along with their object metrics.


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

Same settings have to be taken for the time stack depending on taken {guilabel}`T-Stack` settings in the {guilabel}`Project` tab.

In addition to start with an image plane as input it is also possible to start with an {guilabel}`Empty` image.
Using a blank image is useful for use cases where you are working with objects from a previous pipeline without having to extract objects again.


## Pipeline output

Some of the processing steps are used to extract objects from the input images.
Each detected object is [classified](classification) by assigning to exact on class.
The settings in this section allow you to specify the default class that will be used for each detected object, unless specified otherwise within a pipeline step.


## Pipeline steps

:::{sidebar} Commands

Commands are used to manipulate the input image, extract objects or to work on exiting objects.
A command takes either an image plane or objects as input and returns a manipulated image or objects as output.
In other words, based on the command category, the command either works on images or objects, or transforms an image into an object or vice versa.


This brings us to four principal categories of commands: image processing commands (gray), object segmentation commands (white), object classification commands and object post-processing commands (green).

As not every sequence of commands is possible in a meaningful way, ImageC indicates which command can be connected to the previous one.

```{image} images/command-description.drawio.svg
:class: full-image
```

:::

The goal of each pipeline is to extract regions of interest from an image input plane and store these regions of interest as objects for further object processing.
ImageC provides a wide range of commands that can be used for this purpose.

By clicking on the **--- + ---** button within the pipeline step section, the command selection dialog is opened.
Commands are classified into four principal categories: image processing commands (gray), object segmentation commands (white), object classification commands and object post-processing commands (green).

When opening the command selection dialogue, this dialogue shows all the available commands that can be used at this pipeline position.
Double-click to insert the command.


```{figure} images/screenshot-command-selection.png
:class: small-image
```

A typical pipeline flow might look like this:

1. First of all image processing commands are used to reduce the image noise as much as possible.
2. Object segmentation commands are used to separate foreground from background by using threshold algorithms and convert the grey scale image to a binary image.
3. In the next step an object classification command is used to extract region of interests from the grey scale image and classify them to objects.
4. Object postprocessing and filter commands can be used to do further processing or filtering on the detected objects.




