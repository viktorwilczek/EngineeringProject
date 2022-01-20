import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
from Cloud.util import initialize, list_files, print_containers, delete_blob, delete_container, create_container
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
        self.pushButton_12.clicked.connect(self.delete_container)
        self.pushButton_6.clicked.connect(self.add_container)

    def update_login(self):
        self.connection = self.retrieveLogin()
        self.update_containers()
        #containers = print_containers(self.connection)
        #for i in containers:
            #self.comboBox.addItem(str(i.name))
            #self.comboBox_4.addItem(str(i.name))

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
        if self.comboBox_4.count() <= 0:
            pass
        else:
            self.update_files()

    def encrypt_file(self):
        if not (self.lineEdit.text() == self.lineEdit_2.text()):
            error = ErrorPage()
            error.exec_()
            pass
        elif not self.lineEdit.text():
            pass
        elif self.comboBox.count() <= 0:
            pass
        elif not self.textEdit.toPlainText():
            pass
        else:
            upload_blob(self.connection, self.comboBox.currentText(), self.textEdit.toPlainText(),
                        self.lineEdit.text())
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.textEdit.clear()

    def decrypt_file(self):
        if self.comboBox_4.count() <= 0:
            pass
        elif self.comboBox_3.count() <= 0:
            pass
        elif not self.lineEdit_4.text():
            pass
        else:
            download_blob(self.connection, self.comboBox_4.currentText(), self.comboBox_3.currentText(),
                          self.lineEdit_4.text())
            self.lineEdit_4.clear()

    def delete_file(self):
        if self.comboBox_3.count() <= 0:
            pass
        else:
            delete_blob(self.connection, self.comboBox_4.currentText(), self.comboBox_3.currentText())
            self.select_container()

    def delete_container(self):
        if self.comboBox_4.count() <= 0:
            pass
        else:
            delete_container(self.connection, self.comboBox_4.currentText())
            self.update_containers()
            self.update_files()

    def add_container(self):
        if not self.textEdit_2.toPlainText():
            print("empty")
            pass
        elif self.connection == "empty":
            pass
        else:
            print("create container "+ str(self.textEdit_2.toPlainText))
            create_container(self.connection, self.textEdit_2.toPlainText())
            self.update_containers()
            self.textEdit_2.clear()

    def update_containers(self):
        containers = print_containers(self.connection)
        self.comboBox.clear()
        self.comboBox_4.clear()
        for i in containers:
            self.comboBox.addItem(str(i.name))
            self.comboBox_4.addItem(str(i.name))

    def update_files(self):
        container = self.comboBox_4.currentText()
        files = list_files(container, self.connection)
        self.comboBox_3.clear()
        for i in files:
            self.comboBox_3.addItem(str(i.name))

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())

