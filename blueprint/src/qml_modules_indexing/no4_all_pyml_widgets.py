from collections import defaultdict

from lk_utils import read_and_write

from blueprint.src.common import camel_2_snake_case
from blueprint.src.typehint import *


def main(file_i, file_o):
    data_i = read_and_write.loads(file_i)  # type: TJson3Data
    data_o = defaultdict(lambda: defaultdict(dict))  # type: TJson3Data
    
    for module, v1 in data_i.items():
        for type_, v2 in v1.items():
            package = camel_2_snake_case(module)
            #   e.g. 'qtquick.Controls' -> 'qtquick.controls'
            widget = type_
            #   e.g. 'MouseArea'
            
            data_o[package][widget] = {
                'parent': v2['parent'],
                'props' : dict(zip(
                    map(camel_2_snake_case, v2['props'].keys()),
                    v2['props'].values()
                ))
            }
    
    read_and_write.dumps(data_o, file_o)


if __name__ == '__main__':
    from blueprint.src import io
    
    main(*io.no4)
