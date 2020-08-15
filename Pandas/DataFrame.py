import pandas as pd
import numpy as np

height_A = [150.2,168.3,154,169,125]
weight_A = [52,56,60,62,48]
data = {"height_A":height_A,"weight_A":weight_A}
data_Frame = pd.DataFrame(data,index=['s1','s2','s3','s4','s5'])
# print(data_Frame.columns)

data1 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data1, columns=['a', 'b'])

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, columns=['a', 'b'])

df1 = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 43]}, index=['r1', 'r2', 'r3'])
df1.loc['r4'] = [67, 78]

df2 = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 43]}, index=['r1', 'r2', 'r3'])
print(df2)
# print(df2.loc[1])
# print(df2.iloc[1])
# print(df2.iloc["r2"])
print(df2[1])
