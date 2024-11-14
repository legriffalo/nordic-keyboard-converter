import keyboard
import sys
import threading
import time as t

def send_key(event):
    if event.event_type == 'down':
        keyboard.press(event.name)
    else:
        keyboard.release(event.name)
    
    return 1

def on_key_event(event):
    global flag
    global keysDown
    global mainFlag
    global hot # hotkey combo active 
    global shiftDown
    
    check = ["alt", "caps lock"]
    print(f"start {event.name}",["shiftdown",shiftDown],["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")

    try:
        if event.name == "esc":
            print("esc pressed")
            mainFlag = False
            flag = False
            return False
        
        if set(keysDown)== {'alt', 'caps lock'}:
            hot = True
            
        #when keys are pressed
        if event.event_type == "down":
            if event.name =="shift":
                shiftDown = True
            
            #if a key is part of a hotkey combo avoid triggering key press immediately
            if event.name in check and event.name not in keysDown:
                keysDown.append(event.name)
                return 
            
            
                
                      
            #combos to give letters
            if event.name =="A" and shiftDown and hot:
                print("should print some umlaut a stuff")
                keyboard.write("Ä")
                return
            elif event.name == "O"  and shiftDown and hot:
                print("should print some umlaut o stuff") 
                keyboard.write("Ö") 
                return
            elif event.name == "a" and hot:
                print("should print some (L) umlaut a stuff")
                keyboard.write("ä")
                return
            elif event.name == "o" and hot:
                print("should print some (L) umlaut o stuff") 
                keyboard.write("ö") 
                return
                
            # other elifs in here 
            else:
                send_key(event)
                
        
        # when keys are lifted
        # suppress if hotkey was active             
        if event.event_type == "up":
            if event.name =="shift":
                shiftDown = False
                
            if event.name in check:

                if hot and keysDown:
                    print("should avoid triggering normal behaviour")
                    # print(["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")

                    keysDown.remove(event.name)
                    if len(keysDown)==0:
                        hot = False
                    print(["shiftdown",shiftDown],["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")

                    return
                
                else: 
                    keysDown.remove(event.name)

                    keyboard.press(event.name)
                    keyboard.release(event.name)
                    
                    # send_key(event)
            else:
                send_key(event)       
            
        
        
        
        
    
    
    
    except Exception as error:
        print(error)
        mainFlag = False
    print("end",["shiftdown",shiftDown],["keysdown",keysDown],["upper", upper], ["hot", hot], sep = "\n")
  
    
    
    
def start_keyboard():
    flag = True
    print("starting keyboard blocker")
    keyboard.hook(on_key_event, suppress=True)
    
    while flag:
        t.sleep(0.1)

        continue
    
    
    
keysDown = []
keysUp = []
used = False
hot = False
upper = False
shiftDown = False

# hot = False
# upper = False
    
keyStrokes = threading.Thread(target=start_keyboard, daemon=True)
keyStrokes.start()

mainFlag = True

while mainFlag:
    t.sleep(0.5)
    continue

keyStrokes.join(0)                
