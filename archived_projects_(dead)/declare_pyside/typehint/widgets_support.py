from typing import *

from .common import TFakeModule

if __name__ == '__main__':
    from declare_pyside.widgets.core.prop_delegators \
        import base_delegators as _delegators
else:
    _delegators = TFakeModule

# ------------------------------------------------------------------------------
# `declare_pyside/widgets/core/delegators.py`

TPrimitive = Union[None, bool, float, int, str]
TDelegator = Union[_delegators.PropDelegator, _delegators.PrimitiveDelegator]
TConstructor = Union[TPrimitive, TDelegator]

# ------------------------------------------------------------------------------
# `declare_pyside/widgets/core/authorized_props.py`

TPropName = str
TAuthProps = dict[TPropName, TConstructor]
