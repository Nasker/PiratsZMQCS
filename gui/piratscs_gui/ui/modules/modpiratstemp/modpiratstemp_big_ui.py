# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\modpiratstemp_big.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModulePiratsTempBig(object):
    def setupUi(self, ModulePiratsTempBig):
        ModulePiratsTempBig.setObjectName("ModulePiratsTempBig")
        ModulePiratsTempBig.resize(1064, 730)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(ModulePiratsTempBig)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(ModulePiratsTempBig)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(ModulePiratsTempBig)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.ledit_channel_set = QtWidgets.QLineEdit(ModulePiratsTempBig)
        self.ledit_channel_set.setText("")
        self.ledit_channel_set.setObjectName("ledit_channel_set")
        self.horizontalLayout_11.addWidget(self.ledit_channel_set)
        self.pb_channel_set = QtWidgets.QPushButton(ModulePiratsTempBig)
        self.pb_channel_set.setObjectName("pb_channel_set")
        self.horizontalLayout_11.addWidget(self.pb_channel_set)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.line_6 = QtWidgets.QFrame(ModulePiratsTempBig)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_10.addWidget(self.line_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(ModulePiratsTempBig)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.lbl_set_channel_recvd = QtWidgets.QLabel(ModulePiratsTempBig)
        self.lbl_set_channel_recvd.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_set_channel_recvd.setFont(font)
        self.lbl_set_channel_recvd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd.setObjectName("lbl_set_channel_recvd")
        self.horizontalLayout_12.addWidget(self.lbl_set_channel_recvd)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.lbl_set_channel_recvd_on = QtWidgets.QLabel(ModulePiratsTempBig)
        self.lbl_set_channel_recvd_on.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd_on.setObjectName("lbl_set_channel_recvd_on")
        self.verticalLayout_6.addWidget(self.lbl_set_channel_recvd_on)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(ModulePiratsTempBig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(ModulePiratsTempBig)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(ModulePiratsTempBig)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.lbl_last_temp = QtWidgets.QLabel(ModulePiratsTempBig)
        self.lbl_last_temp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_last_temp.setFont(font)
        self.lbl_last_temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_last_temp.setObjectName("lbl_last_temp")
        self.horizontalLayout_7.addWidget(self.lbl_last_temp)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(ModulePiratsTempBig)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_8.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_acq_btn = QtWidgets.QPushButton(ModulePiratsTempBig)
        self.start_acq_btn.setObjectName("start_acq_btn")
        self.verticalLayout_2.addWidget(self.start_acq_btn)
        self.stop_acq_btn = QtWidgets.QPushButton(ModulePiratsTempBig)
        self.stop_acq_btn.setObjectName("stop_acq_btn")
        self.verticalLayout_2.addWidget(self.stop_acq_btn)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.line_4 = QtWidgets.QFrame(ModulePiratsTempBig)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_11.addWidget(self.line_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(ModulePiratsTempBig)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.chart = PlotWidget(ModulePiratsTempBig)
        self.chart.setObjectName("chart")
        self.horizontalLayout_6.addWidget(self.chart)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.retranslateUi(ModulePiratsTempBig)
        QtCore.QMetaObject.connectSlotsByName(ModulePiratsTempBig)

    def retranslateUi(self, ModulePiratsTempBig):
        _translate = QtCore.QCoreApplication.translate
        ModulePiratsTempBig.setWindowTitle(_translate("ModulePiratsTempBig", "Pirats Temperature Module"))
        self.label.setText(_translate("ModulePiratsTempBig", "Pirats Board Temperature Sense Monitor and Control"))
        self.label_9.setText(_translate("ModulePiratsTempBig", "Select Channel(s)"))
        self.pb_channel_set.setText(_translate("ModulePiratsTempBig", "Send"))
        self.label_10.setText(_translate("ModulePiratsTempBig", "Received:"))
        self.lbl_set_channel_recvd.setText(_translate("ModulePiratsTempBig", "-"))
        self.lbl_set_channel_recvd_on.setText(_translate("ModulePiratsTempBig", "on -"))
        self.label_7.setText(_translate("ModulePiratsTempBig", "Temperature Asyncs"))
        self.label_3.setText(_translate("ModulePiratsTempBig", "Last Temperature(s) Received"))
        self.lbl_last_temp.setText(_translate("ModulePiratsTempBig", "0.0"))
        self.start_acq_btn.setText(_translate("ModulePiratsTempBig", "Start ACQ"))
        self.stop_acq_btn.setText(_translate("ModulePiratsTempBig", "Stop ACQ"))
        self.label_8.setText(_translate("ModulePiratsTempBig", "Temperatures Chart"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModulePiratsTempBig = QtWidgets.QWidget()
    ui = Ui_ModulePiratsTempBig()
    ui.setupUi(ModulePiratsTempBig)
    ModulePiratsTempBig.show()
    sys.exit(app.exec_())
