from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication


class Application(QApplication):
    
    def __init__(self, **kwargs):
        super().__init__()
        
        self.engine = QQmlApplicationEngine()
        self.root = self.engine.rootContext()
        
        # Set organization name to avoid warning info if we use QtQuick.Dialogs.
        # FileDialog component
        self.setOrganizationName(kwargs.get(
            'organization', 'dev.likianta.pyqt_compose'
        ))
        self.set_global_conf()
    
    def set_global_conf(self):
        # Set font to Microsoft Yahei if platform is Windows
        from platform import system
        if system() == 'Windows':
            from PySide6.QtGui import QFont
            self.setFont(QFont('Microsoft YaHei'))

    # noinspection PyMethodMayBeStatic
    def build(self):
        return ''

    def start(self, qmlfile: str):
        # from os.path import exists
        # if not exists(qmlfile):
        with open(qmlfile, 'w', encoding='utf-8') as f:
            f.write(self.build())
        
        self.engine.load(qmlfile)
        self.exec_()
