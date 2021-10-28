from pyml.typehint import *


class StaticKeyword:
    
    def __init__(self, text, value):
        self.text = text
        self.value = value
        
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return str(self.value)


class Const:
    
    def __init__(self, value):
        self.value = value
    

def const(x):
    if isinstance(x, Const):
        return x
    else:
        return Const(x)
        
        
def consts(*args):
    return map(Const, args)


class DynamicKeyword:
    _initialized = False
    
    def __init__(self, name):
        self._virtual_ref = name
        self._real_ref = None  # type: TRepresent
        self._initialized = True
    
    def __setattr__(self, key, value):
        if self._initialized:
            if key not in self.__dict__:
                if self._real_ref:
                    self._real_ref.__setattr__(key, value)
                return
                # raise Exception(key, value)
        super().__setattr__(key, value)

    def point_to(self, com: TComponent):
        self._real_ref = com

    @property
    def represents(self) -> TRepresent:
        return self._real_ref
    
    @property
    def uid(self):
        return self._real_ref.uid


class This(DynamicKeyword):
    index = 0
    
    def __init__(self):
        super().__init__('this')
    
    @property
    def parent(self) -> 'Parent':
        global parent
        return parent
    
    @property
    def siblings(self):
        return self.parent.children
    
    @property
    def last_sibling(self):
        if self.index == 0:
            return None
        else:
            return self.parent.children[self.index - 1]
    
    @property
    def next_sibling(self):
        if self.index == len(self.parent.children) - 1:
            return None
        else:
            return self.parent.children[self.index + 1]


class Parent(DynamicKeyword):
    
    def __init__(self):
        super().__init__('parent')
    
    @property
    def children(self) -> list[TComponent]:
        # noinspection PyTypeChecker
        return self.represents.children
    
    def append(self, com: TComponent):
        self.children.append(com)


# ------------------------------------------------------------------------------

true = StaticKeyword('true', True)
false = StaticKeyword('false', False)
null = StaticKeyword('null', None)

this = This()
parent = Parent()
