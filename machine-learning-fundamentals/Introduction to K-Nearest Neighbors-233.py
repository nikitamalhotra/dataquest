## 2. Introduction to the data ##

import pandas as pd

dc_listings = pd.read_csv('dc_airbnb.csv')
print(dc_listings.iloc[0])

## 4. Euclidean distance ##

import numpy as np

first_distance = abs(3 - dc_listings['accommodates'].iloc[0])

## 5. Calculate distance for all observations ##

dc_listings['distance'] = dc_listings['accommodates'].apply(lambda x: abs(x - 3))
print(dc_listings['distance'].value_counts())

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)

shuffled_indices = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.iloc[shuffled_indices]
dc_listings.sort_values(by='distance', inplace=True)

dc_listings['price'].head(10)

## 7. Average price ##

stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_commas = stripped_commas.str.replace('$', '')

stripped_commas = pd.to_numeric(stripped_commas)
dc_listings['price'] = stripped_commas
mean_price = np.mean(dc_listings['price'].iloc[:5])

## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    ## Complete the function.
    temp_df['distance'] = abs(new_listing - temp_df['accommodates'])
    temp_df.sort_values(by='distance', inplace=True)
    return temp_df['price'].iloc[:5].mean()

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)