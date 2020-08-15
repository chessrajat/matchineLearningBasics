import pandas as pd
import numpy as np

# creating a series
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data,index=["s1","s2","s3","s4","s5"]) # labelling the index
# print(ser.dtype)

# Create another series named heights_B from a 1-D numpy array of 5 elements derived
# from the normal distribution of mean 170.0 and standard deviation 25.0.
np.random.seed(100)
heights_B = np.random.normal(170.0,25.0,5)
weight_B = np.random.normal(75.0,12.0,5)


s = pd.Series([89.2, 76.4, 98.2, 75.9], index=list('abcd'))


s1 = pd.Series([0, 1, 2, 3])
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5])
d = pd.concat([s1, s2, s3], axis=1)

s4 = pd.Series([9.2, 'hello', 89])
s5 = pd.Series([89.2, 76.4, 98.2, 75.9], index=list('abcd'))
print('b' in s5)




