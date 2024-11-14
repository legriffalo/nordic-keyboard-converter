import keyboard
import sys
import threading


def on_key_event(event):
    global flag
    print(event.name)
    if event.name == 'z':
        print("supressing z")

        return
    
    print("sent event through", event.name)

    # for the keys we don't want to suppress, we just send the events back out
    if event.event_type == 'down':
        keyboard.press(event.name)
    else:
        keyboard.release(event.name)
    
    
    if event.name == 'esc':
        print("terminating loop")
        keyboard.unhook(on_key_event)
        flag = False

            
flag = True     
keyboard.hook(on_key_event, suppress=True)

while flag:
    continue

# import keyboard

# def on_key_event(e):
#     print(f"Key {e.name} was {e.event_type}")

# # Set a global hook to listen for all key events
# keyboard.hook(on_key_event)

# # Keep the program running and listen for the "esc" key to exit
# keyboard.wait("esc")