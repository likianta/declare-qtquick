from .__ext__ import PropSheet
from .__ext__ import Signal
from .__ext__ import T
from .__ext__ import ctx_mgr
from .__ext__ import id_mgr
from .__ext__ import init_prop_sheet
from .__ext__ import traits


class Component(traits.PropGetterAndSetter,
                traits.ConstantEnumeration,
                traits.SignalHandler,
                PropSheet):
    qid: T.Qid  # the qid is initialized in its `__enter__` method.
    
    # name: T.Name
    
    def __init__(self):
        traits.PropGetterAndSetter.__init__(self)
        traits.ConstantEnumeration.__init__(self)
        traits.SignalHandler.__init__(self)
    
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
    
    # -------------------------------------------------------------------------
    
    def __getattr__(self, key: str):
        if key in (traits.PROPS, traits.ENUMS, traits.SIGNALS):
            try:
                return traits.base_getattr(self, key)
            except AttributeError:
                return ()
        elif key.startswith('_'):
            return traits.base_getattr(self, key)
        
        if key in self._properties:
            return self.__getprop__(key)
        elif key in self._enumerations:
            return self.__getenum__(key)
        elif key in self._signals:
            return self.__getsignal__(key)
        elif self._is_signal(key):
            signal = self._signals[key] = self._signal_factory(key)
            return signal
        else:
            return traits.base_getattr(self, key)
    
    def __setattr__(self, key: str, value):
        if key.startswith('_') or \
                key in (traits.PROPS, traits.ENUMS, traits.SIGNALS):
            if key == traits.ENUMS and self._enumerations:
                raise AttributeError('ConstantEnumeration is immutable!')
            elif key == traits.SIGNALS and self._signals:
                raise AttributeError('SignalHandler is immutable!')
            
            traits.base_setattr(self, key, value)
            return
        
        if key in self._properties:
            self.__setprop__(key, value)
        elif key in self._enumerations:
            self.__setenum__(key, value)
        elif key in self._signals:
            self.__setsignal__(key, value)
        else:
            traits.base_setattr(self, key, value)
    
    def _signal_factory(self, key):
        return Signal(self.qid, key)
    
    def build(self, level=0) -> str:
        from __ext__.builder import build_component
        return build_component(self, level)
    
    @property
    def properties(self):
        return self._properties
    
    @property
    def signals(self):
        return self._signals
    
    @property
    def widget_name(self):
        return self.__class__.__name__


class QObject:
    """ This is a wrapper for PySide6.QtCore.QObject.
    
    Detailed:
    
    """
    
