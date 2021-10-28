from .__external__ import TsProperty as T
from .base import Property


class Boolean(Property):
    value: T.Bool
    
    def __init__(self, qid, name, default_value=False):
        super().__init__(qid, name, default_value)


class Color(Property):
    value: T.Color
    
    def __init__(self, qid, name, default_value=''):
        super().__init__(qid, name, default_value)


class Number(Property):
    value: T.Number
    
    def __init__(self, qid, name, default_value=0):
        super().__init__(qid, name, default_value)


class String(Property):
    value: T.String
    
    def __init__(self, qid, name, default_value=''):
        super().__init__(qid, name, default_value)
