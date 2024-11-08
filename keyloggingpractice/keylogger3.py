import keyboard as k
# from pynput.keyboard import Key, Controller

# keyboard = Controller()

while True:
    event = k.read_event()
    print(event)
    if event.name =="esc":
        print("loop broken")
        break

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
                