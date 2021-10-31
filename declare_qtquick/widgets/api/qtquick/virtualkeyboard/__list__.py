from .__base__ import *
from .. import Item
from .. import Loader
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


class EnterKeyAction(C, W.PsEnterKeyAction):
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


class InputContext(C, W.PsInputContext):
    pass


class InputEngine(C, W.PsInputEngine):
    pass


class InputMethod(C, W.PsInputMethod):
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


class KeyboardObserver(C, W.PsKeyboardObserver):
    pass


class KeyboardRow(RowLayout, W.PsKeyboardRow):
    pass


class ModeKey(Key, W.PsModeKey):
    pass


class NumberKey(Key, W.PsNumberKey):
    pass


class SelectionListModel(C, W.PsSelectionListModel):
    pass


class ShiftHandler(C, W.PsShiftHandler):
    pass


class ShiftKey(BaseKey, W.PsShiftKey):
    pass


class SpaceKey(Key, W.PsSpaceKey):
    pass


class SymbolModeKey(Key, W.PsSymbolModeKey):
    pass


class Trace(C, W.PsTrace):
    pass


class TraceInputArea(MultiPointTouchArea, W.PsTraceInputArea):
    pass


class TraceInputKey(Item, W.PsTraceInputKey):
    pass


class VirtualKeyboard(C, W.PsVirtualKeyboard):
    pass
