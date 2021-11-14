from .base_item import BaseItem

from .core.authorized_props import ItemProps
from ..typehint import TPath


class Test(BaseItem, ItemProps):
    
    def __init__(self, qmlfile: TPath):
        self.qmlfile = qmlfile
        super().__init__()
