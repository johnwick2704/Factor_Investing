from fyers_api import fyersModel
import pandas as pd
import glob
import time
import os.path
import quantstats_library

client_id = 'APD18S1PBD-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2OTA0MzM4NzEsImV4cCI6MTY5MDUwNDI1MSwibmJmIjoxNjkwNDMzODcxLCJhdWQiOlsiZDoxIiwiZDoyIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa3dmbFAwQVp6ZzJ1MVUycENzUU9falFfaFR3eVV4UnFhRlBHX1FqYjJ0QzI4dlhnUnN3NjRscS1CVDF0ZzZzUzJwWTV6Y2lhUlNpVnVUOGdQb3U0bEZaSS1ENFl4aWZBU1FwUjdNVjlfazRvQzNaaz0iLCJkaXNwbGF5X25hbWUiOiJVVEtBUlNIIFNJTkdIIiwib21zIjoiSzEiLCJoc21fa2V5IjoiYjViNDQ0ZDY5YzY5Nzc3YTU1Nzg5NzcyZTBkYWEzNDY3ZDcwYjE1YmRlZjA4MTRlNDVhYTZkMGEiLCJmeV9pZCI6IlhVMDQwNTMiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.ltUUwYGwKwd2gkTO4Co7rna5laB8XFKPjShZAGI1aes'

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
folder = glob.glob('CSV_files/*.csv')
folder.sort()
c = 0
count = 0

for file in folder:
    count = count + 1
    csv = pd.read_csv(file)
    for index, rows in csv.iterrows():
        symbol = rows['Symbol']
        if os.path.exists(f"D:\CSV/{symbol}"):
            continue
        for year in range(2012, 2023):
            if os.path.exists(f"D:/CSV/{symbol}_{year}_1.csv") or os.path.exists(f"D:/CSV/{symbol}_{year}_2.csv"):
                continue
            print(year)
            if c > 0 and c % 30 == 0:
                time.sleep(20)
            c += 1
            print(rows['Symbol'])
            data_1 = {
                "symbol": f"NSE:{rows['Symbol']}-EQ",
                # "symbol": f"NSE:BCG-EQ",
                "resolution": "D",
                "date_format": "1",
                "range_from": f"{year}-01-01",
                "range_to": f"{year}-06-30",
            }

            data_last = {
                "symbol": f"NSE:{rows['Symbol']}-EQ",
                # "symbol": f"NSE:BCG-EQ",
                "resolution": "D",
                "date_format": "1",
                "range_from": f"{year}-07-01",
                "range_to": f"{year}-12-31",
            }

            data_day_1 = fyers.history(data_1)
            data_day_last = fyers.history(data_last)

            print(data_day_1)
            print(data_day_last)

            if data_day_1['s'] == 'error':
                continue
            if data_day_last['s'] == 'error':
                continue

            if len(data_day_1['candles']) >= 1:
                close = data_day_1['candles']
                df = pd.DataFrame(close, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
                df.to_csv(f"D:/CSV/{symbol}_{year}_1.csv", index=False)
            if len(data_day_last['candles']) >= 1:
                close = data_day_last['candles']
                df = pd.DataFrame(close, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
                df.to_csv(f"D:/CSV/{symbol}_{year}_2.csv", index=False)

# response = fyers.history(data=data)
# df = pd.DataFrame(response['candles'], columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
# print(df)
