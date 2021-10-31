from typing import Union

from .__ext__ import *
from .base import PropSheet

# appendix types
num = Union[int, float]
enum = Union[str, int]

__all__ = [
    'PsAnchors',
    'PsAxis',
    'PsBorder',
    'PsChildrenRect',
    'PsDown',
    'PsDrag',
    'PsEasing',
    'PsFirst',
    'PsFont',
    'PsFontInfo',
    'PsIcon',
    'PsLayer',
    'PsOrigin',
    'PsPinch',
    'PsPoint',
    'PsQuaternion',
    'PsRect',
    'PsSecond',
    'PsSection',
    'PsSelectedNameFilter',
    'PsSize',
    'PsSwipe',
    'PsTarget',
    'PsUp',
    'PsVector2D',
    'PsVector3D',
    'PsVector4D',
    'PsVisibleArea',
    'PsWordCandidateList',
    'PsXAxis',
    'PsYAxis',
]


# ------------------------------------------------------------------------------
# Found in 'All QML Basic Types'

class PsFont(PropSheet):
    """
    Index:
        Qt 6 > Qt Quick > QML Types > font QML Basic Type
    """
    bold: Union[bool, Bool]
    capitalization: Union[enum, Enumeration]
    family: Union[str, String]
    hinting_preference: Union[enum, Enumeration]
    italic: Union[bool, Bool]
    kerning: Union[bool, Bool]
    letter_spacing: Union[float, Number]
    overline: Union[bool, Bool]
    pixel_size: Union[int, Number]
    point_size: Union[float, Number]
    prefer_shaping: Union[bool, Bool]
    strikeout: Union[bool, Bool]
    style_name: Union[str, String]
    underline: Union[bool, Bool]
    weight: Union[enum, Enumeration]
    word_spacing: Union[float, Number]


class PsPoint(PropSheet):
    x: Union[num, Number]
    y: Union[num, Number]


class PsQuaternion(PropSheet):
    scalar: Union[num, Number]
    x: Union[num, Number]
    y: Union[num, Number]
    z: Union[num, Number]


class PsRect(PropSheet):
    height: Union[num, Number]
    width: Union[num, Number]
    x: Union[num, Number]
    y: Union[num, Number]


class PsSize(PropSheet):
    height: Union[num, Number]
    width: Union[num, Number]


class PsVector2D(PropSheet):
    x: Union[num, Number]
    y: Union[num, Number]


class PsVector3D(PropSheet):
    x: Union[num, Number]
    y: Union[num, Number]
    z: Union[num, Number]


class PsVector4D(PropSheet):
    w: Union[num, Number]
    x: Union[num, Number]
    y: Union[num, Number]
    z: Union[num, Number]


# ------------------------------------------------------------------------------
# Found in Qt Doc (All QML Types)

''' All 'group' Types Found in Qt Doc

- anchors
- axis
- border
- children_rect
- down
- drag
- easing
- first
- icon
- origin
- pinch
- second
- section
- selected_name_filter
- swipe
- target_property
- up
- visible_area
- word_candidate_list
- x_axis
- y_axis

You can use `blueprint/src/sidework/list_all_group_properties.py` to view their
detailed attributes.
'''


class PsAnchors(PropSheet):
    align_when_centered: Union[bool, Bool]
    baseline: Property
    baseline_offset: Union[num, Number]
    bottom: Property
    bottom_margin: Union[num, Number]
    center_in: Property
    fill: Property
    horizontal_center: Property
    horizontal_center_offset: Union[num, Number]
    left: Property
    left_margin: Union[num, Number]
    margins: Union[num, Number]
    right: Property
    right_margin: Union[num, Number]
    top_margin: Union[num, Number]
    top: Property
    vertical_center: Property
    vertical_center_offset: Union[num, Number]


class PsAxis(PropSheet):
    x: Union[num, Number]
    y: Union[num, Number]
    z: Union[num, Number]


class PsBorder(PropSheet):
    bottom: Union[num, Number]
    color: Union[str, Color]
    left: Union[num, Number]
    right: Union[num, Number]
    top: Union[num, Number]
    width: Union[num, Number]


class PsChildrenRect(PropSheet):
    height: Union[num, Number]
    width: Union[num, Number]
    x: Union[num, Number]
    y: Union[num, Number]


class PsDown(PropSheet):
    hovered: Union[bool, Bool]
    implicit_indicator_height: Union[num, Number]
    implicit_indicator_width: Union[num, Number]
    indicator: AnyItem
    pressed: Union[bool, Bool]


