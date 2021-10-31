from .__base__ import *
from .. import Item


class Affector(Component, W.PsAffector):
    pass


class Direction(Component, W.PsDirection):
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


class Emitter(Component, W.PsEmitter):
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


class Particle(Component, W.PsParticle):
    pass


class ParticleExtruder(Component, W.PsParticleExtruder):
    pass


class ParticleGroup(Component, W.PsParticleGroup):
    pass


class ParticleSystem(Component, W.PsParticleSystem):
    pass


class PointDirection(Direction, W.PsPointDirection):
    pass


class RectangleShape(Component, W.PsRectangleShape):
    pass


class SpriteGoal(Affector, W.PsSpriteGoal):
    pass


class TargetDirection(Direction, W.PsTargetDirection):
    pass


class TrailEmitter(Component, W.PsTrailEmitter):
    pass


class Turbulence(Affector, W.PsTurbulence):
    pass


class Wander(Affector, W.PsWander):
    pass
