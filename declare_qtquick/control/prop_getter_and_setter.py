from .__external__ import TProperties

_PROPS = 'properties'


class PropGetterAndSetter:
    properties: TProperties
    
    def __init__(self):
        # the subclass should update `properties` in its `__init__` method.
        self.properties = {}
    
    def __getattr__(self, key: str):
        if key == _PROPS:
            return getattr(super(), _PROPS, ())
        elif key.startswith('_'):
            return getattr(super(), key)
        
        if key in self.properties:
            return self.__getprop__(key)
        else:
            return self.__getattribute__(key)
    
    def __setattr__(self, key: str, value):
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
        self.properties[key].set(value)
