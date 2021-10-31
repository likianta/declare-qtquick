from .__base__ import *
from ..qtqml import QtObject
from ..qtquick import PropertyAnimation


class Object3D(QtObject, W.PsObject3D):
    pass


class Node(Object3D, W.PsNode):
    pass


class Camera(Node, W.PsCamera):
    pass


class Light(Node, W.PsLight):
    pass


class Material(Object3D, W.PsMaterial):
    pass


class Command(C, W.PsCommand):
    pass


class Instancing(Object3D, W.PsInstancing):
    pass


class PerspectiveCamera(Camera, W.PsPerspectiveCamera):
    pass


class Bounds(C, W.PsBounds):
    pass


class Buffer(C, W.PsBuffer):
    pass


class BufferInput(Command, W.PsBufferInput):
    pass


class CustomCamera(Camera, W.PsCustomCamera):
    pass


class CustomMaterial(Material, W.PsCustomMaterial):
    pass


class DefaultMaterial(Material, W.PsDefaultMaterial):
    pass


class DirectionalLight(Light, W.PsDirectionalLight):
    pass


class Effect(Object3D, W.PsEffect):
    pass


class FrustumCamera(PerspectiveCamera, W.PsFrustumCamera):
    pass


class Geometry(Object3D, W.PsGeometry):
    pass


class InstanceList(Instancing, W.PsInstanceList):
    pass


class InstanceListEntry(Object3D, W.PsInstanceListEntry):
    pass


class Joint(Node, W.PsJoint):
    pass


class Loader3D(Node, W.PsLoader3D):
    pass


class Model(Node, W.PsModel):
    pass


class MorphTarget(C, W.PsMorphTarget):
    pass


class OrthographicCamera(Camera, W.PsOrthographicCamera):
    pass


class Pass(C, W.PsPass):
    pass


class PickResult(C, W.PsPickResult):
    pass


class PointLight(Light, W.PsPointLight):
    pass


class PrincipledMaterial(Material, W.PsPrincipledMaterial):
    pass


class QuaternionAnimation(PropertyAnimation, W.PsQuaternionAnimation):
    pass


class RenderStats(C, W.PsRenderStats):
    pass


class Repeater3D(Node, W.PsRepeater3D):
    pass


class SceneEnvironment(Object3D, W.PsSceneEnvironment):
    pass


class SetUniformValue(Command, W.PsSetUniformValue):
    pass


class Shader(C, W.PsShader):
    pass


class Skeleton(Node, W.PsSkeleton):
    pass


class SpotLight(Light, W.PsSpotLight):
    pass


class Texture(Object3D, W.PsTexture):
    pass


class TextureData(Object3D, W.PsTextureData):
    pass


class TextureInput(C, W.PsTextureInput):
    pass


class View3D(C, W.PsView3D):
    pass
