from declare_qtquick.widgets.api.qtqml import QtObject
from .__base__ import *
from ... import Canvas
from ... import Item


class KeyboardStyle(QtObject, W.PsKeyboardStyle):
    pass


class KeyIcon(Item, W.PsKeyIcon):
    pass


class KeyPanel(Item, W.PsKeyPanel):
    pass


class SelectionListItem(Item, W.PsSelectionListItem):
    pass


class TraceCanvas(Canvas, W.PsTraceCanvas):
    pass


class TraceInputKeyPanel(Item, W.PsTraceInputKeyPanel):
    pass
