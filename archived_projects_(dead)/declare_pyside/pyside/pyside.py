from PySide6.QtCore import QObject
from PySide6.QtCore import Slot

from .register import PyRegister
from ..typehint.pyside import *


class PySide(QObject, PyRegister):
    
    @Slot(TPyFuncName, result=TQVar)
    @Slot(TPyFuncName, TQVal, result=TQVar)
    @Slot(TPyFuncName, TQVal, TQVal, result=TQVar)
    def call(self, func_name: TPyFuncName,
             args: Optional[TQVal] = None,
             kwargs: Optional[TQVal] = None):
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
