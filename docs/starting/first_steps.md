(first-steps)=
# First steps

The following tutorial will provide an overview of the fundamental concepts and functions of ImageC, offering guidance on the initial steps required for effective utilization of the software.
The tutorial will demonstrate the following:

- ImageC Welcome window
- Creating a new project
- Adding channels
- Starting an analyzes
- Open analyzes results
- Export results to XLSX


## Getting started

:::{note}
If you have problems running ImageC see {doc}`here <../intro/installation>`.
:::

### Running ImageC

Once ImageC has been successfully launched, the user will be directed to the start wizard. 
At this point three options are available: create a new project, open an existing project, open the results of a previous run.


:::{figure} images/screenshot_start_screen.png
:class:  full-image

ImageC start screen
:::

By clicking the {guilabel}`New project` button a project wizard is opened.
You are asked for some basic experiment information:


:::{figure} images/screenshot_start_wizard.png
:class:

ImageC new project wizard
:::



```{eval-rst}
.. csv-table::
  :header: "Title", "Description", ""
  :align: center

  "Scientist name", "Name of the person who is responsible for this analysis", "Optional"
  "Organization", "Organization responsible for the analysis", "Optional"
  "Working directory", "Directory where the images to analyze are stored in", "Mandatory"
  "Images in well order", Describes in which order the images are placed in the well. The number is the image index in well.,"Mandatory"
  "Group by", "Group images either by Filename regex or Directory.","Mandatory"
  "Filename regex", "Regex to extract plate row, plate column and image index from the image filename.","Mandatory"
  "Regex test", "Used to test the regex settings.",""
  "Regex test result", "Result of the regex applied on the text given in the regex test field.",""
  "Notes", "Some free text notes on the experiment.",""


```