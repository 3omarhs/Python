import os
from overlay_images import image_overlay_second_method
import cv2

FILTER_DIR = "data/filters_w/"

def show_filter(filter_name, faces, screen):
    global FILTER_DIR
    if os.path.exists(FILTER_DIR + filter_name + ".png"):
        image = FILTER_DIR + filter_name + ".png"
    else:
        if os.path.exists(FILTER_DIR + filter_name[:-1] + ".png"):
            image = FILTER_DIR + filter_name[:-1] + ".png"
        else:
            if os.path.exists(FILTER_DIR + filter_name[:-2] + ".png"):
                image = FILTER_DIR + filter_name[:-2] + ".png"
            else:
                if os.path.exists(FILTER_DIR + filter_name[:-3] + ".png"):
                    image = FILTER_DIR + filter_name[:-3] + ".png"
                else:
                    if os.path.exists(FILTER_DIR + filter_name[:-4] + ".png"):
                        image = FILTER_DIR + filter_name[:-4] + ".png"
                    else:
                        if os.path.exists(FILTER_DIR + filter_name[:-5] + ".png"):
                            image = FILTER_DIR + filter_name[:-5] + ".png"
                        else:
                            if os.path.exists(FILTER_DIR + filter_name[:-6] + ".png"):
                                image = FILTER_DIR + filter_name[:-6] + ".png"
                            else:
                                if os.path.exists(FILTER_DIR + filter_name[:-7] + ".png"):
                                    image = FILTER_DIR + filter_name[:-7] + ".png"
                                else:
                                    if os.path.exists(FILTER_DIR + filter_name[:-8] + ".png"):
                                        image = FILTER_DIR + filter_name[:-8] + ".png"
                                    else:
                                        if os.path.exists(FILTER_DIR + filter_name[:-9] + ".png"):
                                            image = FILTER_DIR + filter_name[:-9] + ".png"
                                        else:
                                            print('none of above!')

    if 'Natalie Portman' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            img2 = image_overlay_second_method(img, (int(2 * w), int(2.2 * h)), (int(x-0.55*w), int(y-0.35*h)), screen)
    elif 'Anne Hathaway' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            img2 = image_overlay_second_method(img, (int(2 * w), int(3 * h)), (int(x-0.55*w), int(y-0.35*h)), screen)
    elif 'Kate Beckinsale' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            img2 = image_overlay_second_method(img, (int(1.7 * w), int(2.2 * h)), (int(x-0.38*w), int(y-0.35*h)), screen)
    elif 'Angelina Jolie' in image or 'Lucy Liu' in image or 'Sandra Bullock' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            img2 = image_overlay_second_method(img, (int(2.5 * w), int(3 * h)), (int(x-0.55*w), int(y-0.3*h)), screen)
    else:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            img2 = image_overlay_second_method(img, (int(2.04 * w), int(3 * h)), (int(x-0.6*w), int(y-0.3*h)), screen)

    return img2
