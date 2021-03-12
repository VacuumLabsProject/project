from PyQt5 import QtWidgets, QtCore
from dialog_sputtering import Ui_Dialog
from numpy import pi, sqrt, log10

damper_but = "off"
voltage_but = "off"


class Sputtering_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, h, r, material, sputtering_coef, M2, Lambda, Lk):
        super(Sputtering_Window, self).__init__()

        self.setupUi(self)

        self.show()

        ro = 0
        if material == "Cu":
            ro = 8.92
        elif material == "Mo":
            ro = 10.22
        elif material == "Ti":
            ro = 4.54

        h = h / 100  # m
        ro = ro * 1000  # kg/m3
        r = r / 100  # m
        M2 = M2 / 1000
        # дисковый источник

        NA = 6.02 * 10 ** 23
        q = 1.6 * 10 ** (-19)

        I = 0.4 # current
        d = 0.1 # m радиус распылителя
        area = (pi * d ** 2) / 4 # cm^2
        j = I / area # A / cm^2

        Jm = (M2 * sputtering_coef * j) / (NA * q)
        Jrasp_0 = (Jm / 2) * ((2 * (d/h)**2) / (1 + (d/h)**2))
        Jrasp_r = (Jm / 2) * (1 - ((1 + (r/h)**2 - (d/h)**2) / sqrt((1 - (r/h)**2 + (d/h)**2)**2 + 4 * (r/h)**2)))
        Jnap_0 = (Jrasp_0 * Lambda) / (Lambda + (sqrt(Lk) - sqrt(h)) ** 2)
        Jnap_r = (Jrasp_r * Lambda) / (Lambda + (sqrt(Lk) - sqrt(h)) ** 2)
        self.vnap_0 = Jnap_0 / ro
        self.vnap_r = Jnap_r / ro
        self.sputtering_coefficient.setText(str(round(sputtering_coef, 2)))

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

        d0 = self.vnap_0 * self.time * 10**9
        dr = self.vnap_r * self.time * 10**9
        K = (d0 - dr) / d0
        self.d0.setText(str(round(d0, 2)))
        self.dr.setText(str(round(dr, 2)))
        self.K0.setText(str(round(K, 2)))
        self.time_value.setText(str(self.time))

