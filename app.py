import streamlit as st
import datetime
from backtesting.simulator import *
from backtesting.train import *
from backtesting.pred import *
st.title('Trading Strategy Backtesting')
st.write(""" This App will Predict the Profit/loss Based on the input such as stock name, 
time period and amount given by the user and
on the trading strategy that we have created.
""")

st.subheader('Stock Name:')
from data import data
stock_names=data

def format_func(stock):
    return stock_names[stock]

stock = st.selectbox("Stock_name",index=(len(data)-1),options=list(stock_names.keys()),format_func=format_func)

print(stock)
today=datetime.date.today()
st.subheader('Enter Start date of the time period for backtesting')

start_date = st.date_input('Start date',value=datetime.date(2018, 1, 2), min_value=datetime.date(2012, 1, 2),max_value=(today - datetime.timedelta(days=366)))

print(start_date)
print(type(start_date))
st.subheader('Enter End date of the time period for backtesting')


end_date = st.date_input('End date',value=(today - datetime.timedelta(days=1)), min_value=datetime.date(2012, 1, 2),max_value=(today - datetime.timedelta(days=1)))


amount=st.number_input("Amount",value=10000,step=1000,min_value=1000,max_value=1000000)
print(amount)
if st.button('Backtest'):
	if stock=="":
		st.error('Enter a valid Stock Name')
		st.stop()
	model = Model()
	train_execute(model, stock)
	wallet_money,total_stocks,profit,investment,current_price,open_close_graph,sma_graph,signal_graph= simulator_execute(stock,start_date,end_date,amount)
	profit=(profit-investment)
	from graphs import *
	area=create_graphs(stock,start_date,end_date,amount,wallet_money,total_stocks,profit,investment)

	df = {'Wallet Money': [wallet_money] ,'Total Stocks': [total_stocks] ,"Profit":[profit],"Investment":[investment]}
	# df = pd.DataFrame(data=df)
	# df
	# st.bar_chart(df)
	st.pyplot(open_close_graph)
	st.pyplot(sma_graph)
	st.pyplot(signal_graph)
	st.success(area)