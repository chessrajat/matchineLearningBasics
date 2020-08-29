import matplotlib.pyplot as plt
import numpy as np

# Histogram
# hist function is used to plot a histogram.


np.random.seed(100)
x = 60 + 10*np.random.randn(1000)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set(title="Distribution of Student's Percentage",
      ylabel='Count', xlabel='Percentage')
print(ax.hist(x))
# plt.show()

# BoxPlots
# Box plots are used to compare distributions.
# Box plots can also be used to detect outliers.


# np.random.seed(100)
# x = 50 + 10*np.random.randn(1000)
# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111)
# ax.set(title="Box plot of Student's Percentage",
#       xlabel='Class', ylabel='Percentage')
# ax.boxplot(x)
# plt.show()
