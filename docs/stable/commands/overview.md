---
layout: docu
redirect_from:
- /docs/commands/overview
title: Overview
---

## Image processing

Image processing commands work on [image planes](image-planes) manipulating the input image plane and forwarding the newly image to the command output.
ImageC provides a set of image processing algorithm for different use cases.

In general, image preprocessing serves to minimize the image noise as far as possible (maximizing the signal-to-noise ratio) in order to enable separation between the background and the signal.
An [object segmentation command](commands-object-segmentation) is issued after the image preprocessing.

> Tip Image processing commands get an image as input and have a manipulated image as output.


## Object segmentation

Once objects are segmented, the resulting region of interests have to be classified.
Classification in ImageC is the process of converting regions of interest into objects, assigning each object to a class and calculating object metrics.

ImageC provides an object classifier based on segmented images (e.g. after applying a threshold) and an AI classifier which can directly be applied to an image without the need of segmentation before.

> Tip See chapter [classification](classification) for understanding the fundamentals.
