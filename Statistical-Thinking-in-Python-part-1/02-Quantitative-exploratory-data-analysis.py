# --------------------------------------------------- 
# Statistical Thinking in Python (Part 1) - Quantitative exploratory data analysis
# 10 fev 2021 
# VNTBJR 
# --------------------------------------------------- 
#

######################################################################
# Introduction to summary statistics: The sample mean and median  -------------------------------------------
######################################################################
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
df = sns.load_dataset('iris')
versicolor_petal_length = df.petal_length[df['species'] == 'versicolor'].values

# Computing means and medians
# Compute the mean: mean_length_vers
mean_length_vers = np.mean(versicolor_petal_length)
median_length_vers = np.median(versicolor_petal_length)

# Print the result with some nice formatting
print('I. versicolor mean:', mean_length_vers, 'cm')
print('I. versicolor median:', median_length_vers, 'cm')

######################################################################
# Percentiles, outliers, and box plots  -------------------------------------------
######################################################################

# Computing percentiles
# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)

# Comparing perceentiles to ECDF
# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker = 'D', color = 'red',
         linestyle = 'none')

# Show the plot
plt.show()
plt.clf()

# Box-and-whisker plot
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x = 'species', y = 'petal_length', data = df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('peltal length (cm)')

# Show the plot
plt.show()
plt.clf()

######################################################################
# Variance and standard deviation  -------------------------------------------
######################################################################
# Computing the variance
# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit, variance_np)

# The standard deviation and the variance
# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))

######################################################################
# Covariance and the Pearason correlation coefficient  -------------------------------------------
######################################################################
# Covariance summarize how one variable varies in relation to another
# It measure how two quantities vary together
# The covariace is the mean of the product of the difference
# between observations and their respective means
# The Pearson correlation coefficient is a dimensionless measure
# of how two variables depend on each other
# We divide the covariance by the product of the standard deviation
# of x and y variables
# It is the comparison of the variability in the data due to 
# codependence (the covariance) to the variability inherent to 
# each variable indpendently (their standard deviations)

# Scatter plots
versicolor_petal_width = df.petal_width[df['species'] == 'versicolor'].values
# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker = '.', linestyle = 'none')

# Label the axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('petal width (cm)')

# Show the result
plt.show()
plt.clf()

# Computing the covariance
# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0, 1]

# Print the length/width covariance
print(petal_cov)

# Computing the Pearson correlation coefficient
def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)
