import glob
import pandas as pd

folder = glob.glob('CSV_files/*')
folder.sort()
for file in folder:
    csv = pd.read_csv(file)
    print(file)
    year = int(file.split('\\')[-1].split('.')[0])
    print(year)
    for index, rows in csv.iterrows():
        if year == 2018 and rows['Symbol'] in ['VAKRANGEE']:
            print('here ', rows['Symbol'], index)
            csv = csv.drop(csv.index[index])

    csv.to_csv(file, index=False)

