from PySide import QtGui, QtCore
from dialog_vaporization import Ui_Dialog
from numpy import pi, sqrt, log10

damper_but = "off"

"""
def calculate_d0(m, ro, h):
    d0 = m / (4 * pi * ro * h ** 2)
    return d0


def calculate_dr(m, ro, h, r):
    dr = (m / (4 * pi * ro * h ** 2)) * (1 + (r / h) ** 2) ** (-3 / 2)
    return dr


def calculate_p0(A, B, Tvap):
    lgp0 = A - B / Tvap
    p0 = (10 ** lgp0) * 133
    return p0
"""

class Vaporization_Window(QtGui.QDialog, Ui_Dialog):
    def __init__(self, h, r, material, mass):
        super(Vaporization_Window, self).__init__()

        self.setupUi(self)

        self.show()

        self.R = 8.31

        ro = 0
        A = 0
        B = 0
        C = 0
        M = 0
        if material == "Cr":
            ro = 7190
            A = 9.94
            B = 20000
            C = 9.56
            M = 0.0519961
        elif material == "Al":
            ro = 2710
            A = 8.79
            B = 15940
            C = 8.27
            M = 0.0269815386
        elif material == "Ti":
            ro = 4540
            A = 9.5
            B = 23230
            C = 9.11
            M = 0.047867
        self.h = h / 100 # m
        self.m = mass / 1000 # kg
        self.ro = ro # kg/m3
        self.r = r / 100 # m
        self.A = A
        self.B = B
        self.C = C
        self.M = M # kg/mole

        self.jm = 0

        self.d0_val = 0
        self.d0_max = 1

        self.S = 4 * 10 ** -4 # spiral surface area
        self.eps = 0.5
        self.S_B = 5.67 * 10 ** -8

        self.time = 0
        self.time_interval = 10

        self.current_dial.valueChanged.connect(
            self.current_value)
        self.voltage_dial.valueChanged.connect(
            self.voltage_value)
        self.damper.clicked.connect(self.damper_change)
        self.timeSlider.valueChanged.connect(self.Timer_sputtering)

        self.exec_()

    def current_value(self):
        self.current.setText(str(self.current_dial.value()))
        self.Timer_sputtering()

    def voltage_value(self):
        self.voltage.setText(str(self.voltage_dial.value()))
        self.Timer_sputtering()

    def damper_change(self):
        global damper_but
        if damper_but == "off":
            damper_but = "on"
            self.damper_state.setStyleSheet("background-color: green;")
            self.Timer_sputtering()
        else:
            damper_but = "off"
            self.damper_state.setStyleSheet("background-color: red;")

    def Timer_sputtering(self):
        global damper_but
        self.TimerSputtering = QtCore.QTimer()
        if self.S * self.jm * self.time >= self.m:
            pass
        elif damper_but == "on":
            self.TimerSputtering.start()
            Q = self.current_dial.value() * self.voltage_dial.value()
            T = (Q / (self.eps * self.S_B * self.S)) ** (1. / 4)
            self.temperature.setText(str(int(T)))
            # P0 = calculate_p0(self.A, self.B, T)
            self.jm = 10 ** (1 + self.C - 0.5 * log10(T) - (self.B / T))
            self.TimerSputtering.setInterval(
                self.time_interval * self.timeSlider.value())
            self.TimerSputtering.timeout.connect(self.timeCounter)

    def timeCounter(self):
        self.time += 1
        v0 = self.S * self.jm / (pi * self.ro * self.h ** 2)
        vr = v0 * ((1 + (self.r / self.h) ** 2) ** (-2))
        self.d0_val = v0 * self.time
        dr_val = vr * self.time
        K_val = self.d0_val / dr_val
        self.d0.setText(str(round(self.d0_val * 1000000000, 0)))
        self.dr.setText(str(round(dr_val * 1000000000, 0)))
        self.K.setText(str(round(K_val, 2)))
        if self.S * self.jm * self.time >= self.m:
            self.TimerSputtering.stop()



