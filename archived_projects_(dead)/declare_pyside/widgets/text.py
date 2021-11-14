from .base_item import BaseItem

from .core.authorized_props import TextProps
from ..path_model import light_clean_theme_dir


class Text(BaseItem, TextProps):
    qmlfile = f'{light_clean_theme_dir}/LCText.qml'
