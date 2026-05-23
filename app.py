import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Page Title
st.title("Google Search Analysis Dashboard")

# Load Dataset
try:
    df = pd.read_csv('trends.csv')
except:
    st.error("Run analysis.py first to generate trends.csv")
    st.stop()
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Dataset Information
st.subheader("Dataset Shape")
st.write(df.shape)

# Check Missing Values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Line Chart
st.subheader("Google Search Trends")

fig, ax = plt.subplots(figsize=(12,6))

columns_to_plot = ['Python', 'Machine Learning', 'AI', 'Data Science']

sns.lineplot(data=df[columns_to_plot], ax=ax)

plt.xlabel("Time")
plt.ylabel("Search Interest")
plt.title("Keyword Trends")

st.pyplot(fig)

# Correlation Heatmap
st.subheader("Correlation Heatmap")

fig2, ax2 = plt.subplots(figsize=(8,6))

sns.heatmap(df[columns_to_plot].corr(), annot=True, cmap='coolwarm', ax=ax2)

st.pyplot(fig2)

# Machine Learning Prediction
st.subheader("Future Trend Prediction")

# Create Index

df['Index'] = np.arange(len(df))
X = df[['Index']]
y = df['Python']

# Train Model

model = LinearRegression()
model.fit(X, y)

# Future Days

future_days = np.array([[len(df)+1], [len(df)+2], [len(df)+3]])

predictions = model.predict(future_days)

# Show Predictions

prediction_df = pd.DataFrame({
    'Future Day': [1,2,3],
    'Predicted Search Interest': predictions
})

st.dataframe(prediction_df)

# Prediction Graph

fig3, ax3 = plt.subplots(figsize=(10,5))

ax3.plot(df['Index'], y, label='Original Data')
ax3.plot(future_days, predictions, 'ro-', label='Predictions')

plt.xlabel('Days')
plt.ylabel('Search Interest')
plt.title('Future Search Trend Prediction')
plt.legend()

st.pyplot(fig3)

# Footer
st.success("Project Running Successfully")