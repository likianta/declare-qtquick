from PySide6.QtCore import QObject
from PySide6.QtQuick import QQuickItem

from .__ext__ import app, T, id_mgr


def list_all_registered_objects():
    for qid, comp in id_mgr.get_all_components():
        qobj = app.root.findChild(QQuickItem, qid)
        yield qobj, comp


def ensoul(property_object: T.Property):
    for qobj, comp in list_all_registered_objects():
        pass


def _find_by_object_name(object_name: str):
    pass


class ModifiedComponent:
    qobj: T.QQuickItem
    
    def __init__(self, qobj: T.QQuickItem):
        self.qobj = qobj
    
    def __getprop__(self, key: str):
        self.qobj.property(key)
    
    def __setprop__(self, key: str, value):
        pass
