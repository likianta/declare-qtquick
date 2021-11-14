"""
README:
    docs/everything-about-prop-delegators.zh.md
"""
# noinspection PyUnresolvedReferences,PyProtectedMember
from typing import _UnionGenericAlias as RealUnionType

from PySide6.QtQml import QQmlProperty

from .typehint import *
from ....qmlside import qmlside
from ....qmlside.qmlside import convert_name_case
from ....qmlside.qmlside import convert_primitive_type

_REGISTERED_NAMES = (
    'qobj', 'name', 'prop', 'read', 'write', 'kiss', 'bind'
)


class PrimitivePropDelegator:
    qobj: TQObject
    name: TPropName
    
    def __init__(self, qobj: TQObject, name: TPropName):
        self.qobj = qobj
        self.name = name
    
    def read(self):
        return self.qobj.property(convert_name_case(self.name))
    
    def write(self, value):
        self.qobj.setProperty(convert_name_case(self.name), value)


class PropDelegator:
    qobj: TQObject
    name: TPropName
    prop: TProperty
    
    def __init__(self, qobj: TQObject, name: TPropName):
        self.qobj = qobj
        self.name = name
        self.prop = QQmlProperty(qobj, convert_name_case(name))
    
    def __getattr__(self, item):
        if item in _REGISTERED_NAMES or item.startswith('_'):
            return super().__getattribute__(item)
        else:
            return self.__get_subprop__(item)
    
    def __setattr__(self, key, value):
        """
        Examples:
            xxx.name = 'xxx'
            xxx.width = 12
        """
        if key in _REGISTERED_NAMES or key.startswith('_'):
            super().__setattr__(key, value)
        else:
            self.__set_subprop__(key, value)
    
    def __get_subprop__(self, name: TPropName):
        raise NotImplementedError
    
    def __set_subprop__(self, name, value):
        raise NotImplementedError
    
    def read(self):
        return self.prop.read()
    
    def write(self, value):
        self.prop.write(value)
    
    def kiss(self, value):
        self.write(value)
    
    def bind(self, abstract_prop_expression: tuple[TQObject, str]):
        """
        Documents:
            See `docs/black-magic-about-binding-mechanism.zh.md`

        Notes:
            Trying hard to complete dynamic binding feature. You cannot use
            this method for now.
            If you want to dynamically bind the others' properties, try the
            following instead:
                # WIP
                <item_A>.<prop>.bind(<item_B>.<prop>)
                # Workaround
                <item_B>.<prop_changed>.connect(
                    lambda: <item_A>.<prop> = <item_B>.<prop>
                )
        """
        # last_frame = currentframe().f_back
        # event, participants = self._extract_frame_info(last_frame)
        raise NotImplemented
    
    # @staticmethod
    # def _extract_frame_info(frame):
    #     """
    #     Learning:
    #         source code of lk-logger
    #
    #     TODO: much work (unittest & optimization) need to be done...
    #     """
    #     filename = frame.f_code.co_filename
    #     lineno = frame.f_lineno
    #     file = open(filename, 'r', encoding='utf-8')
    #     source_line = file.read().splitlines()[lineno - 1]
    #     file.close()
    #
    #     assert (m := re.match(r'^ +(?:\w+\.)+\.bind\(', source_line)), '''
    #         Your binding statement is too complex to analyse!
    #         In current verison (v0.1.x) we can only parse format likes
    #         `<some_qobj>.<property_name>.bind(<expression>)`.
    #         Here's the position error happened FYI:
    #             Filename: {}
    #             Lineno: {}
    #             Source Line: {}
    #     '''.format(filename, lineno, source_line)
    #     source_line_stem = source_line[m.span()[0]:]
    #
    #     from lk_logger.scanner import get_all_blocks
    #     from ...base_item import BaseItem  # FIXME: not a good way
    #
    #     segs = source_line_stem[1:].split(',')
    #     segs[-1] = segs[-1].rstrip(', ')
    #     event = ''
    #     participants = []
    #     locals_ = frame.f_locals()
    #     for match0 in get_all_blocks(source_line_stem):
    #         event = match0.fulltext.strip()
    #         break
    #     for match in get_all_blocks(*segs, end_mark=','):
    #         obj_name, prop_name, *_ = match.fulltext.split('.')
    #         #   e.g. 'btn.x' -> 'btn'
    #         if obj_name in locals_:
    #             obj = locals_[obj_name]
    #             if isinstance(obj, BaseItem) and prop_name in obj.auth_props:
    #                 participants.append(QQmlProperty(obj.qobj, prop_name))
    #
    #     return event, participants


