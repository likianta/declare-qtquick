from .base_component import BaseComponent


class Rectangle(BaseComponent):
    
    def _init_raw_props(self):
        self.color = '#ffffff'
        self.radius = 0
