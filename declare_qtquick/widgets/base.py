from .__external__ import TsComponent as T
from .__external__ import ctx_mgr

_PROPS = 'properties'


class Component:
    qid: T.Qid
    name: T.Name
    properties: T.Properties
    
    def __init__(self):
        self.properties = {}
        # do not initialize name here, you'd better do it in the class level.
        # see how do subclasses do it.
    
    def build(self, level=0) -> str:
        from declare_qtquick.builder import build_component
        return build_component(self, level)
    
    def __enter__(self):
        self.qid = ctx_mgr.upgrade(self)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx_mgr.downgrade()
    
    def __getattr__(self, key: str):
        if key == _PROPS:
            return getattr(super(), _PROPS, ())
        elif key.startswith('_'):
            return getattr(super(), key)
        
        if key in self.properties:
            return self.__getprop__(key)
        else:
            return self.__getattribute__(key)
    
    def __setattr__(self, key, value):
        if key == _PROPS or key.startswith('_'):
            super().__setattr__(key, value)
            return
        
        if key in self.properties:
            self.__setprop__(key, value)
        else:
            super().__setattr__(key, value)
    
    def __getprop__(self, key):
        return self.properties[key]
    
    def __setprop__(self, key, value):
        self.properties[key].kiss(value)
