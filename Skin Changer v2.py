
import shutil, time, os

def save_paths(skin_path, documents, config_path):
    config_file = open(config_path, "a")
    config_file.write(skin_path + "\n")
    config_file.write(documents)

def read_paths(config_path):
    config_file = open(config_path, "r")
    paths = config_file.read().split("\n")
    return paths[0], paths[1]

def first_path_check(drives, skin_path):
    for drive in drives:
        new_skin_path = drive + skin_path
        if os.path.exists(new_skin_path):
            return new_skin_path
    return "None"

def select_path(dictionary):
    dict_keys = list(dictionary)
    if dictionary[skin_path]:
        return dict_keys[1], "skin"
    return dict_keys[0], "doc"

def add_text(wrong_path):
    if wrong_path[1] == "doc":
        print(" put the skin folder in the documents folder. !read the guide! ")

def get_path(wrong_path):
    running = True
    while running:
        if not os.path.exists(wrong_path[0]):
            print("\n Oops! I can't find the path to your skin :D")
            add_text(wrong_path)
            path = input("\n  Enter the path manually pls: ")
            if os.path.exists(path):
                print("\n Skin path found! ^_^")
                running = False
    return path

def second_path_check(dictionary):
    selected_path = select_path(dictionary)
    return get_path(selected_path)

def kill_steam():
    try:
        os.system("taskkill /f /im Steam.exe")
    except:
        pass

user_folder = os.path.expanduser('~')
config_path = os.path.join(user_folder, r"Documents\config.txt") 
documents = os.path.join(user_folder, r"Documents\skin")
alter_skin_path = r":\Steam\steamui\skins\Minimal-Dark-for-Steam-root"
skin_path = r":\Program Files (x86)" + alter_skin_path[1:]
drives = list("abcdefghijlmnopqrstuvwxyz".upper())

if not os.path.exists(config_path):
    if not os.path.exists(skin_path):
        skin_path = first_path_check(drives, skin_path)
    if not os.path.exists(skin_path):
        skin_path = first_path_check(drives, alter_skin_path)
    if not os.path.exists(skin_path):
        skin_path = second_path_check({documents:False, skin_path:True})
    if not os.path.exists(documents):
        documents = second_path_check({documents:True, skin_path:False})
    save_paths(skin_path, documents, config_path)
else:
    skin_path, documents = read_paths(config_path)

kill_steam()
os.chdir(documents)

for file in os.listdir():
    file_name = "\\" + file
    shutil.copy(file, os.path.join(skin_path + file_name))

print("\n DONE. SKIN UPDATED, HAVE A NICE DAY!!")
time.sleep(5)
