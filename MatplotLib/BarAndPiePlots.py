import matplotlib.pyplot as plt

# BarPlot
# Bar Plot is commonly used for comparing categories.
# bar and barh are used for plotting vertical and horizontal bar plots respectively.

# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111)
# ax.set(title='Avg. Quarterly Sales',
#       xlabel='Quarter', ylabel='Sales (in millions)')
# quarters = [1, 2, 3]
# sales_2017 = [25782, 35783, 36133]
# ax.bar(quarters, sales_2017, color="blue", width = 0.6)
# ax.set_xticks(quarters)
# ax.set_xticklabels(['Q1-2017', 'Q2-2017', 'Q3-2017'])
# plt.show()

# Pie Plot
# used to plot pie charts showing proportions

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set(title='Avg. Quarterly Sales')
sales_2017 = [25782, 35783, 36133]
quarters = ['Q1-2017', 'Q2-2017', 'Q3-2017']
ax.pie(sales_2017, labels=quarters, startangle=90, autopct='%1.1f%%')
plt.show()
