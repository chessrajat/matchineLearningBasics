import matplotlib.pyplot as plt

# LinePlot
# plot(x,y) is used to draw a line plot

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set(title="Avg. Daily Temperature in Jan 2018",
       xlabel="Day", ylabel="Temperature",
       xlim=(0,30),ylim=(25,35))
days = [1,5,8,12,15,19,22,26,29]
temp = [29.3, 30.1, 30.4, 31.5, 32.3, 32.6, 31.8, 32.4, 32.7]
location2_temp = [26.4, 26.8, 26.1, 26.4, 27.5, 27.3, 26.9, 26.8, 27.0]
# ax.plot(days, temp, marker='o')
# # plotting multiple lines
# ax.plot(days,location2_temp, marker='o')
# plt.show()



# Common parameters of plot function

# color: Sets the color of the line.
#
# linestyle: Sets the line style, e.g., solid, dashed, etc.
#
# linewidth: Sets the thickness of a line.
#
# marker: Chooses a marker for data points, e.g., circle, triangle, etc.
#
# markersize: Sets the size of the chosen marker.
#
# label: Names the line, which will come in legend.

# Scatter plots

# Scatter Plot is used for showing how one variable is related with another.
# scatter function is used for drawing scatter plots.

# ax.scatter(days, temp)
# plt.show()

# c: Sets color of markers.
#
# s: Sets size of markers.
#
# marker: Selects a marker. e.g: circle, triangle, etc
#
# edgecolor: Sets the color of lines on edges of markers.
