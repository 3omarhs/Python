import pygame
from pygame.locals import *
from PIL import Image
from PIL import ImageTk
import tkinter

# load image in pygame
pygame.init()
surf = pygame.image.load('Omar Hassan.jpg')         # you can use any Surface a Camers is also an Surface
mode = "RGB"
# export as string / import to PIL
image_str = pygame.image.tostring(surf, mode)         # use 'RGB' to export
size      = (640, 480)
#image    = Image.fromstring(mode, size, image_str)
# use frombuffer() - fromstring() is no longer supported
image     = Image.frombuffer(mode, size, image_str, 'raw', mode, 0, 1) # use 'RGB' to import

# create Tk window/widgets
root      = tkinter.Tk()
tkimage   = ImageTk.PhotoImage(image) # use ImageTk.PhotoImage class instead
label     = tkinter.Label(root, image=tkimage)
label.pack()
root.mainloop()