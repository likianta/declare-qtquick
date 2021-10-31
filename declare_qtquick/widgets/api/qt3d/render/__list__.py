from .__base__ import *
from ..core import BoundingVolume
from ..core import Component3D
from ...qtqml import QtObject
from ...qtquick3d import Node


class RenderState(Node, W.PsRenderState):
    pass


class FrameGraphNode(Node, W.PsFrameGraphNode):
    pass


class AbstractTextureImage(Node, W.PsAbstractTextureImage):
    pass


class AbstractRayCaster(C, W.PsAbstractRayCaster):
    pass


class AbstractTexture(C, W.PsAbstractTexture):
    pass


class AlphaCoverage(RenderState, W.PsAlphaCoverage):
    pass


class AlphaTest(RenderState, W.PsAlphaTest):
    pass


class BlendEquation(RenderState, W.PsBlendEquation):
    pass


class BlendEquationArguments(RenderState, W.PsBlendEquationArguments):
    pass


class BlitFramebuffer(FrameGraphNode, W.PsBlitFramebuffer):
    pass


class BufferCapture(C, W.PsBufferCapture):
    pass


class Camera(Entity, W.PsCamera):
    pass


class CameraLens(Component3D, W.PsCameraLens):
    pass


class CameraSelector(FrameGraphNode, W.PsCameraSelector):
    pass


class ClearBuffers(FrameGraphNode, W.PsClearBuffers):
    pass


class ClipPlane(RenderState, W.PsClipPlane):
    pass


class ColorMask(RenderState, W.PsColorMask):
    pass


class ComputeCommand(Component3D, W.PsComputeCommand):
    pass


class CullFace(RenderState, W.PsCullFace):
    pass


class DebugOverlay(FrameGraphNode, W.PsDebugOverlay):
    pass


class DepthRange(RenderState, W.PsDepthRange):
    pass


class DepthTest(RenderState, W.PsDepthTest):
    pass


class DirectionalLight(C, W.PsDirectionalLight):
    pass


class DispatchCompute(FrameGraphNode, W.PsDispatchCompute):
    pass


class Dithering(RenderState, W.PsDithering):
    pass


class Effect(Node, W.PsEffect):
    pass


class EnvironmentLight(C, W.PsEnvironmentLight):
    pass


class FilterKey(Node, W.PsFilterKey):
    pass


class FrontFace(RenderState, W.PsFrontFace):
    pass


class FrustumCulling(FrameGraphNode, W.PsFrustumCulling):
    pass


class GeometryRenderer(BoundingVolume, W.PsGeometryRenderer):
    pass


class GraphicsApiFilter(QtObject, W.PsGraphicsApiFilter):
    pass


class Layer(Component3D, W.PsLayer):
    pass


class LayerFilter(FrameGraphNode, W.PsLayerFilter):
    pass


class LevelOfDetail(Component3D, W.PsLevelOfDetail):
    pass


class LevelOfDetailBoundingSphere(Component3D, W.PsLevelOfDetailBoundingSphere):
    pass


class LevelOfDetailLoader(Entity, W.PsLevelOfDetailLoader):
    pass


class LevelOfDetailSwitch(Component3D, W.PsLevelOfDetailSwitch):
    pass


class Light(C, W.PsLight):
    pass


class LineWidth(RenderState, W.PsLineWidth):
    pass


class Material(C, W.PsMaterial):
    pass


class MemoryBarrier(FrameGraphNode, W.PsMemoryBarrier):
    pass


class Mesh(C, W.PsMesh):
    pass


class MultiSampleAntiAliasing(RenderState, W.PsMultiSampleAntiAliasing):
    pass


class NoDepthMask(RenderState, W.PsNoDepthMask):
    pass


class NoDraw(FrameGraphNode, W.PsNoDraw):
    pass


class NoPicking(FrameGraphNode, W.PsNoPicking):
    pass


class ObjectPicker(C, W.PsObjectPicker):
    pass


class Parameter(C, W.PsParameter):
    pass


class PickEvent(C, W.PsPickEvent):
    pass


