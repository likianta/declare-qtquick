"""
@Author   : likianta (likianta@foxmail.com)
@FileName : composer.py
@Version  : 0.2.0
@Created  : 2020-11-04
@Updated  : 2020-11-09
@Desc     : 将 pyml 源码编译为 .py & .qml 代码.
    
    注: 请根据 'docs/PyML 实现流程.mm' 进行.

"""
import re

from pyml_rc.declare_pyml.core.composer.ast import SourceAst
from pyml_rc.declare_pyml.core.composer.pyml_interp import PymlInterpreter
from pyml_rc.declare_pyml.core.composer.composer import ComponentComposer, PlainComposer
from pyml_rc.declare_pyml.core._typing_hints import InterpreterHint as Hint
from lk_utils.read_and_write import read_file


def main(pyml_file: str):
    compile_pyml_code(read_file(pyml_file))


def compile_pyml_code(pyml_code: str):
    """
    
    编译过程:
        1. 将 pyml 源码优化为更简洁的格式
        2. 将 pyml 优化后的源码转换为抽象语法树
        3. 根据语法树解读 pyml 功能块
            1. 解析全局引用关系
            2. 解析组件树
        4. 将 pyml 的功能描述交由 python 和 qml 处理器实现

    :param pyml_code: read from .pyml file.
    :return:
    """
    src = optimize_source_code(pyml_code)  # src: source code (abbr)
    ast = SourceAst(src)
    interp = PymlInterpreter(
        ast.source_tree, ast.source_map, ast.source_chain
    )


def optimize_source_code(source_code: str) -> str:
    """ 折叠 "代码块". 将块注释, 行注释, 字符串, 括号等替换为掩码, 以便于后续的
        代码分析.
        
    本方法的目的是, 将原 pyml 代码中的所有可消除的换行符消除. 例如:
        indent | code
             0 | def calc(
             4 |     x, y
             0 | ):
             4 |     a = (
             8 |         x + y
             4 |     ) * 2
    变为:
        indent | code
             0 | def calc(x, y):
             4 |     a = (x + y) * 2
             
    这样, 得到的处理后的代码是严格按照缩进来表示嵌套层次的代码, 有利于后面根据缩
    进量来快速构建代码树.

    :ref: 'docs/掩码处理效果示例.md'
    :return:
    """
    from pyml_rc.declare_pyml.core.composer.mask import Mask
    mask = Mask(source_code)
    
    # 1. 将末尾以 \\ 换行的内容拼接回来.
    #    例如 'a = "xy" \\\n    "z"' -> 'a = "xy" {mask}    "z"'.
    mask.main(re.compile(r'\\ *\n'), cmd='strip_linebreaks')
    # 2. 字符串掩码
    #    示意图: '.assets/snipaste 2020-11-01 171109.png'
    with mask.temp_mask(re.compile(r'(?<!\\)"""'), '"""'), \
         mask.temp_mask(re.compile(r"(?<!\\)'''"), "'''"):
        mask.main(re.compile(r'([\'"]).*?(?<!\\)\1'), cmd='strip_linebreaks')
    # 3. 块注释
    mask.main(re.compile(r'^ *("""|\'\'\')(?:.|\n)*?(?<!\\)\1'),
              cmd='abandon')
    #    非块注释, 长字符串
    mask.main(re.compile(r'("""|\'\'\')(?:.|\n)*?(?<!\\)\1'),
              cmd='strip_linebreaks')
    # 4. 行注释
    mask.main(re.compile(r'#.*'), cmd='abandon')
    # 5. 大中小括号
    mask.main(re.compile(r'\((?:[^(]|\n)*?\)'),
              cmd='circle+strip_linebreaks')
    mask.main(re.compile(r'\[(?:[^\[]|\n)*?]'),
              cmd='circle+strip_linebreaks')
    mask.main(re.compile(r'{(?!mask_holder_\d+})(?:[^{]|\n)*?}'),
              cmd='circle+strip_linebreaks')
    #    到这一步, 会出现 `{A, {mask1}, {mask2}, B}` 的情况, 我们需要把最外边的
    #                      ^----------------------^
    #    花括号也折叠.
    mask.main(re.compile(
        r'{(?!mask_holder_\d+})(?:{mask_holder_\d+}|[^}])*?}'
        # ||  ^A-------------^||  ^B--------------^ ^C-^|  |
        # |^D-----------------^^E-----------------------^  |
        # ^F-----------------------------------------------^
        #   A: 当左花括号右边不是 `mask_holder_\d+}` 时继续
        #   B: 当匹配到 `{mask_holder_\d+}` 时继续
        #   C: 或者当匹配到非 `}` 时继续 (包括: 遇到换行符, 也继续)
        #   F: 非贪婪地匹配, 直到遇到了不符合 B, C 情形的右花括号结束
    ), cmd='strip_linebreaks')
    
    return mask.plain_text


def _compose_plain_code(tree: Hint.SourceTree):  # DEL
    composer = PlainComposer()
    
    def _recurse(subtree: Hint.SourceTree):
        for no, node in subtree.items():
            composer.submit(node)
            _recurse(subtree['children'])
    
    _recurse(tree)
    return composer


def _compose_component_block(tree: Hint.SourceTree):  # DEL
    for no, node in tree.items():
        assert node['level'] == 0
        if node['line_stripped'].startswith('comp '):
            block = node
        else:
            continue
            
        composer = ComponentComposer(block)
