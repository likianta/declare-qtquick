from .__base__ import *
from .. import NumberAnimation
from ...qtqml import QtObject


class Keyframe(QtObject, W.PsKeyframe):
    pass


class KeyframeGroup(QtObject, W.PsKeyframeGroup):
    pass


class Timeline(QtObject, W.PsTimeline):
    pass


class TimelineAnimation(NumberAnimation, W.PsTimelineAnimation):
    pass
