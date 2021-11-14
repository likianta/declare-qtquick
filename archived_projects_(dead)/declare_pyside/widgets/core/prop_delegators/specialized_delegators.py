from lk_logger import lk

from .base_delegators import PropDelegatorB
from .base_delegators import PropDelegatorC
from .base_delegators import QmlSideProp


class AnchorsDelegator(PropDelegatorC):
    
    def __set_subprop__(self, name, value: QmlSideProp):
        setattr(self.qobj, '_is_anchored', True)
        super().__set_subprop__(name, value)


class DragDelegator(PropDelegatorB):
    
    def __set_subprop__(self, name, value):
        if name == 'target':
            if getattr(value.qobj, '_is_anchored', False):
                lk.logt(
                    '[W3833]',
                    'MouseArea.drag won\'t be effected because the target '
                    'object is constraint by its anchors', value.qobj,
                    h='grand_parent'
                )
        super().__set_subprop__(name, value)
