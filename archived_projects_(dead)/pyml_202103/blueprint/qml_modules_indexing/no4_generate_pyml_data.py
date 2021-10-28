import re
from collections import defaultdict

from lk_utils import read_and_write


def main(file_i, file_o):
    """
    Args:
        file_i: '~/resources/no4_all_qml_props.json'. see `no3_all_qml_props.py`
        file_o: '~/resources/no5_pyml_namespaces.json'
    """
    data_i = read_and_write.loads(file_i)  # type: dict
    data_o = defaultdict(lambda: defaultdict(dict))
    '''
        {
            package: {
                widget: {
                    'parent': str,
                    'props': {prop: type, ...}
                }, ...
            }, ...
        }
        e.g. {
            'pyml.qtquick': {
                'Rectangle': {
                    'parent': 'Item',
                    'props': {
                        'border': 'group',
                        'border.color': 'color',
                        ...
                    }
                }, ...
            }, ...
        }
    '''
    
    for module, v1 in data_i.items():
        for type_, v2 in v1.items():
            package = f'pyml.{module.lower()}'
            widget = type_
            
            data_o[package][widget] = {
                'parent': v2['parent'],
                'props' : dict(zip(
                    map(_camel_2_snake_case, v2['props'].keys()),
                    v2['props'].values()
                ))
            }
    
    read_and_write.dumps(data_o, file_o)


def _camel_2_snake_case(name: str):
    """ 驼峰转下划线式命名.
    
    References:
        https://www.yuque.com/tianyunperfect/ygzsw4/av4s8q
    """
    p = re.compile(r'([A-Z]+)')
    name = p.sub(r'_\1', name).lower().lstrip('_')
    return name


if __name__ == '__main__':
    main(
        '../resources/no5_all_qml_props.json',
        '../resources/no6_pyml_namespaces.json'
    )
