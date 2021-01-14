# predict wheather any body have survived the titanic based on there features.
# eg:- age,class
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the dataset
training_set = pd.read_csv("Train_Titanic.csv")

# visualize the data set

survived = training_set[training_set['Survived'] == 1]
not_survived = training_set[training_set["Survived"] == 0]
# print("Total samples = ", len(training_set))
# print("survived passengers = ", len(survived))
# print("not survived passengers = ", len(not_survived))
percent_survived = (len(survived) / len(training_set)) * 100
# print("survived percent = ", percent_survived)

# using sns
plt.figure()
# sns.countplot(x="Pclass",data=training_set)
# sns.countplot(x="Survived",data=training_set)
# sns.countplot(x="Embarked",hue="Survived",color="red",data=training_set)

# hue to show the survived data in respect to x
# sns.countplot(x="SibSp",hue="Survived",color="red",data=training_set)
# sns.countplot(x="Sex",data=training_set)
# sns.countplot(x="Sex",hue="Survived",color="red",data=training_set)

# plt.hist(training_set["Fare"])

# Training/Data Cleaning

# check training samples with NAN

# sns.heatmap(training_set.isnull(),yticklabels=False,cbar=False,cmap="Blues")
# cmap = colormap

# new_training_set = training_set.drop("Cabin",axis=1,inplace=False)
# inplace = False , prevent from altering the original values

training_set.drop(["Cabin", "Name", "Ticket", "Embarked", "PassengerId"], axis=1, inplace=True)


# sns.heatmap(training_set.isnull(),yticklabels=False,cbar=False,cmap="Blues")

# box plot helps to find the average age according to sex
# sns.boxplot(x="Sex", y="Age", data=training_set)


# filling the nan age with the average age
def fill_age(data):
    age = data[0]
    sex = data[1]
    if pd.isnull(age):
        if sex == "male":
            return 29
        else:
            return 25
    else:
        return age


# filtering the data according to a function
training_set["Age"] = training_set[["Age", "Sex"]].apply(fill_age, axis=1)
# sns.heatmap(training_set.isnull(),yticklabels=False,cbar=False,cmap="Blues")

# get_dummies used to convert category into indicators like 1 and 0
male = pd.get_dummies(training_set["Sex"], drop_first=True)
training_set.drop("Sex", inplace=True, axis=1)
# adding a new column in dataframe
training_set = pd.concat([training_set, male], axis=1)

# Model Training
X = training_set.drop("Survived", axis=1).values
Y = training_set["Survived"].values

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# just to split the data in training and testing
# X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

# creating an object of the class and just calling the fit method
classifier = LogisticRegression(random_state=3)
classifier.fit(X, Y)

# checking the trained model prediction
# y_predict = classifier.predict(X_test)

# creating confusion matrix to check the results from the data
# cm = confusion_matrix(Y_test,y_predict)
# plotting it on the chart
# sns.heatmap(cm,annot=True,fmt='d')
# plt.show()

from sklearn.metrics import classification_report


# print(classification_report(Y_test,y_predict))



def test_classify(x_test):
    y_predict = classifier.predict(x_test)
    print(y_predict)
    sns.heatmap(y_predict)
    plt.show()




