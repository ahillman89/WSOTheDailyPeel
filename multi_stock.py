from pandas_datareader import data as web
import plotly.graph_objects as go

ticker1 = 'GME'
ticker2='CF'
df1=web.DataReader(ticker1,data_source='yahoo',start='01-01-2022')
df2=web.DataReader(ticker2,data_source='yahoo',start='01-01-2022')

trace1 = {
    'x': df1.index,
    'open': df1.Open,
    'close': df1.Close,
    'high': df1.High,
    'low': df1.Low,
    'type': 'candlestick',
    'name': ticker1,
    'showlegend': True
}
trace2 = {
    'x': df2.index,
    'open': df2.Open,
    'close': df2.Close,
    'high': df2.High,
    'low': df2.Low,
    'type': 'candlestick',
    'name': ticker2,
    'showlegend': True
}
# Config graph layout
layout = go.Layout( title= ticker1 + ' & ' +ticker2 +' Moving Averages', font_size=15,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

data = [trace1, trace2]
# Config graph layout


fig = go.Figure(data=data, layout=layout)
fig.write_html(ticker1 + "& " +ticker2 +" Stock Price.html")
fig.show()