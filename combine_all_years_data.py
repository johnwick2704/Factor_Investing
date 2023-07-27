import glob
import pandas as pd

data_folder = glob.glob("D:\CSV/all_syms_data/*")

for symbol_folder in data_folder:
    symbol_files = glob.glob(symbol_folder + "/*")
    df = pd.DataFrame()
    symbol = symbol_files[0].split("\\")[2]
    print(symbol)
    for file in symbol_files:
        csv = pd.read_csv(file)
        df = df.append(csv)
    df.to_csv(f"D:\CSV/combined_data/{symbol}.csv", index=False)
