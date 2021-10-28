# 设计思考: UID 为什么要以 class 形式存在, 而不直接用 str 表示?

**为什么**

1. 从 uid 获取 parent_id, 可通过 UID.parent_id 属性
2. 从 uid 获取层级信息, 可通过 UID.layer_level 属性

**为什么不**

1. uid 如果是 str, 那么在转换为 qml code 时:

    ```python
    with Item() as a:
        with Item() as b:
            b.anchors.fill = a
            #   在 pyml 的设计中, 该语句会令 b.anchors.fill 指向 a 的 uid. 如果
            #   uid 是 str, 那么在 b.build 的传统处理中, 会给 str 包裹双引号, 就
            #   会生成这样的源代码:
            #       Item {
            #           id: com_0x1_01
            #           Item {
            #               id: com_0x1_01_01
            #               anchors.fill: "com_0x1_01"
            #               //            ^----------^
            #               //            错误! 不可以对 id 用引号
            #           }
            #       }
            #   解决 b.build 的处理方式并不困难, 但它不符合当前的设计需要.
    ```
