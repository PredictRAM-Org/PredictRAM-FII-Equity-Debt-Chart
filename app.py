import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
equity_data = pd.read_excel("FIIEquityData.xlsx")
debt_data = pd.read_excel("FIIDebtData.xlsx")

# Merge data on 'Date' column
merged_data = pd.merge(equity_data, debt_data, on='Date', how='outer', suffixes=('_equity', '_debt'))

# Convert 'Date' column to datetime
merged_data['Date'] = pd.to_datetime(merged_data['Date'])

# Filter columns for plotting
plot_data = merged_data[['Date', 'Net Investment_equity', 'Net Investment_debt']]

# Streamlit app
st.title("Net Investment Comparison")

# Date selection
selected_date = st.date_input("Select Date", min_value=merged_data['Date'].min(), max_value=merged_data['Date'].max())

# Filter data based on selected date
selected_data = plot_data[plot_data['Date'] == selected_date]

# Plotting
fig = px.bar(selected_data, x='Date', y=['Net Investment_equity', 'Net Investment_debt'],
             labels={'value': 'Net Investment', 'variable': 'Category'}, barmode='group')

# Update layout for better visualization
fig.update_layout(title=f"Net Investment Comparison on {selected_date}",
                  xaxis_title='Date',
                  yaxis_title='Net Investment',
                  legend_title='Category')

# Display the plot
st.plotly_chart(fig)
