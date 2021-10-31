from .__base__ import *
from ..core import Component3D


class AbstractActionInput(Component, W.PsAbstractActionInput):
    pass


class AbstractAxisInput(Component, W.PsAbstractAxisInput):
    pass


class AbstractPhysicalDevice(Component, W.PsAbstractPhysicalDevice):
    pass


class Action(Component, W.PsAction):
    pass


class ActionInput(Component, W.PsActionInput):
    pass


class AnalogAxisInput(Component, W.PsAnalogAxisInput):
    pass


class Axis(Component, W.PsAxis):
    pass


class AxisAccumulator(Component, W.PsAxisAccumulator):
    pass


class AxisSetting(Component, W.PsAxisSetting):
    pass


class ButtonAxisInput(Component, W.PsButtonAxisInput):
    pass


class InputChord(Component, W.PsInputChord):
    pass


class InputSequence(Component, W.PsInputSequence):
    pass


class InputSettings(Component3D, W.PsInputSettings):
    pass


class KeyboardDevice(Node, W.PsKeyboardDevice):
    pass


class KeyboardHandler(Component3D, W.PsKeyboardHandler):
    pass


class KeyEvent(Component, W.PsKeyEvent):
    pass


class LogicalDevice(Component, W.PsLogicalDevice):
    pass


class MouseDevice(Component, W.PsMouseDevice):
    pass


class MouseEvent(Component, W.PsMouseEvent):
    pass


class MouseHandler(Component, W.PsMouseHandler):
    pass


class WheelEvent(Component, W.PsWheelEvent):
    pass
