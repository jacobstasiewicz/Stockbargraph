#!/usr/bin/env python3
import robin_stocks as r
import pandas as pd
import matplotlib.pyplot as plt
#logging in 
r.login("email","password")
#creating a list
my_stocks = r.build_holdings()
#showing the data
df = pd.DataFrame(my_stocks)
df = df.T
df['ticker'] = df.index
df  = df.reset_index(drop=True)
#showing certain indexs
df = df[['price', 'equity', 'percent_change', 'ticker', 'percentage']]
df['price'] = df.price.astype(float)
df['price'].round(decimals=2)
df['percent_change'] = df.percent_change.astype(float)
df
 
df.plot(kind='bar', x='ticker' ,y='price',color='green')
df.plot(kind='bar' , x ='ticker', y='percent_change')
plt.show()
