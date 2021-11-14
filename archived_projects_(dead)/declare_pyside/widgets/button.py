from .base_item import BaseItem

from .core.authorized_props import ButtonProps
from ..path_model import light_clean_theme_dir


class Button(BaseItem, ButtonProps):
    qmlfile = f'{light_clean_theme_dir}/LCButtons/LCButton.qml'
