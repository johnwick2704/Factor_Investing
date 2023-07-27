import pandas as pd
import glob
import os
from datetime import datetime


def get_top_20_symbols(symbol_list, year, start_date, end_date):
    max_gains_list = []
    for symbol in symbol_list:
        path = f"D:\CSV/combined_data/{symbol}.csv"
        isdir = os.path.isfile(path)
        if not isdir:
            continue
        data_file = pd.read_csv(path)

        start_price, end_price = 0, 0

        for row in data_file.itertuples():
            date = int(datetime.fromtimestamp(row.Timestamp).strftime('%y%m%d').replace('-', ''))
            # print(date)
            if start_date > date > end_date:
                continue
            if start_price == 0 and date >= start_date:
                start_price = row.Close
            if end_price == 0 and date >= end_date:
                end_price = row.Close
            if start_price != 0 and end_price != 0:
                break
        if start_price != 0 and end_price != 0:
            diff_perc = ((end_price - start_price) / start_price) * 100
            temp = [symbol, diff_perc]
            max_gains_list.append(temp)
        else:
            print(f"Symbol data not available for {year}")

    max_gains_list.sort(key=lambda x: x[1], reverse=True)
    top_20_stocks = max_gains_list[:20]
    return top_20_stocks


def get_pnl_of_top_20_syms(data_list, start_date, end_date):
    total_pnl = 0
    syms_list, perc_list = map(list, zip(*data_list))
    only_sym_list = []
    all_sym_pnl_list = []
    dt_lst = []

    for symbol in syms_list:
        only_sym_list.append(symbol)
        path = f"D:\CSV/combined_data/{symbol}.csv"
        isdir = os.path.isfile(path)
        if not isdir:
            continue
        data_file = pd.read_csv(path)
        start_price, end_price = 0, 0
        sym_daily_pnl = []
        dt_lst = []

        for row in data_file.itertuples():
            date = int(datetime.fromtimestamp(row.Timestamp).strftime('%y%m%d').replace('-', ''))
            if start_date > date > end_date:
                continue
            if start_price == 0 and date >= start_date:
                start_price = row.Close
                dt_lst = []
            if end_price == 0 and date >= end_date:
                end_price = row.Close
            if start_price > 0 and end_price == 0:
                sym_daily_pnl.append(((row.Close - start_price) / start_price) * 100)
                dt_lst.append(datetime.fromtimestamp(row.Timestamp))
            if start_price > 0 and end_price > 0:
                sym_daily_pnl.append(((row.Close - start_price) / start_price) * 100)
                dt_lst.append(datetime.fromtimestamp(row.Timestamp))
            if start_price != 0 and end_price != 0:
                break
        if start_price != 0 and end_price != 0:
            diff_perc = ((end_price - start_price) / start_price) * 100
            total_pnl = total_pnl + diff_perc
            all_sym_pnl_list.append(sym_daily_pnl)
            # daily_dt_list.append(dt_lst)
            # print(symbol, diff_perc)
        else:
            print(f"Symbol data not available for {year}")
        # print(symbol, len(sym_daily_pnl), len(dt_lst))

    all_list = [sum(i) for i in zip(*all_sym_pnl_list)]

    return total_pnl, only_sym_list, all_list, dt_lst


nifty_500_folder = glob.glob("CSV_files/*")
total_pnl_so_far = 0
symbol_set = set()
profit_per_year = []
daily_pnl_list = []
daily_dt_list_fin = []

for file in nifty_500_folder:
    nifty_500_file = pd.read_csv(file)
    year = file.split('\\')[1].split('.')[0]
    print(year)
    prev_year = str(int(year) - 1)
    symbol_list = nifty_500_file['Symbol']

    lookback_start_date1 = int(prev_year[2:] + "0101")
    lookback_end_date1 = int(prev_year[2:] + "1129")
    lookback_start_date2 = int(prev_year[2:] + "0701")
    lookback_end_date2 = int(str(int(prev_year[2:]) + 1) + "0528")

    holding_start_date1 = int(year[2:] + "0101")
    holding_end_date1 = int(year[2:] + "0628")
    holding_start_date2 = int(year[2:] + "0630")
    holding_end_date2 = int(year[2:] + "1229")

    top_20_syms_1 = get_top_20_symbols(symbol_list, year, lookback_start_date1, lookback_end_date1)
    pnl1, only_syms_list1, daily_pnl1, dt_lst1 = get_pnl_of_top_20_syms(top_20_syms_1, holding_start_date1, holding_end_date1)
    total_pnl_so_far = total_pnl_so_far + pnl1
    profit_per_year.append([year, 1, pnl1])
    # print(top_20_syms_1)
    print("pnl list", daily_pnl1)
    # print("date list", len(dt_lst1))
    print(f"Cumulative_pnl = {total_pnl_so_far}, PNL in last 6 months = {pnl1}")

    top_20_syms_2 = get_top_20_symbols(symbol_list, year, lookback_start_date2, lookback_end_date2)
    pnl2, only_syms_list2, daily_pnl2, dt_lst2 = get_pnl_of_top_20_syms(top_20_syms_2, holding_start_date2, holding_end_date2)
    total_pnl_so_far = total_pnl_so_far + pnl2
    profit_per_year.append([year, 2, pnl2])
    # print(top_20_syms_2)
    print("pnl list", daily_pnl2)
    # print("date list ", len(dt_lst2))
    print(f"Cumulative_pnl = {total_pnl_so_far}, PNL in last 6 months = {pnl2}")

    daily_pnl_list.extend(daily_pnl1)
    daily_pnl_list.extend(daily_pnl2)

    daily_dt_list_fin.extend(dt_lst1)
    daily_dt_list_fin.extend(dt_lst2)

    symbol_set.update(only_syms_list1)
    symbol_set.update(only_syms_list2)

print(symbol_set)
print(profit_per_year)


# df = pd.DataFrame(profit_per_year, columns=['year', 'part', '6_month_profit_perc'])
# df.to_csv('6_months_pnl_perc.csv', index=False)
daily_df = pd.DataFrame(daily_pnl_list, columns=['daily_pnl'])
daily_df['date'] = daily_dt_list_fin
daily_df.to_csv('daily_pnl.csv', index=False)
