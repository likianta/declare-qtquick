""" 术语说明

* package: 包名. 例如: 'pyml.qtquick', 'pyml.qtquick.windows', 'pyml.qtquick
  .controls'
* component: 组件名. 例如: 'Item', 'Rectangle', 'MouseArea'
* props: 组件属性. 例如: 'border', 'border.width', 'color'
"""
from blueprint.qml_modules_indexing import no1_all_qml_modules
from blueprint.qml_modules_indexing import no2_all_qml_types
from blueprint.qml_modules_indexing import no3_all_qml_widgets
from blueprint.qml_modules_indexing import no4_all_pyml_widgets

"""
注: 下面的每个脚本都可以单独运行. 也可以通过本脚本一并执行.
"""

no1_all_qml_modules.main(
    '../resources/no1_all_qml_modules.html',
    '../resources/no2_all_qml_modules.json'
)

no2_all_qml_types.main(
    '../resources/no3_all_qml_types.html',
    '../resources/no4_all_qml_types.json'
)

no3_all_qml_widgets.main(
    '../resources/no4_all_qml_types.json',
    '../resources/no5_all_qml_widgets.json',
    'E:/programs/qt/qt6/Docs/Qt-6.1.3'  # edit this
)

no4_all_pyml_widgets.main(
    '../resources/no5_all_qml_widgets.json',
    '../resources/no6_all_pyml_widgets.json'
)
