from secrets import token_hex
from textwrap import dedent

from PySide6.QtCore import QObject
from PySide6.QtQml import QQmlComponent
from lk_logger import lk

from .__ext__ import *


def setup():  # setup a listener for laterly registering qmlside core.
    def register_qmlside(obj: T.QObject):
        global qmlside
        qmlside.init_core(obj)
        lk.logt('[I0557]', 'registered qmlside object', obj.objectName())
    
    from ..pyside import pyside
    pyside.register(register_qmlside, '__register_qmlside_object')


class QmlSide(QObject):
    qmlfile = common.current_locate('qmlside.qml')
    _core: T.JsEvaluatorCore
    _component_cache = {}  # type: T.ComponentCache
    
    def init_core(self, qobj):
        self._core = qobj
    
    def bind_prop(self,
                  t_obj: T.QObject, t_prop_name: T.PropName,
                  s_obj: T.QObject, s_prop_name: T.PropName):
        # `s -> t`, as known as `t = s`
        expression = '{} = Qt.binding(() => {})'.format(
            f't_obj.{common.convert_name_case(t_prop_name)}',
            f's_obj.{common.convert_name_case(s_prop_name)}'.rstrip('.'),
        )
        lk.loga(expression, h='parent')
        self._core.bind(t_obj, s_obj, expression)
    
    def connect_prop(self, r: T.Receptor, s: T.Sender):
        pass
    
    def connect_func(self, r: T.Receptor, func: T.Callable,
                     s_group: T.Iterator[T.Sender]):
        
        func_id = func.__name__ + '_' + token_hex(8)
        pyside.register(func, func_id)
        
        args = [r[0], [s[0] for s in s_group]]
        
        self._core.eval_js(
            dedent('''
                {r_obj}.{r_prop} = Qt.binding(
                    () => PySide.call({func_id}, {s_group})
                )
            ''').format(
                r_obj='args[0]',
                r_prop=r[1],
                func_id=func_id,
                s_group=[
                    f'args[{i}].{prop}'
                    for i, (_, prop) in enumerate(s_group, 1)
                ]
            ),
            args,
        )
    
    def create_component(
            self, qmlfile: T.QmlFile, save_cache=False
    ) -> T.Component:
        if qmlfile in self._component_cache:
            return self._component_cache[qmlfile]
        else:
            comp = QQmlComponent(app.engine, qmlfile)
            if save_cache:
                self._component_cache[qmlfile] = comp
            return comp
    
    def create_qobject(self,
                       component: T.Component,
                       container: T.QObject) -> T.QObject:
        qobj = self._core.create_object(component, container)
        #   the component type is TComponent, but when `self._core
        #   .create_object` -- which is defined in `declare_pyside/qmlside
        #   /LKQmlSide/QmlSide.qml:<function:create_object>` -- is called,
        #   TComponent will be implicitly translated to `QML:Component` type.
        return qobj
    
    def eval_js(self, code, *args):
        lk.loga(code, len(args), h='parent')
        return self._core.eval_js(
            code.format(*(f'args[{i}]' for i in range(len(args)))), list(args)
        )


qmlside = QmlSide()
