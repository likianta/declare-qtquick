from .__base__ import *
from ...qtqml import QtObject


class AbstractAnimation(Component, W.PsAbstractAnimation):
    pass


class AbstractClipAnimator(Component, W.PsAbstractClipAnimator):
    pass


class AbstractClipBlendNode(Component, W.PsAbstractClipBlendNode):
    pass


class AdditiveClipBlend(Component, W.PsAdditiveClipBlend):
    pass


class AnimationController(Component, W.PsAnimationController):
    pass


class AnimationGroup(Component, W.PsAnimationGroup):
    pass


class BlendedClipAnimator(AbstractClipAnimator, W.PsBlendedClipAnimator):
    pass


class ClipAnimator(AbstractClipAnimator, W.PsClipAnimator):
    pass


class ClipBlendValue(Component, W.PsClipBlendValue):
    pass


class KeyframeAnimation(AbstractAnimation, W.PsKeyframeAnimation):
    pass


class LerpClipBlend(Component, W.PsLerpClipBlend):
    pass


class MorphingAnimation(AbstractAnimation, W.PsMorphingAnimation):
    pass


class MorphTarget(QtObject, W.PsMorphTarget):
    pass


class VertexBlendAnimation(AbstractAnimation, W.PsVertexBlendAnimation):
    pass
