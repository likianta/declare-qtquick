import QtQuick
import QtQuick.Window
import LKQmlSide

Window {
    id: root
    objectName: 'declare_pyside.widgets.window.Window:MainWindow'
    width: 600
    height: 400
    color: '#F2F2F2'
    visible: true

    QmlSide {
        id: qmlside
    }

    Component.onCompleted: {
        console.log('register qmlside object (from MainWindow)')
        pyside.call('__register_qmlside_object', qmlside)
        pyside.call('__build', root)
    }
}
