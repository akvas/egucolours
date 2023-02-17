#
# -- Project information -----------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
import egucolours

project = 'egucolours'
copyright = '2022-2023, Andreas Kvas'
author = 'Andreas Kvas'

version = '0.1'
release = '0.1.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary'
]

autosummary_generate = True
templates_path = ['_templates']


source_suffix = '.rst'

master_doc = 'index'

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_generated/egucolours.Colour.rst', '_generated/egucolours.ColourMapping.rst']

pygments_style = None

html_theme = 'sphinxdoc'

html_static_path = ['_static']

htmlhelp_basename = 'egucolours'
autoclass_content = 'both'