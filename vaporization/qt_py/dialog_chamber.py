# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_chamber.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(334, 180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../vaporization/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(10, 140, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.h_label = QtWidgets.QLabel(Dialog)
        self.h_label.setGeometry(QtCore.QRect(100, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.h_label.setFont(font)
        self.h_label.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.h_label.setAlignment(QtCore.Qt.AlignCenter)
        self.h_label.setObjectName("h_label")
        self.distance = QtWidgets.QDoubleSpinBox(Dialog)
        self.distance.setGeometry(QtCore.QRect(10, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.distance.setFont(font)
        self.distance.setMaximum(20.0)
        self.distance.setSingleStep(0.1)
        self.distance.setObjectName("distance")
        self.weight = QtWidgets.QDoubleSpinBox(Dialog)
        self.weight.setGeometry(QtCore.QRect(10, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.weight.setFont(font)
        self.weight.setDecimals(3)
        self.weight.setMaximum(9.999)
        self.weight.setSingleStep(0.001)
        self.weight.setObjectName("weight")
        self.m_label = QtWidgets.QLabel(Dialog)
        self.m_label.setGeometry(QtCore.QRect(100, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.m_label.setFont(font)
        self.m_label.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.m_label.setAlignment(QtCore.Qt.AlignCenter)
        self.m_label.setObjectName("m_label")
        self.radius = QtWidgets.QDoubleSpinBox(Dialog)
        self.radius.setGeometry(QtCore.QRect(10, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.radius.setFont(font)
        self.radius.setMaximum(10.0)
        self.radius.setSingleStep(0.1)
        self.radius.setObjectName("radius")
        self.r_label = QtWidgets.QLabel(Dialog)
        self.r_label.setGeometry(QtCore.QRect(100, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.r_label.setFont(font)
        self.r_label.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.r_label.setAlignment(QtCore.Qt.AlignCenter)
        self.r_label.setObjectName("r_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chamber"))
        self.comboBox.setItemText(0, _translate("Dialog", "Cu"))
        self.comboBox.setItemText(1, _translate("Dialog", "Al"))
        self.comboBox.setItemText(2, _translate("Dialog", "Cr"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.h_label.setText(_translate("Dialog", "h, cm"))
        self.m_label.setText(_translate("Dialog", "m, g"))
        self.r_label.setText(_translate("Dialog", "r, cm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())