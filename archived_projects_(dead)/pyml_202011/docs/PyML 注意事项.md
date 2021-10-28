# 当前版本 (0.1.x) 局限性

1. 不支持嵌套声明组件

    ```
    comp A:
        comp B:  # <- 不支持!
            pass
    ```

2. 不能正确处理 Python Annotation 语法, 会被当做赋值

    ```
    # python
    class A:
        a: str
        def __init__(self):
            print(self.a is str)
            # -> AttributeError: 'A' object has no attribute 'a'
    
    # pyml
    comp A:
        attr a: str
        on_completed ::
            print(self.a is str)  # -> True
    
    ```

3. 当发生运行时报错, 不能反射定位到 pyml 代码中. 这意味着您在调试时会很困难 (将在下个版本尽快解决)

4. 对有歧义的命名不会报错, 但会造成解析时关联错乱

    ```
    comp A:
        width: 200
        CompB:
            width: root.width  # 200
        CompC: @root    # <- 问题: root 是保留字, 仅用于根组件. 若采用相同的命
            width: 100  #    名, 考虑到 pyml 从上到下的解析顺序, CompB 的宽度会
                        #    变成 200, CompD 的宽度会变成 100. 且在解析到 CompC 
                        #    时, root 会从根组件转向 CompC.
        CompD:
            width: root.width  # 100
    ```

5. 仅支持空格表示的缩进, 且缩进量必须是 0 或 4 的整数倍数 (括号内除外)

    ```
    comp A:          # <- 正确示范
        width: 200   #    正确示范
        height: 100  #    正确示范
    #   ^ 以空格作为缩进, 缩进量是 0, 4, 8, 12, ...
    
        on_completed ::
            a = (12 + 
                 24) * 2
            #    ^ 括号内不需要遵守上述规则
   
      Comp B:  # <- 错误示范
        pass   #    错误示范
    # ^ 缩进量不符合规则!

    ```

6. PyML 尝试通过命名的大小写格式来辅助判断组件类型, 因此请确保:

    1. 组件命名 (包括自定义组件) 使用大写字母开头, 且长度在两个及以上 (不允许在开头字母前加下划线)
    
    2. 属性命名 (包括自定义属性) 使用小写字母开头 (允许在开头字母前加下划线)

7. 一种错误的属性书写

    ```
    comp A:
        # wrong
        width, height = 200, 100
    
    comp B:
        # right (1)
        width: 200
        height: 100
   
    comp C:
        # right (2)
        on_completed ::
            width, height = 200, 100
        
    ```

--------------------------------------------------------------------------------

# 哪些情况会导致 pyml 编译时不报错, 运行时报错

举个例子:

```pyml
import pyml.qtquick.window

comp 123Window(Window): @win  # 1. QML 不允许数字开头的组件命名
    width :: height
        height ++  # 2. Python 不支持 `num++` 语法
        return height

```

pyml 对这种情况在编译时不报错, 但程序运行时会报 QML/Python 语法错误.

这是因为, pyml 只对自己的语法规则做严格要求, 以 **保证能够依据 pyml 语法顺利生成 .qml 和 .py 文件**. 至于生成的代码能否运行, 那是 QML 和 Python 的事情.

PS: 对于上述示例, pyml 将生成以下代码:

```qml
// 123Window.qml
import QtQuick.Window 2.15

Window {
    id: win
    width: PyML.call('method_230410', win)
}

```

```python
from pyml.core import PyMLCore


class PyML(PyMLCore):
    
    def method_230410(self, win):
        prop0 = win.property('height')
        prop0 ++
        win.setProperty('height', prop0)
        return prop0

```
