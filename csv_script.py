import pandas as pd

# Define the path to the input CSV file
input_file_path = "/Users/PRINCESSSADIYA/Downloads/Generation_csv_ Project/input_data.csv"

# Load the CSV data into a DataFrame
data = pd.read_csv(input_file_path)

# Convert all values in the 'Name' column to strings and then to uppercase
data['Name'] = data['Name'].astype(str).str.upper()

# Define the path to the output CSV file
output_file_path = "/Users/PRINCESSSADIYA/Downloads/Generation_csv_ Project/output_data.csv"

# Save the modified DataFrame to a new CSV file
data.to_csv(output_file_path, index=False)

print("Data ETL process completed successfully.")
