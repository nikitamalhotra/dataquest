## 1. Introduction ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import inv

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X = train[features]
y = train['SalePrice']

X_mat = X.as_matrix()
y_mat = y.as_matrix()

a = np.dot(np.dot(inv(np.dot(X_mat.T, X_mat)), X_mat.T), y_mat)

print(X_mat.shape)
print(y_mat.shape)
print(a.shape)