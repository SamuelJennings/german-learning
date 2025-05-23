import os
import sys
from pathlib import Path

import tomllib

# add the current directory to sys.path

sys.path.insert(0, os.path.abspath(".")) 

# Project information --------------------------------------
with open("../pyproject.toml", "rb") as f:
    data = tomllib.load(f)

package_meta = data["tool"]["poetry"]
project = "German Learning"

current_file_path = Path(__file__).parent.absolute()

geoluminate_docs_static = current_file_path / "_static"


# https://sphinx-book-theme.readthedocs.io/en/stable/
html_theme = "sphinx_book_theme"
html_static_path = [
    "_static",
]
html_title = "German Learning"

author=""
html_show_copyright = False
html_last_updated_fmt = "%b %d, %Y"
# html_last_updated_fmt = None


# https://sphinx-book-theme.readthedocs.io/en/stable/reference.html
# https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/index.html
html_theme_options = {
    # "home_page_in_toc": True,
    # "show_prev_next": True,
    "collapse_navbar": True,

}
myst_title_to_header = False

comments_config = {
    "utterances": {
        "repo": "/".join(package_meta["homepage"].split("/")[-2:]),
        "issue-term": "pathname",
        "theme": "preferred-color-scheme",
        "label": "documentation",
        "crossorigin": "anonymous",
    }
}

# Any additional Sphinx extension modules go here
extensions = [
    "sphinx.ext.viewcode",
    "sphinx.ext.duration",
    # 'sphinx.ext.doctest',
    "sphinx.ext.todo",
    # "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    # "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_design",
    # "sphinx_comments",
    "myst_parser",
    "sphinx_comments",
    "extensions.roles",
    "extensions.practice",
    # "sphinx_tippy",
]

rst_prolog = """
.. role:: noun

.. role:: verb
"""
# The suffix of source filenames.

# The master toctree document.
master_doc = "index"

# Path to additional templates relative to this directory
templates_path = ["_templates"]

# The suffix of source filenames.
# source_suffix = ".rst"

html_static_path = ["_static"]

def setup(app):
    app.add_css_file("stylesheet.css")

# The language for content autogenerated by Sphinx. Refer to documentation for a list of supported languages.

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    # match any directory not beginning with docs
    "^(?!docs).*",
    "_build",
]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
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

autosectionlabel_prefix_document = True

custom_roles = [
    "noun",
    "verb",
    "adj",
    "adv",
    "pronoun",
    "prep",
    "conj",
    "article",
    "te",
    "ka",
    "mo",
    "lo",
    "subj",
    "dativ",
    "akk",
]


# -- Options for HTML output ---------------------------------------------------

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}





