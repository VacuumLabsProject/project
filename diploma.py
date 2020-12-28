# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\khony\AppData\Local\Programs\Python\OOP_diploma\project\diploma.ui'
#
# Created: Mon Dec 28 23:28:33 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1165, 696)
        Form.setStyleSheet(".QWidget {\n"
                           "    background-color: rgb(170, 255, 255);\n"
                           "}\n"
                           "\n"
                           ".QLabel, .QDial {\n"
                           "    background-color: silver;\n"
                           "}")
        self.vacuum_chamber = QtGui.QLabel(Form)
        self.vacuum_chamber.setGeometry(QtCore.QRect(40, 40, 681, 161))
        self.vacuum_chamber.setStyleSheet("")
        self.vacuum_chamber.setText("")
        self.vacuum_chamber.setObjectName("vacuum_chamber")
        self.tube_v1_chamber = QtGui.QLabel(Form)
        self.tube_v1_chamber.setGeometry(QtCore.QRect(60, 200, 71, 111))
        self.tube_v1_chamber.setText("")
        self.tube_v1_chamber.setObjectName("tube_v1_chamber")
        self.valve1 = QtGui.QPushButton(Form)
        self.valve1.setEnabled(False)
        self.valve1.setGeometry(QtCore.QRect(60, 310, 71, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.valve1.setFont(font)
        self.valve1.setObjectName("valve1")
        self.tube_tm_v1 = QtGui.QLabel(Form)
        self.tube_tm_v1.setGeometry(QtCore.QRect(60, 390, 71, 111))
        self.tube_tm_v1.setText("")
        self.tube_tm_v1.setObjectName("tube_tm_v1")
        self.tm_pump = QtGui.QPushButton(Form)
        self.tm_pump.setEnabled(False)
        self.tm_pump.setGeometry(QtCore.QRect(20, 500, 151, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.tm_pump.setFont(font)
        self.tm_pump.setObjectName("tm_pump")
        self.tube_v2_tm = QtGui.QLabel(Form)
        self.tube_v2_tm.setGeometry(QtCore.QRect(170, 540, 171, 81))
        self.tube_v2_tm.setText("")
        self.tube_v2_tm.setObjectName("tube_v2_tm")
        self.valve2 = QtGui.QPushButton(Form)
        self.valve2.setEnabled(False)
        self.valve2.setGeometry(QtCore.QRect(340, 540, 71, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.valve2.setFont(font)
        self.valve2.setObjectName("valve2")
        self.tube_fl_v2 = QtGui.QLabel(Form)
        self.tube_fl_v2.setGeometry(QtCore.QRect(410, 540, 181, 81))
        self.tube_fl_v2.setText("")
        self.tube_fl_v2.setObjectName("tube_fl_v2")
        self.fl_pump = QtGui.QPushButton(Form)
        self.fl_pump.setEnabled(False)
        self.fl_pump.setGeometry(QtCore.QRect(590, 500, 151, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.fl_pump.setFont(font)
        self.fl_pump.setObjectName("fl_pump")
        self.tube_fl_v3 = QtGui.QLabel(Form)
        self.tube_fl_v3.setGeometry(QtCore.QRect(630, 390, 71, 111))
        self.tube_fl_v3.setText("")
        self.tube_fl_v3.setObjectName("tube_fl_v3")
        self.valve3 = QtGui.QPushButton(Form)
        self.valve3.setEnabled(False)
        self.valve3.setGeometry(QtCore.QRect(630, 310, 71, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.valve3.setFont(font)
        self.valve3.setObjectName("valve3")
        self.tube_v3_chamber = QtGui.QLabel(Form)
        self.tube_v3_chamber.setGeometry(QtCore.QRect(630, 200, 71, 111))
        self.tube_v3_chamber.setText("")
        self.tube_v3_chamber.setObjectName("tube_v3_chamber")
        self.Enable = QtGui.QPushButton(Form)
        self.Enable.setGeometry(QtCore.QRect(900, 50, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Enable.setFont(font)
        self.Enable.setObjectName("Enable")
        self.tube_fl_v2_2 = QtGui.QLabel(Form)
        self.tube_fl_v2_2.setGeometry(QtCore.QRect(720, 40, 71, 21))
        self.tube_fl_v2_2.setText("")
        self.tube_fl_v2_2.setObjectName("tube_fl_v2_2")
        self.spinbox_l_fl = QtGui.QDoubleSpinBox(Form)
        self.spinbox_l_fl.setGeometry(QtCore.QRect(510, 440, 62, 22))
        self.spinbox_l_fl.setMinimum(0.01)
        self.spinbox_l_fl.setMaximum(30.0)
        self.spinbox_l_fl.setSingleStep(0.01)
        self.spinbox_l_fl.setProperty("value", 0.08)
        self.spinbox_l_fl.setObjectName("spinbox_l_fl")
        self.spinbox_d_fl = QtGui.QDoubleSpinBox(Form)
        self.spinbox_d_fl.setGeometry(QtCore.QRect(510, 470, 62, 22))
        self.spinbox_d_fl.setMinimum(0.01)
        self.spinbox_d_fl.setMaximum(10.0)
        self.spinbox_d_fl.setSingleStep(0.01)
        self.spinbox_d_fl.setProperty("value", 0.04)
        self.spinbox_d_fl.setObjectName("spinbox_d_fl")
        self.time_label1 = QtGui.QLineEdit(Form)
        self.time_label1.setGeometry(QtCore.QRect(950, 190, 71, 22))
        self.time_label1.setObjectName("time_label1")
        self.spinbox_l_tm = QtGui.QDoubleSpinBox(Form)
        self.spinbox_l_tm.setGeometry(QtCore.QRect(190, 440, 62, 22))
        self.spinbox_l_tm.setMinimum(0.01)
        self.spinbox_l_tm.setMaximum(30.0)
        self.spinbox_l_tm.setSingleStep(0.01)
        self.spinbox_l_tm.setProperty("value", 0.3)
        self.spinbox_l_tm.setObjectName("spinbox_l_tm")
        self.spinbox_d_tm = QtGui.QDoubleSpinBox(Form)
        self.spinbox_d_tm.setGeometry(QtCore.QRect(190, 470, 62, 22))
        self.spinbox_d_tm.setMinimum(0.01)
        self.spinbox_d_tm.setMaximum(10.0)
        self.spinbox_d_tm.setSingleStep(0.01)
        self.spinbox_d_tm.setProperty("value", 0.5)
        self.spinbox_d_tm.setObjectName("spinbox_d_tm")
        self.l_tm = QtGui.QLabel(Form)
        self.l_tm.setGeometry(QtCore.QRect(140, 440, 41, 16))
        self.l_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.l_tm.setObjectName("l_tm")
        self.d_tm = QtGui.QLabel(Form)
        self.d_tm.setGeometry(QtCore.QRect(140, 470, 41, 16))
        self.d_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.d_tm.setObjectName("d_tm")
        self.d_fl = QtGui.QLabel(Form)
        self.d_fl.setGeometry(QtCore.QRect(580, 470, 41, 16))
        self.d_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.d_fl.setObjectName("d_fl")
        self.l_fl = QtGui.QLabel(Form)
        self.l_fl.setGeometry(QtCore.QRect(580, 440, 41, 16))
        self.l_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.l_fl.setObjectName("l_fl")
        self.t1 = QtGui.QLabel(Form)
        self.t1.setGeometry(QtCore.QRect(900, 190, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.t1.setFont(font)
        self.t1.setAlignment(QtCore.Qt.AlignCenter)
        self.t1.setObjectName("t1")
        self.t2 = QtGui.QLabel(Form)
        self.t2.setGeometry(QtCore.QRect(900, 220, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.t2.setFont(font)
        self.t2.setAlignment(QtCore.Qt.AlignCenter)
        self.t2.setObjectName("t2")
        self.time_label2 = QtGui.QLineEdit(Form)
        self.time_label2.setGeometry(QtCore.QRect(950, 220, 71, 22))
        self.time_label2.setObjectName("time_label2")
        self.time_rewind = QtGui.QLabel(Form)
        self.time_rewind.setGeometry(QtCore.QRect(900, 330, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.time_rewind.setFont(font)
        self.time_rewind.setAlignment(QtCore.Qt.AlignCenter)
        self.time_rewind.setObjectName("time_rewind")
        self.p = QtGui.QLabel(Form)
        self.p.setGeometry(QtCore.QRect(900, 250, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.p.setFont(font)
        self.p.setAlignment(QtCore.Qt.AlignCenter)
        self.p.setObjectName("p")
        self.pressure_value = QtGui.QLineEdit(Form)
        self.pressure_value.setGeometry(QtCore.QRect(950, 250, 71, 22))
        self.pressure_value.setObjectName("pressure_value")
        self.timeSlider = QtGui.QSlider(Form)
        self.timeSlider.setGeometry(QtCore.QRect(900, 370, 241, 31))
        self.timeSlider.setCursor(QtCore.Qt.OpenHandCursor)
        self.timeSlider.setMouseTracking(False)
        self.timeSlider.setLocale(QtCore.QLocale(QtCore.QLocale.English,
                                                 QtCore.QLocale.UnitedStates))
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
        self.readiness = QtGui.QLineEdit(Form)
        self.readiness.setGeometry(QtCore.QRect(180, 500, 21, 22))
        self.readiness.setStyleSheet("background-color: red;")
        self.readiness.setText("")
        self.readiness.setFrame(True)
        self.readiness.setObjectName("readiness")
        self.spinbox_Qin2 = QtGui.QDoubleSpinBox(Form)
        self.spinbox_Qin2.setGeometry(QtCore.QRect(190, 410, 71, 22))
        self.spinbox_Qin2.setDecimals(4)
        self.spinbox_Qin2.setMinimum(0.0001)
        self.spinbox_Qin2.setMaximum(10.0)
        self.spinbox_Qin2.setSingleStep(0.0001)
        self.spinbox_Qin2.setProperty("value", 0.0001)
        self.spinbox_Qin2.setObjectName("spinbox_Qin2")
        self.spinbox_Qin1 = QtGui.QDoubleSpinBox(Form)
        self.spinbox_Qin1.setGeometry(QtCore.QRect(491, 410, 81, 22))
        self.spinbox_Qin1.setDecimals(4)
        self.spinbox_Qin1.setMinimum(0.0001)
        self.spinbox_Qin1.setMaximum(2000.0)
        self.spinbox_Qin1.setSingleStep(0.0001)
        self.spinbox_Qin1.setProperty("value", 0.5)
        self.spinbox_Qin1.setObjectName("spinbox_Qin1")
        self.spinbox_V = QtGui.QDoubleSpinBox(Form)
        self.spinbox_V.setGeometry(QtCore.QRect(770, 100, 62, 22))
        self.spinbox_V.setMinimum(0.01)
        self.spinbox_V.setMaximum(100.0)
        self.spinbox_V.setSingleStep(0.01)
        self.spinbox_V.setProperty("value", 0.04)
        self.spinbox_V.setObjectName("spinbox_V")
        self.Q_tm = QtGui.QLabel(Form)
        self.Q_tm.setGeometry(QtCore.QRect(140, 410, 41, 16))
        self.Q_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.Q_tm.setObjectName("Q_tm")
        self.Q_fl = QtGui.QLabel(Form)
        self.Q_fl.setGeometry(QtCore.QRect(580, 410, 41, 16))
        self.Q_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.Q_fl.setObjectName("Q_fl")
        self.V_chamber = QtGui.QLabel(Form)
        self.V_chamber.setGeometry(QtCore.QRect(730, 100, 31, 21))
        self.V_chamber.setAlignment(QtCore.Qt.AlignCenter)
        self.V_chamber.setObjectName("V_chamber")
        self.spinbox_S1 = QtGui.QDoubleSpinBox(Form)
        self.spinbox_S1.setGeometry(QtCore.QRect(510, 380, 62, 22))
        self.spinbox_S1.setDecimals(4)
        self.spinbox_S1.setMinimum(0.0001)
        self.spinbox_S1.setMaximum(10.0)
        self.spinbox_S1.setSingleStep(0.0001)
        self.spinbox_S1.setProperty("value", 0.005)
        self.spinbox_S1.setObjectName("spinbox_S1")
        self.S_tm = QtGui.QLabel(Form)
        self.S_tm.setGeometry(QtCore.QRect(140, 380, 41, 16))
        self.S_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.S_tm.setObjectName("S_tm")
        self.spinbox_S2 = QtGui.QDoubleSpinBox(Form)
        self.spinbox_S2.setGeometry(QtCore.QRect(190, 380, 61, 22))
        self.spinbox_S2.setDecimals(4)
        self.spinbox_S2.setMinimum(0.0001)
        self.spinbox_S2.setMaximum(10.0)
        self.spinbox_S2.setSingleStep(0.0001)
        self.spinbox_S2.setProperty("value", 0.09)
        self.spinbox_S2.setObjectName("spinbox_S2")
        self.S_fl = QtGui.QLabel(Form)
        self.S_fl.setGeometry(QtCore.QRect(580, 380, 41, 16))
        self.S_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.S_fl.setObjectName("S_fl")
        self.x1 = QtGui.QLabel(Form)
        self.x1.setGeometry(QtCore.QRect(1000, 410, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.x1.setFont(font)
        self.x1.setAlignment(QtCore.Qt.AlignCenter)
        self.x1.setObjectName("x1")
        self.x100 = QtGui.QLabel(Form)
        self.x100.setGeometry(QtCore.QRect(890, 410, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.x100.setFont(font)
        self.x100.setAlignment(QtCore.Qt.AlignCenter)
        self.x100.setObjectName("x100")
        self.x0_5 = QtGui.QLabel(Form)
        self.x0_5.setGeometry(QtCore.QRect(1110, 410, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.x0_5.setFont(font)
        self.x0_5.setAlignment(QtCore.Qt.AlignCenter)
        self.x0_5.setObjectName("x0_5")
        self.overflow = QtGui.QPushButton(Form)
        self.overflow.setGeometry(QtCore.QRect(790, 30, 51, 41))
        self.overflow.setObjectName("overflow")
        self.overflow.setEnabled(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None,
                                                         QtGui.QApplication.UnicodeUTF8))
        self.valve1.setText(QtGui.QApplication.translate("Form", "V1", None,
                                                         QtGui.QApplication.UnicodeUTF8))
        self.tm_pump.setText(QtGui.QApplication.translate("Form", "TMP", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.valve2.setText(QtGui.QApplication.translate("Form", "V2", None,
                                                         QtGui.QApplication.UnicodeUTF8))
        self.fl_pump.setText(QtGui.QApplication.translate("Form", "FLP", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.valve3.setText(QtGui.QApplication.translate("Form", "V3", None,
                                                         QtGui.QApplication.UnicodeUTF8))
        self.Enable.setText(
            QtGui.QApplication.translate("Form", "Turn on power", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.l_tm.setText(QtGui.QApplication.translate("Form", "l", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.d_tm.setText(QtGui.QApplication.translate("Form", "d", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.d_fl.setText(QtGui.QApplication.translate("Form", "d", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.l_fl.setText(QtGui.QApplication.translate("Form", "l", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.t1.setText(QtGui.QApplication.translate("Form", "t1", None,
                                                     QtGui.QApplication.UnicodeUTF8))
        self.t2.setText(QtGui.QApplication.translate("Form", "t2", None,
                                                     QtGui.QApplication.UnicodeUTF8))
        self.time_rewind.setText(
            QtGui.QApplication.translate("Form", "time", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.p.setText(QtGui.QApplication.translate("Form", "p", None,
                                                    QtGui.QApplication.UnicodeUTF8))
        self.Q_tm.setText(QtGui.QApplication.translate("Form", "Qin", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.Q_fl.setText(QtGui.QApplication.translate("Form", "Qin", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.V_chamber.setText(QtGui.QApplication.translate("Form", "V", None,
                                                            QtGui.QApplication.UnicodeUTF8))
        self.S_tm.setText(QtGui.QApplication.translate("Form", "S", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.S_fl.setText(QtGui.QApplication.translate("Form", "S", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.x1.setText(QtGui.QApplication.translate("Form", "x1", None,
                                                     QtGui.QApplication.UnicodeUTF8))
        self.x100.setText(QtGui.QApplication.translate("Form", "x100", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.x0_5.setText(QtGui.QApplication.translate("Form", "x0.5", None,
                                                       QtGui.QApplication.UnicodeUTF8))
        self.overflow.setText(QtGui.QApplication.translate("Form", "Air", None,
                                                           QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
