from .__base__ import *
from .. import Item
from ..shapes import Shape


class Affector(C, W.PsAffector):
    pass


class Direction(C, W.PsDirection):
    pass


class ParticlePainter(Item, W.PsParticlePainter):
    pass


class Age(Affector, W.PsAge):
    pass


class AngleDirection(Direction, W.PsAngleDirection):
    pass


class Attractor(Affector, W.PsAttractor):
    pass


class CumulativeDirection(Direction, W.PsCumulativeDirection):
    pass


class EllipseShape(Shape, W.PsEllipseShape):
    pass


class Emitter(C, W.PsEmitter):
    pass


class Friction(Affector, W.PsFriction):
    pass


class Gravity(Affector, W.PsGravity):
    pass


class GroupGoal(Affector, W.PsGroupGoal):
    pass


class ImageParticle(ParticlePainter, W.PsImageParticle):
    pass


class ItemParticle(ParticlePainter, W.PsItemParticle):
    pass


class LineShape(Shape, W.PsLineShape):
    pass


class MaskShape(Shape, W.PsMaskShape):
    pass


class Particle(C, W.PsParticle):
    pass


class ParticleExtruder(C, W.PsParticleExtruder):
    pass


class ParticleGroup(C, W.PsParticleGroup):
    pass


class ParticleSystem(C, W.PsParticleSystem):
    pass


class PointDirection(Direction, W.PsPointDirection):
    pass


class RectangleShape(C, W.PsRectangleShape):
    pass


class SpriteGoal(Affector, W.PsSpriteGoal):
    pass


class TargetDirection(Direction, W.PsTargetDirection):
    pass


class TrailEmitter(C, W.PsTrailEmitter):
    pass


class Turbulence(Affector, W.PsTurbulence):
    pass


class Wander(Affector, W.PsWander):
    pass
