# Summary

This is the front page for the API documentation. It uses the special
directive `::: identifier` provided by MkDocstrings.

There is no equivalent for Sphinx's Autosummary, so we have to
create the summary ourselves.

<table markdown="1"><tr><td>
    [`action`](action.md)
</td><td>
    Manual synopsis of function `action`.
</td></tr><tr><td>
    [`actions`](actions.md)
</td><td>
    Manual synopsis of module `actions`.
</td></tr><tr><td>
    [`classes`](classes.md)
</td><td>
    Manual synopsis of module `classes`.
</td></tr></table>

This does not add them to the navigation in the side bar. We have to do
that manually, by editing `mkdocs.yml`, unless we make use of the
[MkDocs-gen-files] plug-in and create these pages on the fly.

[MkDocs-gen-files]: https://oprypin.github.io/mkdocs-gen-files
