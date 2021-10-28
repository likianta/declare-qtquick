from .__external__ import *
from .item import Item


class Window(Item, PWindow):
    name = 'Window'

    def __ready__(self):
        super().__ready__()
        self.properties.update({
            'color': Color(self.qid, 'color', '#000000'),
        })
