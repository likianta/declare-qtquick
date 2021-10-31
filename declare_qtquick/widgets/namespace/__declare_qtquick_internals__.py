"""
See `declare_qtquick.widgets.__init__`.
"""
# noinspection PyUnresolvedReferences
from typing import Union

Component = None
P = None
T = None
W = None
qml_imports = set()

if __name__ == '__main__':
    from declare_qtquick.widgets.base import Component as _Component
    from declare_qtquick.widgets import widget_sheet as _wsheet
    from declare_qtquick import properties as _properties
    from declare_qtquick.typehint import prop_hint as _prop_hint
    
    Component = _Component
    P = _properties
    T = _prop_hint
    #   note: `T` has no usage. we will remove it and its source code in the
    #   future:
    #   - declare_qtquick/widgets/__init__.py
    #   - declare_qtquick/widgets/namespace/__declare_qtquick_internals__.py
    #   - declare_qtquick/typehint/prop_hint.py
    W = _wsheet


def setup(**kwargs):
    global Component, P, T, W
    Component = kwargs['component']
    P = kwargs['properties']
    T = kwargs['prop_hint']
    W = kwargs['widgets_sheet']

    # from lk_logger import lk
    # lk.logp(Component, P, T, W, title='internal things have been set up')

# A.
#   def add_qml_imports(name: str):
#       qml_imports.add(name)
# B.
#   add_qml_imports = qml_imports.add
