import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

st.title('🕯️ Candlestick chart')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

st.plotly_chart(fig)
