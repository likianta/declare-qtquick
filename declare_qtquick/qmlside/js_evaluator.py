from PySide6.QtQml import QQmlComponent
from lk_logger import lk

from .__ext__ import TJsEvaluatorCore
from .__ext__ import app
from .__ext__ import current_locate


class JsEvaluator:
    core: TJsEvaluatorCore
    
    def __init__(self):
        component = QQmlComponent(
            app.engine, current_locate('js_evaluator_controls.qml'))
        qobject = component.create()
        self.core = qobject
        
        # activate `self.core`.
        # FIXME: the following line is very necessary, if we comment this line,
        #   `.layout_helper.LKLayoutHelper.quick_anchors.<usage:eval_js(...)>`
        #   will raise an error says "AttributeError: 'PySide6.QtQuick
        #   .QQuickItem' object has no attribute 'eval_js'". i don't know why
        #   does it happen, unless we instantly call at least once `self.core
        #   .eval_js` here, that problem will be gone.
        lk.log(self.core.eval_js('"JsEvaluator.core is ready to use"', []))
    
    def quick_bind(self, a_obj, a_prop, b_obj, b_prop):
        self.eval_js('{{0}}.{} = Qt.binding(() => {{1}}.{})'.format(
            a_prop, b_prop
        ), a_obj, b_obj)
    
    def eval_js(self, code, *args):
        # lk.log(code.format(
        #     *(f'<QObject#{i}>' if isinstance(x, QObject)
        #       else str(x) for i, x in enumerate(args))), h='parent'
        # )
        # lk.logt('[D3345]', code)
        return self.core.eval_js(
            code.format(*(f'args[{i}]' for i in range(len(args)))),
            list(args)
        )


js_eval = JsEvaluator()
eval_js = js_eval.eval_js
