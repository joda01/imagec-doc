---
layout: docu
redirect_from:
- /docs/commands/classifier
title: Classifier
---

<a href="{{ site.baseurl }}/images/commands/classifier-screenshot.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/classifier-screenshot.png" style="width: 30%" alt="Loading ..."/></a>


The Classifier command is used to convert regions of interest, formally extracted from the image using a segmentation algorithm such as [threshold]({% link docs/stable/commands/binary_image_processing/threshold.md %}), into objects, where each object is assigned to an object class.
For [classified]({% link docs/stable/fundamentals/classification.md %}) objects metrics are calculated, they are stored to the resulting database and can be used in further object-processing steps.


ImageC's classifier provides several filter methods which can be used to to filter out artefact.
All objects which match the filter criteria are assigned to the `match` class, objects not matching the filter criteria are assigned to the `no match`.
The filter can be set for each [threshold classes]({% link docs/stable/commands/binary_image_processing/threshold.md %}#threshold-classes) individually.
This allows the classifier to assign each ROI of a [threshold classes]({% link docs/stable/commands/binary_image_processing/threshold.md %}#threshold-classes) to a specific match and no match object class.
Use the {{icon_add}} button to add as many filters as needed.
As a rule, one filter for each threshold class is used.

> Tip See section [Objects]({% link docs/stable/fundamentals/objects.md %}) for more detailed information about object metrics.



> Objects are extracted from a binary image representing thee regions of interest of the image.
> For each extracted object a class is assigned and metrics are measured.
> Objects are stored to the resulting database and can be used in further pipeline steps.
> 
> <a href="{{ site.baseurl }}/images/commands/classifier.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/classifier.drawio.svg" style="width: 40%" alt="Loading ..."/></a>

