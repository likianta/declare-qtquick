from .__base__ import *
from .. import Item
from .. import TableView
from .. import TextInput
from .. import Window
from ...qtqml import QtObject
from ...qtquick import Text
from ...qtquick import TextEdit


class Control(Item, W.PsControl):
    pass


class AbstractButton(Control, W.PsAbstractButton):
    pass


class Container(Control, W.PsContainer):
    pass


class Pane(Control, W.PsPane):
    pass


class ItemDelegate(AbstractButton, W.PsItemDelegate):
    pass


class Popup(QtObject, W.PsPopup):
    pass


class Button(AbstractButton, W.PsButton):
    pass


class Frame(Pane, W.PsFrame):
    pass


class Action(QtObject, W.PsAction):
    pass


class ActionGroup(QtObject, W.PsActionGroup):
    pass


class ApplicationWindow(Window, W.PsApplicationWindow):
    pass


class BusyIndicator(Control, W.PsBusyIndicator):
    pass


class ButtonGroup(QtObject, W.PsButtonGroup):
    pass


class CheckBox(AbstractButton, W.PsCheckBox):
    pass


class CheckDelegate(ItemDelegate, W.PsCheckDelegate):
    pass


class ComboBox(Control, W.PsComboBox):
    pass


class DelayButton(AbstractButton, W.PsDelayButton):
    pass


class Dial(Control, W.PsDial):
    pass


class Dialog(Popup, W.PsDialog):
    pass


class DialogButtonBox(Container, W.PsDialogButtonBox):
    pass


class Drawer(Popup, W.PsDrawer):
    pass


class GroupBox(Frame, W.PsGroupBox):
    pass


class HorizontalHeaderView(TableView, W.PsHorizontalHeaderView):
    pass


class Label(Text, W.PsLabel):
    pass


class Menu(Popup, W.PsMenu):
    pass


class MenuBar(Container, W.PsMenuBar):
    pass


class MenuBarItem(AbstractButton, W.PsMenuBarItem):
    pass


class MenuItem(AbstractButton, W.PsMenuItem):
    pass


class MenuSeparator(Control, W.PsMenuSeparator):
    pass


class Overlay(Item, W.PsOverlay):
    pass


class Page(Pane, W.PsPage):
    pass


class PageIndicator(Control, W.PsPageIndicator):
    pass


class ProgressBar(Control, W.PsProgressBar):
    pass


class RadioButton(AbstractButton, W.PsRadioButton):
    pass


class RadioDelegate(ItemDelegate, W.PsRadioDelegate):
    pass


class RangeSlider(Control, W.PsRangeSlider):
    pass


class RoundButton(Button, W.PsRoundButton):
    pass


class ScrollBar(Control, W.PsScrollBar):
    pass


class ScrollIndicator(Control, W.PsScrollIndicator):
    pass


class ScrollView(Pane, W.PsScrollView):
    pass


class Slider(Control, W.PsSlider):
    pass


class SpinBox(Control, W.PsSpinBox):
    pass


class SplitHandle(QtObject, W.PsSplitHandle):
    pass


class SplitView(Container, W.PsSplitView):
    pass


class StackView(Control, W.PsStackView):
    pass


class SwipeDelegate(ItemDelegate, W.PsSwipeDelegate):
    pass


class SwipeView(Container, W.PsSwipeView):
    pass


class Switch(AbstractButton, W.PsSwitch):
    pass


class SwitchDelegate(ItemDelegate, W.PsSwitchDelegate):
    pass


class TabBar(Container, W.PsTabBar):
    pass


class TabButton(AbstractButton, W.PsTabButton):
    pass


class TextArea(TextEdit, W.PsTextArea):
    pass


class TextField(TextInput, W.PsTextField):
    pass


class ToolBar(Pane, W.PsToolBar):
    pass


class ToolButton(Button, W.PsToolButton):
    pass


class ToolSeparator(Control, W.PsToolSeparator):
    pass


class ToolTip(Popup, W.PsToolTip):
    pass


class Tumbler(Control, W.PsTumbler):
    pass


class VerticalHeaderView(TableView, W.PsVerticalHeaderView):
    pass
