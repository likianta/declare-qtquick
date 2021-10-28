from .__external__ import PropGetterAndSetter
from .__external__ import TsComponent as T
from .__external__ import ctx_mgr


class Component(PropGetterAndSetter):
    qid: T.Qid  # the qid is initialized in its `__enter__` method.
    name: T.Name
    
    def __init__(self):
        super().__init__()
        # 1. do not initialize name here, you'd better do it in the class level.
        #    see how do subclasses do it.
        # 2. don't forget to update self.properties in subclasses.
        #    see typical usage in `.item.Item.__init__`.
    
    def build(self, level=0) -> str:
        from declare_qtquick.builder import build_component
        return build_component(self, level)
    
    def __enter__(self):
        self.qid = ctx_mgr.upgrade(self)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx_mgr.downgrade()
