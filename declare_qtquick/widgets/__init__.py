from .base import Component

try:
    from os.path import abspath
    from sys import path as syspath
    
    syspath.append(abspath(f'{__file__}/../namespace'))
finally:
    from .api import *
