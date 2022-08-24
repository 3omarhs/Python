import cv2
from overlay_method import process_image
import os


FILTER_DIR = "data/filters_w/"
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
    print(f'Accepted: {image}')


    # for (x, y, w, h) in faces:
    #     # process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    #     # process_image(image, w, h, x, y, screen)
    #     return(process_image(frame=screen, image_path=image))



    if 'Natalie Portman' in filter_name:
        for (x, y, w, h) in faces:
            process_image(image, 2.5*w, 3*h, x+1.8*w, y-0.55*h, screen)
    elif 'Anne Hathaway' in filter_name:
        for (x, y, w, h) in faces:
            process_image(image, 2*w, 3*h, x+1.6*w, y-0.35*h, screen)
    elif 'Kate Beckinsale' in filter_name:
        for (x, y, w, h) in faces:
            process_image(image, 1.7*w, 1.8*h, x+1.36*w, y-0.35*h, screen)
    elif 'Angelina Jolie' in filter_name or 'Lucy Liu' in filter_name or 'Sandra Bullock' in filter_name:
        for (x, y, w, h) in faces:
            process_image(image, 2.5*w, 3*h, x+1.55*w, y-0.3*h, screen)
    else:
        for (x, y, w, h) in faces:
            process_image(image, 2.5*w, 3*h, x+1.8*w, y-0.4*h, screen)
