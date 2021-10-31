from declare_qtquick.widgets.api.qtqml import QtObject
from .__base__ import *


class Dialog(QtObject, W.PsDialog):
    pass


class MenuItem(QtObject, W.PsMenuItem):
    pass


class ColorDialog(Dialog, W.PsColorDialog):
    pass


class FileDialog(Dialog, W.PsFileDialog):
    pass


class FolderDialog(Dialog, W.PsFolderDialog):
    pass


class FontDialog(Dialog, W.PsFontDialog):
    pass


class Menu(QtObject, W.PsMenu):
    pass


class MenuBar(QtObject, W.PsMenuBar):
    pass


class MenuItemGroup(QtObject, W.PsMenuItemGroup):
    pass


class MenuSeparator(MenuItem, W.PsMenuSeparator):
    pass


class MessageDialog(Dialog, W.PsMessageDialog):
    pass


class StandardPaths(QtObject, W.PsStandardPaths):
    pass


class SystemTrayIcon(QtObject, W.PsSystemTrayIcon):
    pass
