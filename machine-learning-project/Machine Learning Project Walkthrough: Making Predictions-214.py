## 1. Recap ##

import pandas as pd

loans = pd.read_csv('cleaned_loans_2007.csv')
loans.info()

## 3. Picking an error metric ##

import pandas as pd

tn = len(loans[(predictions == 0) & (loans['loan_status'] == 0)])
tp = len(loans[(predictions == 1) & (loans['loan_status'] == 1)])
fn = len(loans[(predictions == 0) & (loans['loan_status'] == 1)])
fp = len(loans[(predictions == 1) & (loans['loan_status'] == 0)])

## 5. Class imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))

tn = len(loans[(predictions == 0) & (loans['loan_status'] == 0)])
tp = len(loans[(predictions == 1) & (loans['loan_status'] == 1)])
fn = len(loans[(predictions == 0) & (loans['loan_status'] == 1)])
fp = len(loans[(predictions == 1) & (loans['loan_status'] == 0)])

fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression

features = loans.drop('loan_status', axis=1)
target = loans['loan_status']

lr = LogisticRegression()
lr.fit(features, target)
predictions = lr.predict(features)

## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict, KFold

lr = LogisticRegression()
kf = KFold(features.shape[0], random_state=1)
predictions = pd.Series(cross_val_predict(lr, features, target, cv=kf))

tn = len(loans[(predictions == 0) & (target == 0)])
tp = len(loans[(predictions == 1) & (target == 1)])
fn = len(loans[(predictions == 0) & (target == 1)])
fp = len(loans[(predictions == 1) & (target == 0)])

fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

## 9. Penalizing the classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict

lr = LogisticRegression(class_weight='balanced')
kf = KFold(features.shape[0], random_state=1)
predictions = pd.Series(cross_val_predict(lr, features, target, cv=kf))

tn = len(loans[(predictions == 0) & (target == 0)])
tp = len(loans[(predictions == 1) & (target == 1)])
fn = len(loans[(predictions == 0) & (target == 1)])
fp = len(loans[(predictions == 1) & (target == 0)])

fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

## 10. Manual penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict

penalty = {
    0: 10,
    1: 1
}

lr = LogisticRegression(class_weight=penalty)
kf = KFold(features.shape[0], random_state=1)
predictions = pd.Series(cross_val_predict(lr, features, target, cv=kf))

tn = len(loans[(predictions == 0) & (target == 0)])
tp = len(loans[(predictions == 1) & (target == 1)])
fn = len(loans[(predictions == 0) & (target == 1)])
fp = len(loans[(predictions == 1) & (target == 0)])

fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

## 11. Random forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict

rf = RandomForestClassifier(random_state=1, class_weight='balanced')
kf = KFold(features.shape[0], random_state=1)
predictions = pd.Series(cross_val_predict(rf, features, target, cv=kf))

tn = len(loans[(predictions == 0) & (target == 0)])
tp = len(loans[(predictions == 1) & (target == 1)])
fn = len(loans[(predictions == 0) & (target == 1)])
fp = len(loans[(predictions == 1) & (target == 0)])

fpr = fp / (fp + tn)
tpr = tp / (tp + fn)
