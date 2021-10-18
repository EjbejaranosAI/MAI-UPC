from sklearn import datasets

import numpy as np

from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
#split it in features and leabels
x= iris.data
y = iris.target
print(x.shape)






print(y.shape)


#hours of study vs good/bad grades
#10 different students
#train with 8 students
#predict with the remaining 2
#level of accuracy

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


#Knn_classifier
import panda as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import labelEncoder