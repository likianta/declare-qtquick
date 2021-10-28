from .type_hint import Union
from .type_hint import _TFakeModule

if __name__ == '__main__':
    from declare_qtquick.properties import normal_properties as _norm_prop
    from declare_qtquick.properties import Property as _Property
else:
    _norm_prop = _TFakeModule
    _Property = None


# ------------------------------------------------------------------------------

class PAnchors:  # the initial character 'P' means 'Property'
    fill: _Property
    center_in: _Property
    horizontal_center: _Property
    vertical_center: _Property
    
    left: _Property
    top: _Property
    right: _Property
    bottom: _Property
    
    margins: Union[int, _norm_prop.Number]
    left_margin: Union[int, _norm_prop.Number]
    top_margin: Union[int, _norm_prop.Number]
    right_margin: Union[int, _norm_prop.Number]
    bottom_margin: Union[int, _norm_prop.Number]


class PItem:
    anchors: PAnchors
    height: Union[int, _norm_prop.Number]
    opacity: Union[float, _norm_prop.Number]
    visible: Union[bool, _norm_prop.Boolean]
    width: Union[int, _norm_prop.Number]
    x: Union[int, _norm_prop.Number]
    y: Union[int, _norm_prop.Number]
    z: Union[int, _norm_prop.Number]


class PWindow(PItem):
    color: Union[str, _norm_prop.String]


class PText(PItem):
    color: Union[str, _norm_prop.String]
    text: Union[str, _norm_prop.String]
