# import shutil
import os

# dst_path = r"C:\Users\Omar Hassan\Desktop\New folder"
artistname = 'Nancy Ajram'
# try:
with open(f'C:/Users/Omar Hassan/Desktop/{artistname}.zpl', 'w', encoding="utf-8") as f:
    # f.write('Create a new text file!')
    f.write(f"<?zpl version='2.0' encoding='utf-8'?><smil><head><title>{artistname}</title></head><body><seq>")
    src_path = rf"D:\backup\myMusic\{artistname}"
    files = os.listdir(src_path)
    # for file in files:
    #     filePath = rf"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled\{file}"
    #     musics = os.listdir(filePath)
    for musicname in files:
        # musicPath = rf"C:\Users\Omar Hassan\PycharmProjects\jupyter\face3\lfw_funneled\{file}\{musicname}.mp3"
        # musicPath = f"\n<media src=\"{src_path}\{musicname}\" />"
        try:
            f.write(f"\n<media src=\"{src_path}\{musicname}\" />")
            # f.write(f"\n<media src=\"{src_path}\\")
            # f.write(musicname)
            # f.write('\" />')
        except: pass
        # shutil.copy(photoPath, dst_path)
        print(f'{musicname} Copied')
    f.write("\n</seq> </body> </smil>")
# except FileNotFoundError:
#     print("The 'docs' directory does not exist")
# shutil.copy(src_path, dst_path)
# print('Copied')

# <?zpl version='2.0' encoding='utf-8'?><smil><head><title>Elisa</title></head>     <body><seq>     <media src="D:\backup\myMusic\Elissa\Download unavailable (1).mp3" />       </seq></body>        </smil>
