import numpy as np
from scipy import stats

# print(np.random.choice([11, 22, 33], 2, replace=True))

# np.random.seed(1)
# x = stats.norm.rvs(loc=32,scale=4.5,size=100)
#
# sample_mean = np.mean(x)
# ads_diff= abs(sample_mean - 32)
# print(ads_diff)


# Simulate a random experiment of tossing a coin 10000 times, and determine the count of Heads returned.

n,p = 1,0.5
np.random.seed(1)
x = stats.binom.rvs(n,p,size=10000)
y = np.bincount(x)
head = y[0]
tails = y[1]
print(head)


