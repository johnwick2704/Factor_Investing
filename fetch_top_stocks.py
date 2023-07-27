import pandas
import pandas as pd
import glob
from operator import itemgetter

folder = glob.glob('D:/CSV/all_syms_data/*')
perc_change_list = []
c = 0

for year in range(2012, 2022):
    print(year)
    df = pandas.DataFrame()
    for sym_folders in folder:
        symbol = sym_folders.split('\\')[1]
        file1 = f'{symbol}_{year}_2'
        file2 = f'{symbol}_{year + 1}_1'
        data_folder = glob.glob(sym_folders + '/*')
        closing_day_1 = 0
        closing_day_2 = 0
        for file in data_folder:
            if file.find(file1) >= 0:
                csv = pd.read_csv(file)
                closing_day_1 = csv['Close'].iloc[0]
            if file.find(file2) >= 0:
                csv = pd.read_csv(file)
                closing_day_2 = csv['Close'].iloc[-1]

        if closing_day_1 == 0 or closing_day_2 == 0:
            pass
        else:
            perc_change = ((closing_day_2 - closing_day_1) / closing_day_1) * 100
            print(f'perc_change in {symbol} in {year} is ', perc_change)
            lst = [symbol, perc_change]
            perc_change_list.append(lst)

    perc_change_list.sort(key=lambda x: x[1], reverse=True)
    print(perc_change_list)
    df[f'{year}'] = perc_change_list
    df.to_csv(f'sorted_syms_{year}_{year + 1}.csv', index=False)

