from scipy import stats
import numpy as np

s = [26, 15, 8, 44, 26, 13, 38, 24, 17, 29]

mean = np.mean(s)
print(mean)

median = np.median(s)
print(median)

mode = stats.mode(s)
print(mode)

print("25th percentile = {}".format(np.percentile(s,25)))
print("75th percentile = {}".format(np.percentile(s,75)))

inter_quartile_range = stats.iqr(s,interpolation="lower")
print(inter_quartile_range)

# skewness is the slope of the chart if high on left and low on right means positive skew
skewness = stats.skew(s)
print(skewness)

kurtosis = stats.kurtosis(s)
print(kurtosis)
