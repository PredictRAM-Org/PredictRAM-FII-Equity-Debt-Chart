import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

# Load FII data
equity_data = pd.read_excel("FIIEquityData.xlsx")
debt_data = pd.read_excel("FIIDebtData.xlsx")

# Merge FII data on 'Date' column
merged_fii_data = pd.merge(equity_data, debt_data, on='Date', how='outer', suffixes=('_equity', '_debt'))

# Convert 'Date' column to datetime
merged_fii_data['Date'] = pd.to_datetime(merged_fii_data['Date'])

# Filter columns for plotting
fii_plot_data = merged_fii_data[['Date', 'Net Investment_equity', 'Net Investment_debt']]

# Get Nifty data using yfinance
nifty_data = yf.download('^NSEI', start=fii_plot_data['Date'].min(), end=fii_plot_data['Date'].max())

# Extract Nifty closing prices and calculate percentage change
nifty_data['Date'] = nifty_data.index
nifty_data['Nifty_Close_Percentage'] = nifty_data['Close'].pct_change() * 100

# Merge Nifty data with FII data
merged_data = pd.merge(fii_plot_data, nifty_data[['Date', 'Nifty_Close_Percentage']], on='Date', how='outer')

# Streamlit app
st.title("Net Investment and Nifty Comparison")

# Plotting
fig = px.bar(merged_data, x='Date',
             y=['Net Investment_equity', 'Net Investment_debt', 'Nifty_Close_Percentage'],
             labels={'value': 'Percentage', 'variable': 'Category'},
             barmode='group')

# Update layout for better visualization
fig.update_layout(title="Net Investment and Nifty Comparison",
                  xaxis_title='Date',
                  yaxis_title='Percentage',
                  legend_title='Category')

# Display the plot
st.plotly_chart(fig)
