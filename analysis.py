import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as pe

csv = pd.read_csv("daily_cum_pnl_datetime.csv")

# csv['date1'] = pd.to_datetime(csv['date']).dt.date
# print(csv['date'])
# csv.plot(x='date', y='cum_daily_pnl')
# plt.show()

# csv_mon = csv[['date', 'cum_daily_pnl']].resample('M').first()

fig = pe.line(csv, x='date', y=csv.columns[2:4])

             #  , hover_data={"date": "|%B %d, %Y"},
             # labels={"date": "Dates", "cum_daily_pnl": "Cumulative PNL %"})
# fig.update_xaxes(
#     dtick="M1",
#     tickformat="%b\n%Y")
fig.show()
# fig.write_html('profit_perc_date.html')

# csv = pd.read_csv("6_months_pnl_perc.csv")
# print(csv)
# fig = pe.bar(csv, x="year", y="6_month_profit_perc")
# fig.show()
fig.write_html("nifty_vs_stock.html")