# from traits.etsconfig.etsconfig import ETSConfig
from enthought.etsconfig.etsconfig import ETSConfig
ETSConfig.toolkit = "qt4"
from enthought.enable.api import Window
from enthought.chaco.api import create_line_plot, VPlotContainer, ArrayPlotData, Plot, OverlayPlotContainer, ScatterPlot
from chaco.tools.api import PanTool, ZoomTool, DragZoom, SelectTool, SimpleInspectorTool, ScatterInspector
from enthought.enable.base_tool import BaseTool
from chaco.tools.cursor_tool import CursorTool
from traits.api import HasTraits, Instance
from enthought.chaco.abstract_mapper import AbstractMapper

import sys, random
import math
import numpy as np
from PyQt4 import QtGui, QtCore

class LiveWindow(QtGui.QMainWindow):
    def __init__(self, nsubplots):
        QtGui.QMainWindow.__init__(self)
        self.mainWidget = QtGui.QWidget(self) # dummy widget to contain layout manager
        self.plotview = Plotter(self, nsubplots)

        layout = QtGui.QVBoxLayout(self.mainWidget)
        layout.setObjectName("masterlayout")
        layout.addWidget(self.plotview.widget)

        self.resize(600,400)

        self.setCentralWidget(self.mainWidget)

    def draw_line(self, axnum, linenum, x, y):
        self.plotview.update_data(axnum, linenum, x, y)

class ScrollingWindow(QtGui.QMainWindow):
    def __init__(self, nsubplots, deltax, windowsize=1):
        QtGui.QMainWindow.__init__(self)
        self.mainWidget = QtGui.QWidget(self) # dummy widget to contain layout manager
        self.plotview = ScrollingPlotter(self, nsubplots, deltax, windowsize)

        layout = QtGui.QVBoxLayout(self.mainWidget)
        layout.setObjectName("masterlayout")
        layout.addWidget(self.plotview.widget)

        self.resize(600,400)

        self.setCentralWidget(self.mainWidget)

    def append(self, y, axnum=0):
        self.plotview.update_data(axnum, y)

class DataPlotWidget(QtGui.QWidget):
    def __init__(self, parent=None, nsubplots=1, orientation='h'):
        QtGui.QWidget.__init__(self, parent)
        self.plotview = Plotter(self, nsubplots, orientation=orientation)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.plotview.widget)
        self.setLayout(layout)

    def update_data(self, *args, **kwargs):
        self.plotview.update_data(*args, **kwargs)

    def resizeEvent(self, event):
        self.plotview.window.component.first_draw = True

    def set_xlim(self, *args, **kwargs):
        self.plotview.set_xlim(*args, **kwargs)

class ImageWidget(QtGui.QWidget):
    def __init__(self, parent=None, nsubplots=1):
        QtGui.QWidget.__init__(self, parent)
        self.plotview = ImagePlotter(self, nsubplots)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.plotview.widget)
        self.setLayout(layout)

    def update_data(self, *args, **kwargs):
        self.plotview.update_data(*args, **kwargs)

    def set_xlim(self, *args, **kwargs):
        self.plotview.set_xlim(*args, **kwargs)

class TraceWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        trait_object = SpecialPlotter()
        self.window = Window(self, -1, component=trait_object.plot)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.window.control)
        self.setLayout(layout)
        self.traits = trait_object
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuRequested)

    def update_data(self, *args, **kwargs):
        self.traits.update_data(*args, **kwargs)

    def set_xlim(self, *args, **kwargs):
        self.traits.set_xlim(*args, **kwargs)

    def resizeEvent(self, event):
        tp_bounds = self.traits.trace_plot.bounds
        # print 'trace plot', self.traits.trace_plot.position, tp_bounds
        # print 'stim plot', self.traits.stim_plot.position
        self.traits.stim_plot.set(position=[50,tp_bounds[1]-self.traits.stim_plot_height]) 

    def contextMenuRequested(self, point):
        menu = QtGui.QMenu()
        traits_action = menu.addAction("reset axis limits")
        traits_action.triggered.connect(self.traits.reset_lims)
        menu.exec_(self.mapToGlobal(point))

