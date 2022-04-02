import yfinance as yf
# Request data via Yahoo public API
from pretty_html_table import build_table
import pandas as pd

Tickys=["ETH-USD", "BTC-USD"]
deltas=[None]* len(Tickys)
closes=[None]* len(Tickys)
percents=[None]* len(Tickys)

index=0
for ticky in Tickys:
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

database={"Ticker":Tickys, 'Closing' : closes,'Day Change': deltas,'Percent Change': percents}
crypto=pd.DataFrame(database)
print(database)
