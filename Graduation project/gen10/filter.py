import os
from overlay_images import image_overlay_second_method
import cv2

FILTER_DIR = "data/filters_m/"
# FILTER_DIR = "C:/Users/Omar Hassan/Desktop/redketchup(8)/"


def show_filter(filter_name, faces, screen):
    # FILTER_DIR = "data/filters1/"
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


    if 'Britton Buchanan' in image or 'david beckham' in image or 'harry styles' in image or 'Hugh Jackman' in image or 'Jake Gyllenhaal' in image or 'Nick Jonas' in image or 'Zayn Malik' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.8*w), int(1*h)), (int(x+0.1*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'Ryan Reynolds' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.84*w), int(0.8*h)), (int(x+0.1*w), int(y-0.32*h)), screen)
            except:
                1
    elif 'simon cowell' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.9*w), int(1*h)), (int(x+0.1*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'Clay Aiken' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.85*w), int(0.9*h)), (int(x+0.1*w), int(y-0.29*h)), screen)
            except:
                1
    elif 'Adam Levine' in image or 'Bill_Simon' in image or 'Cam Gigandet' in image or 'James Franco' in image or 'Jose_Maria_Aznar' in image or 'Ricky Martin' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.85*w), int(1*h)), (int(x+0.1*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'Finneas O' in image or 'John Viener' in image or 'John_Bolton' in image or 'Louis Tomlinson' in image or 'Paul Walker' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.93*w), int(1*h)), (int(x+0.05*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'Dev Patel' in image or 'johnny depp' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(1.3*w), int(1.25*h)), (int(x-0.2*w), int(y-0.55*h)), screen)
            except:
                1

    elif 'donald trump' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.9*w), int(1*h)), (int(x+0*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'justin timberlake' in image or 'matt damon' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.90*w), int(1*h)), (int(x+0.1*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'prince harry' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.90*w), int(1*h)), (int(x+0.1*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'richard hammond' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(1.05*w), int(1*h)), (int(x-0.05*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'Robert Pattinson' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(1.15*w), int(1*h)), (int(x-0.1*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'james may' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(1.7*w), int(2.2*h)), (int(x-0.35*w), int(y-0.85*h)), screen)
            except:
                1
    elif 'george clooney' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.97*w), int(1*h)), (int(x+0.035*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'Mark Wahlberg' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.9*w), int(1*h)), (int(x+0.05*w), int(y-0.4*h)), screen)
            except:
                1
    elif 'Troye Sivan' in image:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.95*w), int(1*h)), (int(x+0.04*w), int(y-0.4*h)), screen)
            except:
                1
    else:
        img = cv2.imread(image, -1)
        for (x, y, w, h) in faces:
            try:
                img2 = image_overlay_second_method(img, (int(0.95*w), int(1*h)), (int(x+0.045*w), int(y-0.4*h)), screen)
            except:
                1

    return img2

# def process_image(image, resize_x, resize_y, scale_x, scale_y, screen):
#     image = pygame.transform.scale(image, (int(resize_x), int(resize_y)))
#     screen.blit(image, (640 - int(scale_x), int(scale_y)))
