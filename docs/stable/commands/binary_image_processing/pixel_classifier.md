---
layout: docu
redirect_from:
- /docs/commands/pixel-classifier
title: Pixel classifier
---

The objective of a pixel classifier is to categorize each pixel in an image according to predefined criteria.
The most simple implementation of a pixel classifier is a [threshold]({% link docs/stable/commands/binary_image_processing/threshold.md %}).
A threshold classifies pixels with an intensity value above a defined threshold value as foreground and pixels below as background.

In more complex scenarios, using just one threshold value may be insufficient.
Furthermore, different criteria can be employed alongside simple intensity to categorize a pixel.
Also the number of classes does not need to be limited to just two (foreground and background).

A pixel classifier assigns a specific class or category to each pixel in an image, a task known as semantic segmentation. 

For building a pixel classifier, machine learning algorithms can be used.
ImageC provides a couple of ml algorithms which are documentation in section [Machine Learning]({% link docs/stable/machine_learning/training.md %}).

Using the `Pixel classifier` command pre-trained models can be loaded.
The pixel classifier command takes a 16-bit grayscale image as input and produces a binary image, where each pixel's value corresponds to the recognized class.

An object classifier can be run after the pixel classifier to extract objects from the categorized pixels.

>  The pixel classifier transforms a grayscale image to a classified image, whereby each pixel $$p_x$$ gets a value from $$c=\{0...N\}$$ with c is the class the pixel belongs to.
>
> <a href="{{ site.baseurl }}/images/commands/pixel-classifier.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/pixel-classifier.drawio.svg" style="width: 50%" alt="Loading ..."/></a>
>