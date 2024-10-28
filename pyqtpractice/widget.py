import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

# from PyQt5 import QtWidgets, QtGui


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Nordic Keyboard Converter")
window.setFixedWidth(300)
window.setStyleSheet("")
window.setWindowIcon(QtGui.QIcon('nordic.png'))

window.show()
sys.exit(app.exec())