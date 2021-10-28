from os import PathLike as _PathLike
from typing import *

if __name__ == '__main__':
    from declare_qtquick.widgets.base import Component as _Component
    from declare_qtquick.properties import Property as _Property
else:
    _Component = None
    _Property = None

# ------------------------------------------------------------------------------

TPath = Union[str, _PathLike]

TQid = str
TName = str
TFullName = str

TLevel = int

TPropName = str
TProperty = _Property
TProperties = Dict[TPropName, TProperty]
TComponent = _Component


# ------------------------------------------------------------------------------

class TsProperty:
    Any = Any
    BindingArg0 = Union[TProperty, Iterable[TProperty]]
    BindingArg1 = Optional[Callable]
    Bool = bool
    # Bound = List[Tuple[TProperty, BindingArg1]]
    Bound = List[Tuple[TFullName, BindingArg1]]
    Color = str
    FullName = TFullName
    Name = TName
    Number = Union[int, float]
    Properties = TProperties
    Qid = TQid
    String = str


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
