from .__base__ import *


class WaylandQuickItem(C, W.PsWaylandQuickItem):
    pass


class IdleInhibitManagerV1(C, W.PsIdleInhibitManagerV1):
    pass


class QtTextInputMethodManager(C, W.PsQtTextInputMethodManager):
    pass


class ShellSurface(C, W.PsShellSurface):
    pass


class ShellSurfaceItem(WaylandQuickItem, W.PsShellSurfaceItem):
    pass


class WaylandClient(C, W.PsWaylandClient):
    pass


class WaylandCompositor(C, W.PsWaylandCompositor):
    pass


class WaylandHardwareLayer(C, W.PsWaylandHardwareLayer):
    pass


class WaylandOutput(C, W.PsWaylandOutput):
    pass


class WaylandSeat(C, W.PsWaylandSeat):
    pass


class WaylandSurface(C, W.PsWaylandSurface):
    pass


class WaylandView(C, W.PsWaylandView):
    pass
