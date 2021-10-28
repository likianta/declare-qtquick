from collections import defaultdict

from .__external__ import TsContext as T


class IdGenerator:
    
    def __init__(self, prefix='_'):
        self.level = 0
        self._id_chain = defaultdict(int)  # type: T.IdChain
        self._prefix = prefix
    
    def upgrade(self):
        self.level += 1
        self._id_chain[self.level] += 1
    
    def downgrade(self):
        self.level -= 1
    
    def gen_id(self) -> str:
        return self._prefix + '_'.join(map(hex, self._id_chain))


id_gen = IdGenerator()
gen_id = id_gen.gen_id
