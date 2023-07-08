# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FalconDocumentation'
copyright = '2023, 5190 Programming Team'
author = '5190 Programming Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'

html_theme_options = {
    # color scheme: https://coolors.co/776871-e8fccf
    "light_css_variables": {
        "color-brand-content": "#776871",
    },
    "dark_css_variables": {
        "color-brand-content": "#E8FCCF",
    },

    "announcement": "This project is still in development. There might be some missing content.",
}


html_title = 'Falcon Documentation'

html_static_path = ['_static']
