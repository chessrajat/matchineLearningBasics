#n=9
#p=0.80
#k=6
from scipy import stats
import numpy as np

#binomial probability

probability=stats.binom.pmf(0,4,0.60)
print(probability)

#poisson distribution function
averagepass=10
probability=stats.poisson.pmf(15, averagepass)
print(probability)