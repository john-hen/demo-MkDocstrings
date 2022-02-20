# Overview

Pretend this is the tutorial that gives a general introduction to the
library, providing usage examples and all that.

This is a stand-alone document, in this case a file named `overview.md`
inside the project's `docs` folder. So it is separate from the actual
Python library in the, unimaginatively named, `package` folder. Both
folders are right underneath the project's root in the repo.

With MkDocs alone, ["a section cannot have a page assigned to it"][pages],
which is what we'd like to have for the API summary. But the Material
for MkDocs theme offers [section index pages] as an option. With other
themes, we could use the [MkDocs-section-index] plug-in. As the API
section documents the *public* API, not every doc-string defined in
`package` needs to show up there, only the ones that are important.
However, there is no equivalent for Sphinx's [Autosummary] extension,
so we have to write the summaries manually.

We can link to objects from the API documentation, such as
[`Class1`](api/classes.md#package.classes.Class2) or
[`action`](api/action.md). The syntax is
``[`Class1`](api/classes.md#package.classes.Class2)`` and
``[`action`](api/action.md)``.

[Intersphinx]-like support for [cross-references] to other projects
is provided also by the MkDocstrings plug-in, not MkDocs itself. We get
short-hand link targets to external documentation like to Python's
[`pathlib`][] module with ``[`pathlib`][]``. The syntax here is
different from MyST's, where we would write ``[`pathlib`](python:pathlib)``
instead. MkDocstrings, perhaps more logically so, uses a [collapsed
reference link] with an empty [link label], which is then taken to be
the same as the [link text], stripped of inline mark-up, and looked
up in the (Sphinx-generated) object inventory of other projects
listed in the configuration file.

As we see even from that last example, we can nest mark-up inside link
text, like [a `literal`](https://example.org). Because this is Markdown.


## First steps

This is a section inside the Overview chapter. We did not need to mark
it as a possible link target, MkDocs [creates header anchors
automatically][linking] via Python-Markdown's [Table of Contents]
extension.

Here is a code example:
```python
from package.classes import Class1

class1 = Class1()
class1.action()
```

We used triple back-ticks (` ``` `) to mark the code block.

It's not so clear (to me at least, at this point) how the syntax
highlighting works. MkDocstrings depends on the Material theme for some
reason, so it may not be as easy as it is in Sphinx to switch themes and
highlighting styles.

[pages]:                    https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation
[section index pages]:      https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#section-index-pages
[MkDocs-section-index]:     https://oprypin.github.io/mkdocs-section-index
[cross-references]:         https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories
[collapsed reference link]: https://spec.commonmark.org/0.30/#collapsed-reference-link
[link label]:               https://spec.commonmark.org/0.30/#link-label
[link text]:                https://spec.commonmark.org/0.30/#link-text
[Autosummary]:              https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
[Intersphinx]:              https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
[linking]:                  https://www.mkdocs.org/user-guide/writing-your-docs/#linking-to-pages
[Table of Contents]:        https://python-markdown.github.io/extensions/toc
