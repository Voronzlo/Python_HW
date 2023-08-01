import os

full_puth = __file__ 
# c:\\Users\\Мохнатик\\Desktop\\HW_1\\HW_5\\main_1', '.py'

def info_file(full_path):
    path_file = os.getcwd()
    full_name = full_path.split("/")[-1].split(".")
    name_file, expansion_file = full_name[0], "." + full_name[1]
    info = (path_file, name_file, expansion_file)
    return info

print(info_file(full_puth))
