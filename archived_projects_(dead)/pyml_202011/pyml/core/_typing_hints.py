"""
@Author  : likianta <likianta@foxmail.com>
@Module  : _typing_hints.py
@Created : 2020-11-02
@Updated : 2020-11-10
@Version : 0.4.0
@Desc    :
"""
from typing import *


class RegexHint:
    import re
    RegexPattern = re.Pattern
    RegexMatch = re.Match


class MaskHint(RegexHint):
    PymlText = str
    MaskHolder = Dict[str, PymlText]


class TokenHint:  # comes from `Python39/Lib/token.py`
    ENDMARKER = 0
    NAME = 1
    NUMBER = 2
    STRING = 3
    NEWLINE = 4
    INDENT = 5
    DEDENT = 6
    LPAR = 7
    RPAR = 8
    LSQB = 9
    RSQB = 10
    COLON = 11
    COMMA = 12
    SEMI = 13
    PLUS = 14
    MINUS = 15
    STAR = 16
    SLASH = 17
    VBAR = 18
    AMPER = 19
    LESS = 20
    GREATER = 21
    EQUAL = 22
    DOT = 23
    PERCENT = 24
    LBRACE = 25
    RBRACE = 26
    EQEQUAL = 27
    NOTEQUAL = 28
    LESSEQUAL = 29
    GREATEREQUAL = 30
    TILDE = 31
    CIRCUMFLEX = 32
    LEFTSHIFT = 33
    RIGHTSHIFT = 34
    DOUBLESTAR = 35
    PLUSEQUAL = 36
    MINEQUAL = 37
    STAREQUAL = 38
    SLASHEQUAL = 39
    PERCENTEQUAL = 40
    AMPEREQUAL = 41
    VBAREQUAL = 42
    CIRCUMFLEXEQUAL = 43
    LEFTSHIFTEQUAL = 44
    RIGHTSHIFTEQUAL = 45
    DOUBLESTAREQUAL = 46
    DOUBLESLASH = 47
    DOUBLESLASHEQUAL = 48
    AT = 49
    ATEQUAL = 50
    RARROW = 51
    ELLIPSIS = 52
    COLONEQUAL = 53
    OP = 54
    AWAIT = 55
    ASYNC = 56
    TYPE_IGNORE = 57
    TYPE_COMMENT = 58
    ERRORTOKEN = 59
    COMMENT = 60
    NL = 61
    ENCODING = 62
    N_TOKENS = 63
    NT_OFFSET = 256


class AstHint(TokenHint):
    LineNo = str  # 之所以用 str, 是为了让 Python dict 在输出或读取 json 文件时
    #   键的类型一致 (用 int 作为键的话, json 文件中会转换成 str).
    """ -> 'line{num}' -> num: 从 0 开始数 """
    SourceNode = Dict[str, Union[str, int, Dict[str, Any]]]
    """ -> {
            'lineno': str 'line{num}',
            'line': str,  # 原始的行内容. 便于还原输出
            'line_stripped': str,  # 去除了每行的前面的空格. 便于分析结构
            'level': <int 0, 4, 8, ...>,
            'parent': str lineno,
            'children': {
                lineno: Node,
                ...
            },
            ...
        }
    """
    SourceTree = Dict[LineNo, SourceNode]
    """ -> {LineNo: Node, ...} """
    SourceMap = Dict[LineNo, SourceNode]
    #   SourceTree 是嵌套的, SourceMap 是单层的.
    SourceChain = List[List[SourceNode]]
    """ -> [[Node, ...], ...] """


class RefHint:
    CompName = str
    """ -> <'Text', 'Item', 'Rectangle', ...> """
    CompProps = Dict[str, Union[str, List[str]]]
    """ -> e.g. {
            'module': 'pyml.qtquick',
            'name': 'Text',
            'inherits': 'Item',
            'props': list the_full_props
        }
    """
    CompNameSpace = Dict[CompName, Union[str, List[str]]]
    """ -> see 'pyml/data/pyml_import_namespaces.json'
        e.g. {
            'Text': {
                'import': 'pyml.qtquick',
                'inherits': 'Item',
                'props': [
                    'font.bold',
                    'font.family',
                    'text',
                    ...
                ]
            }
        }
    """
    PymlModule = str
    ModuleNameSpace = Dict[PymlModule, CompNameSpace]


class CompAstHint(AstHint, RefHint):
    CompId = str
    """ -> <'root', 'id1', 'id2', 'id3', ...>
        'root' is the only special id that indicates to the root comp node.
    """
    CompNode = Dict[str, Union[
        CompId, str, List[str],
        Dict[str, Union[CompId, List[CompId]]],
        Dict[CompId, dict],
    ]]
    """ -> {
            'id': CompId,
            'lineno': str,
            'props': [str, ...],
            'on_props': [str, ...],
            'context': {
                'root': CompId,
                'parent': CompId,
                'self': CompId,
                'children': [CompId, ...]
            },
            'children': {
                CompId: CompNode,
                ...
            }
        }
    """
    CompTree = Dict[CompId, CompNode]
    CompMap = Dict[CompId, CompNode]
    CompChain = List[List[CompNode]]


class InterpreterHint(RegexHint, CompAstHint):
    """ -> {'mask_node_{num}': str source_pyml_text_snippet, ...} """
    CompProp = Literal[
        'cascading_prop',
        'class_block',
        'comp_block',
        'func_block',
        'inner_class_block',
        'inner_def_block',
        'pseudo_prop',
        'top_module',
    ]
    Context = List[CompProp]
    NodeType = Literal[
        'comp_def',
        'comp_id',
        'comp_instance',
        'import',
        'pseudo_attr_prop',
        'pseudo_children_prop',
        'pseudo_style_prop',
        'raw_pycode',
    ]
    InterpretedData = Dict[CompAstHint.LineNo, Dict[str, Union[
        NodeType, str, int, dict
    ]]]
    """ -> {
            lineno: {
                'node_type': ''
                **Node,
            }
        }
    """
    
    IDs = Dict[str, CompAstHint.CompNode]
    """ -> {
            buitin_id: CompNode, auto_id: CompNode, custom_id: CompNode
                -> buitin_id: 'root'
                -> auto_id: 'id1', 'id2', 'id3', ...
                -> custom_id: based on the source pyml code, notice that its
                    first letter must be a lower case (additional '_' before
                    first letter is allowed)
        }
    """
    PropAssigns = Dict[str, Dict[str, Tuple[str, str]]]
    """ -> {comp_id: {prop: (operator, expression), ...}, ...} """
