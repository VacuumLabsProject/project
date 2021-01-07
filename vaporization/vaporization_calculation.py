from PySide import QtGui
from dialog_vaporization import Ui_Dialog
from numpy import pi

damper_but = "off"


def calculate_d0(m, ro, h):
    d0 = m / (4 * pi * ro * h ** 2)
    return d0


def calculate_dr(m, ro, h, r):
    dr = (m / (4 * pi * ro * h ** 2)) * (1 + (r / h) ** 2) ** (-3 / 2)
    return dr


class Vaporization_Window(QtGui.QDialog, Ui_Dialog):
    def __init__(self, h, r, material, mass):
        super(Vaporization_Window, self).__init__()

        self.setupUi(self)

        self.show()
        ro = 0
        if material == "Cr":
            ro = 7.19
        elif material == "Al":
            ro = 2.6989
        elif material == "Ti":
            ro = 4.54
        self.h = h
        self.m = mass
        self.ro = ro
        self.r = r

        self.current_dial.valueChanged.connect(
            self.current_value)
        self.voltage_dial.valueChanged.connect(
            self.voltage_value)
        self.damper.clicked.connect(self.damper_change)

        self.exec_()

    def current_value(self):
        self.current.setText(str(self.current_dial.value()))

    def voltage_value(self):
        self.voltage.setText(str(self.voltage_dial.value()))

    def damper_change(self):
        global damper_but
        if damper_but == "off":
            damper_but = "on"
            self.damper_state.setStyleSheet("background-color: green;")
            d0_value = calculate_d0(self.m, self.ro, self.h)
            dr_value = calculate_dr(self.m, self.ro, self.h, self.r)
            K_value = dr_value / d0_value
            self.d0.setText(str(round(d0_value, 2)))
            self.dr.setText(str(round(dr_value, 2)))
            self.K.setText(str(round(K_value, 2)))

        else:
            damper_but = "off"
            self.damper_state.setStyleSheet("background-color: red;")



