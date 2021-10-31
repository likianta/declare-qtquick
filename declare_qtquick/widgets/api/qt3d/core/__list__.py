from .__base__ import *
from ...qtquick import PropertyAnimation


class Node(C, W.PsNode):
    pass


class AbstractSkeleton(Node, W.PsAbstractSkeleton):
    pass


class Component3D(Node, W.PsComponent3D):
    pass


class Entity(Node, W.PsEntity):
    pass


class Armature(Component3D, W.PsArmature):
    pass


class Attribute(C, W.PsAttribute):
    pass


class BoundingVolume(C, W.PsBoundingVolume):
    pass


class Buffer(C, W.PsBuffer):
    pass


class CoreSettings(C, W.PsCoreSettings):
    pass


class EntityLoader(Entity, W.PsEntityLoader):
    pass


class Geometry(Node, W.PsGeometry):
    pass


class GeometryView(Node, W.PsGeometryView):
    pass


class Joint(Node, W.PsJoint):
    pass


class NodeInstantiator(C, W.PsNodeInstantiator):
    pass


class QuaternionAnimation(PropertyAnimation, W.PsQuaternionAnimation):
    pass


class Skeleton(AbstractSkeleton, W.PsSkeleton):
    pass


class SkeletonLoader(AbstractSkeleton, W.PsSkeletonLoader):
    pass


class Transform(Component3D, W.PsTransform):
    pass
