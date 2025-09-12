iPhone Sales Analysis using Python
==================================

This project is aimed at analyzing the sales data of iPhones in India using a dataset obtained from Kaggle. The dataset contains sales data of Apple iPhones on Flipkart. Through data analysis, we aim to understand the relationship between factors like ratings, sale price, discount percentage, and the number of reviews and ratings.

## Table of Contents

- [Project Overview](#project-overview)

- [Dataset](#dataset)

- [Dependencies](#dependencies)

- [Code Overview](#codeoverview)
  
  - [Data Loading](#dataloading)
  
  - [Data Cleaning](#datacleaning)
  
  - [Descriptive Statistics](#descriptivestatistics)
  
  - [Data Visualizations](#datavisualization)

- [How to Run](#howtorun)

- [License](#license)

Project Overview
----------------

Apple iPhones are among the top-selling smartphones globally. Despite intense competition in the Indian smartphone market, where you can find smartphones with similar features for a fraction of the price, iPhones maintain strong sales. This project investigates the factors contributing to the success of iPhones on Flipkart, India’s largest e-commerce platform. 

Using the dataset, we explore:

* The highest-rated iPhones on Flipkart.

* The relationship between sale price, discount percentage, and ratings.

* The effect of reviews and ratings on iPhone sales.

Dataset
-------

The dataset used for this project is obtained from Kaggle and contains iPhone sales data from Flipkart. The dataset includes several columns, such as:

* **Product Name**: Name of the iPhone model.

* **Star Rating**: Customer ratings of the product.

* **Number of Ratings**: Total number of ratings received by the product.

* **Number of Reviews**: Number of product reviews on Flipkart.

* **Sale Price**: Price of the iPhone at the time of sale.

* **Discount Percentage**: Discount applied to the product.

Dependencies
------------

To run this project, you need to have the following Python libraries installed:

* `pandas` - for data manipulation.

* `numpy` - for numerical operations.

* `plotly` - for data visualization.

* `statsmodels` - for statistical modeling.

You can install the necessary libraries using pip:

```bash
pip install pandas numpy plotly statsmodels
```

## Code Overview



### Data Loading

The dataset is loaded using the `pandas` library from a CSV file.

```python
import pandas as pd
data = pd.read_csv("apple_products.csv")
print(data.head())
```

### Data Cleaning

Before performing any analysis, we check for missing values and get a summary of the data.

```python
# Checking for missing values in the dataset

print(data.isnull().sum())

# Descriptive Statistics for the iPhone Sales

print(data.describe())
```

### Descriptive Statistics

We calculate the summary statistics of the dataset, such as mean, median, and standard deviation, for understanding the general trends in iPhone sales.

### Data Visualizations

The project includes various visualizations to help understand the data:

#### Highest Rated iPhones

We sort the dataset to get the top 10 highest-rated iPhones and visualize their ratings.

```python
# Highest-rated iPhones in India on Flipkart

highest_rated = data.sort_values(by=["Star Rating"], ascending=False).head(10)
print(highest_rated["Product Name"])
```

#### Number of Ratings and Reviews

Bar charts are created to show the number of ratings and reviews for the highest-rated iPhones.

```python
# Number of ratings of the highest-rated iPhones

figure = px.bar(highest_rated, x=label, y=counts, title="Number of Ratings of Highest Rated iPhones")
figure.show()

# Number of Reviews of the Highest-rated iPhones

figure = px.bar(highest_rated, x=label, y=counts, title="Number of Reviews of Highest Rated iPhones")
figure.show()

```

#### Sale Price and Ratings Relationship

A scatter plot is created to analyze the relationship between sale price and ratings.

```python
# Relationship between Sale Price and Ratings

figure = px.scatter(data_frame=data, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title="Relationship between Sale Price and Number of Ratings")
figure.show()
```

#### Discount Percentage and Ratings

Another scatter plot shows how the discount percentage affects the number of ratings.

```python
# Relationship between Discount Percentage and Ratings

figure = px.scatter(data_frame=data, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship between Discount Percentage and Number of Ratings")
figure.show()
```

How to Run
----------

1. Download the dataset `apple_products.csv` from Kaggle.

2. Install the required libraries using the command mentioned above.

3. Run the code in a Jupyter notebook or Python environment.

4. The results will be displayed in the form of tables and visualizations.

License
-------

This project is licensed under the MIT License. See the [LICENSE file](https://opensource.org/licenses/MIT) for more details.

---------

Feel free to make modifications or improvements to the analysis and visualizations!
