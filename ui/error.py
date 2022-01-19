import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class ErrorPage(QDialog):
    def __init__(self):
        super(ErrorPage, self).__init__()
        loadUi('errorpage.ui', self)
        self.pushButton.clicked.connect(self.close_dialog)

    def close_dialog(self):
        ErrorPage.done(self, 0)
