from fyers_api import fyersModel
import pandas as pd
import glob
import time
import os.path
import quantstats

client_id = 'APD18S1PBD-100'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2ODc3Njc0NTEsImV4cCI6MTY4NzgyNTgzMSwibmJmIjoxNjg3NzY3NDUxLCJhdWQiOlsiZDoxIiwiZDoyIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa21VbWJLRzRtYkJBUExmMnRRa0Y2U1FJeWl1S1c2Umx2Yk5rNUFBQzV2djRZeGRwNlFxc2p3ZG1LblBBVGNid2hnYjZORE9ubWJMUDZkMW9vR0FSX3BfYU41UDZleFVzVGJ4UlgzNUtLTUhDQXc1UT0iLCJkaXNwbGF5X25hbWUiOiJVVEtBUlNIIFNJTkdIIiwib21zIjoiSzEiLCJmeV9pZCI6IlhVMDQwNTMiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.U7tcIHeXXDml8i77E_dHX5rIcEAsYj1pBX0JZA_Q_AQ'

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
folder = glob.glob('CSV_files/*')
folder.sort()

data_1 = {
    "symbol": f"NSE:AAVAS-EQ",
    # "symbol": f"NSE:BCG-EQ",
    "resolution": "D",
    "date_format": "1",
    "range_from": f"2012-01-01",
    "range_to": f"2012-06-30",
}

data_last = {
    "symbol": f"NSE:AAVAS-EQ",
    # "symbol": f"NSE:BCG-EQ",
    "resolution": "D",
    "date_format": "1",
    "range_from": f"2012-07-01",
    "range_to": f"2012-12-31",
}

data_day_1 = fyers.history(data_1)
data_day_last = fyers.history(data_last)

print(data_day_1)
print(data_day_last)
