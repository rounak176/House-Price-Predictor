# -*- coding: utf-8 -*-
"""Multicollinearity Removal using VIF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dj_xSrk-STmb3yzwUiqq6WhIkH67GXtt
"""

# Read the data
import pandas as pd
data = pd.read_csv("https://trello-attachments.s3.amazonaws.com/5cf2142046ceb163a0e4b189/5d0739020214d314bd77baf8/69885d162bc4e006add707dc14efb596/Housing_Modified_prepared.csv")

# Select independent and dependent variables
Y = data["price"]
independent_variables = data.columns
independent_variables = independent_variables.delete(0)
X = data[independent_variables]

# Fit the Ordinary Least Squared Regression Model
import statsmodels.api as sm
model = sm.OLS(Y, X)

# Train the model
model = model.fit()

# Check the model summary
model.summary()

# Calculate variance inflation factor
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
for i in range(len(independent_variables)):
  vif_list = [vif(data[independent_variables].values, index) for index in range(len(independent_variables))]
  mvif = max(vif_list)
# print("Max VIF value is", mvif)
  drop_index = vif_list.index(mvif)
# print("For the Independent variable", independent_variables[drop_index])
  if mvif > 10:    
#   print("Deleting", independent_variables[drop_index])
    independent_variables = independent_variables.delete(drop_index)
#print("Final Independent Variables", independent_variables)

Y = data["price"]
X = data[independent_variables]
model = sm.OLS(Y, X)
model = model.fit()

model.summary()

import sys
index = 1
user_input = {}
for var in independent_variables:
  temp = sys.argv[index]
  user_input[var] = temp
  index = index + 1
user_df = pd.DataFrame(data=user_input, index=[0], columns=independent_variables)  
import sklearn.linear_model as lm
lr = lm.LinearRegression()
lr.fit(X, Y)
price = lr.predict(user_df)
print("House Price is USD", int(price[0]))

