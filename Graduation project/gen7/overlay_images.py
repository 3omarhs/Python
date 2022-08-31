import numpy as np
import cv2
from time import time

def image_overlay_second_method(img2, dim, location, img01):
    # print(img2.shape)
    img2 = cv2.resize(img2, dim)
    # print(img2.shape)
    x, y = location
    w, h = dim
    # print(f'h={h}, w={w}')

    img1 = img01[y:y + h, x:x + w]
    # print(x)
    # print(img1.shape)
    # print(img01[y:y + h, x:x + w].shape)
    # print(img2.shape)

    img1 = cv2.resize(img1, (w, h), interpolation = cv2.INTER_CUBIC)
    result = np.zeros((h, w, 3), np.uint8)

    #slow
    st = time()
    for i in range(h):
        for j in range(w):
                color1 = img1[i, j]
                color2 = img2[i, j]
                alpha = color2[3] / 255.0
                new_color = [ (1 - alpha) * color1[0] + alpha * color2[0],
                              (1 - alpha) * color1[1] + alpha * color2[1],
                              (1 - alpha) * color1[2] + alpha * color2[2] ]
                result[i, j] = new_color
    end = time() - st
    # print(f'end: {end}')

    #fast
    st = time()
    alpha = img2[:, :, 3] / 255.0
    result[:, :, 0] = (1. - alpha) * img1[:, :, 0] + alpha * img2[:, :, 0]
    result[:, :, 1] = (1. - alpha) * img1[:, :, 1] + alpha * img2[:, :, 1]
    result[:, :, 2] = (1. - alpha) * img1[:, :, 2] + alpha * img2[:, :, 2]
    end = time() - st
    # print(end)
    # print(f'end: {end}')
    img01[y:y + h, x:x + w]=result
    return img01






# background = cv2.imread("photos/BG.jpg", -1)
# haircut = cv2.imread('data/filters_m/bill gates.png', -1)
# size = (250, 250)
# img = image_overlay_second_method(haircut, (200, 200), (200, 200), background)
# cv2.imshow("result", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()