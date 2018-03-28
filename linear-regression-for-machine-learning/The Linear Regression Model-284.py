## 2. Introduction To The Data ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', sep='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]

data.info()

target = 'SalePrice'

## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn as sns

fig = plt.figure(figsize=(7, 15))

ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

ax1.scatter(train['Garage Area'], train['SalePrice'])
ax2.scatter(train['Gr Liv Area'], train['SalePrice'])
ax3.scatter(train['Overall Cond'], train['SalePrice'])
plt.show()

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X=train[['Gr Liv Area']], y=train['SalePrice'])

a1 = lr.coef_
a0 = lr.intercept_

print(a0, a1)

## 6. Making Predictions ##

import numpy as np

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])
yhat_train = lr.predict(train[['Gr Liv Area']])
yhat_test = lr.predict(test[['Gr Liv Area']])

train_rmse = np.sqrt(np.sum(np.power(yhat_train - train['SalePrice'], 2)) / len(train['SalePrice']))

test_rmse = np.sqrt(np.sum(np.power(yhat_test - test['SalePrice'], 2)) / len(test['SalePrice']))

## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']

lr = LinearRegression()
lr.fit(train[cols], train['SalePrice'])
yhat_train = lr.predict(train[cols])
yhat_test = lr.predict(test[cols])

train_rmse_2 = np.sqrt(np.sum(np.power(yhat_train - train['SalePrice'], 2)) / len(train['SalePrice']))

test_rmse_2 = np.sqrt(np.sum(np.power(yhat_test - test['SalePrice'], 2)) / len(test['SalePrice']))