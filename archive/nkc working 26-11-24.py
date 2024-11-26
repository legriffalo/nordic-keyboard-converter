# import all packages
import sys
import os
import threading
import keyboard
import pyperclip
import time as t
import ctypes
# import win32gui
# import win32con
# import pywinauto
# import pyautogui
from PyQt5.QtWidgets import QApplication, QLabel, QSystemTrayIcon, QWidget, QGridLayout
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtGui, QtCore

## resource path function taken from 
#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    print(os.path.join(base_path, relative_path))
    return os.path.join(base_path, relative_path)


# class to customise svg behaviour
class InteractiveSvgWidget(QSvgWidget):
    def __init__(self, svg_file, parent=None, char = None):
        self.char = char

        super().__init__(svg_file, parent)
        # Enable mouse tracking for hover events
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("copied to clipboard")
            pyperclip.copy(self.char)
            self.highlight()
        super().mousePressEvent(event)
        
    def highlight(self):
        # Apply the red background
        self.setStyleSheet("""
            background-color: red;
            border-radius: 25px;
        """)
        
        # Create a single-shot timer to revert the style after 1 second
        QTimer.singleShot(1000, lambda: self.setStyleSheet("""
            background-color: transparent;
            border-radius: 25px;
        """))
        
        # self.unhighlight()
    
    # def unhighlight(self):
    #     t.sleep(1)
    #     print ("1s delay???")
    #     self.setStyleSheet("""
    #             background-color: transparent;
    #             border-radius: 25px;
    #         """)
        



    
# def send_key(event):
#     if event.event_type == 'down':
#         keyboard.press(event.name)
#     else:
#         keyboard.release(event.name)
    
#     return 1

#attempt by amazon Q
# def on_key_event(event):
#     global keysDown
#     global hot
#     global shiftDown
#     global gettable
#     global highlightTarget
    
#     check = ["alt", "caps lock"]
    
#     try:
#         # Only handle specific hotkey combinations, let others pass through
#         if set(keysDown) == {'alt', 'caps lock'}:
#             hot = True
            
#         if event.event_type == "down":
#             if event.name == "shift":
#                 shiftDown = True
            
#             # Only block keys that are part of our hotkey combo
#             if event.name in check and event.name not in keysDown:
#                 keysDown.append(event.name)
#                 return True
            
#             # Handle our specific combinations
#             if hot:
#                 if event.name == "A" and shiftDown:
#                     keyboard.write("Ä")
#                     highlightTarget = gettable[0]
#                     return False
#                 elif event.name == "O" and shiftDown:
#                     keyboard.write("Ö")
#                     highlightTarget = gettable[1]
#                     return False
#                 elif event.name == "a":
#                     keyboard.write("ä")
#                     highlightTarget = gettable[2]
#                     return False
#                 elif event.name == "o":
#                     keyboard.write("ö")
#                     highlightTarget = gettable[3]
#                     return False
            
#             # Let other combinations pass through
#             return True
            
#         if event.event_type == "up":
#             if event.name == "shift":
#                 shiftDown = False
                
#             if event.name in check:
#                 if hot and keysDown:
#                     keysDown.remove(event.name)
#                     if len(keysDown) == 0:
#                         hot = False
#                     return True
#                 else:
#                     keysDown.remove(event.name)
#                     return True
            
#             return True

#     except Exception as error:
#         print(error)
#         return True

#     return True




