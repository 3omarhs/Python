import pygame

FILTER_DIR = "data/filters/"


def show_filter(filter_name, eyes, faces, screen):
    FILTER_DIR = "data/filters/"
    image = pygame.image.load(FILTER_DIR + filter_name + ".png")
    # image = pygame.image.load(fr"C:\Users\Omar Hassan\PycharmProjects\ML_my_proj\Snapchat-Filters-master\data\filters\{filter_name}.png")

    if "hair1" in filter_name:
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
        # if len(eyes) != 2:
        #     return
        # (x, y, min_w, min_h, max_w, max_h) = get_boundaries(eyes)
        # process_image(image, 1.3*max_w, 1.2*min_h, x+1.18*max_w, y-0.1*max_h, screen)
    elif filter_name == "hair2":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair3":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair4":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair5":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair6":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair7":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair8":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair9":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)

    elif filter_name == "hair10":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair11":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair12":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair13":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair14":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair15":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair16":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair17":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair18":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair19":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair20":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair21":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair22":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair23":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair24":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair25":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair26":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair27":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair28":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair29":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair30":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair31":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair32":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair33":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair34":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair35":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair36":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair37":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair38":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair39":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair40":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair41":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair42":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair43":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair44":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair45":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair46":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair47":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair48":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair49":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair50":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair51":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair52":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair53":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair54":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair55":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair56":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair57":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair58":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair59":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair60":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair61":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair62":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair63":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair64":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair65":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair66":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair67":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair68":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair69":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair70":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair71":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair72":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair73":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair74":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair75":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair76":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair77":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair78":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair79":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair80":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair81":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair82":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair83":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair84":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair85":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair86":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair87":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair88":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair89":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair90":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair91":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair92":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair93":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair94":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair95":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair96":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair97":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair98":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair99":

        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair100":
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    elif filter_name == "hair101":
        
        for (x, y, w, h) in faces:
            process_image(image, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)


def show_gif():
    pass


def show_filter_package(package_name, eyes, faces, screen):
   1


def process_image(image, resize_x, resize_y, scale_x, scale_y, screen):
    image = pygame.transform.scale(image, (int(resize_x), int(resize_y)))
    screen.blit(image, (640 - int(scale_x), int(scale_y)))


def get_boundaries(rects):
    if rects[0][0] > rects[1][0]:
        ((rx, ry, rw, rh), (lx, ly, lw, lh)) = rects
    else:
        ((lx, ly, lw, lh), (rx, ry, rw, rh)) = rects

    x = lx
    y = ly
    min_w = lw
    min_h = lh
    max_w = rx + rw - lx
    max_h = ly + lh - ry if ly + lh - ry > lh else ry + rh - ly

    return x, y, min_w, min_h, max_w, max_h
