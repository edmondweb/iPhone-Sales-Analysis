import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display

# Read the CSV file into a DataFrame
data = pd.read_csv("apple_products.csv")
print(data.head())

# Check for null values
print(data.isnull().sum())

# Fill or drop missing values if any
# data = data.dropna()  # Option 1: Drop rows with missing values
# data = data.fillna(0)  # Option 2: Fill missing values with 0

# Ensure correct data types
data["Star Rating"] = data["Star Rating"].astype(float)
data["Number Of Ratings"] = data["Number Of Ratings"].astype(int)

# Descriptive statistics for the iPhone Sales
print(data.describe())

# Highest-rated iPhones in India on Flipkart
highest_rated = data.sort_values(by=["Star Rating"], ascending=False).head(10)
print(highest_rated["Product Name"])

# Number of ratings of the highest-rated iPhones on Flipkart
figure = px.bar(highest_rated, x="Product Name", y="Number Of Ratings",
                title="Number of Ratings of Highest Rated iPhones",
                labels={"Product Name": "iPhone Model", "Number Of Ratings": "Number of Ratings"},
                color="Star Rating")
figure.update_layout(xaxis_title="iPhone Model", yaxis_title="Number of Ratings")
figure.show()

figure.write_html("highest_rated_iphones.html")
