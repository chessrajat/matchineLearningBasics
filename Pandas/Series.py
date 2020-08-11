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
print(heights_B.mean())




