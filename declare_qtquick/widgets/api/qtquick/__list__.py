from .__base__ import *
from ..qtqml import QtObject


class Item(QtObject, W.PsItem):
    pass


class Animation(C, W.PsAnimation):
    pass


class PointerHandler(C, W.PsPointerHandler):
    pass


class PointerDeviceHandler(PointerHandler, W.PsPointerDeviceHandler):
    pass


class Animator(Animation, W.PsAnimator):
    pass


class PropertyAnimation(Animation, W.PsPropertyAnimation):
    pass


class SinglePointHandler(PointerDeviceHandler, W.PsSinglePointHandler):
    pass


class Flickable(Item, W.PsFlickable):
    pass


class MultiPointHandler(PointerDeviceHandler, W.PsMultiPointHandler):
    pass


class NumberAnimation(PropertyAnimation, W.PsNumberAnimation):
    pass


class Image(Item, W.PsImage):
    pass


class Accessible(C, W.PsAccessible):
    pass


class AnchorAnimation(Animation, W.PsAnchorAnimation):
    pass


class AnchorChanges(C, W.PsAnchorChanges):
    pass


class AnimatedImage(Image, W.PsAnimatedImage):
    pass


class AnimatedSprite(Item, W.PsAnimatedSprite):
    pass


class AnimationController(C, W.PsAnimationController):
    pass


class Behavior(C, W.PsBehavior):
    pass


class BorderImage(Item, W.PsBorderImage):
    pass


class BorderImageMesh(C, W.PsBorderImageMesh):
    pass


class Canvas(Item, W.PsCanvas):
    pass


class CanvasGradient(C, W.PsCanvasGradient):
    pass


class CanvasImageData(C, W.PsCanvasImageData):
    pass


class CanvasPixelArray(C, W.PsCanvasPixelArray):
    pass


class ColorAnimation(PropertyAnimation, W.PsColorAnimation):
    pass


class ColorGroup(QtObject, W.PsColorGroup):
    pass


class Column(Item, W.PsColumn):
    pass


class Context2D(C, W.PsContext2D):
    pass


class DoubleValidator(C, W.PsDoubleValidator):
    pass


class Drag(C, W.PsDrag):
    pass


class DragEvent(C, W.PsDragEvent):
    pass


class DragHandler(MultiPointHandler, W.PsDragHandler):
    pass


class DropArea(Item, W.PsDropArea):
    pass


class EnterKey(C, W.PsEnterKey):
    pass


class Flipable(Item, W.PsFlipable):
    pass


class Flow(Item, W.PsFlow):
    pass


class FocusScope(Item, W.PsFocusScope):
    pass


class FontLoader(C, W.PsFontLoader):
    pass


class FontMetrics(C, W.PsFontMetrics):
    pass


class GestureEvent(C, W.PsGestureEvent):
    pass


class Gradient(C, W.PsGradient):
    pass


class GradientStop(C, W.PsGradientStop):
    pass


class GraphicsInfo(C, W.PsGraphicsInfo):
    pass


class Grid(Item, W.PsGrid):
    pass


class GridMesh(C, W.PsGridMesh):
    pass


class GridView(Flickable, W.PsGridView):
    pass


class HandlerPoint(C, W.PsHandlerPoint):
    pass


class HoverHandler(SinglePointHandler, W.PsHoverHandler):
    pass


class IntValidator(C, W.PsIntValidator):
    pass


class ItemGrabResult(QtObject, W.PsItemGrabResult):
    pass


class KeyEvent(C, W.PsKeyEvent):
    pass


class KeyNavigation(C, W.PsKeyNavigation):
    pass


class Keys(C, W.PsKeys):
    pass


class LayoutMirroring(C, W.PsLayoutMirroring):
    pass


class ListView(Flickable, W.PsListView):
    pass


class Loader(Item, W.PsLoader):
    pass


class Matrix4x4(C, W.PsMatrix4x4):
    pass


class MouseArea(Item, W.PsMouseArea):
    pass


class MouseEvent(C, W.PsMouseEvent):
    pass


class MultiPointTouchArea(Item, W.PsMultiPointTouchArea):
    pass


class OpacityAnimator(Animator, W.PsOpacityAnimator):
    pass


class Palette(C, W.PsPalette):
    pass


class ParallelAnimation(Animation, W.PsParallelAnimation):
    pass


class ParentAnimation(Animation, W.PsParentAnimation):
    pass


