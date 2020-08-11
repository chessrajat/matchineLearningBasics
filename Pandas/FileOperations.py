import numpy as np
import pandas as pd

df = pd.read_csv("housing.csv")
# df.rename(columns={"longitude":"long"},inplace=True)
print(df.columns)

# to_csv is used to write the data frame to a csv file
# index_col=0 , when reading or writing , to remove the 0,1,2 natural index

# The Same way we can read data into a dataframe from
#     html
#     csv
#     json
#     sql
#     excel

# reading with mysql
