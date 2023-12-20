# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:43:15 2023

@author: Administrator
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
loandata = pd.read_json('loan_data_json.json')

# Finding Unique values for the purpose column
loandata['purpose'].unique()

# Describe the data
loandata.describe()

# Describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# Using EXP() to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income

# Working with arrays
# 0D Array
arr = np.array(25)

# 1D Array
arr = np.array([1, 2, 3, 4])

# 2D Array
arr = np.array(['1, 2, 3'], [4, 5, 6])

# FICO Score
# fico: The FICO credit score of the borrower.
# - 300 - 400: Very Poor
# - 401 - 600: Poor
# - 601 - 660: Fair
# - 661 - 780: Good
# - 781 - 850: Excellent

ficocat = []
for fico in loandata['fico']:
    if fico >= 300 and fico <= 400:
        cat = 'Very Poor'
    elif fico >= 401 and fico <= 600:
        cat = 'Poor'
    elif fico >= 601 and fico <= 660:
        cat= 'Fair'
    elif fico >= 661 and fico <= 780:
        cat = 'Good'
    elif fico >= 781 and fico <= 850:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat) 

loandata['fico.category'] = ficocat        


# df.loc as conditional statements
# df.loc[df[column_name] condition, newcolumn_name] = 'value if condition is met'

# for interest rates, a new column is wanted. rate > 0.12 then high, else low
loandata.loc [loandata['int.rate'] > 0.12, 'int_rate_type'] = 'high'
loandata.loc[loandata['int.rate'] < 0.12, 'int_rate_type'] = 'low'       
        
# Number of rows by fico.category

catplot = loandata.groupby(['fico.category']).size()        
catplot.plot.bar(color = 'green', width = 0.15)
plt.show()        

purposecount = loandata.groupby(['purpose']).size()       
purposecount.plot.bar(color = 'brown', width = 0.25)
plt.show()        

# Scatter Plot
xpoint = loandata['dti']
ypoint = loandata['annual income']
plt.scatter(xpoint, ypoint, color = 'red')      
plt.show()        
        
# Writing to csv
loandata.to_csv('loandata_cleaned.csv', index = True)
        
        
        
        
        
        
        
        