import Main
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

testing_data = pd.read_csv("Test_Titanic.csv")

testing_data.drop(["Cabin", "Name", "Ticket", "Embarked", "PassengerId"], axis=1, inplace=True)
testing_data["Age"] = testing_data[["Age","Sex"]].apply(Main.fill_age,axis=1)

# checking null values
# sns.heatmap(testing_data.isnull())
# plt.show()

male = pd.get_dummies(testing_data["Sex"], drop_first=True)
testing_data.drop("Sex", inplace=True, axis=1)
testing_data = pd.concat([testing_data,male],axis=1)
xtest = testing_data.values
Main.test_classify(xtest)
print(testing_data.columns)



