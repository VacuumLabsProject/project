from PyQt5 import QtWidgets, QtCore
from magnetron.qt_py.dialog_sputtering import Ui_Dialog
from numpy import pi, sqrt, log10, arctan
# import scipy.integrate as integrate

damper_but = "off"
voltage_but = "off"


class Sputtering_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, h, r, material, sputtering_coef, M2, Lambda, Lk):
        super(Sputtering_Window, self).__init__()

        self.setupUi(self)

        self.show()

        self.d0_start = 0
        self.dr_start = 0
        self.time_start = 0

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

        #self.cathode_r = 3 / 100 # m
        self.ring_r_out = 2.5 / 100  # m
        self.ring_r_in = 2.3 / 100  # m

        self.area = pi * (self.ring_r_out ** 2 - self.ring_r_in ** 2) # площадь плазмы

        # пока что модель бесконечно тонкого кольцевого источника
        self.r_ring = 2.4/100 # m

        self.target_diameter.setText(str(round(self.r * 1000)))
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
        ji = j_razr / 1.1  # A / m^2
        #print("***********************************************")
        self.Jm = (self.M2 * self.sputtering_coef * ji) / (self.NA * self.q)
        # плотность напыления
        """
        Jnap_0 = integrate.quad(self.integral_0, self.ring_r_in, self.ring_r_out)[0]
        Jnap_r = integrate.quad(self.integral_r, self.ring_r_in, self.ring_r_out)[0]
        print(Jnap_0)
        print(Jnap_r)
        Jcond_0 = (Jnap_0 * self.Lambda) / (
                    self.Lambda + (sqrt(self.Lk) - sqrt(self.h)) ** 2)
        Jcond_r = (Jnap_r * self.Lambda) / (
                    self.Lambda + (sqrt(self.Lk) - sqrt(self.h)) ** 2)
        print(Jcond_0)
        print(Jcond_r)
        """
        #print("__________________________________________")
        # толщина 2 мм. Такой рассчет верный, если толщина << радиуса
        # 0.002
        Jnap_0 = (self.Jm * (1 + (self.r_ring / self.h) ** 2) ** (-2)) * 0.002
        #print(Jnap_0)
        Jnap_r = (self.Jm * ((1 + (self.r / self.h) ** 2 +
                        (self.r_ring / self.h) ** 2) /
                       ((1 - (self.r / self.h) ** 2 +
                         (self.r_ring / self.h) ** 2) ** 2 +
                        4 * (self.r_ring / self.h) ** 2) ** (3 / 2))) * 0.002
        #print(Jnap_r)
        # плотность осаждения
        Jcond_0 = (Jnap_0 * self.Lambda) / (self.Lambda + (sqrt(self.Lk) - sqrt(self.h)) ** 2)
        Jcond_r = (Jnap_r * self.Lambda) / (self.Lambda + (sqrt(self.Lk) - sqrt(self.h)) ** 2)
        #print(Jcond_0)
        #print(Jcond_r)

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
            self.current_dial.setEnabled(False)
            self.voltage.setEnabled(False)
            self.damper_state.setStyleSheet("background-color: green;")
            self.Timer_sputtering()
        else:
            damper_but = "off"
            self.current_dial.setEnabled(True)
            self.voltage.setEnabled(True)
            self.d0_start = self.d0_val
            self.dr_start = self.dr_val
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
        self.d0_val = self.d0_start + self.vcond_0 * self.time * 10**9
        self.dr_val = self.dr_start + self.vcond_r * self.time * 10**9
        #K = abs(self.d0_val - self.dr_val) / self.d0_val
        self.d0.setText(str(round(self.d0_val, 2)))
        self.dr.setText(str(round(self.dr_val, 2)))
        #self.K0.setText(str(round(K, 2)))
        self.time_value.setText(str(self.time + self.time_start))

"""
    def integral_0(self, rad):
        l = 0  # center

        d = (2 * (self.h ** 2)) * (((self.h ** 2) + (l ** 2) + (rad ** 2)) /
            (((((self.h ** 2) + (l ** 2) + (rad ** 2)) ** 2) +
            ((2 * l * self.h) ** 2)) ** 1.5)) * rad
        return d

    def integral_r(self, rad):
        l = self.r
        d = (2 * (self.h ** 2)) * (((self.h ** 2) + (l ** 2) + (rad ** 2)) /
            (((((self.h ** 2) + (l ** 2) + (rad ** 2)) ** 2) +
            ((2 * l * self.h) ** 2)) ** 1.5)) * rad
        return d
"""



