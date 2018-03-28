## 1. Introduction to the data ##

import pandas as pd

cars = pd.read_csv("auto.csv")
unique_regions = cars['origin'].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars['year'], prefix='year')
cars = pd.concat([cars, dummy_years], axis=1)
cars.drop(['year', 'cylinders'], axis=1, inplace=True)

cars.head()

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

split_ind = int(0.7 * len(cars))

train = shuffled_cars[:split_ind]
test = shuffled_cars[split_ind:]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

features = ['cyl_3', 'cyl_4', 'cyl_5', 'cyl_6', 'cyl_8', 'year_70', 'year_71',
       'year_72', 'year_73', 'year_74', 'year_75', 'year_76', 'year_77',
       'year_78', 'year_79', 'year_80', 'year_81', 'year_82']

X = train[features]

for ind in unique_origins:
    y = train['origin'] == ind
    model = LogisticRegression()
    model.fit(X, y)
    models[ind] = model

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)

for ind in unique_origins:
    prediction = models[ind].predict_proba(test[features])[:, 1]
    testing_probs[ind] = prediction

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)

predicted_origins.value_counts()