import pygame
# from overlay_method import process_image

FILTER_DIR = "data/filters_w/"


def show_filter(filter_name, eyes, faces, screen):
    global FILTER_DIR
    # FILTER_DIR = "data/filters_w/"
    try: image = pygame.image.load(FILTER_DIR + filter_name + ".png")
    except:
        try:image = pygame.image.load(FILTER_DIR + filter_name[:-9] + ".png")
        except:
            try:image = pygame.image.load(FILTER_DIR + filter_name[:-8] + ".png")
            except:
                try:image = pygame.image.load(FILTER_DIR + filter_name[:-7] + ".png")
                except:
                    try:image = pygame.image.load(FILTER_DIR + filter_name[:-6] + ".png")
                    except:
                        try:image = pygame.image.load(FILTER_DIR + filter_name[:-5] + ".png")
                        except:
                            try:image = pygame.image.load(FILTER_DIR + filter_name[:-4] + ".png")
                            except:
                                try:image = pygame.image.load(FILTER_DIR + filter_name[:-3] + ".png")
                                except:
                                    try:
                                        image = pygame.image.load(FILTER_DIR + filter_name[:-2] + ".png")
                                    except:
                                        try:
                                            image = pygame.image.load(FILTER_DIR + filter_name[:-1] + ".png")
                                        except:
                                            print('none of above!')
    # image = pygame.image.load(fr"C:\Users\Omar Hassan\PycharmProjects\ML_my_proj\Snapchat-Filters-master\data\filters\{filter_name}.png")
    print(f'Accepted: {image}')



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


def process_image(image, resize_x, resize_y, scale_x, scale_y, screen):
    image = pygame.transform.scale(image, (int(resize_x), int(resize_y)))
    screen.blit(image, (640 - int(scale_x), int(scale_y)))
