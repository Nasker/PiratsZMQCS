# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\modpiratsweight_big.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModulePiratsWeightBig(object):
    def setupUi(self, ModulePiratsWeightBig):
        ModulePiratsWeightBig.setObjectName("ModulePiratsWeightBig")
        ModulePiratsWeightBig.resize(1060, 716)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(ModulePiratsWeightBig)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.ledit_channel_set = QtWidgets.QLineEdit(ModulePiratsWeightBig)
        self.ledit_channel_set.setText("")
        self.ledit_channel_set.setObjectName("ledit_channel_set")
        self.horizontalLayout_11.addWidget(self.ledit_channel_set)
        self.pb_channel_set = QtWidgets.QPushButton(ModulePiratsWeightBig)
        self.pb_channel_set.setObjectName("pb_channel_set")
        self.horizontalLayout_11.addWidget(self.pb_channel_set)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.line_6 = QtWidgets.QFrame(ModulePiratsWeightBig)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_10.addWidget(self.line_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spin_period_set = QtWidgets.QSpinBox(ModulePiratsWeightBig)
        self.spin_period_set.setMinimum(10)
        self.spin_period_set.setMaximum(10000)
        self.spin_period_set.setSingleStep(10)
        self.spin_period_set.setProperty("value", 1000)
        self.spin_period_set.setObjectName("spin_period_set")
        self.horizontalLayout.addWidget(self.spin_period_set)
        self.pb_period_set = QtWidgets.QPushButton(ModulePiratsWeightBig)
        self.pb_period_set.setObjectName("pb_period_set")
        self.horizontalLayout.addWidget(self.pb_period_set)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(ModulePiratsWeightBig)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_10.addWidget(self.line_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.lbl_set_channel_recvd = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.lbl_set_channel_recvd.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_set_channel_recvd.setFont(font)
        self.lbl_set_channel_recvd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd.setObjectName("lbl_set_channel_recvd")
        self.horizontalLayout_12.addWidget(self.lbl_set_channel_recvd)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.lbl_set_channel_recvd_on = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.lbl_set_channel_recvd_on.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd_on.setObjectName("lbl_set_channel_recvd_on")
        self.verticalLayout_6.addWidget(self.lbl_set_channel_recvd_on)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(ModulePiratsWeightBig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.lbl_last_weight = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.lbl_last_weight.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_last_weight.setFont(font)
        self.lbl_last_weight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_last_weight.setObjectName("lbl_last_weight")
        self.horizontalLayout_7.addWidget(self.lbl_last_weight)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(ModulePiratsWeightBig)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_8.addWidget(self.line_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_acq_btn = QtWidgets.QPushButton(ModulePiratsWeightBig)
        self.start_acq_btn.setObjectName("start_acq_btn")
        self.verticalLayout.addWidget(self.start_acq_btn)
        self.stop_acq_btn = QtWidgets.QPushButton(ModulePiratsWeightBig)
        self.stop_acq_btn.setObjectName("stop_acq_btn")
        self.verticalLayout.addWidget(self.stop_acq_btn)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.line_4 = QtWidgets.QFrame(ModulePiratsWeightBig)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_11.addWidget(self.line_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(ModulePiratsWeightBig)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.chart = PlotWidget(ModulePiratsWeightBig)
        self.chart.setObjectName("chart")
        self.horizontalLayout_6.addWidget(self.chart)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.btn_clear_chart = QtWidgets.QPushButton(ModulePiratsWeightBig)
        self.btn_clear_chart.setObjectName("btn_clear_chart")
        self.horizontalLayout_6.addWidget(self.btn_clear_chart)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.retranslateUi(ModulePiratsWeightBig)
        QtCore.QMetaObject.connectSlotsByName(ModulePiratsWeightBig)

    def retranslateUi(self, ModulePiratsWeightBig):
        _translate = QtCore.QCoreApplication.translate
        ModulePiratsWeightBig.setWindowTitle(_translate("ModulePiratsWeightBig", "Pirats Weight Module"))
        self.label.setText(_translate("ModulePiratsWeightBig", "Pirats Board Weight Sense Monitor and Control"))
        self.label_9.setText(_translate("ModulePiratsWeightBig", "Select Channel(s)"))
        self.pb_channel_set.setText(_translate("ModulePiratsWeightBig", "Send"))
        self.label_2.setText(_translate("ModulePiratsWeightBig", "Measurement Period(ms)"))
        self.pb_period_set.setText(_translate("ModulePiratsWeightBig", "Send"))
        self.label_10.setText(_translate("ModulePiratsWeightBig", "Received:"))
        self.lbl_set_channel_recvd.setText(_translate("ModulePiratsWeightBig", "-"))
        self.lbl_set_channel_recvd_on.setText(_translate("ModulePiratsWeightBig", "on -"))
        self.label_7.setText(_translate("ModulePiratsWeightBig", "Weight Asyncs"))
        self.label_3.setText(_translate("ModulePiratsWeightBig", "Last Weight(s) Received"))
        self.lbl_last_weight.setText(_translate("ModulePiratsWeightBig", "0.0"))
        self.start_acq_btn.setText(_translate("ModulePiratsWeightBig", "Start ACQ"))
        self.stop_acq_btn.setText(_translate("ModulePiratsWeightBig", "Stop ACQ"))
        self.label_8.setText(_translate("ModulePiratsWeightBig", "Weight Chart"))
        self.btn_clear_chart.setText(_translate("ModulePiratsWeightBig", "Clear Chart"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModulePiratsWeightBig = QtWidgets.QWidget()
    ui = Ui_ModulePiratsWeightBig()
    ui.setupUi(ModulePiratsWeightBig)
    ModulePiratsWeightBig.show()
    sys.exit(app.exec_())
