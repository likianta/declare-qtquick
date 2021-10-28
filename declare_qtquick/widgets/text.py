from .__external__ import *
from .item import Item


class Text(Item, PText):
    name = 'Text'
    
    def __init__(self):
        super().__init__()
        self.properties.update({
            'color': Color(self.qid, 'color', '#000000'),
            'text' : Number(self.qid, 'text', ''),
        })
