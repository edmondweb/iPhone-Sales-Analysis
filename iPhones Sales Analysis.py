import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display
import statsmodels.api as sm
import plotly.io as pio
import plotly.offline as pyo



data = pd.read_csv("apple_products.csv")
print(data.head())

#checking whether the dataset contain any null values
print(data.isnull().sum())

#Descriptive Stastics for the iPhone Sales
print(data.describe())

#Highest-rated iPhones in India on Flipkart dataframe. The dataframe enables determining the most liked iPhone in India

highest_rated = data.sort_values(by=["Star Rating"], ascending = False)
highest_rated = highest_rated.head(10)
print(highest_rated["Product Name"])

#Number of ratings of the highest-rated iPhones on Flipkart
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label,
                        y=counts,
                title="Number of Ratings of Highest Rated iPhones")
figure.show()

#Humber of Reviews of the Highest-rated iPhones on Flipkart
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label, y=counts,
                title= "Number of Reviews of Highest Rated iPhones")
figure.show()

#Relationship Between the Sale Price of iPhones and their Flipkart Ratings
figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Sale Price", size= "Discount Percentage",
                    trendline="ols",
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()

#Relationship Between Discount Percentage on iPhones on Flipkart and the Number of Ratings
figure = px.scatter(data_frame= data, x="Number Of Ratings",
                    y="Discount Percentage", size="Sale Price",
                    trendline="ols",
                    title="Relationship between Discount Percentage and Number of Ratings of iPhones")
figure.show()