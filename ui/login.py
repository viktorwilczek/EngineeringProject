import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi('loginpage.ui', self)
        self.pushButton.clicked.connect(self.retrieveCredentials)
        self.pushButton_2.clicked.connect(self.closeDialog)

    def retrieveCredentials(self):
        name = self.lineEdit.text()
        key = self.lineEdit_2.text()
        return name, key

    def closeDialog(self):
        LoginPage.done(self, 0)
