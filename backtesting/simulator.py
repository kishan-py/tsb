# Takes output predicted by ML model 
# Outputs how much profit user would have made if he/she would have used model to trade

# Importing required modules
import pandas as pd
from backtesting.pred import *
import matplotlib.pyplot as plt
import numpy as np
import pprint


# Function   :- fetches output predicted by ML model
# Returns    :- DataFrame containing output predicted by model
def get_pred(stock,start_date,end_date):
    return calls(stock,start_date,end_date)

# Function   :- calculates and finds how much profit or loss would have happened if user invested according ML model
# Parameters :- t - DataFrame containing output of ML model
def simulator(t,amount):
    # m - amount which user want to invest
    # c - count of stock
    m = amount
    dm=amount
    c = 0
    print(f'Default Money = {m}')
    print("\n")
    # calculating profit or loss according output predicted by ML model
    for i in range(len(t)):
        if (t['pred'][i] > 0):
            if m > t['Close'][i]:
                m = m - t['Close'][i]
                c = c + 1

        else:
            if c > 0:
                m = m + t['Close'][i]
                c = c - 1
    profit=c*t["Open"][-1] + m
    print(f'Money = {m}')
    print(f'Stock = {c}')
    print(f'Profit = {c*t["Open"][-1] + m}')
    #open close price graph

    open_close_graph = plt.figure(figsize=(12.5, 6.5))
    plt.plot(t['Open'], label='Open price')
    plt.plot(t['Close'], label= 'closing price')
    plt.xlabel('opening/closing price')
    plt.ylabel('Dates')
    plt.legend(loc='upper left')

    #sma graph
    sma_graph=plt.figure(figsize=(12.5, 4.5))
    plt.plot(t['Adj Close'], label='Adj Close')
    plt.plot(t['SMA30'], label= 'SMA30')
    plt.plot(t['SMA60'], label= 'SMA60')
    plt.plot(t['SMA90'], label= 'SMA90')

    plt.xlabel('Adj Close')
    plt.ylabel('SMA30')

    plt.legend(loc='upper left')

    #signal graphs
    t["sell signal"] = np.nan
    t["buy signal"] = np.nan
    for x in t['pred']:
        if(x==0):
            t['sell signal'] = t['Adj Close']
        else:
            t['buy signal'] = t['Adj Close']
    signal_graph = plt.figure(figsize=(12.5, 4.5))
    plt.plot(t['Adj Close'], label='Adj Close',color = 'orange', linewidth=2)
    for x in t['pred']:
        if x == 0:
            plt.scatter(t.index, t['sell signal'], marker='v' , color = 'green')
        else:
            plt.scatter(t.index, t['buy signal'], marker='^' , color = 'blue')
    plt.xlabel('price')
    # plt.ylabel('index')
    plt.legend(loc='upper left')
    t.to_csv(r'x.csv', index = False)

    return m,c,profit,dm,open_close_graph,sma_graph,signal_graph

# Function   :- fetches output predicted by ML model and give it to simulator()
def simulator_execute(stock,start_date,end_date,amount):
    from yahoo_fin import stock_info as si
    print(type(stock))
    current_price=si.get_live_price(stock)
    print(current_price)
    df = get_pred(stock,start_date,end_date)
    print(type(df))
    print(df)

    wallet_money,total_stocks,profit,investment,open_close_graph,sma_graph,signal_graph= simulator(df,amount)
    return wallet_money,total_stocks,profit,investment,current_price,open_close_graph,sma_graph,signal_graph
