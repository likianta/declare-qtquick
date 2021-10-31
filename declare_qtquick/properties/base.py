from .__ext__ import PropGetterAndSetter
from .__ext__ import T

__all__ = ['Property', 'PropertyGroup', 'Signal']


class Property:
    qid: T.Qid
    name: T.PropName
    bound: T.Bound
    value: T.Any
    
    def __init__(self, qid: T.Qid, name: T.Name, default_value=None):
        """
        
        Args:
            qid:
            name:
            default_value: Optional[Any]
                None: no value defined, it won't be generated to QML layout.
                      See the process logic in: `..builder.build_properties`.
                It is suggested that the subclasses do not modify default_value
                in its __init__ method.
        """
        self.qid = qid
        self.name = name
        self.bound = []
        self.value = default_value
    
    def kiss(self, arg_0):
        self.value = arg_0
        # if isinstance(arg_0, Property):
        #     self.value = arg_0.value
        # else:
        #     self.value = arg_0
    
    set = kiss  # alias (this is more popular to use)
    
    def bind(self, arg_0: T.BindingArg0, arg_1: T.BindingArg1 = None):
        """ Property binding.

        Notes:
            In declare-qtquick version 0.x, we support only the following types
            of bindings:
                A.width.bind(B.width)
                A.width.bind(B.width, lambda: B.width + 10)
                A.width.bind([B.width, C.width], lambda: B.width or C.width)
            In the future v1.x, we will support advanced bindings like this:
                A.width.bind(B.width)
                A.width.bind(B.width + 10)
                A.width.bind(B.width or C.width)
        """
        if arg_1 is None:
            assert isinstance(arg_0, Property)
            self.bound.append((arg_0.fullname, None))
            return
        
        if isinstance(arg_0, Property):
            arg_0 = (arg_0,)
        for arg in arg_0:
            self.bound.append((arg.fullname, arg_1))
    
    @property
    def fullname(self) -> T.FullName:
        return f'{self.qid}.{self.name}'
    
    def adapt(self) -> str:
        """ Convert python type to qml type. """
        if self.value is None:
            # return something like fullname but a little different.
            from ..common import convert_name_case
            return '{}.{}'.format(self.qid, convert_name_case(self.name))
        elif isinstance(self.value, Property):
            return self.value.adapt()
        else:
            return str(self.value)


class PropertyGroup(PropGetterAndSetter):
    qid: T.Qid
    # overwrite this value in subclass level.
    # see typical usage in `.group_properties.Anchors`.
    name: T.GroupName
    
    # _properties: T.Properties  # came from super class.
    
    def __init__(self, qid: T.Qid, *_):
        PropGetterAndSetter.__init__(self)
        self.qid = qid
        from .prop_sheet.base import init_prop_sheet
        init_prop_sheet(self, prefix=self.name)
    
    def kiss(self, _):
        raise Exception(
            'PropertyGroup doesnt support `kiss` method. '
            'You can only call its sub property to set values.'
        )
    
    set = kiss
    
    def bind(self, *_):
        raise Exception(
            'PropertyGroup doesnt support `bind` method. '
            'You can only call its sub property to bind values.'
        )
    
    @property
    def fullname(self) -> T.FullName:
        return f'{self.qid}.{self.name}'
    
    @property
    def properties(self):
        return self._properties
    
    def adapt(self) -> str:
        return self.fullname


class Signal:
    qid: T.Qid
    name: T.Name
    func: T.Any
    
    def __init__(self, qid: T.Qid, name: T.Name):
        self.qid = qid
        self.name = name
    
    def connect(self, func):
        # from ..common import aslambda  # TODO
        self.func = func
    
    def emit(self, *args, **kwargs):
        self.func(*args, **kwargs)
    
    def adapt(self) -> str:
        from ..pyside import pyside
        func_id = str(id(self.func))
        pyside.register(self.func, name=func_id)
        return 'pyside.call("{}")'.format(func_id)
