# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

project = "stockage-service"
copyright = "2024, Jilvo"
author = "Jilvo"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(
    0, os.path.abspath("../../")
)  # Ajustez ce chemin selon la structure de votre projet

extensions = [
    "sphinx.ext.autodoc",
    # Optionnel, pour une meilleure prise en charge des docstrings de style
    # Google et NumPy
    "sphinx.ext.napoleon",
    # Pour inclure les annotations de type dans la documentation]
    "sphinx_autodoc_typehints",
]
templates_path = ["_templates"]
exclude_patterns = []
source_suffix = ".rst"
master_doc = "index"
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
