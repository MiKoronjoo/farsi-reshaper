# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.12.1

import reshaper
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 306)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainText.setGeometry(QtCore.QRect(13, 90, 661, 171))
        self.plainText.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plainText.setAutoFillBackground(False)
        self.plainText.setPlainText("")
        self.plainText.setBackgroundVisible(True)
        self.plainText.setCenterOnScroll(False)
        self.plainText.setObjectName("plainText")
        self.reshapeBt = QtWidgets.QPushButton(self.centralwidget)
        self.reshapeBt.setGeometry(QtCore.QRect(20, 40, 171, 41))
        self.reshapeBt.setObjectName("reshapeBt")
        self.clearBt = QtWidgets.QPushButton(self.centralwidget)
        self.clearBt.setGeometry(QtCore.QRect(20, 10, 81, 25))
        self.clearBt.setObjectName("clearBt")
        self.undoBt = QtWidgets.QPushButton(self.centralwidget)
        self.undoBt.setGeometry(QtCore.QRect(110, 10, 81, 25))
        self.undoBt.setObjectName("undoBt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 46, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.reshapeBt.clicked.connect(on_reshape)
        self.plainText.textChanged.connect(self.label.clear)
        self.clearBt.clicked.connect(on_clear)
        self.undoBt.clicked.connect(on_undo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", reshaper.__title__))
        self.reshapeBt.setText(_translate("MainWindow", "Reshape and Copy"))
        self.clearBt.setText(_translate("MainWindow", "Clear"))
        self.undoBt.setText(_translate("MainWindow", "Undo"))
        self.undoBt.setEnabled(False)


def on_reshape():
    reshaper.reshape(ui.plainText.toPlainText())
    ui.label.setText('Done!')


def on_clear():
    global last_text
    last_text = ui.plainText.toPlainText()
    ui.plainText.clear()
    ui.undoBt.setEnabled(True)


def on_undo():
    ui.plainText.setPlainText(last_text)
    ui.undoBt.setEnabled(False)


if __name__ == "__main__":
    import sys

    last_text = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
