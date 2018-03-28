## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers['Year'] > 1960]

## 5. Consolidating Deaths ##

def yes_no_to_num(val):
    if val == 'YES':
        return 1
    elif val == 'NO':
        return 0

death_cols = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
deaths = true_avengers[death_cols]

for col in death_cols:
    deaths[col] = deaths[col].apply(yes_no_to_num)
    
death_sums = deaths.sum(axis=1, skipna=True)

true_avengers['Deaths'] = death_sums


## 6. Verifying Years Since Joining ##

joined_accuracy_count = int()

for i in range(len(true_avengers['Years since joining'])):
    if true_avengers['Years since joining'].iloc[i]  == (2015 - true_avengers['Year'].iloc[i]):
        joined_accuracy_count += 1