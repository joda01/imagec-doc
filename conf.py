# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ImageC'
copyright = '2023-2024, Joachim Danmayr'
author = 'ImageC authors'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_design',
    #'sphinx.ext.autosectionlabel',
    'sphinx_search.extension'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'old', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_theme_options = {
    'style_nav_header_background': '#343131'
}

html_css_files = [
    'css/custom.css',
]

master_doc = 'index'

rst_prolog = """
.. |br| raw:: html

  <br/>

.. |vertical_ellipsis| unicode:: 0x22EE

.. |copyright| unicode:: 0xA9

"""

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


highlight_language = 'groovy'

html_logo = 'docs/images/imagec_128.png'

html_favicon = 'docs/images/imagec.ico'

release = '2.0.0-alpha'
version = '2.0.0-alpha'

# myst_heading_anchors = 2

myst_substitutions = {

    "info": '<img src="../images/icons/icons8-info-50-circle.png" />',
    "icon_info": '<img src="../images/icons/icons8-info-50-circle.png" class="inline-icon" />',
    "tool_info": '<img src="../images/icons/icons8-info-50-circle.png" class="tool-icon" />',

    "play": '<img src="../images/icons/icons8-play-96.png" />',
    "icon_play": '<img src="../images/icons/icons8-play-96.png" class="inline-icon" />',
    "tool_play": '<img src="../images/icons/icons8-play-96.png" class="tool-icon" />',


    "bioformats": '<img src="../images/icons/omero-features-icons_bio-formats.svg" />',
    "icon_bioformats": '<img src="../images/icons/omero-features-icons_bio-formats.svg" class="inline-icon" />',
    "tool_bioformats": '<img src="../images/icons/omero-features-icons_bio-formats.svg" class="tool-icon" />',

    "ome": '<img src="../images/icons/ome.png" />',
    "icon_ome": '<img src="../images/icons/ome.png" class="inline-icon" />',
    "tool_ome": '<img src="../images/icons/ome.png" class="tool-icon" />',


    "externallink": '<img src="../images/icons/icons8-external-link-50.png" />',
    "icon_externallink": '<img src="../images/icons/icons8-external-link-50.png" class="inline-icon" />',
    "tool_externallink": '<img src="../images/icons/icons8-external-link-50.png" class="tool-icon" />',

    "addcolumn": '<img src="../images/icons/icons8-add-column-96.png" />',
    "icon_addcolumn": '<img src="../images/icons/icons8-add-column-96.png" class="inline-icon" />',
    "tool_addcolumn": '<img src="../images/icons/icons8-add-column-96.png" class="tool-icon" />',

    "heatmap": '<img src="../images/icons/icons8-heat-map-96.png" />',
    "icon_heatmap": '<img src="../images/icons/icons8-heat-map-96.png" class="inline-icon" />',
    "tool_heatmap": '<img src="../images/icons/icons8-heat-map-96.png" class="tool-icon" />',

    "unavailable": '<img src="../images/icons/icons8-unavailable-96.png" />',
    "icon_unavailable": '<img src="../images/icons/icons8-unavailable-96.png" class="inline-icon" />',
    "tool_unavailable": '<img src="../images/icons/icons8-unavailable-96.png" class="tool-icon" />',

    "download": '<img src="../images/icons/icons8-download-96.png" />',
    "icon_download": '<img src="../images/icons/icons8-download-96.png" class="inline-icon" />',
    "tool_download": '<img src="../images/icons/icons8-download-96.png" class="tool-icon" />',

    "bookmark": '<img src="../images/icons/icons8-bookmark-96.png" />',
    "icon_bookmark": '<img src="../images/icons/icons8-bookmark-96.png" class="inline-icon" />',
    "tool_bookmark": '<img src="../images/icons/icons8-bookmark-96.png" class="tool-icon" />',

    "external_link": '<img src="../images/icons/icons8-external-link-96.png />',
    "icon_external_link": '<img src="../images/icons/icons8-external-link-96.png" class="inline-icon" />',
    "tool_external_link": '<img src="../images/icons/icons8-external-link-96.png" class="tool-icon" />',


    "add": '<img src="../images/icons/icons8-add-96.png />',
    "icon_add": '<img src="../images/icons/icons8-add-96.png" class="inline-icon" />',
    "tool_add": '<img src="../images/icons/icons8-add-96.png" class="tool-icon" />',

    "menu": '<img src="../images/icons/icons8-menu-96.png />',
    "icon_menu": '<img src="../images/icons/icons8-menu-96.png" class="inline-icon" />',
    "tool_menu": '<img src="../images/icons/icons8-menu-96.png" class="tool-icon" />',

    "refresh": '<img src="../images/icons/icons8-refresh-96.png />',
    "icon_refresh": '<img src="../images/icons/icons8-refresh-96.png" class="inline-icon" />',
    "tool_refresh": '<img src="../images/icons/icons8-refresh-96.png" class="tool-icon" />',

    "open": '<img src="../images/icons/icons8-open-96.png />',
    "icon_open": '<img src="../images/icons/icons8-open-96.png" class="inline-icon" />',
    "tool_open": '<img src="../images/icons/icons8-open-96.png" class="tool-icon" />',

    "eva": '<img src="../images/icon_eva.png />',
    "icon_eva": '<img src="../images/icon_eva.png" class="inline-icon" />',
    "tool_eva": '<img src="../images/icon_eva.png" class="tool-icon" />',

    "openedfolder": '<img src="../images/icons/icons8-opened-folder-96.png />',
    "icon_openedfolder": '<img src="../images/icons/icons8-opened-folder-96.png" class="inline-icon" />',
    "tool_openedfolder": '<img src="../images/icons/icons8-opened-folder-96.png" class="tool-icon" />',

    "save": '<img src="../images/icons/icons8-save-96.png />',
    "icon_save": '<img src="../images/icons/icons8-save-96.png" class="inline-icon" />',
    "tool_save": '<img src="../images/icons/icons8-save-96.png" class="tool-icon" />',

    "max_classes": "65535",
}
