"""
# Preparation

1. Install Qt application (Qt 6 is recommended).
2. Edit variable `qtdoc_dir` path to be the qt path in your computer:
        qtdoc_dir = `<qt>/Docs/Qt-<your_qt_version>`
   For example:
        qtdoc_dir = 'E:/programs/qt/qt6/Docs/Qt-6.1.3'
3. Copy `<qtdoc_dir>/qtdoc/modules-qml.html` to `<resources_dir>/qtdoc/1_all_qml
   _modules.html`.
4. Copy `<qtdoc_dir>/qtdoc/qmltypes.html` to `<resources_dir>/qtdoc/2_all_qml
   _types.html`.
5. Finished. Now you can start running `./main.py`.
"""
from os.path import dirname
from os.path import abspath

_curr_dir = dirname(__file__)
_proj_dir = abspath(_curr_dir + '/../..').replace('\\', '/')

# editable (change this to your qt path in your computer.)
qtdoc_dir = 'E:/programs/qt/qt6/Docs/Qt-6.1.3'
resources_dir = f'{_proj_dir}/blueprint/resources'
widgets_dir = f'{_proj_dir}/declare_qtquick/widgets/api'

html_1 = f'{resources_dir}/qtdoc/1_all_qml_modules.html'
html_2 = f'{resources_dir}/qtdoc/2_all_qml_types.html'

json_1 = f'{resources_dir}/qtdoc/1_all_qml_modules.json'
json_2 = f'{resources_dir}/qtdoc/2_all_qml_types.json'
json_3 = f'{resources_dir}/qtdoc_compiled/3_all_qml_widgets.json'
json_4 = f'{resources_dir}/qtdoc_compiled/4_all_pyml_widgets.json'

text_1 = f'{resources_dir}/widgets_template/__init__.py'
text_2 = f'{resources_dir}/widgets_template/__base__.py'
text_3 = f'{resources_dir}/widgets_template/__list__.py'

no1 = (html_1, json_1)
no2 = (html_2, json_2)
no3 = (json_2, json_3)
no4 = (json_3, json_4)
