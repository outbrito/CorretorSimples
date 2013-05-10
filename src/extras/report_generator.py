#-*- coding: UTF-8 -*-

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.validators import Auto
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.textlabels import Label
from reportlab.platypus.flowables import Spacer, PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.xpreformatted import XPreformatted
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.spider import SpiderChart
from reportlab.graphics.widgets.markers import makeMarker

DEFAULT_DRAWING_WIDTH = 740
DEFAULT_DRAWING_HEIGHT = 480
DEFAULT_CHART_WIDTH = 540
DEFAULT_CHART_HEIGHT = 380
COLORS = [v for k,v in colors.getAllNamedColors().items()]


def getbarchart(title, data=[()], values={"min":0,"max":100,"step":5}, catNames=[], subCatNames=[]):
    
    drawing = Drawing(DEFAULT_DRAWING_WIDTH, DEFAULT_DRAWING_HEIGHT)
    
    drawing.add(String(DEFAULT_CHART_WIDTH/2,DEFAULT_CHART_HEIGHT+60,title), name='title')
    drawing.title.fontName = 'Helvetica-Bold'
    drawing.title.fontSize = 16
    
    bc = VerticalBarChart()
    bc.x = 50
    bc.y = 50
    bc.width = DEFAULT_CHART_WIDTH
    bc.height = DEFAULT_CHART_HEIGHT
    bc.data = data    

    bc.strokeColor = colors.black

    bc.valueAxis.valueMin = values["min"]
    bc.valueAxis.valueMax = values["max"]
    bc.valueAxis.valueStep = values["step"]
    bc.valueAxis.labels.fontSize = 12

    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = 8
    bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.labels.angle = 30
    bc.categoryAxis.labels.fontSize = 12

    bc.categoryAxis.categoryNames = catNames
    
    for i in range(len(data)):
        bc.bars[i].fillColor = COLORS[i]
    
    drawing.add(bc)
    drawing.add(_getswatches(bc, subCatNames))    
    
    
    return drawing


def getlinechart(title, data=[()], values={"min":0,"max":100,"step":5}, catNames=[], subCatNames=[]):
    
    drawing = Drawing(DEFAULT_DRAWING_WIDTH, DEFAULT_DRAWING_HEIGHT)
    
    drawing.add(String(DEFAULT_CHART_WIDTH/2,DEFAULT_CHART_HEIGHT+60,title), name='title')
    drawing.title.fontName = 'Helvetica-Bold'
    drawing.title.fontSize = 12
    
    lc = HorizontalLineChart()
    lc.x = 50
    lc.y = 50
    lc.width = DEFAULT_CHART_WIDTH
    lc.height = DEFAULT_CHART_HEIGHT
    
    lc.data = data
    
#    lc.joinedLines = 1
    lc.lines.symbol = makeMarker("FilledDiamond")
    lc.lineLabelFormat = "%d"
    
    lc.strokeColor = colors.black

    lc.valueAxis.valueMin = values["min"]
    lc.valueAxis.valueMax = values["max"]
    lc.valueAxis.valueStep = values["step"]
    lc.valueAxis.labels.fontSize = 12

    lc.categoryAxis.labels.boxAnchor = 'ne'
    lc.categoryAxis.labels.dx = 8
    lc.categoryAxis.labels.dy = -2
    lc.categoryAxis.labels.angle = 30
    lc.categoryAxis.labels.fontSize = 12
    
    lc.categoryAxis.categoryNames = catNames
    
    for i in range(len(data)):
        lc.lines[i].strokeColor = COLORS[i]
        lc.lines[i].strokeWidth = 3
    
    drawing.add(lc)
    drawing.add(_getswatches(lc, subCatNames))  

    return drawing


def _getswatches( chart, subCatNames ):
    "Add sample swatches to a diagram."

    swatches = Legend()
    swatches.alignment = 'right'
    swatches.x = DEFAULT_CHART_WIDTH+60
    swatches.y = DEFAULT_CHART_HEIGHT
    swatches.deltax = 60
    swatches.dxTextSpace = 10
    swatches.columnMaximum = 10
    swatches.fontSize = 10

    items = []
    for i in range(len(subCatNames)):
        items.append((COLORS[i],subCatNames[i]))
    
    
    swatches.colorNamePairs = items
    
    return swatches

#===============================================================================
#===============================================================================

def getpie():
    width = 300
    height = 150
    d = Drawing(width, height)
    pc = Pie()
    pc.x = 150
    pc.y = 50
    pc.data = [1, 50, 100, 100, 100, 100, 100, 100, 100, 50]
    pc.labels = ['0','a','b','c','d','e','f','g','h','i']
    pc.slices.strokeWidth=0.5
    pc.slices[3].popout = 20
    pc.slices[3].strokeWidth = 2
    pc.slices[3].strokeDashArray = [2,2]
    pc.slices[3].labelRadius = 1.75
    pc.slices[3].fontColor = colors.red
    d.add(pc)
    legend = Legend()
    legend.x = width-5
    legend.y = height-5
    legend.dx = 20
    legend.dy = 5
    legend.deltax = 0
    legend.boxAnchor = 'nw'
    legend.colorNamePairs=Auto(chart=pc)
    d.add(legend)
    return d






#===============================================================================
# from reportlab.graphics.shapes import Drawing, String
# from reportlab.graphics.charts.barcharts import HorizontalBarChart
# class MyBarChartDrawing(Drawing):
#    def __init__(self, width=400, height=200, *args, **kw):
#        apply(Drawing.__init__,(self,width,height)+args,kw)
#        self.add(HorizontalBarChart(), name='chart')
#        self.add(String(200,180,'Hello World'), name='title')
#        #set any shapes, fonts, colors you want here.  We'll just
#        #set a title font and place the chart within the drawing
#        self.chart.x = 20
#        self.chart.y = 20
#        self.chart.width = self.width - 20
#        self.chart.height = self.height - 40
#        self.title.fontName = 'Helvetica-Bold'
#        self.title.fontSize = 12
#        
#        self.chart.data = [[100,150,200,235]]
#        
# if __name__=='__main__':
#    #use the standard 'save' method to save barchart.gif, barchart.pdf etc
#    #for quick feedback while working.
#   
#    MyBarChartDrawing().save(formats=['gif','png','jpg','pdf'],outDir='.',fnRoot='barchart')
#===============================================================================