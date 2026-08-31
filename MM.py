import keyboard
import time
import random
from threading import Thread
import win32api
import win32con

is_active = True
current_mode = "-"


def press_r_multiple_times():
    if not is_active:
        return
    

    r1 = random.uniform(0.015, 0.002)
    delay = random.uniform(r1, 0.05)
    time.sleep(0.02)

    ## press_count = random.randint(1, 3)

    for _ in range(1):
        vk = 0x52
        win32api.keybd_event(vk, 0, 0, 0)
        time.sleep(random.uniform(0.01, 0.05))
        win32api.keybd_event(vk, 0, win32con.KEYEVENTF_KEYUP, 0)


        time.sleep(random.uniform(0.04, 0.1))


def on_key_press(key):
    global is_active, current_mode

    if key.name == '=':
        is_active = not is_active
        return

    if key.name == '-':
        current_mode = "-"
        return

    if current_mode == "-" and key.name == '1' and is_active:
        t = Thread(target=press_r_multiple_times)
        t.start()


keyboard.on_press(on_key_press)

try:
    keyboard.wait()
except KeyboardInterrupt:
    pass