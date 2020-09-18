# --------------------------------------------------- 
# Introduction to Python - Phyton Basics 
# 18 set 2020 
# VNTBJR 
# --------------------------------------------------- 
#
# Load packages  -------------------------------------------
library(reticulate)

# The Python interface  -------------------------------------------
# Example, do not modify!
print(5 / 8)

# Print the sum of 7 and 10
print(7 + 10)

# Python as a calculator
# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)
 
######################################################################
# Variables & Types  -------------------------------------------
# Create a variable savings
savings = 100

# Print out savings
print(savings)

# Calculation with variables
# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print(result)

# Other variable types
# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

# Assign product of growth_multiplier and savings to year1
year1 = growth_multiplier * savings

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)

# Type conversion
# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + 
". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
print(pi_float)
 
######################################################################
