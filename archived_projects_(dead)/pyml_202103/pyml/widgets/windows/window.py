from pyml.keywords import true
from pyml.widgets.item import Item


class Window(Item):
    
    def _init_raw_props(self):
        super()._init_raw_props()
        self.color = '#ffffff'
        self.visile = true
    
    def _init_custom_props(self):
        self.size = (0, 0)
