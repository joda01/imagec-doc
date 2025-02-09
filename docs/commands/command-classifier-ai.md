(command-classifier-ai)=
# AI classifier

:::{sidebar} AI prediction

The image plane is forwarded to a pre-trained AI model.
The output is an prediction whereby each prediction is assigned to a output class and a confidence.
Using the ImageC AI classifier the predicted output is transformed to classified objects.

```{figure} images/classifier-ai.drawio.svg
:class: full-image
```

:::

```{figure} images/classifier-ai-screenshot.png
:class: small-image
```

In some cases, it may not be feasible to differentiate between the background and the signal based solely on intensity values.
This makes the use of threshold as a segmentation technique impractical in such situations.
To overcome this limitation ImageC allows the use of artificial intelligence models for object segmentation and classification as an alternative to threshold techniques.


## Deep learning models

:::{sidebar} AI model support

ImageC is compatible with a wide range of models of [BioImage Model Zoo](https://bioimage.io/#/)
ImageC compatible models for object segmentation can be downloaded from [imagec.org](https://imagec.org) below the Download section.
Copy the downloaded model to the {file}`./models` folder.
ImageC will load all models from this folder automatically on startup and provides them in the {guilabel}`AI model` dropdown for selection.

:::

On startup ImageC searches the `./models` folder for compatible AI models and presents them in the drop-down menu for selection.
In the actual implementation of ImageC [YoloyV5](https://github.com/ultralytics/yolov5) and [U-Net](https://www.sciencedirect.com/topics/computer-science/u-net#:~:text=U%2DNet%20is%20a%20fully%20convolutional%20encoder%2Fdecoder%20structure%20aimed,size%20via%20an%20upsampling%20method.) model architecture are supported.

ImageC expects a `rdf.yaml` file beside the weight file.
This resource definition file according to the bio image zoo schema [rdf definition](https://bioimage-io.github.io/spec-bioimage-io/bioimageio_schema_latest/index.html) describes the model input and output parameters required by ImageC for correct interpretation of the prediction output.

After downloading a new model, either from [ImageC AI models](https://imagec.org/ai-models.html) or [BioImage Model Zoo](https://bioimage.io/#/), unzip the content and copy the unpacked folder to the `./models` directory {{icon_open}} of the ImageC installation directory.
Press the refresh button {{icon_refresh}} and select the model from the {guilabel}`model path` dropdown.

Most of the settings are taken automatically based on the parsed information of the `rdf.yaml` file.
For non onnx models the number of model classes must be set manually.

:::{note}
Select the number of output classes and select an ImageC object class to associate with each output class.
:::

## Deep learning engines

ImageC actually includes the engines PyTorch and OnnxRuntime.

Using PyTorch, [TorchScript](https://pytorch.org/docs/stable/jit.html) models are supported, with OnnxRuntime all models saved on [onnx](https://onnx.ai/) format can be used.

:::{important}
ImageC supports PyTorch TorchScript format and OnnxRuntime's onnx format.
:::



The provided AI classifier combines object segmentation and classification in one command since both is done by the trained AI model in one step.
When an image is forwarded to the AI model, the result is a prediction of objects, with each predicted object having a confidence and being assigned to an AI output class.
ImageC AI classifier providers a filter tab for each possible output class of the AI model.
These filters can be used to assign the predicted output classes of the AI model to an ImageC object class.

## Thresholds

Thresholds in the context of AI are probability thresholds which define the minimum probability of a detection output to mark the prediction as valid.

### Mask threshold

A typical output of an AI model for image segmentation is a matrix containing a probability value for each pixel, where each of these probability values represents the probability that the pixel belongs to the background or to the foreground.

The mask threshold defines the minimum probability required for a pixel to be defined as a foreground pixel.

### Class threshold

The class threshold is a probability value ranging from zero to one, where one represents 100%.
Once the image has been processed by the AI network, a matrix of probabilities is created.
One of these probabilities is the probability that a detected object can be assigned to one of the defined classes.

With the class threshold, it is possible to define the minimum probability that a detected object must have in order to be identified as an object of a class. 


---

## Experimental
### Probability handicap

:::{warning}
This is an experimental feature.
:::

The probability handicap allows to define a handicap for the resulting probabilities of a class.
The resulting probabilities for the class probability the handicap was defined for are multiplied by this handicap value.
This allows to add an additional manual defined weight for wanted prediction classes.

Possible applications are adding a handicap > 1 to classes with less training data.
Such classes may have poor prediction accuracy, this may be compensated with a handicap value.


:::{note}
A manual how to train your own model can be found in the advanced chapter, section [AI training](ai-training).
:::


:::{warning}
AI based object segmentation is still in alpha phase.
It is safe to use but not feature complete yet.
:::
