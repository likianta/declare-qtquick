from .__external__ import PAnchors
from .__external__ import TsProperty as T
from .base import Property
from .base import PropertyGroup
from .normal_properties import Number


class Anchors(PropertyGroup, PAnchors):
    
    def __init__(self, qid: T.Qid, name: T.Name = 'anchors'):
        super().__init__(qid, name)
        self.properties.update({
            'center_in'        : Property(qid, name, None),
            'fill'             : Property(qid, name, None),
            'left'             : Property(qid, name, None),
            'top'              : Property(qid, name, None),
            'right'            : Property(qid, name, None),
            'bottom'           : Property(qid, name, None),
            'horizontal_center': Property(qid, name, None),
            'vertical_center'  : Property(qid, name, None),
            'margins'          : Number(qid, name, 0),
            'left_margin'      : Number(qid, name, 0),
            'top_margin'       : Number(qid, name, 0),
            'right_margin'     : Number(qid, name, 0),
            'bottom_margin'    : Number(qid, name, 0),
        })
    
    def __getprop__(self, key: str):
        if key == 'center_in' or key == 'fill':
            raise AttributeError('You cannot access this property from getter, '
                                 'this is a write-only property.', key)
        elif key == 'horizontal_center' or key == 'vertical_center':
            return self.fullname  # str
        elif key == 'margins' or key.endswith('_margin'):
            return self.properties[key].value  # int or float
        else:  # left, top, right, bottom
            return f'{self.fullname}.{key}'
    
    def __setprop__(self, key, value):
        if key == 'center_in' or key == 'fill':
            # assert isinstance(value, Property)
            self.properties[key].set(value.qid)
        elif key == 'margins' or key.endswith('_margin'):
            # assert isinstance(value, (int, float))
            self.properties[key].set(value)
        elif key == 'horizontal_center' or key == 'vertical_center':
            # assert value == key
            self.properties[key].set(value)
        else:  # left, top, right, bottom
            self.properties[key].set(value)
