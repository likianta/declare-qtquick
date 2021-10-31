from .__base__ import *
from ..core import Component3D
from ...qtquick3d import Node


class AbstractActionInput(C, W.PsAbstractActionInput):
    pass


class AbstractAxisInput(C, W.PsAbstractAxisInput):
    pass


class AbstractPhysicalDevice(C, W.PsAbstractPhysicalDevice):
    pass


class Action(C, W.PsAction):
    pass


class ActionInput(C, W.PsActionInput):
    pass


class AnalogAxisInput(C, W.PsAnalogAxisInput):
    pass


class Axis(C, W.PsAxis):
    pass


class AxisAccumulator(C, W.PsAxisAccumulator):
    pass


class AxisSetting(C, W.PsAxisSetting):
    pass


class ButtonAxisInput(C, W.PsButtonAxisInput):
    pass


class InputChord(C, W.PsInputChord):
    pass


class InputSequence(C, W.PsInputSequence):
    pass


class InputSettings(Component3D, W.PsInputSettings):
    pass


class KeyboardDevice(Node, W.PsKeyboardDevice):
    pass


class KeyboardHandler(Component3D, W.PsKeyboardHandler):
    pass


class KeyEvent(C, W.PsKeyEvent):
    pass


class LogicalDevice(C, W.PsLogicalDevice):
    pass


class MouseDevice(C, W.PsMouseDevice):
    pass


class MouseEvent(C, W.PsMouseEvent):
    pass


class MouseHandler(C, W.PsMouseHandler):
    pass


class WheelEvent(C, W.PsWheelEvent):
    pass
