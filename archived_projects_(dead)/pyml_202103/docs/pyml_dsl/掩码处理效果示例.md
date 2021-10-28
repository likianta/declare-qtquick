相关模块及方法: `pyml.core.composer.Composer._collapse_code_block()`

处理前:

```pyml
# main.pyml
import pyml.qtquick
import pyml.qtquick.window


comp MyWindow(Window): @win
    """ This is the main window. """
    visible: True
    
    def get_timestamp():
        """
        :return: E.g. '2020-11-01 21:50:00'
        """
        from lk_utils.time_utils import simple_timestamp
        return simple_timestamp('y-m-d h:n:s')

    on_completed:
        print(get_timestamp())

```

处理后:

```
{mask1}
import pyml.qtquick
import pyml.qtquick.window


comp MyWindow{mask2}: @win
    {mask3}
    visible: True
    
    def get_timestamp{mask4}:
        {mask5}
        from lk_utils.time_utils import simple_timestamp
        return simple_timestamp{mask6}

    on_completed:
        print{mask7}

```
