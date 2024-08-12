import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('website access.csv')

# Convert 'CreatedDate' and 'UpdatedDate' columns to datetime format
# Use errors='coerce' to convert invalid values to NaT
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'], errors='coerce')
df['UpdatedDate'] = pd.to_datetime(df['UpdatedDate'], errors='coerce')

# Plot the total page views by device type
plt.figure(figsize=(10, 6))
df.groupby('Device Used')['PageViews'].sum().plot(kind='bar')
plt.title('Total Page Views by Device Type')
plt.xlabel('Device Type')
plt.ylabel('Total Page Views')
plt.xticks(rotation=45)
plt.show()

# Plot the average bounce rate by device type
plt.figure(figsize=(10, 6))
df.groupby('Device Used')['BounceRate'].mean().plot(kind='bar', color='orange')
plt.title('Average Bounce Rate by Device Type')
plt.xlabel('Device Type')
plt.ylabel('Bounce Rate (%)')
plt.xticks(rotation=45)
plt.show()

# Plot the average session duration by device type
plt.figure(figsize=(10, 6))
df.groupby('Device Used')['AverageSessionDuration'].mean().plot(kind='bar', color='green')
plt.title('Average Session Duration by Device Type')
plt.xlabel('Device Type')
plt.ylabel('Average Session Duration (minutes)')
plt.xticks(rotation=45)
plt.show()

# Plot total page views and unique visitors over time
plt.figure(figsize=(12, 8))
df.groupby('CreatedDate').agg({'PageViews': 'sum', 'UniqueVisitors': 'sum'}).plot()
plt.title('Total Page Views and Unique Visitors Over Time')
plt.xlabel('Date')
plt.ylabel('Total Page Views / Unique Visitors')
plt.legend(['Total Page Views', 'Unique Visitors'])
plt.show()








