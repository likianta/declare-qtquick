# 历史遗留问题说明

## 关于项目命名混乱

在验证多条技术路线时期, 我创建了多个名称类似的仓库. 如下列表是已存在的命名:

- declare-qt
- declare-qtquick (当前项目)
- declare-qml
- declare-pyside

现在我决定只保留 `declare-qt` 和 `declare-qtquick` 两个项目. 其他项目将被存档并从仓库中移除.

关于 `declare-qt` 和 `declare-qtquick` 的区别如下:

`declare-qt` 将专注于为 QtWidgets 创建声明式的语法结构, 并提供一些类似 QML 的简化写法加速开发.

`declare-qtquick` 将专注于用纯 Python 语法替代 QML, 同样提供声明式的语法结构, 最终的产物是 QML 对象.
