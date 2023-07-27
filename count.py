import pandas as pd
import glob

folder = glob.glob("CSV_files/*")
comp = []

for file in folder:
    csv = pd.read_csv(file)
    print(csv)
    for index, row in csv.iterrows():
        if row['Symbol'] not in comp:
            comp.append(row['Symbol'])

print(comp)
print(len(comp))