import numpy as np 
import pandas as pd
df = pd.read_csv(r'Data\df_final.csv')

# HOUSES
houses_df = df[df['Type_of_property'] == 'HOUSE']    
# Function to check if a value is "No info"
def has_no_info(value):
    return value != 'No info'

# Apply the function to all cells in the DataFrame
houses_df_cleaned = houses_df[houses_df.applymap(has_no_info).all(axis=1)]
# Find columns with "No info" values
columns_with_no_info = houses_df_cleaned.columns[houses_df_cleaned.isin(['No info']).any()]

# Count occurrences of "No info" in each column
count_no_info = houses_df_cleaned[columns_with_no_info].apply(lambda col: col.eq('No info').sum())

# Output the results
print("Columns with 'No info' values:")
print(columns_with_no_info)

print("\nCount of 'No info' occurrences in each column:")
print(count_no_info)

x_h = houses_df_cleaned.drop(columns=["Unnamed: 0.1", "Unnamed: 0","id","Locality","Type_of_sale", "Postcode",	"Street",'Type_of_property'	, "Number",	"Subtype_of_property","Price","Fully_equipped_kitchen","Furnished","Garden","Open_fire","Terrace"," Swimming_pool", "State_of_the_building",'Garden' ])
features_h = x_h.columns
x_h = x_h.to_numpy()
y_h = houses_df_cleaned.Price.to_numpy().reshape(-1 , 1)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR


def training_testing_scores(x_data, y_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, random_state=42)
    train_list = []
    test_list=[]
    for regressor in [DecisionTreeRegressor(max_depth=10),LinearRegression(), SVR(kernel='linear', C=1.0)]: 
     regressor.fit(x_train,y_train)
     train_score = regressor.score(x_train, y_train)
     test_score =regressor.score(x_test, y_test)
     train_list.append(train_score)
     test_list.append(test_score)

    return train_list, test_list

print(training_testing_scores(x_h,y_h),"Houses Scores")


#Apartments
apartments_df = df[df['Type_of_property'] == 'APARTMENT']
apartments_df = apartments_df.drop(['Surface_of_the_land', 'Surface_area_of_the_plot_of_land'], axis=1)

# Find columns with "No info" values
columns_with_no_info = apartments_df.columns[apartments_df.isin(['No info']).any()]

# Count occurrences of "No info" in each column
count_no_info = apartments_df[columns_with_no_info].apply(lambda col: col.eq('No info').sum())

# Output the results
print("Columns with 'No info' values:")
print(columns_with_no_info)

print("\nCount of 'No info' occurrences in each column:")
print(count_no_info)

# Function to check if a value is "No info"
def has_no_info(value):
    return value != 'No info'

# Apply the function to all cells in the DataFrame
apartments_df_cleaned = apartments_df[apartments_df.applymap(has_no_info).all(axis=1)]

apartments_df_cleaned.isna().sum().sum()

x_a = apartments_df_cleaned.drop(columns=["Unnamed: 0.1", "Unnamed: 0","id","Locality","Type_of_sale", "Postcode",	"Street",'Type_of_property'	, "Number",	"Subtype_of_property","Price","Fully_equipped_kitchen","Furnished","Garden","Open_fire","Terrace"," Swimming_pool", "State_of_the_building" ,'Garden','Number_of_facades'])
features_a = x_a.columns
x_a = x_a.to_numpy()
y_a = apartments_df_cleaned.Price.to_numpy().reshape(-1 , 1)
print(training_testing_scores(x_a,y_a), "Apartement Scores")