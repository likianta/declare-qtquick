import re

from PySide6.QtQml import QQmlProperty

from ...typehint.qmlside import *
from ...typehint.widgets_support import *

""" what-is-prime-delegators-and-subprime-delegators.zh.md

`PrimePropDelegator` 用于代理 qml 中结构较为简单的属性. 例如: width, height, x,
y 等; `SubprimePropDelegator` 用于代理具有次级属性的 qml 属性, 例如 anchors
(anchors.fill, anchors.centerIn, anchors.top, etc.), font (font.pixelSize, font
.family, etc.).
"""


class AbstractDelegatorExpression:  # DELETE
    qobj: TQObject
    expression: str
    
    def __init__(self, qobj):
        self.qobj = qobj
        self.expression = ''
    
    # def _randomize_placeholders(self, expression: str):
    #     def _gen_random_slot_name():
    #         return 'x' + token_hex(8)
    
    def update(self, value: str):
        self.expression += value
        return self.expression


class PropDelegator:
    
    def __init__(self, qobj: TQObject, name: TPropName):
        self.qobj = qobj
        self.name = name
        self.prop = QQmlProperty(qobj, name)
    
    def __getattr__(self, item):
        if item == 'bind':
            raise NotImplemented('Binding method is not ready to use!')
            # if self.prop.hasNotifySignal():
            #     assert gstates.is_binding is False, (
            #         'The binding state is occupied by other Delegator'
            #     )
            #     gstates.is_binding = True
            # else:
            #     raise Exception(
            #         'Property not bindable!',
            #         self.qobj, self.name, self.prop.read()
            #     )
        return super().__getattribute__(item)
    
    def read(self):
        return self.prop.read()
    
    def write(self, value):
        self.prop.write(value)
    
    def kiss(self, value):
        # TODO: check whether `value` type immutable
        self.prop.write(value)
    
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
    
    @staticmethod
    def _extract_frame_info(frame):
        """
        Learning:
            source code of lk-logger
            
        TODO: much work (unittest & optimization) need to be done...
        """
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        file = open(filename, 'r', encoding='utf-8')
        source_line = file.read().splitlines()[lineno - 1]
        file.close()
        
        assert (m := re.match(r'^ +(?:\w+\.)+\.bind\(', source_line)), '''
            Your binding statement is too complex to analyse!
            In current verison (v0.1.x) we can only parse format likes
            `<some_qobj>.<property_name>.bind(<expression>)`.
            Here's the position error happened FYI:
                Filename: {}
                Lineno: {}
                Source Line: {}
        '''.format(filename, lineno, source_line)
        source_line_stem = source_line[m.span()[0]:]
        
        from lk_logger.scanner import get_all_blocks
        from ..base_item import BaseItem
        
        segs = source_line_stem[1:].split(',')
        segs[-1] = segs[-1].rstrip(', ')
        event = ''
        participants = []
        locals_ = frame.f_locals()
        for match0 in get_all_blocks(source_line_stem):
            event = match0.fulltext.strip()
            break
        for match in get_all_blocks(*segs, end_mark=','):
            obj_name, prop_name, *_ = match.fulltext.split('.')
            #   e.g. 'btn.x' -> 'btn'
            if obj_name in locals_:
                obj = locals_[obj_name]
                if isinstance(obj, BaseItem) and prop_name in obj.auth_props:
                    participants.append(QQmlProperty(obj.qobj, prop_name))
        
        return event, participants


class PrimePropDelegator(PropDelegator):
    pass


class SubprimePropDelegator(PropDelegator):
    
    def __getattr__(self, item):
        if item in super().__getattribute__('auth_props', ()):
            pass
        
        return super().__getattribute__(item)


def adapt_delegator(qobj, name, type_: TConstructor) -> TDelegator:
    if type_ is SubprimePropDelegator:
        return SubprimePropDelegator(qobj, name)
    else:
        return PrimePropDelegator(qobj, name)
