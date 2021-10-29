from .__external__ import TsProperty as T
from .base import Property


class Boolean(Property):
    value: T.Bool
    
    def adapt(self):
        return 'true' if self.value else 'false'


class Color(Property):
    value: T.Color
    
    def adapt(self):
        return f'"{self.value}"'


class Number(Property):
    value: T.Number


class String(Property):
    value: T.String
    
    def adapt(self):
        return f'"{self.value}"'
