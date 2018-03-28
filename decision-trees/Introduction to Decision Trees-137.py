## 2. Overview of the Data Set ##

import pandas as pd

# Set index_col to False to avoid pandas thinking that the first column is row indexes (it's age)
income = pandas.read_csv("income.csv", index_col=False)
print(income.head(5))

## 3. Converting Categorical Variables ##

# Convert a single column from text categories to numbers
col = pandas.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))

cols = ['education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'high_income']
for col in cols:
    column = pandas.Categorical.from_array(income[col])
    income[col] = column.codes

## 5. Creating Splits ##

# Enter your code here
private_incomes = income[income['workclass'] == 4]
public_incomes = income[income['workclass'] != 4]

## 9. Overview of Data Set Entropy ##

import math
# We'll do the same calculation we did above, but in Python
# Passing in 2 as the second parameter to math.log will take a base 2 log
entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
print(entropy)

p0 = len(income[income['high_income'] == 0]) / len(income)
p1 = len(income[income['high_income'] == 1]) / len(income)

income_entropy = -(p0 * math.log(p0, 2) + p1 * math.log(p1, 2))

## 11. Information Gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify that our function matches our answer from earlier
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)

median = income['age'].median()
left_branch = income[income['age'] <= median]['high_income']
right_branch = income[income['age'] > median]['high_income']
entropy = calc_entropy(income['high_income'])
entropy_left = calc_entropy(left_branch)
entropy_right = calc_entropy(right_branch)
ratio_left = len(left_branch) / len(income)
ratio_right = len(right_branch) / len(income)

age_information_gain = entropy - (ratio_left * entropy_left + ratio_right * entropy_right)

## 12. Finding the Best Split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data, based on the median
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain
    return original_entropy - to_subtract

# Verify that our answer is the same as on the last screen
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

information_gains = []

for col in columns:
    information_gain = calc_information_gain(income, col, 'high_income')
    information_gains.append(information_gain)

highest_gain = columns[information_gains.index(max(information_gains))]
print(highest_gain)