from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi('loginpage.ui', self)
        self.pushButton.clicked.connect(self.close_dialog)

    def retrieve_credentials(self):
        name = self.lineEdit.text()
        key = self.lineEdit_2.text()
        return name, key

    def close_dialog(self):
        LoginPage.done(self, 0)
