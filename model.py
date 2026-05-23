import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv('trends.csv')

# Create numerical index

df['Index'] = np.arange(len(df))

# Feature and target

X = df[['Index']]
y = df['Python']

# Train model

model = LinearRegression()
model.fit(X, y)
future_days = np.array([[len(df)+1], [len(df)+2], [len(df)+3]])
predictions = model.predict(future_days)

print("Future Predictions:")
print(predictions)

# Plot graph

plt.figure(figsize=(10,5))
plt.plot(df['Index'], y, label='Original Data')
plt.plot(future_days, predictions, 'ro-', label='Predictions')

plt.xlabel('Days')
plt.ylabel('Search Interest')
plt.title('Google Trend Prediction')
plt.legend()

plt.show()