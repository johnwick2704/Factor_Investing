import pandas as pd
import plotly.express as pe

csv = pd.read_csv("nifty_50_new.csv")
start = 0
end = 0
lst = []
c = 0

for row in csv.itertuples():
    if c == 0:
        start = row.close
    lst.append(row.close - start)
    c = c + 1

df = pd.DataFrame(lst)
df.to_csv("result_absolute.csv", index=False)


