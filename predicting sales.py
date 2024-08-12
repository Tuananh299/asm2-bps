import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example data: Past monthly sales
data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Sales': [200, 220, 230, 250, 240, 260, 270, 280, 300, 310, 320, 340]
}
df = pd.DataFrame(data)

# Prepare data
X = df[['Month']]  # Independent variable (Month)
y = df['Sales']    # Dependent variable (Sales)

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict sales for the next 3 months
future_months = np.array([[13], [14], [15]])
predicted_sales = model.predict(future_months)

# Print predicted sales
print(f'Predicted sales for month 13, 14, 15: {predicted_sales}')

# Plotting the results
plt.scatter(X, y, color='blue', label='Actual Sales')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(future_months, predicted_sales, color='green', label='Predicted Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Prediction')
plt.legend()
plt.show()
