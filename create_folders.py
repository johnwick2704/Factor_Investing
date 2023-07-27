import glob
import os

folder = glob.glob("D:/CSV/*")

for file in folder:
    path = file.split('\\')[0]
    symbol = file.split('\\')[1].split('_')[0]
    path_folder = path + '/' + symbol
    if os.path.exists(path_folder):
        print(True)
    else:
        os.mkdir(path_folder)
