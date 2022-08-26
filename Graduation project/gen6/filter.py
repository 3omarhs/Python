# import pygame
import cv2
from overlay_method_externalFacesRead import process_image
import os


FILTER_DIR = "data/filters1/"
# FILTER_DIR = "C:/Users/Omar Hassan/Desktop/redketchup(8)/"


def show_filter(filter_name, eyes, faces, screen):
    # FILTER_DIR = "data/filters1/"
    global FILTER_DIR

    if os.path.exists(FILTER_DIR + filter_name + ".png"):
        image = cv2.imread(FILTER_DIR + filter_name + ".png")
    else:
        if os.path.exists(FILTER_DIR + filter_name[:-1] + ".png"):
            image = cv2.imread(FILTER_DIR + filter_name[:-1] + ".png")
        else:
            if os.path.exists(FILTER_DIR + filter_name[:-2] + ".png"):
                image = cv2.imread(FILTER_DIR + filter_name[:-2] + ".png")
            else:
                if os.path.exists(FILTER_DIR + filter_name[:-3] + ".png"):
                    image = cv2.imread(FILTER_DIR + filter_name[:-3] + ".png")
                else:
                    if os.path.exists(FILTER_DIR + filter_name[:-4] + ".png"):
                        image = cv2.imread(FILTER_DIR + filter_name[:-4] + ".png")
                    else:
                        if os.path.exists(FILTER_DIR + filter_name[:-5] + ".png"):
                            image = cv2.imread(FILTER_DIR + filter_name[:-5] + ".png")
                        else:
                            if os.path.exists(FILTER_DIR + filter_name[:-6] + ".png"):
                                image = cv2.imread(FILTER_DIR + filter_name[:-6] + ".png")
                            else:
                                if os.path.exists(FILTER_DIR + filter_name[:-7] + ".png"):
                                    image = cv2.imread(FILTER_DIR + filter_name[:-7] + ".png")
                                else:
                                    if os.path.exists(FILTER_DIR + filter_name[:-8] + ".png"):
                                        image = cv2.imread(FILTER_DIR + filter_name[:-8] + ".png")
                                    else:
                                        if os.path.exists(FILTER_DIR + filter_name[:-9] + ".png"):
                                            image = cv2.imread(FILTER_DIR + filter_name[:-9] + ".png")
                                        else:
                                            print('none of above!')

    for (x, y, w, h) in faces:
        # return process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
        return process_image(image, w*1.01, h*1, x, y, screen)
        # process_image(image, w, h, x, y, screen)
        # return(process_image(frame=screen, image_path=image))
        # return(process_image(frame=screen, increase_sizex=0, increase_sizey=-0.05, move_right=-0.0, move_up=3.5, image_path=image))
