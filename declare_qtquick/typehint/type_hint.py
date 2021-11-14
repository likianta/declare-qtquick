from os import PathLike as _PathLike
from typing import *

from PySide6 import QtCore as _QtCore
from PySide6 import QtQuick as _QtQuick
from PySide6.QtQml import QJSValue as _QJSValue
from lk_lambdex import lambdex as _lambdex

_TFakeModule = _lambdex('', """
    class FakeModule:
        def __getattr__(self, item):
            return None
        def __call__(self, *args, **kwargs):
            return None
    return FakeModule()
""")()

if __name__ == '__main__':
    from PySide6.QtCore import QObject as _QObject
    from declare_qtquick.widgets.base import Component as _Component
    from declare_qtquick.properties import base as _prop_base
    from declare_qtquick.properties.prop_sheet import base as _prop_sheet
else:
    _Component = None
    _QObject = None
    _prop_base = _TFakeModule
    _prop_sheet = _TFakeModule

# ------------------------------------------------------------------------------

TPath = Union[str, _PathLike]

TQid = str
TName = str
TFullName = str
TPropName = str
TSignalName = str

TProperty = _prop_base.Property
TPropertyGroup = _prop_base.PropertyGroup
TSignal = _prop_base.Signal

TProperties = Dict[TPropName, Union[TProperty, TPropertyGroup]]
TSignals = Dict[TSignalName, TSignal]

TBound = List[Tuple[TFullName, Optional[Callable]]]

TLevel = int
TComponent = _Component
TQObject = _QObject


# ------------------------------------------------------------------------------

class TsBlackMagic:
    Property = TProperty
    QQuickItem = _QtQuick.QQuickItem


class TsComponent:
    Component = TComponent
    FullName = TFullName
    Name = TName
    Properties = TProperties
    Qid = TQid


class TsContext:
    Component = TComponent
    # Context = Dict[TLevel, List[TComponent]]
    Context = List[Tuple[TComponent, 'Context']]
    IdChain = Dict[TLevel, int]
    Level = TLevel
    Qid = TQid
    QidList = List[TQid]


class TsProperty:
    Any = Any
    BindingArg0 = Union[TProperty, Iterable[TProperty]]
    BindingArg1 = Optional[Callable]
    Bool = bool
    Bound = TBound
    Color = str
    Component = TComponent
    Date = str
    FullName = TFullName
    GroupName = TName
    Int = int
    List = Union[list, tuple, set]
    Name = TName
    Number = Union[int, float]
    PropName = TPropName
    Properties = TProperties
    Qid = TQid
    String = str
    Union = Union


class TsPropSheet:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    from typing import _UnionGenericAlias as RealUnionType
    
    Constructable = Union[TProperty, Callable]
    PropSheet = _prop_sheet.PropSheet
    PropSheetIter = Iterator[_prop_sheet.PropSheet]
    Property = TProperty
    PropsIter = Iterator[Tuple[TPropName, TProperty]]
    RawType = Union[TProperty, RealUnionType]
    Target = Union[TComponent, _prop_base.PropertyGroup, _prop_sheet.PropSheet]


class TsPySide:
    Callable = Callable
    Optional = Optional
    
    Arg0 = Literal['', 'self', 'cls']
    NArgs = int  # nargs: 'number of args', int == -1 or >= 0. -1 means
    #   uncertain.
    
    PyClassName = str
    PyFuncName = str
    PyMethName = str
    _RegisteredName = str  # usually this name is same with `TPyFuncName` or
    #   `TPyMethName`, but you can define it with a custom name (something like
    #   "alias").
    
    PyClassHolder = Dict[
        PyClassName, Dict[
            PyMethName, Tuple[_RegisteredName, NArgs]
        ]
    ]
    
    _PyFunction = Callable
    PyFuncHolder = Dict[_RegisteredName, Tuple[_PyFunction, NArgs]]
    
    QVar = 'QVariant'
    QVal = _QJSValue


class TsTraits:
    Properties = TProperties
    Enumerations = Dict[str, Union[int, float, bool, str]]
    Signals = Dict[str, Callable]
