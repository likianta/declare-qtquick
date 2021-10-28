## 不要使用 style 中定义的属性

```pyml
comp Rectangle:
    style:
        width: 100
    width: 'my width'  # Error: 你不能自定义一个叫做 'width' 的变量, 因为这与 
    #   style 中的 width 属性产生混淆.

    Text:
        text: str(parent.width) + 'px'  # 我们使用 `parent.width` 引用 parent 的
        #   style 中的 width 属性. 而不是用 `parent.style.width`.

```
