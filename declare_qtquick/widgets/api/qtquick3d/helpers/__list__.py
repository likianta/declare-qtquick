from .__base__ import *
from .. import Instancing
from .. import Object3D
from ...qtquick import Item
from ...qtquick import Rectangle


class AxisHelper(Node, W.PsAxisHelper):
    pass


class DebugView(Rectangle, W.PsDebugView):
    pass


class GridGeometry(Geometry, W.PsGridGeometry):
    pass


class InstanceRange(Object3D, W.PsInstanceRange):
    pass


class RandomInstancing(Instancing, W.PsRandomInstancing):
    pass


class WasdController(Item, W.PsWasdController):
    pass
