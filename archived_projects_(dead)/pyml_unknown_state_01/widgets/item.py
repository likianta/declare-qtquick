from ..properties.anchors import Anchors
from pyml.keywords import true

from .base_component import BaseComponent


class Item(BaseComponent):
    anchors: Anchors
    enabled: bool
    height: float
    width: float
    
    size: tuple
    
    def _init_raw_props(self):
        self.anchors = Anchors()
        self.enabled = true
        self.height = 0
        self.width = 0
    
    def _init_custom_props(self):
        self.size = (0, 0)
    
    def on_size_changed(self, v):
        self.width, self.height = v
    
    def on_width_changed(self, v):
        self.size = (v, self.height)
    
    def on_height_changed(self, v):
        self.size = (self.width, v)
    
    @property
    def full(self):
        return str(self.uid)
    
    @property
    def left(self):
        return f'{self.uid}.left'
    
    @property
    def right(self):
        return f'{self.uid}.right'
    
    @property
    def top(self):
        return f'{self.uid}.top'
    
    @property
    def bottom(self):
        return f'{self.uid}.bottom'
    
    @property
    def hcenter(self):
        return f'{self.uid}.horizontalCenter'
    
    @property
    def vcenter(self):
        return f'{self.uid}.verticalCenter'
