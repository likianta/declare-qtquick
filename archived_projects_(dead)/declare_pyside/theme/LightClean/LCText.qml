import QtQuick
import LKQmlSide
import "./LCStyle/palette.js" as LCPalette
import "./LCStyle/typography.js" as LCTypo

Text {
    id: root
    color: LCPalette.TextNormal
    font.pixelSize: LCTypo.FontSizeM

    property string p_alignment: "center"  // see `LCLayout.easyAlign`
    property alias  p_bold: root.font.bold
    property alias  p_color: root.color
    property alias  p_size: root.font.pixelSize
    property alias  p_text: root.text

    Component.onCompleted: {
        LayoutHelper.easyAlign(root, p_alignment)
    }
}
