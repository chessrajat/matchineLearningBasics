import numpy as np
from scipy import stats

# Hypothesis Testing is a methodology for evaluating if a claim is acceptable or not, based on data.
# steps in hypothesis testing
# Define the null hypothesis and the alternative hypothesis.
# Select a test statistics whose probability distribution function can be found under the null hypothesis.
# Collect data.
# Compute the test statistics from the data and calculate its p-value under the null hypothesis.
# Null hypothesis is rejected if the p-value is lower than predetermined significance value.
#
# choosing the test statistics
# stats.ttest_1samp: Tests if the mean of a population is a given value.
# stats.ttest_ind: Tests if the means of two independent samples are equal.
# stats.ttest_rel: Tests if the means of two paired samples are equal.

# mu, sigma = 0.8, 0.5
# X = stats.norm(mu, sigma)
#
# # Deriving a sample
# n = 100
# X_sample = X.rvs(n)
#
# # Computing test statistic
# t, p = stats.ttest_1samp(X_sample, 1.0)
# print(t, p)

# X1 = stats.norm(0.25, 1.0)
# X2 = stats.norm(0.50, 1.0)
#
# X1_sample = X1.rvs(100)
# X2_sample = X2.rvs(100)
#
# t, p = stats.ttest_ind(X1_sample, X2_sample)
# print(t, p)


# s1 = [45, 38, 52, 48, 25, 39, 51, 46, 55, 46]
# s2 = [34, 22, 15, 27, 37, 41, 24, 19, 26, 36]
#
# t,p = stats.ttest_ind(s1,s2)
# print(t)
# print(p)

s1 = [12, 7, 3, 11, 8, 5, 14, 7, 9, 10]
s2 = [8, 7, 4, 14, 6, 7, 12, 5, 5, 8]

t,p = stats.ttest_rel(s1,s2)
print(t)
print(p)