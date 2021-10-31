from .__base__ import *


class WaylandQuickItem(Component, W.PsWaylandQuickItem):
    pass


class IdleInhibitManagerV1(Component, W.PsIdleInhibitManagerV1):
    pass


class QtTextInputMethodManager(Component, W.PsQtTextInputMethodManager):
    pass


class ShellSurface(Component, W.PsShellSurface):
    pass


class ShellSurfaceItem(WaylandQuickItem, W.PsShellSurfaceItem):
    pass


class WaylandClient(Component, W.PsWaylandClient):
    pass


class WaylandCompositor(Component, W.PsWaylandCompositor):
    pass


class WaylandHardwareLayer(Component, W.PsWaylandHardwareLayer):
    pass


class WaylandOutput(Component, W.PsWaylandOutput):
    pass


class WaylandSeat(Component, W.PsWaylandSeat):
    pass


class WaylandSurface(Component, W.PsWaylandSurface):
    pass


class WaylandView(Component, W.PsWaylandView):
    pass
