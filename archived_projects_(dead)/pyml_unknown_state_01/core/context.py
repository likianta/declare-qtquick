from pyml.typehint import *
from .dict_tree import DictTreeEx


class Context:
    _com_tree = DictTreeEx(
        {'uid': None, 'level': 0, 'com': None, 'children': {}},
        setin='children'
    )
    ''' {
            uid: {
                'uid': TComponentID,
                'level': 0,
                'com': com,
                'children': {
                    uid: {...},
                    ...
                }
            },
            ...
        }
    '''
    
    def update(self, uid: TComponentID, layer_level: TLayerLevel,
               com: TComponent, last_com: TRepresent):
        """
        Returns:
            (this, parent)
        """
        parent_id = str(uid.parent_id)
        uid = str(uid)
        
        kwargs = {'uid': uid, 'level': layer_level, 'com': com}
        
        curr_level = layer_level
        last_level = last_com.level if last_com else -1
        
        if curr_level > last_level:
            self._com_tree.insert_inside(uid, **kwargs)
        elif curr_level == last_level:
            self._com_tree.insert_beside(uid, **kwargs)
        else:
            if (dedent_count := last_level - curr_level) == 1:
                self._com_tree.insert_ouside(uid, **kwargs)
            else:
                # noinspection PyTypeChecker
                for key in ([None] * (dedent_count - 1) + [uid]):
                    self._com_tree.insert_ouside(key)
        
        # ----------------------------------------------------------------------
        
        from pyml.core import id_ref
        this_com = id_ref[uid] = com
        parent_com = id_ref[parent_id]
        
        # FIXME: 相互指认关系的行为是否合适?
        this_com.parent = parent_com
        if parent_com: parent_com.children.append(this_com)
        
        from pyml.keywords import this, parent
        this.point_to(this_com)
        parent.point_to(parent_com)
        
        return this, parent


# class Property:
#     _deliver: list
#
#     def __init__(self):
#         pass
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#         if (on_key := f'on_{key}') not in self.__dict__:
#             self.__dict__[on_key] = Signal(self._deliver)
#
#     def _on_prop_changed(self, prop, value):
#         pass
#
#
# class Signal:
#
#     def __init__(self, _deliver):
#         self.slots = set()
#         self._deliver = _deliver
#
#     def __call__(self, *args, **kwargs):
#         """
#         Examples:
#             # assume button.clicked is an instance of Signal
#             button.clicked()
#         """
#         for f in self.slots:
#             f(*self._deliver, *args, **kwargs)
#
#     def binding(self, func):
#         """
#         Examples:
#             # assume button.clicked is an instance of Signal
#             button.clicked.binding(lambda : print('button is clicked'))
#         """
#         self.slots.add(func)


context = Context()
