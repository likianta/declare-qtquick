from PySide6.QtCore import QObject
from PySide6.QtCore import Slot

from .__ext__ import T
from .register import PyRegister


class PySide(QObject, PyRegister):
    
    @Slot(T.PyFuncName, result=T.QVar)
    @Slot(T.PyFuncName, T.QVal, result=T.QVar)
    @Slot(T.PyFuncName, T.QVal, T.QVal, result=T.QVar)
    def call(self, func_name: T.PyFuncName,
             args: T.Optional[T.QVal] = None,
             kwargs: T.Optional[T.QVal] = None):
        """ Call Python functions in QML files.
        
        See detailed docstring at `~/docs/pyside-handler-usage.md`.
        """
        func, narg = self._pyfunc_holder[func_name]  # narg: 'number of args'
        
        args = [] if args is None else (args.toVariant() or [])
        kwargs = {} if kwargs is None else (kwargs.toVariant() or {})
        
        if kwargs:
            return func(*args, **kwargs)
        elif narg == 0:
            return func()
        elif narg == -1:  # see `PyRegister._get_number_of_args.<return>`
            return func(*args)
        else:
            if isinstance(args, list) and narg > 1:
                return func(*args)
            else:  # this is a feature.
                return func(args)


pyside = PySide()
reg = pyside.register_via_decorator
