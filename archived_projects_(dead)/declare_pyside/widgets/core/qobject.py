class QObject:
    
    def __init__(self, qobj):
        self.qobj = qobj
    
    def __getattr__(self, item):
        pass
        
    def __setattr__(self, key, value):
        pass
