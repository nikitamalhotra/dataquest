## 1. Introduction ##

import pandas as pd
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
filtered_cars = cars[cars['horsepower'] != '?']
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype('float')

## 3. Bias-variance tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    lr = LinearRegression()
    lr.fit(filtered_cars[cols], filtered_cars['mpg'])
    prediction = lr.predict(filtered_cars[cols])
    mse = mean_squared_error(prediction, filtered_cars['mpg'])
    var = np.var(prediction)
    return mse, var

cyl_mse, cyl_var = train_and_test(['cylinders'])
weight_mse, weight_var = train_and_test(['weight'])

## 4. Multivariate models ##

# Our implementation for train_and_test, takes in a list of strings.
def train_and_test(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(filtered_cars["mpg"], predictions)
    variance = np.var(predictions)
    return(mse, variance)

one_mse, one_var = train_and_test(["cylinders"])
two_mse, two_var = train_and_test(['cylinders', 'displacement'])
three_mse, three_var = train_and_test(['cylinders', 'displacement', 'horsepower'])
four_mse, four_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight'])
five_mse, five_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration'])
six_mse, six_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year'])
seven_mse, seven_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin'])

print(one_mse, two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse)
print(one_var, two_var, three_var, four_var, five_var, six_var, seven_var)

## 5. Cross validation ##

from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
import numpy as np

def train_and_cross_val(cols):
    
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    m = len(features)
    
    mses = []
    varis = []
    
    kf = KFold(m, n_folds=10, shuffle=True, random_state=3)
    for train_index, test_index in kf:
        x_train, x_test = features.iloc[train_index], features.iloc[test_index]
        y_train, y_test = target.iloc[train_index], target.iloc[test_index]
    
        lr = LinearRegression()
        lr.fit(x_train, y_train)
        yhat = lr.predict(x_test)
        
        mse = mean_squared_error(yhat, y_test)
        var = np.var(yhat)
        mses.append(mse)
        varis.append(var)
    
    return np.mean(mses), np.mean(varis)

two_mse, two_var = train_and_cross_val(['cylinders', 'displacement'])
three_mse, three_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower'])
four_mse, four_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight'])
five_mse, five_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration'])
six_mse, six_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year'])
seven_mse, seven_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin'])
        
    
    

## 6. Plotting cross-validation error vs. cross-validation variance ##

# We've hidden the `train_and_cross_val` function to save space but you can still call the function!
import matplotlib.pyplot as plt
        
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])

num_features = [2, 3, 4, 5, 6, 7]
mses = [two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse]
varis = [two_var, three_var, four_var, five_var, six_var, seven_var]

plt.scatter([2, 3, 4, 5, 6, 7], mses, c='red')
plt.scatter([2, 3, 4, 5, 6, 7], varis, c='blue')
plt.show()