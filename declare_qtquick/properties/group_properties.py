"""
References:
    Online: All QML Basic Types:
        https://doc.qt.io/qt-6/qmlbasictypes.html
    Qt Assistant > Qt <version> Reference Documentation > QML Types:
        All QML Basic Types
        
Relations:
    .prop_sheet.api
"""
from .base import PropertyGroup
from .prop_sheet.api import *
from .__ext__ import proxy

__all__ = [
    'Anchors',
    'Axis',
    'Border',
    'ChildrenRect',
    'Down',
    'Drag',
    'Easing',
    'First',
    'Font',
    'FontInfo',
    'Icon',
    'Layer',
    'Origin',
    'Pinch',
    'Point',
    'Quaternion',
    'Rect',
    'Second',
    'Section',
    'SelectedNameFilter',
    'Size',
    'Swipe',
    'Target',
    'Up',
    'Vector2D',
    'Vector3D',
    'Vector4D',
    'VisibleArea',
    'WordCandidateList',
    'XAxis',
    'YAxis',
]


class Anchors(PropertyGroup, PsAnchors):
    name = 'anchors'
    
    # ref: declare_qtquick.control.traits.PropGetterAndSetter
    #      .__getprop__,.__setprop__
    
    def __getprop__(self, key: str):
        if key == 'center_in' or key == 'fill':
            raise AttributeError('You cannot access this property from getter, '
                                 'this is a write-only property.', key)
        elif key == 'horizontal_center' or key == 'vertical_center':
            return proxy.getprop(self, key, self.fullname)  # -> str
        elif key == 'margins' or key.endswith('_margin'):  # -> int or float
            return proxy.getprop(self, key, self._properties[key].value)
        else:  # left, top, right, bottom
            return proxy.getprop(self, key, f'{self.fullname}.{key}')
    
    def __setprop__(self, key, value):
        if key == 'center_in' or key == 'fill':
            from ..widgets.api.qtquick import Window
            if isinstance(value, str):
                # # self._properties[key].set(value)
                proxy.setprop(
                    self, key, value,
                    lambda key, value: self._properties[key].set(value)
                )
            elif isinstance(value, Window):
                # # self._properties[key].set(value.content_item)
                proxy.setprop(
                    self, key, value,
                    lambda key, value: self._properties[key].set(
                        value.content_item)
                )
            else:
                # # self._properties[key].set(value.qid)
                proxy.setprop(
                    self, key, value,
                    lambda key, value: self._properties[key].set(value.qid)
                )
        elif key == 'margins' or key.endswith('_margin'):
            # assert isinstance(value, (int, float))
            # # self._properties[key].set(value)
            proxy.setprop(
                self, key, value,
                lambda key, value: self._properties[key].set(value)
            )
        elif key == 'horizontal_center' or key == 'vertical_center':
            # assert value == key
            # # self._properties[key].set(value)
            proxy.setprop(
                self, key, value,
                lambda key, value: self._properties[key].set(value)
            )
        else:  # left, top, right, bottom
            # # self._properties[key].set(value)
            proxy.setprop(
                self, key, value,
                lambda key, value: self._properties[key].set(value)
            )


class Axis(PropertyGroup, PsAxis):
    name = 'axis'


class Border(PropertyGroup, PsBorder):
    name = 'border'


class ChildrenRect(PropertyGroup, PsChildrenRect):
    name = 'children_rect'


class Down(PropertyGroup, PsDown):
    name = 'down'


class Drag(PropertyGroup, PsDrag):
    name = 'drag'


class Easing(PropertyGroup, PsEasing):
    name = 'easing'


class First(PropertyGroup, PsFirst):
    name = 'first'


class Font(PropertyGroup, PsFont):
    name = 'font'


class FontInfo(PropertyGroup, PsFontInfo):
    name = 'fontInfo'


class Icon(PropertyGroup, PsIcon):
    name = 'icon'


class Layer(PropertyGroup, PsLayer):
    name = 'layer'


class Origin(PropertyGroup, PsOrigin):
    name = 'origin'


class Pinch(PropertyGroup, PsPinch):
    name = 'pinch'


class Point(PropertyGroup, PsPoint):
    name = 'point'


class Quaternion(PropertyGroup, PsQuaternion):
    name = 'quaternion'


class Rect(PropertyGroup, PsRect):
    name = 'rect'


class Second(PropertyGroup, PsSecond):
    name = 'second'


class Section(PropertyGroup, PsSection):
    name = 'section'


class SelectedNameFilter(PropertyGroup, PsSelectedNameFilter):
    name = 'selected_name_filter'


class Size(PropertyGroup, PsSize):
    name = 'size'


class Swipe(PropertyGroup, PsSwipe):
    name = 'swipe'


class Target(PropertyGroup, PsTarget):
    name = 'target'


class Up(PropertyGroup, PsUp):
    name = 'up'


class Vector2D(PropertyGroup, PsVector2D):
    name = 'vector2d'


class Vector3D(PropertyGroup, PsVector3D):
    name = 'vector3d'


class Vector4D(PropertyGroup, PsVector4D):
    name = 'vector4d'


class VisibleArea(PropertyGroup, PsVisibleArea):
    name = 'visible_area'


class WordCandidateList(PropertyGroup, PsWordCandidateList):
    name = 'word_candidate_list'


class XAxis(PropertyGroup, PsXAxis):
    name = 'x_axis'


class YAxis(PropertyGroup, PsYAxis):
    name = 'y_axis'