class PickingProxy(Component3D, W.PsPickingProxy):
    pass


class PickingSettings(C, W.PsPickingSettings):
    pass


class PickLineEvent(C, W.PsPickLineEvent):
    pass


class PickPointEvent(C, W.PsPickPointEvent):
    pass


class PickTriangleEvent(C, W.PsPickTriangleEvent):
    pass


class PointLight(C, W.PsPointLight):
    pass


class PointSize(RenderState, W.PsPointSize):
    pass


class PolygonOffset(RenderState, W.PsPolygonOffset):
    pass


class ProximityFilter(FrameGraphNode, W.PsProximityFilter):
    pass


class RasterMode(RenderState, W.PsRasterMode):
    pass


class RayCaster(C, W.PsRayCaster):
    pass


class RenderCapabilities(C, W.PsRenderCapabilities):
    pass


class RenderCapture(FrameGraphNode, W.PsRenderCapture):
    pass


class RenderCaptureReply(C, W.PsRenderCaptureReply):
    pass


class RenderPass(Node, W.PsRenderPass):
    pass


class RenderPassFilter(FrameGraphNode, W.PsRenderPassFilter):
    pass


class RenderSettings(C, W.PsRenderSettings):
    pass


class RenderStateSet(FrameGraphNode, W.PsRenderStateSet):
    pass


class RenderSurfaceSelector(FrameGraphNode, W.PsRenderSurfaceSelector):
    pass


class RenderTarget(C, W.PsRenderTarget):
    pass


class RenderTargetOutput(Node, W.PsRenderTargetOutput):
    pass


class RenderTargetSelector(FrameGraphNode, W.PsRenderTargetSelector):
    pass


class SceneLoader(Component, W.PsSceneLoader):
    pass


class ScissorTest(RenderState, W.PsScissorTest):
    pass


class ScreenRayCaster(C, W.PsScreenRayCaster):
    pass


class SeamlessCubemap(RenderState, W.PsSeamlessCubemap):
    pass


class ShaderImage(C, W.PsShaderImage):
    pass


class ShaderProgram(C, W.PsShaderProgram):
    pass


class ShaderProgramBuilder(C, W.PsShaderProgramBuilder):
    pass


class SharedGLTexture(C, W.PsSharedGLTexture):
    pass


class SortPolicy(FrameGraphNode, W.PsSortPolicy):
    pass


class SpotLight(C, W.PsSpotLight):
    pass


class StencilMask(RenderState, W.PsStencilMask):
    pass


class StencilOperation(RenderState, W.PsStencilOperation):
    pass


class StencilOperationArguments(QtObject, W.PsStencilOperationArguments):
    pass


class StencilTest(RenderState, W.PsStencilTest):
    pass


class StencilTestArguments(QtObject, W.PsStencilTestArguments):
    pass


class SubtreeEnabler(FrameGraphNode, W.PsSubtreeEnabler):
    pass


class Technique(C, W.PsTechnique):
    pass


class TechniqueFilter(FrameGraphNode, W.PsTechniqueFilter):
    pass


class Texture1D(C, W.PsTexture1D):
    pass


class Texture1DArray(C, W.PsTexture1DArray):
    pass


class Texture2D(C, W.PsTexture2D):
    pass


class Texture2DArray(C, W.PsTexture2DArray):
    pass


class Texture2DMultisample(C, W.PsTexture2DMultisample):
    pass


class Texture2DMultisampleArray(C, W.PsTexture2DMultisampleArray):
    pass


class Texture3D(C, W.PsTexture3D):
    pass


class TextureBuffer(C, W.PsTextureBuffer):
    pass


class TextureCubeMap(C, W.PsTextureCubeMap):
    pass


class TextureCubeMapArray(C, W.PsTextureCubeMapArray):
    pass


class TextureImage(AbstractTextureImage, W.PsTextureImage):
    pass


class TextureLoader(C, W.PsTextureLoader):
    pass


class TextureRectangle(C, W.PsTextureRectangle):
    pass


class Viewport(FrameGraphNode, W.PsViewport):
    pass
