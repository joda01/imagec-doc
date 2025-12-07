---
layout: docu
redirect_from:
- /internals/tutorials/evanalyzer/spot-count
title: Spot count
---

The "Spot Count" template was migrated from EVAnalyzer1 and provides a simple pipelines for detecting EVs/spots in fluorescence microscopy images.

Spots are detected in one image channel using the EV pipeline, while the Tetraspeck pipeline locates reference beads in another channel. 
To ensure accurate EV identification, all spots matching Tetraspeck bead positions are filtered out.

### EV Detection


<div style="display:flex; align-items:flex-start; gap:16px;">
<a href="{{ site.baseurl }}/images/tutorials/spot-count-pipeline-01.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/tutorials/spot-count-pipeline-01.png" style="width: 150px; height:auto;" alt="Loading ..."/></a>

  <p style="margin:0;">
      <ul>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/image_processing/rolling_ball">Rolling Ball</a>: Remove background noise and exposer invariance.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/image_processing/blur">Smoothing</a>: Remove noise artifacts.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/binary_image_processing/threshold">Threshold</a>: Has to be <b>adapted manually</b> to distinguish between background and foreground.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/binary_image_processing/watershed">Watershed</a>: Separate spots which are close together.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/classification/classifier">Object classifier</a>: Assign the spot class to the extracted foreground regions</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/measurement/measure_intensity">Measure intensity</a>: Measure the intensity of the found spots. Add other image channel if wanted.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/object_processing/save_control_image">Save control image</a>: Save a control image. Remove this command if not needed.</li>
    </ul>
  </p>
</div>


### Tetraspeck


<div style="display:flex; align-items:flex-start; gap:16px;">
<a href="{{ site.baseurl }}/images/tutorials/spot-count-pipeline-02.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/tutorials/spot-count-pipeline-02.png" style="width: 150px; height:auto;" alt="Loading ..."/></a>

  <p style="margin:0;">
      <ul>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/image_processing/rolling_ball">Rolling Ball</a>: Remove background noise and exposer invariance.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/image_processing/blur">Smoothing</a>: Remove noise artifacts.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/binary_image_processing/threshold">Threshold</a>: Has to be <b>adapted manually</b> to distinguish between background and foreground.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/binary_image_processing/watershed">Watershed</a>: Separate spots which are close together.</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/classification/classifier">Object classifier</a>: Assign the spot class to the extracted foreground regions</li>
        <li><a href="{{ site.baseurl }}/docs/stable/commands/object_processing/reclassify">Reclassify</a>: Assigns to all spots found in EV detection pipeline the class Tetraspeck which intersects with a spot found in this pipeline. So this step is used to remove the Tetraspecks from the group of EVs.</li>
    </ul>
  </p>
</div>

## Advanced

Below the JSON representation of the template project is shown.
This JSON can be used together with the ImageC [CLI]({% link docs/stable/cli/cli.md %}) functionality to script the detection process.

