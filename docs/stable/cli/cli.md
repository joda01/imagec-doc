---
layout: docu
redirect_from:
- /docs/cli
- /docs/cli/
title: Command Line Interface
---

Besides the ImageC graphical user interface (GUI), which provides intuitive access to its features, the program can also be fully controlled through a command-line interface (CLI).
The usage of the CLI allows to automate processes and allows to integrate ImageC into external workflows or applications.
Another typical use case for the CLI usage is the remote control of ImageC which allows ImageC to run on an external server / super computer and be controlled via network from a users workstation to start analysis and export results.


To operate ImageC via the CLI, open a terminal (such as Bash on Linux or PowerShell on Windows), navigate to the directory containing the ImageC executable, and execute `./imagec --help` (Windows: `imagec.exe --help`).

<a href="{{ site.baseurl }}/images/cli/screenshot_cli_help.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/cli/screenshot_cli_help.png" style="width: 80%" alt="Loading ..."/></a>

A list of all support CLI commands is presented.
Run help on any listed command to get help about it `./imagec run --help`.

## run

The run command is used to start an analysis.
As well as the input folder containing the images to analyse, it expects the path to a valid ImageC project file as input, as well as an optional job name under which the results are stored.

`./imagec run -p settings.icproj -i /path/to/images -j job-01`


## export

Once the analysis has been finished the results can be exported from the ImageC database file to `xlsx` or `R`.

Use `./imagec export -i results.icdb -o /path/to/export -f xlsx --style table <SUB-COMMAND>`.


| Option | Description                        |
|--------|------------------------------------|
|-i      |Path to the ImageC database file `icdb` from which the data should be exported from.|
|-o      |Path to the folder the data should be exported to |
|-f      |Export format. Allowed are `xlsx` or `r` |
|-s      |Style of the output. Can either be `table` or `heatmap`.|
|-c      |Optional: Path to a column settings file which specifies which columns should be exported, if not given the default settings from the project file are taken.


Once the options are specified the wanted output context has to be specified. 
ImageC allows to either export the data for a whole `plate` a `well / group` or an individual `image`.

If `well` or `plate` is used for export it is mandatory to specify the name of the plate / image which should be exported.
To get a list of available plates / images use the `database` command.

## database

The `database` command can be used to have a deeper look into the data stored in the results database.

Use either the subcommand `wells` to list all analyzed wells or `images` to list all analyzed images of this job.

`/imagec database -i /path/to/results.icdb view <wells|images>`



## Automatic parameter variation

Sometimes an analysis requires testing many different image-processing parameters on a set of images to determine the best-fitting pipeline.
Using an ImageC project file (.icproj), which is a JSON formatted file, together with the CLI option allows you to automatically vary parameters and execute the pipeline with different parameter sets.


One best practice may be to use Python as scripting language, parse the project file, modify the wanted parameters and run the pipeline using the CLI option.

The following example shows a Python script which executes a pipeline with four different kernel sizes for the blur command (5, 7, 9, 11).

*run.py*
```py
import json
import subprocess

#
# Modify kernel size in $blur step
#
def modifyBlurKernelSize(filename, kernelSize):
    # Load JSON
    with open(filename, "r") as f:
        data = json.load(f)

    modified = False

    # Iterate through pipelines and their steps
    for pipeline in data.get("pipelines", []):
        for step in pipeline.get("pipelineSteps", []):
            if "$blur" in step:
                step["$blur"]["kernelSize"] = kernelSize
                modified = True
                print("Updated kernelSize in $blur step.")

    if not modified:
        print("Warning: No $blur step found in the pipeline!")

    # Save updated JSON
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print("File updated successfully!")

#
# Run ImageC analysis
#
def runAnalysis(projectFileName, imagePath, jobName):
    result = subprocess.run(
        ["./imagec", "run", "-p", projectFileName, "-i", imagePath, "-j", jobName],
        capture_output=True,
        text=True
    )
    
    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)


for kernelSize in range(5, 13, 2):   # 5, 7, 9, 11
    modifyBlurKernelSize("project.icproj", kernelSize)
    runAnalysis("project.icproj", "/path/to/images", "try-" + str(kernelSize))

```
The used example project file:

