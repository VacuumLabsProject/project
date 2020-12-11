from PySide import QtGui, QtCore
from diploma import Ui_Form
from numpy import exp
import sys
import vacuum_system
import time

fl_but = "off"
v1_but = "off"
v2_but = "off"
v3_but = "off"
tm_but = "off"
time_test= time


class MainWindow(QtGui.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.time = 0
        self.time_interval = 1000

        self.p0 = 760
        self.p_cur = self.p0

        self.setupUi(self)
        self.time1.setText(str(self.time))
        self.pressure_value.setText(str(self.p_cur * 133))
        self.show()

        # instantiation the vacuum system
        self.vac_system = vacuum_system.VacuumSystem(1010)

    def Enable_on(self):
        if self.fl_pump.isEnabled():
            self.valve1.setEnabled(False)
            self.valve2.setEnabled(False)
            self.valve3.setEnabled(False)
            self.tm_pump.setEnabled(False)
            self.fl_pump.setEnabled(False)
            self.Enable.setText(
                QtGui.QApplication.translate("Form", "Turn on power", None,
                                             QtGui.QApplication.UnicodeUTF8))
        else:
            self.valve1.setEnabled(True)
            self.valve2.setEnabled(True)
            self.valve3.setEnabled(True)
            self.tm_pump.setEnabled(True)
            self.fl_pump.setEnabled(True)
            self.Enable.setText(
                QtGui.QApplication.translate("Form", "Turn off power", None,
                                             QtGui.QApplication.UnicodeUTF8))

    def Enable_on_fl(self):
        global fl_but
        if fl_but == "off":
            fl_but = "on"
            self.Timer_on()
        else:
            fl_but = "off"

    def Enable_on_v3(self):
        global v3_but
        if v3_but == "off":
            v3_but = "on"
            # open valve between chamber and pump
            self.vac_system.valve_between_chamber_and_pump = "open"
            # change the color of valve(button) if it's open
            ui.valve3.setStyleSheet("background-color: #C0C0C0")
            self.Timer_on()
        else:
            v3_but = "off"
            self.vac_system.valve_between_chamber_and_pump = "close"
            ui.valve3.setStyleSheet("background-color: #EFEFEF")
            self.Timer_on()

    def Timer_on(self):
        self.TimerUp = QtCore.QTimer()  # do not move to __init__
        if fl_but == "on" and v3_but == "on":
            self.TimerUp.start()
            self.TimerUp.setInterval(self.time_interval)
            self.TimerUp.timeout.connect(self.updateTime)
        else:
            self.TimerUp.stop()

    def updateTime(self):
        self.time += 1
        # I'm stopping here)) time.sleep is bad idea
        # fake pre pump
        while self.vac_system.chamber.air.pressure > 1000:
            self.p_cur = self.vac_system.pump.start_pump()
            self.pressure_value.setText(str(self.p_cur))
            time_test.sleep(1)
        # self.p_cur = pre_vacuum(self.time, self.p0, self.p_cur)
        self.time1.setText(str(self.time))
        # self.pressure_value.setText(str(int(round(self.p_cur * 133))))


def pre_vacuum(time, p0, p_cur):
    ppr1 = 0.01
    d_fl_pump = 0.02
    l_fl_pump = 1.5
    S_vsp = 0.005
    V = 1
    pmid = (p_cur * 133 + ppr1 * 133) / 2
    # l/d > 50
    if 0.005 / (p_cur * 133) >= d_fl_pump / 3:
        U = 12.1 * d_fl_pump ** 3 / l_fl_pump
    else:
        if 0.005 / (p_cur * 133) <= d_fl_pump / 100:
            U = (1360 * d_fl_pump ** 4 / l_fl_pump) * pmid
        else:
            U = ((12.1 * d_fl_pump ** 3 / l_fl_pump) * (
                    1 + 201 * d_fl_pump * pmid) + 2633 * (
                         d_fl_pump * pmid) * (d_fl_pump * pmid)) / (
                        1 + 236 * d_fl_pump * pmid)
    if p_cur <= 1:
        S0 = S_vsp * ((p0 - ppr1) / (1 - ppr1))
    else:
        S0 = S_vsp

    Seff = S0 * U / (S0 + U)
    return ppr1 + (p0 - ppr1) * exp(-1 * Seff / V * time)


if __name__ == "__main__":
    # create app
    app = QtGui.QApplication(sys.argv)

    # create form and init UI
    ui = MainWindow()

    # logic

    ui.Enable.clicked.connect(ui.Enable_on)
    ui.fl_pump.clicked.connect(ui.Enable_on_fl)
    ui.valve3.clicked.connect(ui.Enable_on_v3)

    # run app
    sys.exit(app.exec_())
