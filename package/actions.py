"""
This is the first line in the doc-string of module `actions`.

We can reference other objects, such as [`Class1`][package.Class1] and
[Class2][package.Class2]. We can link back to one of the main documents
as a whole, for example [Overview][overview], or [a specific
section][first-steps]. We can create [cross-references to other
projects][intersphinx], like to [`pathlib.Path`][].

And we can have highlighted code examples:
```python
from package import action
from package import Class1

action(do='whatever')
class1 = Class1()
class1.action()
```

MkDocstrings created this page from a "stub" file named `actions.md`
in the `api` folder underneath `docs`. It contains very little:
```markdown
# actions

::: package.actions
```

MkDocstrings takes care of the rest and fills in the blanks, pulling
in signatures and doc-strings from the package's source code. And
it shows a box with the source code for each object. We cannot, however,
look at the source code of the entire module, as with Autodoc. (Though
the [MkDocstrings-sourcelink] plug-in appears to be able to generate
direct links back to the corresponding source code line in the original
repository.)

[MkDocstrings-sourcelink]: https://ai2business.github.io/mkdocstrings-sourcelink
"""


def action(do='something'):
    """
    This is the first line in the doc-string of the function `action`.

    It is defined in module [`actions`][package.actions].
    """
    pass
