# Overview

Pretend this is the tutorial that gives a general introduction to the
library, providing usage examples and all that.

This is a stand-alone document, in this case a file named `overview.md`
inside the project's `docs` folder. So it is separate from the actual
Python library in the, unimaginatively named, `package` folder. Both
folders are right underneath the project's root in the repo.

In the side bar navigation on the left, we cannot have the API summary
as a top-level page, as we do in the Sphinx project. With MkDocs,
["a section cannot have a page assigned to it"][pages]. So it is now
the first page inside that section. As it documents the *public* API,
not every doc-string defined in `package` needs to show up there,
only the ones that are important. However, there is no equivalent for
Sphinx's [Autosummary] extension, so we have to create the summary
ourselves.

We can link to objects from the API documentation, such as
[`Class1`](api/classes.md#package.classes.Class2) or
[`action`](api/action.md). The syntax is
``[`Class1`](api/classes.md#package.classes.Class2)`` and
``[`action`](api/action.md)``.

[Intersphinx]-like support for references across projects is provided
also by the MkDocstrings plug-in, not MkDocs itself. We get short-hand
link targets to external documentation, like to Python's [`pathlib`][]
module with just ``[`pathlib`][]``. Note the strange link syntax here.
In MyST, we would use `[]()`-type links, not `[][]`. Even though it makes
more sense to use `[][]` like MkDocstrings does, given that these are
in fact reference links much like those in plain Markdown, it makes no
sense whatsoever to have the link target in the place where we usually
put the link text.

As we see even from that last example, we can nest mark-up inside link
text, like [a `literal`](https://example.org). Because this is Markdown.


## First steps

This is a section inside the Overview chapter. We did not need to mark
it as a possible link target, MkDocs creates header anchors automatically.

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

[pages]:        https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation
[Autosummary]:  https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
[Intersphinx]:  https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
[linking]:      https://www.mkdocs.org/user-guide/writing-your-docs/#linking-to-pages
