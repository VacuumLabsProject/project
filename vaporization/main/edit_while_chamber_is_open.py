from PyQt5 import QtWidgets
from vaporization.qt_py.dialog_chamber import Ui_Dialog


class New_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(New_Window, self).__init__()

        self.setupUi(self)

        self.show()

        self.ok_button.clicked.connect(self.close)

        self.exec_()






