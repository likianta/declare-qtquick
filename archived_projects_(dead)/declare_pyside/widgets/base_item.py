from PySide6.QtQml import QQmlComponent

from declare_foundation.context_manager import Context
from .core.authorized_props import AuthorizedProps
from .core.prop_delegators import PropDelegator
from .core.prop_delegators import adapt_delegator
from ..pyside import app
from ..qmlside import qmlside
from ..typehint.qmlside import *

QPROPS = '_qprops'


class BaseItem(Context, AuthorizedProps):
    component: TComponent
    parent: Optional['BaseItem']
    qmlfile: TQmlFile
    qobj: TQObject
    
    def __init__(self):
        Context.__init__(self)
        AuthorizedProps.__init__(self)
        
        self.component = QQmlComponent(app.engine, self.qmlfile)
    
    def __enter__(self):
        super().__enter__()
        # instantiate a QObject
        self.qobj = self.create_object()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
    
    def __getattr__(self, item: str):
        if item == QPROPS:
            return getattr(super(), QPROPS, ())
        elif item.startswith('_'):
            return getattr(super(), item)
        
        # https://stackoverflow.com/questions/3278077/difference-between-getattr
        # -vs-getattribute
        if item in self._qprops:
            return super().__getattribute__('__getprop__')(item)
        else:
            return super().__getattribute__(item)
    
    def __setattr__(self, key: str, value):
        # # if key == QPROPS:
        if key == QPROPS or key.startswith('_'):
            super().__setattr__(key, value)
            return
        
        if key in self._qprops:
            self.__setprop__(key, value)
        else:
            super().__setattr__(key, value)
    
    def __getprop__(self, name: TPropName):
        prop_type = self._qprops[name]
        prop_delegator = adapt_delegator(self.qobj, name, prop_type)
        return prop_delegator.read()
    
    def __setprop__(self, name, value):
        # A
        # self.qobj.setProperty(name, value)
        
        # B
        # prop = QQmlProperty(self.qobj, name)
        # prop.write(value)
        
        # C
        type_ = self._qprops[name]
        prop_delegator = adapt_delegator(self.qobj, name, type_)
        if isinstance(value, PropDelegator):
            prop_delegator.write(value.read())
        else:
            prop_delegator.write(value)
    
    def create_object(self) -> TQObject:
        """
        
        TODO:
            `self.component` (the instance of QQmlComponent) doesn't provide a
            function that can directly create a QObject within defined parent.
            It means, by `qobj = self.component.create(...)` that the `qobj`
            won't be shown in GUI -- we've tried many things to make it work --
            but for now it still totally invalid.
            So we have to create `qobj` by `qmside.create_qobject`. The key
            method is `QML:Component.createObject` (`QML:Component` inherits
            from `PySide6.QtQml.QQmlComponent`, see [link#1][1] and
            [link#2][2]).
                [1]: https://doc.qt.io/qt-5/qqmlcomponent.html
                [2]: https://doc.qt.io/qt-5/qml-qtqml-component.html
                
            Backup Works:
                ctx = app.engine.contextForObject(self.parent.qobj)
                qobj = self.component.create(ctx)
                qobj.setParent(self.parent.qobj)
                return qobj
        """
        qobj = qmlside.create_qobject(self.component, self.parent.qobj)
        return qobj

    @property
    def is_anchored(self) -> bool:
        """
        References:
            https://stackoverflow.com/questions/51673449/how-can-i-test-if-an
            -item-is-anchored
        
        Usages:
            `.core.prop_delegators.specialized_delegators.AnchorsDelegator
            .__set_subprop__`
        """
        return getattr(self.qobj, '_is_anchored', False)
