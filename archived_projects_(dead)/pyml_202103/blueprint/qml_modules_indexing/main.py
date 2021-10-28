""" README

# 术语说明

* package: 包名. 例如: 'pyml.qtquick', 'pyml.qtquick.windows', 'pyml.qtquick
  .controls'
* component: 组件名. 例如: 'Item', 'Rectangle', 'MouseArea'
* props: 'properties' 组件的属性. 例如: 'border', 'border.width', 'color'
"""
from blueprint.qml_modules_indexing import no1_all_qml_modules
from blueprint.qml_modules_indexing import no2_all_qml_types
from blueprint.qml_modules_indexing import no3_all_qml_props
from blueprint.qml_modules_indexing import no4_generate_pyml_data

no1_all_qml_modules.main(
    '../resources/no1_all_qml_modules.html',
    '../resources/no2_all_qml_modules.json'
)

no2_all_qml_types.main(
    '../resources/no3_all_qml_types.html',
    '../resources/no4_all_qml_types.json'
)

no3_all_qml_props.main(
    '../resources/no4_all_qml_types.json',
    '../resources/no5_all_qml_props.json',
    'D:/programs/qt/qt_5.14.2/Docs/Qt-5.14.2'
)

no4_generate_pyml_data.main(
    '../resources/no5_all_qml_props.json',
    '../resources/no6_pyml_namespaces.json'
)
