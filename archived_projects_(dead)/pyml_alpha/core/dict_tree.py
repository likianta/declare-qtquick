from copy import deepcopy


class DictTree:
    """
    case:
        case1: insert_inside
        case2: insert_beside
        case3: insert_ouside

    new node insertion scheme:
        {
            last_last_node: {
                last_node: {
                    node: {
                        > case1_new_node_here
                          note that the ancestor nodes also changed in this case
                    }
                    > case2_new_node_here
                }
                > case3_new_node_here
                  note that the ancestor nodes also changed in this case
            }
        }
    """
    default: dict
    
    _key_chain: list
    _key_chain_joint: str
    
    _struct: dict
    
    _last_last_last_node: dict
    _last_last_node: dict
    _last_node: dict
    _node: dict
    
    def __init__(self, default: dict = None):
        self.default = default or {}
        self._struct = {}
        
        self._key_chain = []
        self._key_chain_joint = '◆'
        ''' 关于 self._key_chain_joint 的设计
        
        1. self._key_chain_joint 必须满足特殊性, 也就是说, self._key_chain_joint
           所代表的符号, 在您的源文档应该尽可能不要出现 (或者即使出现, 也不要在
           每节标题中出现)
        2. 如果 self._key_chain_joint 不能满足特殊性, 例如,
           self._key_chain_joint 使用了一个书写频率很高的字符 (比如 '.'), 那么会
           引入一定的解析风险
           该风险的表现是这样的:
                假设在您的源文档中, 有这样的章节:
                    # 我的项目
                    ...
                    ## 架构
                    ...
                    ## 我的项目.架构
                    ...
                那么, 会造成 '## 架构' 中的内容泄露给 '## 我的项目.架构', 较轻的
                影响是进度计算不准确, 严重的影响是 self._key_chain 引用异常!
        '''
        self._init_nodes()
    
    # noinspection PyTypeChecker
    def _init_nodes(self):
        self._last_last_last_node = None
        self._last_last_node = None
        self._last_node = None
        self._node = self._struct
    
    ''' 为什么在 insert_inside, insert_beside 中, 要求参数不能是 None, 而 insert
        _ouside 允许?
    insert_inside 是因为在处理源文档时, 源文档的结构特征在递进时是必须满足 **逐
    级** 递进, 因此每次递进必须是有效值.
    insert_beside 则是从逻辑上来看, 调用者只有在要求给 beside 处插入节点时才会调
    用, 这就要求待插入的节点必须是有效值, 否则 self._node 会无法正常工作.
    insert_ouside 在源文档的结构中, 就允许连续多级反递进, 而且反递进的过程中, 不
    需要传入值 (引用反递进遇到的都是已存在的节点), 所以允许无效值来实现多级 (>1)
    的反递进.
    '''
    
    def insert_inside(self, key, **kwargs):
        self._last_last_last_node = self._last_last_node
        self._last_last_node = self._last_node
        self._last_node = self._node
        
        if key is None:  # see reason at long comment above
            raise KeyError('Key cannot be None when inserting inside')
        default = deepcopy(self.default | kwargs)
        self._node = self._node.setdefault(key, default)
        
        self._key_chain.append(key)
        
        return self._node
    
    def insert_beside(self, key, **kwargs):
        if key is None:  # see reason at long comment above
            raise KeyError('Key cannot be None when inserting beside')
        default = deepcopy(self.default | kwargs)
        self._node = self._last_node.setdefault(key, default)
        
        self._key_chain[-1] = key
        
        return self._node
    
    def insert_ouside(self, key, **kwargs):
        if key is None:
            self._node = self._last_node
        else:
            default = deepcopy(self.default | kwargs)
            self._node = self._last_last_node.setdefault(key, default)
        
        self._last_node = self._last_last_node
        self._last_last_node = self._last_last_last_node
        
        self._key_chain.pop()
        self._key_chain[-1] = key
        
        return self._node
    
    def walk(self):
        """
        Examples:
            self.struct = {
                'A1': {
                    'B1': {},
                    'B2': {
                        'C1': {},
                        'C2': {},
                    }
                }
            }
            -> yields:
                ('A1', 'A1')
                ('A1.B1', 'B1')
                ('A1.B2', 'B2')
                ('A1.B2.C1', 'C1')
                ('A1.B2.C2', 'C2')

        Yields:
            (str key_chain, str key)
        """
        key_chain = []
        
        def rec(node: dict):
            for k, v in node.items():
                key_chain.append(k)  # ['A1'] -> ['A1.B1']
                yield self._key_chain_joint.join(key_chain), k
                yield from rec(v)  # ['A1.B1'] -> ['A1']
            if key_chain:
                key_chain.pop()
        
        yield from rec(self._struct)
    
    def split_keys(self, key_chain: str):
        """
        Warnings: see `self.__init__:attrs:_key_chain_joint:comments:关于 self.
            _key_chain_joint 的设计`
        """
        return key_chain.split(self._key_chain_joint)
    
    def relocate_chain(self, key_chain: str, force_create_node=False, **kwargs):
        """
        
        Warnings: 该函数的处理逻辑较冗长, 请避免高频调用.
        
        Examples: see `worklog_report_generator.main._report`
        """
        if force_create_node is False:
            # FIXME: self._node doesn't catch up the step
            return eval('self.struct[{}]'.format(
                key_chain.replace(self._key_chain_joint, '][')
            ))
        else:
            self._init_nodes()
            for key in self.split_keys(key_chain):
                self.insert_inside(key, **kwargs)
    
    @property
    def struct(self):
        return self._struct
    
    @property
    def node(self):
        return self._node
    
    @property
    def key(self):
        return self._key_chain[-1]
    
    @property
    def key_chain(self):
        return self._key_chain_joint.join(self._key_chain)


class DictTreeEx(DictTree):
    """
    Examples:
        see typical usage at `worklog_report_generator.main._report`
    """
    
    def __init__(self, default, setin: str):
        assert setin in default and isinstance(default[setin], dict)
        self._setin = setin
        
        super().__init__(default)
        
        self._struct = {setin: {}}
        self._node = self._struct
    
    def insert_inside(self, key, **kwargs):
        # pretend
        temp = self._node
        self._node = self._node[self._setin]
        
        super().insert_inside(key, **kwargs)
        
        # unpretend
        self._last_node = temp
        
        return self._node
    
    def insert_beside(self, key, **kwargs):
        # pretend
        temp = self._last_node
        self._last_node = self._last_node[self._setin]
        
        super().insert_beside(key, **kwargs)
        
        # unpretend
        self._last_node = temp
        
        return self._node
    
    def insert_ouside(self, key, **kwargs):
        # pretend
        temp = self._last_last_node
        self._last_last_node = self._last_last_node[self._setin]
        
        super().insert_ouside(key, **kwargs)
        
        # unpretend
        self._last_last_node = temp
        self._last_node = self._last_last_node
        
        return self._node
    
    def walk(self):
        raise NotImplementedError('StructEx.walk() is disabled!')
    
    @property
    def struct(self):
        return self._struct[self._setin]
