import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

print(plt.style.available)

# using a style

plt.style.use("ggplot")

# matplotlib uses all the settings specified in matplotlibrc file.
#
# These settings are known as rc settings or rc parameters.
#
# For customization, rc settings can be altered in the file or interactively.
#
# The location of active matplotlibrc file used by matplotlib can be found with below expression.


fig = plt.figure()

axes1 = plt.subplot(2, 2, (1,3), title='Plot1')
axes2 = plt.subplot(2, 2, 2, title='Plot2')
axes3 = plt.subplot(2, 2, 4, title='Plot3')
plt.show()