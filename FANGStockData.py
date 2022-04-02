# importing pandas as pd
import yfinance as yf
# Request data via Yahoo public API
from pretty_html_table import build_table
import pandas as pd

Tickers=["FB", "AMZN","GOOG","TSLA", "NVDA", "AMD", "TCEHY", "BABA", "CSCO", "INTC", "TCEHY", "AVGO", "ADBE", "QCOM", "PYPL", "TXN", "NFLX", "MSFT", "AAPL"]
deltas=[None]* len(Tickers)
closes=[None]* len(Tickers)
percents=[None]* len(Tickers)

index=0
for ticky in Tickers:
    index=index+1
   
    ticker=yf.Ticker(ticky)

    data = ticker.history(period="1mo")
    df=data
    tickdata=df.to_numpy()
    

    current=tickdata[df.shape[0]-1,3]
    closes[index-1]='${:.2f}'.format(current)
   
    yesterday_close=tickdata[df.shape[0]-2,3]
    

    delta=current-yesterday_close
    deltas[index-1]='${:.2f}'.format(delta)
    percents[index-1] = "{:.3%}".format(delta/yesterday_close)
    
database={"Ticker":Tickers, 'Closing' : closes,'Day Change': deltas,'Percent Change': percents}
df=pd.DataFrame(database)
print(df)
html_table = build_table(df, 'yellow_dark', font_size='medium', width='auto', text_align='center', font_family='Open Sans', even_color='black')
                                        

with open('pretty_table.html', 'w') as f:
    f.write(html_table)

# Compare to the pandas .to_html method:
with open('pandas_table.html', 'w') as f:
    f.write(df.to_html())



