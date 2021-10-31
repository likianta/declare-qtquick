from .__base__ import *


class AbstractSeries(C, W.PsAbstractSeries):
    pass


class AbstractBarSeries(AbstractSeries, W.PsAbstractBarSeries):
    pass


class AbstractAxis(C, W.PsAbstractAxis):
    pass


class XYSeries(AbstractSeries, W.PsXYSeries):
    pass


class ChartView(C, W.PsChartView):
    pass


class AreaSeries(AbstractSeries, W.PsAreaSeries):
    pass


class BarCategoryAxis(AbstractAxis, W.PsBarCategoryAxis):
    pass


class BarSeries(AbstractBarSeries, W.PsBarSeries):
    pass


class BarSet(C, W.PsBarSet):
    pass


class BoxPlotSeries(AbstractSeries, W.PsBoxPlotSeries):
    pass


class BoxSet(C, W.PsBoxSet):
    pass


class CandlestickSeries(AbstractSeries, W.PsCandlestickSeries):
    pass


class CandlestickSet(C, W.PsCandlestickSet):
    pass


class CategoryAxis(AbstractAxis, W.PsCategoryAxis):
    pass


class CategoryRange(C, W.PsCategoryRange):
    pass


class DateTimeAxis(AbstractAxis, W.PsDateTimeAxis):
    pass


class HBarModelMapper(C, W.PsHBarModelMapper):
    pass


class HBoxPlotModelMapper(C, W.PsHBoxPlotModelMapper):
    pass


class HCandlestickModelMapper(C, W.PsHCandlestickModelMapper):
    pass


class HorizontalBarSeries(AbstractBarSeries, W.PsHorizontalBarSeries):
    pass


class HorizontalPercentBarSeries(AbstractBarSeries, W.PsHorizontalPercentBarSeries):
    pass


class HorizontalStackedBarSeries(AbstractBarSeries, W.PsHorizontalStackedBarSeries):
    pass


class HPieModelMapper(C, W.PsHPieModelMapper):
    pass


class HXYModelMapper(C, W.PsHXYModelMapper):
    pass


class Legend(C, W.PsLegend):
    pass


class LineSeries(XYSeries, W.PsLineSeries):
    pass


class LogValueAxis(AbstractAxis, W.PsLogValueAxis):
    pass


class Margins(C, W.PsMargins):
    pass


class PercentBarSeries(AbstractBarSeries, W.PsPercentBarSeries):
    pass


class PieSeries(AbstractSeries, W.PsPieSeries):
    pass


class PieSlice(C, W.PsPieSlice):
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


class VBarModelMapper(C, W.PsVBarModelMapper):
    pass


class VBoxPlotModelMapper(C, W.PsVBoxPlotModelMapper):
    pass


class VCandlestickModelMapper(C, W.PsVCandlestickModelMapper):
    pass


class VPieModelMapper(C, W.PsVPieModelMapper):
    pass


class VXYModelMapper(C, W.PsVXYModelMapper):
    pass


class XYPoint(C, W.PsXYPoint):
    pass
