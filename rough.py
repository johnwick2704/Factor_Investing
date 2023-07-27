import pandas as pd
import plotly.express as pe

csv = pd.read_csv("result.csv")
# lst = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
#               'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
#
# for row in csv.itertuples():
#     if row.date.split('-')[1] in lst:
#         stre = (row.date.replace(row.date.split('-')[1], month_dict[row.date.split('-')[1]]))
#         csv = csv.append({'date_fm': stre}, ignore_index=True)
#     else:
#         csv = csv.append({'date_fm': row.date}, ignore_index=True)
#
# csv.to_csv('nifty_50_new.csv', index=False)

# csv['date_fm'] = pd.to_datetime(csv['date_fm'], format='%d-%m-%Y')
# csv.to_csv('date.csv', index=False)

fig = pe.line(csv, x="date_fm", y=["result"])
fig.show()

