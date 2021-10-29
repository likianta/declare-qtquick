from collections import defaultdict
from os.path import exists

from bs4 import BeautifulSoup
from lk_logger import lk
from lk_utils import dumps
from lk_utils import loads


def main(file_i, file_o, qtdoc_dir: str):
    """
    Args:
        file_i: '~/resources/no4_all_qml_types.json'. see `no2_all_qml_types.py`
        file_o: '~/resources/no5_all_qml_widgets.json'
        qtdoc_dir: 请传入您的 Qt 安装程序的 Docs 目录. 例如: 'D:/Programs/Qt
            /Docs/Qt-5.14.2' (该路径须确实存在)
    """
    reader = loads(file_i)  # type: dict
    writer = defaultdict(lambda: defaultdict(lambda: {
        'parent': '',
        'props' : {},
    }))
    
    assert exists(qtdoc_dir), (
        'The Qt Docs directory doesn\'t exist!', qtdoc_dir
    )
    
    for module, qmltype, file_i in _get_files(reader, qtdoc_dir):
        lk.logax(qmltype)
        
        if not exists(file_i):
            lk.logt('[I3924]', 'file not found', qmltype)
            continue
        
        try:
            parent, props = _parse_file(file_i)
        except Exception as e:
            lk.logp(module, qmltype, file_i,
                    title='error happened when parsing file')
            raise e
        
        writer[module][qmltype]['parent'] = parent
        writer[module][qmltype]['props'].update(props)
    
    dumps(writer, file_o)


def _parse_file(file):
    soup = BeautifulSoup(loads(file), 'html.parser')
    # 下面以 '{qtdoc_dir}/qtquick/qml-qtquick-rectangle.html' 为例分析 (请在
    # 浏览器中查看此 html, 打开开发者工具.)
    
    parent = ''
    props = {}
    
    try:  # get parent
        '''
        <table class="alignedsummary">
            <tr>...</tr>
            # 目标可能在第二个 tr, 也可能在第三个 tr. 例如 Rectangle 和
            # Button 的详情页. 有没有其他情况不太清楚 (没有做相关测试). 安全
            # 起见, 请逐个 tr 进行检查.
            <tr>
                <td class="memItemLeft rightAlign topAlign"> Inherits:</td>
                <td class="memItemRight bottomAlign">
                    <p>
                        <a href="qml-qtquick-item.html">Item</a>
                    </p>
                </td>
            </tr>
            ...
        </table>
        '''
        e = soup.find('table', 'alignedsummary')
        # noinspection PyTypeChecker
        for tr in e.find_all('tr'):
            if tr.td.text.strip() == 'Inherits:':
                td = tr.find('td', 'memItemRight bottomAlign')
                parent = td.text.strip()
                break
    except AttributeError:
        pass
    
    try:  # props
        e = soup.find(id='properties')
        e = e.find_next_sibling('ul')
        # noinspection PyTypeChecker
        for li in e.find_all('li'):
            '''
            <li class="fn">
                ...
                    <a href=...>border</a>  # this is `prop`
                    # border 的值的类型是空, 我们用 'group' 替代
                ...
                <ul>
                    <li class="fn">
                        ...
                            <a href=...>border.color</a>  # this is `prop`
                        ...
                        " : color"  # this is `type`
                    </li>
                    ...
                </ul>
            </li>

            References:
                https://blog.csdn.net/Kwoky/article/details/82890689
            '''
            # `p` and `t` means 'property' and 'type'
            p = li.a.text
            try:
                t = li.contents[-1].strip(' :').strip() or 'group'
                #   .strip(' :').strip()
                #       后一个 strip 是为了去除未知的空白符, 比如换行符或者其他
                #       看不见的字符 (后者通常是 html 数据不规范引起的).
                #   or 'group'
                #       对于 border, font, anchors 这种 "属性组", 它们的
                #       `li.contents[-1]` 是一个 '\n'. 也就是说经过 strip 后就变
                #       成了空字符串. 我们会用 'group' 来代替.
            except TypeError:
                '''
                该错误在 Qt 6 中首次出现.
                通常来说, `li.contents` 只会有两种形态:
                    1. [<a>...</a>, str]
                    2. [<a>...</a>, <ul><li>...</li><li>...</li>...</ul>, '\n']
                我们在 try 块中处理的就是以上两种情况.
                第三种情况出现在: qt 添加了拟案属性, 其标签树如下所示:
                    <li>
                        <a>...</a>
                        '...'  # 这里是原本要获取的属性类型
                        <code> (preliminary)</code>  # 新增加了一个 code 标签
                    </li>
                所以我们改用 `li.contents[-2]` 来获得目标.
                '''
                assert len(li.contents) == 3
                assert li.contents[-1].text == ' (preliminary)'
                t = li.contents[-2].strip(' :').strip()
                lk.logt('[I5118]', 'found a preliminary type', parent, t, file)
            props[p] = t
    except AttributeError:
        pass
    except Exception as e:
        breakpoint()
        raise e
    
    return parent, props


def _get_files(data: dict, dir_i: str):
    for module_group, node1 in data.items():
        for module, node2 in node1.items():
            for qmltype, relpath in node2.items():
                yield module, qmltype, dir_i + '/' + relpath


if __name__ == '__main__':
    main('../resources/no4_all_qml_types.json',
         '../resources/no5_all_qml_widgets.json',
         'E:/programs/qt/qt6/Docs/Qt-6.1.3')
