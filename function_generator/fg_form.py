# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function_generator.ui'
#
# Created: Wed Apr 24 15:09:07 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fgform(object):
    def setupUi(self, fgform):
        fgform.setObjectName(_fromUtf8("fgform"))
        fgform.resize(659, 662)
        self.layoutWidget = QtGui.QWidget(fgform)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 657, 661))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.main_layout = QtGui.QGridLayout(self.layoutWidget)
        self.main_layout.setMargin(0)
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.outplot = MatplotlibWidget(self.layoutWidget)
        self.outplot.setObjectName(_fromUtf8("outplot"))
        self.main_layout.addWidget(self.outplot, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 2)
        self.aisr_edit = QtGui.QLineEdit(self.layoutWidget)
        self.aisr_edit.setObjectName(_fromUtf8("aisr_edit"))
        self.gridLayout_3.addWidget(self.aisr_edit, 0, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.aotime = QtGui.QLabel(self.layoutWidget)
        self.aotime.setObjectName(_fromUtf8("aotime"))
        self.gridLayout_3.addWidget(self.aotime, 5, 2, 1, 1)
        self.ainpts_edit = QtGui.QLineEdit(self.layoutWidget)
        self.ainpts_edit.setObjectName(_fromUtf8("ainpts_edit"))
        self.gridLayout_3.addWidget(self.ainpts_edit, 1, 2, 1, 1)
        self.aichan_box = QtGui.QComboBox(self.layoutWidget)
        self.aichan_box.setObjectName(_fromUtf8("aichan_box"))
        self.gridLayout_3.addWidget(self.aichan_box, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 4, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.aitime = QtGui.QLabel(self.layoutWidget)
        self.aitime.setObjectName(_fromUtf8("aitime"))
        self.gridLayout_3.addWidget(self.aitime, 5, 0, 1, 2)
        self.reset_box = QtGui.QCheckBox(self.layoutWidget)
        self.reset_box.setChecked(True)
        self.reset_box.setObjectName(_fromUtf8("reset_box"))
        self.gridLayout_3.addWidget(self.reset_box, 3, 2, 1, 1)
        self.main_layout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ttl = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ttl.setFont(font)
        self.ttl.setLineWidth(6)
        self.ttl.setScaledContents(False)
        self.ttl.setObjectName(_fromUtf8("ttl"))
        self.verticalLayout.addWidget(self.ttl)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.aochan_box = QtGui.QComboBox(self.layoutWidget)
        self.aochan_box.setObjectName(_fromUtf8("aochan_box"))
        self.horizontalLayout.addWidget(self.aochan_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.amp_edit = QtGui.QLineEdit(self.layoutWidget)
        self.amp_edit.setObjectName(_fromUtf8("amp_edit"))
        self.gridLayout.addWidget(self.amp_edit, 3, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.npts_edit = QtGui.QLineEdit(self.layoutWidget)
        self.npts_edit.setObjectName(_fromUtf8("npts_edit"))
        self.gridLayout.addWidget(self.npts_edit, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.sr_edit = QtGui.QLineEdit(self.layoutWidget)
        self.sr_edit.setObjectName(_fromUtf8("sr_edit"))
        self.gridLayout.addWidget(self.sr_edit, 0, 2, 1, 1)
        self.freq_edit = QtGui.QLineEdit(self.layoutWidget)
        self.freq_edit.setObjectName(_fromUtf8("freq_edit"))
        self.gridLayout.addWidget(self.freq_edit, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.wvfm_group = QtGui.QGroupBox(self.layoutWidget)
        self.wvfm_group.setObjectName(_fromUtf8("wvfm_group"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wvfm_group)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.sin_radio = QtGui.QRadioButton(self.wvfm_group)
        self.sin_radio.setChecked(True)
        self.sin_radio.setObjectName(_fromUtf8("sin_radio"))
        self.horizontalLayout_4.addWidget(self.sin_radio)
        self.square_radio = QtGui.QRadioButton(self.wvfm_group)
        self.square_radio.setObjectName(_fromUtf8("square_radio"))
        self.horizontalLayout_4.addWidget(self.square_radio)
        self.saw_radio = QtGui.QRadioButton(self.wvfm_group)
        self.saw_radio.setObjectName(_fromUtf8("saw_radio"))
        self.horizontalLayout_4.addWidget(self.saw_radio)
        self.wav_radio = QtGui.QRadioButton(self.wvfm_group)
        self.wav_radio.setObjectName(_fromUtf8("wav_radio"))
        self.horizontalLayout_4.addWidget(self.wav_radio)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.wvfm_group)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.browse_button = QtGui.QPushButton(self.layoutWidget)
        self.browse_button.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_button.sizePolicy().hasHeightForWidth())
        self.browse_button.setSizePolicy(sizePolicy)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.horizontalLayout_3.addWidget(self.browse_button)
        self.folder_edit = QtGui.QLineEdit(self.layoutWidget)
        self.folder_edit.setEnabled(False)
        self.folder_edit.setObjectName(_fromUtf8("folder_edit"))
        self.horizontalLayout_3.addWidget(self.folder_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.start_button = QtGui.QPushButton(self.layoutWidget)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontalLayout_2.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(self.layoutWidget)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.horizontalLayout_2.addWidget(self.stop_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.main_layout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.inplot = MatplotlibWidget(self.layoutWidget)
        self.inplot.setObjectName(_fromUtf8("inplot"))
        self.main_layout.addWidget(self.inplot, 1, 1, 1, 1)

        self.retranslateUi(fgform)
        QtCore.QMetaObject.connectSlotsByName(fgform)

    def retranslateUi(self, fgform):
        fgform.setWindowTitle(_translate("fgform", "Form", None))
        self.label_9.setText(_translate("fgform", "AI points to read:", None))
        self.aisr_edit.setText(_translate("fgform", "1000", None))
        self.label_8.setText(_translate("fgform", "AI sample rate:", None))
        self.aotime.setText(_translate("fgform", "AO time:", None))
        self.ainpts_edit.setText(_translate("fgform", "1000", None))
        self.label_7.setText(_translate("fgform", "AI Channel :", None))
        self.aitime.setText(_translate("fgform", "AI time:", None))
        self.reset_box.setText(_translate("fgform", "Reset display", None))
        self.ttl.setText(_translate("fgform", "Function Generator", None))
        self.label_6.setText(_translate("fgform", "AO channel :", None))
        self.label_5.setText(_translate("fgform", "frequency :", None))
        self.label_4.setText(_translate("fgform", "amplitude :", None))
        self.label_2.setText(_translate("fgform", "no. of  points:", None))
        self.amp_edit.setText(_translate("fgform", "1", None))
        self.label_3.setText(_translate("fgform", "Function", None))
        self.npts_edit.setText(_translate("fgform", "1000", None))
        self.label.setText(_translate("fgform", "sample rate (s/sec):", None))
        self.sr_edit.setText(_translate("fgform", "1000", None))
        self.freq_edit.setText(_translate("fgform", "3", None))
        self.wvfm_group.setTitle(_translate("fgform", "Waveform", None))
        self.sin_radio.setText(_translate("fgform", "sin", None))
        self.square_radio.setText(_translate("fgform", "square", None))
        self.saw_radio.setText(_translate("fgform", "sawtooth", None))
        self.wav_radio.setText(_translate("fgform", ".wav", None))
        self.browse_button.setText(_translate("fgform", "...", None))
        self.folder_edit.setText(_translate("fgform", "C:\\Users\\amy.boyle\\sampledata\\M1_FD024", None))
        self.start_button.setText(_translate("fgform", "Start", None))
        self.stop_button.setText(_translate("fgform", "Stop", None))

from matplotlibwidget import MatplotlibWidget