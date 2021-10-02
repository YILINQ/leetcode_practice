from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Read pointer position
# Set pointer position

while True:
    mouse.position = (10, 20)
    time.sleep(5)
    # Move pointer relative to current position
    mouse.move(5000, -5)
    mouse.click(Button.left, 2)
    time.sleep(5)

    mouse.position = (100, 202)
    mouse.click(Button.left, 2)
    # Press and release
    # Double click; this is different from pressing and releasing
    # twice on Mac OSX