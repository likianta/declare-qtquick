from .__base__ import *


class DelegateModel(Component, W.PsDelegateModel):
    pass


class DelegateModelGroup(Component, W.PsDelegateModelGroup):
    pass


class Instantiator(Component, W.PsInstantiator):
    pass


class ItemSelectionModel(Component, W.PsItemSelectionModel):
    pass


class ListElement(Component, W.PsListElement):
    pass


class ListModel(Component, W.PsListModel):
    pass


class ObjectModel(Component, W.PsObjectModel):
    pass


class Package(Component, W.PsPackage):
    pass
