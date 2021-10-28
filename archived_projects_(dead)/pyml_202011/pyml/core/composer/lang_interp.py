"""
@Author  : likianta <likianta@foxmail.com>
@Module  : lang_interp.py
@Created : 2020-11-04
@Updated : 2020-11-05
@Version : 0.1.0
@Desc    : Language oriented interpreter.

    DELETE: This module is going to be removed.
    
    本模块用于将 pyml 语法转换为其他声明式 ui 的语法. 目前主要提供面向 qml 的转
    换. 例如:
    
    # pyml           | // qml
    on_completed ::  | Component.onCompleted {
        pass         |     // pass
                     | }
"""
import re
from pyml.core._typing_hints import InterpreterHint as Hint


class BaseInterpreter:
    code: list
    ids: Hint.IDs
    info: dict
    node: Hint.SourceNode
    source_chain: Hint.SourceChain
    source_map: Hint.SourceMap
    
    def __init__(self, ids, source_map, source_chain):
        self.ids = ids
        self.source_map = source_map
        self.source_chain = source_chain
        self.code = []
        self.info = {}
        
    def main(self, node: Hint.SourceNode) -> dict:
        raise NotImplementedError


# noinspection PyMethodMayBeStatic
class PymlInterpreter(BaseInterpreter):
    
    def main(self, node):
        """
        
        :param node:
        :return: {
                'type': str,
                key: value,
                ...
                    -> key: based on which 'type' is
                    -> value: <str, list, dict>
            }
        """
        # self.node = node
        if node['node_type'] == 'comp_def':
            return self._dissolve_comp_def(node)
        elif node['node_type'] == 'pseudo_field':
            return {}
        elif node['node_type'] == 'comp_instance':
            return self._dissolve_comp_instance(node)
        elif node['node_type'] == 'on_signal':
            return self._dissolve_on_signal(node)
        elif node['node_type'] == 'prop_assigns':
            pass

    def _dissolve_prop_assigns(self, node):
        pattern = re.compile(
            r'(_*[a-z][.\w]*) *(<==>|<=>|==|<=|=>|:=|::|:|=) *(.*)'
            # ^-------------^  ^---------------------------^  ^--^
            #  property         operator                       expression
            #                   注意: operator 的匹配符号的顺序必须是从长到短排
        )
        match = pattern.search(node['line_stripped'])
        prop, oper, expr = \
            match.group(1), match.group(2), match.group(3)
        
        # analyse expression
        
        
        return {
            'type': 'prop_assign',
            'property': prop,
            'operator': oper,
            'expression': '',
            'ids': {
            
            }
        }

    def _dissolve_on_signal(self, node):
        pattern = re.compile(r'on_([^_]+)')
        signal = pattern.search(node['line_stripped']).group(1)
        return {
            'type': 'on_signal',
            'signal': signal,
            'passive_voice': signal.endswith('ed')
        }
        
    def _dissolve_comp_instance(self, node):
        pattern = re.compile(r'\w+')
        name = pattern.match(node['line_stripped']).group()
        return {
            'type': 'comp_instance',
            'comp_name': name
        }

    def _dissolve_comp_def(self, node):
        """
        E.g.
            IN: comp Window: @win
            OT: {
                    'type': 'comp_def',
                    'parent_comp_name': 'Window',
                    'self_comp_name': 'Window',
                    'id': 'win', ...
                }
        """
        pattern = re.compile(r'comp +(\w+)\((\w+)\):|comp +(\w+):')
        a, b, c = pattern.search(node['line_stripped'])
        """
            'comp MyWindow(Window):' -> a, b, c = 'MyWindow', 'Window', None
            'comp Window:'           -> a, b, c = None, None, 'Window'
        """
        return {
            'type': 'comp_def',
            'parent_comp_name': a or c,
            'self_comp_name': b or c,
        }


class PythonInterpreter(BaseInterpreter):
    pass


class QmlInterpreter(BaseInterpreter):
    prop: str
    oper: str
    expr: str
    
    def __init__(self, ids, source_map, source_chain):
        super().__init__(ids, source_map, source_chain)

    def main(self, prop: str, oper: str, expr: str, **kwargs):
        self.prop, self.oper, self.expr = prop, oper, expr
        
        if prop.startswith('on_'):
            self._convert_onprop(
                kwargs['pymethod'],
                kwargs.get('args', [])
            )
            
    def _convert_onprop(self, pymethod, args):
        s = self.prop.split('_')
        p = s[0] + ''.join(map(lambda x: x.title(), s[1:]))
        if not p.endswith('ed'):
            p += 'Changed'
        p += ': '
        self.prop = p
        
        assert self.oper == '::'
        self.oper = '''{{ return PyML.call("{0}", {1}) }}'''.format(
            pymethod, {
                0: '',
                1: args[0],
            }.get(len(args), '[' + ','.join(args) + ']')
        )
