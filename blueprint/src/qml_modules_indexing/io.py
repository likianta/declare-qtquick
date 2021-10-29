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

# editable (change this to your qt path in your computer.)
qtdoc_dir = 'E:/programs/qt/qt6/Docs/Qt-6.1.3'
resources_dir = '../../resources'

# ------------------------------------------------------------------------------

no1 = (
    f'{resources_dir}/qtdoc/1_all_qml_modules.html',
    f'{resources_dir}/qtdoc_compiled/1_all_qml_modules.json'
)

no2 = (
    f'{resources_dir}/qtdoc/2_all_qml_types.html',
    f'{resources_dir}/qtdoc_compiled/2_all_qml_types.json'
)

no3 = (
    f'{resources_dir}/qtdoc_compiled/2_all_qml_types.json',
    f'{resources_dir}/qtdoc_compiled/3_all_qml_widgets.json'
)

no4 = (
    f'{resources_dir}/qtdoc_compiled/3_all_qml_widgets.json',
    f'{resources_dir}/qtdoc_compiled/4_all_pyml_widgets.json'
)

# ------------------------------------------------------------------------------

pass
