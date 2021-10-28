# PyML

PyML (Python Markup Language) lets you write QML-like code in pure Python way.

You keep both declarative programming style and Python syntax (means it also works well with Pycharm Intellisense and so on), no need to write QML code, because PyML will generate them in runtime.

Here is a "Hello World" written in PyML:

```py
# hello_world.py
from lk_lambdex import lambdex  # pip install lk-lambdex

from pyml.core import app
from pyml.keywords import this, parent, true, false
from pyml.widgets import MouseArea, Rectangle, Text
from pyml.widgets.window import Window


def build():
    with Window() as win:
        win.color = '#cccccc'
        win.size = (600, 800)
        win.visible = true

        with Rectangle() as rect:
            rect.anchors.fill = parent
            rect.anchors.margins = 10
            rect.color = 'white'
            rect.radius = 12
            
            with Text() as txt:
                txt.anchors.center = parent.center
                txt.text = 'Hello World!'

            with MouseArea() as area:
                area.anchors.fill = parent
                area.on_clicked.connect(lambdex((), '''
                    txt.text = 'Hello PyML!'
                '''))

        return win


if __name__ == '__main__':
    win = build()
    app.start(win)

```

--------------------------------------------------------------------------------

<!-- delete below -->

# PyML 是什么?

PyML (Python Markup Language) 是 Python 版的 QML, 可在声明式 UI 中引用 Python 的模块.

PyML 受 enaml 启发而诞生, 与 enaml 有诸多相似之处, 但它看起来更像 yaml 风格.

PyML 糅合了 qml, enaml, kv lang 中的一些特色语法, 写出来的代码看起来长这样:

**示例: 矩形缩放动画**

```pyml
import pyml.qtquick
import pyml.qtquick.window


comp MyWindow(Window): @win  # 使用 `@win` 声明一个 id (`id: win` 同样支持)
    visible: True
    color: '#cccccc'
    width: 600
    height: 800

    Item: @container
        attr active: False  # `attr` 声明一个自定义属性
        margin: 20
        size: 'fill'
        #   1. `size` 是 `(width, height)` 的代理
        #   2. `'fill'` 表示设置宽高与父组件一致
        #   3. `size` 支持的类型有: 
        #       1. str: 'fill', 'ifill', 'ofill', 'wrap', 'iwrap', 'owrap' 
        #       2. size: `parent.size`, etc. 
        #       3. tuple: `(width, height)`, `width, height` 
        #       4. list: `[width, height]` 
        #       5. *iter: `*{'width': w, 'height': h}.values()`, etc.

        Rectangle:
            width: 100
            height: 200
            color: '#ffffff'
            radius: 8
            border.width: 1
            border.color: '#cccccc'
            anim:  # 对动画属性做了简化
                NumberAnimation:
                    when: container.active
                    props:
                        width: parent.width
                        height: parent.height
                    duration: 1000
            Text:
                pos: 'center'
                text: 'Hello World'
            MouseArea:
                size: 'fill'
                on_clicked ::
                    state = container.active = !container.active
                    print('{} animating'.format(
                        'Release' if state is True else 'Withdraw'
                    ))


if __name__ == '__main__':
    from pyml.core import Application
    with Application() as app:
        win = MyWindow()
        win.show()
        app.start()

```

![](gallery/pyml_intro.gif)
