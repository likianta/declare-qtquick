"""
@Author   : Likianta (likianta@foxmail.com)
@FileName : composer.py
@Version  : 0.3.0
@Created  : 2020-11-02
@Updated  : 2020-11-06
@Desc     : DELETE: This module is going to be removed.
"""
import re
from collections import defaultdict

from lk_logger import lk

from pyml_dsl.core._typing_hints import InterpreterHint as Hint


class PlainComposer:
    
    def __init__(self):
        self.lines = defaultdict(list)  # {source_lineno: lines, ...}
    
    def submit(self, node: Hint.SourceNode):
        self.lines[node['lineno']].append(node['line'])
    
    def export(self):
        out = []
        for lineno, lines in self.lines.items():
            out.extend(lines)
        return out


class ComponentComposer:
    
    def __init__(self, comp_block: Hint.SourceNode):
        self.lines = defaultdict(list)  # {source_lineno: lines, ...}
        
        self._comp_block = comp_block  # a single comp block
        self._comp_block_tree = {comp_block['lineno']: comp_block}
        
        self.ids = {}  # type: Hint.IDs
        self._build_ids()  # `self._comp_block` and `self.ids` got updated
        self._build_fields()
        self._build_node_types()
    
    def _build_ids(self):
        """
        
        :return: {
                ...
                'context': {
                    relative_id: absolute_id,
                        -> relative_id: <'root', 'parent', 'self'>
                        -> absolute_id: see `self.ids` dict
                    custom_id: absolute_id,
                    ...
                }
            }
        """
        
        # noinspection PyUnboundLocalVariable
        def _custom_id(line: str):
            # please pass node['line_stripped'] to the param
            if ('@' in line) and \
                    (match := re.compile(r'(?<= @)\w+').search(line)):
                _id = match.group(0)
            elif (line.startswith('id')) and \
                    (match := re.compile(r'^id *: *(\w+)').search(line)):
                _id = match.group(1)
            else:
                _id = ''
            return _id
        
        def _recurse(tree: Hint.SourceTree, parent):
            for node in tree.values():
                if self._is_component_name(node['line_stripped']):
                    node['context'] = {
                        'root'  : 'root',
                        'parent': parent['context']['self'],
                        'self'  : self._register_id(node),
                    }
                else:
                    node['context'] = parent['context']
                    
                    # ????????????????????????, ?????????
                    if _id := _custom_id(node['line_stripped']):
                        self._register_id(parent, _id)
                
                _recurse(node['children'], node)
        
        # ----------------------------------------------------------------------
        
        self._comp_block.update({
            'context': {
                'root'  : 'root',
                'parent': '',
                'self'  : self._register_id(self._comp_block, 'root'),
            }
        })
        # ????????????????????????, ?????????
        if _id := _custom_id(self._comp_block['line_stripped']):
            self._register_id(self._comp_block, _id)
        
        _recurse(self._comp_block['children'], self._comp_block)
    
    def _build_fields(self):
        """
        
        :return: {
                'field': <'comp_def', 'comp_body', 'attr', 'style', 'children'>,
                ...
            }
        """
        pattern = re.compile(r'<(\w+)>')
        
        def _recurse(tree: Hint.SourceTree):
            for node in tree.values():
                ln = node['line_stripped']
                if ln.startswith('comp '):
                    field = 'comp_def'
                elif m := pattern.match(ln):
                    field = m.group(1)
                else:
                    field = 'comp_body'
                node['field'] = field
                _recurse(node['children'])
        
        _recurse(self._comp_block_tree)
    
    def _build_node_types(self):
        """
        
        :return: {
                'node_type': <
                    str
                        'class_def',
                        'comp_def',
                        'comp_instance',
                        'func_def',
                        'import',
                        'on_signal',
                        'prop_assign',
                        'pseudo_field',
                >,
                ...
            }
        """
        _temp_token = ''
        
        def _recurse(tree: Hint.SourceTree):
            nonlocal _temp_token
            
            for node in tree.values():
                ln = node['line_stripped']
                # simple
                if ln.startswith(('import ', 'from ')):
                    node['node_type'] = 'import'
                elif ln.startswith('comp '):
                    node['node_type'] = 'comp_def'
                elif ln.startswith('class '):
                    node['node_type'] = 'class_def'
                elif ln.startswith('def '):
                    node['node_type'] = 'func_def'
                # not stable
                elif ln.startswith('<') and ln.endswith('>'):
                    node['node_type'] = 'pseudo_field'
                elif ln.startswith('on_'):
                    node['node_type'] = 'on_signal'
                # complex
                elif ln.endswith('::'):
                    node['node_type'] = 'prop_assigns'
                    _temp_token = '::'
                elif self._is_component_name(ln) and _temp_token == '':
                    node['node_type'] = 'comp_instance'
                else:
                    node['node_type'] = 'prop_assigns'
                
                _recurse(node['children'])
                _temp_token = ''
        
        _recurse(self._comp_block_tree)
    
    # --------------------------------------------------------------------------
    
    _simple_num = 0  # see `self._register_id`
    
    def _register_id(self, node: Hint.SourceNode, comp_id=''):
        if comp_id == '':
            self._simple_num += 1
            comp_id = f'id{self._simple_num}'
        # self.ids[comp_id] = node  # A
        self.ids[comp_id] = node['lineno']  # B
        # setattr(self.ids, comp_id, node)
        return comp_id
    
    @staticmethod
    def _is_component_name(name) -> bool:
        """ ???????????????????????????, ???????????? name ???????????????????????????: ?????????, ?????????
            ????????????; ??????????????????.
        
        WARNING: ???????????????????????????????????????, ??????????????????! ????????????????????? import
            ?????????????????????.
            
        :param name: ????????? node['line_stripped'] <- node: CompAstHint.AstNode
        :return:
        """
        pattern = re.compile(r'[A-Z]\w+')
        return bool(pattern.match(name))
    
    # --------------------------------------------------------------------------
    
    def main(self):
        from pyml_dsl.core.composer.lang_interp import (
            PymlInterpreter, PythonInterpreter, QmlInterpreter
        )
        
        pyml_interp = PymlInterpreter()
        python_interp = PythonInterpreter()
        qml_interp = QmlInterpreter()
        """ pyml_interp ????????? pyml ?????? (??????????????????) ???????????????,
            python_interp ??? qml_interp ????????? pyml_interp ??????????????????????????????
            Python ??? QML ??????.
        """
        
        def _recurse(subtree: Hint.SourceTree):
            for no, node in subtree.items():
                pyml_interp.main(node)
                # TODO
            
        prop_assigns = self._extract_property_assignments()
    
    def _extract_property_assignments(self):
        out = {}  # {parent_id: {property: (operator, raw_expression)}}
        
        pattern = re.compile(
            r'(_*[a-z]\w*) *(<==>|<=>|==|<=|=>|:=|::|:|=) *(.*)'
            # ^----------^  ^---------------------------^  ^--^
            #  property      operator                       expression
            #                ??????: operator ????????????????????????????????????????????????
        )
        
        pseudo_fields = (
            'children', 'attr', 'style',
        )
        
        def _recurse(tree: Hint.SourceTree):
            for node in tree.values():
                
                if node['field'] in pseudo_fields:
                    _recurse(node['children'])
                    continue
                
                for match in pattern.finditer(node['line_stripped']):
                    prop, oper, expr = \
                        match.group(1), match.group(2), match.group(3)
                    lk.loga('{:15}\t{:^5}\t{:<}'.format(prop, oper, expr))
                    #        ^A--^  ^B--^  ^C-^
                    #   A: ?????????, ?????? 15; B: ??????, ?????? 5; C: ?????????, ????????????
                    
                    if expr:
                        """
                        ??????????????????????????? (??????):
                            width: height + 10
                        ?????? pyml ????????????, ?????????????????????, ????????????????????????, ???
                        ???????????????????????????????????????:
                            width: height + 10
                                if height + 10 > 10:
                                    return 10
                                else:
                                    return height
                        """
                        assert bool(node['children']) is False
                    else:
                        """
                        ??????????????????????????? (??????):
                            width:
                                if height > 10:
                                    return 10
                                else:
                                    return height
                        ?????? prop = 'width', oper = ':', expr ??????????????? '', ???
                        ??????????????????????????????. ????????????????????????????????????.
                        """
                        
                        def _recurse_expr_block(tree: Hint.SourceTree):
                            nonlocal expr
                            for node in tree.values():
                                expr += node['line'] + '\n'
                                _recurse_expr_block(node['children'])
                        
                        _recurse_expr_block(node['children'])
                    
                    x = out.setdefault(node['context']['self'], {})
                    x[prop] = (oper, expr)
        
        _recurse(self._comp_block['children'])
        return out
