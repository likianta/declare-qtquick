from .__ext__ import TsTraits as T

ENUMS = '_enumerations'
PROPS = '_properties'


class _BaseClass:
    pass


def regular_setattr(self, name, value):
    _BaseClass.__setattr__(self, name, value)

    
def regular_getattr(self, name):
    return _BaseClass.__getattribute__(self, name)


# ------------------------------------------------------------------------------

class ConstantEnumeration:
    _enumerations: T.Enumerations
    
    def __init__(self):
        self._enumerations = {}
    
    def __getattr__(self, key: str):
        if key == ENUMS:
            try:
                return regular_getattr(self, ENUMS)
            except AttributeError:
                return ()
        elif key.startswith('_'):
            return regular_getattr(self, key)
        
        if key in self._enumerations:
            return self.__getenum__(key)
        else:
            return self.__getattribute__(key)
    
    def __setattr__(self, key: str, value):
        if key == ENUMS:
            if self._enumerations:
                raise AttributeError('ConstantEnumeration is immutable!')
            else:
                regular_setattr(self, ENUMS, value)
                return
        elif key.startswith('_'):
            regular_setattr(self, key, value)
            return
        
        if key in self._enumerations:
            self.__setenum__(key, value)
        else:
            regular_setattr(self, key, value)
    
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
                return regular_getattr(self, PROPS)
            except AttributeError:
                return ()
        elif key.startswith('_'):
            return regular_getattr(self, key)
        
        if key in self._properties:
            return self.__getprop__(key)
        else:
            return self.__getattribute__(key)
    
    def __setattr__(self, key: str, value):
        if key == PROPS or key.startswith('_'):
            regular_setattr(self, key, value)
            return
        
        if key in self._properties:
            self.__setprop__(key, value)
        else:
            regular_setattr(self, key, value)
    
    def __getprop__(self, key):
        return self._properties[key]
    
    def __setprop__(self, key, value):
        self._properties[key].set(value)
