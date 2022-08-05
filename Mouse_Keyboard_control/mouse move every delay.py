import mouse
import pyautogui
import time

while(True):
    # pyautogui.moveTo(50, 50)
    mouse.move(150, 150, absolute=False, duration=2)
    x = mouse.get_position()
    print(x)
    time.sleep(1800)

    mouse.move(-150, -150, absolute=False, duration=2)
    x = mouse.get_position()
    print(x)
    time.sleep(1800)