from .__base__ import *
from ..qtquick import Item


class SignalSpy(Item, W.PsSignalSpy):
    pass


class TestCase(Item, W.PsTestCase):
    pass


class TouchEventSequence(Component, W.PsTouchEventSequence):
    pass
