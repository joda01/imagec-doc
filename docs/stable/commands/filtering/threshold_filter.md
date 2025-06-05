---
layout: docu
redirect_from:
- /docs/commands/threshold-filter
title: Threshold filter
---

<a href="{{ site.baseurl }}/images/commands/threshold-filter-screenshot.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/threshold-filter-screenshot.png" style="width: 30%" alt="Loading ..."/></a>


To get comparable results in one experiment, it is common to use the same manual threshold value for all images.
Nevertheless, given the considerable range of exposure times for images, it is possible that the selected threshold value may prove insufficient for some images.
This leads to a kind of overexposed image after the threshold, in which the background is erroneously recognized as a signal.

To filter out images that are affected by this problem, ImageC offers a  `Threshold filter` filter.
In the event that the selected threshold value is less than the value observed at the maximum of the image histogram, multiplied by the aforementioned factor, the filter is applied.



> The intensity value at the maximum of the histogram of the image multiplied by the `Threshold filter` defines the area of allowed threshold values for the image.
> If the min. threshold value is lower than the lowe bound of this area, the image id filtered out.
> 
> <a href="{{ site.baseurl }}/images/commands/threshold-filter.drawio.svg" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/threshold-filter.drawio.svg" style="width: 30%" alt="Loading ..."/></a>
