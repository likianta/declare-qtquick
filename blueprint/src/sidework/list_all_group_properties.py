from collections import defaultdict

from lk_logger import lk
from lk_utils import dumps
from lk_utils import loads

from blueprint.src.common import camel_2_snake_case
from blueprint.src import io
from blueprint.src.typehint import *


def main(**kwargs):
    file_i = io.json_3
    data_r = loads(file_i)  # type: TJson3Data
    
    group_names = set()
    group_attrs = defaultdict(dict)
    
    for v0 in data_r.values():
        for v1 in v0.values():
            props = v1['props']  # type: TProps
            
            for k, v in props.items():
                if v == 'group':
                    group_names.add(k)
                elif '.' in k:
                    name, attr = k.split('.', 1)
                    group_attrs[name][attr] = v
    
    if kwargs.get('strip_unrecognized_properties', True):
        # filter out the group names that are not recognized by group_names.
        # for example 'list<qt.cursorShape>' -> 'list<qt' was found in group_attrs,
        # but it is not in group_names. we need to pop it from group_attrs.
        keys_to_pop = []
        for k, v in group_attrs.items():
            if k not in group_names:
                lk.logp(k, v, title='key to pop')
                keys_to_pop.append(k)
        for k in keys_to_pop:
            group_attrs.pop(k)

    # sort dict
    group_attrs, temp = defaultdict(dict), group_attrs
    for k0 in sorted(temp):
        for k1 in sorted(temp[k0]):
            if kwargs.get('use_snake_case', True):
                new_k0 = camel_2_snake_case(k0)
                new_k1 = camel_2_snake_case(k1)
            else:
                new_k0 = k0
                new_k1 = k1
            group_attrs[new_k0][new_k1] = temp[k0][k1]

    # dump to file
    file_o = './result.json'
    dumps(group_attrs, file_o, pretty_dump=True)


if __name__ == '__main__':
    main(
        strip_unrecognized_properties=False,
        use_snake_case=True,
    )
