from PyQt5 import QtWidgets, QtCore
from evaporation.qt_py.dialog_evaporation import Ui_Dialog
from numpy import pi, sqrt, log10

damper_but = "off"
heat_but = "off"


def calculate_d0(m, ro, h):
    d0 = m / (pi * ro * h ** 2)
    return d0


def calculate_dr(m, ro, h, r):
    dr = (m / (pi * ro * h ** 2)) * (1 + (r / h) ** 2) ** (-2)
    return dr


def calculate_p0(A, B, Tvap):
    lgp0 = A - B / Tvap
    p0 = (10 ** lgp0) * 133
    return p0


def calculate_Jm(B, C, T):
    Jm = 10 ** (1 + C - 0.5 * log10(T) - (B / T))
    return Jm


class Vaporization_Window(QtWidgets.QDialog, Ui_Dialog):
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
        if material == "Cu":
            ro = 8920
            A = 8.96
            B = 16980
            C = 8.63
            M = 0.063546
        elif material == "Al":
            ro = 2710
            A = 8.79
            B = 15940
            C = 8.27
            M = 0.0269815386
        elif material == "Cr":
            ro = 7190
            A = 9.94
            B = 20000
            C = 9.56
            M = 0.0519961

        self.h = h / 100 # m
        self.m = mass / 1000000 # kg
        self.ro = ro # kg/m3
        self.r = r / 100 # m
        self.A = A
        self.B = B
        self.C = C
        self.M = M # kg/mole

        self.jm = 0
        self.T = 0

        self.S = 4 * 10 ** -4 # spiral surface area
        self.eps = 0.8
        self.S_B = 5.67 * 10 ** -8

        self.d0_max = calculate_d0(self.m, self.ro, self.h)
        self.dr_max = calculate_dr(self.m, self.ro, self.h, self.r)
        self.K_max = (self.d0_max - self.dr_max) / self.d0_max

        self.time = 0
        self.time_interval = 10

        self.current_dial.valueChanged.connect(
            self.current_value)
        self.voltage_dial.valueChanged.connect(
            self.voltage_value)
        self.damper.clicked.connect(self.damper_change)
        self.timeSlider.valueChanged.connect(self.Timer_sputtering)
        self.heat.clicked.connect(self.heat_clicked)

        self.exec_()

    def heat_clicked(self):
        global heat_but
        if heat_but == "off":
            heat_but = "on"
        else:
            heat_but = "off"
        self.p_limitation()

    def p_limitation(self):
        global heat_but
        if int(self.T) == 0:
            self.damper.setEnabled(False)
            self.status.setText("Set the temperature of evaporation")
        else:
            if heat_but != "on":
                self.status.setText("Heat the substrate")
                self.damper.setEnabled(False)
            else:
                self.P0 = calculate_p0(self.A, self.B, self.T)
                if self.P0 < 133:
                    self.damper.setEnabled(True)
                    self.status.setText("Ready for work")
                else:
                    self.damper.setEnabled(False)
                    self.status.setText("Saturated steam pressure too high. "
                                    "Decrease the temperature.")


    def current_value(self):
        self.current.setText(str(self.current_dial.value()))
        Q = self.current_dial.value() * self.voltage_dial.value()
        self.T = (Q / (self.eps * self.S_B * self.S)) ** (1. / 4)
        self.temperature.setText(str(int(self.T)))
        self.p_limitation()

    def voltage_value(self):
        self.voltage.setText(str(self.voltage_dial.value()))
        Q = self.current_dial.value() * self.voltage_dial.value()
        self.T = (Q / (self.eps * self.S_B * self.S)) ** (1. / 4)
        self.temperature.setText(str(int(self.T)))
        self.p_limitation()

    def damper_change(self):
        global damper_but
        if damper_but == "off":
            damper_but = "on"
            self.current_dial.setEnabled(False)
            self.voltage_dial.setEnabled(False)
            self.heat.setEnabled(False)
            self.damper_state.setStyleSheet("background-color: green;")
            self.Timer_sputtering()
        else:
            damper_but = "off"
            self.current_dial.setEnabled(True)
            self.voltage_dial.setEnabled(True)
            self.heat.setEnabled(True)
            self.TimerSputtering.stop()
            self.damper_state.setStyleSheet("background-color: red;")

    def Timer_sputtering(self):
        global damper_but
        self.TimerSputtering = QtCore.QTimer()
        if self.S * self.jm * self.time >= self.m:
            pass
        elif damper_but == "on":
            self.status.setText("in progress...")
            self.TimerSputtering.start()
            self.jm = calculate_Jm(self.B, self.C, self.T)
            self.TimerSputtering.setInterval(
                self.time_interval * self.timeSlider.value())
            self.TimerSputtering.timeout.connect(self.timeCounter)

    def timeCounter(self):
        self.time += 1
        if self.S * self.jm * self.time >= self.m:
            self.d0.setText(str(round(self.d0_max * 1000000000, 0)))
            self.dr.setText(str(round(self.dr_max * 1000000000, 0)))
            self.K.setText(str(round(self.K_max, 2)))
            self.t.setText(str(self.time))
            self.status.setText("Done")
            self.TimerSputtering.stop()
        else:
            v0 = self.S * self.jm / (pi * self.ro * self.h ** 2)
            vr = v0 * ((1 + (self.r / self.h) ** 2) ** (-2))
            self.d0_val = v0 * self.time
            dr_val = vr * self.time
            K_val = (self.d0_val - dr_val) / self.d0_val
            self.d0.setText(str(round(self.d0_val * 1000000000, 1)))
            self.dr.setText(str(round(dr_val * 1000000000, 1)))
            self.K.setText(str(round(K_val, 2)))
            self.t.setText(str(self.time))




