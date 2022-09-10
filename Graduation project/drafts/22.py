import os
Male_list = []
def fn():       # 1.Get file names from directory
    file_list=os.listdir(r"C:\Users\Omar Hassan\PycharmProjects\Graduation project\gen8\photos\mens1")
    # file_list = os.listdir(images_path_M_single_per)
    for img_name in file_list:
        Male_list.append(img_name[:-4])
    print (Male_list)
fn()