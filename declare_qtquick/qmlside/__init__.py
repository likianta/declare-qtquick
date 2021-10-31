"""
This package is partially copied from lk-qtquick-scaffold project.
"""
try:
    from .qlogger import setup as _setup
    
    _setup()
    
finally:
    del _setup
    from .hot_loader import hot_loader
