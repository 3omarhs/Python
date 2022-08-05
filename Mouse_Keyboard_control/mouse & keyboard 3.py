from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import time

pr = ""
pr_copied = ""





def current_milli_time():
    return round(time.time()*100)



def on_press(key):
    # pr = "Key pressed: {0}".format(key), "     ", current_milli_time()
    pr = '{0}'.format(key)
    try:
        prr = int(pr[1:-1])
        if prr >= 96 and prr <= 105:
            pr = prr - 96
        if prr == 110:
            pr = '.'
    except ValueError:
        gotdata = 'null'
    print(pr)


def on_release(key):
    pr = '{0}'.format(key)
    try:
        prr = int(pr[1:-1])
        if prr >= 96 and prr <= 105:
            pr = "error"
        if prr == 110:
            pr = 'error'
    except ValueError:
        gotdata = 'null'
    # pr = "Key released: {0}".format(key), "     ", current_milli_time()
    if pr != "error":
        print(pr)

def on_move(x, y):
    # pr = "Mouse moved to ({0}, {1})".format(x, y), "     ", current_milli_time()
    pr = '{0}, {1}'.format(x, y)
    print(pr)


def on_click(x, y, button, pressed):
    if pressed:
        first_time = current_milli_time()
        # pr = 'Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button), "     ", first_time
        pr = '{0}, {1}'.format(x, y, button)
        file1 = open("../Draft/test.txt", "a")
        open("../Draft/test.txt", "w").close()
        file1.write(str(first_time))
        print(pr)
    else:
        second_time = current_milli_time()
        #pr = 'Mouse released at ({0}, {1}) with {2}'.format(x, y, button), "     ", second_time
        pr = '{0}, {1}'.format(x, y, button)
        print(pr)
        #print(f"pressed for:{(second_time - first_time)}")
        with open('../Draft/test.txt') as f:
            lines = str(f.readlines())
            print(f"pressed for:{(second_time - int(lines[2:-2]))/100} second")

def on_scroll(x, y, dx, dy):
    # pr = 'Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy), "     ", current_milli_time()
    pr = '{3}'.format(x, y, dx, dy)
    print(pr)


# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
