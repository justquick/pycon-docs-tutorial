# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
from getpass import getuser
sys.path.insert(0, os.path.abspath('..'))

project = 'Pycon Tutorial'
copyright = '2023, Justin Quick'
author = 'Justin Quick'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    'sphinx.ext.viewcode',
    # 'sphinxcontrib.confluencebuilder',
]
autoclass_content = 'both'


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

def confenv(name, default=None, isbool=False):
    '''
    Returns the env vars value by name.upper idenetified by CONFLUENCE_ prepended
    Used to map vars to config values for the confluencebuilder plugin
    '''
    name = f'CONFLUENCE_{name.upper()}'
    return name in os.environ if isbool else os.getenv(name, default)


# This is a configuration option for the confluencebuilder plugin.
confluence_publish = confenv('publish', False, True)  # publish or not
confluence_space_key = confenv('space_key', 'GITPOD')  # existing space key
confluence_server_url = confenv('server_url', 'https://innerspace.stsci.edu/')  # innerspace by default


# Either auth by user or token
token = confenv('publish_token')
if token:
    confluence_publish_token = token  # ci job
else:
    confluence_ask_password = confenv('ask_password', True, True)  # manual run
    confluence_server_user = confenv('server_user', getuser())

# Misc opts
confluence_parent_page = confenv('parent_page')  # Documentation parent page
confluence_page_hierarchy = confenv('page_hierarchy', True, True)
confluence_publish_dryrun = confenv('publish_dryrun', False, True)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
