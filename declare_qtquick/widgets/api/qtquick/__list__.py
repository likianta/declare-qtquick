from .__base__ import *
from ..qtqml import QtObject


class Item(QtObject, W.PsItem):
    pass


class Animation(Component, W.PsAnimation):
    pass


class PointerHandler(Component, W.PsPointerHandler):
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


class Accessible(Component, W.PsAccessible):
    pass


class AnchorAnimation(Animation, W.PsAnchorAnimation):
    pass


class AnchorChanges(Component, W.PsAnchorChanges):
    pass


class AnimatedImage(Image, W.PsAnimatedImage):
    pass


class AnimatedSprite(Item, W.PsAnimatedSprite):
    pass


class AnimationController(Component, W.PsAnimationController):
    pass


class Behavior(Component, W.PsBehavior):
    pass


class BorderImage(Item, W.PsBorderImage):
    pass


class BorderImageMesh(Component, W.PsBorderImageMesh):
    pass


class Canvas(Item, W.PsCanvas):
    pass


class CanvasGradient(Component, W.PsCanvasGradient):
    pass


class CanvasImageData(Component, W.PsCanvasImageData):
    pass


class CanvasPixelArray(Component, W.PsCanvasPixelArray):
    pass


class ColorAnimation(PropertyAnimation, W.PsColorAnimation):
    pass


class ColorGroup(QtObject, W.PsColorGroup):
    pass


class Column(Item, W.PsColumn):
    pass


class Context2D(Component, W.PsContext2D):
    pass


class DoubleValidator(Component, W.PsDoubleValidator):
    pass


class Drag(Component, W.PsDrag):
    pass


class DragEvent(Component, W.PsDragEvent):
    pass


class DragHandler(MultiPointHandler, W.PsDragHandler):
    pass


class DropArea(Item, W.PsDropArea):
    pass


class EnterKey(Component, W.PsEnterKey):
    pass


class Flipable(Item, W.PsFlipable):
    pass


class Flow(Item, W.PsFlow):
    pass


class FocusScope(Item, W.PsFocusScope):
    pass


class FontLoader(Component, W.PsFontLoader):
    pass


class FontMetrics(Component, W.PsFontMetrics):
    pass


class GestureEvent(Component, W.PsGestureEvent):
    pass


class Gradient(Component, W.PsGradient):
    pass


class GradientStop(Component, W.PsGradientStop):
    pass


class GraphicsInfo(Component, W.PsGraphicsInfo):
    pass


class Grid(Item, W.PsGrid):
    pass


class GridMesh(Component, W.PsGridMesh):
    pass


class GridView(Flickable, W.PsGridView):
    pass


class HandlerPoint(Component, W.PsHandlerPoint):
    pass


class HoverHandler(SinglePointHandler, W.PsHoverHandler):
    pass


class IntValidator(Component, W.PsIntValidator):
    pass


class ItemGrabResult(QtObject, W.PsItemGrabResult):
    pass


class KeyEvent(Component, W.PsKeyEvent):
    pass


class KeyNavigation(Component, W.PsKeyNavigation):
    pass


class Keys(Component, W.PsKeys):
    pass


class LayoutMirroring(Component, W.PsLayoutMirroring):
    pass


class ListView(Flickable, W.PsListView):
    pass


class Loader(Item, W.PsLoader):
    pass


class Matrix4x4(Component, W.PsMatrix4x4):
    pass


class MouseArea(Item, W.PsMouseArea):
    pass


class MouseEvent(Component, W.PsMouseEvent):
    pass


class MultiPointTouchArea(Item, W.PsMultiPointTouchArea):
    pass


class OpacityAnimator(Animator, W.PsOpacityAnimator):
    pass


class Palette(Component, W.PsPalette):
    pass


class ParallelAnimation(Animation, W.PsParallelAnimation):
    pass


class ParentAnimation(Animation, W.PsParentAnimation):
    pass


class ParentChange(Component, W.PsParentChange):
    pass


class Path(Component, W.PsPath):
    pass


class PathAngleArc(Component, W.PsPathAngleArc):
    pass


class PathAnimation(Animation, W.PsPathAnimation):
    pass


class PathArc(Component, W.PsPathArc):
    pass


class PathAttribute(Component, W.PsPathAttribute):
    pass


class PathCubic(Component, W.PsPathCubic):
    pass


class PathCurve(Component, W.PsPathCurve):
    pass


class PathElement(Component, W.PsPathElement):
    pass


class PathInterpolator(Component, W.PsPathInterpolator):
    pass


class PathLine(Component, W.PsPathLine):
    pass


class PathMove(Component, W.PsPathMove):
    pass


class PathMultiline(Component, W.PsPathMultiline):
    pass


class PathPercent(Component, W.PsPathPercent):
    pass


class PathPolyline(Component, W.PsPathPolyline):
    pass


class PathQuad(Component, W.PsPathQuad):
    pass


class PathSvg(Component, W.PsPathSvg):
    pass


class PathText(Component, W.PsPathText):
    pass


class PathView(Item, W.PsPathView):
    pass


class PauseAnimation(Animation, W.PsPauseAnimation):
    pass


class PinchArea(Item, W.PsPinchArea):
    pass


class PinchEvent(Component, W.PsPinchEvent):
    pass


class PinchHandler(MultiPointHandler, W.PsPinchHandler):
    pass


class PointHandler(SinglePointHandler, W.PsPointHandler):
    pass


class Positioner(Component, W.PsPositioner):
    pass


class PropertyAction(Animation, W.PsPropertyAction):
    pass


class PropertyChanges(Component, W.PsPropertyChanges):
    pass


class Rectangle(Item, W.PsRectangle):
    pass


class RegularExpressionValidator(Component, W.PsRegularExpressionValidator):
    pass


class Repeater(Item, W.PsRepeater):
    pass


class Rotation(Component, W.PsRotation):
    pass


class RotationAnimation(PropertyAnimation, W.PsRotationAnimation):
    pass


class RotationAnimator(Animator, W.PsRotationAnimator):
    pass


class Row(Item, W.PsRow):
    pass


class Scale(Component, W.PsScale):
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


class Shortcut(Component, W.PsShortcut):
    pass


class SmoothedAnimation(NumberAnimation, W.PsSmoothedAnimation):
    pass


class SpringAnimation(NumberAnimation, W.PsSpringAnimation):
    pass


class Sprite(Component, W.PsSprite):
    pass


class SpriteSequence(Item, W.PsSpriteSequence):
    pass


class State(Component, W.PsState):
    pass


class StateChangeScript(Component, W.PsStateChangeScript):
    pass


class StateGroup(Component, W.PsStateGroup):
    pass


class SystemPalette(Component, W.PsSystemPalette):
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


class TextMetrics(Component, W.PsTextMetrics):
    pass


class TouchPoint(Component, W.PsTouchPoint):
    pass


class Transform(Component, W.PsTransform):
    pass


class Transition(Component, W.PsTransition):
    pass


class Translate(Component, W.PsTranslate):
    pass


class UniformAnimator(Animator, W.PsUniformAnimator):
    pass


class Vector3dAnimation(PropertyAnimation, W.PsVector3dAnimation):
    pass


class ViewTransition(Component, W.PsViewTransition):
    pass


class WheelEvent(Component, W.PsWheelEvent):
    pass


class WheelHandler(SinglePointHandler, W.PsWheelHandler):
    pass


class Window(Component, W.PsWindow):
    pass


class XAnimator(Animator, W.PsXAnimator):
    pass


class YAnimator(Animator, W.PsYAnimator):
    pass
