from PyQt5 import QtWidgets, QtCore
from diploma import Ui_Form
import sys
import vacuum_system
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

fl_but = "off"
tm_but = "off"
enable = "off"
overflow = "off"
ready = "red"


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel('t, с')
        self.axes.set_ylabel('P, Па')
        self.axes.yaxis.set_label_position('right')
        super(PlotCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.current_time = 0
        self.P = [100000]
        self.time_massive = [0]
        self.t = 0
        self.time = 0
        self.time02 = 0
        self.time03 = 0
        self.time_interval = 10
        self.p0 = 100000
        self.p02 = 133
        self.p_cur = self.p0

        self.setupUi(self)

        self.canvas = PlotCanvas(self)
        self.canvas.axes.semilogy(self.time_massive, self.P)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.graphicsView.setLayout(layout)

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
            self.Enable.setEnabled(False)
        else:
            fl_but = "off"
            self.status.setText("Disabled forevacuum pump")
            self.valve3.setEnabled(False)
            self.valve2.setEnabled(False)
            self.overflow.setEnabled(True)
            self.Enable.setEnabled(True)

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
            self.Timer_common_func()
        else:
            self.vac_system.valve1.state = "close"
            self.status.setText("Enabled high vacuum pump")
            self.Timer_common_func()

    def Enable_valve_2(self):
        if self.vac_system.valve2.state == "close" and self.p_cur > 133:
            self.vac_system.valve2.state = "open"
            self.valve3.setEnabled(False)
            self.Timer_common_func()

        elif self.vac_system.valve2.state == "close" and self.p_cur < 133:
            self.vac_system.valve2.state = "open"
            self.valve3.setEnabled(False)
            self.tm_pump.setEnabled(True)
            self.Timer_common_func()

        else:
            self.vac_system.valve2.state = "close"
            self.valve3.setEnabled(True)
            self.tm_pump.setEnabled(False)
            self.Timer_common_func()

    def Enable_valve_3(self):
        global v3_but
        if self.vac_system.valve3.state == "close":
            self.vac_system.valve3.state = "open"
            self.valve2.setEnabled(False)
            self.Timer_common_func()

        else:
            self.vac_system.valve3.state = "close"
            self.valve2.setEnabled(True)
            self.Timer_common_func()

    def Enable_overflow(self):
        global overflow
        if overflow == "on":
            overflow = "off"
            self.p0 = self.p_cur
            self.fl_pump.setEnabled(True)
            self.Enable.setEnabled(True)
            self.Timer_common_func()
        else:
            overflow = "on"
            self.fl_pump.setEnabled(False)
            self.Enable.setEnabled(False)
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
            self.t = random.randint(720, 900)
            self.status.setText("Running-up high vacuum pump")
            self.p02 = self.p_cur
            self.Timer_common.setInterval(
                self.time_interval * self.timeSlider.value())
            self.Timer_common.timeout.connect(self.count_time)

        elif tm_but == "off" and self.t == 0 and self.valve1.isEnabled():
            self.valve2.setEnabled(False)
            self.valve1.setEnabled(False)
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
        self.time_massive.append(self.current_time + self.time)
        # print self.P

        self.update_canvas()

        self.pressure_value.setText(str(round(self.p_cur, 2)))
        if self.p_cur > 133:
            self.progressBar.setValue(int(self.p_cur))
        else:
            self.progressBar_2.setValue(int(self.p_cur))
        self.time_label1.setText(str(self.time))

    def turbomolecular(self):
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
        self.time_massive.append(self.current_time + self.time + self.time02)
        # print self.P
        self.update_canvas()

        self.pressure_value.setText(str(round(self.p_cur, 5)))
        self.progressBar_2.setValue(int(self.p_cur))
        self.time_label2.setText(str(self.time02))

    def updateOverflow(self):
        self.time03 += 1
        self.p_cur = self.vac_system.pump.overflow(self.time03, self.p_cur)
        self.P.append(self.p_cur)
        self.time_massive.append(self.current_time + self.time + self.time02 + self.time03)
        self.p02 = 133

        self.update_canvas()

        self.progressBar_2.setValue(133)
        self.progressBar.setValue(int(self.p_cur))
        self.pressure_value.setText(str(round(self.p_cur, 0)))
        if int(self.p_cur) == self.p0:
            self.Timer_common.stop()
            self.current_time = self.current_time + self.time + self.time02 + self.time03
            self.time_label1.setText(str(0))
            self.time_label2.setText(str(0))
            self.time = 0
            self.time02 = 0
            self.time03 = 0

    def update_canvas(self):
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.semilogy(self.time_massive, self.P)
        self.canvas.axes.set_xlabel('t, с')
        self.canvas.axes.set_ylabel('P, Па')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


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

    # run app
    sys.exit(app.exec_())