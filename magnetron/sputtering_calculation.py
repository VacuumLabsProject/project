from PyQt5 import QtWidgets, QtCore
from dialog_sputtering import Ui_Dialog
from numpy import pi, sqrt, log10, arctan

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
        M2 = M2 / 1000  # kg/mole Target

        # кольцевой источник
        NA = 6.02 * 10 ** 23
        q = 1.6 * 10 ** (-19)

        cathode_r = 3  # cm
        ring_r_out = 2.5  # cm
        ring_r_in = 2  # cm

        S = pi * ((ring_r_out / 100) ** 2 - (ring_r_in / 100) ** 2) # площадь плазмы

        I = 0.4 # A
        j = I / S # A/m2

        Jm = (M2 * sputtering_coef * j) / (NA * q)
        # пока что модель бесконечно тонкого кольцевого источника
        r_ring = 2.25/100 # m
        Jrasp_0 = Jm * (1 + (r_ring/h)**2)**(-2)
        Jrasp_r = Jm * ((1 + (r/h)**2 + (r_ring/h)**2) / ((1 - (r/h)**2 + (r_ring/h)**2)**2 + 4 * (r_ring/h)**2) ** (3/2))
        Jnap_0 = (Jrasp_0 * Lambda) / (Lambda + (sqrt(Lk) - sqrt(h)) ** 2)
        Jnap_r = (Jrasp_r * Lambda) / (Lambda + (sqrt(Lk) - sqrt(h))**2)
        self.v_nap_0 = Jnap_0 / ro
        self.v_nap_r = Jnap_r / ro
        # print(self.v_nap_0)
        # print(self.v_nap_r)
        self.sputtering_coefficient.setText(
            str(round(sputtering_coef, 2)))
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
        d0 = self.v_nap_0 * self.time * 10**9
        dr = self.v_nap_r * self.time * 10**9
        self.d0.setText(str(round(d0, 2)))
        self.dr.setText(str(round(dr, 2)))
        # self.K0.setText(str(round(K, 2)))
        self.time_value.setText(str(self.time))
