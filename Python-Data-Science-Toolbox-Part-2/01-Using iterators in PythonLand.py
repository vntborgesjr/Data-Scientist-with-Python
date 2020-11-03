####################################################
# Python Data Science Toolbox (Part 2) - Using iterators in PythonLand
# 02 Nov 2020
# VNTBJR
####################################################
#
# Load packages
library(reticulate)

####################################################
# Introduction to iterators ------------------------------
####################################################
# An iterable is an object that has an associated iter method. Once this 
# iter method is applyed to an iterable, an iterator object is created.
# An iterator is defined as an object tha as an associated next method
# that produces the consecutive values.
# To create an iterator from an iterable all we need to do is to use the 
# fucntion iter and pass it the iterable. Once we have the itearator 
# defined, we pass it to the function next and this returns the first 
# value.
word = 'data' # iterable
it = iter(word) # iterator
next(it)
word = 'data'
print(*it)

# Iterators vs Iterables
flash1 = ['jay garrick', 'barry allen', 'wally west', 'bart allen'] 
# Iterable
flash2 = iter(flash1) # Iterator
next(flash2)

# Iterating over iterables (1)
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop

for person in flash:
  print(person)
quit()
# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

# Iterate over iterables (2)
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values

for num in range(3):
  print(num)
quit()
# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 **100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

# Iterators as functions arguments
# Create a range object: values
values = range(10, 21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)

####################################################
# Playing with iterators ------------------------------
####################################################
#
# enumerate() is a function that takes any iterable as arguments, such as
# a list, and returns a special enumerate object, which consists of pairs
# containing the elements of the original iterable, along with their 
# index within the iterable.
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers) 
print(type(e))
e_list = list(e)
print(e_list)
print(*e)

# zip() accepts an arbitrary number of iterables and returns an iterator
# tuples.
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)
print(type(z))
z_list = list(z)
print(z_list)
print(*z)

# Using enumerate
# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)
quit()
# Change the start index
for index2, value2 in enumerate(mutants, start = 1):
    print(index2, value2)
quit()

# Using zip
# Create three lists: mutants, aliases, and powers
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']
aliases = ['prof x', 
            'iceman', 
            'nightcrawler', 
            'magneto', 
            'shadowcat']
powers = ['telepathy', 
          'thermokinesis', 
          'teleportation', 
          'magnetokinesis', 
          'intangibility']
# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
quit()

# Using * and zip to 'unzip'
# Create two tupples called: mutants and powers
mutants = ('charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde')
powers = ('telepathy', 
          'thermokinesis', 
          'teleportation', 
          'magnetokinesis', 
          'intangibility')

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

####################################################
# Using iterators to load large files into memory ------------------------------
####################################################
#
# Processing large amounts of Twitter data
import pandas as pd
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('Datasets/tweets.csv', chunksize =  10):
    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
quit()
# Print the populated dictionary
print(counts_dict)

# Extracting information for large amounts of Twitter data
# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}
    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):
        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    # Return counts_dict
    return counts_dict
quit()
# Call count_entries(): result_counts
result_counts = count_entries('Datasets/tweets.csv', c_size = 10, colname = 'lang')

# Print result_counts
print(result_counts)
