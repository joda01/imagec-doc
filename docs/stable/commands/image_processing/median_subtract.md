---
layout: docu
redirect_from:
- /docs/commands/median-subtract
title: Median subtract
---

> Deprecated Use [Rank filter]({% link docs/stable/commands/image_processing/rank_filter.md %}) in combination with [Image math]({% link docs/stable/commands/image_processing/image_math.md %}) instead for future projects!

<img src="{{ site.baseurl }}/images/commands/median-subtract-screenshot.png" alt="Screenshot" style="width: 30%; height: auto;">


Median subtraction is a sort of noise filtering which can be used to reduce background noise similar to the [rolling ball]() algorithm.
Behind the scenes a rank filter is used to calculate the median of the image intensity, which is subtracted afterwards from the original image.

The kernel size defines the window size used for the rank filter to calculate the median.
Bigger kernels reduces more details from the image than smaller ones.






