import pandas as pd
import numpy as np

# working with csv
height_A = pd.Series([176.2, 158.4, 167.6, 156.2,161.4] ,
                     index=["s1","s2","s3","s4","s5"])

weight_A = pd.Series([85.1, 90.2, 76.8, 80.4,78.9],
                     index=["s1","s2","s3","s4","s5"])

df_A = pd.DataFrame({"Student_height":height_A,"Student_weight":weight_A},
                    index=["s1","s2","s3","s4","s5"])
#
# print(df_A.to_csv("handson.csv"))

# --------------------------------------------------

# Handson with indexes

# date = pd.date_range(start="1-Sep-2017", end="15-Sep-2017")
# print(date[2])

# converting date string into datetime object

# datelist = ['14-Sep-2017', '9-Sep-2017']
#
# dates_to_be_searched = pd.to_datetime(datelist)
# output = dates_to_be_searched.isin(date)
# print(output)

# creating a multi index

# arraylist = [['classA']*5 + ['classB']*5, ['s1', 's2', 's3','s4', 's5']*2]
# mi_index = pd.MultiIndex.from_arrays(arraylist)
# print(mi_index)

# -------------------------------------------------------------------------

# Accessing elements in datastructure

# height_A = pd.Series([176.2, 158.4, 167.6, 156.2,161.4] ,
#                      index=["s1","s2","s3","s4","s5"])
# print(height_A[1])

# -------------------------------------------------------------------------


# Data Cleaning handson

# df_A.loc["s3"] = [np.nan,np.nan]
# df_A.loc["s5"][1] = np.nan
# df_A2 = df_A.dropna(how="any") # drop row with any nan
# # df_B = df_A.dropna(how="all") # drop row with all nan
# print(df_A2)

# -------------------------------------------------------------------------

# Data Aggregation

# df_A_filter1 = df_A.loc[(df_A["Student_height"]>160.0) &
#                            (df_A["Student_weight"]<80.0)]
# print(df_A_filter1)

# To select rows whose column value equals a scalar, some_value, use ==:
#
# df.loc[df['column_name'] == some_value]
# To select rows whose column value is in an iterable, some_values, use isin:
#
# df.loc[df['column_name'].isin(some_values)]
# Combine multiple conditions with &:
#
# df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]
# Note the parentheses. Due to Python's operator precedence rules, & binds more tightly than <= and >=.
# Thus, the parentheses in the last example are necessary. Without the parentheses
#
# df['column_name'] >= A & df['column_name'] <= B
# is parsed as
#
# df['column_name'] >= (A & df['column_name']) <= B
# which results in a Truth value of a Series is ambiguous error.
#
# To select rows whose column value does not equal some_value, use !=:
#
# df.loc[df['column_name'] != some_value]
# isin returns a boolean Series, so to select rows whose value is not in some_values, negate the boolean Series using ~:
#
# df.loc[~df['column_name'].isin(some_values)]

# --------------------------------------------------------------------------

# Data Merge Hands on

# gender = ['M', 'F', 'M', 'M', 'F']
# df_A["Gender"] = gender
#
# s = pd.Series([165.4, 82.7, 'F'],
#               index=['Student_height', 'Student_weight', 'Gender'],name="s6")
# df_AA = df_A.append(s)
# print(df_AA)

# nameid = pd.Series(range(101, 111))
# name = pd.Series(['person' + str(i) for i in range(1, 11)])
#
# master = pd.DataFrame({"nameid":nameid,"name":name})
# transaction = pd.DataFrame({'nameid':[108, 108, 108,103], 'product':['iPhone', 'Nokia', 'Micromax', 'Vivo']})
#
# mdf = master.merge(transaction,on="nameid",how="inner")
# print(mdf)












