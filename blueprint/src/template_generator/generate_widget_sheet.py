import re
from collections import defaultdict
from textwrap import dedent
from textwrap import indent

from lk_logger import lk
from lk_utils import dumps
from lk_utils import loads

from blueprint.src import io
from blueprint.src.common import camel_2_snake_case
from blueprint.src.typehint import *

BASE_CLASS = 'P.PropSheet'
# DEFAULT_OUTPUT_FILE = io.project_dir \
#                       + '/declare_qtquick/properties/prop_sheet/ext.py'
DEFAULT_OUTPUT_FILE = io.project_dir \
                      + '/declare_qtquick/widgets/widget_sheet.py'


def main(output_file: TPath = DEFAULT_OUTPUT_FILE):
    data_r = loads(io.json_3)  # type: TJson3Data
    data_w = defaultdict(dict)  # type: TWidgetSheetData1
    
    # data_r 的数据结构比较复杂. 下面的代码逻辑主要基于 `io.json_3.<data>.<key
    # :qtquick>` 进行观察和编写.
    
    with lk.counting(len(data_r)):
        
        for package, v0 in data_r.items():
            if package == '': continue
            lk.logdx(package)
            
            with lk.counting(len(v0)):
                
                for widget_name, v1 in v0.items():
                    widget_name = 'Ps' + widget_name
                    
                    if v1['parent']:
                        # noinspection PyTypeChecker
                        parent_name = 'Ps' + v1['parent']
                    else:
                        parent_name = BASE_CLASS
                    
                    lk.logax(widget_name, parent_name)
                    
                    props = v1['props']
                    data_w[widget_name][parent_name] = props
    
    widgets_dict = {}  # type: TWidgetSheetData2
    widget_tmpl = dedent('''
        class {WIDGET}({PARENT}):
            {PROPS}
    ''').strip()
    
    for widget_name, parent_name, raw_props in _merge_multi_parent_case(data_w):
        if raw_props:
            widgets_dict[widget_name] = (
                parent_name,
                widget_tmpl.format(
                    WIDGET=widget_name,
                    PARENT=parent_name,
                    PROPS=indent(
                        '\n'.join((
                            f'{k}: {v}'
                            for k, v in _generate_props(raw_props)
                        )),
                        '    '
                    ).lstrip(),
                )
            )
        else:
            widgets_dict[widget_name] = (
                parent_name,
                widget_tmpl.format(
                    WIDGET=widget_name,
                    PARENT=parent_name,
                    PROPS='pass',
                )
            )
    
    # TEST
    # template = dedent('''
    #     from typing import Union
    #
    #     from declare_qtquick import properties as P  # noqa
    #
    #
    #     {WIDGETS}
    # ''')
    template = dedent('''
        """
        - This module is auto generated by `declare-qtquick/blueprint/src
          /template_generator/create_widget_sheet.py`.
        - Please do not edit this file directly.
        - (For developer) this module shouldn't be imported by `declare_qtquick
          .properties.prop_sheet.__init__`, although it is in the same folder.
          Otherwise it will cause a circular import error.
        - The prefix 'Ps' means 'declare_qtquick.properties.prop_sheet
          .PropSheet'.
        - The prefix 'P' means 'declare_qtquick.properties'.
        """
        from typing import Union
        
        from __declare_qtquick_internals__ import P
        
        
        {WIDGETS}
    ''')
    dumps(template.format(WIDGETS='\n\n\n'.join(
        _sort_formatted_list(widgets_dict, exclusions=(BASE_CLASS,))
    )).strip(), output_file)


def _merge_multi_parent_case(data: TWidgetSheetData1) \
        -> Iterator[Tuple[TWidgetName, TParentName, TProps]]:
    """
    Before:
        {
            aaa: {
                bbb: {'x': 0, 'y': 0},
                ccc: {'width': 0, 'height': 0},
                ...
            }
        }
    After:
        {
            aaa: (BASE_CLASS, {'x': 0, 'y': 0, 'width': 0, 'height': 0})
        }
    """
    
    def _loop(widget_name):
        if widget_name not in data:
            return
        for parent_name, props in data[widget_name].items():
            yield props
            yield from _loop(parent_name)
    
    for widget_name, v0 in data.items():
        if len(v0) == 0:
            raise ValueError(widget_name)
        elif len(v0) == 1:
            for parent_name, props in v0.items():
                yield widget_name, parent_name, props
        else:
            all_props = {}
            [all_props.update(x) for x in _loop(widget_name)]
            yield widget_name, BASE_CLASS, all_props


