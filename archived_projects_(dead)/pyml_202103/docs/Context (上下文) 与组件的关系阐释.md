# Context (上下文) 与组件的关系阐释

* context 维护着唯一的全局组件树
* this, parent 的行为只是在 context 的组件树上定位和更新定位
* 每当产生一个新组件时 (开启 `with` 语句块), 都会更新 context, 以及 this, parent
* 每当退出该组件块时 (结束 `with` 语句块), 都会更新 context, 以及 this, parent
* 每个组件都持有它的直接子组件的引用 (`Component.children`)
