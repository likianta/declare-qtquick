from .__base__ import *
from ..core import BoundingVolume
from ..core import Component3D
from ...qtqml import QtObject


class RenderState(Node, W.PsRenderState):
    pass


class FrameGraphNode(Node, W.PsFrameGraphNode):
    pass


class AbstractTextureImage(Node, W.PsAbstractTextureImage):
    pass


class AbstractRayCaster(Component, W.PsAbstractRayCaster):
    pass


class AbstractTexture(Component, W.PsAbstractTexture):
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


class BufferCapture(Component, W.PsBufferCapture):
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


class DirectionalLight(Component, W.PsDirectionalLight):
    pass


class DispatchCompute(FrameGraphNode, W.PsDispatchCompute):
    pass


class Dithering(RenderState, W.PsDithering):
    pass


class Effect(Node, W.PsEffect):
    pass


class EnvironmentLight(Component, W.PsEnvironmentLight):
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


class Light(Component, W.PsLight):
    pass


class LineWidth(RenderState, W.PsLineWidth):
    pass


class Material(Component, W.PsMaterial):
    pass


class MemoryBarrier(FrameGraphNode, W.PsMemoryBarrier):
    pass


class Mesh(Component, W.PsMesh):
    pass


class MultiSampleAntiAliasing(RenderState, W.PsMultiSampleAntiAliasing):
    pass


class NoDepthMask(RenderState, W.PsNoDepthMask):
    pass


class NoDraw(FrameGraphNode, W.PsNoDraw):
    pass


class NoPicking(FrameGraphNode, W.PsNoPicking):
    pass


class ObjectPicker(Component, W.PsObjectPicker):
    pass


class Parameter(Component, W.PsParameter):
    pass


class PickEvent(Component, W.PsPickEvent):
    pass


class PickingProxy(Component3D, W.PsPickingProxy):
    pass


class PickingSettings(Component, W.PsPickingSettings):
    pass


class PickLineEvent(Component, W.PsPickLineEvent):
    pass


class PickPointEvent(Component, W.PsPickPointEvent):
    pass


class PickTriangleEvent(Component, W.PsPickTriangleEvent):
    pass


class PointLight(Component, W.PsPointLight):
    pass


class PointSize(RenderState, W.PsPointSize):
    pass


class PolygonOffset(RenderState, W.PsPolygonOffset):
    pass


class ProximityFilter(FrameGraphNode, W.PsProximityFilter):
    pass


class RasterMode(RenderState, W.PsRasterMode):
    pass


class RayCaster(Component, W.PsRayCaster):
    pass


class RenderCapabilities(Component, W.PsRenderCapabilities):
    pass


class RenderCapture(FrameGraphNode, W.PsRenderCapture):
    pass


class RenderCaptureReply(Component, W.PsRenderCaptureReply):
    pass


class RenderPass(Node, W.PsRenderPass):
    pass


class RenderPassFilter(FrameGraphNode, W.PsRenderPassFilter):
    pass


class RenderSettings(Component, W.PsRenderSettings):
    pass


class RenderStateSet(FrameGraphNode, W.PsRenderStateSet):
    pass


class RenderSurfaceSelector(FrameGraphNode, W.PsRenderSurfaceSelector):
    pass


class RenderTarget(Component, W.PsRenderTarget):
    pass


class RenderTargetOutput(Node, W.PsRenderTargetOutput):
    pass


class RenderTargetSelector(FrameGraphNode, W.PsRenderTargetSelector):
    pass


class SceneLoader(Component, W.PsSceneLoader):
    pass


class ScissorTest(RenderState, W.PsScissorTest):
    pass


class ScreenRayCaster(Component, W.PsScreenRayCaster):
    pass


class SeamlessCubemap(RenderState, W.PsSeamlessCubemap):
    pass


class ShaderImage(Component, W.PsShaderImage):
    pass


class ShaderProgram(Component, W.PsShaderProgram):
    pass


class ShaderProgramBuilder(Component, W.PsShaderProgramBuilder):
    pass


class SharedGLTexture(Component, W.PsSharedGLTexture):
    pass


class SortPolicy(FrameGraphNode, W.PsSortPolicy):
    pass


class SpotLight(Component, W.PsSpotLight):
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


class Technique(Component, W.PsTechnique):
    pass


class TechniqueFilter(FrameGraphNode, W.PsTechniqueFilter):
    pass


class Texture1D(Component, W.PsTexture1D):
    pass


class Texture1DArray(Component, W.PsTexture1DArray):
    pass


class Texture2D(Component, W.PsTexture2D):
    pass


class Texture2DArray(Component, W.PsTexture2DArray):
    pass


class Texture2DMultisample(Component, W.PsTexture2DMultisample):
    pass


class Texture2DMultisampleArray(Component, W.PsTexture2DMultisampleArray):
    pass


class Texture3D(Component, W.PsTexture3D):
    pass


class TextureBuffer(Component, W.PsTextureBuffer):
    pass


class TextureCubeMap(Component, W.PsTextureCubeMap):
    pass


class TextureCubeMapArray(Component, W.PsTextureCubeMapArray):
    pass


class TextureImage(AbstractTextureImage, W.PsTextureImage):
    pass


class TextureLoader(Component, W.PsTextureLoader):
    pass


class TextureRectangle(Component, W.PsTextureRectangle):
    pass


class Viewport(FrameGraphNode, W.PsViewport):
    pass