def on_key_event(event):
    # global flag
    global keysDown
    # global mainFlag
    global hot # hotkey combo active 
    global shiftDown
    global gettable
    global highlightTarget

    
    check = ["alt", "caps lock"]
    print(f"start {event.name}",["shiftdown",shiftDown],["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")

    try:
        # kill key for testing 
        # if event.name == "esc":
        #     print("esc pressed")
        #     # mainFlag = False
        #     # flag = False
        #     keyboard.unhook_all()
        #     return False
        
        if set(keysDown)== {'alt', 'caps lock'}:
            hot = True
            
        #when keys are pressed
        if event.event_type == "down":
            if event.name =="shift":
                shiftDown = True
            
            #if a key is part of a hotkey combo avoid triggering key press immediately
            if event.name in check and event.name not in keysDown:
                keysDown.append(event.name)
                return False
                       
            #combos to give letters
            if event.name =="A" and shiftDown and hot:
                print("should print some umlaut a stuff")
                keyboard.write("Ä")
                highlightTarget = gettable[0]

                return
            elif event.name == "O"  and shiftDown and hot:
                print("should print some umlaut o stuff") 
                keyboard.write("Ö") 
                highlightTarget = gettable[1]
                return
            elif event.name == "a" and hot:
                print("should print some (L) umlaut a stuff")
                keyboard.write("ä")
                highlightTarget = gettable[2]

                return
            elif event.name == "o" and hot:
                print("should print some (L) umlaut o stuff") 
                keyboard.write("ö") 
                highlightTarget = gettable[3]

                return False
                
            # other elifs in here 
            else:
                return True
                # send_key(event)
                
        
        # when keys are lifted
        # suppress if hotkey was active             
        if event.event_type == "up":
            if event.name =="shift":
                shiftDown = False
                
            if event.name in check:

                if hot and len(keysDown) > 0:
                    print("should avoid triggering normal behaviour")
                    # print(["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")

                    keysDown.remove(event.name)
                    if len(keysDown)==0:
                        hot = False
                    print(["shiftdown",shiftDown],["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")

                    return False
                
                else: 
                    keysDown.remove(event.name)
                    return True
                    # keyboard.press(event.name)
                    # keyboard.release(event.name)
                    
                    # send_key(event)
            return True      

    except Exception as error:
        print(error)
        return False
    print("end",["shiftdown",shiftDown],["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")


# Function for initialising keyboard ( will be thread 1)
def start_keyboard():
    # flag = True
    # print("starting keyboard blocker")
    keyboard.hook(on_key_event, suppress=True)
    
    # while flag:
    #     t.sleep(0.1)

    #     continue
    # keyboard.unhook_all()


# function for listening for style changes (will be thread 2)
def highlight_listener():
    while True:
        global highlightTarget
        if highlightTarget !='':
            make_highlight(highlightTarget)
            highlightTarget = ''
        t.sleep(0.2)
    return "style change process terminated"  
        
# funciton to make style changes 
def make_highlight(target):
    global window
    
    target.setStyleSheet("""background-color:orange;border-radius:25px;""")
           
    t.sleep(1)
    target.setStyleSheet("""background-color:none;""")
    
    return "highlighted"

    

   
# function to build widget
def build_widget(assetsFolderPath):
    app = QApplication(sys.argv)
    # mainwindow = QMainWindow()

    app.setWindowIcon(QtGui.QIcon(resource_path(f'{assetsFolderPath}\\nordic.ico')))
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
    window.setWindowTitle("NKC")
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
    svg_widget1 = InteractiveSvgWidget(resource_path(f'{assetsFolderPath}\\A.svg'), char = "Ä")
    svg_widget2 = InteractiveSvgWidget(resource_path(f'{assetsFolderPath}\\O.svg'), char = "Ö")
    svg_widget3 = InteractiveSvgWidget(resource_path(f'{assetsFolderPath}\\aa.svg'),char = "ä")
    svg_widget4 = InteractiveSvgWidget(resource_path(f'{assetsFolderPath}\\oo.svg'), char = "ö")
    

    svg_widget1.setStyleSheet("""border-radius:25px;""")


    

    # label with key commands
    label1 = QLabel("alt,caps,shift + a")
    label2 = QLabel("alt,caps,shift + a")
    label3 = QLabel("alt,caps + a")
    label4 = QLabel("alt,caps + o")
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
    
    gettable = [svg_widget1, svg_widget2, svg_widget3, svg_widget4]
    

    return app,window, gettable



# Make sure app ctype is set
myappid = 'nordic.keyboard.converter.version1.1' # arbitrary version string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#start build GUI
app,window,gettable = build_widget('assets')


# set global variables for interthread comms #
    # Will be set to name of svgs to highlight key in use
highlightTarget = ''


keysDown = []
keysUp = []
used = False
hot = False
upper = False
shiftDown = False
mainFlag = True

# hot = False
# upper = False
    

# start threads 
keyStrokes = threading.Thread(target=start_keyboard, daemon=True)
styleChanges = threading.Thread(target=highlight_listener, daemon=True)    

keyStrokes.start()
styleChanges.start()


window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)  

# show GUI window
window.show()
# execute event loop of app as interpretter closes
sys.exit(app.exec())