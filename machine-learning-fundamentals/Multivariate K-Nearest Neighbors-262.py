## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings.info()

## 2. Removing features ##

columns_to_delete = ['room_type', 'city', 'state', 'latitude', 'longitude', 'zipcode', 'host_response_rate', 'host_acceptance_rate', 'host_listings_count']

dc_listings.drop(columns_to_delete, axis=1, inplace=True)
print(dc_listings.isnull().sum())

## 3. Handling missing values ##

dc_listings.drop(['cleaning_fee', 'security_deposit'], axis=1, inplace=True)
dc_listings.dropna(axis=0, inplace=True)
print(dc_listings.isnull().sum())

## 4. Normalize columns ##

normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())
normalized_listings['price'] = dc_listings['price']
normalized_listings.head(3)

## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance

first_fifth_distance = distance.euclidean(normalized_listings[['accommodates', 'bathrooms']].iloc[0], normalized_listings[['accommodates', 'bathrooms']].iloc[4])

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]

knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
knn.fit(train_df[['accommodates', 'bathrooms']], train_df['price'])
predictions = knn.predict(test_df[['accommodates', 'bathrooms']])
predictions

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.metrics import mean_squared_error
import numpy as np

train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])


two_features_mse = mean_squared_error(test_df['price'], predictions)
two_features_rmse = np.sqrt(two_features_mse)

print(two_features_mse, two_features_rmse)

## 9. Using more features ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
knn.fit(train_df[features], train_df['price'])
four_predictions = knn.predict(test_df[features])

four_mse = mean_squared_error(test_df['price'], four_predictions)
four_rmse = np.sqrt(four_mse)
print(four_mse, four_rmse)

## 10. Using all features ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

cols = [col for col in train_df.columns if col != 'price']

knn = KNeighborsRegressor(algorithm='brute', n_neighbors=5)
knn.fit(train_df[cols], train_df['price'])
all_features_predictions = knn.predict(test_df[cols])

all_features_mse = mean_squared_error(test_df['price'], all_features_predictions)
all_features_rmse = np.sqrt(all_features_mse)
print(all_features_mse, all_features_rmse)