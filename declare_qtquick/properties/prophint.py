from .__external__.typehint import Union
from .base import Property


class PItem:
    height: Union[int, Property]
    opacity: Union[float, Property]
    visible: Union[bool, Property]
    width: Union[int, Property]
    x: Union[int, Property]
    y: Union[int, Property]
    z: Union[int, Property]


class PWindow(PItem):
    color: Union[str, Property]


class PText(PItem):
    color: Union[str, Property]
    text: Union[str, Property]
