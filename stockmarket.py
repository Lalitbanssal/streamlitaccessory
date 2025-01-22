import streamlit as st
import pandas as pd
import yfinance as yf
import datetime


st.title("Stock Market Predicition Made by Lalit Bansal")
st.write("This is my sample website for testing")

import datetime
start_date = st.date_input("Please enter Starting Date", datetime.date(2024,12,1))
end_date = st.date_input("Please enter Ending Date", datetime.date(2025,1,16))
import yfinance as yf
ticker_symbol ='RELIANCE.NS'
ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period='1d',start=f"{start_date}",end=f"{end_date}")
st.dataframe(ticker_df)

st.write("""## Daily Closing Price""")


st.line_chart(ticker_df.Close)
