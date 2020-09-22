# --------------------------------------------------- 
# Intermediate Python - Loops 
# 22 set 2020 
# VNTBJR 
# --------------------------------------------------- 
#
# Load packages
library(reticulate)

# while loop  -------------------------------------------
# Basic while loop
# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
  print("correcting...")
  offset = offset - 1
  print(offset)
quit()

# Add conditionals
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1
    print(offset)
quit()

######################################################################
# for loop  -------------------------------------------
# Loop over a list
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas :
  print(area)
quit()

# Indexes and values
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))
quit()

# Indexes and values (2)
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))
quit()

# Loop over list of lists
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room, area in house :
  print("the " + str(room) + " is " + str(area) + " sqm")
quit()

######################################################################
# Loop Data Structures Part 1  -------------------------------------------
# Loop over dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items() :
  print("the capital of " + str(key) + " is " + str(value))
quit()

# Loop over Numpy array
# Import numpy as np
import numpy as np
import pandas as pd

# Load data
mlb = pd.read_csv("Datasets/MLB.csv", sep = ",")

# Create data for the exercise
np_height = np.array(mlb[["Height"]])
np_weight = np.array(mlb[["Weight"]])

np_baseball = []
for height in np.nditer(np_height) :
  for weight in np.nditer(np_weight) :
    np_baseball.append([height, weight])
quit()
np_baseball = np.array(np_baseball)
type(np_baseball)

# For loop over np_height
for height in np.nditer(np_height) : 
  print(str(height) + " inches")
quit()

# For loop over np_baseball
for hw in np.nditer(np_baseball) :
  print(hw)
quit()
 
######################################################################
# Loop Data Structures Part 2  -------------------------------------------
# Loop over DataFrame (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('Datasets/Cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
  print(lab)
  print(row)
quit()

# Loop over DataFrame (2)
# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ": " + str(row["cars_per_cap"]))
quit()

# Add column (1)
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
  cars.loc[lab, "COUNTRY"] = row["country"].upper()
quit()

# Print cars
print(cars)

# Add column (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('Datasets/Cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)
 
######################################################################
