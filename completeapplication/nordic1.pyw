import keyboard as k
import sys
import threading
import time as t

# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QTwidgets, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtWidgets import QApplication, QLabel,QSystemTrayIcon, QWidget, QGridLayout, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore, QtSvg
from PyQt5.QtGui import QCursor
import ctypes





def highlight(target):
    map = {1:svg_widget1,
           2:svg_widget2,
           3:svg_widget3,
           4:svg_widget4}
    
    map[target].setStyleSheet("""background-color:orange;border-radius:25px;""")
    t.sleep(1)
    map[target].setStyleSheet("""background-color:none;""")

# keyboard = Controller()
def startkeyboard():
    while True:
        event = k.read_event()
        
        if k.is_pressed('alt'):
            
            if k.is_pressed('shift'):
                if k.is_pressed('a'):
                    k.write("Ä",exact = True)
                    highlight(1)
                if k.is_pressed('o'):
                    k.write("Ö",exact = True)
                    highlight(2)
            else:
                if k.is_pressed('a'):
                    k.write("ä",exact = True)
                    highlight(3)
                if k.is_pressed('o'):
                    k.write("ö",exact = True)
                    highlight(4)
                    
            




# def buttonClicked(x):
#     x.setStyleSheet("""background-color:orange;
#                            border-radius:25px;""")
    

myappid = 'mycompany.myrulesbiiiatttch.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QApplication(sys.argv)

mainwindow = QMainWindow()

app.setWindowIcon(QtGui.QIcon('nordic1.ico'))
mainwindow.setWindowIcon(QtGui.QIcon('nordic1.ico'))

app.setWindowIcon(QtGui.QIcon('./nordic1.ico'))
# app.setWindowIcon(QtGui.QIcon('./nordic.ico'))

# trayIcon = QSystemTrayIcon(QtGui.QIcon('nordic.png'), parent = app)
# trayIcon.setToolTip("Nordic is here bebe")
# trayIcon.show()


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





# #test button

# button = QPushButton("CLICK")
# button.clicked.connect(buttonClicked())
# button.setStyleSheet("color:white")
# grid.addWidget(button, 0,0)




grid.addWidget(label1, 2,0)
grid.addWidget(label2, 2,1)
grid.addWidget(label3, 2,2)
grid.addWidget(label4, 2,3)






# two seperate threads to run gui and keylog continuously
keystrokes = threading.Thread(target=startkeyboard, daemon=True)

# gui = threading.Thread(target=startgui, daemon=True)    

keystrokes.start()
# startgui()
window.show()
sys.exit(app.exec())
