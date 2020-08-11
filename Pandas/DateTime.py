import pandas as pd

ufo = pd.read_csv("http://bit.ly/uforeports")
# print(ufo.dtypes)

# converting the time column to pandas datetime format

ufo["Time"]= pd.to_datetime(ufo.Time)
# print(ufo.Time.dt.hour)
# print(ufo.Time.dt.dayofyear)

ts = pd.to_datetime("1/2/1999")
# print(ts)
# print(ufo.loc[ufo.Time >= ts]) # comparing time