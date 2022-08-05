import shutil
import  os


dst_path = r"C:\Users\Omar Hassan\Desktop\Celebrities photos"

src_path = r"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled"
files = os.listdir(src_path)
for file in files:
    filePath = rf"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled\{file}"
    photos = os.listdir(filePath)

    photoPath = rf"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled\{file}\{photos[0]}"
    shutil.copy(photoPath, dst_path)
    print(f'{photos[0]} Copied')
# shutil.copy(src_path, dst_path)
# print('Copied')