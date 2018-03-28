## 3. Reading in to Pandas ##

import pandas as pd

loans_2007 = pd.read_csv('loans_2007.csv')

print(loans_2007.iloc[0])
print(loans.shape[1])

## 5. First group of columns ##

cols_to_drop = ['id', 'member_id', 'funded_amnt', 'funded_amnt_inv', 'grade', 'sub_grade', 'emp_title', 'issue_d']

loans_2007.drop(cols_to_drop, axis=1, inplace=True)

## 7. Second group of features ##

cols_to_drop = ['zip_code', 'out_prncp', 'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv', 'total_rec_prncp']
loans_2007.drop(cols_to_drop, axis=1, inplace=True)

## 9. Third group of features ##

cols_to_drop = ['total_rec_int', 'total_rec_late_fee', 'recoveries', 
                'collection_recovery_fee', 'last_pymnt_d', 'last_pymnt_amnt']

loans_2007.drop(cols_to_drop, axis=1, inplace=True)

## 10. Target column ##

loans_2007['loan_status'].value_counts()

## 12. Binary classification ##

loans_2007 = loans_2007[(loans_2007['loan_status'] == 'Fully Paid') | (loans_2007['loan_status'] == 'Charged Off')]

mapping_dict = {
    'loan_status': {
        'Fully Paid': 1,
        'Charged Off': 0
    }
}

loans_2007 = loans_2007.replace(mapping_dict)

## 13. Removing single value columns ##

def find_single_valued(df):
    """Returns the names of columns in df with single values (not including np.nan)"""
    
    single_valued = []
    for col in df.columns:
        if len(df[col].dropna().unique()) == 1:
            single_valued.append(col)
    return single_valued

drop_cols = find_single_valued(loans_2007)
loans_2007.drop(drop_cols, axis=1, inplace=True)
print(drop_cols)