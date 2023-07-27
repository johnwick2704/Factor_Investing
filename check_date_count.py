import glob
import pandas as pd

folder = glob.glob("D:\CSV/combined_data/*")

for file in folder:
    csv = pd.read_csv(file)
    if csv.shape[0] > 2700:
        print(file.split('\\')[-1].split('.')[0])
        print(csv.shape)
