import quantstats as qs

# extend pandas functionality with metrics, etc.
qs.extend_pandas()

# fetch the daily returns for a stock
stock = qs.utils.download_returns('META')

# show sharpe ratio
print(qs.stats.sharpe(stock))
print(qs.reports.metrics(stock))
