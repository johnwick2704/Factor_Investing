import pandas as pd
from ta.volume import money_flow_index
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = pd.read_csv("combined_nifty.csv")
data['mfi'] = money_flow_index(data['High'], data['Low'], data['Close'], data['Volume'], 50)

lim_mfi = data['mfi'].quantile(0.1)

data['ma50'] = data['Close'].rolling(50).mean()
data['ma100'] = data['Close'].rolling(100).mean()

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x=data['Date'], y=data['ma50'], name="50ma"), secondary_y=True,)
fig.add_trace(go.Scatter(x=data['Date'], y=data['ma100'], name="100ma"), secondary_y=True,)
# fig.add_trace(go.Scatter(x=data['Date'], y=data['mfi'], name="mfi"), secondary_y=False,)
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Close"), secondary_y=True,)

fig.show()

