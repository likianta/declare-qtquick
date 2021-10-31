from .__ext__ import TsContext as T
from .id_system import id_gen


class ContextManager:
    
    def __init__(self):
        self._id_gen = id_gen
        self._root = []
        self._node = self._root
        self._node_history = []
    
    def upgrade(self, obj: T.Component):
        temp = []
        self._node.append((obj, temp))
        last_node, self._node = self._node, temp
        self._node_history.append(last_node)
        
        ''' Illustration
        
        step 1:
            [(A, [])] -> [(A, [(B, [])])]
            |    ^^1|    |    | ^2 ^^3| |
            ^-4-----^    |    ^-1-----^ |
                         ^-4------------^
            1: self._node
            2: obj
            3: temp
            4: self._root
            ~. self._node_history = [#4]
        
        step 2:
            [(A, [(B, [])])]
            |    |    ^^1| |
            |    ^-2-----^ |
            ^-3------------^
            1. self._node = temp
            3. self._root
            ~. self._node_history = [#3, #2]
        '''

        self._id_gen.upgrade()
        return self._id_gen.gen_id()
    
    def downgrade(self):
        self._node = self._node_history.pop()
        self._id_gen.downgrade()
    
    def dump(self):
        return self._root
    
    @property
    def level(self):
        return self._id_gen.level


ctx_mgr = ContextManager()
