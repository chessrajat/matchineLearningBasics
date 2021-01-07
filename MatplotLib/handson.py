import matplotlib.pyplot as plt
import numpy as np

# first figure
# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111)
# t = [5, 10, 15, 20, 25]
# d = [25, 50, 75, 100, 125]
# ax.set(title='Time vs Distance Covered',
#       xlabel='time (seconds)', ylabel='distance (meters)',
#        xlim=(0,30), ylim=(0,130))
# plt.plot(d,t,label="d = 5t")
# plt.legend()
# plt.show()

# scatter plots
# fig = plt.figure(figsize=(12,3))
# ax = fig.add_subplot(111)
# t = np.linspace(0.0,2.0,200)
# v = np.sin(2.5*np.pi*t)
# ax.set(title="Sine wave",
#        xlabel="Time (seconds)", ylabel="Voltage (mV)",
#        xlim=(0,2), ylim=(-1,1))
# ticks = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8,2.0]
# ax.tick_params(axis="both",which="major")
# ax.set_xticks(ticks)
# ax.set_yticks([-1,0,1])
# # adding a grid
# plt.grid(which="major",linestyle="--")
# plt.plot(t,v,label="sin(t)", color="red")
# plt.legend()
# plt.show()


t = np.arange(0.0, 5.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(2,1,)
plt.suptitle("Sin(2*pi*x)")



