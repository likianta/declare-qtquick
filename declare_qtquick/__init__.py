from . import widgets
from .application import Application
from .pyside import pyside
from .pyside import reg
from .widgets import *

try:
    def _setup():
        from .application import app
        app.register_pyobj(pyside, 'pyside')
        app.register_pyobj(pyside, 'PySide')
    
    
    _setup()
finally:
    del _setup

__version__ = '0.1.0'
