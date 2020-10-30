# -------------------------------------------------
# Data Manipulation with pandas - Aggregating data
# 26 out 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages
library(reticulate)

####################################################
# Summary statistics 
####################################################
# .mean() - retunrs the mean
# .median()
# .mode()
# .min()
# .max()
# .var()
# .std()
# .sum()
# .quantile()
# .agg() - allows you to compute custom statistics
# .cumsum() - returns the cummulative sum
# .cummax()
# .cummin()
# .cumprod()
import pandas as pd
sales = pd.read_csv('Datasets/sales_subset.csv', sep = ',')

# Mean and median
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())

# The mean weekly sales amount is almost double the median week;y sales amount.
# This means that there are a few very high sales weeks that are making the mean
# so much higher than the median.

# Summarizing dates
# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())

# The time period covered by the data set ranges from February of 2010 to October
# of 2012

# Efficient summaries
# IQR is short for interquartile range, which is the 75th precentile minus the 25th
# percentile. It's an alternative to standard deviation that is helpful if the data 
# contains outliers
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
quit()    
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))

# Import NumPy 
import numpy as np

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# Cummulative statistics
# Create a DataFrame called sales_1_1  that contains the sales data for department 1
# o store 1
sales_1_1 = sales[(sales['department'] == 1) & (sales['store'] == 1)]

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date', ascending = True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

####################################################
# Counting -----------------------------------------
####################################################
# .drop_duplicates(subset = "") - removes duplicates from the colunms informed 
# in the subset argument
# .value_counts(sort = , normalize = ) - counts the number of times each element apear in a specific
# column. Use the sort argument to sort the count. The normalize argument can be
# used to turn the counts into proportions of the total

# Dropping duplicates
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset = ['store', 'type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset = ['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset = 'date')

# Print date col of holiday_dates
print(holiday_dates['date'])

# Counting catergrical variables
# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize = True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort = True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort = True, 
normalize = True)
print(dept_props_sorted)

####################################################
# Grouped summary statistics ------------------------------
####################################################
# .groupby()
# What percent of sales occurred at each store type?
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# About 91% of sales occurred in stores if type A; 9% in stores of type B, and 
# there are no records for stores of type C

# Calculation with .groupby()
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

# Multiple grouped summaries
# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)

# The minimum weekly_sales is negative because some stores had more returns than 
# sales

####################################################
# Pivot tables ------------------------------
####################################################
# .pivot_table(values =, index =, aggfunc =, columns =,  fill_value =, margins =) - 
# summarizes the column provided in the values
# argument and groups by the column provided in the index argument. By default,
# pivot_table takes the mean value for each group. Use aggfunc argument to pass it
# a different function or list of function. To group by two different variables,
# pass a second variable name into the columns argument. Use fill_values = 0 to 
# get all NaNsfilled with zeros. If we set the margins = True, the last row and 
# last columns of the pivot table will contain the mean of all the values in the
# column or row, not including the missing values that were filled in with zeros

# Pivoting on one variable 
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values = 'weekly_sales', index = 'type')

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values = 'weekly_sales', index = 'type', aggfunc = [np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values = 'weekly_sales', columns = 'is_holiday', index = 'type')

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Fill in missing values and sum values with pivot tables
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values = 'weekly_sales', index = 'department', columns = 'type', fill_value = 0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", margins = True, aggfunc = sum, fill_value = 0))