def _generate_props(props: Dict[str, str]) -> Iterator[Tuple[str, str]]:
    basic_qml_types = {
        # summary:
        #   keys are qml basic types. values are `declare_qtquick.properties`.
        # keys:
        #   the keys are from qt documentation (see `declare_qtquick
        #   .properties.basic_properties.<docstring>.references`).
        #   you can also find all basic qml types in `io.json_3.<data>
        #   .<key=''>.<keys which starts with lower case character>`.
        # values:
        #   some values are tuple[python_primitive_type, custom_type], others
        #   are tuple['', custom_type].
        'bool'                : ('bool', 'P.Bool'),
        'color'               : ('str', 'P.Color'),
        'date'                : ('', 'P.Date'),
        'double'              : ('float', 'P.Double'),
        'enumeration'         : ('int', 'P.Enumeration'),  
        #   ps: we're considering change the value to 'Enum'. currently 
        #   (2021-10-30) it is not implemented yet.
        'int'                 : ('int', 'P.Int'),
        'list'                : ('list', 'P.List'),
        'matrix4x4'           : ('', 'P.Matrix4x4'),
        'real'                : ('float', 'P.Real'),
        'string'              : ('str', 'P.String'),
        'url'                 : ('str', 'P.Url'),
        'var'                 : ('', 'P.Var'),
        
        # group properties
        'anchors'             : ('', 'P.Anchors'),
        'axis'                : ('', 'P.Axis'),
        'border'              : ('', 'P.Border'),
        'children_rect'       : ('', 'P.ChildrenRect'),
        'down'                : ('', 'P.Down'),
        'drag'                : ('', 'P.Drag'),
        'easing'              : ('', 'P.Easing'),
        'first'               : ('', 'P.First'),
        'font'                : ('', 'P.Font'),
        'font_info'           : ('', 'P.FontInfo'),
        'icon'                : ('', 'P.Icon'),
        'layer'               : ('', 'P.Layer'),
        'origin'              : ('', 'P.Origin'),
        'pinch'               : ('', 'P.Pinch'),
        'point'               : ('', 'P.Point'),
        'quaternion'          : ('', 'P.Quaternion'),
        'rect'                : ('', 'P.Rect'),
        'second'              : ('', 'P.Second'),
        'section'             : ('', 'P.Section'),
        'selected_name_filter': ('', 'P.SelectedNameFilter'),
        'size'                : ('', 'P.Size'),
        'swipe'               : ('', 'P.Swipe'),
        'target'              : ('', 'P.Target'),
        'up'                  : ('', 'P.Up'),
        'vector2d'            : ('', 'P.Vector2D'),
        'vector3d'            : ('', 'P.Vector3D'),
        'vector4d'            : ('', 'P.Vector4D'),
        'visible_area'        : ('', 'P.VisibleArea'),
        'word_candidate_list' : ('', 'P.WordCandidateList'),
        'x_axis'              : ('', 'P.XAxis'),
        'y_axis'              : ('', 'P.YAxis'),
        
        # unlisted
        'float'               : ('float', 'P.Number'),
    }
    
    # prop_list = []  # type: List[str]
    # prop_tmpl = '{PROP_NAME}: {PROP_TYPE}'
    
    for prop_name, prop_type in props.items():
        # adjust prop_name
        if '.' in prop_name:
            continue
        prop_name = camel_2_snake_case(prop_name)
        #   e.g. 'checkStateMixed' -> 'check_state_mixed'
        if prop_name in ('from', 'name', 'properties'):  # FIXME
            #   'name', 'properties' are occupied by `declare_qtquick.widgets
            #   .base.Component`
            prop_name += '_'
        
        # ----------------------------------------------------------------------
        
        # adjust prop_type
        prop_type = prop_type.lower()
        if '::' in prop_type:
            prop_type = prop_type.replace('::', '.')
        prop_type = re.match(r'[.\w]+', prop_type).group()
        
        if prop_type[0].isupper():  # e.g. 'Item'
            prop_type = 'Union[{}, P.Delegate]'.format(prop_type)
        
        else:
            if prop_type == 'group':
                _temp_collector['group_props'].add((prop_name, prop_type))
                prop_type = prop_name
            
            if prop_type in basic_qml_types:
                a, b = basic_qml_types[prop_type]
                if a:
                    prop_type = 'Union[{}, {}]'.format(a, b)
                    #   e.g. 'Union[str, String]'
                else:
                    prop_type = b  # e.g. 'Anchors'
            else:
                prop_type = 'P.Property'
                # prop_type = 'Union["{}", P.Property]'.format(prop_type)
                _temp_collector['unknown_props'].add((prop_name, prop_type))
        
        yield prop_name, prop_type


# TODO: unify with `.main.sort_widget_list`
def _sort_formatted_list(widgets_dict: TWidgetSheetData2,
                         exclusions: tuple = None) -> TFormatted:
    if exclusions is None:
        exclusions = ()
    
    # counter
    who_is_most_required = defaultdict(int)  # {parent_name: count, ...}
    
    def _loop(widget_name):
        if widget_name not in widgets_dict:
            lk.logt('[W4227]', 'this name is not in __list__', widget_name)
            return
        
        parent_name = widgets_dict[widget_name][0]
        if parent_name in exclusions:
            return
        
        who_is_most_required[parent_name] += 1
        _loop(parent_name)
    
    for widget_name in widgets_dict:
        _loop(widget_name)
    
    lk.logp(sorted(
        [(k, v) for k, v in who_is_most_required.items()],
        key=lambda k_v: k_v[1], reverse=True
    ), title="who's the most required")
    
    for widget_name in sorted(
            widgets_dict.keys(),
            key=lambda widget_name: who_is_most_required[widget_name],
            reverse=True
    ):
        yield widgets_dict[widget_name][1]


if __name__ == '__main__':
    _temp_collector = {  # TEST
        'group_props'  : set(),
        'unknown_props': set(),
    }
    
    # main('../../../tests/test1.py')
    main(DEFAULT_OUTPUT_FILE)
    
    lk.logp(_temp_collector)
