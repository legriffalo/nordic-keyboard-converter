
# pyautogui.FAILSAFE = False
#function to bring window to foreground
# import pygetwindow as gw

# Find a window by title
# def bring_window_to_foreground(title):
#     windows = gw.getWindowsWithTitle(title)  # Replace with your target window's title

#     if windows:
#         window = windows[0]
#         window.activate()  # Brings the window to the front
#         window.restore()   # Restores the window if it's minimized
#     else:
#         print("Window not found!")
    
# def bring_window_to_foreground(window_title):
#     # mouse out of where ever it is allows nordic to move order
#     original_position = pyautogui.position()
#     pywinauto.mouse.move(coords=(-10000, 500))
#     # pyautogui.moveTo(-10000, 500)    
#     # Find the window by title
#     hwnd = win32gui.FindWindow(None, window_title)
#     print(hwnd)
    
#     if hwnd:
#         print("moving to foreground")
#         # Bring the window to the front
#         win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore the window if minimized
#         win32gui.SetForegroundWindow(hwnd)  
#         # Bring the window to the foreground
#     else:
#         print(f"Window with title '{window_title}' not found!")

#     #after window is moved replace mouse
#     pywinauto.mouse.move(coords=(original_position[0], original_position[1])  ) 

#     # #click may be needed ot get back in to app
#     pyautogui.click()