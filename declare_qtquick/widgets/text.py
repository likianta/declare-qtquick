from .__external__ import *
from .item import Item


class Text(Item, PText):
    name = 'Text'

    def __ready__(self):
        super().__ready__()
        self.properties.update({
            'color': Color(self.qid, 'color'),
            'text' : String(self.qid, 'text', ''),
        })
