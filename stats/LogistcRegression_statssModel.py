import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Download the popular iris data set (containing data of 3 species) from R repository.
# Subset the data of only two species.
# Perform transformations, if required.
# Define a patsy formula and create a model using logit.
# Fit the model with supplied data.
# View summary of the model.

df = sm.datasets.get_rdataset("iris").data
# df.info()
# df.Species.unique()

# filtering for two species

# df_subset = df[(df.Species == "versicolor") | (df.Species == "virginica")].copy()
# print(df_subset.Species.unique())\
#
# df_subset.Species = df_subset.Species.map({"versicolor": 1, "virginica": 0})
#
# df_subset.rename(columns={"Sepal.Length": "Sepal_Length", "Sepal.Width": "Sepal_Width",
#                           "Petal.Length": "Petal_Length", "Petal.Width": "Petal_Width"}, inplace=True)
# # creating a model
# model = smf.logit("Species ~ Petal_Length + Petal_Width",data=df_subset)
# result = model.fit()
# # print(result.summary())
#
# # predicting response values
#
# df_new = pd.DataFrame({"Petal_Length": np.random.randn(20)*0.5 + 5,
#                        "Petal_Width": np.random.randn(20)*0.5 + 1.7})
# df_new["P-Species"] = result.predict(df_new)
# df_new["P-Species"].head(3)

dataset = sm.datasets.get_rdataset("biopsy",package="MASS").data
dataset.rename(columns={"class":"Class"},inplace=True)
dataset.Class = dataset.Class.map({"benign":0, "malignant":1})
model = smf.logit("Class ~ V1",data=dataset)
result = model.fit()

print(result.prsquared)