class PropDelegatorA(PropDelegator):
    
    def __get_subprop__(self, name):
        # e.g. xxx.width.color -> error
        raise AttributeError(
            'Illegal property: {}.{}!'.format(self.name, name),
            'This property ({}) doesn\'t support accessing secondary property '
            'from it.'.format(self.name),
            'Did you mean `PropDelegatorB` or `PropDelegatorC`?'
        )
    
    def __set_subprop__(self, name, value):
        # e.g. xxx.width.color = '#FFFFFF'
        raise AttributeError(
            'Illegal property: {}.{}!'.format(self.name, name),
            'This property ({}) doesn\'t support setting a secondary property '
            'value to it.'.format(self.name),
            'Did you mean `PropDelegatorB` or `PropDelegatorC`?'
        )


class PropDelegatorB(PropDelegator):
    
    def __get_subprop__(self, name) -> PropDelegatorA:
        # e.g. border.width -> PropDelegator(<border.width>)
        #             ^^^^^
        #             name
        return PropDelegatorA(self.prop.read(), name)
    
    def __set_subprop__(self, name, value):
        # e.g. border.width = 12
        #             ^^^^^   ^^
        #             name    value
        prop = self.__get_subprop__(name)
        if isinstance(value, PropDelegator):
            prop.write(value.read())
        else:
            prop.write(getattr(value, 'qobj', value))
    
    def read(self):
        return self


class PropDelegatorC(PropDelegator):
    
    def __get_subprop__(self, name):
        # e.g. anchors.top -> QQmlSideProp(<anchors.top>)
        return QmlSideProp(self.qobj, f'{self.name}.{name}')
    
    def __set_subprop__(self, name, value: 'QmlSideProp'):
        # e.g. anchors.top = xxx.anchors.bottom
        self.__get_subprop__(name).write(value)
        # t = self.__get_subprop__(name)
        # s = value
        # qmlside.bind_prop(t.qobj, t.prop_name, s.qobj, s.prop_name)
    
    def read(self):
        return self
    
    def write(self, value: 'QmlSideProp'):
        # e.g. anchors.write(xxx.anchors.top)
        raise AttributeError('Property not writable: {}'.format(self.name))


class QmlSideProp:
    
    def __init__(self, qobj: TQObject, prop_name: str, **kwargs):
        self.qobj = qobj
        self.prop_name = prop_name
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    def read(self):
        return qmlside.eval_js('{{0}}.{}'.format(
            convert_name_case(self.prop_name)
        ), self.qobj)
    
    def write(self, value: 'QmlSideProp'):
        t_obj, t_prop_name = self.qobj, self.prop_name
        if isinstance(value, QmlSideProp):
            s_obj, s_prop_name = value.qobj, value.prop_name
        elif hasattr(value, 'qobj'):
            s_obj, s_prop_name = value.qobj, ''
        else:
            s_obj, s_prop_name = convert_primitive_type(value), ''
        
        if t_prop_name == 'anchors.center_in':
            s_prop_name = ''
        elif t_prop_name == 'anchors.fill':
            pass
        elif t_prop_name.startswith('anchors.'):
            s_prop_name = s_prop_name.removeprefix('anchors.')
        
        qmlside.bind_prop(t_obj, t_prop_name, s_obj, s_prop_name)
        
    def __add__(self, other):
        return self.read() + other
    
    def __radd__(self, other):
        return other + self.read()


def adapt_delegator(qobj: TQObject, name: TPropName,
                    constructor: TConstructor) -> TDelegator:
    if type(constructor) is RealUnionType:
        # e.g. Union[float, PropDelegatorA]
        delegator = constructor.__args__[-1]  # -> PropDelegatorA
        #   we had an agreement that always put `type:TDelegator` in the last
        #   position of `TConstructor`. see reason at [TODO] and some
        #   implementation code at `..authorized_props.ItemProps`.
    else:
        # noinspection PyTypeChecker
        if issubclass(constructor, PropDelegator):
            # e.g. constructor is PropDelegatorA
            delegator = constructor
        else:
            # e.g. constructor is float
            delegator = PrimitivePropDelegator
    return delegator(qobj, name)
