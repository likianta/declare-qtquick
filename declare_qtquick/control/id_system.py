from collections import defaultdict

from .__ext__ import TsContext as T


class IdGenerator:
    
    def __init__(self, prefix='qid_'):
        self.level = 0
        self._id_chain = defaultdict(int)  # type: T.IdChain
        self._prefix = prefix
    
    def upgrade(self):
        self.level += 1
        self._id_chain[self.level] += 1
    
    def downgrade(self):
        # reset children level count
        for level in range(self.level + 1, max(self._id_chain)):
            self._id_chain.pop(level)
        self.level -= 1  # go to uplevel
    
    def gen_id(self) -> str:
        return self._prefix + '_'.join(
            hex(self._id_chain[level]) for level in range(1, self.level + 1)
        )
    
    @property
    def root_id(self):
        return self._prefix + '0x1'


def get_id_level(qid: T.Qid):
    return qid.count('_') - 1


class IdManager:
    _tile_struct: dict
    _relations: dict
    
    def __init__(self):
        self._tile_struct = {}
    
    def set(self, qid: T.Qid, comp: T.Component):
        self._tile_struct[qid] = comp
    
    def finalized(self):
        self._relations = defaultdict(list)
        for qid, comp in self._tile_struct.items():
            # assert '_' in qid
            parent_qid = qid.rsplit('_', 1)[0]
            self._relations[parent_qid].append(comp)
    
    def get_component(self, qid: T.Qid) -> T.Component:
        return self._tile_struct[qid]
    
    def get_children(self, qid: T.Qid) -> T.QidList:
        return self._relations.get(qid, [])
    
    def get_all_components(self):
        for qid, comp in self._tile_struct.items():
            yield qid, comp


id_gen = IdGenerator()
gen_id = id_gen.gen_id

id_mgr = IdManager()
