import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize, Qt 

class WarningWindow(QMainWindow):
    def __init__(self, error = "Some error"):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(400, 200))    
        self.setWindowTitle("Warning") 

        alert = QLabel(error, self)
        alert.setAlignment(Qt.AlignCenter)
        alert.setStyleSheet("QLabel { background-color : red; color : blue;}")
        alert.resize(400,200)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = WarningWindow()
    
    sys.exit( app.exec_() )