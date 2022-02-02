# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\modpiratsinout_big.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModulePiratsInOutBig(object):
    def setupUi(self, ModulePiratsInOutBig):
        ModulePiratsInOutBig.setObjectName("ModulePiratsInOutBig")
        ModulePiratsInOutBig.resize(1064, 718)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(ModulePiratsInOutBig)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(ModulePiratsInOutBig)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(ModulePiratsInOutBig)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lbl_set_channel_recvd = QtWidgets.QLabel(ModulePiratsInOutBig)
        self.lbl_set_channel_recvd.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_set_channel_recvd.setFont(font)
        self.lbl_set_channel_recvd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd.setObjectName("lbl_set_channel_recvd")
        self.horizontalLayout_3.addWidget(self.lbl_set_channel_recvd)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lbl_set_channel_recvd_on = QtWidgets.QLabel(ModulePiratsInOutBig)
        self.lbl_set_channel_recvd_on.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_channel_recvd_on.setObjectName("lbl_set_channel_recvd_on")
        self.verticalLayout_4.addWidget(self.lbl_set_channel_recvd_on)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.line_2 = QtWidgets.QFrame(ModulePiratsInOutBig)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_11.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(ModulePiratsInOutBig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.outputs_gridLayout = QtWidgets.QGridLayout()
        self.outputs_gridLayout.setObjectName("outputs_gridLayout")
        self.horizontalLayout.addLayout(self.outputs_gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(ModulePiratsInOutBig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.start_acq_btn = QtWidgets.QPushButton(ModulePiratsInOutBig)
        self.start_acq_btn.setObjectName("start_acq_btn")
        self.horizontalLayout_4.addWidget(self.start_acq_btn)
        self.stop_acq_btn = QtWidgets.QPushButton(ModulePiratsInOutBig)
        self.stop_acq_btn.setObjectName("stop_acq_btn")
        self.horizontalLayout_4.addWidget(self.stop_acq_btn)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(ModulePiratsInOutBig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.inputs_gridLayout = QtWidgets.QGridLayout()
        self.inputs_gridLayout.setObjectName("inputs_gridLayout")
        self.horizontalLayout_2.addLayout(self.inputs_gridLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_11.addLayout(self.verticalLayout_2)

        self.retranslateUi(ModulePiratsInOutBig)
        QtCore.QMetaObject.connectSlotsByName(ModulePiratsInOutBig)

    def retranslateUi(self, ModulePiratsInOutBig):
        _translate = QtCore.QCoreApplication.translate
        ModulePiratsInOutBig.setWindowTitle(_translate("ModulePiratsInOutBig", "Pirats Ins And Outs Module"))
        self.label.setText(_translate("ModulePiratsInOutBig", "Pirats Board Inputs Sense and Output Control"))
        self.label_6.setText(_translate("ModulePiratsInOutBig", "Received:"))
        self.lbl_set_channel_recvd.setText(_translate("ModulePiratsInOutBig", "-"))
        self.lbl_set_channel_recvd_on.setText(_translate("ModulePiratsInOutBig", "on -"))
        self.label_2.setText(_translate("ModulePiratsInOutBig", "Outputs Control"))
        self.start_acq_btn.setText(_translate("ModulePiratsInOutBig", "Start ACQ"))
        self.stop_acq_btn.setText(_translate("ModulePiratsInOutBig", "Stop ACQ"))
        self.label_3.setText(_translate("ModulePiratsInOutBig", "Inputs Reading"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModulePiratsInOutBig = QtWidgets.QWidget()
    ui = Ui_ModulePiratsInOutBig()
    ui.setupUi(ModulePiratsInOutBig)
    ModulePiratsInOutBig.show()
    sys.exit(app.exec_())
