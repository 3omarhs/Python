import os

import matplotlib.pyplot as plt
from os import walk
import shutil
import  os


dst_path = r"C:\Users\Omar Hassan\Desktop\New folder"
im_path = r'C:\Users\Omar Hassan\Desktop\New folder (5)'


mypath = src_path = im_path
# mypath = src_path = 'C:/Users/Omar Hassan/Desktop/last'
f = []
need_preproceess = []
need_preproceess_layers = []

# files = os.listdir(src_path)
photos = os.listdir(src_path)

for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    for i in filenames:
        pic = plt.imread(f'{im_path}/{i}')
        # pic = plt.imread(f'C:/Users/Omar Hassan/Desktop/last/{i}')
        if pic.shape[2] == 4:
            print(f"passed: {i}")
            1
        else:
            print(f'need to resize layers:{i}, it`s layers size is: {pic.shape[2]}')
            need_preproceess.append(i)
            need_preproceess_layers.append(pic.shape[2])
            # photoPath = f"{src_path}/{i}"
            # shutil.copy(photoPath, dst_path)
            # print(f'{i} Copied')

    break
# print(f)
print(need_preproceess)
print(need_preproceess_layers)
print(f'count of images that need preprocess: {len(need_preproceess)}')


# import cv2
#
# # for i in os.read(r'C:\Users\Omar Hassan\Desktop\New folder', 'r'):
# img = cv2.imread(r'C:\Users\Omar Hassan\PycharmProjects\opencv\output.png')
# print(img.shape)