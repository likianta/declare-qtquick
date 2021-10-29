""" 术语说明

* package: 包名. 例如: 'pyml.qtquick', 'pyml.qtquick.windows', 'pyml.qtquick
  .controls'
* component: 组件名. 例如: 'Item', 'Rectangle', 'MouseArea'
* props: 组件属性. 例如: 'border', 'border.width', 'color'
"""
from blueprint.src.qml_modules_indexing import io
from blueprint.src.qml_modules_indexing import no1_all_qml_modules
from blueprint.src.qml_modules_indexing import no2_all_qml_types
from blueprint.src.qml_modules_indexing import no3_all_qml_widgets
from blueprint.src.qml_modules_indexing import no4_all_pyml_widgets

"""
注: 下面的每个脚本都可以单独运行. 也可以通过本脚本一并执行.
"""

no1_all_qml_modules.main(*io.no1)
no2_all_qml_types.main(*io.no2)
no3_all_qml_widgets.main(*io.no3, io.qtdoc_dir)
no4_all_pyml_widgets.main(*io.no4)
