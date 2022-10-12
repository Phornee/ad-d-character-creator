import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QWidget
)
from PyQt5.uic import loadUi
from character_creator import create_char

from gui.stat_widget import Ui_stat

class StatWidget(QWidget, Ui_stat):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        # self.action_Exit.triggered.connect(self.close)
        # self.action_Find_Replace.triggered.connect(self.findAndReplace)
        # self.action_About.triggered.connect(self.about)
        # self.create.clicked.connect(self.createClick)
        pass

    def set_name(self, name):
        self.name.setText(name)

    def set_value(self, value):
        self.value.setText(str(value))

