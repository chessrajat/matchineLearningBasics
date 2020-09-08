# you have been hired as a consultant to a startup that is running a targetted marketing ads on facebook.
# The company want to analyze customer behaviour by predicting which customer clicks on the advertisement

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns


training_data = pd.read_csv("Facebook_Ads.csv", encoding="ISO-8859-1")

# checking if there is any nan value
# print(training_data["Clicked"].isnull().values.any())

training_data.drop(["Names","emails","Country"],inplace=True, axis=1)


X = training_data.drop("Clicked",axis=1).values
Y = training_data["Clicked"].values


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# scaling the input still don't understand yet
sc = StandardScaler()
X = sc.fit_transform(X)



xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.2,random_state=0)
classifier = LogisticRegression(random_state=0)
classifier.fit(xtrain,ytrain)


ypredict = classifier.predict(xtest)

# cm = confusion_matrix(ytest,ypredict)
# sns.heatmap(cm,annot=True,fmt='d')
# plt.show()

# visualize Training and testing dataset in a scatter plot

X_set, y_set = xtest, ytest
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.70, cmap = ListedColormap(('magenta', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('magenta', 'blue'))(i), label = j)
plt.title('Facebook Ad: Customer Click Prediction (Training set)')
plt.xlabel('Time Spent on Site')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()



