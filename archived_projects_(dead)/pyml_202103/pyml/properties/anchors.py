from pyml._typing_hint import *
from pyml.keywords import const, consts

from .property_control import GPropertyControl


# noinspection PyUnusedLocal
class Anchors(GPropertyControl):
    fill: TConstable[TComponentID]
    
    center: TConstable[TComponentID]
    horizontal_center: TConstable[TComponentID]
    vertical_center: TConstable[TComponentID]
    
    left: TConstable[TComponentID]
    right: TConstable[TComponentID]
    top: TConstable[TComponentID]
    bottom: TConstable[TComponentID]
    
    margins: Union[int, tuple[int, ...], list[int]]
    left_margin: TConstable[int]
    right_margin: TConstable[int]
    top_margin: TConstable[int]
    bottom_margin: TConstable[int]
    
    def _init_properties(self):
        self.fill = ''
        self.center = ''
        self.left = ''
        self.right = ''
        self.top = ''
        self.bottom = ''
        self.margins = 0
        self.left_margin = 0
        self.right_margin = 0
        self.top_margin = 0
        self.bottom_margin = 0
    
    def on_fill_changed(self, v):
        self.left = self.right = self.top = self.bottom = const(v)
        self.center = ''
    
    def on_left_changed(self, v):
        if self.fill != v: self.fill = const('')
        if v: self.center = const('')
    
    def on_right_changed(self, v):
        if self.fill != v: self.fill = const('')
        if v: self.center = const('')
    
    def on_top_changed(self, v):
        if self.fill != v: self.fill = const('')
        if v: self.center = const('')
    
    def on_bottom_changed(self, v):
        if self.fill != v: self.fill = const('')
        if v: self.center = const('')
    
    def on_center_changed(self, v):
        self.fill = self.left = self.right = self.top = self.bottom = const('')
    
    def on_horizontal_center_changed(self, v):
        if v: self.left = self.right = const('')
    
    def on_vertical_center_changed(self, v):
        if v: self.top = self.bottom = const('')
    
    def on_margins_changed(self, v):
        if isinstance(v, int):
            self.left_margin = self.right_margin = \
                self.top_margin = self.bottom_margin = const(v)
        else:
            v = (list(v) + [0, 0, 0, 0])[:4]
            self.left_margin, self.top_margin, \
                self.right_margin, self.bottom_margin = consts(*v)
    
    def __str__(self):
        out = []
        
        if self.fill:
            if self.left == self.right == self.top == self.bottom == self.fill:
                out.append(f'anchors.fill: {self.fill}')
        elif self.center:
            out.append(f'anchors.centerIn: {self.center}')
        else:
            if self.horizontal_center:
                out.append(f'anchors.horizontalCenter: '
                           f'{self.horizontal_center}')
            else:
                if self.left:
                    out.append(f'anchors.left: {self.left}')
                if self.right:
                    out.append(f'anchors.right: {self.right}')
            if self.vertical_center:
                out.append(f'anchors.verticalCenter: '
                           f'{self.vertical_center}')
            else:
                if self.top:
                    out.append(f'anchors.left: {self.top}')
                if self.bottom:
                    out.append(f'anchors.left: {self.bottom}')
        
        if self.margins:
            out.append(f'anchors.margins: {self.margins}')
        if self.left_margin != self.margins:
            out.append(f'anchors.leftMargin: {self.left_margin}')
        if self.right_margin != self.margins:
            out.append(f'anchors.rightMargin: {self.right_margin}')
        if self.top_margin != self.margins:
            out.append(f'anchors.topMargin: {self.top_margin}')
        if self.bottom_margin != self.margins:
            out.append(f'anchors.bottomMargin: {self.bottom_margin}')
        
        return '\n'.join(out)


class DialectAnchors(Anchors):
    lcenter: TConstable[TComponentID]
    rcenter: TConstable[TComponentID]
    tcenter: TConstable[TComponentID]
    bcenter: TConstable[TComponentID]
    hcenter: TConstable[TComponentID]
    vcenter: TConstable[TComponentID]
    
    lside: TConstable[TComponentID]
    rside: TConstable[TComponentID]
    tside: TConstable[TComponentID]
    bside: TConstable[TComponentID]
    hside: TConstable[TComponentID]
    vside: TConstable[TComponentID]
    
    lmargin: TConstable[int]
    rmargin: TConstable[int]
    tmargin: TConstable[int]
    bmargin: TConstable[int]
    hmargins: Union[TConstable[int], tuple[TConstable[int], TConstable[int]]]
    vmargins: Union[TConstable[int], tuple[TConstable[int], TConstable[int]]]
    
    def _init_properties(self):
        super(DialectAnchors, self)._init_properties()
        self.lcenter = ''
        self.rcenter = ''
        self.tcenter = ''
        self.bcenter = ''
        self.hcenter = ''
        self.vcenter = ''
        self.lside = ''
        self.rside = ''
        self.tside = ''
        self.bside = ''
        self.hside = ''
        self.vside = ''
        self.lmargin = 0
        self.rmargin = 0
        self.tmargin = 0
        self.bmargin = 0
        self.hmargins = 0
        self.vmargins = 0
    
    def on_lcenter_changed(self, v):
        self.on_left_changed(v)
        self.on_vertical_center_changed(v)
    
    def on_rcenter_changed(self, v):
        self.on_right_changed(v)
        self.on_vertical_center_changed(v)
    
    def on_tcenter_changed(self, v):
        self.on_top_changed(v)
        self.on_horizontal_center_changed(v)
    
    def on_bcenter_changed(self, v):
        self.on_bottom_changed(v)
        self.on_horizontal_center_changed(v)
    
    def on_hcenter_changed(self, v):
        self.on_horizontal_center_changed(v)
    
    def on_vcenter_changed(self, v):
        self.on_vertical_center_changed(v)
    
    def on_lside_changed(self, v):
        self.on_left_changed(v)
    
    def on_rside_changed(self, v):
        self.on_right_changed(v)
    
    def on_tside_changed(self, v):
        self.on_top_changed(v)
    
    def on_bside_changed(self, v):
        self.on_bottom_changed(v)
    
    def on_hside_changed(self, v):
        self.on_left_changed(v)
        self.on_right_changed(v)
    
    def on_vside_changed(self, v):
        self.on_top_changed(v)
        self.on_bottom_changed(v)
    
    def on_hmargins_changed(self, v):
        if isinstance(v, TConstable[int]):
            self.left_margin = self.right_margin = v
        else:
            self.left_margin, self.right_margin = v
    
    def on_vmargins_changed(self, v):
        if isinstance(v, TConstable[int]):
            self.top_margin = self.bottom_margin = v
        else:
            self.top_margin, self.bottom_margin = v
