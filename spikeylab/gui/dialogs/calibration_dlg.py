import re

from PyQt4 import QtGui, QtCore
from caldialog_form import Ui_CalibrationDialog
from spikeylab.gui.plotting.pyqtgraph_widgets import SimplePlotWidget

class CalibrationDialog(QtGui.QDialog):
    """Dialog to set current calibration and reference point for intensity-frequency-voltage"""
    def __init__(self, fscale, defaultVals=None, datafile=None):
        QtGui.QDialog.__init__(self, None)
        self.ui = Ui_CalibrationDialog()
        self.ui.setupUi(self)
        
        if datafile is not None:
            cal_names = datafile.calibration_list()
            self.ui.calChoiceCmbbx.insertItems(0, cal_names)
        if defaultVals is not None:
            if defaultVals['calname'] != '':
                calidx = cal_names.index(defaultVals['calname'])
                self.ui.calChoiceCmbbx.setCurrentIndex(calidx)
            self.ui.calfileRadio.setChecked(defaultVals['use_calfile'])
            self.ui.frangeLowSpnbx.setValue(defaultVals['frange'][0]/fscale)
            self.ui.frangeHighSpnbx.setValue(defaultVals['frange'][1]/fscale)
        self.fscale = fscale
        self.pw = None
        self.datafile = datafile
        # default Vals can't be none, or I need a separate calf arg
        self.calf = defaultVals['calf']

    def maxRange(self):
        try:
            x, freqs = self.datafile.get_calibration(self.ui.calChoiceCmbbx.currentText(), self.calf)
            self.ui.frangeLowSpnbx.setValue(freqs[0]/self.fscale)
            self.ui.frangeHighSpnbx.setValue(freqs[-1]/self.fscale)
            print 'set freq range', freqs[0], freqs[-1], freqs[0]/self.fscale, freqs[-1]/self.fscale
        except IOError:
            QtGui.QMessageBox.warning(self, "File Read Error", "Unable to read calibration file")
        except KeyError:
            QtGui.QMessageBox.warning(self, "File Data Error", "Unable to find data in file")
           
    def plotCurve(self):
        try:
            attenuations, freqs = self.datafile.get_calibration(self.ui.calChoiceCmbbx.currentText(), self.calf)
            self.pw = SimplePlotWidget(freqs, attenuations, parent=self)
            self.pw.setWindowFlags(QtCore.Qt.Window)
            self.pw.setLabels('Frequency', 'Attenuation', 'Calibration Curve')
            self.pw.show()
        except IOError:
            QtGui.QMessageBox.warning(self, "File Read Error", "Unable to read calibration file")
        except KeyError:
            QtGui.QMessageBox.warning(self, "File Data Error", "Unable to find data in file")

    def values(self):
        results = {}
        results['use_calfile'] = self.ui.calfileRadio.isChecked()
        results['calname'] = self.ui.calChoiceCmbbx.currentText()
        results['frange'] = (self.ui.frangeLowSpnbx.value()*self.fscale, self.ui.frangeHighSpnbx.value()*self.fscale)
        return results

    def conditional_accept(self):
        if self.ui.calfileRadio.isChecked() and self.ui.calChoiceCmbbx.currentText() == '':
            self.ui.noneRadio.setChecked(True)
        if self.ui.calfileRadio.isChecked():
            try:
                x, freqs = self.datafile.get_calibration(self.ui.calChoiceCmbbx.currentText(), self.calf)
            except IOError:
                QtGui.QMessageBox.warning(self, "File Read Error", "Unable to read calibration file")
                return
            except KeyError:
                QtGui.QMessageBox.warning(self, "File Data Error", "Unable to find data in file")
                return
            if self.ui.frangeLowSpnbx.value()*self.fscale < freqs[0] or \
                self.ui.frangeHighSpnbx.value()*self.fscale > freqs[-1]:
                QtGui.QMessageBox.warning(self, "Invalid Frequency Range", 
                    "Provided frequencys outside of calibration file range of {} - {} Hz".format(freqs[0], freqs[-1]))
                return

        self.accept()