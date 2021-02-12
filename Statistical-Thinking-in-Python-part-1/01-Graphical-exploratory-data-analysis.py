# --------------------------------------------------- 
# Statistical Thinking in Python (Part 1) - Graphical exploratory data analysis 
# 10 fev 2021 
# VNTBJR 
# --------------------------------------------------- 
#

######################################################################
# Plotting a histogram  -------------------------------------------
######################################################################
# Plotting a histogram of iris data
df = sns.load_dataset('iris')
versicolor_petal_length = df.petal_length[df['species'] == 'versicolor'].values

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Label axes
_ = plt.xlabel('Petal length (cm)')
_ = plt.ylabel('Count of lengths')

# Show histogram
plt.show()
plt.clf()

# Adjusting the number of bins in a histogram
# Import numpy
import numpy as np

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
_ = plt.hist(versicolor_petal_length, bins = n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()
plt.clf()

######################################################################
# Plot all of your data: Bee swarm plots  -------------------------------------------
######################################################################
# Bee sawrm plot
# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(y = 'petal_length', x = 'species', data = df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
plt.clf()

######################################################################
# Plot all of your data: ECDFs  -------------------------------------------
######################################################################
# Computing the ECDF
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y

# Plotting the ECDF
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

# Label the axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
plt.clf()

# Comparison of ECDFs
setosa_petal_length = df.petal_length[df['species'] == 'setosa'].values
virginica_petal_length = df.petal_length[df['species']  == 'virginica'].values
# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker = '.', linestyle = 'none')
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')
_ = plt.plot(x_virg, y_virg, marker = '.', linestyle = 'none')

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
