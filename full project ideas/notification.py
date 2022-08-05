import os
from win10toast import  ToastNotifier
def notification():
    os.chdir(os.path.dirname((os.path.realpath(__file__))))
    toast = ToastNotifier()
    title = "Notification"
    message = "here is 3omar.hs"
    length = 30
    toast.show_toast(title, message)
notification()