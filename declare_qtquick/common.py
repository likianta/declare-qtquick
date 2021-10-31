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


def convert_name_case(snake_case: str):
    """ snake_case to camelCase. For example, 'hello_world' -> 'helloWorld'. """
    if '.' in snake_case:
        # return '.'.join(convert_name_case(s) for s in snake_case.split('.'))
        return '.'.join(map(convert_name_case, snake_case.split('.')))
    
    if '_' not in snake_case:
        camel_case = snake_case
    else:
        segs = snake_case.split('_')
        camel_case = segs[0] + ''.join(x.title() for x in segs[1:])
    
    return camel_case
