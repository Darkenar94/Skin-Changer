
import shutil, os

os.chdir(r"C:\Users\prais\Documents\skin")
path = r"C:\Program Files (x86)\Steam\steamui\skins\Minimal-Dark-for-Steam-root"

for file in os.listdir():
    file_name = "\\" + file
    shutil.copy(file, os.path.join(path + file_name))

