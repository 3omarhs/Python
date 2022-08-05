import shutil
import  os


dst_path = r"C:\Users\Omar Hassan\Desktop\New folder"

src_path = r"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled"
files = os.listdir(src_path)
for file in files:
    filePath = rf"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled\{file}"
    photos = os.listdir(filePath)
    for photo in photos:
        photoPath = rf"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled\{file}\{photo}"
        shutil.copy(photoPath, dst_path)
        print(f'{photo} Copied')
# shutil.copy(src_path, dst_path)
# print('Copied')