from __future__ import annotations

import pytest


@pytest.mark.sphinx(testroot="simple", buildername="text")
def test_domain_py_objects(app, status, warning):
    app.builder.build_all()
    result = (app.outdir / "index.txt").read_text()

    lines = [line.rstrip("\n") for line in result.splitlines() if line.strip()]

    assert lines == [
        "misc (alphabetical)",
        "await *self*",
        "*self*(*args, **kwargs)",
        "dir(self)",
        "format(self, fmt)",
        "hash(self)",
        "repr(self)",
        "sys.getsizeof(self)",
        "type coercion",
        "str(self)",
        "bytes(self)",
        "bool(self)",
        "int(self)",
        "float(self)",
        "complex(self)",
        "operator.index(self)",
        "attribute access",
        "getattr(self, attr)",
        "setattr(self, attr, value)",
        "delattr(self, attr)",
        "sequence methods",
        "*value* in *self*",
        "*self*[*item*]",
        "*self*[*item*] = *value*",
        "del *self*[*item*]",
        "iter(self)",
        "len(self)",
        "operator.length_hint(self)",
        "reversed(self)",
        "unary operators (alphabetical)",
        "~*self*",
        "-*self*",
        "+*self*",
        "binary operators (alphabetical)",
        "*self* + *other*",
        "*self* & *other*",
        "divmod(self, other)",
        "*self* == *other*",
        "*self* // *other*",
        "*self* >= *other*",
        "*self* > *other*",
        "*self* <= *other*",
        "*self* << *other*",
        "*self* < *other*",
        "*self* @ *other*",
        "*self* % *other*",
        "*self* * *other*",
        "*self* != *other*",
        "*self* | *other*",
        "*self* ** *other*",
        "*self* >> *other*",
        "*self* - *other*",
        "*self* / *other*",
        "*self* ^ *other*",
        "other math",
        "abs(self)",
        "math.ceil(self)",
        "math.floor(self)",
        "round(self, n)",
        "math.trunc(self)",
    ]
