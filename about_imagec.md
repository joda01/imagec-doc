---
layout: docu
title: About ImageC
---

When we started our research, we were faced with the challenge of quantifying a large number of images taken using our microscopes.
The number of images grow and grow thanks to new microscopy technologies which allows automatically image generations.

Starting with the search for a low cost / free tool which could help us to taming the amount of data we came up with a couple of tools including [ImageJ](https://imagej.net/ij/), [CellProfiler](https://cellprofiler.org/) and a couple of other smaller applications.

All of them are feature rich but non fulfil our requirements for an easy to use tool which can do reproducible data quantification.

This was the starting point of [EVAnalyzer1](https://github.com/joda01/evanalyzer) a ImageJ plugin which automats a lot of processes in quantification of images in the research field of extracellular vesicles.
[EVAnalyzer1](https://github.com/joda01/evanalyzer) allows to do batch processing for hundreds of images including a couple of predefined often used functions like, counting and colocalization measurement of spots in images.

Over time the applications get more and more complex beginning with the switch from in vitro to in vivo.
Histological images are large and require more effort to analyze.
Further applications, such as serum assays, made the processing algorithms even more complex.

Even for more complex applications we wanted to provide a easy to use tool, but it has to be more flexible then [EVAnalyzer1](https://github.com/joda01/evanalyzer).
So the development of ImageC alias EVAnalyzer2 started.

It should be a standalone application that bridges the gap between applications such as ImageJ, which excel at processing single images and provide a wide range of toolboxes, and applications such as CellProfiler, which also provide a large number of plugins, but which may be more complex to use and require a deep understanding of image processing.


## What makes ImageC

### Easy

ImageC's focus was on simple as possible usage providing a modern graphical user interface.
We decided against a PlugIn mechanism to keep the application simple and harmonized providing a well selected and documented amount of processing algorithms.

### Portable

ImageC users don't need to install any third-party software or plugins, and the application is not dependent on any other software.
To take the simple, stupid approach, just download, unzip and start ImageC.
Even those with no experience of computers should be able to use complex image-processing algorithms using ImageC.

In addition ImageC is provided for Linux, Windows and macOS (in progress).
ImageC is the same independent on which host system you start it.
Pipelines can shared across the operating systems without loosing any functionality.


### Fast

ImageC has a focus on really high throughput image processing.
That's why it was written in C++, one of the fastest programming languages, to get the most out of your computer.

A side effect of this approach is that the ImageC software can be used on standard laptops, eliminating the need for expensive hardware, even for complex pipelines.

### Free

The philosophy behind ImageC was to give everyone the opportunity to perform complex image processing and analysis. 
Even small laboratories without the funds to purchase expensive proprietary software should be able to conduct their research with ImageC.

Consequently, ImageC will continue to be made available at no cost to non-commercial organizations in the future.

ImageC was created as an unpaid leisure project. 
The programmer does not earn any money with it and does not receive any payment, therefore we appeal to the idea of fair use and ask companies or provit organizations to get in contact if they tend to use it.

## Who is ImageC

ImageC is an open source project initiated as a leisure project by Joachim Danmayr and Melanie Schürz.


## Acknowledgements

ImageC draws inspiration from scientific publications and uses components from various open-source projects. 
Thanks to all of them, but especially to:

* [ImageJ](https://imagej.net/ij/) as it provides a big set of image processing algorithm which some of them I ported to C++ for ImageC.
* [CellProfiler](https://cellprofiler.org/) for giving the idea of building processing pipelines.
* The [openCV](https://opencv.org/) open source project which builds the basis for most of the implemented image processing algorithms.
* To the developers if [QT](https://www.qt.io/) which libraries I used to build up the ImageC graphical user interface.
* Many thanks to the [BioFormats](https://www.openmicroscopy.org/bio-formats/) project which is used to decode and open the different image formats.
* Thanks to the developers of [DuckDB](https://duckdb.org/) the fast feature rich database which I used in the background for data storage and inspired me with their excellence documentation.


Last but not least the biggest thanks go to to the team of the [AG Meisner-Kober](https://www.plus.ac.at/biosciences/the-department/research-groups/meisner-kober/?lang=en) at the [Paris Lodron University of Salzburg](https://www.plus.ac.at/) and the [Ludwig Boltzmann Institute for Nanovesicular Precision Medicine](https://nvpm.lbg.ac.at/) who made the project possible driven by their own needs and actively supported the realization and testing.



