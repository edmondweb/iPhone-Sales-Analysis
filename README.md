iPhone Sales Analysis using Python
==================================

This project is aimed at analyzing the sales data of iPhones in India using a dataset obtained from Kaggle. The dataset contains sales data of Apple iPhones on Flipkart. Through data analysis, we aim to understand the relationship between factors like ratings, sale price, discount percentage, and the number of reviews and ratings.


## Table of Contents

-----------------

* [Project Overview](#project-overview)
* [Dataset](#dataset)
* [Dependencies](#dependencies)
* [Code Overview](#code overview)
  * [Data Loading](#data loading)
  * [Data Cleaning](#data cleaning)
  * [Descriptive Statistics](#descriptive statistics)
  * [Data Visualization](#data visualization)
* [How to Run](#how to run)
* [License](#license)

Project Overview
----------------

Apple iPhones are among the top-selling smartphones globally. Despite intense competition in the Indian smartphone market, where you can find smartphones with similar features for a fraction of the price, iPhones maintain strong sales. This project investigates the factors contributing to the success of iPhones on Flipkart, India’s largest e-commerce platform. Using the dataset, we explore:

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
