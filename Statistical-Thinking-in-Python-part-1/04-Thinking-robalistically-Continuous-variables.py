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




# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
