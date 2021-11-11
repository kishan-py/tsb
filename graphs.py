import os,io,time,ssl
import streamlit as st
import pprint
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from altair import Chart, X, Y, Axis, SortField, OpacityValue
def create_graphs(stock,start_date,end_date,amount,wallet_money,total_stocks,profit,investment):
	print(stock)
	stocks = web.DataReader(stock, 'yahoo', start_date, end_date)
	stocks_close = pd.DataFrame(web.DataReader(stock, 'yahoo', start_date, end_date)['Close'])
	st.area_chart(stocks_close)






    #candle stick graph
	# candlestick = go.Figure(data = [go.Candlestick(x = stocks.index,
    #                                            open = stocks[('Open',stock)],
    #                                            high = stocks[('High', stock)],
    #                                            low = stocks[('Low', stock)],
    #                                            close = stocks[('Close',    stock)])])
	# candlestick.update_layout(xaxis_rangeslider_visible = False, title = stock+' SHARE PRICE (' +start_date+"-"+end_date+")")
	# candlestick.update_xaxes(title_text = 'Date')
	# candlestick.update_yaxes(title_text = stock+' Close Price', tickprefix = '$/Rs')

    # #generating temp plot image
	# # img2 = io.BytesIO()
	# area_chart = px.area(stocks_close, title =stock+' SHARE PRICE (' +start_date+"-"+end_date+")")

    # #area graph
	# area_chart.update_xaxes(title_text = 'Date')
	# area_chart.update_yaxes(title_text = stock+' Close Price', tickprefix = '$/Rs ')
	# area_chart.update_layout(showlegend = False)

    #generating temp plot image
	plt.clf()
	plt.cla()
	plt.close()
	return 1