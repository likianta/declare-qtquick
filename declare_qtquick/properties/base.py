from .__external__ import TsProperty as T


class Property:
    qid: T.Qid
    name: T.Name
    bound: T.Bound
    value: T.Any
    
    def __init__(self, qid: T.Qid, name: T.Name, default_value=None):
        self.qid = qid
        self.name = name
        self.bound = []
        self.value = default_value
    
    def kiss(self, arg_0):
        if isinstance(arg_0, Property):
            self.value = arg_0.value
        else:
            self.value = arg_0
    
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
            self.value = arg_0.fullname
            return
        
        if isinstance(arg_0, Property):
            arg_0 = (arg_0,)
        for arg in arg_0:
            self.bound.append((arg.fullname, arg_1))
    
    @property
    def fullname(self) -> T.FullName:
        return f'{self.qid}.{self.name}'
