# --------------------------------------------------- 
# Intermediate Python - Case Study: Hacker Statistics 
# 22 set 2020 
# VNTBJR 
# --------------------------------------------------- 
#
# Load packages
library(reticulate)

# Hypotetical sitiuation  -------------------------------------------

# You're walkinng up the emopire state building to DataCamp HeadQuarters and you're 
# playing a game with a friend. You throw a dice 100 times. If it's 1 or 2 you'll
# go one step down. If it's 3, 4, or 5 you'll go one step up. If you throw a 6,
# you'll throw the dice again and will walk up the resulting number of steps.
# You can not go bellow step 0. And also, you admit that you're a bit clumsy and 
# have a chance of 0.1% of falling down the stairs when you make a move. It means
# that you have to start again from step 0.
# With all this in mind you bet with your friend that you'll reach 60 steps high.
# What is the chance that you will win this bet?

# Solutions:
# 1 - Analyticaly
# 2 - Simulate the process

# Random Numbers  -------------------------------------------
# Random float
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Roll the dice
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(low = 1, high = 7))

# Use randint() again
print(np.random.randint(low = 1, high = 7))

# Detremine your next move
# Numpy is imported, seed is set
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(low = 1, high = 7) 

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)
quit()

# Print out dice and step
print(dice)
print(step)

# The next step
# Numpy is imported, seed is set
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]
    # Roll the dice
    dice = np.random.randint(1,7)
    # Determine next step
    if dice <= 2 :
        step = step - 1
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1,7)
    # append next_step to random_walk
    random_walk.append(step)
quit()
# Print random_walk
print(random_walk)

# How low can you go?
# Numpy is imported, seed is set
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
quit()
print(random_walk)

# Visualize the walk
# Numpy is imported, seed is set
np.random.seed(123)

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
quit()
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
plt.clf()
 
######################################################################
# Distribution  -------------------------------------------
# Simulationg multiple walks
# Numpy is imported; seed is set
np.random.seed(123)

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :
    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    # Append random_walk to all_walks
    all_walks.append(random_walk)
quit()
# Print all_walks
print(all_walks)

# Visualize all walks
# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
plt.clf()

# Implement clumsiness
# numpy and matplotlib imported, seed set
np.random.seed(123)
# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
quit()
# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
plt.clf()

# Plot the distribution
# numpy and matplotlib imported, seed set
np.random.seed(123)
# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
quit()
# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# Calculate the odds

print(sum(ends >= 60) / 500)

# The odds are 78.4%
