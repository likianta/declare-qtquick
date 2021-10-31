from .__base__ import *
from .. import Item
from .. import MultiPointTouchArea
from ..layouts import ColumnLayout
from ..layouts import RowLayout


class BaseKey(Item, W.PsBaseKey):
    pass


class Key(BaseKey, W.PsKey):
    pass


class BackspaceKey(BaseKey, W.PsBackspaceKey):
    pass


class ChangeLanguageKey(BaseKey, W.PsChangeLanguageKey):
    pass


class EnterKey(BaseKey, W.PsEnterKey):
    pass


class EnterKeyAction(Component, W.PsEnterKeyAction):
    pass


class FillerKey(BaseKey, W.PsFillerKey):
    pass


class FlickKey(Key, W.PsFlickKey):
    pass


class HandwritingInputPanel(Item, W.PsHandwritingInputPanel):
    pass


class HandwritingModeKey(Key, W.PsHandwritingModeKey):
    pass


class HideKeyboardKey(BaseKey, W.PsHideKeyboardKey):
    pass


class InputContext(Component, W.PsInputContext):
    pass


class InputEngine(Component, W.PsInputEngine):
    pass


class InputMethod(Component, W.PsInputMethod):
    pass


class InputModeKey(Key, W.PsInputModeKey):
    pass


class InputPanel(Item, W.PsInputPanel):
    pass


class KeyboardColumn(ColumnLayout, W.PsKeyboardColumn):
    pass


class KeyboardLayout(ColumnLayout, W.PsKeyboardLayout):
    pass


class KeyboardLayoutLoader(Loader, W.PsKeyboardLayoutLoader):
    pass


class KeyboardObserver(Component, W.PsKeyboardObserver):
    pass


class KeyboardRow(RowLayout, W.PsKeyboardRow):
    pass


class ModeKey(Key, W.PsModeKey):
    pass


class NumberKey(Key, W.PsNumberKey):
    pass


class SelectionListModel(Component, W.PsSelectionListModel):
    pass


class ShiftHandler(Component, W.PsShiftHandler):
    pass


class ShiftKey(BaseKey, W.PsShiftKey):
    pass


class SpaceKey(Key, W.PsSpaceKey):
    pass


class SymbolModeKey(Key, W.PsSymbolModeKey):
    pass


class Trace(Component, W.PsTrace):
    pass


class TraceInputArea(MultiPointTouchArea, W.PsTraceInputArea):
    pass


class TraceInputKey(Item, W.PsTraceInputKey):
    pass


class VirtualKeyboard(Component, W.PsVirtualKeyboard):
    pass
