import pandas_datareader
from pandas_datareader import data as web
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import traceback
import logging
import tkinter as tk
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Create a tkinter object that is called tk
root= tk.Tk()

#go out and get stock data from yahoo
tickers = 'AAPL'
start_date = '2019-06-01'
end_date = '2022-04-01'
df3=web.DataReader(tickers, 'yahoo', start_date, end_date)
closing_price=df3['Close']
dates=df3.index.tolist()

data2 = {'Date': dates,
         'AAPL Stock Price': closing_price
        }
df2 = DataFrame(data2,columns=['Date','AAPL Stock Price'])

figure2 = plt.Figure(figsize=(6,6), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['AAPL Stock Price']]
df2.plot(kind='line', legend=True, ax=ax2, fontsize=10)
ax2.set_title('Apple Stock Price Over Time')


FigureCanvasTkAgg(figure2, root)


root.mainloop()



