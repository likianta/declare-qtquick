from secrets import token_hex
from textwrap import dedent
from textwrap import indent

from .control import id_mgr
from .properties.base import PropertyGroup
from .pyside import pyside
from .typehint import *


def build_component(comp: TComponent, level=0) -> str:
    def _loop(comp: TComponent, level: int):
        # assert level % 4 == 0
        return indent(
            dedent('''
                {widget_name} {{
                    id: {qid}
                    
                    {properties}
                    
                    {connections}
                    
                    {children}
                }}
            ''').rstrip().format(
                widget_name=comp.name,
                qid=comp.qid,
                properties=indent(
                    '\n'.join(build_properties(comp.properties)),
                    '    '
                ).lstrip() or '// NO_PROPERTY_DEFINED',
                connections=indent(
                    '\n'.join(build_connections(comp.properties)),
                    '    '
                ).lstrip() or '// NO_CONNECTION_DEFINED',
                children='\n\n'.join(
                    _loop(x, level + 4).lstrip()
                    for x in id_mgr.get_children(comp.qid)
                ) or '// NO_CHILDREN_DEFINED',
            ),
            ' ' * level
        )
    
    return _loop(comp, level=level)


def build_properties(props: TProperties, group_name=''):
    for name, prop in props.items():
        # note prop type is Union[TProperty, TPropertyGroup], we should check
        # its type first.
        if isinstance(prop, PropertyGroup):
            yield from build_properties(prop.properties, prop.name)
        elif prop.value is None:
            continue
        else:
            # yield name, prop.value
            if group_name:
                yield '{}.{}: {}'.format(
                    group_name, _convert_name_case(name), prop.adapt()
                )
            else:
                yield '{}: {}'.format(_convert_name_case(name), prop.adapt())


def build_connections(props: TProperties):
    for name, prop in props.items():
        if isinstance(prop, PropertyGroup):
            yield from build_connections(prop.properties)
        else:
            for notifier_name, func in prop.bound:
                if func is None:
                    yield '{}: {}'.format(
                        _convert_name_case(name),
                        _convert_name_case(notifier_name)
                    )
                else:
                    # assert isinstance(notifier_name, list)
                    pyside.register(
                        lambda *args: func(),
                        name=(random_id := token_hex(8))
                    )
                    yield '{}: pyside.call("{}", {})'.format(
                        _convert_name_case(name),
                        random_id,
                        list(map(_convert_name_case, notifier_name))
                    )


def _convert_name_case(snake_case: str):
    """ snake_case to camelCase. For example, 'hello_world' -> 'helloWorld'. """
    if '.' in snake_case:
        # return '.'.join(convert_name_case(s) for s in snake_case.split('.'))
        return '.'.join(map(_convert_name_case, snake_case.split('.')))
    
    if '_' not in snake_case:
        camel_case = snake_case
    else:
        segs = snake_case.split('_')
        camel_case = segs[0] + ''.join(x.title() for x in segs[1:])
    
    return camel_case
