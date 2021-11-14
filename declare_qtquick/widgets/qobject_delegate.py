from PySide6.QtCore import QObject


class QObjectDelegate:
    qobj: QObject
    
    def __init__(self, qobj):
        self.qobj = qobj

    
