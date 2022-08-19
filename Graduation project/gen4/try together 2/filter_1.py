import pygame
import cv2
import numpy as np


# FILTER_DIR = "data/filters1/"
FILTER_DIR = "C:/Users/Omar Hassan/PycharmProjects/Graduation project/gen4/try together 2/data/filters1/"


def show_filter(filter_name, video_capture, faces, screen):
    # FILTER_DIR = "data/filters1/"
    FILTER_DIR = "C:/Users/Omar Hassan/PycharmProjects/Graduation project/gen4/try together 2/data/filters1/"

    # except:
    #     try:image = pygame.image.load(FILTER_DIR + filter_name[:-1] + ".png")
    #     except:
    #         try:image = pygame.image.load(FILTER_DIR + filter_name[:-2] + ".png")
    #         except:
    #             try:image = pygame.image.load(FILTER_DIR + filter_name[:-3] + ".png")
    #             except:
    #                 try:image = pygame.image.load(FILTER_DIR + filter_name[:-4] + ".png")
    #                 except:
    #                     try:image = pygame.image.load(FILTER_DIR + filter_name[:-5] + ".png")
    #                     except:
    #                         try:image = pygame.image.load(FILTER_DIR + filter_name[:-6] + ".png")
    #                         except:
    #                             try:image = pygame.image.load(FILTER_DIR + filter_name[:-7] + ".png")
    #                             except:
    #                                 try:
    #                                     image = pygame.image.load(FILTER_DIR + filter_name[:-8] + ".png")
    #                                 except:
    #                                     try:
    #                                         image = pygame.image.load(FILTER_DIR + filter_name[:-9] + ".png")
    #                                     except:
    #                                         print('none of above!')try: image = pygame.image.load(FILTER_DIR + filter_name + ".png")

    # try:
    #     image = cv2.imread(FILTER_DIR + filter_name[:-9] + ".png")
    #     cv2.imread(FILTER_DIR + filter_name[:-9] + ".png")
    # except:
    try:
        image = cv2.imread(FILTER_DIR + filter_name[:-8] + ".png")
        cv2.imread(FILTER_DIR + filter_name[:-8] + ".png")
    except:
        try:
            image = cv2.imread(FILTER_DIR + filter_name[:-7] + ".png")
            cv2.imread(FILTER_DIR + filter_name[:-7] + ".png")
        except:
            try:
                image = cv2.imread(FILTER_DIR + filter_name[:-6] + ".png")
                cv2.imread(FILTER_DIR + filter_name[:-6] + ".png")
            except:
                try:
                    image = cv2.imread(FILTER_DIR + filter_name[:-5] + ".png")
                    cv2.imread(FILTER_DIR + filter_name[:-5] + ".png")
                except:
                    try:
                        image = cv2.imread(FILTER_DIR + filter_name[:-4] + ".png")
                        cv2.imread(FILTER_DIR + filter_name[:-4] + ".png")
                    except:
                        try:
                            image = cv2.imread(FILTER_DIR + filter_name[:-3] + ".png")
                            cv2.imread(FILTER_DIR + filter_name[:-3] + ".png")
                        except:
                            try:
                                image = cv2.imread(FILTER_DIR + filter_name[:-2] + ".png")
                                cv2.imread(FILTER_DIR + filter_name[:-2] + ".png")
                            except:
                                try:
                                    image = cv2.imread(FILTER_DIR + filter_name[:-1] + ".png")
                                    cv2.imread(FILTER_DIR + filter_name[:-1] + ".png")
                                except:
                                    try:
                                        image = cv2.imread(FILTER_DIR + filter_name + ".png")
                                        cv2.imread(FILTER_DIR + filter_name + ".png")
                                    except:
                                        print('none of above!')
    # image = pygame.image.load(fr"C:\Users\Omar Hassan\PycharmProjects\ML_my_proj\Snapchat-Filters-master\data\filters\{filter_name}.png")

    for (x, y, w, h) in faces:
        frame = process_image(image, video_capture, 1.0*w, 1.2*h, x+1.0*w, y-0.4*h, screen)
    return frame



def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    try:
        imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
    except:
        imgRGBA = cv2.bitwise_and(imgFront, maskBGR)
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)
    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv
    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)
    return imgBack


def show_gif():
    pass


def show_filter_package(package_name, faces, screen):
   1


def process_image(image, video_capture, resize_x, resize_y, scale_x, scale_y, screen):
    # image = pygame.transform.scale(image, (int(resize_x), int(resize_y)))
    dim = (int(resize_x), int(resize_y))
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    overlayPNG(screen, image)

    size = 100
    logo = cv2.resize(image, (size, size))
    # Create a mask of logo
    img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    # Region of Interest (ROI), where we want
    # to insert logo
    roi = video_capture[-size - 10:-10, -size - 10:-10]
    # Set an index of where the mask is
    roi[np.where(mask)] = 0
    roi += logo



    # return frame
    # pos = [0, 0]
    # hf, wf, cf = image.shape
    # hb, wb, cb = screen.shape
    # *_, mask = cv2.split(image)
    # maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    # maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # # try:
    # # imgRGBA = cv2.bitwise_and(image, maskBGRA
    # imgRGBA = cv2.bitwise_and(image, maskBGR)
    # # except:
    # #     imgRGBA = cv2.bitwise_and(image, maskBGR)
    # imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)
    # imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    # imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    # imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    # maskBGRInv = cv2.bitwise_not(maskBGR)
    # imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv
    # screen = cv2.bitwise_and(screen, imgMaskFull2)
    # screen = cv2.bitwise_or(screen, imgMaskFull)
    # # screen.blit(image, (640 - int(scale_x), int(scale_y)))


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
