# How composer works?

## 示例

```
# pyml
import pyml.qtquick
import pyml.qtquick.controls
import pyml.qtquick.window


comp Window:
    visible: True
    size: (800, 600)

    <attr>
        active: False
        cmd: {'btn': 'start'}
        tip: ''

    <layout>
        size: 'fill'

    def test_func(win):
        win.tip = ''
        win.active = False
        win.cmd.clear()
        win.cmd['btn'] = 'over'
    
    Rectangle:
        Button:
            text: cmd['btn']
            on_clicked: test_func(root)
        Text:
            <style>
                anchor: 
                    top: last_comp.bottom
                    right: parent.right
            text <= tip + '!'
            on_text:
                cmd['btn'] = 'exit'


if __name__ == '__main__':
    from pyml.core import Application
    with Application as app:
        win = Window()
        win.show()


// -> generated qml code
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15


Window {
    id: root
    visible: true
    width: 800
    height: 600

    property string tip: ''
    property bool active: false
    property var cmd: {'btn': 'start'}

    Rectangle {
        anchors.fill: parent
        Button {
            text: cmd['btn']
            onClicked: {
                PyML.call('reset_20201030_165540', root)
            }
        }
    }
}


# -> generated python code
from pyml.core import PyMLCore


class Window(PyMLCore):
    
    def reset_20201030_165540(self, win):
        win = self.proxy_qobject(win)
        
        prop = win.get('tip')
        prop = ''
        win.set('tip', prop)

        prop = win.get('active')
        prop = False
        win.set('active', prop)

        prop = win.get('cmd')
        prop['btn'] = 'over'
        win.set('cmd', prop)


if __name__ == '__main__':
    from pyml.core import Application
    with Application as app:
        win = Window(app)
        win.show()

```

