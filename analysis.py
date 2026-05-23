from pytrends.request import TrendReq
import pandas as pd

# Connect to Google
pytrends = TrendReq(hl='en-US', tz=330)
# Keywords
keywords = ["Python", "Machine Learning", "AI", "Data Science"]

# Build payload
pytrends.build_payload(keywords, timeframe='today 12-m')

# Get trends data
trends_data = pytrends.interest_over_time()

# Remove unnecessary column
if 'isPartial' in trends_data.columns:
    trends_data = trends_data.drop('isPartial', axis=1)

# Save CSV
trends_data.to_csv('trends.csv')

print("Data Saved Successfully")
print(trends_data.head())