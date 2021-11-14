"""
Python Side Handlers.
See also Qt Modeling Side Handlers at `../qmlside`.

Note this package is mostly copied from my another project `lk-qtquick-scaffold`.
"""
from .application import Application
from .application import app
from .pyside import pyside
from .pyside import reg

app.register_pyobj(pyside, 'pyside')
