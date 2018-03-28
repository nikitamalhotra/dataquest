## 2. Calculating expected values ##

males_over50k = (0.669 * 0.241) * 32561
females_over50k = (0.331 * 0.241) * 32561
males_under50k = (0.669 * 0.759) * 32561
females_under50k = (0.331 * 0.759) * 32561

## 3. Calculating chi-squared ##

expected = [5249.8, 2597.4, 16533.5, 8180.3]
observed = [6662, 1179, 15128, 9592]

chisq_gender_income = 0

for i in range(len(expected)):
    chisq_gender_income += ((expected[i] - observed[i]) ** 2) / expected[i]


    

## 4. Finding statistical significance ##

from scipy.stats import chisquare

expected = [5249.8, 2597.4, 16533.5, 8180.3]
observed = [6662, 1179, 15128, 9592]

chisquare_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import pandas
import numpy as np
from scipy.stats import chi2_contingency

table = pandas.crosstab(income["sex"], [income["race"]])

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)
