(templates)=
# Templates

Once you have created a pipeline that works well for a specific application, you may be able to reuse these settings for similar applications or share them with others. 
To meet this need, ImageC offers a wide range of template functions.

There are three types of templates provided in ImageC:

* Pipeline templates (*.ictempl)
* Classification templates (*.ictemplcc)
* Result export templates  (*.ictemplexp)
* Project templates (*.ictemplproj)

On startup ImageC is looking for templates within the directory `~/.imagec/templates` and provides all found templates for selection.

:::{note}
Templates should be stored in the folder `~/.imagec/templates`, this allows ImageC to automatically find and provide templates.
:::

(pipeline-template)=
## Pipeline templates

```{figure} images/template_pipeline.png
:class: full-image
Pipeline template management
```

A pipeline template stores the settings and pipeline steps of one specific pipeline and allows to reuse these settings within a project.
Using the store button {{icon_download}} allows to store the actual pipeline as template.

With the dropdown on the left hand side a available template can be selected which is added as new pipeline to the project.
Using the open {{icon_openedfolder}} button from within the pipeline editor load the template settings direct to the opened editor.


(classification-template)=
## Classification template

```{figure} images/template_classification.png
:class: medium-image
Classification template management
```

Similar to pipeline templates, classification templates can be used to reuse taken classification settings.
Using th dropdown allows to open an existing classification template.


(results-export-template)=
## Results export template

```{figure} images/results_templates_results.png
:class: medium-image
Results template management
```

Beside the definition of the image processing pipelines the presentation of the data is an other important step.
It is necessary to think about which data should be exported after a run.
Results templates can be used to define the columns of data to be exported.
When opening a results database file, these settings are loaded per default and presents the data.

Result templates are stored together with the project settings when defined from the projects tab or can be stored as reusable standalone template from the results analysis panel.


(project-template)=
## Project template

A project template combines all of the templates above to one file.
Once a project template is loaded, pipelines, classification settings and results export setting are loaded.
Project templates can either be loaded using the open {{icon_openedfolder}} button in the toolar, looking for `*.ictemplproj` files or by choosing one of the predefined project pipelines from the from the drop down.

Use the save {{icon_save}} button and select {guilabel}`ImageC project Template` to store a project template.