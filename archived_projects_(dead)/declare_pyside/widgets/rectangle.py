from .base_item import BaseItem

from .core.authorized_props import RectangleProps
from ..path_model import light_clean_theme_dir


class Rectangle(BaseItem, RectangleProps):
    qmlfile = f'{light_clean_theme_dir}/LCRectangle.qml'
