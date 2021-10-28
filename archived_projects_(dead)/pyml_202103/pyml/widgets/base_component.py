# noinspection PyProtectedMember
from sys import _getframe

from pyml._typing_hint import *


class BaseComponent:
    uid: TComponentID
    name: str
    level: TLayerLevel
    
    # parent, children 在 __enter__ 中才能确定
    parent: TRepresent
    children: list[TComponent]
    
    _initialized = False
    _propagating = False
    _propagations: set
    _props: dict
    
    def __init__(self):
        from pyml.core.inspect import inspect
        frame = _getframe(1)
        inspect.chfile(frame.f_code.co_filename)
        srcln = inspect.get_line(frame.f_lineno)
        spacing = len(srcln) - len(srcln.lstrip())
        level = int(spacing / 4)  # starts from 0
        
        from pyml.core import gen_id
        self.uid = gen_id(level)
        self.name = self.__class__.__name__
        self.level = level
        
        self.parent = None
        self.children = []
        
        self._propagations = set()
        self._props = {'raw_props': [], 'custom_props': []}
        
        self._init_raw_props()
        self._init_custom_props()
        
        self._initialized = True
    
    def _init_raw_props(self):
        raise NotImplementedError
    
    def _init_custom_props(self):
        pass
    
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
        # https://www.cnblogs.com/hester/articles/4767152.html
        caller_name = _getframe(1).f_code.co_name  # type: str
        
        if self._initialized:
            ''' 如何避免无限回调?
            1. self._propagations 维护一个传播链
            2. 当 on_prop_changed 的 prop 第一次触发时, 由于该 prop 不在传播链
               上, 所以正常触发
               1. 此时 self._propagations 记录该 prop
            3. 当 prop 因为某种联动机制再次到来时, 由于不是第一次触发,
               self._propagations 有记录, 所以不予触发, 直接返回
            4. 什么时候清空传播链? 当外部调用者触发时 (由下面的语句判断是否为外
               部调用者), 将传播链清零, 并重复步骤 2 的过程
            '''
            if (
                    caller_name.startswith('on_') and
                    caller_name.endswith('_changed')
            ):  # the caller is from inner method, so we prevent it if not the
                # first time triggered follows step 3
                if key in self._propagations:
                    return
                # else it it the first time occurred, we pass through it follows
                # step 2
            else:
                # else the caller is from outside, so we clear the propagation
                # chain and pass through it follows step 2
                self._propagations.clear()
            self._propagations.add(key)
        
        super().__setattr__(key, value)
        
        if self._initialized is False:
            if caller_name == '_init_raw_props':
                self._props['raw_props'].append(key)
            elif caller_name == '_init_custom_props':
                self._props['custom_props'].append(key)
        else:
            getattr(self, f'on_{key}_changed', lambda v: v)(value)
    
    def __enter__(self):
        """
        with Component() as com:
            #   1. update `this` indicates to `com`
            #   2. update `context` surrounds `com`
            ...
        """
        from pyml.core import context
        from pyml.keywords import this
        
        # 此时的 this 代表的是上个组件 (上个组件指的可能是父组件, 兄弟组件或兄弟
        # 组件的子孙组件)
        last_com = this.represents
        context.update(self.uid, self.level, self, last_com)
        # 经过 context 更新后, this 和 parent 的指向都正常了
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        from pyml.core import id_ref
        from pyml.keywords import this, parent
        this.point_to(id_ref[(pid := self.uid.parent_id)])
        parent.point_to(id_ref[pid.parent_id] if pid is not None else None)
    
    def build(self, offset=0):
        """
        Examples:
            see TODO
        """
        from textwrap import indent, dedent
        
        def strip(block_string: str):
            return dedent(block_string)[1:].rstrip()
            #   `[1:]`: 去除首行 (空行)
            #   `.rstrip()`: 去除尾部的空行和空格
        
        qml_code = strip('''
            {component} {{
                id: {id}
                objectName: "{object_name}"
                
                // properties
                {properties}
                
                // children
                {children}
            }}
        ''').format(
            id=self.uid,
            object_name=self.name + str(self.uid)[3:],
            component=self.name,
            properties='\n    '.join(self.properties),
            children='\n\n    '.join(
                x.build(4).lstrip() for x in self.children
            ) if self.children else '// NO CHILD'
        )
        
        return indent(qml_code, ' ' * offset)
    
    @property
    def properties(self):
        out = []
        
        for k in self._props['raw_props']:
            v = getattr(self, k)
            
            if k == 'anchors':
                if v := str(v):
                    out.extend(v.split('\n'))
                continue
                
            if isinstance(v, str):
                v = f'"{v}"'
            out.append(f'{name_2_camel_case(k)}: {v}')
            
            # if isinstance(v, BaseComponent):
            #     out.append(v.build())
            # else:
            #     out.append(f'{name_2_camel_case(k)}: {getattr(self, k)}')
        
        return out


def name_2_camel_case(name: str):
    # e.g. 'background_color' -> 'backgroundColor'
    segs = name.split('_')
    return segs[0] + ''.join(x.title() for x in segs[1:])
