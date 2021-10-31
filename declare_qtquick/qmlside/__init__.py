"""
This package is copied from lk-qtquick-scaffold. Currently, the most modules
are redundant to use. I've commented some of them in the __init__ file (see
below).
"""
# from .data_model import ModelGenerator
# from .hot_loader import hot_loader
# from .js_evaluator import eval_js
# from .js_evaluator import js_eval
# from .layout_helper import LayoutHelper
# from .resource_manager import BaseResourceManager
# from .type_adapter import adapt_argtypes

try:
    from .qlogger import setup as _setup
    
    _setup()
finally:
    del _setup
    from .hot_loader import hot_loader
