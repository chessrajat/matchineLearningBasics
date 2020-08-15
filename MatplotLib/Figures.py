import matplotlib.pyplot as plt

# change the size of the figure using figure size

# fig = plt.figure()
fig = plt.figure(figsize=(8, 6)) # 8 -> width , 6 -> height
# viewing the figure
# plt.show()

# axes can be added using the add_subplot()
# Hence, add_subplot(1, 1, 1) and add_subplot(111) are same.
# set method can be used on created axes, ax, to set various parameters such as xlabel, ylabel and title.
ax = fig.add_subplot(111)
print(type(ax))
ax.set(title='My First Plot',
      xlabel='X-Axis', ylabel='Y-Axis',
      xlim=(0, 5), ylim=(0,10))
# can also be done like this
# ax.set_title("My First Plot")
# ax.set_xlabel("X-Axis"); ax.set_ylabel('Y-Axis')
# ax.set_xlim([0,5]); ax.set_ylim([0,10])

# plot is one of the functions used for plotting data points.
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
# label can be used to give the value to the plot
plt.plot([10, 12, 14, 16], label="linear-growth")
plt.legend() # this is used to show the label on the plot
plt.show()