*project.icproj*
```json
{
  "configSchema": "https://imagec.org/schemas/v1/analyze-settings.json",
  "imageSetup": {
    "imagePixelSizeSettings": {
      "mode": "Automatic",
      "pixelHeight": 0.0,
      "pixelSizeUnit": "um",
      "pixelWidth": 0.0
    },
    "imageTileSettings": {
      "tileHeight": 4096,
      "tileWidth": 4096
    },
    "series": 0,
    "tStackHandling": "EachOne",
    "tStackSettings": {
      "endFrame": -1,
      "startFrame": 0
    },
    "zStackHandling": "ExactOne",
    "zStackSettings": {
      "defaultZProjection": "MaxIntensity"
    }
  },
  "imagecMeta": {
    "buildTime": "2025-12-02 05:01:09",
    "imagecVersion": "devel-build"
  },
  "meta": {
    "color": "#B91717",
    "icon": "",
    "modifiedAt": "2025-12-03T05-01-44",
    "name": "",
    "notes": "",
    "revision": "",
    "tags": [],
    "uid": ""
  },
  "pipelineSetup": {
    "realSizesUnit": "Px"
  },
  "pipelines": [
    {
      "disabled": false,
      "locked": false,
      "meta": {
        "color": "#B91717",
        "icon": "",
        "name": "Manual pipeline",
        "notes": "",
        "revision": "",
        "tags": [],
        "uid": "6a144412-f9bc-4803-9553-761959f33092"
      },
      "pipelineSetup": {
        "cStackIndex": 0,
        "defaultClassId": "7",
        "source": "FromFile",
        "tStackIndex": -1,
        "zProjection": "None",
        "zStackIndex": -1
      },
      "pipelineSteps": [
        {
          "$blur": {
            "kernelSize": 3,
            "mode": "Blur",
            "repeat": 1
          },
          "disabled": false,
          "locked": false
        },
        {
          "$measureIntensity": {
            "inputClasses": [
              "7"
            ],
            "planesIn": [
              {
                "imagePlane": {
                  "cStack": 0,
                  "tStack": -1,
                  "zStack": -1
                },
                "memoryId": "None",
                "zProjection": "MaxIntensity"
              },
              {
                "imagePlane": {
                  "cStack": 1,
                  "tStack": -1,
                  "zStack": -1
                },
                "memoryId": "None",
                "zProjection": "MaxIntensity"
              }
            ]
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
          "classId": "7",
          "color": "#FF33FF",
          "defaultMeasurements": [
            {
              "measureChannel": "Count",
              "stats": [
                "Off"
              ]
            },
            {
              "measureChannel": "IntensityAvg",
              "stats": [
                "Avg"
              ]
            },
            {
              "measureChannel": "IntensityMin",
              "stats": [
                "Avg"
              ]
            },
            {
              "measureChannel": "IntensityMax",
              "stats": [
                "Avg"
              ]
            }
          ],
          "name": "cy7@spot",
          "notes": ""
        }
      ],
      "configSchema": "https://imagec.org/schemas/v1/classification-settings.json",
      "meta": {
        "color": "#B91717",
        "icon": "",
        "name": "",
        "notes": "",
        "revision": "",
        "tags": [],
        "uid": ""
      }
    },
    "experimentSettings": {
      "experimentId": "6fc87cc8-686e-4806-a78a-3f623c849cb7",
      "experimentName": "Experiment",
      "notes": ""
    },
    "plate": {
      "filenameRegex": "((.)([0-9]+))_([0-9]+)",
      "groupBy": "Filename",
      "imageFolder": "/path/to/my/images",
      "name": "",
      "notes": "",
      "plateId": 1,
      "plateSetup": {
        "cols": 24,
        "rows": 16,
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
  }
}
```

