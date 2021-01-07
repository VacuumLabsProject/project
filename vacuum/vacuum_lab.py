from PySide import QtGui, QtCore
from diploma import Ui_Form
from numpy import exp
import sys
import vacuum_system
import time
import calculating_pressure
import core
import random

fl_but = "off"
v1_but = "off"
v2_but = "off"
v3_but = "off"
tm_but = "off"
enable = "off"
overflow = "off"
ready = "red"


class MainWindow(QtGui.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.P = [100000]
        self.time = 0
        self.time02 = 0
        self.time03 = 0
        self.time_interval = 10
        self.p0 = 100000
        self.p02 = 133
        self.p_cur = self.p0

        # determination of the moment of switching on of overflow
        self.q1 = 0
        self.q2 = 0

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

        elif enable == "on":
            enable = "off"
            self.status.setText("Power off")
            self.fl_pump.setEnabled(False)
            self.overflow.setEnabled(False)

    def Enable_fl_pump(self):
        global fl_but
        if fl_but == "off":
            fl_but = "on"
            self.status.setText("Enabled forevacuum pump")
            self.valve3.setEnabled(True)
            self.valve2.setEnabled(True)
            self.Timer_on()
        else:
            fl_but = "off"
            self.status.setText("Disabled forevacuum pump")
            self.valve3.setEnabled(False)
            self.valve2.setEnabled(False)
            self.Timer_on()

    def Enable_tm_pump(self):
        global tm_but
        if tm_but == "off":
            tm_but = "on"
            self.Timer_tm_pump()
            self.Timer_on()
        else:
            tm_but = "off"
            self.Timer_tm_pump()
            self.Timer_on()

    def Enable_valve_1(self):
        global v1_but
        if v1_but == "off":
            v1_but = "on"
            self.overflow.setEnabled(False)
            self.Timer_on()
        else:
            v1_but = "off"
            self.status.setText("Enabled high vacuum pump")
            self.overflow.setEnabled(True)
            self.Timer_on()

    def Enable_valve_2(self):
        global v2_but
        if v2_but == "off":
            v2_but = "on"
            self.valve3.setEnabled(False)
            self.tm_pump.setEnabled(True)
            self.Timer_on()
        else:
            v2_but = "off"
            self.valve3.setEnabled(True)
            self.tm_pump.setEnabled(False)
            self.Timer_on()

    def Enable_valve_3(self):
        global v3_but
        if v3_but == "off":
            v3_but = "on"
            self.overflow.setEnabled(False)
            self.valve2.setEnabled(False)
            self.Timer_on()
        else:
            v3_but = "off"
            self.overflow.setEnabled(True)
            self.valve2.setEnabled(True)
            self.Timer_on()

    # Fake timer, that runs when timeSlider switched
    # while activating or deactivating tm pump
    def FakeTimer(self):
        global tm_but
        self.TimerTmPump = QtCore.QTimer()  # do not move to __init__
        self.TimerTmPump.start()
        if not self.valve1.isEnabled() and self.p_cur < 133 and tm_but == "on":
            self.TimerTmPump.setInterval(
                self.time_interval * self.timeSlider.value())
            self.TimerTmPump.timeout.connect(self.count_time)

        elif not self.valve1.isEnabled() and self.p_cur < 133 and tm_but == "off":
            self.TimerTmPump.setInterval(
                self.time_interval * self.timeSlider.value())
            self.TimerTmPump.timeout.connect(self.count_time2)

    # powered up and powered-down tm_pump
    def Timer_tm_pump(self):
        self.TimerTmPump = QtCore.QTimer()  # do not move to __init__
        self.TimerTmPump.start()
        if not self.valve1.isEnabled() and self.p_cur < 133:
            self.t = random.randint(720, 900)
            self.status.setText("Running-up high vacuum pump")
            self.TimerTmPump.setInterval(self.time_interval*self.timeSlider.value())
            self.TimerTmPump.timeout.connect(self.count_time)

        elif self.valve1.isEnabled():
            self.t = random.randint(720, 900)
            self.valve1.setEnabled(False)
            self.valve2.setEnabled(False)
            self.status.setText("Running-down high vacuum pump")
            self.TimerTmPump.setInterval(self.time_interval*self.timeSlider.value())
            self.TimerTmPump.timeout.connect(self.count_time2)

    def count_time(self):
        global ready
        self.t -= 1
        # print self.t
        if self.t == 0:
            self.readiness.setStyleSheet("background-color: green;")
            ready = "green"
            self.status.setText("Enabled high vacuum pump")
            self.valve1.setEnabled(True)
            self.TimerTmPump.stop()

    def count_time2(self):
        global ready
        self.t -= 1
        # print self.t
        if self.t == 0:
            self.readiness.setStyleSheet("background-color: red;")
            ready = "red"
            self.status.setText("Disabled high vacuum pump")
            self.valve2.setEnabled(True)
            self.TimerTmPump.stop()

    # calculating pressure at both modes
    def Timer_on(self):
        self.TimerUp = QtCore.QTimer()  # do not move to __init__
        if fl_but == "on" and v3_but == "on":
            self.TimerUp.start()
            self.status.setText("Forevacuum pumping in progress")
            self.TimerUp.setInterval(self.time_interval*self.timeSlider.value())
            self.TimerUp.timeout.connect(self.updateTime)

        elif fl_but == "on" and tm_but == "on" and v2_but == "on" and v1_but == "on" and v3_but == "off":
            self.TimerUp.start()
            self.status.setText("High vacuum pumping in progress")
            self.TimerUp.setInterval(self.time_interval*self.timeSlider.value())
            self.TimerUp.timeout.connect(self.updateTime2)

        elif fl_but == "on" and v3_but == "off" and v2_but == "off":
            self.TimerUp.stop()
            self.status.setText("Enabled forevacuum pump")
            self.p02 = self.p_cur

        else:
            self.TimerUp.stop()

    def updateTime(self):
        self.time += 1
        self.p_cur = self.vac_system.pump.start_pump(self.time,
                                                     self.p0,
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
        if self.p_cur > 133:
            self.progressBar.setValue(self.p_cur)
        else:
            self.progressBar_2.setValue(self.p_cur)
        self.time_label1.setText(str(self.time))

    def updateTime2(self):
        self.time02 += 1
        self.p_cur = self.vac_system.pump2.start_pump(self.time02,
                                                      self.p02,
                                                      S01=self.spinbox_S1.value(),
                                                      S02=self.spinbox_S2.value(),
                                                      V=self.spinbox_V.value(),
                                                      Qin1=self.spinbox_Qin1.value(),
                                                      Qin2=self.spinbox_Qin2.value(),
                                                      d1=self.spinbox_d_fl.value(),
                                                      l1=self.spinbox_l_fl.value(),
                                                      d2=self.spinbox_d_tm.value(),
                                                      l2=self.spinbox_d_tm.value()
                                                      )
        self.P.append(self.p_cur)
        #print self.P
        self.pressure_value.setText(str(round(self.p_cur, 5)))
        self.progressBar_2.setValue(self.p_cur)
        self.time_label2.setText(str(self.time02))

    # running time-slider
    def chose_time(self):
        globals()
        if fl_but == "on" and v3_but == "on" and v2_but == "off" and v1_but == "off" and tm_but == "off" or fl_but == "on" and v3_but == "off" and v2_but == "on" and v1_but == "on" and tm_but == "on":
            self.Timer_on()
        elif fl_but == "on" and v3_but == "off" and v2_but == "on" and v1_but == "off" and tm_but == "on":
            self.FakeTimer()
        elif fl_but == "on" and v3_but == "off" and v2_but == "on" and v1_but == "off" and tm_but == "off" and ready == "green":
            self.FakeTimer()
        elif overflow == "on" and int(self.p_cur) == self.p0:
            pass
        elif overflow == "on":
            self.updateOverflow()

    def overflow_but(self):
        global overflow
        self.TimerOverflow = QtCore.QTimer()  # do not move to __init__
        if overflow == "off":
            overflow = "on"
            if not self.valve1.isEnabled():
                self.q1 = 1
            else:
                self.valve1.setEnabled(False)
            if not self.valve3.isEnabled():
                self.q2 = 1
            else:
                self.valve3.setEnabled(False)
            self.TimerOverflow.start()
            self.status.setText("Air is admitted")
            self.TimerOverflow.setInterval(
                self.time_interval * self.timeSlider.value())
            self.TimerOverflow.timeout.connect(self.updateOverflow)
        else:
            overflow = "off"
            if self.q1 == 0:
                self.valve1.setEnabled(True)
            else:
                pass
            if self.q2 == 0:
                self.valve3.setEnabled(True)
            else:
                pass
            self.status.setText("Ready to work")
            self.TimerOverflow.stop()

    def updateOverflow(self):
        self.time03 += 1
        self.p_cur = self.vac_system.pump.overflow(self.time03, self.p_cur)
        self.P.append(self.p_cur)

        self.progressBar_2.setValue(133)
        self.progressBar.setValue(self.p_cur)
        self.pressure_value.setText(str(round(self.p_cur, 0)))
        if int(self.p_cur) == self.p0:
            self.time = 0
            self.time02 = 0
            self.time03 = 0
            self.TimerOverflow.stop()


if __name__ == "__main__":
    # create app
    app = QtGui.QApplication(sys.argv)

    # create form and init UI
    ui = MainWindow()

    # logic

    ui.Enable.clicked.connect(ui.Enable_but)
    ui.fl_pump.clicked.connect(ui.Enable_fl_pump)
    ui.valve3.clicked.connect(ui.Enable_valve_3)
    ui.valve2.clicked.connect(ui.Enable_valve_2)
    ui.valve1.clicked.connect(ui.Enable_valve_1)
    ui.tm_pump.clicked.connect(ui.Enable_tm_pump)
    ui.timeSlider.valueChanged.connect(ui.chose_time)
    ui.overflow.clicked.connect(ui.overflow_but)


    # run app
    sys.exit(app.exec_())
