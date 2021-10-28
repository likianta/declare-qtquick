from .__external__ import TsProperty as T
from .base import Property


class ColorProp(Property):
    value: T.Color
    
    def __init__(self, qid: T.Qid, name: T.Name, default_value=''):
        super().__init__(qid, name, default_value)


class NumberProp(Property):
    value: T.Number
    
    def __init__(self, qid: T.Qid, name: T.Name, default_value=0):
        super().__init__(qid, name, default_value)


class StringProp(Property):
    value: T.String
    
    def __init__(self, qid: T.Qid, name: T.Name, default_value=''):
        super().__init__(qid, name, default_value)
