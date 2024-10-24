import keyboard
import time 

# from datetime import datetime

log_file = 'sessionlog2.txt'
start_time = time.localtime()
formatted_time = time.strftime("%D:%B:%Y  %H:%M:%S",start_time)

def startup():
    with open(log_file, 'w') as f:
        f.write(formatted_time)
        f.write("\n\n")
    f.close()

# def on_key_press(event):
#     print("received a key press")
#     return event.name


startup()


# version using with open is more 
# efficient but wnat to try to update keylog live

# with open(log_file, 'a') as f:
#     while True:
#         event = keyboard.read_event()
#         print(event)
#         if event.name =="a":
#             print("loop broken")
#             break
#         elif event.event_type == "down":
#             print("didn't hit a key so we keep going")
#             f.write('{}, '.format(event.name))
#             f.write('{}\n'.format(event.event_type))

# hot key combo to start umlaut input
initiate_umlaut = []
key_strokes = ["alt", "Num_1", "NUM_3", "NUM_2"]

def make_umlaut():
    keyboard.press_and_release(key_strokes)
    

while True:
    event = keyboard.read_event()
    print(event)
    if event.name =="a":
        print("loop broken")
        break
    if event.name =="s":
        make_umlaut()
    elif event.event_type == "down":
        print("didn't hit a key so we keep going")
        with open(log_file, "a") as f:
            f.write('{}, '.format(event.name))
            f.write('{}\n'.format(event.event_type))
        f.close()
        





    

