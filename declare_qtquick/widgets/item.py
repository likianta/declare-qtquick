from .__external__ import Number
from .__external__ import PItem
from .base import Component


class Item(Component, PItem):
    name = 'Item'
    
    def __init__(self):
        super().__init__()
        self.properties.update({
            'x'      : Number(self.qid, 'x', 0),
            'y'      : Number(self.qid, 'y', 0),
            'z'      : Number(self.qid, 'z', 0),
            'width'  : Number(self.qid, 'width', 0),
            'height' : Number(self.qid, 'height', 0),
            'opacity': Number(self.qid, 'opacity', 0.0),
        })
