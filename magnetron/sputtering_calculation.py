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

        self.d0_start = 0
        self.dr_start = 0

        ro = 0
        if material == "Cu":
            ro = 8.92
        elif material == "Mo":
            ro = 10.22
        elif material == "Ti":
            ro = 4.54

        self.h = h / 100  # m
        self.ro = ro * 1000  # kg/m3
        self.r = r / 100  # m
        self.M2 = M2 / 1000  # kg/mole Target
        self.sputtering_coef = sputtering_coef
        self.Lambda = Lambda
        self.Lk = Lk

        # кольцевой источник
        self.NA = 6.02 * 10 ** 23
        self.q = 1.6 * 10 ** (-19)

        self.cathode_r = 3  # cm
        self.ring_r_out = 2.5  # cm
        self.ring_r_in = 2  # cm

        self.area = pi * ((self.ring_r_out / 100) ** 2 - (self.ring_r_in / 100) ** 2) # площадь плазмы

        # пока что модель бесконечно тонкого кольцевого источника
        self.r_ring = 2.25/100 # m

        self.sputtering_coefficient.setText(
            str(round(sputtering_coef, 2)))

        I = self.current_dial.value() / 10 # A
        Jcond_0, Jcond_r = self.calculate_J(I)
        self.vcond_0 = Jcond_0 / self.ro
        self.vcond_r = Jcond_r / self.ro

        self.current.setText(str(I))

        self.time = 0
        self.time_interval = 10

        self.current_dial.valueChanged.connect(self.current_change)
        self.voltage.clicked.connect(self.voltage_button)
        self.damper.clicked.connect(self.damper_change)
        self.timeSlider.valueChanged.connect(self.Timer_sputtering)

        self.exec_()

    def calculate_J(self, I):
        # дисковый источник
        j_razr = I / self.area # A/m2
        # учитываем вторичную эмиссию, примем её 0.1
        ji = j_razr / 1.2  # A / m^2

        Jm = (self.M2 * self.sputtering_coef * ji) / (self.NA * self.q)
        # плотность напыления
        Jnap_0 = Jm * (1 + (self.r_ring / self.h) ** 2) ** (-2)
        Jnap_r = Jm * ((1 + (self.r / self.h) ** 2 + (self.r_ring / self.h) ** 2) / (
                    (1 - (self.r / self.h) ** 2 + (self.r_ring / self.h) ** 2) ** 2 + 4 * (
                        self.r_ring / self.h) ** 2) ** (3 / 2))
        # плотность осаждения
        Jcond_0 = (Jnap_0 * self.Lambda) / (self.Lambda + (sqrt(self.Lk) - sqrt(self.h)) ** 2)
        Jcond_r = (Jnap_r * self.Lambda) / (self.Lambda + (sqrt(self.Lk) - sqrt(self.h)) ** 2)

        return Jcond_0, Jcond_r

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

        self.current.setText(str(I))
        Jcond_0, Jcond_r = self.calculate_J(I)
        self.vcond_0 = Jcond_0 / self.ro
        self.vcond_r = Jcond_r / self.ro

    def damper_change(self):
        global damper_but
        if damper_but == "off":
            damper_but = "on"
            self.damper_state.setStyleSheet("background-color: green;")
            self.Timer_sputtering()
        else:
            damper_but = "off"
            self.d0_start = self.d0_val
            self.dr_start = self.dr_val
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
        self.d0_val = self.d0_start + self.vcond_0 * self.time * 10**9
        self.dr_val = self.dr_start + self.vcond_r * self.time * 10**9
        self.d0.setText(str(round(self.d0_val, 2)))
        self.dr.setText(str(round(self.dr_val, 2)))
        # self.K0.setText(str(round(K, 2)))
        self.time_value.setText(str(self.time))
