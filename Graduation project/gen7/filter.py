import pygame
import os

FILTER_DIR = "data/filters_m/"
# FILTER_DIR = "C:/Users/Omar Hassan/Desktop/redketchup(8)/"


def show_filter(filter_name, eyes, faces, screen):
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


    # image = pygame.image.load(fr"C:\Users\Omar Hassan\PycharmProjects\ML_my_proj\Snapchat-Filters-master\data\filters_m\{filter_name}.png")
    # image = r"C:\Users\Omar Hassan\Desktop\New folder\Ashton Kutcher.png"
    if 'Britton Buchanan' in image or 'david beckham' in image or 'harry styles' in image or 'Hugh Jackman' in image or 'Jake Gyllenhaal' in image or 'Mark Wahlberg' in image or 'Nick Jonas' in image or 'simon cowell' in image or 'Zayn Malik' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.8*w, 1*h, x+0.9*w, y-0.4*h, screen)
    elif 'Ryan Reynolds' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.84*w, 0.8*h, x+0.92*w, y-0.32*h, screen)
    elif 'Clay Aiken' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.85*w, 0.9*h, x+0.915*w, y-0.29*h, screen)
    elif 'Adam Levine' in image or 'Bill_Simon' in image or 'Cam Gigandet' in image or 'James Franco' in image or 'Jose_Maria_Aznar' in image or 'Ricky Martin' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.85*w, 1*h, x+0.92*w, y-0.4*h, screen)
    elif 'Finneas O' in image or 'John Viener' in image or 'John_Bolton' in image or 'Louis Tomlinson' in image or 'Paul Walker' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.93*w, 1*h, x+0.95*w, y-0.4*h, screen)
    elif 'Dev Patel' in image or 'johnny depp' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 1.3*w, 1.25*h, x+1.2*w, y-0.55*h, screen)
    elif 'donald trump' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.9*w, 1*h, x+1*w, y-0.4*h, screen)
    elif 'justin timberlake' in image or 'matt damon' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.90*w, 1*h, x+0.97*w, y-0.4*h, screen)
    elif 'prince harry' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.90*w, 1*h, x+0.94*w, y-0.4*h, screen)
    elif 'richard hammond' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 1.05*w, 1*h, x+1.05*w, y-0.4*h, screen)
    elif 'Robert Pattinson' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 1.15*w, 1*h, x+1.1*w, y-0.4*h, screen)
    elif 'james may' in image:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 1.5*w, 2*h, x+1.27*w, y-0.85*h, screen)
    # elif 'Ryan Reynolds' in image:
    #     img = pygame.image.load(image)
    #     for (x, y, w, h) in faces:
    #         process_image(img, 0.8*w, 0.85*h, x+0.9*w, y-0.4*h, screen)
    else:
        img = pygame.image.load(image)
        for (x, y, w, h) in faces:
            process_image(img, 0.9*w, 1*h, x+0.95*w, y-0.4*h, screen)


def process_image(image, resize_x, resize_y, scale_x, scale_y, screen):
    image = pygame.transform.scale(image, (int(resize_x), int(resize_y)))
    screen.blit(image, (640 - int(scale_x), int(scale_y)))
