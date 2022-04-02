from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
from pretty_html_table import build_table
import pandas as pd
import html2image

url1 = "https://money.cnn.com/data/markets"
page1 = urlopen(url1)
html = page1.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
browser = mechanicalsoup.Browser()
page2 = browser.get(url1)


string1='data-ticker-name="Dow"'
string2='data-ticker-name="S&amp;P"'
string3='data-ticker-name="Nasdaq"'
string4='class="quote-dollar" title="Gold"'
string5='class="quote-dollar" title="Oil"'
string6='title="10-year yield"'

strings=[string1, string2, string3, string4, string5, string6]
indices=[1]* len(strings)
font_colors=[1]* len(strings)

# setting flag and index to 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
flag6 = 0


index = 0
percent_changes=[None]* len(strings)
basis=[None]* len(strings)
# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

lines=html.split("\n")

for line in lines:
    index = index+1 
      
    # checking string is present in line or not
    if string1 in line:
        
      flag1 = 1
      indices[0]=index
      soup1 = BeautifulSoup(line, "html.parser")
      soup11 = BeautifulSoup(lines[index+1], "html.parser")
      soup10 = BeautifulSoup(lines[index+1], "html.parser")
    if string2 in line:
          
      flag2 = 1 
      indices[1]=index
      soup2 = BeautifulSoup(line, "html.parser")
      soup21 = BeautifulSoup(lines[index+1], "html.parser")
      
    if string3 in line:
          
      flag3 = 1
      indices[2]=index
      soup3 = BeautifulSoup(line, "html.parser")  
      soup31 = BeautifulSoup(lines[index+1], "html.parser")
    if string4 in line:
          
      flag4 = 1
      indices[3]=index
      soup4 = BeautifulSoup(lines[index], "html.parser")
      soup41 = BeautifulSoup(lines[index-1], "html.parser") 
    if string5 in line:
          
      flag5 = 1
      indices[4]=index
      soup5 = BeautifulSoup(lines[index], "html.parser")
      soup51 = BeautifulSoup(lines[index-1], "html.parser")
    if string6 in line:
          
      flag6 = 1
      indices[5]=index
      soup6 = BeautifulSoup(lines[index], "html.parser")
      soup61 = BeautifulSoup(lines[index-1], "html.parser")
 
      
      
# checking condition for string found or not
if flag1 == 0: 
   print('String', string1 , 'Not Found') 
else: 
   
   percent_changes[0] = soup1.get_text()
   if percent_changes[0][1]=='-':
       font_colors[0]='color: red'
   else:
       font_colors[0]='color: green'
if flag2 == 0: 
   print('String', string2 , 'Not Found') 
else: 
   
   
   percent_changes[1]  = soup2.get_text()
   if percent_changes[1][1]=='-':
       font_colors[1]='color: red'
   else:
       font_colors[1]='color: green'
if flag3 == 0: 
   print('String', string3 , 'Not Found') 
else: 
   
   percent_changes[2]  = soup3.get_text()
   if percent_changes[2][1]=='-':
       font_colors[2]='color: red'
   else:
       font_colors[2]='color: green'
if flag4 == 0: 
   print('String', string4 , 'Not Found') 
else: 
   
   
   percent_changes[3]  = soup4.get_text()
   if percent_changes[3][1]=='-':
       font_colors[3]='color: red'
   else:
       font_colors[3]='color: green'
if flag5 == 0: 
   print('String', string5 , 'Not Found') 
else: 
   
   
   percent_changes[4]  = soup5.get_text()
   if percent_changes[4][1]=='-':
       font_colors[4]='color: red'
   else:
       font_colors[4]='color: green'
if flag6 == 0: 
   print('String', string6 , 'Not Found') 
else: 
   
   
   percent_changes[5]  = soup6.get_text()
   if percent_changes[5][1]=='-':
       font_colors[5]='color: red'
   else:
       font_colors[5]='color: green'

basis[0]  = soup11.get_text()
basis[1]  = soup21.get_text()
basis[2]  = soup31.get_text()
basis[3]  = soup41.get_text()
basis[4]  = soup51.get_text()
basis[5]  = soup61.get_text()

Tickers=['The Dow', 'S&P 500', 'Nasdaq', 'Gold', 'Oil', '10-Year Yield']


import yfinance as yf
# Request data via Yahoo public API
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

for i in range(len(Tickys)):
    Tickers.append(Tickys[i])
    basis.append(closes[i])
    percent_changes.append(percents[i])
    if percents[i][0]=='-':
        font_colors.append('color: red')
    else:
        font_colors.append('color: green')

datainfo={"Index":Tickers, 'Closing' : basis,'Change': percent_changes}

df=pd.DataFrame(datainfo)
print(df)
html_table = build_table(df, 'blue_dark', width='auto', text_align='left', font_family='Sans Serif, verdana', even_color='black', conditions={'border-collapse': 'collapse'})                              


lines=html_table.split("\n")
Tickers[1]='S&amp;P 500'
index=0
for ticky in Tickers:

    
    for i in range(len(lines)):
        if ticky in lines[i]:
            index=index+1
            
            if index % 2==1:
                
                lines[i+2]='      <td style = "background-color: #D9E1F2;'+font_colors[index-1]+';font-family: Sans Serif, verdana;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">'+percent_changes[index-1]+'</td>'
                
            else: 
                lines[i+2]='      <td style = "background-color: white;'+font_colors[index-1]+';font-family: Sans Serif, verdana;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">'+percent_changes[index-1]+'</td>'
                
test_table="\n".join(lines)

with open('pretty_table.html', 'w') as f:
    f.write(test_table)





