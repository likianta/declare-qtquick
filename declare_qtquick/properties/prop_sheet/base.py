"""
README:
    See full documentation in `docs/how-does-prop-sheet-work.md`.
"""
# noinspection PyUnresolvedReferences,PyProtectedMember
from typing import _UnionGenericAlias as RealUnionType

from .__ext__ import Delegate
from .__ext__ import T


class PropSheet:
    pass


def init_prop_sheet(target: T.Target, prefix=''):
    """
    References:
        https://stackoverflow.com/questions/2611892/how-to-get-the-parents-of-a
        -python-class
    """
    assert all((
        hasattr(target, 'qid'),
        # hasattr(target, 'name'),
        hasattr(target, '_properties'),
    ))
    
    bases = target.__class__.__bases__
    assert len(bases) > 1 and issubclass(bases[-1], PropSheet)
    #   ^ assert 2+           ^ assert target's mixin classes[-1] is PropSheet
    
    for prop_name, constructor in _get_all_props(bases[-1]):
        # noinspection PyProtectedMember
        target._properties[prop_name] = constructor(
            target.qid,
            prefix + '.' + prop_name if prefix else prop_name
            #   ^ e.g. 'anchors.top'                ^ e.g. 'width'
        )


def _get_all_props(target_class: T.PropSheet) -> T.PropsIter:
    if target_class is PropSheet:
        raise Exception(
            'This function should be used in subclass of `PropSheet`!'
        )
    for cls in _get_all_super_classes(target_class):
        for k, v in cls.__annotations__.items():
            if not k.startswith('_'):
                prop_name = k
                constructor = _get_prop_constructor(v)
                yield prop_name, constructor


def _get_all_super_classes(cls: T.PropSheet) -> T.PropSheetIter:
    """
    Examples:
        class PropSheet:
            pass
            
        class AAA(PropSheet):
            pass
            
        class BBB(AAA):
            pass
            
        for cls in PropSheet._get_all_super_classes():
            pass  # -> got nothing
            
        for cls in AAA._get_all_super_classes():
            pass  # -> got AAA
            
        for cls in BBB._get_all_super_classes():
            pass  # -> got BBB, AAA
    
    Yields:
        subclass inherits from PropSheet.
    """
    temp_cls = cls
    while issubclass(temp_cls, PropSheet):
        yield temp_cls
        temp_cls = temp_cls.__base__


def _get_prop_constructor(raw_type: T.RawType) -> T.Constructable:
    if type(raw_type) is RealUnionType:
        # e.g. Union[float, Number]
        constructor = raw_type.__args__[-1]
        if constructor is Delegate:
            constructor = lambda qid, name: Delegate(
                qid, name, delegate=raw_type.__args__[-2]
            )
    else:
        constructor = raw_type
    return constructor
