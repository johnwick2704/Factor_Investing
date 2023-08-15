import pandas as pd
from ta.volume import money_flow_index
from ta.volatility import ulcer_index
from ta.trend import aroon_up, aroon_down, cci
from ta.others import cumulative_return
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = pd.read_csv("combined_nifty.csv")

data['mfi'] = money_flow_index(data['High'], data['Low'], data['Close'], data['Volume'], 50)

data['ma50'] = data['Close'].rolling(50).mean()
data['ma100'] = data['Close'].rolling(100).mean()

data['ui'] = ulcer_index(data['Close'], 20)

data['aroon_up'] = aroon_up(data['Close'], 50)
data['aroon_down'] = aroon_down(data['Close'], 50)
data['aroon'] = data['aroon_up'] - data['aroon_down']

data['cci'] = cci(data['High'], data['Low'], data['Close'], window=50)

# for row in data.itertuples():
#     if row.Close <= row.supertrend:
#         print(row.Date)


lim_mfi = data['mfi'].quantile(0.1)

fig = make_subplots(specs=[[{"secondary_y": True}]])

# fig.add_trace(go.Scatter(x=data['Date'], y=data['ma50'], name="50ma"), secondary_y=True,)
# fig.add_trace(go.Scatter(x=data['Date'], y=data['ma100'], name="100ma"), secondary_y=True,)
# fig.add_trace(go.Scatter(x=data['Date'], y=data['mfi'], name="mfi"), secondary_y=False,)
# fig.add_trace(go.Scatter(x=data['Date'], y=data['ui'], name="ui"), secondary_y=True,)
# fig.add_trace(go.Scatter(x=data['Date'], y=data['cci'], name="cci"), secondary_y=True,)
fig.add_trace(go.Scatter(x=data['Date'], y=data['aroon'], name="aroon"), secondary_y=True,)
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Close"), secondary_y=False,)

fig.show()

