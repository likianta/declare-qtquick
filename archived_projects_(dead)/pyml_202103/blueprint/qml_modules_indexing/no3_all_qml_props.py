from collections import defaultdict
from os.path import exists

from bs4 import BeautifulSoup
from lk_utils import read_and_write
from lk_utils.lk_logger import lk
from lk_utils.read_and_write import loads


def main(file_i, file_o, qtdoc_dir: str):
    """
    Args:
        file_i: '~/resources/no4_all_qml_types.json'. see `no2_all_qml_types.py`
        file_o: '~/resources/no5_all_qml_props.json'
            {
                module: {
                    qmltype: {
                        'parent': parent_qmltype,
                        'props': {prop: type, ...}
                    }, ...
                }, ...
            }
        qtdoc_dir: 请传入您的 Qt 安装程序的 Docs 目录. 例如: 'D:/Programs/Qt
            /Docs/Qt-5.14.2' (该路径须确实存在)
    """
    reader = read_and_write.loads(file_i)  # type: dict
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
        
        soup = BeautifulSoup(loads(file_i), 'html.parser')
        #   以 '{qtdoc_dir}/qtquick/qml-qtquick-rectangle.html' 为例分析 (请在
        #   浏览器中查看此 html, 打开开发者工具.
        
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
            parent = ''
            e = soup.find('table', 'alignedsummary')
            for tr in e.find_all('tr'):
                if tr.td.text.strip() == 'Inherits:':
                    td = tr.find('td', 'memItemRight bottomAlign')
                    parent = td.text.strip()
                    break
        except AttributeError:
            parent = ''
        
        try:  # props
            e = soup.find(id='properties')
            e = e.find_next_sibling('ul')
            props = {}
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
                t = li.contents[-1].strip(' :').strip()
                #   后一个 strip 是为了去除未知的空白符, 比如换行符或者其他看不
                #   见的字符 (后者通常是 html 数据不规范引起的)
                assert isinstance(t, str)
                if t == '': t = 'group'
                props[p] = t
        except AttributeError:
            props = {}
        
        writer[module][qmltype]['parent'] = parent
        writer[module][qmltype]['props'].update(props)
        
        del soup
    
    read_and_write.dumps(writer, file_o)


def _get_files(data: dict, dir_i: str):
    for module_group, node1 in data.items():
        for module, node2 in node1.items():
            for qmltype, relpath in node2.items():
                yield module, qmltype, dir_i + '/' + relpath


if __name__ == '__main__':
    main('../resources/no4_all_qml_types.json',
         '../resources/no5_all_qml_props.json',
         'D:/programs/qt/qt_5.14.2/Docs/Qt-5.14.2')
    lk.print_important_msg()
