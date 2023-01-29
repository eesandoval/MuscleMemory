import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from x11inputs import craft

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(210, 170)
        self.setWindowTitle("Muscle Memory")

        self.keyPressLabel = QLabel("Keypress", self)
        self.keyPressLabel.move(10, 15)
        self.keyPress = QLineEdit(self)
        self.keyPress.move(75, 10)

        self.macroTimeLabel = QLabel("Time", self)
        self.macroTimeLabel.move(10, 60)
        self.macroTime = QSpinBox(self)
        self.macroTime.move(75, 55)
        self.calculateTime = QPushButton("Calculate", self)
        self.calculateTime.move(120, 55)
        self.calculateTime.clicked.connect(self.calculateTimeClick)
        self.calculateTime.setEnabled(False)

        self.craftAmountLabel = QLabel("Amount", self)
        self.craftAmountLabel.move(10, 100)
        self.craftAmount = QSpinBox(self)
        self.craftAmount.move(75, 95)
        self.craftButton = QPushButton("Craft", self)
        self.craftButton.move(120, 95)
        self.craftButton.clicked.connect(self.craftButtonClick)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(10, 135, 190, 25)

    def calculateTimeClick(self):
        # TODO: Open dialog, then parse the macro and figure out how long it takes
        pass

    def craftButtonClick(self):
        craft(self.keyPress.text(), self.macroTime.value(), self.craftAmount.value(), self.progressBar)
