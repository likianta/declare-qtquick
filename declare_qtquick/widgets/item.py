from .__external__ import NumberProp
from .__external__.prophint import PItem
from .base import Component


class Item(Component, PItem):
    name = 'Item'
    
    def __init__(self):
        super().__init__()
        self.properties.update({
            'x'      : NumberProp(self.qid, 'x', 0),
            'y'      : NumberProp(self.qid, 'y', 0),
            'z'      : NumberProp(self.qid, 'z', 0),
            'width'  : NumberProp(self.qid, 'width', 0),
            'height' : NumberProp(self.qid, 'height', 0),
            'opacity': NumberProp(self.qid, 'opacity', 0.0),
        })
