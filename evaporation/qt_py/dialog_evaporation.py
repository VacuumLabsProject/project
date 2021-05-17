# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_evaporation.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../evaporation/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.current_dial = QtWidgets.QDial(Dialog)
        self.current_dial.setGeometry(QtCore.QRect(10, 40, 50, 64))
        self.current_dial.setMaximum(100)
        self.current_dial.setSingleStep(1)
        self.current_dial.setPageStep(1)
        self.current_dial.setProperty("value", 0)
        self.current_dial.setTracking(True)
        self.current_dial.setWrapping(False)
        self.current_dial.setNotchesVisible(True)
        self.current_dial.setObjectName("current_dial")
        self.current_label = QtWidgets.QLabel(Dialog)
        self.current_label.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.current_label.setFont(font)
        self.current_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_label.setObjectName("current_label")
        self.damper = QtWidgets.QPushButton(Dialog)
        self.damper.setEnabled(False)
        self.damper.setGeometry(QtCore.QRect(280, 20, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.damper.setFont(font)
        self.damper.setObjectName("damper")
        """
        self.voltage_dial = QtWidgets.QDial(Dialog)
        self.voltage_dial.setGeometry(QtCore.QRect(70, 40, 50, 64))
        self.voltage_dial.setMaximum(20)
        self.voltage_dial.setSingleStep(1)
        self.voltage_dial.setPageStep(1)
        self.voltage_dial.setProperty("value", 0)
        self.voltage_dial.setTracking(True)
        self.voltage_dial.setWrapping(False)
        self.voltage_dial.setNotchesVisible(True)
        self.voltage_dial.setObjectName("voltage_dial")
        self.voltage_label = QtWidgets.QLabel(Dialog)
        self.voltage_label.setGeometry(QtCore.QRect(70, 10, 51, 31))
        """
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        #self.voltage_label.setFont(font)
        #self.voltage_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.voltage_label.setObjectName("voltage_label")
        self.current_tempeature_label = QtWidgets.QLabel(Dialog)
        self.current_tempeature_label.setGeometry(QtCore.QRect(10, 140, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.current_tempeature_label.setFont(font)
        self.current_tempeature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_tempeature_label.setObjectName("current_tempeature_label")
        self.heat = QtWidgets.QPushButton(Dialog)
        self.heat.setGeometry(QtCore.QRect(100, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.heat.setFont(font)
        self.heat.setObjectName("heat")
        self.damper_state = QtWidgets.QLabel(Dialog)
        self.damper_state.setGeometry(QtCore.QRect(280, 90, 111, 16))
        self.damper_state.setStyleSheet("background-color: red;")
        self.damper_state.setText("")
        self.damper_state.setObjectName("damper_state")
        self.d0_label = QtWidgets.QLabel(Dialog)
        self.d0_label.setGeometry(QtCore.QRect(280, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.d0_label.setFont(font)
        self.d0_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d0_label.setObjectName("d0_label")
        self.dr_label = QtWidgets.QLabel(Dialog)
        self.dr_label.setGeometry(QtCore.QRect(280, 200, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dr_label.setFont(font)
        self.dr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dr_label.setObjectName("dr_label")
        self.k_label = QtWidgets.QLabel(Dialog)
        self.k_label.setGeometry(QtCore.QRect(280, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.k_label.setFont(font)
        self.k_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k_label.setObjectName("k_label")
        self.x100 = QtWidgets.QLabel(Dialog)
        self.x100.setGeometry(QtCore.QRect(300, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x100.setFont(font)
        self.x100.setAlignment(QtCore.Qt.AlignCenter)
        self.x100.setObjectName("x100")
        self.time_rewind = QtWidgets.QLabel(Dialog)
        self.time_rewind.setGeometry(QtCore.QRect(310, 340, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_rewind.setFont(font)
        self.time_rewind.setAlignment(QtCore.Qt.AlignCenter)
        self.time_rewind.setObjectName("time_rewind")
        self.timeSlider = QtWidgets.QSlider(Dialog)
        self.timeSlider.setGeometry(QtCore.QRect(310, 400, 241, 31))
        self.timeSlider.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.timeSlider.setMouseTracking(False)
        self.timeSlider.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeSlider.setMinimum(1)
        self.timeSlider.setMaximum(200)
        self.timeSlider.setSingleStep(1)
        self.timeSlider.setProperty("value", 100)
        self.timeSlider.setSliderPosition(100)
        self.timeSlider.setTracking(True)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setInvertedAppearance(False)
        self.timeSlider.setInvertedControls(False)
        self.timeSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.timeSlider.setTickInterval(50)
        self.timeSlider.setObjectName("timeSlider")
        self.x1 = QtWidgets.QLabel(Dialog)
        self.x1.setGeometry(QtCore.QRect(410, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x1.setFont(font)
        self.x1.setAlignment(QtCore.Qt.AlignCenter)
        self.x1.setObjectName("x1")
        self.x0_5 = QtWidgets.QLabel(Dialog)
        self.x0_5.setGeometry(QtCore.QRect(520, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x0_5.setFont(font)
        self.x0_5.setAlignment(QtCore.Qt.AlignCenter)
        self.x0_5.setObjectName("x0_5")
        self.time_label = QtWidgets.QLabel(Dialog)
        self.time_label.setGeometry(QtCore.QRect(280, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.substrate_tempeature_label = QtWidgets.QLabel(Dialog)
        self.substrate_tempeature_label.setGeometry(QtCore.QRect(10, 240, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.substrate_tempeature_label.setFont(font)
        self.substrate_tempeature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.substrate_tempeature_label.setObjectName("substrate_tempeature_label")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(10, 350, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setStyleSheet("background-color: white;")
        self.status.setFrameShape(QtWidgets.QFrame.Box)
        self.status.setText("")
        self.status.setTextFormat(QtCore.Qt.AutoText)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setWordWrap(True)
        self.status.setObjectName("status")
        self.current = QtWidgets.QLabel(Dialog)
        self.current.setGeometry(QtCore.QRect(10, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.current.setFont(font)
        self.current.setStyleSheet("background-color: white;")
        self.current.setFrameShape(QtWidgets.QFrame.Box)
        self.current.setAlignment(QtCore.Qt.AlignCenter)
        self.current.setObjectName("current")
        #self.voltage = QtWidgets.QLabel(Dialog)
        #self.voltage.setGeometry(QtCore.QRect(70, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        """
        self.voltage.setFont(font)
        self.voltage.setStyleSheet("background-color: white;")
        self.voltage.setFrameShape(QtWidgets.QFrame.Box)
        self.voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.voltage.setObjectName("voltage")
        """
        self.temperature = QtWidgets.QLabel(Dialog)
        self.temperature.setGeometry(QtCore.QRect(10, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("background-color: white;")
        self.temperature.setFrameShape(QtWidgets.QFrame.Box)
        self.temperature.setText("")
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName("temperature")
        self.substrate_temperature = QtWidgets.QLabel(Dialog)
        self.substrate_temperature.setGeometry(QtCore.QRect(10, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.substrate_temperature.setFont(font)
        self.substrate_temperature.setStyleSheet("background-color: white;")
        self.substrate_temperature.setFrameShape(QtWidgets.QFrame.Box)
        self.substrate_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.substrate_temperature.setObjectName("substrate_temperature")
        self.t = QtWidgets.QLabel(Dialog)
        self.t.setGeometry(QtCore.QRect(350, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t.setFont(font)
        self.t.setStyleSheet("background-color: white;")
        self.t.setFrameShape(QtWidgets.QFrame.Box)
        self.t.setAlignment(QtCore.Qt.AlignCenter)
        self.t.setObjectName("t")
        self.d0 = QtWidgets.QLabel(Dialog)
        self.d0.setGeometry(QtCore.QRect(350, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.d0.setFont(font)
        self.d0.setStyleSheet("background-color: white;")
        self.d0.setFrameShape(QtWidgets.QFrame.Box)
        self.d0.setAlignment(QtCore.Qt.AlignCenter)
        self.d0.setObjectName("d0")
        self.dr = QtWidgets.QLabel(Dialog)
        self.dr.setGeometry(QtCore.QRect(350, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dr.setFont(font)
        self.dr.setStyleSheet("background-color: white;")
        self.dr.setFrameShape(QtWidgets.QFrame.Box)
        self.dr.setAlignment(QtCore.Qt.AlignCenter)
        self.dr.setObjectName("dr")
        self.K = QtWidgets.QLabel(Dialog)
        self.K.setGeometry(QtCore.QRect(350, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.K.setFont(font)
        self.K.setStyleSheet("background-color: white;")
        self.K.setFrameShape(QtWidgets.QFrame.Box)
        self.K.setAlignment(QtCore.Qt.AlignCenter)
        self.K.setObjectName("K")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Evaporation"))
        self.current_label.setText(_translate("Dialog", "I, A"))
        self.damper.setText(_translate("Dialog", "Damper"))
        #self.voltage_label.setText(_translate("Dialog", "U, V"))
        self.current_tempeature_label.setText(_translate("Dialog", "Current temperature, K"))
        self.heat.setText(_translate("Dialog", "Heat"))
        self.d0_label.setText(_translate("Dialog", "d0, nm"))
        self.dr_label.setText(_translate("Dialog", "dr, nm"))
        self.k_label.setText(_translate("Dialog", "K"))
        self.x100.setText(_translate("Dialog", "x100"))
        self.time_rewind.setText(_translate("Dialog", "time"))
        self.x1.setText(_translate("Dialog", "x1"))
        self.x0_5.setText(_translate("Dialog", "x0.5"))
        self.time_label.setText(_translate("Dialog", "t, s"))
        self.substrate_tempeature_label.setText(_translate("Dialog", "Substrate temperature, K"))
        self.current.setText(_translate("Dialog", "0"))
        #self.voltage.setText(_translate("Dialog", "0"))
        self.substrate_temperature.setText(_translate("Dialog", "600"))
        self.t.setText(_translate("Dialog", "0"))
        self.d0.setText(_translate("Dialog", "0"))
        self.dr.setText(_translate("Dialog", "0"))
        self.K.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
