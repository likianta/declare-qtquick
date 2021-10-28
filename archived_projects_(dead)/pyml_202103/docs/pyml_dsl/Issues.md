# Composer 实现难点

## 代理属性

```pyml
comp Text:
    text: parent.border.color.replace('#', '')
    """ 我希望生成的 qml 格式为:
            text: PyML.py_eval(
                "args[0].replace(('#', ''))",
                parent.border.color
            )
        如何才能让 Composer 知道, `parent.border.color` 是一个属性呢?
    """
```

目前的解决方法: 列出所有受支持的属性, 如果符合, 则合并; 不符合则结束并提交:

```
text: parent.border.color.replace('#', '')
    1. parent -> 关键字
    2. border -> style 属性
    3. color -> border 的属性
    4. replace -> 不是 color 的属性, 结束, 并将前述 `parent.border.color` 提交
```
