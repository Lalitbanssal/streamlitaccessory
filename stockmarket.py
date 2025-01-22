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

nse_top_15 = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "Hindustan Unilever": "HINDUNILVR.NS",
    "State Bank of India": "SBIN.NS",
    "Bajaj Finance": "BAJFINANCE.NS",
    "Bharti Airtel": "BHARTIARTL.NS",
    "Adani Enterprises": "ADANIENT.NS",
    "Asian Paints": "ASIANPAINT.NS",
    "ITC Limited": "ITC.NS",
    "Kotak Mahindra Bank": "KOTAKBANK.NS",
    "Wipro": "WIPRO.NS",
    "Larsen & Toubro": "LT.NS"
}


# Dropdown to select a stock ticker
st.write("## Select a Stock from Top 15 NSE Companies")
selected_company = st.selectbox("Choose a company:", options=list(nse_top_15.keys()))
ticker_symbol = nse_top_15[selected_company]

ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period='1d',start=f"{start_date}",end=f"{end_date}")
st.dataframe(ticker_df)

st.write("""## Daily Closing Price""")


st.line_chart(ticker_df.Close)
