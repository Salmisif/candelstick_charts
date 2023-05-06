#we wille work with dates
import datetime as dt
from pickle import TRUE
from tracemalloc import start
#to read the data we give 
import pandas_datareader as pd
#to plot and visual the dtat 
import matplotlib.pyplot as mp
#we wille convert our date to specific format
import matplotlib.dates as md
# ohlc => open height low close we need it to order our data withe spcific 
from mpl_finance import candlestick_ohlc
import yfinance as yf

#define time frame


start = dt.datetime(2012,9,1)
end = dt.datetime.now()

#load data
data = yf.download("EURUSD=X", start=start, end=end)




#Restructure data
data= data[['Open','High','Low','Close']]

#here we will add indexs to our data
data.reset_index(inplace=True)

#convert Date to numerique nmber by using dte2num methode
data['Date']= data ['Date'].map(md.date2num)

#plote our data visualiwation

ax = mp.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.xaxis_date()

candlestick_ohlc(ax,data.values,width=0.5,colorup='#00ff00')

mp.show()