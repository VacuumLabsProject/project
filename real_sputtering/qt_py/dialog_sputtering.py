# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_sputtering.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(602, 463)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../real_sputtering/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.current_label = QtWidgets.QLabel(Dialog)
        self.current_label.setGeometry(QtCore.QRect(40, 100, 51, 31))
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
        self.damper.setGeometry(QtCore.QRect(370, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.damper.setFont(font)
        self.damper.setObjectName("damper")
        self.damper_state = QtWidgets.QLabel(Dialog)
        self.damper_state.setGeometry(QtCore.QRect(370, 80, 111, 16))
        self.damper_state.setStyleSheet("background-color: red;")
        self.damper_state.setText("")
        self.damper_state.setObjectName("damper_state")
        self.d0_label = QtWidgets.QLabel(Dialog)
        self.d0_label.setGeometry(QtCore.QRect(370, 150, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.d0_label.setFont(font)
        self.d0_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d0_label.setObjectName("d0_label")
        self.dr_label = QtWidgets.QLabel(Dialog)
        self.dr_label.setGeometry(QtCore.QRect(370, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dr_label.setFont(font)
        self.dr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dr_label.setObjectName("dr_label")
        self.k_label = QtWidgets.QLabel(Dialog)
        self.k_label.setGeometry(QtCore.QRect(370, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.k_label.setFont(font)
        self.k_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k_label.setObjectName("k_label")
        self.x100 = QtWidgets.QLabel(Dialog)
        self.x100.setGeometry(QtCore.QRect(20, 410, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x100.setFont(font)
        self.x100.setAlignment(QtCore.Qt.AlignCenter)
        self.x100.setObjectName("x100")
        self.time_rewind = QtWidgets.QLabel(Dialog)
        self.time_rewind.setGeometry(QtCore.QRect(30, 310, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_rewind.setFont(font)
        self.time_rewind.setAlignment(QtCore.Qt.AlignCenter)
        self.time_rewind.setObjectName("time_rewind")
        self.timeSlider = QtWidgets.QSlider(Dialog)
        self.timeSlider.setGeometry(QtCore.QRect(30, 370, 241, 31))
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
        self.x1.setGeometry(QtCore.QRect(130, 410, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x1.setFont(font)
        self.x1.setAlignment(QtCore.Qt.AlignCenter)
        self.x1.setObjectName("x1")
        self.x0_5 = QtWidgets.QLabel(Dialog)
        self.x0_5.setGeometry(QtCore.QRect(240, 410, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x0_5.setFont(font)
        self.x0_5.setAlignment(QtCore.Qt.AlignCenter)
        self.x0_5.setObjectName("x0_5")
        self.time_label = QtWidgets.QLabel(Dialog)
        self.time_label.setGeometry(QtCore.QRect(370, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(40, 190, 211, 111))
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
        self.target_diameter_label = QtWidgets.QLabel(Dialog)
        self.target_diameter_label.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.target_diameter_label.setFont(font)
        self.target_diameter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.target_diameter_label.setObjectName("target_diameter_label")
        self.sputtering_coefficient_label = QtWidgets.QLabel(Dialog)
        self.sputtering_coefficient_label.setGeometry(QtCore.QRect(170, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sputtering_coefficient_label.setFont(font)
        self.sputtering_coefficient_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sputtering_coefficient_label.setObjectName("sputtering_coefficient_label")
        self.voltage = QtWidgets.QPushButton(Dialog)
        self.voltage.setEnabled(True)
        self.voltage.setGeometry(QtCore.QRect(200, 110, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.voltage.setFont(font)
        self.voltage.setStyleSheet("background-color: red;")
        self.voltage.setObjectName("voltage")
        self.K0 = QtWidgets.QLineEdit(Dialog)
        self.K0.setGeometry(QtCore.QRect(440, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.K0.setFont(font)
        self.K0.setAlignment(QtCore.Qt.AlignCenter)
        self.K0.setObjectName("K0")
        self.time_value = QtWidgets.QLineEdit(Dialog)
        self.time_value.setGeometry(QtCore.QRect(440, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.time_value.setFont(font)
        self.time_value.setAlignment(QtCore.Qt.AlignCenter)
        self.time_value.setObjectName("time_value")
        self.dr = QtWidgets.QLineEdit(Dialog)
        self.dr.setGeometry(QtCore.QRect(440, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dr.setFont(font)
        self.dr.setAlignment(QtCore.Qt.AlignCenter)
        self.dr.setObjectName("dr")
        self.d0 = QtWidgets.QLineEdit(Dialog)
        self.d0.setGeometry(QtCore.QRect(440, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.d0.setFont(font)
        self.d0.setAlignment(QtCore.Qt.AlignCenter)
        self.d0.setObjectName("d0")
        self.sputtering_coefficient = QtWidgets.QLabel(Dialog)
        self.sputtering_coefficient.setGeometry(QtCore.QRect(220, 50, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sputtering_coefficient.setFont(font)
        self.sputtering_coefficient.setStyleSheet("background-color: white;")
        self.sputtering_coefficient.setFrameShape(QtWidgets.QFrame.Box)
        self.sputtering_coefficient.setAlignment(QtCore.Qt.AlignCenter)
        self.sputtering_coefficient.setObjectName("sputtering_coefficient")
        self.current = QtWidgets.QLabel(Dialog)
        self.current.setGeometry(QtCore.QRect(40, 130, 51, 41))
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
        self.target_diameter = QtWidgets.QLabel(Dialog)
        self.target_diameter.setGeometry(QtCore.QRect(40, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.target_diameter.setFont(font)
        self.target_diameter.setStyleSheet("background-color: white;")
        self.target_diameter.setFrameShape(QtWidgets.QFrame.Box)
        self.target_diameter.setAlignment(QtCore.Qt.AlignCenter)
        self.target_diameter.setObjectName("target_diameter")
        self.current_dial = QtWidgets.QDial(Dialog)
        self.current_dial.setGeometry(QtCore.QRect(100, 110, 50, 64))
        self.current_dial.setMinimum(3)
        self.current_dial.setMaximum(15)
        self.current_dial.setSingleStep(1)
        self.current_dial.setPageStep(1)
        self.current_dial.setProperty("value", 4)
        self.current_dial.setTracking(True)
        self.current_dial.setWrapping(False)
        self.current_dial.setObjectName("current_dial")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sputtering"))
        self.current_label.setText(_translate("Dialog", "I, A"))
        self.damper.setText(_translate("Dialog", "Damper"))
        self.d0_label.setText(_translate("Dialog", "d0, nm"))
        self.dr_label.setText(_translate("Dialog", "dr, nm"))
        self.k_label.setText(_translate("Dialog", "K"))
        self.x100.setText(_translate("Dialog", "x100"))
        self.time_rewind.setText(_translate("Dialog", "time"))
        self.x1.setText(_translate("Dialog", "x1"))
        self.x0_5.setText(_translate("Dialog", "x0.5"))
        self.time_label.setText(_translate("Dialog", "t, s"))
        self.target_diameter_label.setText(_translate("Dialog", "Target diameter, mm"))
        self.sputtering_coefficient_label.setText(_translate("Dialog", "Sputtering coefficient"))
        self.voltage.setText(_translate("Dialog", "Voltage"))
        self.K0.setText(_translate("Dialog", "0"))
        self.time_value.setText(_translate("Dialog", "0"))
        self.dr.setText(_translate("Dialog", "0"))
        self.d0.setText(_translate("Dialog", "0"))
        self.sputtering_coefficient.setText(_translate("Dialog", "0"))
        self.current.setText(_translate("Dialog", "0.4"))
        self.target_diameter.setText(_translate("Dialog", "100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
