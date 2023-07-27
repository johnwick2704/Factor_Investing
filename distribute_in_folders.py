import glob
import os
import shutil

folder = glob.glob("D:/CSV/*.csv")

for file in folder:
    path = file.split('\\')[0]
    symbol = file.split('\\')[1].split('_')[0]
    path_folder = path + '/' + symbol
    if os.path.exists(path_folder):
        pass
    else:
        os.mkdir(path_folder)
    print(file)
    print(path_folder)
    shutil.move(file, path_folder)


