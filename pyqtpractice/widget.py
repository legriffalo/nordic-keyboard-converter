import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore, QtSvg
from PyQt5.QtGui import QCursor

widgets = {
    "logo":[],
    "indicator":[]
}



def buttonClicked(x):
    x.setStyleSheet("""background-color:orange;
                           border-radius:25px;""")
    

app = QApplication(sys.argv)


# check monitor size to place window in bottom right 
screen = app.primaryScreen()
print('Screen: %s' % screen.name())
size = screen.size()
print('Size: %d x %d' % (size.width(), size.height()))
rect = screen.availableGeometry()
print('Available: %d x %d' % (rect.width(), rect.height()))

xDisplacement = rect.width()-500
yDisplacement = rect.height()-250

window = QWidget()
window.setWindowTitle("Nordic Keyboard Converter")
window.setFixedWidth(500)
window.setFixedHeight(200)

window.setStyleSheet("background:black;")
window.setWindowIcon(QtGui.QIcon('nordic.png'))
grid = QGridLayout()
window.setLayout(grid)

window.move(xDisplacement,yDisplacement)


# display logo 

image = QPixmap("nordic.png")
image = image.scaledToWidth(50)
logo = QLabel()
logo.setPixmap(image)
grid.addWidget(logo, 0, 4)

# display svgs
svg_widget1 = QtSvg.QSvgWidget("../General assets/umlaut caps A.svg")
svg_widget2 = QtSvg.QSvgWidget("../General assets/umlaut caps O.svg")
svg_widget3 = QtSvg.QSvgWidget("../General assets/umlaut lower a.svg")
svg_widget4 = QtSvg.QSvgWidget("../General assets/umlaut lower o.svg")
svg_widget1.setStyleSheet("""border-radius:25px;""")


grid.addWidget(svg_widget1, 1,0)
grid.addWidget(svg_widget2, 1,1)
grid.addWidget(svg_widget3, 1,2)
grid.addWidget(svg_widget4, 1,3)

# label with key commands
label1 = QLabel("alt+shft+A")
label2 = QLabel("alt+shft+O")
label3 = QLabel("alt+A")
label4 = QLabel("alt+O")

label1.setAlignment(QtCore.Qt.AlignCenter)
label2.setAlignment(QtCore.Qt.AlignCenter)
label3.setAlignment(QtCore.Qt.AlignCenter)
label4.setAlignment(QtCore.Qt.AlignCenter)

label1.setStyleSheet("""color:white;""")
label2.setStyleSheet("""color:white;""")
label3.setStyleSheet("""color:white;""")
label4.setStyleSheet("""color:white;""")





#test button

button = QPushButton("CLICK")
button.clicked.connect(buttonClicked())
button.setStyleSheet("color:white")
grid.addWidget(button, 0,0)




grid.addWidget(label1, 2,0)
grid.addWidget(label2, 2,1)
grid.addWidget(label3, 2,2)
grid.addWidget(label4, 2,3)




window.show()
sys.exit(app.exec())