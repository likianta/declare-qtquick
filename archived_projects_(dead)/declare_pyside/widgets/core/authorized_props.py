from PySide6.QtCore import QObject
from PySide6.QtQuick import QQuickItem

from .prop_delegators import *
from ...typehint.qmlside import *
from ...typehint.widgets_support import *


class AuthorizedProps:
    """
    Notes.zh-CN:
        所有继承本类的子类, 如果该子类属于 Mixin 类型, 则必须将本类放在第一继承
        位置. 否则将导致 [MARK][1] 发生异常.
        
    Notes:
        All subclasses that inherit from this class, if the subclass is a Mixin
        type, it must place AuthorizedProps in its first Mixin position.
        Otherwise [MARK][1] will match a wrong baseclass.
        
        [1]: `<child_class>.<classmethod:get_authorized_props>.<while_loop>
             .<var:tmp_cls>.<code:'tmp_cls = tmp_cls.__base__'>`
    """
    # this is a special attribute that its name must be prefixed with
    # underscore. otherwise it will puzzle `<globals>._get_authorized_props
    # .<code:'if not k.startswith('_')'>`.
    _qprops: TAuthProps
    
    def __init__(self):
        self._init_authorized_props()
    
    def _init_authorized_props(self):
        """
        References:
            https://stackoverflow.com/questions/2611892/how-to-get-the-parents
                -of-a-python-class
        """
        if self.__class__ is AuthorizedProps:
            raise Exception('This method should be used in subclasses of '
                            '`AuthorizedProps`!')
        # trick: search `self.__class__.__bases__` by reversed sequence. this
        #   can be a little faster to find the target baseclass because usually
        #   we like putting `AuthorizedProps` or its subclasses in the end of
        #   mixin list.
        for cls in reversed(self.__class__.__bases__):
            # lk.logt('[D5835]', cls.__name__)
            if issubclass(cls, AuthorizedProps):
                self._qprops = cls._get_authorized_props()
                return
    
    @classmethod
    def _get_authorized_props(cls) -> TAuthProps:
        out = {}
        tmp_cls = cls
        while issubclass(tmp_cls, AuthorizedProps):
            out.update(_get_authorized_props(tmp_cls))
            tmp_cls = tmp_cls.__base__
        return out


def _get_authorized_props(cls) -> Iterable[tuple[TPropName, TConstructor]]:
    for k, v in cls.__annotations__.items():
        if not k.startswith('_'):
            yield k, v


# ------------------------------------------------------------------------------
# TODO: the following can be generated from blueprint

class AnchorsGroup(AuthorizedProps):
    fill: Union[str, PrimitivePropDelegator]
    center: Union[str, PrimitivePropDelegator]
    center_in: Union[str, PrimitivePropDelegator]
    
    left: Union[str, PrimitivePropDelegator]
    right: Union[str, PrimitivePropDelegator]
    top: Union[str, PrimitivePropDelegator]
    bottom: Union[str, PrimitivePropDelegator]
    
    margins_left: Union[str, PrimitivePropDelegator]
    margins_right: Union[str, PrimitivePropDelegator]
    margins_top: Union[str, PrimitivePropDelegator]
    margins_bottom: Union[str, PrimitivePropDelegator]


class DragGroup(AuthorizedProps):
    active: Union[bool, PrimitivePropDelegator]
    target: Union[TQObject, TItem, PropDelegatorA]


class FontGroup(AuthorizedProps):
    family: Union[str, PrimitivePropDelegator]
    pixel_size: Union[int, PrimitivePropDelegator]


class ItemProps(AuthorizedProps):
    anchors: Union[AnchorsGroup, AnchorsDelegator]
    height: Union[float, PropDelegatorA]
    object_name: Union[str, PropDelegatorA]
    width: Union[float, PropDelegatorA]
    x: Union[float, PropDelegatorA]
    y: Union[float, PropDelegatorA]
    z: Union[float, PropDelegatorA]


# ------------------------------------------------------------------------------

class ButtonProps(ItemProps):
    text: Union[str, PropDelegatorA]
    background: Union[object, PropDelegatorA]


class MouseAreaProps(ItemProps):
    drag: Union[DragGroup, DragDelegator]


class RectangleProps(ItemProps):
    background: Union[QQuickItem, PropDelegatorA]
    border: Union[QObject, PropDelegatorB]
    color: Union[str, PropDelegatorA]


class TextProps(ItemProps):
    font: Union[FontGroup, PropDelegatorC]
    text: Union[str, PropDelegatorA]


class WindowProps(ItemProps):
    color: Union[str, PropDelegatorA]
    visible: Union[bool, PropDelegatorA]
