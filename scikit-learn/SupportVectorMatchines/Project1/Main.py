# cancer diagnosis procedure

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importing data
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

# print(cancer.keys()) # viewing the data available in dataset
# print(cancer["DESCR"])  # description about the dataset
# print(cancer["target_names"]) # target result
# print(cancer["feature_names"])  # all the columns

# converting this data into dataframe
# noinspection PyTypeChecker
cancer_df = pd.DataFrame(np.c_[cancer["data"], cancer["target"]],
                         columns=np.append(cancer["feature_names"],"target"))

# visualize the data
# sns.pairplot(cancer_df, hue="target",
#              vars=["mean radius","mean texture","mean area","mean perimeter","mean smoothness"])
# we visualize the data mainly to find out which algo to use for classification


# Training data
X = cancer_df.drop("target",axis=1).values
Y = cancer_df["target"].values

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix

xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.25)

svc_model = SVC()
svc_model.fit(xtrain,ytrain)

# Evaluate the model
# y_predict = svc_model.predict(xtest)

# Improving the model
# Normalising the data

min_train = xtrain.min()

range_train = (xtrain - min_train).max()
xtrain_scaled = (xtrain - min_train)/range_train







