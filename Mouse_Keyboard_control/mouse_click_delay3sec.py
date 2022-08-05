import time
import mouse
import pyautogui


x = mouse.get_position()
print(x)
while True:
    mouse.click('left')
    x = mouse.get_position()
    print(x)
    time.sleep(3)