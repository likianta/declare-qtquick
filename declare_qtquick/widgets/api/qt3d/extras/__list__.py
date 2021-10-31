from .__base__ import *


class ConeGeometry(Component, W.PsConeGeometry):
    pass


class ConeGeometryView(Component, W.PsConeGeometryView):
    pass


class ConeMesh(Component, W.PsConeMesh):
    pass


class CuboidGeometry(Component, W.PsCuboidGeometry):
    pass


class CuboidGeometryView(Component, W.PsCuboidGeometryView):
    pass


class CuboidMesh(Component, W.PsCuboidMesh):
    pass


class CylinderGeometry(Component, W.PsCylinderGeometry):
    pass


class CylinderGeometryView(Component, W.PsCylinderGeometryView):
    pass


class CylinderMesh(Component, W.PsCylinderMesh):
    pass


class DiffuseMapMaterial(Material, W.PsDiffuseMapMaterial):
    pass


class DiffuseSpecularMapMaterial(Material, W.PsDiffuseSpecularMapMaterial):
    pass


class DiffuseSpecularMaterial(Component, W.PsDiffuseSpecularMaterial):
    pass


class ExtrudedTextGeometry(Component, W.PsExtrudedTextGeometry):
    pass


class ExtrudedTextMesh(Component, W.PsExtrudedTextMesh):
    pass


class FirstPersonCameraController(Entity, W.PsFirstPersonCameraController):
    pass


class ForwardRenderer(Component, W.PsForwardRenderer):
    pass


class GoochMaterial(Material, W.PsGoochMaterial):
    pass


class MetalRoughMaterial(Component, W.PsMetalRoughMaterial):
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


class PlaneGeometry(Component, W.PsPlaneGeometry):
    pass


class PlaneGeometryView(Component, W.PsPlaneGeometryView):
    pass


class PlaneMesh(Component, W.PsPlaneMesh):
    pass


class SkyboxEntity(Component, W.PsSkyboxEntity):
    pass


class SphereGeometry(Component, W.PsSphereGeometry):
    pass


class SphereGeometryView(Component, W.PsSphereGeometryView):
    pass


class SphereMesh(Component, W.PsSphereMesh):
    pass


class Text2DEntity(Component, W.PsText2DEntity):
    pass


class TorusGeometry(Component, W.PsTorusGeometry):
    pass


class TorusGeometryView(Component, W.PsTorusGeometryView):
    pass


class TorusMesh(Component, W.PsTorusMesh):
    pass
