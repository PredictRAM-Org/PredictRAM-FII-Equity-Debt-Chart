import pandas as pd
import plotly.express as px

# Load the data from the Excel file
file_path = 'NIFTY.xlsx'
data = pd.read_excel(file_path)

# Print column names for user selection
print("Available columns:")
for col in data.columns:
    print(col)

# User input for date selection
selected_date = input("Enter the date (in the format YYYY-MM-DD): ")
selected_columns = input("Enter the column names (comma-separated) for the line chart: ").split(',')

# Filter data based on user input
selected_data = data[data['Date'] == selected_date][['Date'] + selected_columns]

# Line chart using Plotly Express
fig = px.line(selected_data, x='Date', y=selected_columns, title=f'Line Chart for {selected_date}')
fig.show()
