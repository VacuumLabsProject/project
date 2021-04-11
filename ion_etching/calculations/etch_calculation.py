from PyQt5 import QtWidgets, QtCore
from ion_etching.ui_py.dialog_etching import Ui_Dialog
from numpy import pi, sqrt

damper_but = "off"
voltage_but = "off"


class Etch_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, r, material, sputtering_coef, M2):
        super(Etch_Window, self).__init__()

        self.setupUi(self)

        self.show()

        self.V_etch_val = 0
        self.H_etch_val = 0
        self.time_start = 0

        ro = 0
        if material == "Cu":
            ro = 8.92
        elif material == "Mo":
            ro = 10.22
        elif material == "Ti":
            ro = 4.54

        self.ro = ro * 1000  # kg/m3
        self.r = r / 100  # m
        self.M2 = M2
        self.sputtering_coef = sputtering_coef

        self.NA = 6.02 * 10 ** 23
        self.q = 1.6 * 10 ** (-19)

        self.target_diameter.setText(str(round(self.r * 1000)))
        self.sputtering_coefficient.setText(str(round(sputtering_coef, 2)))

        I = self.current_dial.value() / 10
        self.gamma = 0.1
        # self.gamma = 0
        self.V_etch_val = self.calculate_etching_rate(I)

        self.current.setText(str(I))
        self.time = 0
        self.time_interval = 10

        self.current_dial.valueChanged.connect(self.current_change)
        self.voltage.clicked.connect(self.voltage_button)
        self.damper.clicked.connect(self.damper_change)
        self.timeSlider.valueChanged.connect(self.Timer_sputtering)
        self.exec_()

    def calculate_etching_rate(self, I):
        area = (pi * self.r ** 2) / 4  # m^2
        j_full = I / area  # A / m^2
        j_ion = j_full / (1 + self.gamma)
        etch_rate = (j_ion * self.M2 * self.sputtering_coef) / (self.q * self.ro * self.NA)
        return etch_rate

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

    def current_change(self):
        I = self.current_dial.value() / 10
        self.V_etch_val = self.calculate_etching_rate(I)
        self.current.setText(str(I))

    def damper_change(self):
        global damper_but
        if damper_but == "off":
            damper_but = "on"
            self.current_dial.setEnabled(False)
            self.voltage.setEnabled(False)
            self.damper_state.setStyleSheet("background-color: green;")
            self.Timer_sputtering()
        else:
            damper_but = "off"
            self.current_dial.setEnabled(True)
            self.voltage.setEnabled(True)
            self.time_start = self.time
            self.time = 0
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
        self.V_etch.setText(str((self.V_etch_val * 10 ** 9).__round__(2)))
        self.H_etch_val = self.V_etch_val * self.time * 10 ** 9
        self.H_etch.setText(str(self.H_etch_val.__round__(2)))
        self.time_value.setText(str(self.time + self.time_start))
        self.movie.jumpToNextFrame()
