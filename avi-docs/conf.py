import os
import sys
from datetime import datetime

# Add the ETL source path to sys.path for autodoc imports.
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../avi-etl-pipeline'))

project = 'All India Villages API Documentation'
author = 'All India Villages API Engineering'
release = '1.0.0'
version = release

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_tabs.tabs',
    'sphinxcontrib.mermaid',
    'sphinx_togglebutton',
    'sphinxext.opengraph',
    'autodocsumm',
    'sphinx_rtd_theme',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = 'All India Villages API Docs'
html_logo = None
html_theme_options = {
    # 'sidebar_hide_name': True,
    'navigation_with_keys': True,
}

autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autodoc_typehints_format = 'short'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'inherited-members': True,
}
autosummary_generate = True

autodoc_mock_imports = [
    'flask',
    'pandas',
    'sqlalchemy',
    'dotenv',
    'werkzeug',
    'openpyxl',
    'psycopg2',
    'psycopg2_binary',
]

js_language = 'typescript'
js_source_path = '../All_India_Villages_API/src'

# Additional metadata for ReadTheDocs and social previews.
ogp_site_url = 'https://readthedocs.org/projects/all-india-villages-api/'
ogp_image = 'https://raw.githubusercontent.com/USERNAME/REPO/main/docs/_static/opengraph.png'
ogp_description_length = 200

def setup(app):
    app.add_css_file('custom.css')
