from textwrap import dedent
from textwrap import indent

from declare_qtquick.typehint import TsComponent as T


def build_component(comp: T.Component, level=0) -> str:
    # assert level % 4 == 0
    return indent(
        dedent('''
                {widget_name} {{
                    id: {qid}
                    
                    // Properties
                    {properties}
                    
                    // Connections
                    {connections}
                    
                    // Children
                    {children}
                }}
            ''').strip().format(
            widget_name=comp.name,
            qid=comp.qid,
            properties=indent(
                '\n'.join(build_properties(comp.properties)),
                '    '
            ) or '// NO_PROPERTIES_DEFINITION',
            connections=indent(
                '\n'.join(build_connections(comp.properties)),
                '    '
            ) or '// NO_CONNECTION_DEFINITION',
            children='{children}'
        ),
        ' ' * level
    )


def build_properties(props: T.Properties):
    for name, prop in props.items():
        # yield name, prop.value
        yield f'{name}: {prop.value}'


def build_connections(props: T.Properties):
    for name, prop in props.items():
        # yield name, prop.value
        yield f'{name}: {prop.value}'


class NameConversion:
    
    @staticmethod
    def snake_case_to_camel_case(name: str):
        return ''.join(
            [
                word.capitalize()
                for word in name.split('_')
            ]
        )
