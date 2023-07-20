# Project Immo Eliza

Real Estate Data Scraping and regression

This repository contains the code and data used to scrape real estate listings from a immoweb website and then classify the properties into two categories: apartments and houses. The data is collected, preprocessed, and split into training and testing sets to build a regression model to predict price of properties.


Table of Contents
1-Introduction
2-Requirements
3-Data Preprocessing
4-Data Analyzing
5-Usage
6-Contributing
7-License


1-Introduction
The aim of this project is to collect real estate data from a specific real estate website, categorize the properties into apartments and houses, and then use the data to train and test a regression model. By doing this, we can predict the property type of new listings based on the features of the property.


2-Requirements
Before running the code in this repository, you will need the following:
Python (version 3.1.1.4)
Pandas library
Scikit-learn library


3-Data Preprocessing
The data collection process involved the removal of duplicates and missing values.


4-Data Analyzing
After preprocessing the data, it is split into training and testing sets. We then use machine learning to build a regression model using DecisionTreeRegressor,LinearRegression, SVR function that can predict prices of a properties in future. 


5-Usage
You can use this repository as a starting point to scrape real estate data from other websites or experiment with different regression models and features for price prediction. 


6-Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. We welcome any improvements or additional features!


7-License
This project is licensed under the MIT License, allowing you to use, modify, and distribute the code freely. However, please note that the data scraped from the real estate website might have its terms of use and restrictions. Make sure to comply with the website's policy when using the data.














