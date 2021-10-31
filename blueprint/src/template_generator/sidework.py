"""
DELETE (2021-10-31)
"""
from collections import defaultdict

from lk_utils import dumps
from lk_utils import loads


def stat_qml_basic_types(file_i, file_o):
    """ 统计 qml 的基本类型有哪些.
    
    Args:
        file_i: 'blueprint/resources/no5_all_qml_widgets.json'
            structure: {
                module: {
                    qmltype: {
                        'parent': ...,
                        'props': {prop: type, ...}
                    }, ...              ^--^ 我们统计的是这个.
                }, ...
            }
        file_o: Optional[str *.txt].
            None means 'do not dump to file, just print it in the console'.
            structure: [type, ...]. 一个去重后的列表, 按照字母表顺序排列.
            
    Outputs:
        data_w: {type: [(module, qmltype, prop), ...], ...}
    """
    data_r = loads(file_i)
    data_w = defaultdict(set)  # type: dict[str, set[tuple[str, str, str]]]
    
    for k1, v1 in data_r.items():
        for k2, v2 in v1.items():
            for k3, v3 in v2['props'].items():
                # k1: module; k2: qmltype; k3: prop; v3: type
                data_w[v3].add((k1, k2, k3))
    
    [print(i, k) for i, k in enumerate(sorted(data_w.keys()), 1)]
    
    if file_o:
        data_w = {k: sorted(data_w[k]) for k in sorted(data_w.keys())}
        dumps(data_w, file_o, pretty_dump=True)


if __name__ == '__main__':
    stat_qml_basic_types(
        '../../resources/qtdoc_compiled/3_all_qml_widgets.json',
        '../../tests/data1.json'
    )
