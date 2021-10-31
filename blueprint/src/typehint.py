from os import PathLike
from typing import *

TPath = Union[str, PathLike]

TPackageName = str  # e.g. 'QtQuick.Controls'
TWidgetName = str  # e.g. 'Item', 'Rectangle', 'MouseArea', ...
TParentName = TWidgetName
TPropName = str  # e.g. 'border', 'border.color', 'width', 'height', ...

TQmlType = Literal[
    'array', 'bool', 'color', 'group', 'int', 'real', 'string', 'var'
]


class TWidgetValue(TypedDict):
    parent: Tuple[TPackageName, TWidgetName]
    props: Dict[TPropName, TQmlType]


TWidgetData = Dict[TWidgetName, TWidgetValue]
TJson3Data = Dict[TPackageName, TWidgetData]
'''e.g. {
        'QtQuick': {
            'Rectangle': {
                'parent': ['QtQuick', 'Item'],
                'props': {
                    'border': 'group',
                    'border.color': 'color',
                    ...
                }
            }, ...
        }, ...
    }
'''

TTemplate = str
TFormatted = str

TPropType = str
TProps = Dict[TPropName, TPropType]
TWidgetSheetData1 = Dict[TWidgetName, Dict[TParentName, TProps]]
TWidgetSheetData2 = Dict[TWidgetName, Tuple[TParentName, TFormatted]]
