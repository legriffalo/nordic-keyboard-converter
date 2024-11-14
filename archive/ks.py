import keyboard
import sys
import threading
import time as t

def on_key_event(event):
    global flag
    global keysDown
    global main_flag
    global used
    global hot
    global upper
    
    check = ["alt", "left windows", "shift"]
    # mods = ["a"]
    
    
    try:
        print(event.name)
                
        if event.name == 'esc':
            print("terminating loop")
            keyboard.unhook(on_key_event)
            flag = False
            main_flag = False

        if event.event_type =="down":
            
            if set(keysDown) == ("alt", "left windows", "shift"):
                # print(set(keysDown))
                # print("wow its uppered")
                upper = True
                hot = True
                
            if set(keysDown) == {'alt', 'left windows'}:
                # print(set(keysDown))
                # print("hot key armed")
                upper = False
                hot = True
                
            else:
                upper = False
                hot = False
        


        print ("hot", hot, "upper", upper)

        # deal with modifier keys we want to be hotkeys
        if event.name in check:
            # if upper:
            #     return 
            # if hot and event.name != "shift":
            #     return
            # check keys held down
            if event.event_type == "down" and event.name not in keysDown and event.name in check:
                keysDown.append(event.name)                
                # if correct combos flag htkey armed
                if "alt" in keysDown and "shift" in keysDown and "shift" in keysDown:
                    hot = True
                    upper = True 
                    
                elif "alt" in keysDown and "shift" in keysDown:
                    hot = True  
                return
            
            # check when hotkeys get raised
            if event.event_type == "up" and hot and keysDown: 
                  
                ## remove form keys down
                keysDown.remove(event.name)
                return

            # makes sure keypress signal is sent off

            else:
                ## remove form keys down
                keysDown.remove(event.name)
                #send normal response
                keyboard.press(event.name)
                keyboard.release(event.name)
                # print("from key by key reducer")
                # print(keysDown)
                # print ("hot", hot, "upper", upper)
                # keysDown.remove(event.name)
                return
                
        
        
        elif event.name == "a" and event.event_type == "down":
            if upper:
                print("umcaps A should print")
                keyboard.write("Ä")
                used = True
                return
            elif hot:
                print("lower um a")
                keyboard.write("ä",exact = True)
                used = True

                return
            else:
                print("just an a")
                keyboard.press(event.name)
                        
        # # if hotkey active and using a modable key       
        # if event.name in mods and hot:
        #     if event.event_type == "down":
        #         if upper and event.name =="a":
        #             keyboard.write("Ä",exact = True)
        #         else:
        #             keyboard.write("ä",exact = True)
        #         return
        #     else:
        #         print("key up")
                
        else:  
        # for the keys we don't want to suppress, we just send the events back out
            if event.event_type == 'down':
                keyboard.press(event.name)
            else:
                keyboard.release(event.name)
    
        print(set(keysDown))
        print("used", used)
        print("hot", hot, "upper", upper)


        

            
    except Exception as error:
        print(error)
        main_flag = False



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

# hot = False
# upper = False
    
keyStrokes = threading.Thread(target=start_keyboard, daemon=True)
keyStrokes.start()

main_flag = True

while main_flag:
    t.sleep(0.5)
    continue

keyStrokes.join(0)
# def on_key_event(e):
#     print(f"Key {e.name} was {e.event_type}")

# # Set a global hook to listen for all key events
# keyboard.hook(on_key_event)

# # Keep the program running and listen for the "esc" key to exit
# keyboard.wait("esc")