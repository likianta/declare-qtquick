from .__external__ import Number
from .__external__ import PItem
from .__external__ import Anchors
from .__external__ import Boolean
from .base import Component


class Item(Component, PItem):
    name = 'Item'
    
    def __ready__(self):
        self.properties.update({
            'anchors': Anchors(self.qid, 'anchors'),
            'x'      : Number(self.qid, 'x'),
            'y'      : Number(self.qid, 'y'),
            'z'      : Number(self.qid, 'z'),
            'width'  : Number(self.qid, 'width'),
            'height' : Number(self.qid, 'height'),
            'opacity': Number(self.qid, 'opacity'),
            'visible': Boolean(self.qid, 'visible'),
        })
