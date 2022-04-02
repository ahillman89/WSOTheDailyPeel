import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go

ticker = 'MSFT'
df=web.DataReader(ticker,data_source='yahoo',start='01-01-2022')

trace1 = {
    'x': df.index,
    'open': df.Open,
    'close': df.Close,
    'high': df.High,
    'low': df.Low,
    'type': 'candlestick',
    'name': ticker,
    'showlegend': True
}
# Config graph layout
layout = go.Layout({
    'title': {
        'text': ticker +' Moving Averages',
        'font': {
            'size': 15
        }
    }
})

avg_30 = df.Close.rolling(window=30, min_periods=1).mean()
#30 day average onto chart
trace2 = {
    'x': df.index,
    'y': avg_30,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
            },
    'name': 'Moving Average of 30 trading days'
}
avg_50 = df.Close.rolling(window=50, min_periods=1).mean()
#50 day average onto chart
trace3 = {
    'x': df.index,
    'y': avg_50,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'red'
    },
    'name': 'Moving Average of 50 trading days'
}
data = [trace1, trace2, trace3]
# Config graph layout


fig = go.Figure(data=data, layout=layout)
fig.write_html(ticker + " Moving Averages.html")
fig.show()