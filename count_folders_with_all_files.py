import glob
import os

folder = glob.glob("D:/CSV/*")
all_dates = []

for symbols in folder:
    files = glob.glob(f"{symbols}/*.csv")

    if len(files) == 22:
        all_dates.append(symbols.split('\\')[1])

print(all_dates)
print(len(all_dates))
