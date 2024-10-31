(commands-object-classification)=
# Object classification

(classifier)=
## Classifier

Used to extract and classify objects from a binary image containing regions of interest.

(artificial-intelligence)=
## Artificial intelligence

In some cases, it may not be feasible to differentiate between the background and the signal based solely on intensity values.
Images of unlabeled brightfield cells may be such an example for difficult to detect objects using just thresholds.

:::{sidebar} AI models

ImageC supports AI models in ONNX format.
Compatible models can be downloaded from [imagec.org](https://imagec.org).
A manual how to train your own model can be found in the advanced chapter, section [AI training](ai-training).

:::

In such use cases, ImageC permits the utilization of artificial intelligence models for object segmentation as an alternative to thresholding techniques.

ImageC compatible models for object segmentation can be downloaded from [imagec.org](https://imagec.org) below the Download section.
Copy the downloaded model to the {file}`./path/to/ImageC/models` folder.
ImageC will load all models from this folder automatically on startup and provides them in the {guilabel}`AI model` dropdown for selection.

In contrast to the threshold, a minimum probability is now specified.
All detected object with a minimum probability higher than this value will be used.

:::{note}
AI based object segmentation is still in alpha phase.
It is safe to use but not feature complete yet.
:::