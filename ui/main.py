import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from Cloud.util import initialize
from login import LoginPage
from Cloud.upload import print_containers, upload_blob


class MainPage(QDialog):

    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('mainpage.ui', self)
        block_blob_service_init = self.pushButton_7.clicked.connect(self.update_login)
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton_3.clicked.connect(self.encrypt_file)

    def update_login(self):
        connection = self.retrieveLogin()
        containers = print_containers(connection)
        for i in containers:
            self.comboBox.addItem(str(i.name))


    def retrieveLogin(self):
        login = LoginPage()
        login.exec_()
        account_name, account_key = login.retrieveCredentials()
        return initialize(account_name, account_key)

    def open_file(self):
        self.open_file_dialog()

    def open_file_dialog(self):
        file = QFileDialog.getOpenFileName()
        filename = file[0]
        self.textEdit.setText(filename)

    def encrypt_file(self):




app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())

