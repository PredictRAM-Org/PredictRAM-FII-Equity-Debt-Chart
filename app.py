import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data from the Excel file
file_path = 'NIFTY.xlsx'
data = pd.read_excel(file_path)

# Convert 'Date' column to Pandas Timestamp
data['Date'] = pd.to_datetime(data['Date'])

# Streamlit app
st.title("NIFTY Data Visualization App")

# Sidebar for user input
st.sidebar.header("User Input")

# Option to select start date
start_date = st.sidebar.date_input("Select Start Date", data['Date'].min().date())

# Option to select end date
end_date = st.sidebar.date_input("Select End Date", data['Date'].max().date(), data['Date'].min().date(), data['Date'].max().date())

# Specify columns for the line chart
selected_columns = st.sidebar.multiselect(
    "Select Columns for Line Chart",
    ['Close', 'Points Change', 'Debt Net Investment', 'Equity Net Investment']
)

# Filter data based on user input date range
selected_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Line chart using Plotly Express
if not selected_data.empty and selected_columns:
    st.plotly_chart(px.line(selected_data, x='Date', y=selected_columns, title=f'Line Chart for {start_date} to {end_date}'))

# Show selected data in a table
st.write("Selected Data:")
st.write(selected_data)
