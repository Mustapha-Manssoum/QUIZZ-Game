
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from mainwindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()


    sys.exit(app.exec_())