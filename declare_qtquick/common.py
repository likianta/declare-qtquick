import os
import os.path
from functools import wraps
from inspect import currentframe
from threading import Thread

from lk_lambdex import lambdex


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


def _new_thread(func):
    """ New thread decorator. """
    
    @wraps(func)
    def decorate(*args, **kwargs) -> Thread:
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        return t
    
    return decorate


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


def exlambda(args, code, use_context=True, **kwargs):
    return lambdex(args, code, use_context=use_context, **kwargs)


@_new_thread
def aslambda(args, code, use_context=True, **kwargs):
    return lambdex(args, code, use_context=use_context, **kwargs)
