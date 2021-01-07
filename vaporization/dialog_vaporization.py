# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\khony\AppData\Local\Programs\Python\OOP_diploma\project\vaporization\dialog_vaporization.ui'
#
# Created: Thu Jan 07 17:45:57 2021
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 549)
        self.current = QtGui.QLineEdit(Dialog)
        self.current.setGeometry(QtCore.QRect(10, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.current.setFont(font)
        self.current.setAlignment(QtCore.Qt.AlignCenter)
        self.current.setObjectName("current")
        self.current_dial = QtGui.QDial(Dialog)
        self.current_dial.setGeometry(QtCore.QRect(10, 40, 50, 64))
        self.current_dial.setMaximum(100)
        self.current_dial.setSingleStep(1)
        self.current_dial.setPageStep(1)
        self.current_dial.setProperty("value", 0)
        self.current_dial.setTracking(True)
        self.current_dial.setWrapping(False)
        self.current_dial.setNotchesVisible(True)
        self.current_dial.setObjectName("current_dial")
        self.current_label = QtGui.QLabel(Dialog)
        self.current_label.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.current_label.setFont(font)
        self.current_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_label.setObjectName("current_label")
        self.damper = QtGui.QPushButton(Dialog)
        self.damper.setGeometry(QtCore.QRect(280, 20, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.damper.setFont(font)
        self.damper.setObjectName("damper")
        self.voltage = QtGui.QLineEdit(Dialog)
        self.voltage.setGeometry(QtCore.QRect(70, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.voltage.setFont(font)
        self.voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.voltage.setObjectName("voltage")
        self.voltage_dial = QtGui.QDial(Dialog)
        self.voltage_dial.setGeometry(QtCore.QRect(70, 40, 50, 64))
        self.voltage_dial.setMaximum(20)
        self.voltage_dial.setSingleStep(1)
        self.voltage_dial.setPageStep(1)
        self.voltage_dial.setProperty("value", 0)
        self.voltage_dial.setTracking(True)
        self.voltage_dial.setWrapping(False)
        self.voltage_dial.setNotchesVisible(True)
        self.voltage_dial.setObjectName("voltage_dial")
        self.voltage_label = QtGui.QLabel(Dialog)
        self.voltage_label.setGeometry(QtCore.QRect(70, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.voltage_label.setFont(font)
        self.voltage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.voltage_label.setObjectName("voltage_label")
        self.temperature_spinBox = QtGui.QSpinBox(Dialog)
        self.temperature_spinBox.setGeometry(QtCore.QRect(60, 160, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.temperature_spinBox.setFont(font)
        self.temperature_spinBox.setMinimum(293)
        self.temperature_spinBox.setMaximum(673)
        self.temperature_spinBox.setSingleStep(1)
        self.temperature_spinBox.setObjectName("temperature_spinBox")
        self.tempeature_label = QtGui.QLabel(Dialog)
        self.tempeature_label.setGeometry(QtCore.QRect(10, 150, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.tempeature_label.setFont(font)
        self.tempeature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tempeature_label.setObjectName("tempeature_label")
        self.temperature = QtGui.QLineEdit(Dialog)
        self.temperature.setGeometry(QtCore.QRect(10, 250, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.temperature.setFont(font)
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName("temperature")
        self.current_tempeature_label = QtGui.QLabel(Dialog)
        self.current_tempeature_label.setGeometry(QtCore.QRect(10, 200, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.current_tempeature_label.setFont(font)
        self.current_tempeature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_tempeature_label.setObjectName("current_tempeature_label")
        self.heat = QtGui.QPushButton(Dialog)
        self.heat.setGeometry(QtCore.QRect(150, 160, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.heat.setFont(font)
        self.heat.setObjectName("heat")
        self.damper_state = QtGui.QLabel(Dialog)
        self.damper_state.setGeometry(QtCore.QRect(280, 90, 111, 16))
        self.damper_state.setStyleSheet("background-color: red;")
        self.damper_state.setText("")
        self.damper_state.setObjectName("damper_state")
        self.d0_label = QtGui.QLabel(Dialog)
        self.d0_label.setGeometry(QtCore.QRect(280, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.d0_label.setFont(font)
        self.d0_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d0_label.setObjectName("d0_label")
        self.d0 = QtGui.QLineEdit(Dialog)
        self.d0.setGeometry(QtCore.QRect(350, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.d0.setFont(font)
        self.d0.setAlignment(QtCore.Qt.AlignCenter)
        self.d0.setObjectName("d0")
        self.dr_label = QtGui.QLabel(Dialog)
        self.dr_label.setGeometry(QtCore.QRect(280, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.dr_label.setFont(font)
        self.dr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dr_label.setObjectName("dr_label")
        self.dr = QtGui.QLineEdit(Dialog)
        self.dr.setGeometry(QtCore.QRect(350, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.dr.setFont(font)
        self.dr.setAlignment(QtCore.Qt.AlignCenter)
        self.dr.setObjectName("dr")
        self.k_label = QtGui.QLabel(Dialog)
        self.k_label.setGeometry(QtCore.QRect(280, 200, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.k_label.setFont(font)
        self.k_label.setAlignment(QtCore.Qt.AlignCenter)
        self.k_label.setObjectName("k_label")
        self.K = QtGui.QLineEdit(Dialog)
        self.K.setGeometry(QtCore.QRect(350, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.K.setFont(font)
        self.K.setAlignment(QtCore.Qt.AlignCenter)
        self.K.setObjectName("K")
        self.x100 = QtGui.QLabel(Dialog)
        self.x100.setGeometry(QtCore.QRect(300, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.x100.setFont(font)
        self.x100.setAlignment(QtCore.Qt.AlignCenter)
        self.x100.setObjectName("x100")
        self.time_rewind = QtGui.QLabel(Dialog)
        self.time_rewind.setGeometry(QtCore.QRect(310, 340, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.time_rewind.setFont(font)
        self.time_rewind.setAlignment(QtCore.Qt.AlignCenter)
        self.time_rewind.setObjectName("time_rewind")
        self.timeSlider = QtGui.QSlider(Dialog)
        self.timeSlider.setGeometry(QtCore.QRect(310, 400, 241, 31))
        self.timeSlider.setCursor(QtCore.Qt.OpenHandCursor)
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
        self.timeSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.timeSlider.setTickInterval(50)
        self.timeSlider.setObjectName("timeSlider")
        self.x1 = QtGui.QLabel(Dialog)
        self.x1.setGeometry(QtCore.QRect(410, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.x1.setFont(font)
        self.x1.setAlignment(QtCore.Qt.AlignCenter)
        self.x1.setObjectName("x1")
        self.x0_5 = QtGui.QLabel(Dialog)
        self.x0_5.setGeometry(QtCore.QRect(520, 440, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.x0_5.setFont(font)
        self.x0_5.setAlignment(QtCore.Qt.AlignCenter)
        self.x0_5.setObjectName("x0_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.current.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.current_label.setText(QtGui.QApplication.translate("Dialog", "I, A", None, QtGui.QApplication.UnicodeUTF8))
        self.damper.setText(QtGui.QApplication.translate("Dialog", "Damper", None, QtGui.QApplication.UnicodeUTF8))
        self.voltage.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.voltage_label.setText(QtGui.QApplication.translate("Dialog", "U, V", None, QtGui.QApplication.UnicodeUTF8))
        self.tempeature_label.setText(QtGui.QApplication.translate("Dialog", "T, K", None, QtGui.QApplication.UnicodeUTF8))
        self.temperature.setText(QtGui.QApplication.translate("Dialog", "293", None, QtGui.QApplication.UnicodeUTF8))
        self.current_tempeature_label.setText(QtGui.QApplication.translate("Dialog", "Current temperature, K", None, QtGui.QApplication.UnicodeUTF8))
        self.heat.setText(QtGui.QApplication.translate("Dialog", "Heat", None, QtGui.QApplication.UnicodeUTF8))
        self.d0_label.setText(QtGui.QApplication.translate("Dialog", "d0, nm", None, QtGui.QApplication.UnicodeUTF8))
        self.d0.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.dr_label.setText(QtGui.QApplication.translate("Dialog", "dr, nm", None, QtGui.QApplication.UnicodeUTF8))
        self.dr.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.k_label.setText(QtGui.QApplication.translate("Dialog", "K", None, QtGui.QApplication.UnicodeUTF8))
        self.K.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.x100.setText(QtGui.QApplication.translate("Dialog", "x100", None, QtGui.QApplication.UnicodeUTF8))
        self.time_rewind.setText(QtGui.QApplication.translate("Dialog", "time", None, QtGui.QApplication.UnicodeUTF8))
        self.x1.setText(QtGui.QApplication.translate("Dialog", "x1", None, QtGui.QApplication.UnicodeUTF8))
        self.x0_5.setText(QtGui.QApplication.translate("Dialog", "x0.5", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
