from PyQt5 import QtWidgets, QtCore
from dialog_sputtering import Ui_Dialog
from numpy import pi, sqrt, log10

damper_but = "off"
voltage_but = "off"


class Sputtering_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, h, r, material, sputtering_coef):
        super(Sputtering_Window, self).__init__()

        self.setupUi(self)

        self.show()

        ro = 0
        M = 0
        if material == "Cu":
            ro = 8.92
            M = 63.546
        elif material == "Mo":
            ro = 10.22
            M = 95.96
        elif material == "Ti":
            ro = 4.54
            M = 47.867

        self.h = h / 100 # m
        self.ro = ro # g/cm3
        self.r = r / 100 # m
        self.M = M # g/mole
        self.sputtering_coef = sputtering_coef
        self.NA = 6.02 * 10 ** 23

        I = 0.3 # current
        d = 10 # cm
        area = (pi * d ** 2) / 4 # cm^2
        self.j = I / area # A / cm^2


        self.q = 1.6 * 10 ** -19

        self.sputtering_coefficient.setText(str(round(self.sputtering_coef, 2)))

        self.time = 0
        self.time_interval = 10

        self.voltage.clicked.connect(self.voltage_button)
        self.damper.clicked.connect(self.damper_change)
        self.timeSlider.valueChanged.connect(self.Timer_sputtering)

        self.exec_()

    def voltage_button(self):
        global voltage_but
        if voltage_but == "off":
            voltage_but = "on"
            self.voltage.setStyleSheet("background-color: green;")
            self.damper.setEnabled(True)
        else:
            voltage_but = "off"
            self.voltage.setStyleSheet("background-color: red;")
            self.damper.setEnabled(False)

    def damper_change(self):
        global damper_but
        if damper_but == "off":
            damper_but = "on"
            self.damper_state.setStyleSheet("background-color: green;")
            self.Timer_sputtering()
        else:
            damper_but = "off"
            self.damper_state.setStyleSheet("background-color: red;")
            self.Timer_sputtering()

    def Timer_sputtering(self):
        global damper_but
        self.TimerSputtering = QtCore.QTimer()
        if damper_but == "on":
            self.status.setText("in progress...")
            self.TimerSputtering.start()
            self.TimerSputtering.setInterval(
                self.time_interval * self.timeSlider.value())
            self.TimerSputtering.timeout.connect(self.timeCounter)
        else:
            self.TimerSputtering.stop()

    def timeCounter(self):
        self.time += 1
        v_sput = ((6.25 * 10 ** 25) * self.j * self.sputtering_coef * self.M) / (self.NA * self.ro)
        v_deposition_0 = (v_sput / 2) * (1 + (self.r ** 2 - self.h ** 2) / ((self.h ** 2 + self.r ** 2) ** 0.5))
        v_deposition_r = (v_sput / 2) * (1 + (0 - self.h ** 2) / (((self.h ** 2) + (2 * self.r * self.h) ** 2) ** 0.5))
        d0 = v_deposition_0 * self.time
        dr = v_deposition_r * self.time
        K = v_deposition_r / v_deposition_0
        self.d0.setText(str(round(d0, 1)))
        self.dr.setText(str(round(dr, 1)))
        self.K0.setText(str(round(K, 2)))
        self.time_value.setText(str(self.time))

