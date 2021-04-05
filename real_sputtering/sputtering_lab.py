import random
import sys

from PyQt5 import QtWidgets, QtCore
import sputtering_calculation
import edit_while_chamber_is_open
import vacuum_system
from diploma_sputtering import Ui_Form
import sputtering_coefficient_calculation
import calculating_things

fl_but = "off"
tm_but = "off"
enable = "off"
overflow = "off"
ready = "red"
water = "off"


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.P = [100000]
        self.t = 0
        self.time = 0
        self.time02 = 0
        self.time03 = 0
        self.time_interval = 10
        self.p0 = 100000
        self.p02 = 133
        self.p_cur = self.p0

        self.setupUi(self)
        self.time_label1.setText(str(0))
        self.time_label2.setText(str(0))
        self.pressure_value.setText(str(self.p0))
        self.show()
        # instantiation the vacuum system
        self.vac_system = vacuum_system.VacuumSystem(self.p0)

    def Enable_but(self):
        global enable
        if enable == "off":
            enable = "on"
            self.status.setText("Power on")
            self.fl_pump.setEnabled(True)
            self.overflow.setEnabled(True)
            self.openChamber.setEnabled(False)
            self.spinbox_V.setEnabled(False)
            self.spinbox_l_fl.setEnabled(False)
            self.spinbox_d_fl.setEnabled(False)
            self.spinbox_Qin1.setEnabled(False)
            self.spinbox_S1.setEnabled(False)
            self.spinbox_l_tm.setEnabled(False)
            self.spinbox_d_tm.setEnabled(False)
            self.spinbox_Qin2.setEnabled(False)
            self.spinbox_S2.setEnabled(False)

        elif enable == "on":
            enable = "off"
            self.status.setText("Power off")
            self.fl_pump.setEnabled(False)
            self.overflow.setEnabled(False)
            if int(self.p_cur) == self.p0:
                self.openChamber.setEnabled(True)
                self.spinbox_V.setEnabled(True)
                self.spinbox_l_fl.setEnabled(True)
                self.spinbox_d_fl.setEnabled(True)
                self.spinbox_Qin1.setEnabled(True)
                self.spinbox_S1.setEnabled(True)
                self.spinbox_l_tm.setEnabled(True)
                self.spinbox_d_tm.setEnabled(True)
                self.spinbox_Qin2.setEnabled(True)
                self.spinbox_S2.setEnabled(True)

    def Enable_fl_pump(self):
        global fl_but
        if fl_but == "off":
            fl_but = "on"
            self.status.setText("Enabled forevacuum pump")
            self.valve3.setEnabled(True)
            self.valve2.setEnabled(True)
            self.overflow.setEnabled(False)

        else:
            fl_but = "off"
            self.status.setText("Disabled forevacuum pump")
            self.valve3.setEnabled(False)
            self.valve2.setEnabled(False)
            self.overflow.setEnabled(True)

    def Enable_tm_pump(self):
        global tm_but
        if tm_but == "off":
            tm_but = "on"
            self.Timer_common_func()
        else:
            tm_but = "off"
            self.Timer_common_func()

    def Enable_valve_1(self):
        if self.vac_system.valve1.state == "close":
            self.vac_system.valve1.state = "open"
            self.tm_pump.setEnabled(False)
            self.Timer_common_func()
        else:
            self.vac_system.valve1.state = "close"
            self.tm_pump.setEnabled(True)
            self.status.setText("Enabled high vacuum pump")
            self.Timer_common_func()

    def Enable_valve_2(self):
        if self.vac_system.valve2.state == "close" and self.p_cur > 133:
            self.vac_system.valve2.state = "open"
            self.valve3.setEnabled(False)
            self.fl_pump.setEnabled(False)
            self.Timer_common_func()

        elif self.vac_system.valve2.state == "close" and self.p_cur < 133:
            self.vac_system.valve2.state = "open"
            self.valve3.setEnabled(False)
            self.tm_pump.setEnabled(True)
            self.fl_pump.setEnabled(False)
            self.Timer_common_func()

        else:
            self.vac_system.valve2.state = "close"
            self.valve3.setEnabled(True)
            self.tm_pump.setEnabled(False)
            self.fl_pump.setEnabled(True)
            self.Timer_common_func()

    def Enable_valve_3(self):
        global v3_but
        if self.vac_system.valve3.state == "close":
            self.vac_system.valve3.state = "open"
            self.valve2.setEnabled(False)
            self.fl_pump.setEnabled(False)
            self.Timer_common_func()

        else:
            self.vac_system.valve3.state = "close"
            self.valve2.setEnabled(True)
            self.fl_pump.setEnabled(True)
            self.Timer_common_func()

    def Enable_overflow(self):
        global overflow
        if overflow == "on":
            overflow = "off"
            self.p0 = self.p_cur
            self.fl_pump.setEnabled(True)
            self.Timer_common_func()
        else:
            overflow = "on"
            self.fl_pump.setEnabled(False)
            self.Timer_common_func()

    def Timer_common_func(self):
        globals()
        self.Timer_common = QtCore.QTimer()
        self.Timer_common.start()
        # forevacuum
        if self.vac_system.valve3.state == "open":
            self.status.setText("Forevacuum pumping in progress")
            self.Timer_common.setInterval(
                self.time_interval * self.timeSlider.value())
            self.Timer_common.timeout.connect(self.forevacuum)

        # running-up and running-down
        elif tm_but == "on" and self.t == 0 and not self.valve1.isEnabled():
            self.valve2.setEnabled(False)
            self.tm_pump.setEnabled(False)
            self.t = random.randint(720, 900)
            self.status.setText("Running-up high vacuum pump")
            self.Timer_common.setInterval(
                self.time_interval * self.timeSlider.value())
            self.Timer_common.timeout.connect(self.count_time)

        elif tm_but == "off" and self.t == 0 and self.valve1.isEnabled():
            self.valve2.setEnabled(False)
            self.valve1.setEnabled(False)
            self.tm_pump.setEnabled(False)
            self.t = random.randint(720, 900)
            self.status.setText("Running-down high vacuum pump")
            self.Timer_common.setInterval(
                self.time_interval * self.timeSlider.value())
            self.Timer_common.timeout.connect(self.count_time)

        elif tm_but == "on" and self.t != 0 or tm_but == "off" and self.t != 0:
            print(self.t)
            self.Timer_common.setInterval(
                self.time_interval * self.timeSlider.value())
            self.Timer_common.timeout.connect(self.count_time)

        # turbomolecular
        elif self.vac_system.valve1.state == "open":
            self.status.setText("High vacuum pumping in progress")
            self.Timer_common.setInterval(
                self.time_interval * self.timeSlider.value())
            self.Timer_common.timeout.connect(self.turbomolecular)

        # overflow
        elif overflow == "on":
            self.status.setText("Air is admitted")
            self.Timer_common.setInterval(
                self.time_interval * self.timeSlider.value())
            self.Timer_common.timeout.connect(self.updateOverflow)

        # stop
        else:
            self.Timer_common.stop()

    def count_time(self):
        global ready
        self.t -= 1
        if self.t == 0:
            self.tm_pump.setEnabled(True)
            if ready == "red":
                self.readiness.setStyleSheet("background-color: green;")
                ready = "green"
                self.status.setText("Enabled high vacuum pump")
                self.valve1.setEnabled(True)
                self.Timer_common.stop()
            else:
                self.readiness.setStyleSheet("background-color: red;")
                ready = "red"
                self.status.setText("Disabled high vacuum pump")
                self.valve2.setEnabled(True)
                self.Timer_common.stop()

    def forevacuum(self):
        self.time += 1
        self.p_cur = self.vac_system.pump.start_pump(self.time,
                                                     self.p_cur,
                                                     p02=self.p02,
                                                     S01=self.spinbox_S1.value(),
                                                     S02=self.spinbox_S2.value(),
                                                     V=self.spinbox_V.value(),
                                                     Qin1=self.spinbox_Qin1.value(),
                                                     Qin2=self.spinbox_Qin2.value(),
                                                     d1=self.spinbox_d_fl.value(),
                                                     l1=self.spinbox_l_fl.value(),
                                                     d2=self.spinbox_d_tm.value(),
                                                     l2=self.spinbox_d_tm.value())
        self.P.append(self.p_cur)
        # print self.P
        self.pressure_value.setText(str(round(self.p_cur, 2)))
        self.time_label1.setText(str(self.time))

    def turbomolecular(self):
        global water
        self.time02 += 1
        Q_flow = self.gas_flow.value() * 10 ** -5
        total_flow = Q_flow + self.spinbox_Qin2.value()
        self.p_cur = self.vac_system.pump2.start_pump(self.time02,
                                                      self.p_cur,
                                                      p02=self.p02,
                                                      S01=self.spinbox_S1.value(),
                                                      S02=self.spinbox_S2.value(),
                                                      V=self.spinbox_V.value(),
                                                      Qin1=self.spinbox_Qin1.value(),
                                                      Qin2=total_flow,
                                                      d1=self.spinbox_d_fl.value(),
                                                      l1=self.spinbox_l_fl.value(),
                                                      d2=self.spinbox_d_tm.value(),
                                                      l2=self.spinbox_d_tm.value()
                                                      )
        self.P.append(self.p_cur)
        # print self.P
        self.pressure_value.setText(str(round(self.p_cur, 5)))
        self.time_label2.setText(str(self.time02))
        if float(self.p_cur) < 0.0005:
            self.gas_flow.setEnabled(True)
        if Q_flow > 0 and self.goal_pressure-0.1 < self.p_cur < self.goal_pressure+0.1 and water == "on":
            self.calculatingFilm.setEnabled(True)
        else:
            self.calculatingFilm.setEnabled(False)

    def updateOverflow(self):
        self.time03 += 1
        self.p_cur = self.vac_system.pump.overflow(self.time03, self.p_cur)
        self.P.append(self.p_cur)
        self.p02 = 133
        if self.time != 0:
            self.time = 0
            self.time02 = 0
            self.time03 = 0
        self.pressure_value.setText(str(round(self.p_cur, 0)))
        if int(self.p_cur) == self.p0:
            self.Timer_common.stop()

    def open_chamber_but(self):
        info = edit_while_chamber_is_open.New_Window()
        self.r = info.radius.value()
        self.material = info.target.currentText()
        self.inert_gas = info.gas.currentText()
        self.energy = info.energy.value()
        self.goal_pressure = info.pressure.value()
        T = 773

        self.S = sputtering_coefficient_calculation.calculation(self.material,
                                                                self.inert_gas,
                                                                self.energy)

        if self.S == "No such pair":
            self.status_2.setText("Unavailable combination of material and gas")
        else:
            self.M1 = self.S[1]
            self.M2 = self.S[2]
            d1 = self.S[3]
            d2 = self.S[4]
            self.Ecv = self.S[5]
            self.S = self.S[0]
            self.h_and_L = calculating_things.calculating_h(T, self.M1,
                                                            self.M2, d1, d2,
                                                            self.Ecv,
                                                            self.goal_pressure)
            self.status_2.setText(
                "Recommended h = {} cm".format(self.h_and_L[1]))
            self.Lambda = self.h_and_L[0]
            self.h = self.h_and_L[1]
            self.Lk = self.h_and_L[2]
            self.Enable.setEnabled(True)
            self.overflow.setEnabled(True)
            self.gas.setText(self.inert_gas)

    def calculating_film_but(self):
        sputtering_calculation.Sputtering_Window(h=self.h,
                                                 r=self.r,
                                                 material=self.material,
                                                 sputtering_coef=self.S,
                                                 M2=self.M2,
                                                 Lambda=self.Lambda,
                                                 Lk=self.Lk)

    def water_button_clicked(self):
        global water
        if water == "off":
            water = "on"
            self.water_button.setStyleSheet(
                "background-color: rgb(0, 255, 255)")
        else:
            water = "off"
            self.water_button.setStyleSheet(
                "background-color: rgb(204, 204, 204)")


if __name__ == "__main__":
    # create app
    app = QtWidgets.QApplication(sys.argv)

    # create form and init UI
    ui = MainWindow()

    # logic
    ui.Enable.clicked.connect(ui.Enable_but)
    ui.fl_pump.clicked.connect(ui.Enable_fl_pump)
    ui.valve3.clicked.connect(ui.Enable_valve_3)
    ui.valve2.clicked.connect(ui.Enable_valve_2)
    ui.valve1.clicked.connect(ui.Enable_valve_1)
    ui.tm_pump.clicked.connect(ui.Enable_tm_pump)
    ui.timeSlider.valueChanged.connect(ui.Timer_common_func)
    ui.overflow.clicked.connect(ui.Enable_overflow)
    ui.openChamber.clicked.connect(ui.open_chamber_but)
    ui.calculatingFilm.clicked.connect(ui.calculating_film_but)
    ui.water_button.clicked.connect(ui.water_button_clicked)

    # run app
    sys.exit(app.exec_())
