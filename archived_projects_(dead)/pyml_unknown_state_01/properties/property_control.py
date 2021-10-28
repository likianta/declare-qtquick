# noinspection PyProtectedMember
from sys import _getframe

from pyml.keywords import *


class _PropertyControl:
    __initialized = False
    __propagating = False
    __propagations: set
    
    def __init__(self):
        self._init_properties()
        self.__propagations = set()
        self.__initialized = True
    
    def _init_properties(self):
        raise NotImplementedError
    
    # def __getattr__(self, item):
    #     if (
    #             isinstance(item, str) and
    #             item.startswith('on_') and
    #             item.endswith('_changed')
    #     ):
    #         return self.__dict__.get(item, lambda v: v)
    #     else:
    #         return self.__dict__[item]
    
    def __setattr__(self, key, value, propagate=True):
        
        if self.__initialized:
            if isinstance(value, (const, true, false, null)):
                send_signal = False
                if isinstance(value, const):
                    value = value.value
            else:
                send_signal = True
                
                ''' 如何避免无限回调?
                1. self._propagations 维护一个传播链
                2. 当 on_prop_changed 的 prop 第一次触发时, 由于该 prop 不在传播
                    链上, 所以正常触发
                    1. 此时 self._propagations 记录该 prop
                3. 当 prop 因为某种联动机制再次到来时, 由于不是第一次触发,
                    self._propagations 有记录, 所以不予触发, 直接返回
                4. 什么时候清空传播链? 当外部调用者触发时 (由下面的语句判断是否
                    为外部调用者), 将传播链清零, 并重复步骤 2 的过程
                '''
                # https://www.cnblogs.com/hester/articles/4767152.html
                caller_name = _getframe(1).f_code.co_name  # type: str
                if (
                        caller_name.startswith('on_') and
                        caller_name.endswith('_changed')
                ):  # the caller is from inner method, so we prevent it if not
                    # the first time triggered follows step 3
                    if key in self.__propagations:
                        return
                    # else it it the first time occurred, we pass through it
                    # follows step 2
                else:
                    # else the caller is from outside, so we clear the
                    # propagation chain and pass through it follows step 2
                    self.__propagations.clear()
                self.__propagations.add(key)
        else:
            send_signal = False
        
        super().__setattr__(key, value)
        
        if send_signal:
            getattr(self, f'on_{key}_changed', lambda v: v)(value)


class QPropertyControl(_PropertyControl):
    """ QQuickItem Property (原生属性) """
    
    def _init_properties(self):
        raise NotImplementedError


class GPropertyControl(_PropertyControl):
    """ GroupProperty (属性组|级联属性) """
    
    def _init_properties(self):
        raise NotImplementedError


class LPropertyControl(_PropertyControl):
    """ Linkage Property (联动属性) """
    
    def _init_properties(self):
        raise NotImplementedError
