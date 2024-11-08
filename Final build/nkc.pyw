# import all packages
import keyboard as k
import sys
import threading
import time as t
import ctypes
#import pyperclip
from PyQt5.QtWidgets import QApplication, QLabel, QSystemTrayIcon, QWidget, QGridLayout, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore, QtSvg



# Function for initialising keyboard ( will be thread 1)
def start_keyboard():
    while True:
        event = k.read_event()
        
        if k.is_pressed('alt'):
            
            if k.is_pressed('shift'):
                if k.is_pressed('a'):
                    k.write("Ä",exact = True)
                if k.is_pressed('o'):
                    k.write("Ö",exact = True)
            else:
                if k.is_pressed('a'):
                    k.write("ä",exact = True)
                if k.is_pressed('o'):
                    k.write("ö",exact = True)



# function for listening for style changes (will be thread 2)
def highlight_listener():
    while True:
        if highlightTarget:
            make_highlight(highlightTarget)
            highlightTarget = ''
        t.sleep(0.5)
    return "style change process terminated"  
        
# funciton to make style changes 
def make_highlight(target):
    target.setStyleSheet("""background-color:orange;border-radius:25px;""")
    t.sleep(1)
    target.setStyleSheet("""background-color:none;""")
    return "highlighted"

    

   
# function to build widget
def build_widget(assetsFolderPath):
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()

    app.setWindowIcon(QtGui.QIcon(f'{assetsFolderPath}/nordic.ico'))
    # mainwindow.setWindowIcon(QtGui.QIcon('nordic1.ico'))
    
#could be useful to transition to tray application

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
    
    # values to put window in bottom right of primary display
    xDisplacement = rect.width()-500
    yDisplacement = rect.height()-250
    
    #create a widget called window in which to build GUI
    window = QWidget()
    window.setWindowTitle("Nordic Keyboard Converter")
    window.setFixedWidth(500)
    window.setFixedHeight(200)
    window.setStyleSheet("background:black;")

    grid = QGridLayout()
    window.setLayout(grid)

    window.move(xDisplacement,yDisplacement)
# not sure if needed so deactivated for now
    # # display logo in  
    # image = QPixmap("nordic.png")
    # image = image.scaledToWidth(50)
    # logo = QLabel()
    # logo.setPixmap(image)
    # grid.addWidget(logo, 0, 4)

    # display svgs
    svg_widget1 = QtSvg.QSvgWidget(f'{assetsFolderPath}/umlaut caps A.svg')
    svg_widget2 = QtSvg.QSvgWidget(f'{assetsFolderPath}/umlaut caps O.svg')
    svg_widget3 = QtSvg.QSvgWidget(f'{assetsFolderPath}/umlaut lower a.svg')
    svg_widget4 = QtSvg.QSvgWidget(f'{assetsFolderPath}/umlaut lower o.svg')
    svg_widget1.setStyleSheet("""border-radius:25px;""")


    

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


    grid.addWidget(label1, 2,0)
    grid.addWidget(label2, 2,1)
    grid.addWidget(label3, 2,2)
    grid.addWidget(label4, 2,3)
    grid.addWidget(svg_widget1, 1,0)
    grid.addWidget(svg_widget2, 1,1)
    grid.addWidget(svg_widget3, 1,2)
    grid.addWidget(svg_widget4, 1,3)

    return app,window



# Make sure app ctype is set
myappid = 'nordic.keyboard.converter.version1.1' # arbitrary version string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# set global variables for interthread comms #
    # Will be set to name of svgs to highlight key in use
highlightTarget = ''

    # Requested will allow buttons in app window to contact keyboard
requested = 'ä'

# start threads 
keyStrokes = threading.Thread(target=start_keyboard, daemon=True)
styleChanges = threading.Thread(target=highlight_listener, daemon=True)    

keyStrokes.start()
styleChanges.start()

#start build GUI
app,window = build_widget('./assets')

# show GUI window
window.show()
# execute event loop of app as interpretter closes
sys.exit(app.exec())