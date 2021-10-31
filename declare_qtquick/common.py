import os
import os.path
from inspect import currentframe


def get_current_dir(_level=1):
    """
    This is learnt from lk-logger:
        lk_logger.sourcemap.FrameFinder
            getframe
            getinfo
    """
    frame = currentframe()
    for i in range(_level):
        frame = frame.f_back
    filename = frame.f_code.co_filename
    return os.path.dirname(filename).replace('\\', '/')


def current_locate(path_stub):  # TODO: rename to 'currloc'?
    return get_current_dir(2) + '/' + path_stub
