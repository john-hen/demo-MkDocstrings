# Introduction

This is a demo show-casing how to document a Python library with
[MkDocs], including the library's public API via the [MkDocstrings]
plug-in. It uses [Markdown] throughout the project, in the hand-written
documents as well as in doc-strings embedded with the library code.

We want to see how MkDocs + MkDocstrings stacks up against Sphinx +
Autodoc: [demo-Sphinx-autodoc].

One difference we already encounter here, though it's not obvious
from the rendered HTML page: The table of contents, and thus the side
bar, is not defined in this very document, but in the `mkdocs.yml`
configuration file. There is also no way to easily inspect the source
of the pages, as there is with Sphinx.

[![GitHub repo][GitHub badge]][GitHub repo]

[MkDocs]:              https://www.mkdocs.org
[MkDocstrings]:        https://mkdocstrings.github.io
[Markdown]:            https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown
[demo-Sphinx-autodoc]: https://demo-Sphinx-autodoc.readthedocs.io
[GitHub badge]:        https://img.shields.io/badge/GitHub-100000?logo=github
[GitHub repo]:         https://github.com/john-hen/demo-MkDocstrings
