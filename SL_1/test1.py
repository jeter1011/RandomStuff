import ptvsd
from streamlit.proto.RootContainer_pb2 import MAIN
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
TickerDf = tickerData.history( period = '1d', start = '2010-5-31', end = '2020-5-31')

ptvsd.enable_attach(address=("localhost", 5678))
ptvsd.wait_for_attach()
st.line_chart(TickerDf.Close)
st.line_chart(TickerDf.Volume)
