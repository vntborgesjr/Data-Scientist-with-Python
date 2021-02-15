# --------------------------------------------------- 
# Statistical Thinking in Python (Part 1) - Thinking probalistically -- Continuous variables 
# 11 fev 2021 
# VNTBJR 
# --------------------------------------------------- 
#
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
# Probability density functions ------------------------------------------------
# Probability density function (PDF) - it is a mathematical description of
# the relative likelihood of observing a value of a continuos variable
# Areas under the de PDF gives the probabilities.
# Normal cumulative distribution function (Normal CDF) - it gives the 
# probability the measured speed of light will be less than the value 
# on the x-axis

# Introduction to the normal distribution ------------------------------------------------
# Normal distribution - it describes a continuous variable whose PDF
# has a single and simmetric peak.
# The normal distribution is parametrized by two parameters, the mean
# and the standard deviation.The mean determines where the center of
# the peak is. The standard deviation is measure of how wide the peak is,
# or how spread out the data are.

# The Normal PDF
# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20, 1, 100000)
samples_std3 = np.random.normal(20, 3, 100000)
samples_std10 = np.random.normal(20, 10, 100000)

# Make histograms
_ = plt.hist(samples_std1, bins = 100, density = True, histtype = 'step')
_ = plt.hist(samples_std3, bins = 100, density = True, histtype = 'step')
_ = plt.hist(samples_std10, bins = 100, density = True, histtype = 'step')

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
plt.clf()

# The Normal CDF
# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3)
x_std10, y_std10 = ecdf(samples_std10)

# Plot CDFs
_ = plt.plot(x_std1, y_std1, marker = '.', linestyle = 'none')
_ = plt.plot(x_std3, y_std3, marker = '.', linestyle = 'none')
_ = plt.plot(x_std10, y_std10, marker = '.', linestyle = 'none')

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()
plt.clf()

# Thee Normal distribution: Properties and warnings ------------------------------------------------
# Are the Belmont Stakes results Normally distributed?
# Compute mean and standard deviation: mu, sigma
mean = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)

# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mean, sigma, 10000)

# Get the CDF of the samples and of the data
x_theor, y_theor = ecdf(samples)
x, y = ecdf(belmont_no_outliers)

# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()

# What are the chances of a horse matching or beating Secretariat's
# record?
# Take a million samples out of the Normal distribution: samples
samples = np.random.normal(mu, sigma, 1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob = len(samples[samples >= 144])/len(samples)

# Print the result
print('Probability of besting Secretariat:', prob)

# The exponential distribution ------------------------------------------------
# The waiting time between arrivals of a Poisson process are Exponentially
# distributed. It has a single parameter: the mean waiting time.
# This distribution is not peaked. 
# If you have a story you can simulate it!
def successive_poisson(tau1, tau2, size = 1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2

# Distribution of no-hitters and cycles
# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764, 715, 100000)

# Make the histogram
_ = plt.hist(waiting_times, bins = 100, density = True, histtype = "step")


# Label axes
_ = plt.xlabel('waiting time')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
plt.clf()

# Plot the CDF
x_waiting_time, y_waiting_time = ecdf(waiting_time)
_ = plt.plot(x_waiting_time, y_waiting_time, marker = '.', linestyle = 'none')
_ = plt.ylabel('CDF')
_ = plt.xlabel('waiting time')
plt.show()
plt.clf()
