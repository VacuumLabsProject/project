from load_lab.qt_py.load_lab import Ui_Dialog
from PyQt5 import QtWidgets
import sys
from subprocess import call


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.show()

    def vacuum_lab_start(self):
        call(["python", "../vacuum/main/vacuum_lab.py"])

    def vaporization_lab_start(self):
        call(["python", "../vaporization/main/vaporization_lab.py"])

    def sputtering_lab_start(self):
        call(["python", "../real_sputtering/main/sputtering_lab.py"])

    def magnetron_lab_start(self):
        call(["python", "../magnetron/main/sputtering_lab.py"])

    def etching_lab_start(self):
        call(["python", "../ion_etching/main_machine/main.py"])


if __name__ == "__main__":
    # create app
    app = QtWidgets.QApplication(sys.argv)

    # create form and init UI
    ui = MainWindow()

    # logic
    ui.vacuum_l.clicked.connect(ui.vacuum_lab_start)
    ui.vaporization_l.clicked.connect(ui.vaporization_lab_start)
    ui.sputtering_l.clicked.connect(ui.sputtering_lab_start)
    ui.magnetron_l.clicked.connect(ui.magnetron_lab_start)
    ui.etching_l.clicked.connect(ui.etching_lab_start)

    # run app
    sys.exit(app.exec_())
