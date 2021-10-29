from typing import *

TClassName = str  # e.g. 'Item', 'Rectangle', 'MouseArea', ...
TModuleName = str
TPackageName = str  # e.g. 'QtQuick.Controls'

TProperty = str  # e.g. 'border', 'border.color', 'width', 'height', ...

TQType = Literal[
    'array', 'bool', 'color', 'group', 'int', 'real', 'string', 'var'
]
TQmlType = str


# ------------------------------------------------------------------------------

class _TDataNo5Value(TypedDict):
    parent: TQmlType
    props: Dict[TProperty, TQType]


TDataNo5 = Dict[TModuleName, Dict[TQmlType, _TDataNo5Value]]
'''
    {
        module: {
            qmltype: {
                'parent': parent_qmltype,
                'props': {prop: type, ...}
            }, ...
        }, ...
    }
'''


class _TDataNo6Value(TypedDict):
    parent: TClassName
    props: Dict[TProperty, TQType]


TDataNo6 = Dict[TPackageName, Dict[TClassName, _TDataNo6Value]]
'''
    {
        TPackageName: {
            TClassName: {
                'parent': TClassName,
                'props': {TProperty: TQType, ...}
            }, ...
        }, ...
    }
    e.g. {
        'qtquick': {
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
