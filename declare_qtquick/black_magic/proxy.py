from typing import Optional

from PySide6.QtQuick import QQuickItem

from .__ext__ import T

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


def getprop(comp, key, default_get):
    from ..properties import PropertyGroup
    if not _root:
        return default_get(key)
    if isinstance((x := default_get(key)), PropertyGroup):
        return x
    qobj = _root.findChild(QQuickItem, comp.qid)
    try:
        return qobj.property(key)
    except AttributeError:
        return PropDelegate(qobj, key)


def setprop(comp, key, value, default_set):
    from ..properties import PropertyGroup
    from ..qmlside import qmlside
    
    if not _root:
        default_set(key, value)
        return
    
    if isinstance(value, PropertyGroup):
        raise Exception('This is not writable', comp, key, value)
    
    qobj = _root.findChild(comp.qid)
    if isinstance(value, PropDelegate):
        qmlside.bind_prop(qobj, key, value.qobj, value.prop)
    else:
        try:
            qobj.setProperty(key, value)
        except AttributeError:
            qmlside.bind_prop(qobj, key, value.qobj, value.prop)


class PropDelegate:
    
    def __init__(self, qobj, prop):
        self.qobj = qobj
        self.prop = prop
    
    # def __setattr__(self, key, value):
    #     qmlside.eval_js()
