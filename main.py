from sys import argv, exit
from mainwindow import MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def main():
    application = QApplication(argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(application.exec_())

if __name__ == "__main__":
    main()
