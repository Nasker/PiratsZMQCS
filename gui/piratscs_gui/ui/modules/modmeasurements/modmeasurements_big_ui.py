# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\modmeasurements_big.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModuleMeasurementsBig(object):
    def setupUi(self, ModuleMeasurementsBig):
        ModuleMeasurementsBig.setObjectName("ModuleMeasurementsBig")
        ModuleMeasurementsBig.resize(1226, 888)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(ModuleMeasurementsBig)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.ledit_measurement_set = QtWidgets.QLineEdit(ModuleMeasurementsBig)
        self.ledit_measurement_set.setText("")
        self.ledit_measurement_set.setObjectName("ledit_measurement_set")
        self.horizontalLayout_11.addWidget(self.ledit_measurement_set)
        self.pb_measurement_set = QtWidgets.QPushButton(ModuleMeasurementsBig)
        self.pb_measurement_set.setObjectName("pb_measurement_set")
        self.horizontalLayout_11.addWidget(self.pb_measurement_set)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.measWeightCheckBox = QtWidgets.QCheckBox(ModuleMeasurementsBig)
        self.measWeightCheckBox.setObjectName("measWeightCheckBox")
        self.gridLayout.addWidget(self.measWeightCheckBox, 1, 0, 1, 1)
        self.measTempCheckBox = QtWidgets.QCheckBox(ModuleMeasurementsBig)
        self.measTempCheckBox.setObjectName("measTempCheckBox")
        self.gridLayout.addWidget(self.measTempCheckBox, 0, 0, 1, 1)
        self.measPressureCheckBox = QtWidgets.QCheckBox(ModuleMeasurementsBig)
        self.measPressureCheckBox.setObjectName("measPressureCheckBox")
        self.gridLayout.addWidget(self.measPressureCheckBox, 0, 1, 1, 1)
        self.measVoltageCheckBox = QtWidgets.QCheckBox(ModuleMeasurementsBig)
        self.measVoltageCheckBox.setObjectName("measVoltageCheckBox")
        self.gridLayout.addWidget(self.measVoltageCheckBox, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.line_2 = QtWidgets.QFrame(ModuleMeasurementsBig)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_10.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_2 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        self.spin_period_set = QtWidgets.QSpinBox(ModuleMeasurementsBig)
        self.spin_period_set.setMinimum(10)
        self.spin_period_set.setMaximum(10000)
        self.spin_period_set.setSingleStep(10)
        self.spin_period_set.setProperty("value", 1000)
        self.spin_period_set.setObjectName("spin_period_set")
        self.horizontalLayout_13.addWidget(self.spin_period_set)
        self.pb_period_set = QtWidgets.QPushButton(ModuleMeasurementsBig)
        self.pb_period_set.setObjectName("pb_period_set")
        self.horizontalLayout_13.addWidget(self.pb_period_set)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.line_6 = QtWidgets.QFrame(ModuleMeasurementsBig)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_10.addWidget(self.line_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.lbl_set_channel_recvd = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.lbl_set_channel_recvd.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_set_channel_recvd.setFont(font)
        self.lbl_set_channel_recvd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd.setObjectName("lbl_set_channel_recvd")
        self.horizontalLayout_12.addWidget(self.lbl_set_channel_recvd)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.lbl_set_channel_recvd_on = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.lbl_set_channel_recvd_on.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd_on.setObjectName("lbl_set_channel_recvd_on")
        self.verticalLayout_6.addWidget(self.lbl_set_channel_recvd_on)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(ModuleMeasurementsBig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.lbl_last_measurement = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.lbl_last_measurement.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_last_measurement.setFont(font)
        self.lbl_last_measurement.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_last_measurement.setObjectName("lbl_last_measurement")
        self.verticalLayout_4.addWidget(self.lbl_last_measurement)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(ModuleMeasurementsBig)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_8.addWidget(self.line_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_11 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        self.ledit_filename_set = QtWidgets.QLineEdit(ModuleMeasurementsBig)
        self.ledit_filename_set.setObjectName("ledit_filename_set")
        self.horizontalLayout_14.addWidget(self.ledit_filename_set)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_14)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_acq_btn = QtWidgets.QPushButton(ModuleMeasurementsBig)
        self.start_acq_btn.setObjectName("start_acq_btn")
        self.verticalLayout_2.addWidget(self.start_acq_btn)
        self.stop_acq_btn = QtWidgets.QPushButton(ModuleMeasurementsBig)
        self.stop_acq_btn.setObjectName("stop_acq_btn")
        self.verticalLayout_2.addWidget(self.stop_acq_btn)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.line_4 = QtWidgets.QFrame(ModuleMeasurementsBig)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_11.addWidget(self.line_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_13.addItem(spacerItem4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.tempGraph = PlotWidget(ModuleMeasurementsBig)
        self.tempGraph.setObjectName("tempGraph")
        self.horizontalLayout_4.addWidget(self.tempGraph)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_4 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_15.addWidget(self.label_4)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_15)
        self.voltageGraph = PlotWidget(ModuleMeasurementsBig)
        self.voltageGraph.setObjectName("voltageGraph")
        self.horizontalLayout_6.addWidget(self.voltageGraph)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_5 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_14.addWidget(self.label_5)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.pressureGraph = PlotWidget(ModuleMeasurementsBig)
        self.pressureGraph.setObjectName("pressureGraph")
        self.horizontalLayout_5.addWidget(self.pressureGraph)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_6 = QtWidgets.QLabel(ModuleMeasurementsBig)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_12.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.weightGraph = PlotWidget(ModuleMeasurementsBig)
        self.weightGraph.setObjectName("weightGraph")
        self.horizontalLayout_3.addWidget(self.weightGraph)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.btn_clear_chart = QtWidgets.QPushButton(ModuleMeasurementsBig)
        self.btn_clear_chart.setObjectName("btn_clear_chart")
        self.horizontalLayout_2.addWidget(self.btn_clear_chart)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ModuleMeasurementsBig)
        QtCore.QMetaObject.connectSlotsByName(ModuleMeasurementsBig)

    def retranslateUi(self, ModuleMeasurementsBig):
        _translate = QtCore.QCoreApplication.translate
        ModuleMeasurementsBig.setWindowTitle(_translate("ModuleMeasurementsBig", "Measurements Module"))
        self.label.setText(_translate("ModuleMeasurementsBig", "Pirats Board Measurements Manager"))
        self.label_9.setText(_translate("ModuleMeasurementsBig", "Select Measurements"))
        self.pb_measurement_set.setText(_translate("ModuleMeasurementsBig", "Send"))
        self.measWeightCheckBox.setText(_translate("ModuleMeasurementsBig", "Weight Measurement"))
        self.measTempCheckBox.setText(_translate("ModuleMeasurementsBig", "Temperature Measurement"))
        self.measPressureCheckBox.setText(_translate("ModuleMeasurementsBig", "Pressure Measurement"))
        self.measVoltageCheckBox.setText(_translate("ModuleMeasurementsBig", "Voltages Measurement"))
        self.label_2.setText(_translate("ModuleMeasurementsBig", "Measurement Period(ms)"))
        self.pb_period_set.setText(_translate("ModuleMeasurementsBig", "Send"))
        self.label_10.setText(_translate("ModuleMeasurementsBig", "Received:"))
        self.lbl_set_channel_recvd.setText(_translate("ModuleMeasurementsBig", "-"))
        self.lbl_set_channel_recvd_on.setText(_translate("ModuleMeasurementsBig", "on -"))
        self.label_3.setText(_translate("ModuleMeasurementsBig", "Last Async(s) Received"))
        self.lbl_last_measurement.setText(_translate("ModuleMeasurementsBig", "0.0"))
        self.label_11.setText(_translate("ModuleMeasurementsBig", "File Name"))
        self.start_acq_btn.setText(_translate("ModuleMeasurementsBig", "Start Measurement"))
        self.stop_acq_btn.setText(_translate("ModuleMeasurementsBig", "Stop Measurement"))
        self.label_8.setText(_translate("ModuleMeasurementsBig", "Temperature"))
        self.label_4.setText(_translate("ModuleMeasurementsBig", "Voltage"))
        self.label_5.setText(_translate("ModuleMeasurementsBig", "Pressure"))
        self.label_6.setText(_translate("ModuleMeasurementsBig", "Weight"))
        self.btn_clear_chart.setText(_translate("ModuleMeasurementsBig", "Clear Graphs"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModuleMeasurementsBig = QtWidgets.QWidget()
    ui = Ui_ModuleMeasurementsBig()
    ui.setupUi(ModuleMeasurementsBig)
    ModuleMeasurementsBig.show()
    sys.exit(app.exec_())
