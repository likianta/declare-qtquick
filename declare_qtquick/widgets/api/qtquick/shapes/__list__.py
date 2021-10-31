from .__base__ import *
from .. import Gradient
from .. import Item


class ShapeGradient(Gradient, W.PsShapeGradient):
    pass


class ConicalGradient(ShapeGradient, W.PsConicalGradient):
    pass


class LinearGradient(ShapeGradient, W.PsLinearGradient):
    pass


class RadialGradient(ShapeGradient, W.PsRadialGradient):
    pass


class Shape(Item, W.PsShape):
    pass


class ShapePath(Path, W.PsShapePath):
    pass
