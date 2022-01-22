from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class InfoPage(QDialog):
    def __init__(self):
        super(InfoPage, self).__init__()
        loadUi('infopage.ui', self)
        self.pushButton.clicked.connect(self.close_dialog)

    def close_dialog(self):
        InfoPage.done(self, 0)
