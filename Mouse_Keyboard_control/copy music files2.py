# import shutil
import os

# dst_path = r"C:\Users\Omar Hassan\Desktop\New folder"
artistname = 'Nancy Ajram'
with open(f'C:/Users/Omar Hassan/Desktop/{artistname}.txt', 'w', encoding="utf-8") as f:
    files = os.listdir(rf"D:\backup\myMusic\{artistname}")
    for musicname in files:
        try:1
        except: pass
        f.write(musicname)
        print(f'{musicname} Copied')

# <?zpl version='2.0' encoding='utf-8'?><smil><head><title>Elisa</title></head>     <body><seq>     <media src="D:\backup\myMusic\Elissa\Download unavailable (1).mp3" />       </seq></body>        </smil>
