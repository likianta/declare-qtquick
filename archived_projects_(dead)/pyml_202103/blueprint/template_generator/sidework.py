from lk_logger import lk
from lk_utils.read_and_write import loads, dumps


def static_qml_basic_types(file_i, file_o):
    """ 统计 qml 的基本类型有哪些.
    
    Args:
        file_i: 'blueprint/resources/no5_all_qml_props.json'
            structure: {
                module: {
                    qmltype: {
                        'parent': ...,
                        'props': {prop: type, ...}
                                        ^--^ 我们统计的是这个.
                    }, ...
                }, ...
            }
        file_o: *.txt or empty str. the empty string means 'donot dump to file,
            just print it on the console'.
            structure: [type, ...]. 一个去重后的列表, 按照字母表顺序排列.
    """
    data_r = loads(file_i)
    data_w = set()
    
    for v1 in data_r.values():
        for v2 in v1.values():
            for v3 in v2['props'].values():
                type_ = v3
                data_w.add(type_)
                
    data_w = sorted(data_w)
    if file_o == '':
        lk.logp(data_w)
    else:
        dumps(data_w, file_o)


if __name__ == '__main__':
    static_qml_basic_types(
        '../resources/no5_all_qml_props.json', ''
    )
