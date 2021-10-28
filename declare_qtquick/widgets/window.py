from .__external__ import *
from .item import Item


class Window(Item, PWindow):
    name = 'Window'
    
    def __init__(self):
        super().__init__()
        self.properties.update({
            'color': ColorProp(self.qid, 'color', '#000000'),
        })
