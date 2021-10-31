from declare_qtquick import *
from declare_qtquick.common import exlambda

with Application() as app:
    
    with Window() as win:
        win.visible = True
        
        with Button() as btn:
            btn.anchors.center_in = win
            btn.text = "Click me!"
            btn.on_clicked.connect(exlambda('', """
                win.width += 100
            """))
    
    app.debug('view.qml')
