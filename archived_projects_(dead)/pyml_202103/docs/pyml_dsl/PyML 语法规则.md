# 概念定义

- 将 `comp MyComponent` (组件声明) 看作是一个 Python class, 很多行为可以从这个角度来理解

- 组件由属性的嵌套来定义, 组件的所有属性都是嵌套关系

    ```
    comp Rectangle:
        style:
            border:
                width: 1
                color: '#cccccc'
    ```

    - 属性通过缩进层级定义, 也可以通过 "级联符号" 定义和访问

    ```
    comp Rectangle:
        style:
            border.width: 1
            border.color: '#cccccc'
        on_completed ::
            print(self.border.color)  # -> '#cccccc'
            #   注: style 是 "伪属性", 所以不要写成 `self.style.border.color`
            #   关于伪属性会在后面语法定义章节详解
    ```

    - `on_{prop}` 在 QML 中是一个信号-槽结构, 但在 PyML 中同样可看作是一个 "属性":

    ```
    comp Text:
        text: 'Default text'
        
        on_text:
            enabled: False
        #   或者可以这样写: on_text.enabled: False
        
        on_text ::  # 注意二者的不同
            # 由于我们设置 enabled 为 False, 所以该信号不会被触发
            print('text has changed')
    ```

# 语法定义

## 组件

### 声明组件

声明一个组件类似于声明一个类 (在 Python 中的概念). 声明的组件如果没有被实例化, 则不会产生实例.

格式: `comp {qml_component}:` | `comp {custom_component}({qml_component}):`

```
import pyml.qtquick

comp Rectangle:
    pass
```

```
import pyml.qtquick

comp MyRectangle(Rectangle):
    pass
```

注:

1. 组件名字开头必须是大写字母
2. 组件名字前面不可以跟下划线, 即 `comp _Rectangle` 不受支持
3. 您必须先导入 QML 组件的命名空间, 才可以使用 / 继承 QML 组件. 例如, 在声明 `comp Button` 之前需要 `import qml.qtquick.controls`

### 实例化组件

格式: `{component}()` | `{component}(prop=value, ...)`

```
import pyml.qtquick.window


comp MyWindow(Window):
    style:
        visible: true
        width: 100
        height: 80


my_win = MyWindow()
print('This is a window instance:', my_win)

```

```
import pyml.qtquick.window


comp MyWindow(Window):
    style:
        visible: True
        width: 100
        height: 80


my_win = MyWindow(width=200, height=160, color='#f2f2f2')
print('This is a window instance:', my_win)

```

## 操作符

### 绑定或赋值

将值和属性绑定.

格式: `:` | `=`

```
comp A:
    attr:
        path: ''
```

```
comp A:
    attr:
        path = ''
```

注:

1. 当操作符右边是不可变类型时, 属性和值是 "赋值" 关系; 当操作符右边是可变类型时, 属性和值是 "绑定" 关系
2. 如果值里面包含其他属性的引用, 则一定是 "绑定" 关系
3. 赋值关系表示: 当属性或值改变时, 另一方不会变化
4. 绑定关系表示: 当值发生变化时, 属性会得到更新 (但反过来不会)

### 向左同步

格式: `<=`

```
comp A:
    style:
        width <= height
```

### 向右同步

格式: `=>`

```
comp A:
    style:
        width => height
```

注:

1. 仅支持简单的属性作为值. 例如 `width => height + radius` 是不允许的, 因为这意味着宽度变化时, 高度和弧度都要变化, 但它们缺乏明确的指导该如何变化. 此外 `width => height + 2` 在当前 PyML 版本 (<=1.x) 同样不受支持 (在未来可能提供有限度的支持)

### 双向同步

格式: `<=>` | `<==>`

```
comp A:
    style:
        width <=> height
```

注:

1. 仅支持简单的属性作为值. 例如 `width <=> height + radius` 是不允许的, 因为这意味着宽度变化时, 高度和弧度都要变化, 但它们缺乏明确的指导该如何变化. 此外 `width <=> height + 2` 在当前 PyML 版本 (<=1.x) 同样不受支持 (在未来可能提供有限度的支持)

### 静态赋值

始终将操作符右侧作为一次性赋值处理.

格式: `==`

```
comp A:
    style:
        width == height
```

注:

1. 它相当于:

    ```
    comp A:
        on_completed ::
            root.width = root.height
    ```

### 功能块

格式: `::`

```
comp Button:
    enabled ::
        return bool(parent.content.strip())
    text: 'Save'
    on_clicked ::
        with open(parent.file, 'w') as f:
            f.write(parent.content)
```

注:

1. 它相当于:

    ```
    comp Button:

        def _is_enabled(self, item):
            return bool(item.content.strip())

        def _click_event(self, item):
            with open(item.file, 'w') as f:
                f.write(item.content)

        enabled: _is_enabled(parent)
        text: 'Save'
        on_clicked:
            enabled: self.enabled
            emit: _click_event(parent)

    ```
    
2. 请注意区分 `:` 和 `::`

3. `::` 后跟的功能块必须有返回值, 当没有显式 `return` 时, 返回的是 None

