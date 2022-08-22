import pygame

FILTER_DIR = "data/filters1/"




def show_filter(filter_name, eyes, faces, screen):
    FILTER_DIR = "data/filters1/"
    try: image = pygame.image.load(FILTER_DIR + filter_name + ".png")
    except:
        try:image = pygame.image.load(FILTER_DIR + filter_name[:-1] + ".png")
        except:
            try:image = pygame.image.load(FILTER_DIR + filter_name[:-2] + ".png")
            except:
                try:image = pygame.image.load(FILTER_DIR + filter_name[:-3] + ".png")
                except:
                    try:image = pygame.image.load(FILTER_DIR + filter_name[:-4] + ".png")
                    except:
                        try:image = pygame.image.load(FILTER_DIR + filter_name[:-5] + ".png")
                        except:
                            try:image = pygame.image.load(FILTER_DIR + filter_name[:-6] + ".png")
                            except:
                                try:image = pygame.image.load(FILTER_DIR + filter_name[:-7] + ".png")
                                except:
                                    try:
                                        image = pygame.image.load(FILTER_DIR + filter_name[:-8] + ".png")
                                    except:
                                        try:
                                            image = pygame.image.load(FILTER_DIR + filter_name[:-9] + ".png")
                                        except:
                                            print('none of above!')
    # image = pygame.image.load(fr"C:\Users\Omar Hassan\PycharmProjects\ML_my_proj\Snapchat-Filters-master\data\filters\{filter_name}.png")

    for (x, y, w, h) in faces:
        process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)



def process_image(image, resize_x, resize_y, scale_x, scale_y, screen):
    image = pygame.transform.scale(image, (int(resize_x), int(resize_y)))
    screen.blit(image, (640 - int(scale_x), int(scale_y)))
