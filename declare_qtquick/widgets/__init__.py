from .base import Component

try:
    
    def _setup():
        """
        Caution.zh:
            我们需要先在这里, 将 "namespace" 文件夹加入到 sys.path 中, 这样
            "api" 目录才可以使用 "namespace" 目录下的
            `__declare_qtquick_internals__` 模块.
            需要注意的是, 我们不能使用相对导入来调用
            `__declare_qtquick_internals__`, 比如会出现下面这种情况:
                from .namespace import __declare_qtquick_internals__
                setattr(__declare_qtquick_internals__, 'xxx', True)
            当其他模块通过绝对导入调用时, 会发现找不到 'xxx' 属性:
                from __declare_qtquick_internals__ import xxx
                # AttributeError: <module> object has no attribute 'xxx'
        """
        from os.path import abspath
        from sys import path as syspath
        
        from . import widget_sheet
        from .. import properties
        from ..typehint import prop_hint
        
        # this file will be added to sys.path, to provide itself to
        # `../api/<all_widgets>:<use_absolute_imports_safely>`.
        syspath.append(abspath(f'{__file__}/../namespace'))
        
        # here we must use absolute import, see reason in docstring above.
        from __declare_qtquick_internals__ import setup
        
        setup(component=Component,
              properties=properties,
              prop_hint=prop_hint,
              widgets_sheet=widget_sheet)
    
    
    _setup()

except Exception as e:
    raise e

else:
    from .api import *
