import numpy as np
import pandas as pd

# Data Merging refers to combining data stored in multiple entities based on a specific criteria.
# pandas provide utility like merge to merge two data frames
data1 = {"HPI": [80,85,88,85],
         "GDP":[50,55,65,55]}
data2 = {"HPI": [80,85,88,85],
         "GDP":[50,55,65,53]}
year = [2001,2002,2003,2004]


df1 = pd.DataFrame(data1,index=year)
df2 = pd.DataFrame(data2, index=year)

merged = pd.merge(df1,df2,on="HPI") # we can also provide list in on argument

s1 = pd.Series([0, 1, 2, 3])
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5])
d = pd.concat([s1, s2, s3], axis=1)
print(d.shape)

