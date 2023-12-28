import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data from the Excel file
file_path = 'NIFTY.xlsx'
data = pd.read_excel(file_path)

# Streamlit app
st.title("NIFTY Data Visualization App")

# Sidebar for user input
st.sidebar.header("User Input")
start_date = st.sidebar.date_input("Select Start Date", data['Date'].min())
end_date = st.sidebar.date_input("Select End Date", data['Date'].max(), data['Date'].min(), data['Date'].max())
selected_columns = st.sidebar.multiselect("Select Columns for Line Chart", data.columns[2:])

# Filter data based on user input date range
selected_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)][['Date'] + selected_columns]

# Line chart using Plotly Express
if not selected_data.empty:
    st.plotly_chart(px.line(selected_data, x='Date', y=selected_columns, title=f'Line Chart for {start_date} to {end_date}'))

# Show selected data in a table
st.write("Selected Data:")
st.write(selected_data)