class Plotter():
    def __init__(self, parent, nsubplots=1, orientation='h'):
        self.plotdata = []
        for isubplot in range(nsubplots):
            self.plotdata.append(ArrayPlotData(x=np.array([]),  y=np.array([])))
        self.window, self.plots = self.create_plot(parent, orientation)
        self.widget = self.window.control
        self.index_mapper = Instance(AbstractMapper)
        
    def update_data(self, x, y, axnum=0, linenum=0):
        self.plotdata[axnum].set_data("x", x)
        self.plotdata[axnum].set_data("y", y)

    def set_xlim(self, lim, axnum=0):
        self.plots[axnum].range2d.x_range.low = lim[0]
        self.plots[axnum].range2d.x_range.high = lim[1]

    def create_plot(self, parent, orientation):
        plots = []
        for idata in self.plotdata:
            print idata.get_data('x')
            # plot = create_line_plot([idata.get_data('x'), idata.get_data('y')], 
            #                         index_sort='ascending', add_axis=True,)
            plot = Plot(idata, padding=50, border_visible=True)
            plot.plot(("x", "y"), name="data plot", color="green")
            plot.orientation = orientation
            plot.padding_top = 10
            plot.padding_bottom = 10
            plot.tools.append(PanTool(plot))
            plot.tools.append(ZoomTool(plot))
            # plot.overlays.append(CursorTool(plot,
            #             drag_button="left",
            #             color='blue'))
            # plot.tools.append(SimpleInspectorTool(plot))
            # plot.tools.append(MyPointMarker(plot))
            # plot.tools.append(MyTool(plot, selection_mode="single"))
            # plot.tools.append(MyScatterInspector(plot))

            plots.append(plot)

        plots[0].padding_bottom = 30
        plots[-1].padding_top = 30
        container = VPlotContainer(*plots)
        container.spacing = 0

        return Window(parent, -1, component=container), plots

class SpecialPlotter(HasTraits):
    plot = Instance(OverlayPlotContainer)
    # trace_data = ArrayPlotData
    # times_index = Array
    # response_data = Array
    # spike_data = Array

    # def __init__(self):
    
    def _plot_default(self):
        #make some data
        index = np.linspace(-10,10,512)
        value = np.sin(index)
        self.trace_data = ArrayPlotData(times=[], response=[], spikes=[])
        value = np.sin(3*index)
        self.stim_data = ArrayPlotData(times=[], signal=[])

        #create a LinePlot instance and add it to the subcontainer
        # trace_plot = create_line_plot([index, value], add_grid=True,
        #                         add_axis=True, index_sort='ascending')
        # raster_plot = create_scatter_plot([index, value])

        trace_plot = Plot(self.trace_data)
        trace_plot.plot(('times', 'response'), type='line', name='response potential')
        trace_plot.plot(('times', 'spikes'), type='scatter', name='detected spikes')
        trace_plot.set(bounds=[600,500], position=[50,50])

        self.stim_plot_height = 20
        stim_plot = Plot(self.stim_data)
        stim_plot.plot(('times', 'signal'), type='line', 
                        name='stim signal', color='blue')
        stim_plot.set(resizable='h',
                      bounds=[600,self.stim_plot_height+30], 
                      position=[50,350], 
                      border_visible=False,
                      overlay_border=False)
        stim_plot.y_axis.orientation = "right"
        stim_plot.x_axis.axis_line_visible = False
        stim_plot.x_axis.tick_visible = False
        stim_plot.x_axis.tick_label_formatter = self.noticks
        stim_plot.y_grid.visible = False

        trace_plot.tools.append(PanTool(trace_plot))
        trace_plot.overlays.append(ZoomTool(trace_plot))

        # link x-axis ranges
        trace_plot.index_range = stim_plot.index_range

        container = OverlayPlotContainer()
        # self.plot = container
        container.add(trace_plot)
        container.add(stim_plot)

        self.trace_plot = trace_plot
        self.stim_plot = stim_plot
        return container

    def update_data(self, data, axeskey, datakey):
        if axeskey == 'stim':
            self.stim_data.set_data(datakey, data)
        if axeskey == 'response':
            self.trace_data.set_data(datakey, data)

    def set_xlim(self, lim):
        self.trace_plot.index_range.low = lim[0]
        self.trace_plot.index_range.high = lim[1]

    def set_ylim(self, lim):
        self.trace_plot.value_range.low = lim[0]
        self.trace_plot.value_range.high = lim[1]

    def reset_lims(self):
        xdata = self.trace_data.get_data('times')
        self.set_xlim((xdata[0],xdata[-1]))
        ydata = self.trace_data.get_data('response')
        self.set_ylim((ydata.min(), ydata.max()))

    def noticks(self,num):
        return ''

