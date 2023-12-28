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
selected_date = st.sidebar.date_input("Select Date", data['Date'].min(), data['Date'].min(), data['Date'].max())
selected_columns = st.sidebar.multiselect("Select Columns for Line Chart", data.columns[2:])

# Filter data based on user input
selected_data = data[data['Date'] == selected_date][['Date'] + selected_columns]

# Line chart using Plotly Express
if not selected_data.empty:
    st.plotly_chart(px.line(selected_data, x='Date', y=selected_columns, title=f'Line Chart for {selected_date}'))

# Show selected data in a table
st.write("Selected Data:")
st.write(selected_data)
