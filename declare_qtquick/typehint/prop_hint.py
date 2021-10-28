from .type_hint import Union

if __name__ == '__main__':
    from declare_qtquick.properties import Property as _Property
else:
    _Property = None


class PAnchors:
    center_in: _Property
    fill: _Property
    left: _Property
    right: _Property
    top: _Property
    bottom: _Property
    horizontal_center: _Property
    vertical_center: _Property


class PItem:
    height: Union[int, _Property]
    opacity: Union[float, _Property]
    visible: Union[bool, _Property]
    width: Union[int, _Property]
    x: Union[int, _Property]
    y: Union[int, _Property]
    z: Union[int, _Property]


class PWindow(PItem):
    color: Union[str, _Property]


class PText(PItem):
    color: Union[str, _Property]
    text: Union[str, _Property]
