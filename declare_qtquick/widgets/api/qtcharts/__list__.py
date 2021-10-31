from .__base__ import *


class AbstractSeries(Component, W.PsAbstractSeries):
    pass


class AbstractBarSeries(AbstractSeries, W.PsAbstractBarSeries):
    pass


class AbstractAxis(Component, W.PsAbstractAxis):
    pass


class XYSeries(AbstractSeries, W.PsXYSeries):
    pass


class ChartView(Component, W.PsChartView):
    pass


class AreaSeries(AbstractSeries, W.PsAreaSeries):
    pass


class BarCategoryAxis(AbstractAxis, W.PsBarCategoryAxis):
    pass


class BarSeries(AbstractBarSeries, W.PsBarSeries):
    pass


class BarSet(Component, W.PsBarSet):
    pass


class BoxPlotSeries(AbstractSeries, W.PsBoxPlotSeries):
    pass


class BoxSet(Component, W.PsBoxSet):
    pass


class CandlestickSeries(AbstractSeries, W.PsCandlestickSeries):
    pass


class CandlestickSet(Component, W.PsCandlestickSet):
    pass


class CategoryAxis(AbstractAxis, W.PsCategoryAxis):
    pass


class CategoryRange(Component, W.PsCategoryRange):
    pass


class DateTimeAxis(AbstractAxis, W.PsDateTimeAxis):
    pass


class HBarModelMapper(Component, W.PsHBarModelMapper):
    pass


class HBoxPlotModelMapper(Component, W.PsHBoxPlotModelMapper):
    pass


class HCandlestickModelMapper(Component, W.PsHCandlestickModelMapper):
    pass


class HorizontalBarSeries(AbstractBarSeries, W.PsHorizontalBarSeries):
    pass


class HorizontalPercentBarSeries(AbstractBarSeries, W.PsHorizontalPercentBarSeries):
    pass


class HorizontalStackedBarSeries(AbstractBarSeries, W.PsHorizontalStackedBarSeries):
    pass


class HPieModelMapper(Component, W.PsHPieModelMapper):
    pass


class HXYModelMapper(Component, W.PsHXYModelMapper):
    pass


class Legend(Component, W.PsLegend):
    pass


class LineSeries(XYSeries, W.PsLineSeries):
    pass


class LogValueAxis(AbstractAxis, W.PsLogValueAxis):
    pass


class Margins(Component, W.PsMargins):
    pass


class PercentBarSeries(AbstractBarSeries, W.PsPercentBarSeries):
    pass


class PieSeries(AbstractSeries, W.PsPieSeries):
    pass


class PieSlice(Component, W.PsPieSlice):
    pass


class PolarChartView(ChartView, W.PsPolarChartView):
    pass


class ScatterSeries(XYSeries, W.PsScatterSeries):
    pass


class SplineSeries(XYSeries, W.PsSplineSeries):
    pass


class StackedBarSeries(AbstractBarSeries, W.PsStackedBarSeries):
    pass


class ValueAxis(AbstractAxis, W.PsValueAxis):
    pass


class VBarModelMapper(Component, W.PsVBarModelMapper):
    pass


class VBoxPlotModelMapper(Component, W.PsVBoxPlotModelMapper):
    pass


class VCandlestickModelMapper(Component, W.PsVCandlestickModelMapper):
    pass


class VPieModelMapper(Component, W.PsVPieModelMapper):
    pass


class VXYModelMapper(Component, W.PsVXYModelMapper):
    pass


class XYPoint(Component, W.PsXYPoint):
    pass
