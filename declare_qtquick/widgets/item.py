from .__external__ import Number
from .__external__ import PItem
from .__external__ import Anchors
from .base import Component


class Item(Component, PItem):
    name = 'Item'
    
    def __ready__(self):
        self.properties.update({
            'anchors': Anchors(self.qid, 'anchors'),
            'x'      : Number(self.qid, 'x', 0),
            'y'      : Number(self.qid, 'y', 0),
            'z'      : Number(self.qid, 'z', 0),
            'width'  : Number(self.qid, 'width', 0),
            'height' : Number(self.qid, 'height', 0),
            'opacity': Number(self.qid, 'opacity', 0.0),
        })
