from .__base__ import *
from ..core import Entity
from ...qtquick3d import Material


class ConeGeometry(C, W.PsConeGeometry):
    pass


class ConeGeometryView(C, W.PsConeGeometryView):
    pass


class ConeMesh(C, W.PsConeMesh):
    pass


class CuboidGeometry(C, W.PsCuboidGeometry):
    pass


class CuboidGeometryView(C, W.PsCuboidGeometryView):
    pass


class CuboidMesh(C, W.PsCuboidMesh):
    pass


class CylinderGeometry(C, W.PsCylinderGeometry):
    pass


class CylinderGeometryView(C, W.PsCylinderGeometryView):
    pass


class CylinderMesh(C, W.PsCylinderMesh):
    pass


class DiffuseMapMaterial(Material, W.PsDiffuseMapMaterial):
    pass


class DiffuseSpecularMapMaterial(Material, W.PsDiffuseSpecularMapMaterial):
    pass


class DiffuseSpecularMaterial(C, W.PsDiffuseSpecularMaterial):
    pass


class ExtrudedTextGeometry(C, W.PsExtrudedTextGeometry):
    pass


class ExtrudedTextMesh(C, W.PsExtrudedTextMesh):
    pass


class FirstPersonCameraController(Entity, W.PsFirstPersonCameraController):
    pass


class ForwardRenderer(C, W.PsForwardRenderer):
    pass


class GoochMaterial(Material, W.PsGoochMaterial):
    pass


class MetalRoughMaterial(C, W.PsMetalRoughMaterial):
    pass


class NormalDiffuseMapAlphaMaterial(Material, W.PsNormalDiffuseMapAlphaMaterial):
    pass


class NormalDiffuseMapMaterial(Material, W.PsNormalDiffuseMapMaterial):
    pass


class NormalDiffuseSpecularMapMaterial(Material, W.PsNormalDiffuseSpecularMapMaterial):
    pass


class OrbitCameraController(Entity, W.PsOrbitCameraController):
    pass


class PerVertexColorMaterial(Material, W.PsPerVertexColorMaterial):
    pass


class PhongAlphaMaterial(Material, W.PsPhongAlphaMaterial):
    pass


class PhongMaterial(Material, W.PsPhongMaterial):
    pass


class PlaneGeometry(C, W.PsPlaneGeometry):
    pass


class PlaneGeometryView(C, W.PsPlaneGeometryView):
    pass


class PlaneMesh(C, W.PsPlaneMesh):
    pass


class SkyboxEntity(C, W.PsSkyboxEntity):
    pass


class SphereGeometry(C, W.PsSphereGeometry):
    pass


class SphereGeometryView(C, W.PsSphereGeometryView):
    pass


class SphereMesh(C, W.PsSphereMesh):
    pass


class Text2DEntity(C, W.PsText2DEntity):
    pass


class TorusGeometry(C, W.PsTorusGeometry):
    pass


class TorusGeometryView(C, W.PsTorusGeometryView):
    pass


class TorusMesh(C, W.PsTorusMesh):
    pass
