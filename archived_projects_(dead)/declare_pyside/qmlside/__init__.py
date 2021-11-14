"""
Qt Modeling Side Handlers.
See also Python Side Handlers at `../pyside`.
"""
from .hot_loader import hot_loader
from .qmlside import qmlside

if True:
    from .qlogger import setup as _setup_qlogger
    from .qmlside import setup as _setup_qmlside
    
    _setup_qlogger()
    _setup_qmlside()
