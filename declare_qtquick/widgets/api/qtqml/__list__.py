from .__base__ import *


class Binding(Component, W.PsBinding):
    pass


class Component(Component, W.PsComponent):
    pass


class Connections(Component, W.PsConnections):
    pass


class Date(Component, W.PsDate):
    pass


class Locale(Component, W.PsLocale):
    pass


class LoggingCategory(Component, W.PsLoggingCategory):
    pass


class Number(Component, W.PsNumber):
    pass


class Qt(Component, W.PsQt):
    pass


class QtObject(Component, W.PsQtObject):
    pass


class String(Component, W.PsString):
    pass


class Timer(Component, W.PsTimer):
    pass
