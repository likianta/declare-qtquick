# Widgets Documentation

## Package Structure

```
declare_qtquick
|== widgets
    |== api
        |== qtquick
            |-- __init__.py : from .__list__ import *
            |-- __list__.py ::
            |       from .__base__ import *
            |
            |       class Item(Component):
            |           ...
            |       class MouseArea(Item):
            |           ...
            |       class Text(Item):
            |           ...
            |       ...
            |-- __base__.py
            |== controls
                |-- __init__.py
                |-- __list__.py
                |-- __base__.py
            |== window
                |-- __init__.py
                |-- __list__.py
                |-- __base__.py
            |== ...
    |-- __init__.py : from .api import qtquick
    |-- base.py
```