class ScrollingPlotter(Plotter):
    def __init__(self, parent, nsubplots, deltax, windowsize=1):
        Plotter.__init__(self, parent, nsubplots)
        self.plots = self.window.component.components
        # time steps between data points
        self.deltax = deltax
        print "delta x", deltax
        # time window of display (seconds)
        self.windowsize = windowsize
        for plot in self.plots:
            plot.range2d.x_range.low = 0
            plot.range2d.x_range.high = windowsize


        self.plotdata[0].set_data('x', [-1])
        self.plotdata[0].set_data('y', [0])

    def update_data(self, y, axnum=0):
        # append the y data and append appropriate number of 
        # x points
        points_to_add = len(y)
        xdata = self.plotdata[axnum].get_data('x')
        x_to_append = np.arange(xdata[-1]+self.deltax, 
                            xdata[-1]+self.deltax+(self.deltax*points_to_add),
                            self.deltax)
        xdata = np.append(xdata, x_to_append)
        self.plotdata[axnum].set_data("x", xdata)
        ydata = self.plotdata[axnum].get_data('y')
        ydata = np.append(ydata,y)
        self.plotdata[axnum].set_data("y", ydata)
        
        # now scroll axis limits
        if self.plots[axnum].range2d.x_range.high <= xdata[-1]:
            self.plots[axnum].range2d.x_range.high += self.deltax*points_to_add
            self.plots[axnum].range2d.x_range.low += self.deltax*points_to_add

class ImagePlotter():
    def __init__(self, parent=None, nsubplots=1):
        self.plotdata = []
        for isubplot in range(nsubplots):
            pd = ArrayPlotData()
            pd.set_data('imagedata', np.zeros((5,5)))
            self.plotdata.append(pd)
        self.window = self.create_plot(parent)
        self.widget = self.window.control
        self.plots = self.window.component.components

    def update_data(self, imgdata, axnum=0, xaxis=None, yaxis=None):
        self.plotdata[axnum].set_data("imagedata", imgdata)
        # set CMapImagePlot axes data, assume only one renderer per axes
        if xaxis is not None and yaxis is not None:
            self.plots[axnum].components[0].index.set_data(xaxis, yaxis)
        self.window.component.components[axnum].request_redraw()

    def set_xlim(self, lim, axnum=0):
        self.plots[axnum].range2d.x_range.low = lim[0]
        self.plots[axnum].range2d.x_range.high = lim[1]
        
    def create_plot(self, parent):
        plots = []
        for data in self.plotdata:
            plot = Plot(data)
            plot.img_plot('imagedata', name="spectrogram")
            plot.padding_top = 10
            plot.padding_bottom = 10
            plot.tools.append(PanTool(plot))
            plot.tools.append(ZoomTool(plot))
            plots.append(plot)

        plots[0].padding_bottom = 30
        plots[-1].padding_top = 30
        container = VPlotContainer(*plots)
        container.spacing = 0

        return Window(parent, -1, component=container)


class MyTool(SelectTool):

    # def dispatch(self,event, suffix):
    #     print event, suffix

    def normal_left_down(self, event):
        print 'nld', event
        super(MyTool,self).normal_left_down(event)        

    def _select(self, event, append):
        print 'limburger', event, append
        indxs = self.component.index_mapper(event.x)
        # hit = self.component.hittest((event.x, event.y))
        # print 'hit', hit
        #super(MyTool, self)._select(*args)

    def _get_selection_state(self, event):
        print 'gss', event
        return (False, True)

class MyScatterInspector(ScatterInspector):
    def normal_left_down(self, event):
        print 'nld', event
        super(MyScatterInspector,self).normal_left_down(event)

    def _select(self, *args, **kwargs):
        print 'limburger', args
        super(MyScatterInspector, self)._select(*args, **kwargs)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    # plot = DataPlotWidget()
    plot = TraceWidget()
    plot.resize(600, 400)
    plot.show()

    # x = np.arange(200)
    # y = random.randint(0,10) * np.sin(x)
    # plot.update_data(x,y)

    sys.exit(app.exec_())