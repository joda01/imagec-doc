(command-classifier-ai)=
## AI classifier

:::{sidebar} AI prediction

The image plane is forwarded to a pre-trained AI model.
The output is an prediction whereby each prediction is assigned to a output class and a confidence.
Using the ImageC AI classifier the predicted output is transformed to classified objects.

```{figure} images/classifier_ai.drawio.svg
:class: full-image
```

:::

```{figure} images/classifier_ai_screenshot.png
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




:::{note}
A manual how to train your own model can be found in the advanced chapter, section [AI training](ai-training).
:::


:::{warning}
AI based object segmentation is still in alpha phase.
It is safe to use but not feature complete yet.
:::