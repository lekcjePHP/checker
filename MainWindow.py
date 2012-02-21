# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Feb 21 15:24:50 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(375, 444)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 341, 391))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEditLogin = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditLogin.setObjectName(_fromUtf8("lineEditLogin"))
        self.verticalLayout.addWidget(self.lineEditLogin)
        self.labelLogin = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelLogin.setObjectName(_fromUtf8("labelLogin"))
        self.verticalLayout.addWidget(self.labelLogin)
        self.lineEditPassword = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.labelPassword = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.verticalLayout.addWidget(self.labelPassword)
        self.lineEditDestinationEmail = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditDestinationEmail.setObjectName(_fromUtf8("lineEditDestinationEmail"))
        self.verticalLayout.addWidget(self.lineEditDestinationEmail)
        self.labelEmail = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelEmail.setObjectName(_fromUtf8("labelEmail"))
        self.verticalLayout.addWidget(self.labelEmail)
        self.lineEditAddressil = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditAddressil.setObjectName(_fromUtf8("lineEditAddressil"))
        self.verticalLayout.addWidget(self.lineEditAddressil)
        self.labelAdres = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelAdres.setObjectName(_fromUtf8("labelAdres"))
        self.verticalLayout.addWidget(self.labelAdres)
        self.lineEditSearch = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditSearch.setObjectName(_fromUtf8("lineEditSearch"))
        self.verticalLayout.addWidget(self.lineEditSearch)
        self.labelSearch = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelSearch.setObjectName(_fromUtf8("labelSearch"))
        self.verticalLayout.addWidget(self.labelSearch)
        self.pushButtonStart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.verticalLayout.addWidget(self.pushButtonStart)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLogin.setText(QtGui.QApplication.translate("MainWindow", "Login Gmail", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPassword.setText(QtGui.QApplication.translate("MainWindow", "Haslo gmail", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEmail.setText(QtGui.QApplication.translate("MainWindow", "destination email", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAdres.setText(QtGui.QApplication.translate("MainWindow", "adrs monitorowanej strony", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSearch.setText(QtGui.QApplication.translate("MainWindow", "Szukane slowo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))

