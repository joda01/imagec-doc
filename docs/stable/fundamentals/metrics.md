---
layout: docu
redirect_from:
- /docs/fundamentals/metrics
- /docs/fundamentals/metrics
title: Metrics
---

During an analysis ImageC measures a couple of metrics of each detected [object]({% link docs/stable/fundamentals/objects.md %}).
All the measured data are stored in a SQL database on disk (internally we are using [DuckDB](https://duckdb.org/)).
Once the analysis is finished the collected data can be displayed within the ImageC results viewer and either be exported to **XLSX** or **R** afterwards.

However, as the number of data generated can be very large, ImageC allows to choose which data to display in the result view.
One way to specify the columns to show is using the [class edit]({% link docs/stable/first_steps/operation.md %}#classification-tab) dialog in the classification tab.

<img src="../first_steps/images/screenshot_classification_editor.png" alt="Class editor" style="width: 30%; height: auto;">


When the result file is opened after a run, ImageC displays the result columns as specified there.
Even if a column is not specified, the metric is still measured and can be added at any time, even after the analysis has been completed.


## Metrics and Statistics {#metrics-and-statistics}

A measurement in the context of ImageC is a metrics calculated during the analysis for an object.
The statistics is applied to the selected measurement.
The following table gives an overview of the valid combinations of metics and statistics which are available.

### Plate view

|Measurement             |Statistics           |Description                                                                     |
|-------------           |---------------------|-----------------------                                                         | 
|Count                   |CNT                  |The average of the object number per image in the well.                         |
|Intersection            |CNT                  |The average of the number of objects A intersecting with object class B per image in the well.                 |
|Area size               |AVG                  |The average of the average object area sizes per image in the well.             |
|Area size               |MEDIAN               |The average of the median of the object area sizes per image in the well.       |
|Area size               |MIN                  |The average of the minimum of the object area sizes per image in the well.      |
|Area size               |MAX                  |The average of the maximum of the object area sizes per image in the well.      |
|Area size               |STDEV                |The average of the standard deviations of the object area sizes per image in the well.  |
|Area size               |SUM                  |The average of the sum of the object area sizes per image in the well.          |
|Area size               |CNT                  |The average number of objects per image in the well used to calculate the statistics.|
|Perimeter               |AVG                  |The average of the average object perimeters per image in the well.             |
|Perimeter               |MEDIAN               |The average of the median of the object perimeters per image in the well.       |
|Perimeter               |MIN                  |The average of the minimum of the object perimeters per image in the well.      |
|Perimeter               |MAX                  |The average of the maximum of the object perimeters per image in the well.      |
|Perimeter               |STDEV                |The average of the standard deviations of the object perimeters per image in the well.  |
|Perimeter               |SUM                  |The average of the sum of the object perimeters per image in the well.          |
|Perimeter               |CNT                  |The average number of objects per image in the well used to calculate the statistics.|
|Circularity             |AVG                  |The average of the average object circularities per image in the well.          |
|Circularity             |MEDIAN               |The average of the median of the object circularities per image in the well.    |
|Circularity             |MIN                  |The average of the minimum of the object circularities per image in the well.   |
|Circularity             |MAX                  |The average of the maximum of the object circularities per image in the well.   |
|Circularity             |STDEV                |The average of the standard deviations of the object circularities per image in the well.  |
|Circularity             |SUM                  |The average of the sum of the object circularities per image in the well.        |
|Circularity             |CNT                  |The average number of objects per image in the well used to calculate the statistics.|
|Intensity (min/max/avg) |AVG                  |The average of the average object intensities per image in the well.             |
|Intensity (min/max/avg) |MEDIAN               |The average of the median of the object intensities per image in the well.       |
|Intensity (min/max/avg) |MIN                  |The average of the minimum of the object intensities per image in the well.      |
|Intensity (min/max/avg) |MAX                  |The average of the maximum of the object intensities per image in the well.      |
|Intensity (min/max/avg) |STDEV                |The average of the standard deviations of the object intensities per image in the well.  |
|Intensity (min/max/avg) |SUM                  |The average of the sum of the object intensities per image in the well.          |
|Intensity (min/max/avg) |CNT                  |The average number of objects per image in the well used to calculate the statistics.|


### Well view

|Measurement             |Statistics           |Description                                                                     |
|-------------           |---------------------|-----------------------                                                         | 
|Count                   |CNT                  |The number of detected objects in the image.                       |
|Intersection            |CNT                  |The number of objects A intersecting with object class B in the image.               |
|Area size               |AVG                  |The average object area sizes in the image.           |
|Area size               |MEDIAN               |The median of the object area sizes in the image.     |
|Area size               |MIN                  |The minimum of the object area sizes in the image.    |
|Area size               |MAX                  |The maximum of the object area sizes in the image.    |
|Area size               |STDEV                |The standard deviations of the object area sizes in the image.|
|Area size               |SUM                  |The sum of the object area sizes in the image.        |
|Area size               |CNT                  |The number of objects in the image used to calculate the statistics.|
|Perimeter               |AVG                  |The average object perimeters in the image.           |
|Perimeter               |MEDIAN               |The median of the object perimeters in the image.     |
|Perimeter               |MIN                  |The minimum of the object perimeters in the image.    |
|Perimeter               |MAX                  |The maximum of the object perimeters in the image.    |
|Perimeter               |STDEV                |The standard deviations of the object perimeters in the image.|
|Perimeter               |SUM                  |The sum of the object perimeters in the image.        |
|Perimeter               |CNT                  |The number of objects in the image used to calculate the statistics.|
|Circularity             |AVG                  |The average object circularities in the image.        |
|Circularity             |MEDIAN               |The median of the object circularities in the image.  |
|Circularity             |MIN                  |The minimum of the object circularities in the image. |
|Circularity             |MAX                  |The maximum of the object circularities in the image. |
|Circularity             |STDEV                |The standard deviations of the object circularities in the image.|
|Circularity             |SUM                  |The sum of the object circularities in the image.      |
|Circularity             |CNT                  |The number of objects in the image used to calculate the statistics.|
|Intensity (min/max/avg) |AVG                  |The average object intensities in the image.           |
|Intensity (min/max/avg) |MEDIAN               |The median of the object intensities in the image.     |
|Intensity (min/max/avg) |MIN                  |The minimum of the object intensities in the image.    |
|Intensity (min/max/avg) |MAX                  |The maximum of the object intensities in the image.    |
|Intensity (min/max/avg) |STDEV                |The standard deviations of the object intensities in the image.|
|Intensity (min/max/avg) |SUM                  |The sum of the object intensities in the image.        |
|Intensity (min/max/avg) |CNT                  |The number of objects in the image used to calculate the statistics.|

### Image view

|Measurement             |Statistics           |Description                                           |
|-------------           |---------------------|-----------------------                               | 
|Intersection            |-                    |The number of objects intersecting with this object.  |
|Area size               |-                    |The object area size.                                 |
|Perimeter               |-                    |The object perimeters.                                |
|Circularity             |-                    |The object circularity.                               |
|Intensity min           |-                    |The object min intensity.                             |
|Intensity max           |-                    |The object max intensity.                             |
|Intensity avg           |-                    |The object avg intensity.                             |
|Center of mass X        |-                    |X coordinates of the center of mass of the object in the image. |
|Center of mass Y        |-                    |Y coordinates of the center of mass of the object in the image. |
|Object ID               |-                    |Unique object ID.                                     |
|Origin object ID        |-                    |If it was copied by reclassify this is the Object ID of the object this object was copied from. If not copied the value is 0.|
|Parent object ID        |-                    |If the object was reclassified using intersection, this is the Object ID of the object this object was intersecting with. If not reclassified the value is 0. |
|Tracking ID             |-                    |If the object has been tracked e.g. by coloc or timeframe, all related objects will have the same tracking ID. The table is sorted by Tracking ID.                         |