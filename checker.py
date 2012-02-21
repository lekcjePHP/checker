import sys
from PyQt4 import QtCore, QtGui
from MainWindow import Ui_MainWindow
from backend import *


class notifyerForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
      QtGui.QWidget.__init__(self,parent)
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      QtCore.QObject.connect(self.ui.pushButtonStart, QtCore.SIGNAL("clicked()"), self.startuj)        


    def startuj(self):   
        pageAddress = self.ui.lineEditAddressil.text
        destinEmail = self.ui.lineEditDestinationEmail.text
        passwordEmail = self.ui.lineEditPassword.text
        loginEmail = self.lineEditPassword.text
        message = pageAddress+" zmienila sie tresc! Pzdr"

        watcher(pageAddress, destinEmail, message, loginEmail, passwordEmail )
        sys.exit() 


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = notifyerForm()
    myapp.show()
    sys.exit(app.exec())
    