class ParentChange(C, W.PsParentChange):
    pass


class Path(C, W.PsPath):
    pass


class PathAngleArc(C, W.PsPathAngleArc):
    pass


class PathAnimation(Animation, W.PsPathAnimation):
    pass


class PathArc(C, W.PsPathArc):
    pass


class PathAttribute(C, W.PsPathAttribute):
    pass


class PathCubic(C, W.PsPathCubic):
    pass


class PathCurve(C, W.PsPathCurve):
    pass


class PathElement(C, W.PsPathElement):
    pass


class PathInterpolator(C, W.PsPathInterpolator):
    pass


class PathLine(C, W.PsPathLine):
    pass


class PathMove(C, W.PsPathMove):
    pass


class PathMultiline(C, W.PsPathMultiline):
    pass


class PathPercent(C, W.PsPathPercent):
    pass


class PathPolyline(C, W.PsPathPolyline):
    pass


class PathQuad(C, W.PsPathQuad):
    pass


class PathSvg(C, W.PsPathSvg):
    pass


class PathText(C, W.PsPathText):
    pass


class PathView(Item, W.PsPathView):
    pass


class PauseAnimation(Animation, W.PsPauseAnimation):
    pass


class PinchArea(Item, W.PsPinchArea):
    pass


class PinchEvent(C, W.PsPinchEvent):
    pass


class PinchHandler(MultiPointHandler, W.PsPinchHandler):
    pass


class PointHandler(SinglePointHandler, W.PsPointHandler):
    pass


class Positioner(C, W.PsPositioner):
    pass


class PropertyAction(Animation, W.PsPropertyAction):
    pass


class PropertyChanges(C, W.PsPropertyChanges):
    pass


class Rectangle(Item, W.PsRectangle):
    pass


class RegularExpressionValidator(C, W.PsRegularExpressionValidator):
    pass


class Repeater(Item, W.PsRepeater):
    pass


class Rotation(C, W.PsRotation):
    pass


class RotationAnimation(PropertyAnimation, W.PsRotationAnimation):
    pass


class RotationAnimator(Animator, W.PsRotationAnimator):
    pass


class Row(Item, W.PsRow):
    pass


class Scale(C, W.PsScale):
    pass


class ScaleAnimator(Animator, W.PsScaleAnimator):
    pass


class ScriptAction(Animation, W.PsScriptAction):
    pass


class SequentialAnimation(Animation, W.PsSequentialAnimation):
    pass


class ShaderEffect(Item, W.PsShaderEffect):
    pass


class ShaderEffectSource(Item, W.PsShaderEffectSource):
    pass


class Shortcut(C, W.PsShortcut):
    pass


class SmoothedAnimation(NumberAnimation, W.PsSmoothedAnimation):
    pass


class SpringAnimation(NumberAnimation, W.PsSpringAnimation):
    pass


class Sprite(C, W.PsSprite):
    pass


class SpriteSequence(Item, W.PsSpriteSequence):
    pass


class State(C, W.PsState):
    pass


class StateChangeScript(C, W.PsStateChangeScript):
    pass


class StateGroup(C, W.PsStateGroup):
    pass


class SystemPalette(C, W.PsSystemPalette):
    pass


class TableView(Flickable, W.PsTableView):
    pass


class TapHandler(SinglePointHandler, W.PsTapHandler):
    pass


class Text(Item, W.PsText):
    pass


class TextEdit(Item, W.PsTextEdit):
    pass


class TextInput(Item, W.PsTextInput):
    pass


class TextMetrics(C, W.PsTextMetrics):
    pass


class TouchPoint(C, W.PsTouchPoint):
    pass


class Transform(C, W.PsTransform):
    pass


class Transition(C, W.PsTransition):
    pass


class Translate(C, W.PsTranslate):
    pass


class UniformAnimator(Animator, W.PsUniformAnimator):
    pass


class Vector3dAnimation(PropertyAnimation, W.PsVector3dAnimation):
    pass


class ViewTransition(C, W.PsViewTransition):
    pass


class WheelEvent(C, W.PsWheelEvent):
    pass


class WheelHandler(SinglePointHandler, W.PsWheelHandler):
    pass


class Window(C, W.PsWindow):
    pass


class XAnimator(Animator, W.PsXAnimator):
    pass


class YAnimator(Animator, W.PsYAnimator):
    pass
