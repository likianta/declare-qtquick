from declare_qtquick import *

with Application() as app:
    
    with Window() as win:
        win.width = 800
        win.height = 600
        win.color = 'gray'
        win.visible = True
        
        with Rectangle() as rect:
            rect.anchors.fill = win
            rect.anchors.margins = 10
            rect.color = '#e28086'
            rect.radius = 8
            
            with MouseArea() as area:
                area.anchors.fill = rect
        
        with Text() as txt:
            txt.anchors.center_in = win
            txt.text = 'Hello World'
    
    app.build('view.qml')
    # app.start('view.qml')
    # app.debug('view.qml')
