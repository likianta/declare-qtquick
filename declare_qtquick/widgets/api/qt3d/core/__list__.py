from .__base__ import *
from ...qtquick import PropertyAnimation


class Node(Component, W.PsNode):
    pass


class AbstractSkeleton(Node, W.PsAbstractSkeleton):
    pass


class Component3D(Node, W.PsComponent3D):
    pass


class Entity(Node, W.PsEntity):
    pass


class Armature(Component3D, W.PsArmature):
    pass


class Attribute(Component, W.PsAttribute):
    pass


class BoundingVolume(Component, W.PsBoundingVolume):
    pass


class Buffer(Component, W.PsBuffer):
    pass


class CoreSettings(Component, W.PsCoreSettings):
    pass


class EntityLoader(Entity, W.PsEntityLoader):
    pass


class Geometry(Node, W.PsGeometry):
    pass


class GeometryView(Node, W.PsGeometryView):
    pass


class Joint(Node, W.PsJoint):
    pass


class NodeInstantiator(Component, W.PsNodeInstantiator):
    pass


class QuaternionAnimation(PropertyAnimation, W.PsQuaternionAnimation):
    pass


class Skeleton(AbstractSkeleton, W.PsSkeleton):
    pass


class SkeletonLoader(AbstractSkeleton, W.PsSkeletonLoader):
    pass


class Transform(Component3D, W.PsTransform):
    pass
