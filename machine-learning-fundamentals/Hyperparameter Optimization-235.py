## 1. Recap ##

import pandas as pd

train_df = pd.read_csv('dc_airbnb_train.csv')
test_df = pd.read_csv('dc_airbnb_test.csv')

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

cols = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

hyper_params = [1, 2, 3, 4, 5]
mse_values = []

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm='brute')
    knn.fit(train_df[cols], train_df['price'])
    prediction = knn.predict(test_df[cols])
    
    mse_values.append(mean_squared_error(test_df['price'], prediction))

print(mse_values)

## 3. Expanding grid search ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

cols = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

hyper_params = list(range(1, 21))
mse_values = []

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm='brute')
    knn.fit(train_df[cols], train_df['price'])
    prediction = knn.predict(test_df[cols])
    
    mse_values.append(mean_squared_error(test_df['price'], prediction))

print(mse_values)

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(hyper_params, mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

hyper_params = [x for x in range(1,21)]
mse_values = list()

cols = [col for col in train_df.columns if col != 'price']

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm='brute')
    knn.fit(train_df[cols], train_df['price'])
    prediction = knn.predict(test_df[cols])
    
    mse_values.append(mean_squared_error(test_df['price'], prediction))
    
plt.scatter(hyper_params, mse_values)
plt.show()

## 6. Practice the workflow ##

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
two_mse_values = list()
# Append the second model's MSE values to this list.
three_mse_values = list()
two_hyp_mse = dict()
three_hyp_mse = dict()


for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm='brute')
    knn.fit(train_df[two_features], train_df['price'])
    prediction = knn.predict(test_df[two_features])
    
    two_mse_values.append(mean_squared_error(test_df['price'], prediction))
    
for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm='brute')
    knn.fit(train_df[three_features], train_df['price'])
    prediction = knn.predict(test_df[three_features])
    
    three_mse_values.append(mean_squared_error(test_df['price'], prediction))
    
two = list(enumerate(two_mse_values))
three = list(enumerate(three_mse_values))
    
two.sort(key=lambda x: x[1])
three.sort(key=lambda x: x[1])

two_hyp_mse[two[0][0] + 1] = two[0][1]
three_hyp_mse[three[0][0] + 1] = three[0][1]