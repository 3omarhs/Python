import time
from pynput.mouse import Listener
import logging

def current_milli_time():
    return round(time.time()*100)


logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))
    print("moving to: (",x,",",y,") ,   ", current_milli_time())#mouse.get_position())

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        print(button, current_milli_time())

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    scroll = "null"
    if dy == 1:
        print("scroll: up", current_milli_time())
    else:
        print("scroll: down", current_milli_time())

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()



