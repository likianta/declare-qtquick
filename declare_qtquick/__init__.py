from . import widgets
from .application import Application
from .application import app
from .pyside import pyside
from .pyside import reg
from .widgets import *

app.register_pyobj(pyside, 'pyside')
app.register_pyobj(pyside, 'PySide')

__version__ = '0.1.0'
