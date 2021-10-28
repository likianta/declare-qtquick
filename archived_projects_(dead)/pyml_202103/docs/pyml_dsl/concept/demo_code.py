# raw concepts


class Application:
    pass


class Window:
    pass


class Rectangle:
    pass


class Repeater:
    pass


class Text:
    pass


class MouseArea:
    pass


class Item:
    pass


class Anchors:
    right_bottom: str
    

class NumberAnimation:
    
    def __init__(self, *args, **kwargs):
        pass


class QBuiltinWord:
    left: str
    right: str
    top: str
    bottom: str
    
    def __init__(self, w):
        self.w = w


parent = QBuiltinWord('parent')
this = QBuiltinWord('this')
true = QBuiltinWord('true')
false = QBuiltinWord('false')
last_sibling = QBuiltinWord('last_sibling')
next_sibling = QBuiltinWord('next_sibling')
anchors = Anchors()


# ------------------------------------------------------------------------------

def main():
    with Application() as app:
        with Window() as win:
            win.name = 'main_window'
            win.color = '#f2f2f2'
            win.size = (500, 600)
            
            with Rectangle() as rect:
                rect.anchors.fill = parent
                
                with MouseArea() as area:
                    area.anchors.fill = parent
                    
                    with Item() as container:
                        container.anchors.fill = parent
                        container.colors = [
                            'yellow', 'blue', 'red', 'green', 'gray'
                        ]
                        
                        def rescale(self, wheel):
                            # scroll wheel to change `self.scale` property
                            if wheel.modifiers:
                                delta = wheel.angle_delta.y / 1200
                                self.scale = max((self.scale + delta, 0))
                        
                        # drag to move container, wheel to rescale container
                        area.drag.target = container
                        area.on_wheel.binding(
                            lambda wheel: rescale(container, wheel)
                        )
                        container.anim_scale.binding(
                            NumberAnimation(
                                duration=100,
                                easing_type='easing.out_quart',
                            )
                        )
                        
                        with Rectangle() as brick:
                            this.pos = (0, 0)
                            this.size = (30, 30)
                            this.color = container.colors[0]
                        
                        with Rectangle():
                            this.pos = (100, 0)
                            this.size = brick.size
                            this.color = container.colors[1]
                        
                        with Rectangle():
                            this.pos = (200, 0)
                            this.size = brick.size
                            this.color = container.colors[2]
                        
                        with Rectangle():
                            this.pos = (300, 0)
                            this.size = brick.size
                            this.color = container.colors[3]
                        
                        with Rectangle():
                            this.pos = (0, 100)
                            this.size = brick.size
                            this.color = container.colors[4]

            # show container's scale percentage on the right bottom corner
            with Text() as scale_txt:
                scale_txt.anchors = anchors.right_bottom
                scale_txt.anchors.margins = 10
                #   or: scale_txt.anchors = {'right': 10, 'bottom': 10}
                scale_txt.canvas_scale = container.scale
                scale_txt.on_text.binding(
                    lambda: str(round(scale_txt.canvas_scale * 100)) + '%'
                )
            
            win.show()
        app.start()


''' the main() function converted to qml layout like below:
import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    id: comp01
    objectName: 'main_window'
    color: '#f2f2f2'
    width: 500; height: 500
    visible: true

    Rectangle {
        id: comp02
        anchors.fill: parent
        
        MouseArea {
            id: comp03
            anchors.fill: parent
            
            Item {
                id: comp04
                anchors.fill: parent
                
                property var colors: [
                    'yellow', 'blue', 'red', 'green', 'gray'
                ]
                
                Behavior on scale {
                    NumberAnimation {
                        duration: 100
                        easing.type: easing.out_quart
                    }
                }
                
                Component.onCompleted: {
                    comp03.drag.target = comp04
                    comp03.wheel.connect(PySide.call('method01', wheel))
                }
                
                Rectangle {
                    id: comp05
                    x: 0
                    y: 0
                    width: 30
                    height: 30
                    color: comp04.colors[0]
                }
                
                Rectangle {
                    id: comp06
                    x: 100
                    y: 0
                    width: 30
                    height: 30
                    color: comp04.colors[1]
                }
                
                Rectangle {
                    id: comp07
                    x: 200
                    y: 0
                    width: 30
                    height: 30
                    color: comp04.colors[2]
                }
                
                Rectangle {
                    id: comp08
                    x: 300
                    y: 0
                    width: 30
                    height: 30
                    color: comp04.colors[3]
                }
                
                Rectangle {
                    id: comp09
                    x: 0
                    y: 100
                    width: 30
                    height: 30
                    color: comp04.colors[4]
                }
            }
        }
    }
    
    Text {
        id: comp10
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 10
        
        property alias canvas_scale: comp04.scale
        
        Component.onCompleted: {
            comp10.textChanged.connect(PySide.call('method02'))
        }
    }
}
'''
