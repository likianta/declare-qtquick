from .__base__ import *
from ...qtqml import QtObject


class AbstractAnimation(C, W.PsAbstractAnimation):
    pass


class AbstractClipAnimator(C, W.PsAbstractClipAnimator):
    pass


class AbstractClipBlendNode(C, W.PsAbstractClipBlendNode):
    pass


class AdditiveClipBlend(C, W.PsAdditiveClipBlend):
    pass


class AnimationController(C, W.PsAnimationController):
    pass


class AnimationGroup(C, W.PsAnimationGroup):
    pass


class BlendedClipAnimator(AbstractClipAnimator, W.PsBlendedClipAnimator):
    pass


class ClipAnimator(AbstractClipAnimator, W.PsClipAnimator):
    pass


class ClipBlendValue(C, W.PsClipBlendValue):
    pass


class KeyframeAnimation(AbstractAnimation, W.PsKeyframeAnimation):
    pass


class LerpClipBlend(C, W.PsLerpClipBlend):
    pass


class MorphingAnimation(AbstractAnimation, W.PsMorphingAnimation):
    pass


class MorphTarget(QtObject, W.PsMorphTarget):
    pass


class VertexBlendAnimation(AbstractAnimation, W.PsVertexBlendAnimation):
    pass
