---
layout: docu
title: Frequently Asked Questions
---

<!-- ################################################################################# -->
<!-- ################################################################################# -->
<!-- ################################################################################# -->

## Overview

<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### Who develops ImageC?

<div class="answer" markdown="1">

ImageC is an open source project initiated as a leisure project by Joachim Danmayr and Melanie Schürz in cooperation with the [Paris Lodron University of Salzburg](https://www.plus.ac.at/) and the [Ludwig Boltzmann Institute for Nanovesicular Precision Medicine](https://nvpm.lbg.ac.at/).


</div> 

</div>

<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### Why call it ImageC?

<div class="answer" markdown="1">

Inspired by [ImageJ](https://imagej.net/ij/) a <b>J</b> AVA written image processing tool for single image processing, ImageC is a high throughput image processing tool written in <b>C</b>++.

</div>

</div>

<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### Is ImageC open-source?

<div class="answer" markdown="1">

ImageC is fully open-source under the [AGPL-3.0](https://github.com/joda01/imagec?tab=AGPL-3.0-1-ov-file#readme) license and its development takes place [on GitHub in the `joda01/imagec` repository](https://github.com/joda01/imagec).
ImageC is available as a free version under this license for non commercial use.

</div>

</div>


<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### I would like to request a new feature for ImageC. How do I proceed?

<div class="answer" markdown="1">



* Use the [ImageC forum](https://forum.image.sc/tag/imagec/) to discuss your new feature idea.
* Once accepted one of the ImageC contributors will create an [github issue](https://github.com/joda01/imagec/issues) linking to the forum post.


</div>

</div>

<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### I found a bug or have a question. What should I do?

<div class="answer" markdown="1">



* Have a look to the [ImageC forum](https://forum.image.sc/tag/imagec/), probably your question is still answered there.
* If not open a new thread in the forum with the `imagec` tag.

If you are really sure you found a bug you can directly create an issue on the [github issues page](https://github.com/joda01/imagec/issues).


</div>

</div>


<!-- ################################################################################# -->
<!-- ################################################################################# -->
<!-- ################################################################################# -->

## Performance

<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### Do I need a super computer to run ImageC?

<div class="answer" markdown="1">

No! ImageC is designed having a low performance footprint and can also be executed on a normal home PC or Laptop.
For the minimum hardware requirements refer to the section [Resources and limits]({% link docs/stable/technical/limits.md %}).

</div>

</div>

<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### My pipelines run very slow what should I do?

<div class="answer" markdown="1">

There are many factors which influences the processing speed of your pipelines.
Here are a few rules of thumb: 

* Bigger images needs longer to analyze.
* The longer the pipeline, the longer the analysis time.
* The more objects detected in the image, the longer the analysis time.
* Rolling ball, Watershed and Median rank filter are commands which costs a lot of time.
* Classical object segmentation is faster than AI object detection.

ImageC tries to use all your available CPU cores to run the analysis.
Using a PC with multiple cores can significantly increase processing time.

</div>

</div>

<!-- ################################################################################# -->
<!-- ################################################################################# -->
<!-- ################################################################################# -->

## Use Cases for ImageC


<!-- ----- ----- ----- ----- ----- ----- Q&A entry ----- ----- ----- ----- ----- ----- -->

<div class="qa-wrap" markdown="1">

### What are typical use cases for ImageC?

<div class="answer" markdown="1">

ImageC was developed in a group of biologists specialized on nano vesicle.
Therefore one of the main use cases for ImageC is identifying spots in fluorescence microscopy images, counting them and calculate the colocalization of them.

However, ImageC is highly flexible and can be used in fields other than biology. For instance, it could be used in astronomy to count the stars in the sky.

In a nutshell in every application you have the need to automatically quantify images and automate this process.

</div>

</div>

