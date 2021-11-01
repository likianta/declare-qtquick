<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
<!-- This file is saved using a hacked version of FreeMind. visit: http://freemind-mmx.sourceforge.net -->
<!-- Orignal FreeMind, can download from http://freemind.sourceforge.net -->
<!-- This .mm file is CVS/SVN friendly, some atts are saved in .mmx file. (from ossxp.com) -->
<node ID="ID_857944159" 
	TEXT="Declare QtQuick Project Kanban">
<node FOLDED="true" ID="ID_1891674065" POSITION="right" 
	TEXT="函数绑定问题">
<node FOLDED="true" ID="ID_1886988876" 
	TEXT="Example:&#xa;    with Window() as win:&#xa;        with Button() as btn:&#xa;            btn.on_clicked.connect(lamblock(&apos;&apos;, &quot;&quot;&quot;&#xa;                win.width += 10&#xa;            &quot;&quot;&quot;))">
<node FOLDED="true" ID="ID_1568576449" 
	TEXT="win.width += 10">
<node FOLDED="true" ID="ID_1799684503" 
	TEXT="__getprop__ 在 app.build 完成后发生行为变化">
<node FOLDED="true" ID="ID_618894821" 
	TEXT="black_magic">
<node FOLDED="true" ID="ID_86059074" 
	TEXT="遍历 context_manager 中的所有节点, 为每个 component 的 __getprop__ 等魔术方法提供行为转换">
<node FOLDED="true" ID="ID_526849670" 
	TEXT="__getprop__ (example)">
<node ID="ID_492305607" 
	TEXT="def __getprop__(self, key: str):&#xa;    if &lt;is_key_accessable_by_pyside&gt;:&#xa;        return self._qobj.property(key)&#xa;    else:&#xa;        return &lt;get value by qmlside, and convert it to python object&gt;"/>
</node>
<node FOLDED="true" ID="ID_791140360" 
	TEXT="__setprop__ (example)">
<node ID="ID_1549851475" 
	TEXT="def __setprop__(self, key, value):&#xa;    if &lt;is key operatable in pyside&gt;:&#xa;        self._qobj.setProperty(key, value)&#xa;    else:&#xa;        &lt;set property by qmlside&gt;"/>
</node>
</node>
</node>
</node>
</node>
</node>
<node FOLDED="true" ID="ID_772657107" 
	TEXT="在函数中是否能够使用布局语法?">
<node FOLDED="true" ID="ID_1023749264" 
	TEXT="Example:&#xa;    with Window() as win:&#xa;        with Button() as btn:&#xa;            btn.on_clicked.connect(lamblock(&apos;&apos;, &quot;&quot;&quot;&#xa;                btn.width.bind(win.width - 400)&#xa;                win.width.set_anim()&#xa;                win.width += 10&#xa;            &quot;&quot;&quot;))">
<node FOLDED="true" ID="ID_1361892960" 
	TEXT="win.width.set_anim()">
<node FOLDED="true" ID="ID_1185910286" 
	TEXT="方案 1: 生成 qml 代码片段">
<node ID="ID_1672071418" 
	TEXT="qml 引擎如何执行"/>
</node>
<node FOLDED="true" ID="ID_1062690573" 
	TEXT="方案 2: 生成 js 代码片段">
<node ID="ID_960590572" 
	TEXT="cons: 需要另写一套 js 生成器"/>
<node ID="ID_64403972" 
	TEXT="可能需要生成碎片文件, 或者 exec snippet string"/>
</node>
</node>
</node>
</node>
</node>
</node>
</map>
