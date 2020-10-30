####################################################
# Data Manipulation with Pandas - Slicing and Indexing
# 26 Out 2020
# VNTBJR
####################################################
# 
# Load packages
library(reticulate)

####################################################
# Explicit indexes ------------------------------
####################################################
# .set_index() - moves a column from the body of the DataFrame to the index
# .reset_index(drop =) - undo what .set_index() did. drop argument allows to 
# dsicard an index
# .sort_index(level =, ascending =) - sorts by index values.By default, it sorts all index levels  
# from outer to inner, in ascending order. The sorting can be controled by passing
# lists to the level and ascending arguments.

# Settindg and removing indexes 
import pandas as pd 
temperatures = pd.read_csv('Datasets/temperatures.csv', sep = ',')

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop = True))

# Subsetting with .loc[]
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Setting multi-level indexes
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sorting by index values
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level = 'city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level = ['country', 'city'], ascending = [True, False]))

####################################################
# Slicing and subsetting with .loc and.iloc ------------------------------
####################################################
# Remember that you can only slice a DataFrame by index if the index is sorted
# To slice at the outer leel, first and lasta can be a string 
# To slice at inner levels, first and lasta should be tuples
# If you passa a single slice to.loc[], it will slice the rows

# Slincing index values
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc['Lahore':'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia', 'Moscow')])

# Slicing in both directions
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c'])

# Slicing time series
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-01')]
print(temperatures_bool)

# Set date as an index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2012'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08':'2011-03'])

# Subseting by row/column number
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])

####################################################
# Working with pivot tables ------------------------------
####################################################
# .mean(axis = ['index', 'column']) - in pivot tables it takes the mean 'across the 
# rows' for 'index', and 'across the columns' for columns

# Pivot temperature by city and year
from datetime import datetime
date = []
for index, date_str in temperatures['date'].iteritems():
    # Convert each date to a datetime object: date_dt
    date.append(datetime.strptime(date_str, '%Y-%m-%d'))
quit()    
temperatures['date'] = date

# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values = 'avg_temp_c', index = ['country', 'city'], columns = 'year')

# See the result
print(temp_by_country_city_vs_year)

# Subsetting pivot tables
# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc['Egypt':'India'])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi')])

# Subset in both directions at once
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi'), '2005':'2010'])

# Calculationg on a pivot table
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis = 'index')

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year.iloc[:] == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = 'columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city.iloc[:] == mean_temp_by_city.min()])

####################################################
  