```json
{
  "configSchema": "https://imagec.org/schemas/v1/analyze-settings.json",
  "imageSetup": {
    "imageTileSettings": {
      "tileHeight": 4096,
      "tileWidth": 4096
    },
    "series": 0,
    "tStackHandling": "EachOne",
    "zStackHandling": "ExactOne"
  },
  "imagecMeta": {
    "buildTime": "2025-05-18 08:49:40",
    "imagecVersion": "v1.0.0-beta.17"
  },
  "meta": {
    "author": "Melanie Schuerz",
    "organization": "University of Salzburg",
    "color": "#B91717",
    "group": "EVAnalyzer",
    "icon": "",
    "modifiedAt": "2025-05-19T08-10-55",
    "name": "Spot count",
    "notes": "Count the number of spots in an image channel.",
    "revision": "1.0",
    "tags": ["fluorescence","count"],
    "uid": ""
  },
  "pipelines": [
    {
      "disabled": false,
      "history": [],
      "locked": false,
      "meta": {
        "color": "#B91717",
        "group": "ev",
        "icon": "",
        "name": "EV Detection",
        "notes": "1. output class can be renamed in classification tab (ch1@.. can be e.g. GFP@...)\n2. Select EV image channel\n3. Adapt manual threshold\n4. Object can be gated by size/circularity in \"Classifier\"\n",
        "revision": "Coun",
        "tags": [
          "ev",
          "evs",
          "extracellular vesicle"
        ],
        "uid": ""
      },
      "pipelineSetup": {
        "cStackIndex": -2,
        "defaultClassId": "0",
        "source": "FromFile",
        "tStackIndex": -1,
        "zProjection": "MaxIntensity",
        "zStackIndex": -1
      },
      "pipelineSteps": [
        {
          "$rollingBall": {
            "ballSize": 4,
            "ballType": "Paraboloid"
          },
          "disabled": false,
          "locked": true
        },
        {
          "$blur": {
            "kernelSize": 3,
            "mode": "Blur",
            "repeat": 2
          },
          "disabled": false,
          "locked": true
        },
        {
          "$threshold": {
            "modelClasses": [
              {
                "cValue": 0,
                "method": "Manual",
                "pixelClassId": 1,
                "thresholdMax": 65535,
                "thresholdMin": 200
              }
            ]
          },
          "disabled": false,
          "locked": false
        },
        {
          "$watershed": {
            "maximumFinderTolerance": 0.5
          },
          "disabled": false,
          "locked": true
        },
        {
          "$classify": {
            "detectionHierarchy": "Inner",
            "modelClasses": [
              {
                "filters": [
                  {
                    "intensity": {
                      "imageIn": {
                        "imagePlane": {
                          "cStack": -1,
                          "tStack": -1,
                          "zStack": -1
                        },
                        "memoryId": "None",
                        "zProjection": "$"
                      },
                      "maxIntensity": -1,
                      "minIntensity": -1
                    },
                    "metrics": {
                      "maxParticleSize": -1,
                      "minCircularity": 0.10000000149011612,
                      "minParticleSize": 3
                    },
                    "outputClass": "$"
                  }
                ],
                "pixelClassId": 1,
                "outputClassNoMatch": "None",
                "probabilityHandicap": 1.0
              }
            ]
          },
          "disabled": false,
          "locked": false
        },
        {
          "$measureIntensity": {
            "inputClasses": [
              "$"
            ],
            "planesIn": [
              {
                "imagePlane": {
                  "cStack": -1,
                  "tStack": -1,
                  "zStack": -1
                },
                "memoryId": "None",
                "zProjection": "$"
              }
            ]
          },
          "disabled": false,
          "locked": true
        },
        {
          "$saveImage": {
            "canvas": "$",
            "classesIn": [
              {
                "inputClass": "$",
                "paintBoundingBox": false,
                "paintObjectId": false,
                "style": "Filled"
              }
            ],
            "compression": 1,
            "namePrefix": "ev",
            "subFolder": "images/${imageName}"
          },
          "disabled": false,
          "locked": true
        }
      ]
    },
    {
      "disabled": true,
      "history": [],
      "locked": false,
      "meta": {
        "color": "#B91717",
        "group": "ev",
        "icon": "",
        "name": "Tetraspeck",
        "notes": "This pipeline steps enables the removal of calibration beads (e.g. tetraspeck) that are fluorescent in all channels. \n1. Enable pipeline\n2. Select Tetraspeck image channel (channel showing only tetraspecks)\n3. Adapt (manual) threshold \n4. Within the *Reclassify* command select the channels where tetraspeck need to be removed.",
        "revision": "",
        "tags": [
          "ev",
          "evs",
          "extracellular vesicle"
        ],
        "uid": ""
      },
      "pipelineSetup": {
        "cStackIndex": -2,
        "defaultClassId": "5",
        "source": "FromFile",
        "tStackIndex": -1,
        "zProjection": "MaxIntensity",
        "zStackIndex": -1
      },
      "pipelineSteps": [
        {
          "$rollingBall": {
            "ballSize": 4,
            "ballType": "Paraboloid"
          },
          "disabled": false,
          "locked": true
        },
        {
          "$blur": {
            "kernelSize": 3,
            "mode": "Blur",
            "repeat": 2
          },
          "disabled": false,
          "locked": true
        },
        {
          "$threshold": {
            "modelClasses": [
              {
                "cValue": 0,
                "method": "Manual",
                "pixelClassId": 1,
                "thresholdMax": 65535,
                "thresholdMin": 200
              }
            ]
          },
          "disabled": false,
          "locked": false
        },
        {
          "$watershed": {
            "maximumFinderTolerance": 0.5
          },
          "disabled": false,
          "locked": true
        },
        {
          "$classify": {
            "detectionHierarchy": "Outer",
            "modelClasses": [
              {
                "filters": [
                  {
                    "intensity": {
                      "imageIn": {
                        "imagePlane": {
                          "cStack": -1,
                          "tStack": -1,
                          "zStack": -1
                        },
                        "memoryId": "None",
                        "zProjection": "$"
                      },
                      "maxIntensity": -1,
                      "minIntensity": -1
                    },
                    "metrics": {
                      "maxParticleSize": -1,
                      "minCircularity": 0.0,
                      "minParticleSize": 5
                    },
                    "outputClass": "$"
                  }
                ],
                "pixelClassId": 1,
                "outputClassNoMatch": "None",
                "probabilityHandicap": 1.0
              }
            ]
          },
          "disabled": false,
          "locked": false
        },
        {
          "$reclassify": {
            "hierarchyMode": "CreateTree",
            "inputClasses": [],
            "intensity": {
              "imageIn": {
                "imagePlane": {
                  "cStack": -1,
                  "tStack": -1,
                  "zStack": -1
                },
                "memoryId": "None",
                "zProjection": "$"
              },
              "maxIntensity": -1,
              "minIntensity": -1
            },
            "intersection": {
              "filterLogic": 0,
              "inputClassesIntersectWith": [
                "5"
              ],
              "minIntersection": 0.10000000149011612
            },
            "metrics": {
              "maxParticleSize": -1,
              "minCircularity": -1.0,
              "minParticleSize": -1
            },
            "mode": "ReclassifyMove",
            "newClassId": "None"
          },
          "disabled": false,
          "locked": false
        }
      ]
    }
  ],
  "projectSettings": {
    "address": {
      "city": "",
      "country": "",
      "email": "",
      "firstName": "",
      "lastName": "",
      "organization": "",
      "postalCode": "",
      "streetAddress": ""
    },
    "classification": {
      "classes": [
        {
          "classId": "0",
          "color": "#33CFFF",
          "defaultMeasurements": [
            {
              "measureChannel": "Count",
              "stats": [
                "Off"
              ]
            },
            {
              "measureChannel": "AreaSize",
              "stats": [
                "Avg"
              ]
            },
            {
              "measureChannel": "Circularity",
              "stats": [
                "Avg"
              ]
            },
            {
              "measureChannel": "IntensitySum",
              "stats": [
                "Avg"
              ]
            },
            {
              "measureChannel": "IntensityAvg",
              "stats": [
                "Avg"
              ]
            }
          ],
          "name": "ch1@spot",
          "notes": ""
        },
        {
          "classId": "5",
          "color": "#66FF33",
          "defaultMeasurements": [
            {
              "measureChannel": "Count",
              "stats": [
                "Off"
              ]
            }
          ],
          "name": "tetraspeck@spot",
          "notes": ""
        }
      ],
      "configSchema": "https://imagec.org/schemas/v1/classification-settings.json",
      "meta": {
        "color": "#B91717",
        "icon": "",
        "name": "User defined",
        "notes": "",
        "revision": "",
        "tags": [],
        "uid": ""
      }
    },
    "experimentSettings": {
      "experimentId": "",
      "experimentName": "Experiment",
      "notes": "1. Define working directory (all images in the respective directory will be analyzed with the same pipeline)\n2. If you have a plate-format design\n    -Group your images per well \n    -Define well order (how images are taken on the \t\t      microscope)"
    },
    "plates": [
      {
        "filenameRegex": "_((.)([0-9]+))_([0-9]+)",
        "groupBy": "Off",
        "imageFolder": "",
        "name": "",
        "notes": "",
        "plateId": 0,
        "plateSetup": {
          "cols": 0,
          "rows": 0,
          "wellImageOrder": [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ],
            [
              13,
              14,
              15,
              16
            ]
          ]
        }
      }
    ],
    "workingDirectory": ""
  }
}
```
