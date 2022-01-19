import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from Cloud.util import initialize, list_files, print_containers, delete_blob
from login import LoginPage
from error import ErrorPage
from Cloud.upload import upload_blob
from Cloud.download import download_blob


class MainPage(QDialog):

    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('mainpage.ui', self)
        self.connection = "empty"
        self.pushButton_7.clicked.connect(self.update_login)
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton_11.clicked.connect(self.select_container)
        self.pushButton_3.clicked.connect(self.encrypt_file)
        self.pushButton_4.clicked.connect(self.decrypt_file)
        self.pushButton_10.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.delete_file)

    def update_login(self):
        self.connection = self.retrieveLogin()
        containers = print_containers(self.connection)
        for i in containers:
            self.comboBox.addItem(str(i.name))
            self.comboBox_4.addItem(str(i.name))

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

    def select_container(self):
        container = self.comboBox_4.currentText()
        files = list_files(container, self.connection)
        self.comboBox_3.clear()
        for i in files:
            self.comboBox_3.addItem(str(i.name))

    def encrypt_file(self):
        #if [x for x in (self.comboBox.currentText(), self.textEdit.toPlainText(), self.lineEdit.text(), )
                #if x is None]:
        if not (self.lineEdit.text() == self.lineEdit_2.text()):
            error = ErrorPage()
            error.exec_()
            pass
        elif not self.lineEdit.text():
            pass
        elif self.comboBox.count() <= 0:
            pass
        elif not self.textEdit.toPlainText:
            pass
        else:
            upload_blob(self.connection, self.comboBox.currentText(), self.textEdit.toPlainText(),
                        self.lineEdit.text())
            self.lineEdit.clear()
            self.lineEdit_2.clear()

    def decrypt_file(self):
        download_blob(self.connection, self.comboBox_4.currentText(), self.comboBox_3.currentText(),
                      self.lineEdit_4.text())
        self.lineEdit_4.clear()

    def delete_file(self):
        delete_blob(self.connection, self.comboBox_4.currentText(), self.comboBox_3.currentText())
        self.select_container()

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())

