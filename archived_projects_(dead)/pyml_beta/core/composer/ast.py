"""
@Author   : likianta (likianta@foxmail.com)
@FileName : ast.py
@Version  : 0.5.0
@Created  : 2020-11-02
@Updated  : 2020-11-10
@Desc     :
"""
import re
from collections import defaultdict

from pyml_rc.declare_pyml.core._typing_hints import CompAstHint as Hint


class SourceAst2:
    
    def __init__(self, pyml_file: str):
        self.source_map = self._tokenize(pyml_file)
        pass
    
    @staticmethod
    def _tokenize(pyml_file: str):
        import tokenize
        from lk_utils.lk_logger import lk
        
        out = {}
        
        with tokenize.open(pyml_file) as file:
            tokens = tokenize.generate_tokens(file.readline)
            for token in tokens:
                type_, name, start, end, line = token
                
                # exact type
                if type_ == tokenize.OP:
                    type_ = token.exact_type
                
                lineno = f'line{start[0]}'
                if lineno not in out:
                    out[lineno] = {
                        'lineno': lineno,
                        'line'  : line,
                        'level' : 0 if type_ not in (
                            Hint.INDENT, Hint.DEDENT
                        ) else len(name),
                        #   type_: 'INDENT' -> name: e.g. '    '
                        'tokens': []
                    }
                out[lineno]['tokens'].append((name, type_))
                
                lk.logax(type_, name, start, end)
        
        # merge lines
        pass
        
        return out


class SourceAst:
    """ Source code abstract syntax tree. """
    
    def __init__(self, source_code: str):
        """

        :param source_code: from `Mask.get_plain_text(merge_block=True)`
        """
        # self.source_code = source_code
        self.source_tree = self._build_source_tree(source_code.split('\n'))
        self.source_map = self._build_source_map(self.source_tree)
        self.source_chain = self._build_source_chain(self.source_tree)
    
    @staticmethod
    def _build_source_tree(code_lines: list) -> Hint.SourceTree:
        root_node_scaffold = {  # type: Hint.SourceNode
            'lineno'  : '',
            'level'   : -4,  # abbreviation: lv
            'parent'  : None,
            'children': {}
            #           ^^ 这里才是我们最终要的结果, root_node_scaffold 本身只是
            #              一个脚手架.
        }
        node_chain = [root_node_scaffold]
        """ How does node chain work?

            if curr_lv > last_lv:
                [..., last_node] -> [..., last_node, curr_node]
                                                     ^ added
            if curr_lv == last_lv:
                [..., last_last_node, last_node] ->
                [..., last_last_node, curr_node]
                                      ^ substituted
            if curr_lv < last_lv:
                It depends on how many reverse indents:
                    -1 indent:
                        [..., lalalast_node, lalast_node, last_node] ->
                        [..., lalalast_node, curr_node]
                                             ^ substituted
                    -2 indents:
                        [..., lalalalast_node, lalalast_node,
                         lalast_node, last_node] ->
                        [..., lalalalast_node, curr_node]
                                               ^ substituted
                    -3 indents:
                        [..., lalalalalast_node, lalalalast_node,
                         lalalast_node, lalast_node, last_node] ->
                        [..., lalalalalast_node, curr_node]
                                                 ^ substituted
                    ...

            We can use pop-and-add action to implement it easily, please see it
            at "# === Node chain implementation ===".
        """
        
        last_lv = -4
        
        def _get_level(line):
            pattern = re.compile(r'^ *')
            whitespaces = pattern.match(line).group()
            return len(whitespaces)
            #   assert len(whitespaces) % 4 == 0
        
        for curr_no, curr_ln in enumerate(code_lines):
            #   curr_no: current line number; curr_ln: current line
            if curr_ln.strip() == '':
                continue
            
            curr_lv = _get_level(curr_ln)
            assert curr_lv % 4 == 0, (curr_no, curr_ln)
            
            # === Node chain implementation ===
            if curr_lv > last_lv:
                pass
            elif curr_lv == last_lv:
                node_chain = node_chain[:-1]
            else:
                pos = int(curr_lv / 4) + 1
                #   e.g. curr_lv = 0 -> pos = 1 -> data_node_chain = [root]
                node_chain = node_chain[:pos]
            curr_node = node_chain[-1]['children'].setdefault(
                f'line{curr_no}', {
                    'lineno'       : f'line{curr_no}',
                    'line'         : curr_ln,
                    'line_stripped': curr_ln.strip(),
                    'level'        : curr_lv,
                    'parent'       : node_chain[-1]['lineno'],
                    #   'parent'  : node_chain[-1],  # 未采用, 这样会导致输出
                    #       json 时产生回环错误.
                    'children'     : {},
                }
            )
            node_chain.append(curr_node)
            
            last_lv = curr_lv
        
        root_node = root_node_scaffold['children']  # type: Hint.SourceTree
        return root_node
    
    @staticmethod
    def _build_source_map(tree: Hint.SourceTree):
        out = {}
        
        def _recurse(subtree: Hint.SourceTree):
            for lineno, node in subtree.items():
                out[lineno] = node
                _recurse(node['children'])
        
        _recurse(tree)
        return out
    
    @staticmethod
    def _build_source_chain(tree: Hint.SourceTree):
        scaffold = defaultdict(list)
        
        def _recurse(subtree: Hint.SourceTree):
            for lineno, node in subtree.items():
                scaffold[node['level']].append(node)
                _recurse(node['children'])
        
        _recurse(tree)
        
        out = []
        for k in sorted(scaffold.keys()):
            out.append(scaffold[k])
        return out
    
    # --------------------------------------------------------------------------
    
    def get_compdef_blocks(self):
        """
        注意: 当前版本不支持嵌套组件声明. 也就是说:
            comp A:
                comp B:  # <- 不支持!
                    pass
        :return:
        """
        out = []
        for no, node in self.source_tree.items():
            assert node['level'] == 0
            if node['line_stripped'].startswith('comp '):
                out.append(node)
        return out
    
    @staticmethod
    def output_plain_text_from_struct(struct: Hint.SourceNode):
        """ 将 struct 转换为纯字符串. 与 self._build_tree() 的过程相反. """
        out = [struct['line']]
        
        def _recurse(subtree: Hint.SourceTree):
            for no, node in subtree.items():
                out.append(node['line'])
                _recurse(node['children'])
        
        _recurse(struct['children'])
        return '\n'.join(out)


