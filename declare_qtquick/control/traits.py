import re

from .__ext__ import TsTraits as T  # noqa
from .__ext__ import proxy

ENUMS = '_enumerations'
PROPS = '_properties'
SIGNALS = '_signals'


class _BaseClass:
    pass


def base_setattr(self, name, value):
    _BaseClass.__setattr__(self, name, value)


def base_getattr(self, name):
    return _BaseClass.__getattribute__(self, name)


# ------------------------------------------------------------------------------

class ConstantEnumeration:
    _enumerations: T.Enumerations
    
    def __init__(self):
        self._enumerations = {}
    
    def __getattr__(self, key: str):
        if key == ENUMS:
            try:
                return base_getattr(self, ENUMS)
            except AttributeError:
                return ()
        elif key.startswith('_'):
            return base_getattr(self, key)
        
        if key in self._enumerations:
            return self.__getenum__(key)
        else:
            return self.__getattribute__(key)
    
    def __setattr__(self, key: str, value):
        if key == ENUMS:
            if self._enumerations:
                raise AttributeError('ConstantEnumeration is immutable!')
            else:
                base_setattr(self, ENUMS, value)
                return
        elif key.startswith('_'):
            base_setattr(self, key, value)
            return
        
        if key in self._enumerations:
            self.__setenum__(key, value)
        else:
            base_setattr(self, key, value)
    
    def __getenum__(self, key: str):
        return self._enumerations[key]
    
    def __setenum__(self, *_):
        raise AttributeError('ConstantEnumeration is immutable!')


class PropGetterAndSetter:
    _properties: T.Properties
    
    def __init__(self):
        # the subclass should update `properties` in its `__init__` method.
        self._properties = {}
    
    def __getattr__(self, key: str):
        if key == PROPS:
            try:
                return base_getattr(self, PROPS)
            except AttributeError:
                return ()
        elif key.startswith('_'):
            return base_getattr(self, key)
        
        if key in self._properties:
            return self.__getprop__(key)
        else:
            return self.__getattribute__(key)
    
    def __setattr__(self, key: str, value):
        if key == PROPS or key.startswith('_'):
            base_setattr(self, key, value)
            return
        
        if key in self._properties:
            self.__setprop__(key, value)
        else:
            base_setattr(self, key, value)
    
    def __getprop__(self, key):
        return proxy.getprop(
            self, key, self._properties[key]
        )
    
    def __setprop__(self, key, value):
        return proxy.setprop(
            self, key, value,
            lambda key, value: self._properties[key].set(value)
        )


class SignalHandler:
    _signals: T.Signals
    _signal_pattern = re.compile(r'^on_\w+ed$')
    
    def __init__(self):
        self._signals = {}
    
    def _is_signal(self, item: str):
        return bool(self._signal_pattern.match(item))
    
    def _signal_factory(self, key):
        raise NotImplementedError
    
    def __getattr__(self, key: str):
        if key == SIGNALS:
            try:
                return base_getattr(self, SIGNALS)
            except AttributeError:
                return ()
        elif key.startswith('_'):
            return base_getattr(self, key)
        
        if key in self._signals:
            return self.__getsignal__(key)
        elif self._is_signal(key):
            signal = self._signals[key] = self._signal_factory(key)
            return signal
        else:
            return self.__getattribute__(key)
    
    def __setattr__(self, key: str, value):
        if key == SIGNALS or key.startswith('_'):
            base_setattr(self, key, value)
            return
        
        if key in self._signals:
            self.__setsignal__(key, value)
        else:
            base_setattr(self, key, value)
    
    def __getsignal__(self, key: str):
        return self._signals[key]
    
    def __setsignal__(self, key, value):
        raise AttributeError('Signal is immutable!')
