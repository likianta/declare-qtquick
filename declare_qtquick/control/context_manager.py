from .__ext__ import TsContext as T
from .id_system import id_gen


class ContextManager:
    
    def __init__(self):
        self._id_gen = id_gen
        self._root = []
        self._node = self._root
        self._node_chain = self._root
    
    def upgrade(self, obj: T.Component):
        self._id_gen.upgrade()
        
        temp = []
        self._node.append((obj, temp))
        self._node_chain.append(temp)
        self._node = temp
        
        return self._id_gen.gen_id()
    
    def downgrade(self):
        self._node_chain.pop()
        self._node = self._node_chain[-1]
    
    def dump(self):
        return self._root
    
    @property
    def level(self):
        return self._id_gen.level


ctx_mgr = ContextManager()