class PsDrag(PropSheet):
    active: Union[bool, Bool]
    axis: Union[enum, Enumeration]
    filter_children: Union[bool, Bool]
    maximum_x: Union[num, Number]
    maximum_y: Union[num, Number]
    minimum_x: Union[num, Number]
    minimum_y: Union[num, Number]
    smoothed: Union[bool, Bool]
    source: AnyItem
    target: AnyItem
    threshold: Union[num, Number]
    x: Union[num, Number]
    y: Union[num, Number]


class PsEasing(PropSheet):
    amplitude: Union[num, Number]
    bezier_curve: Union[list, List]
    overshoot: Union[num, Number]
    period: Union[num, Number]
    type: Union[enum, Enumeration]


class PsFirst(PropSheet):
    handle: AnyItem
    hovered: Union[bool, Bool]
    implicit_handle_height: Union[num, Number]
    implicit_handle_width: Union[num, Number]
    position: Union[num, Number]
    pressed: Union[bool, Bool]
    value: Union[num, Number]
    visual_position: Union[num, Number]


class PsFontInfo(PropSheet):
    bold: Union[bool, Bool]
    family: Union[str, String]
    italic: Union[bool, Bool]
    pixel_size: Union[str, String]
    point_size: Union[num, Number]
    style_name: Union[str, String]
    weight: Union[int, Int]


class PsIcon(PropSheet):
    cache: Union[bool, Bool]
    color: Union[str, Color]
    height: Union[num, Number]
    mask: Union[bool, Bool]
    name_: Union[str, String]
    source: Union[str, Url]
    width: Union[num, Number]


class PsLayer(PropSheet):
    effect: AnyItem
    enabled: Union[bool, Bool]
    format: Union[enum, Enumeration]
    mipmap: Union[bool, Bool]
    sampler_name: Union[str, String]
    samples: Union[enum, Enumeration]
    smooth: Union[bool, Bool]
    source_rect: PsRect
    texture_mirroring: Union[enum, Enumeration]
    texture_size: PsSize
    wrap_mode: Union[enum, Enumeration]


class PsOrigin(PropSheet):
    x: Union[num, Number]
    y: Union[num, Number]


class PsPinch(PropSheet):
    active: Union[bool, Bool]
    drag_axis: Union[enum, Enumeration]
    maximum_rotation: Union[num, Number]
    maximum_scale: Union[num, Number]
    maximum_x: Union[num, Number]
    maximum_y: Union[num, Number]
    minimum_rotation: Union[num, Number]
    minimum_scale: Union[num, Number]
    minimum_x: Union[num, Number]
    minimum_y: Union[num, Number]
    target: AnyItem


class PsSecond(PropSheet):
    handle: AnyItem
    hovered: Union[bool, Bool]
    implicit_handle_height: Union[num, Number]
    implicit_handle_width: Union[num, Number]
    position: Union[num, Number]
    pressed: Union[bool, Bool]
    value: Union[num, Number]
    visual_position: Union[num, Number]


class PsSection(PropSheet):
    criteria: Union[enum, Enumeration]
    delegate: AnyItem
    label_positioning: Union[enum, Enumeration]
    property: Union[str, String]


class PsSelectedNameFilter(PropSheet):
    extensions: Union[list, List]
    index: Union[int, Int]
    name_: Union[str, String]


class PsSwipe(PropSheet):
    behind: AnyItem
    behind_item: AnyItem
    complete: Union[bool, Bool]
    enabled: Union[bool, Bool]
    left: AnyItem
    left_item: AnyItem
    position: Union[num, Number]
    right: AnyItem
    right_item: AnyItem
    # noinspection PyUnresolvedReferences
    transition: AnyItem


class PsTarget(PropSheet):
    name_: Union[str, String]
    object: AnyItem


class PsUp(PropSheet):
    hovered: Union[bool, Bool]
    implicit_indicator_height: Union[num, Number]
    implicit_indicator_width: Union[num, Number]
    indicator: AnyItem
    pressed: Union[bool, Bool]


class PsVisibleArea(PropSheet):
    height_ratio: Union[num, Number]
    width_ratio: Union[num, Number]
    x_position: Union[num, Number]
    y_position: Union[num, Number]


class PsWordCandidateList(PropSheet):
    always_visible: Union[bool, Bool]
    auto_hide_delay: Union[int, Int]


class PsXAxis(PropSheet):
    enabled: Union[bool, Bool]
    maximum: Union[num, Number]
    minimum: Union[num, Number]


class PsYAxis(PropSheet):
    enabled: Union[bool, Bool]
    maximum: Union[num, Number]
    minimum: Union[num, Number]
