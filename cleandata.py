import pandas as pd
import os

# Load the data from the CSV file
df = pd.read_csv('customer.csv')

# Drop any columns that are completely empty
df.dropna(how='all', axis=1, inplace=True)

# Remove any rows where CustomerID is null
df.dropna(subset=['CustomerID'], inplace=True)

# Convert the CustomerID to integers
df['CustomerID'] = df['CustomerID'].astype(int)

# Fill missing values in the Gender column with 'Unknown'
df['Gender'] = df['Gender'].fillna('Unknown')

# Fill missing values in the FirstName and other string columns with 'Unknown'
df.fillna({'FirstName': 'Unknown',
           'LastName': 'Unknown',
           'Email': 'Unknown',
           'PhoneNumber': 'Unknown',
           'Address': 'Unknown',
           'City': 'Unknown',
           'State': 'Unknown',
           'ZipCode': 'Unknown',
           'Country': 'Unknown'}, inplace=True)

# Convert the DateOfBirth to datetime format
df['DateOfBirth'] = pd.to_datetime(df['DateOfBirth'], errors='coerce')

# Drop any rows with invalid DateOfBirth
df.dropna(subset=['DateOfBirth'], inplace=True)

# Save the cleaned data to a new CSV file
output_path = 'customer_cleaned.csv'
df.to_csv(output_path, index=False)

print(f'Data cleaned and saved to {output_path}')





