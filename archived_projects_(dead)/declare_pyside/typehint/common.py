# tip: if importing a package/lib other than `typing` lib, it is suggested to do:
#   1. do not use import all statement (i.e. `import *`)
#   2. use 'import something as _something' statement to avoid leaking its name
#      to `.__init__.<public_namespace>`
from os import PathLike as _PathLike
from typing import *

from lk_lambdex import lambdex as _lambdex

# see typical usages in `.delegators`
TFakeModule = _lambdex('', """
    class FakeModule:
        def __getattr__(self, item):
            return None
        def __call__(self, *args, **kwargs):
            return None
    return FakeModule()
""")()

TPath = Union[_PathLike, str, bytes]
