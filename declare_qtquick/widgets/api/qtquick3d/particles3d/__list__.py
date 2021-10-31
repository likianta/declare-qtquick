from xml.dom import Node

from .__base__ import *
from .. import Object3D
from ...qt3d.core import Node
from ...qtqml import QtObject


class Affector3D(Node, W.PsAffector3D):
    pass


class Direction3D(QtObject, W.PsDirection3D):
    pass


class Particle3D(Object3D, W.PsParticle3D):
    pass


class ParticleEmitter3D(Node, W.PsParticleEmitter3D):
    pass


class Attractor3D(Affector3D, W.PsAttractor3D):
    pass


class EmitBurst3D(QtObject, W.PsEmitBurst3D):
    pass


class Gravity3D(Affector3D, W.PsGravity3D):
    pass


class ModelParticle3D(Particle3D, W.PsModelParticle3D):
    pass


class ParticleShape3D(QtObject, W.PsParticleShape3D):
    pass


class ParticleSystem3D(Node, W.PsParticleSystem3D):
    pass


class ParticleSystem3DLogging(QtObject, W.PsParticleSystem3DLogging):
    pass


class PointRotator3D(Affector3D, W.PsPointRotator3D):
    pass


class SpriteParticle3D(Particle3D, W.PsSpriteParticle3D):
    pass


class TargetDirection3D(Direction3D, W.PsTargetDirection3D):
    pass


class TrailEmitter3D(ParticleEmitter3D, W.PsTrailEmitter3D):
    pass


class VectorDirection3D(Direction3D, W.PsVectorDirection3D):
    pass


class Wander3D(Affector3D, W.PsWander3D):
    pass
