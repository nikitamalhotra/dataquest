## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings = dc_listings.iloc[np.random.permutation(dc_listings.shape[0])]
split_one = dc_listings.iloc[:1862]
split_two = dc_listings.iloc[1862:]

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])
prediction = knn.predict(test_one[['accommodates']])
iteration_one_rmse = np.sqrt(mean_squared_error(test_one['price'], prediction))

knn = KNeighborsRegressor()
knn.fit(train_two[['accommodates']], train_two['price'])
prediction = knn.predict(test_two[['accommodates']])
iteration_two_rmse = np.sqrt(mean_squared_error(test_two['price'], prediction))

avg_rmse = np.mean([iteration_one_rmse, iteration_two_rmse])

## 3. K-Fold Cross Validation ##

dc_listings.set_value(dc_listings.index[0:744], "fold", 1)
dc_listings.set_value(dc_listings.index[744:1488], "fold", 2)
dc_listings.set_value(dc_listings.index[1488:2232], "fold", 3)
dc_listings.set_value(dc_listings.index[2232:2976], "fold", 4)
dc_listings.set_value(dc_listings.index[2976:3723], "fold", 5)

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_df = dc_listings[dc_listings['fold'] != 1]
test_df = dc_listings[dc_listings['fold'] == 1]
knn = KNeighborsRegressor()
knn.fit(train_df[['accommodates']], train_df['price'])
prediction = knn.predict(test_df[['accommodates']])
iteration_one_rmse = mean_squared_error(test_df['price'], prediction) ** (1/2)


## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1, 2, 3, 4, 5]

def train_and_validate(df, fold_ids):
    rmses = []
    for fold_id in fold_ids:
        train_df = df[df['fold'] != fold_id]
        test_df = df[df['fold'] == fold_id]
        
        knn = KNeighborsRegressor()
        knn.fit(train_df[['accommodates']], train_df['price'])
        prediction = knn.predict(test_df[['accommodates']])
        rmse = mean_squared_error(test_df['price'], prediction) ** (1/2)
        rmses.append(rmse)
    return rmses

rmses = train_and_validate(dc_listings, fold_ids)

avg_rmse = np.mean(rmses)
print(rmses, avg_rmse)

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold

kf = KFold(n_splits=5, shuffle=True, random_state=1)
knn = KNeighborsRegressor()
mses = cross_val_score(knn, dc_listings[['accommodates']], dc_listings['price'], scoring='neg_mean_squared_error', cv=kf)
avg_rmse = np.mean(np.abs(mses) ** (1/2))


## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))