class ComponentAst:
    """
    
    """
    
    def __init__(self, comp_block_tree: Hint.SourceTree,
                 namespace: Hint.CompNameSpace):
        """
        
        :param comp_block_tree:
        :param namespace:
        """
        self._idx = 0
        self._namespace = namespace
        
        self.comp_tree = self._build_comp_tree(comp_block_tree)
        self.comp_map = self._build_comp_map(self.comp_tree)
        self.comp_chain = self._build_comp_chain(self.comp_tree)
    
    def _build_comp_tree(self, root: Hint.SourceTree) -> Hint.CompTree:
        """ 识别组件块中的每一个组件节点, 为其创建一个组件 id, 并获取它的内建属
            性信息.
        :return:
        """
        root_id = 'root'
        root_node_scaffold = {
            'id'      : '',
            'lineno'  : '',
            'props'   : [],
            'context' : {
                'root'    : root_id,
                'parent'  : '',
                'self'    : root_id,
                'children': []
            },
            'children': {}
        }
        
        def _recurse(tree: Hint.SourceTree, parent):
            for lineno, node in tree.items():
                if comp_props := self._is_component(node['line_stripped']):
                    comp_id = self._gen_auto_id()
                    
                    next_parent = parent['children'][comp_id] = {
                        'id'      : comp_id,
                        'lineno'  : lineno,
                        'props'   : comp_props['props'],
                        'context' : {
                            'root'    : root_id,
                            'parent'  : parent['id'],
                            'self'    : comp_id,
                            'children': []
                        },
                        'children': {
                        
                        }
                    }
                    parent['context']['children'][comp_id] = next_parent
                    
                    next_tree = node['children']
                    _recurse(next_tree, next_parent)
        
        _recurse(root, root_node_scaffold)
        
        root_node = root_node_scaffold['children']
        return root_node
    
    @staticmethod
    def _build_comp_map(tree: Hint.CompTree) -> Hint.CompMap:
        out = {}
        
        def _recurse(subtree: Hint.CompTree):
            for compid, node in subtree.items():
                out[compid] = node
                _recurse(node['children'])
        
        _recurse(tree)
        return out
    
    @staticmethod
    def _build_comp_chain(tree: Hint.CompTree) -> Hint.CompChain:
        scaffold = defaultdict(list)
        level = 0
        
        def _recurse(subtree: Hint.CompTree):
            nonlocal level
            level += 1
            for compid, node in subtree.items():
                scaffold[level].append(node)
                _recurse(node['children'])
            level -= 1
        
        _recurse(tree)
        
        out = []
        for k in sorted(scaffold.keys()):
            out.append(scaffold[k])
        return out
    
    def _gen_auto_id(self) -> Hint.CompId:
        self._idx += 1
        return f'id{self._idx}'
    
    def _is_component(self, line: str) -> Hint.CompProps:
        pattern = re.compile(r'^[A-Z]\w*([A-Z]\w*):|^([A-Z]\w*):')
        #                               ^--------^   ^--------^
        if match := pattern.search(line):
            name = match.group(1) or match.group(2)
            if name in self._namespace:
                return self._namespace[name]
            else:
                raise Exception('Unknown component name which is unregistered '
                                'in namespace', name)
        else:
            return None
