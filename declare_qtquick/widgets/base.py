from .__ext__ import PropSheet
from .__ext__ import T
from .__ext__ import ctx_mgr
from .__ext__ import id_mgr
from .__ext__ import init_prop_sheet
from .__ext__ import traits


class Component(traits.PropGetterAndSetter,
                traits.ConstantEnumeration, PropSheet):
    qid: T.Qid  # the qid is initialized in its `__enter__` method.
    # name: T.Name
    
    def __init__(self):
        traits.PropGetterAndSetter.__init__(self)
        traits.ConstantEnumeration.__init__(self)
    
    def __enter__(self):
        self.qid = ctx_mgr.upgrade(self)
        self.__ready__()
        return self
    
    def __ready__(self):
        # in ready stage, `self.qid` is available to use.
        init_prop_sheet(self)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx_mgr.downgrade()
        id_mgr.set(self.qid, self)
    
    def __getattr__(self, key: str):
        if key == traits.PROPS or key == traits.ENUMS:
            try:
                return traits.regular_getattr(self, key)
            except AttributeError:
                return ()
        elif key.startswith('_'):
            return traits.regular_getattr(self, key)
        
        if key in self._properties:
            return self.__getprop__(key)
        elif key in self._enumerations:
            return self.__getenum__(key)
        else:
            return traits.regular_getattr(self, key)
    
    def __setattr__(self, key: str, value):
        if key.startswith('_') or key in (traits.PROPS, traits.ENUMS):
            if key == traits.ENUMS:
                if self._enumerations:
                    raise AttributeError('ConstantEnumeration is immutable!')
            
            traits.regular_setattr(self, key, value)
            return
        
        if key in self._properties:
            self.__setprop__(key, value)
        elif key in self._enumerations:
            self.__setenum__(key, value)
        else:
            traits.regular_setattr(self, key, value)
    
    def build(self, level=0) -> str:
        from __ext__.builder import build_component
        return build_component(self, level)
    
    @property
    def properties(self):
        return self._properties
    
    @property
    def widget_name(self):
        return self.__class__.__name__
