from secrets import token_hex
from textwrap import dedent
from textwrap import indent

from .common import convert_name_case
from .control import id_mgr
from .properties.base import PropertyGroup
from .pyside import pyside
from .typehint import *


def build_component(comp: TComponent, level=0) -> str:
    # assert level % 4 == 0
    
    def _loop(comp: TComponent):
        return dedent('''
            {widget_name} {{
                id: {qid}
                objectName: "{qid}"
                
                {properties}
                
                {connections}
                
                {signals}
                
                {children}
            }}
        ''').strip().format(
            widget_name=comp.widget_name,
            qid=comp.qid,
            properties=indent(
                '\n'.join(sorted(build_properties(comp.properties))),
                '    '
            ).lstrip() or '// NO_PROPERTY_DEFINED',
            connections=indent(
                '\n'.join(sorted(build_connections(comp.properties))),
                '    '
            ).lstrip() or '// NO_CONNECTION_DEFINED',
            signals=indent(
                '\n'.join(sorted(build_signals(comp.signals))),
                '    '
            ).lstrip() or '// NO_SIGNAL_DEFINED',
            children=indent(
                '\n\n'.join(map(_loop, id_mgr.get_children(comp.qid))),
                '    '
            ).lstrip() or '// NO_CHILD_DEFINED',
        )
    
    out = indent(_loop(comp), ' ' * level)
    return out


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
                    group_name, convert_name_case(name), prop.adapt()
                )
            else:
                yield '{}: {}'.format(convert_name_case(name), prop.adapt())


def build_connections(props: TProperties):
    for name, prop in props.items():
        if isinstance(prop, PropertyGroup):
            yield from build_connections(prop.properties)
        else:
            for notifier_name, func in prop.bound:
                if func is None:
                    yield '{}: {}'.format(
                        convert_name_case(name),
                        convert_name_case(notifier_name)
                    )
                else:
                    # assert isinstance(notifier_name, list)
                    pyside.register(
                        lambda *args: func(),
                        name=(random_id := token_hex(8))
                    )
                    yield '{}: pyside.call("{}", {})'.format(
                        convert_name_case(name),
                        random_id,
                        list(map(convert_name_case, notifier_name))
                    )


def build_signals(signals: TSignals):
    for name, signal in signals.items():
        yield '{}: {}'.format(
            convert_name_case(name),
            signal.adapt()
        )
