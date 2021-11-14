from typing import Optional

from PySide6.QtQuick import QQuickItem

from .__ext__ import T
from .__ext__ import convert_name_case

_root = None  # type: Optional[T.QObject]


def build(qobj):
    # note: do not use collector to collect all qobjects, for example this is
    #   not correct:
    #       from ..control import id_mgr
    #       collector = {}
    #       for qid, _ in id_mgr.get_all_components():
    #           collector[qid] = qobj.findChild(QQuickItem, qid)
    #   because c++ internals will destroy all qobjects dynamically, the
    #   collector is hooking invalid qobjects.
    global _root
    _root = qobj


def getprop(comp, key, default_value):
    from ..properties import PropertyGroup
    if not _root:
        return default_value
    if isinstance(default_value, PropertyGroup):
        return default_value
    
    qobj = _root.findChild(QQuickItem, comp.qid)
    
    try:
        return qobj.property(convert_name_case(key))
    except RuntimeError:
        return PropDelegate(qobj, key)


def setprop(comp, key, value, default_set):
    from ..properties import Anchors
    from ..properties import PropertyGroup
    from ..qmlside import qmlside
    
    if not _root:
        default_set(key, value)
        return
    
    if isinstance(value, PropertyGroup):
        raise Exception('This is not writable', comp, key, value)
    
    qobj = _root.findChild(comp.qid)
    key = convert_name_case(key)
    
    if isinstance(comp, PropertyGroup):
        group_name = convert_name_case(comp.name)
        if isinstance(comp, Anchors):
            if key in ('centerIn', 'fill'):
                qmlside.bind_prop(qobj, f'{group_name}.{key}', value.qobj, '')
            else:
                qmlside.bind_prop(
                    qobj, f'{group_name}.{key}', value.qobj, value.prop)
        else:
            qmlside.bind_prop(
                qobj, f'{group_name}.{key}', value.qobj, value.prop)
        
    elif isinstance(value, PropDelegate):
        qmlside.bind_prop(qobj, key, value.qobj, value.prop)
    else:
        try:
            qobj.setProperty(key, value)
        except AttributeError:
            qmlside.bind_prop(qobj, key, value, '')


class PropDelegate:
    
    def __init__(self, qobj, prop):
        self.qobj = qobj
        self.prop = prop
