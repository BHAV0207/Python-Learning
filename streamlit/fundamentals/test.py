import streamlit as st
import yfinance as yf
import datetime

st.write("""
         # stock Price  
         these are new stock price 
         """)



ticker_symbol = st.text_input("please enter the stock name " , 'AAPL' , key="placeholder")
ticker_data = yf.Ticker(ticker_symbol)

col1 , col2  = st.columns(2)

with col1:
  start_date = st.date_input("please enter the start date" , 
                           datetime.date(2019,1,1))
with col2:
  end_date = st.date_input("please enter the end date",
                         datetime.date(2022,12,31))
  
  

ticker_df = ticker_data.history(period="1d" , start=f"{start_date}" , end=f"{end_date}")

st.dataframe(ticker_df)


st.write("""
         # Chart for closing
         """)
st.line_chart(ticker_df.Close)


