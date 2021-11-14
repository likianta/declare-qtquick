from .base_item import BaseItem

from .core.authorized_props import MouseAreaProps
from ..path_model import widgets_dir


class MouseArea(BaseItem, MouseAreaProps):
    qmlfile = f'{widgets_dir}/qml_assets/MouseArea.qml'
