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
:class: tiny-image
```



In some cases, it may not be feasible to differentiate between the background and the signal based solely on intensity values.
This makes the use of threshold as a segmentation technique impractical in such situations.
To overcome this limitation ImageC allows the use of artificial intelligence models for object segmentation and classification as an alternative to threshold techniques.

:::{sidebar} AI models

ImageC compatible models for object segmentation can be downloaded from [imagec.org](https://imagec.org) below the Download section.
Copy the downloaded model to the {file}`./path/to/ImageC/models` folder.
ImageC will load all models from this folder automatically on startup and provides them in the {guilabel}`AI model` dropdown for selection.

:::

The provided AI classifier combines object segmentation in classification in one command since both is done by the trained AI model in one step.
When an image is fed to the AI model, the result is a prediction of objects, with each predicted object having a confidence and being assigned to an AI output class.
ImageC AI classifier providers a filter tab for each possible output class of the AI model.
Using these filter tabs, it is now possible to assign the prediction to an ImageC object class, in addition to applying some pre-filtering.

## Class threshold

The class threshold is a probability value from in the range of zero to one, with one stands for 100%.
Once the image was processed by the AI net, a matrix of probabilities is created.
One of these probabilities is the probability that a detected object can be assigned to one of the defined classes.

With the class threshold it is possible to define the minimum probability a detected object must have to be identified as object of a class. 

## Mask threshold

In the addition to the probability of being a specific object the probabilities of the object borders are also part of the resulting probability matrix.
The mask threshold defines the minimum probability of a pixel value needed to assign this pixel value to a specific object.

Higher mask probability values lead to a more accurate shape of the object.

## Probability handicap

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