## 在矩形中居中显示一串文字, 点击矩形, 文字发生变化

```qml
import QtQuick 2.15

Rectangle {
    width: 100
    height: 100

    Text {
        id: txt
        anchors.centerIn: parent
        text: 'The default state'
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            txt.text = 'You clicked me!'
        }
    }
}
```

```pyml
import pyml.qtquick


comp Rectangle:
    size: (100, 100)
    
    Text: @txt
        pos: 'center'
        text: 'The default state'
    
    MouseArea:
        size: 'fill'
        on_clicked ::
            txt.text = 'You clicked me!'

```

## 子组件对齐于父组件的左上右三边

```qml
import QtQuick 2.15

Rectangle {
    width: 100
    height: 100

    Rectangle {
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.right: parent.right
        width: 30
        height: 30
        color: 'yellow'
    }
}
```

```pyml
import pyml.qtquick


comp Rectangle:
    size: (100, 100)
    
    Rectangle:
        anchor: 'fill'
            del bottom
        size: (30, 30)
        color: 'yellow'

```


