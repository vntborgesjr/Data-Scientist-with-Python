# -------------------------------------------------
# Data Manipulation with pandas - Transforming Data
# 29 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages
library(reticulate)

#######################################################
# Introducing DataFrames ------------------------------------------------
#######################################################
# Eploring a DateFrame: 
# .head() - returns only the first rows of a DataFrame
# .info() - display the names of columns, the data types they contain, and 
# whether they have missing values
# .shape - contains a tuple that holds the number of rows followed by the number
# of columns
# .describe() - computes soe summary statistics for numerical columns, like mean 
# and median. Count is the number of non-missing values in each column
# Components of DataFrames:
# .value = contains the data values in a 2-dimensional NumPy array
# .columns - contains column names
# .index - contains row numbers or row names 

# Inspecting a DataFrame
# Import packages and load data
import pandas as pd
homelessness = pd.read_csv('Datasets/homelessness.csv', sep = ',')

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

# Parts of a DataFrame
# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

#######################################################
# Sorting and subsetting ------------------------------------------------
#######################################################
# .sort_values() - sort rows according to one or more specific columns
# DataFrame['column name'] - subset just one column
# DataFrame[['column name1', 'column name2']] - subset multiple columns
# .isin() - filter on mltiple values of categorical variable

# Sorting rows
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending = False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], 
ascending = [True, False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Subsetting columns
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[['state', 'family_members']]

# Print the head of the result
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals', 'state']]

# Print the head of the result
print(ind_state.head())

# Subsetting rows
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region'] == 'Mountain']

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & 
(homelessness['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)

# Subseting rows by categorical variables
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[homelessness['region'].isin(['South Atlantic',
'Mid-Atlantic'])]

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)

#######################################################
# New columns ------------------------------------------------
#######################################################
# Adding new columns
# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_individuals col as proportion of individuals
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

# See the result
print(homelessness)

# Combo-attack!
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop'] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending = False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)

#######################################################