4. 在功能块中, 所有外部属性必须通过组件 id 获取. 即:

    ```
    comp Button: @btn
        text: 'Save'
        on_clicked ::
            # 您在代码块中, 必须使用组件 id 来访问组件属性.
            # 特殊 id 有: root, parent, self
            # 自定义 id 有 (本示例中): btn
            print(btn.text)  # or: print(self.text)
    ```

5. 功能块可类比于 Python 中的 `def(self, ...)` (类方法) 来理解. 不同的是, 类方法传的是 `def(self)`, 功能块默认可 **直接** 访问到组件中的 id

## 属性

### 属性的定义

属性用来描述组件是怎样的, 是做什么的.

属性分为内置属性, 附加属性, 伪属性和自定义属性.

### 属性的表示方式

属性支持嵌套表示和级联符号表示.

示例:

```
comp Rectangle:
    style:
        width: 100
        height: 80
        border:
            width: 1
            color: 'gray'
```

```
comp Rectangle:
    style:
        width: 100
        height: 80
        border.width: 1
        border.color: 'gray'
```

### 内置属性

内置属性由组件类型决定, 当您导入或继承 QML 组件时, 可以使用 QML 组件的内置属性 (通过 Qt 助手手册可查询).

例如, `pyml.qtquick.controls.Button` 的内置属性有: `width`, `height`, `text`, `background` 等.

### 附加属性

附加属性以 'on_' 开头, 后跟一个常规属性的名字, 用来表示当此 (常规) 属性发生改变, 或某状态被激活时的动作.

附加属性可以通过 `:` 或 `.` 来访问它的级联属性:

```
comp Text:
    text: 'Default text'
    on_text:
        enabled: True
        emit: some_event_function()
```

```
comp Text:
    text: 'Default text'
    on_text.enabled: True
    on_text.emit: some_event_function()
```

附加属性通常后跟 `::` 开启一个功能块:

```
comp Text:
    text: 'Default text'
    on_text ::
        print('Text has changed! New text is: ' + self.text)
```

特殊的附加属性有:

- `on_completed`: 表示当组件实例化完成时
- `on_keyevent`: 表示响应一个按键事件

*(具体可参考 QML 对 `Component.onCompleted` 的说明.)*

### 伪属性

伪属性是 PyML 特有的一种属性类型.

PyML 的伪属性有:

- `attr`: 表示声明一个组件成员 (变量). 相当于 QML 的 `property var xxx`
- `style`: 定义组件的风格
- `children`: 统一定义组件的 (一级) 子组件的基础风格
  - 您可以通过 `children:    inherit: True` 使控制所有子孙组件

示例:

```
comp Column: @col
    style:
        spacing: 10
        width: 100
        height: 300
    children:
        color: 'white'
        width: self.width  # 这里的 self 指的是 col
        height: 30
    
    Rectangle:
        style:
            pass  # 全部继承 col.children (伪属性中) 定义的风格

    Rectangle:
        style:  # 您可以在 col.children 的风格基础上覆写和扩展属性
            color: 'gray'
            height: 'fill'

```

注意:

1. PyML 的伪属性没有 "级联属性" 概念, 所以它不能通过 `.` 访问, 为了在写法上明确这种区别, 我们定义空格作为它的单行式. 示例:

    ```
    comp Rectangle:
        attr active: False
        attr path: ''
        style width: 100
        style height: 80
        style border.width: 1
        style border.color: '#cccccc'
    ```

2. 当外部要访问伪属性的子属性时, 不需要通过伪属性级联访问 (因为它没有级联的概念), 而是直接访问到. 示例:

    ```
    comp Rectangle:
        style border.width: 1
        
        Text:
            text: 'Border length: ' + str(parent.border.width)
            #   注意不要写成 `parent.style.border.width`
            style:
                pos: 'center'
    ```

3. 那么可以不通过伪属性来定义自己的属性吗? 这是一个有争议的话题, 目前的初步结论是:

    1. `style` 是非必须的. 即写成 `style width: 10` 和 `width: 10`都可以
    2. `attr` 是必须的. 即必须通过 `attr my_var: dict` 来声明一个自定义属性, 而不能直接用 `my_var: dict` 声明
    3. `children` 是必须的

    我们推荐的做法仍然是: 请积极使用伪属性的写法. 即便 `style` 不是必须的, 但它有利于编译器检查, 提前发现错误, 以及保持代码的格式一致性.

    > `style` 的争议性来源于这样的讨论: 我该怎么确定某个属性是不是一个 "风格"? 如果我认为一个叫 `width` 的内置属性不属于风格, 我可不可以把它放到 `style` 之外定义?
    > 
    > `style` 并不是一个具有强约束力的伪属性, 甚至在当前 PyML 版本 (<=1.x) 中也不具备编译期的检查功能; 它只是推荐您把样式相关的属性放在一起定义, 以便于从 PyML 代码中区分开哪些是视图的属性, 哪些是业务属性.

### 属性覆写

当我们继承了某个组件或某个属性集时, 我们如有需要修改 / 扩展 / 删除继承来的属性定义, 则通过属性覆写实现.

```
comp A:
    style:
        width: 100
        height: 80

comp B(A):
    style:
        height: 30
```

```
comp A:
    style:
        width: 100
        height: 80
        radius: 4

    B:
        style: parent.style
            height: 30     # edit
            pos: 'center'  # add
            del radius     # delete (即使不删除, 也不会报错, PyML 会忽略无效属性)
```
