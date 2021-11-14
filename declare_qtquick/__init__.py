try:
    def _setup():
        
        def _setup_pyside():
            from .application import app
            from .pyside import pyside
            app.register_pyobj(pyside, 'pyside')
            app.register_pyobj(pyside, 'PySide')
            
        def _setup_qmlside():
            from .qmlside.qlogger import setup as setup1
            from .qmlside.qmlside import setup as setup2
            setup1()
            setup2()
        
        def _setup_widgets_api():
            from os.path import abspath
            from sys import path as syspath
            """
            Caution.zh:
                我们需要先在这里, 将 "widgets/namespace" 文件夹加入到 sys.path
                中, 这样 "widgets/api" 目录才可以使用 "widgets/namespace" 目录
                下的 `__declare_qtquick_internals__` 模块.
                需要注意的是, 我们不能使用相对导入来调用
                `__declare_qtquick_internals__`, 比如会出现下面这种情况:
                    from .namespace import __declare_qtquick_internals__
                    setattr(__declare_qtquick_internals__, 'xxx', True)
                当其他模块通过绝对导入调用时, 会发现找不到 'xxx' 属性:
                    from __declare_qtquick_internals__ import xxx
                    # AttributeError: <module> object has no attribute 'xxx'
            """
            # this file will be added to sys.path, to provide itself to
            # `../api/<all_widgets>:<use_absolute_imports_safely>`.
            syspath.append(abspath(f'{__file__}/../widgets/namespace'))
            
            from . import properties
            from .typehint import prop_hint
            from .widgets import Component
            from .widgets import widget_sheet
            # here we must use absolute import, see reason in docstring above.
            from __declare_qtquick_internals__ import setup
            setup(component=Component,
                  properties=properties,
                  prop_hint=prop_hint,
                  widgets_sheet=widget_sheet)
            
        _setup_pyside()
        _setup_qmlside()
        _setup_widgets_api()
    
    
    _setup()

except Exception as e:
    raise e

else:
    from . import widgets
    from .application import Application
    from .pyside import pyside
    from .pyside import reg
    from .qmlside import hot_loader
    from .qmlside import qmlside
    from .widgets.api import *

finally:
    del _setup

__version__ = '0.2.0'
