## 1. Recap ##

import pandas as pd

loans = pd.read_csv("filtered_loans_2007.csv")
null_counts = loans.isnull().sum()

## 2. Handling missing values ##

loans.drop("pub_rec_bankruptcies", axis=1, inplace=True)
loans.dropna(inplace=True)
loans.dtypes.value_counts()

## 3. Text columns ##

object_columns_df = loans.select_dtypes(include=['object'])
print(object_columns_df.iloc[0])

## 5. First 5 categorical columns ##

cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']

for col in cols:
    print(loans[col].value_counts())
    print()

## 6. The reason for the loan ##

print(loans['purpose'].value_counts())
print()
print(loans['title'].value_counts())

## 7. Categorical columns ##

mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}

cols_to_drop = ['last_credit_pull_d', 'addr_state', 'title', 'earliest_cr_line']
loans.drop(cols_to_drop, axis=1, inplace=True)
loans['int_rate'] = loans['int_rate'].str.rstrip('%')
loans['int_rate'] = loans['int_rate'].astype('float')
loans['revol_util'] = loans['revol_util'].str.rstrip('%')
loans['revol_util'] = loans['revol_util'].astype('float')
loans = loans.replace(mapping_dict)

## 8. Dummy variables ##

cols_to_encode = ['home_ownership', 'verification_status', 'purpose', 'term']
encoded = pd.get_dummies(loans[cols_to_encode])
loans = pd.concat([loans, encoded], axis=1)
loans.drop(cols_to_encode, axis=1, inplace=True)