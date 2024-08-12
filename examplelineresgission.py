import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data (X: hours studied, y: test scores)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions using the model
y_pred = model.predict(X)

# Plotting the data points
plt.scatter(X, y, color='blue', label='Actual Data')

# Plotting the regression line
plt.plot(X, y_pred, color='red', label='Regression Line')

# Adding titles and labels
plt.title('Linear Regression Example')
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')
plt.legend()

# Show the plot
plt.show()
