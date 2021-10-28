"""
Requirements:
    如需运行本模块, 请先安装 Qt 5.0+ (推荐 5.15) 完整版.
    本模块所用到的离线文件读取自:
        "{YourQtProgram}/Docs/Qt-{version}/qtdoc/qmltypes.html".
"""
import re
from collections import defaultdict

from bs4 import BeautifulSoup
from lk_logger import lk
from lk_utils import read_and_write


def main(file_i, file_o):
    """
    
    Args:
        file_i: '~/blueprint/resources/no2_all_qml_types.html'. 该文件被我事先从
            "{YourQtProgram}/Docs/Qt-{version}/qtdoc/qmltypes.html" 拷贝过来.
        file_o: 生成文件. "~/blueprint/resources/no3_all_qml_types.json"
            {module_group: {module: {type_name: path}, ...}, ...}
            #   {模组: {模块: {类型: 路径}}}
            e.g. {
                'qtquick': {
                    'qtquick': {
                        'Rectangle': 'qtquick/qml-qtquick-rectangle.html',
                        'Text': 'qtquick/qml-qtquick-text.html',
                        ...
                    },
                    'qtquick-window': {
                        'Window': 'qtquick/qml-qtquick-window-window.html',
                        ...
                    },
                    ...
                },
                ...
            }
    
    思路:
        1. 我们安装了 Qt 主程序以后, 在软件安装目录下的 'Docs/Qt-{version}' 中有
           它的 API 文档
        2. 其中 "~/Docs/Qt-{version}/qtdoc/qmltypes.html" 列出了全部的 qml types
        3. 我们对 "qmltypes.html" 用 BeautifulSoup 解析, 从中获取每个 qml types
           和它的链接, 最终我们将得到这些信息: 模组, 模块, 类型, 路径等
        4. 将这些信息保存到本项目下的 "~/resources/qmltypes.json" 文件中
    """
    soup = BeautifulSoup(read_and_write.read_file(file_i), 'html.parser')
    
    # https://www.itranslater.com/qa/details/2325827141935563776
    data = defaultdict(lambda: defaultdict(dict))
    #   {module_group: {module: {type_name: filename, ...}, ...}, ...}
    
    container = soup.find('div', 'flowListDiv')
    for e in container.find_all('dd'):
        link = e.a['href']  # type: str
        #   e.g. "../qtdatavisualization/qml-qtdatavisualization-
        #         abstract3dseries.html"
        
        match = re.search(r'\.\./(\w+)/([-\w]+)\.html', link)
        #                  |     ^-1-^ ^--2---^      |
        #                  ^-------- group(0) -------^
        #   match.group(0): '../qtdatavisualization/qml-qtdatavisualization
        #       -abstract3dseries.html'
        #   match.group(1): 'qtdatavisualization'
        #   match.group(2): 'qml-qtdatavisualization-abstract3dseries'
        assert match, e
        
        module_group = match.group(1)
        module = match.group(2)
        # see `blueprint/qml_modules_indexing/no1_all_qml_modules.py:comments
        # :针对 QtQuick Controls 的处理`
        if module_group == 'qtquickcontrols1':
            continue
        if 'qtquick-controls2' in module:
            #   e.g. 'qml-qtquick-controls2-label'
            module = module.replace('controls2', 'controls')
        
        path = match.group(0).lstrip('../')
        #   -> 'qtdatavisualization/qml-qtdatavisualization-abstract3dseries
        #   .html'
        module_group = _correct_module_lettercase(module_group)
        #   'qtdatavisualization' -> 'QtDataVisualization'
        module = _correct_module_lettercase('-'.join(module.split('-')[1:-1]))
        #   eg1: 'qml-qtdatavisualization-abstract3dseries' -> ['qml',
        #   'qtdatavisualization', 'abstract3dseries'] -> [
        #   'qtdatavisualization'] -> 'qtdatavisualization'
        #   -> 'QtDataVisualization'
        #   eg2: 'qml-qt3d-input-abstractactioninput' -> ['qml', 'qt3d',
        #   'input', 'abstractactioninput'] -> ['qt3d', 'input',
        #   'abstractactioninput'] -> 'qt3d-input' -> 'Qt3D.Input'
        #   注: 为什么要舍去末尾的元素? 因为末尾的那个是 `type_name`, 不是
        #   `module`. 接下来我们会抽取 `type_name`.
        type_name = e.text.split(':', 1)[0]
        #   注意我们不使用 `correct_module_lettercase(match.group(2).split('-')
        #   [-1])`, 是因为 `correct_module_lettercase` 的词库范围比较小, 仅对
        #   `module_group` 和 `module` 做了覆盖, 不能保证对 `type_name` 的处理正
        #   确; 而 `soup` 是可以比较轻松地通过 tag 提取到它的, 所以通过 html 元
        #   素获取.
        #   e.g. 'RadioButton: QtQuickControls' -> 'RadioButton'
        
        lk.loga(module_group, module, type_name)
        data[module_group][module][type_name] = path
    
    read_and_write.dumps(data, file_o)


# ------------------------------------------------------------------------------

qml_modules = read_and_write.loads('../resources/no2_all_qml_modules.json')
qml_modules = qml_modules['module_group'] | qml_modules['module']  # type: dict
qml_modules.update({  # 扩充
    ''                        : '',
    'qtquick-controls-private': 'QtQuick.Controls.Private',
    'mediaplayer-qml'         : 'MediaPlayer.Qml',
    #   注: 这个其实是不存在的, 只是为了不报错所以加上去
})


def _correct_module_lettercase(module: str):
    """ 修正模块的大小写.
    
    示例:
        'qtquick-window' -> 'QtQuick.Window'
        'qtgraphicaleffects' -> 'QtGraphicalEffects
    
    注意: 存在一些特殊情况:
        'qt-labs-animation' -> 'Qt.labs.animation'
        
    思路:
        1. 我们需要把模块的名字按照词来拆分:
            'qtgraphicaleffects' -> ['qt', 'graphical', 'effects']
        2. 然后将每个词的首字母大写:
            ['Qt', 'Graphical', 'Effects']
        3. 再拼接回去:
            'QtGraphicalEffects'
            
            (对于一些特殊情况, 比如 Qt.labs 要求全小写, 则需要进一步判断和调整.)
    
    单词拆分该怎么实现?
        方案 1: 引入一个第三方库来切词. 缺点是词库体积大, 有些 Qt 自定义词不在里
        面 (自己也不一定找全), 甚至可能会切分存在歧义导致不准确. 成本高且效果差.
        方案 2: 从 "{YourQtProgram}/Docs/Qt-{version}/qtdoc/modules-qml.html" 页
        面, 把里面提到的所有单词都提取出来, 然后组成一个列表. 这里的单词应该完整
        覆盖了模块的名字中的所有情况. 然后我们把列表转换成一个前缀树, 就可以以一
        种简单且准确的方式去分词了.
        目前采用的是方案 2. 方案 2 需要提前准备这样一个单词列表, 见:
            `blueprint/qml_indexing/no1_all_qml_modules.py`.
    """
    global qml_modules
    return qml_modules[module]


if __name__ == '__main__':
    main('../resources/no3_all_qml_types.html',
         '../resources/no4_all_qml_types.json')
