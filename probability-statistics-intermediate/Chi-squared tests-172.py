## 2. Calculating differences ##

female_diff = (10771 - 16280.5) / 16280.5
male_diff = (21790 - 16280.5) / 16280.5

## 3. Updating the formula ##

female_diff = ((10771 - 16280.5) ** 2) / 16280.5
male_diff = ((21790 - 16280.5) ** 2) / 16280.5
gender_chisq = female_diff + male_diff

## 4. Generating a distribution ##

chi_squared_values = []

for _ in range(1000):
    random_nums = numpy.random.random(32561,)
    for i, num in enumerate(random_nums):
        if num < 0.5:
            random_nums[i] = 0
        else:
            random_nums[i] = 1
    male_count = random_nums.tolist().count(0)
    female_count = random_nums.tolist().count(1)
    male_diff = ((male_count - 16280.5) ** 2) / 16280.5
    female_diff = ((female_count - 16280.5) ** 2) / 16280.5
    chi_sq = male_diff + female_diff
    chi_squared_values.append(chi_sq)

plt.hist(chi_squared_values)

## 6. Smaller samples ##

female_diff = ((107.71 - 162.805) ** 2) / 162.805
male_diff = ((217.90 - 162.805) ** 2) / 162.805

gender_chisq = female_diff + male_diff

## 7. Sampling distribution equality ##

chi_squared_values = []

for _ in range(1000):
    random_nums = numpy.random.random(300,)
    bools = (random_nums >= 0.5) * 1
    male_freq = bools.tolist().count(0)
    female_freq = 300 - male_freq
    male_diff = ((150 - male_freq) ** 2) / 150
    female_diff = ((150 - female_freq) ** 2) / 150
    chi_sq = male_diff + female_diff
    chi_squared_values.append(chi_sq)
    
plt.hist(chi_squared_values)
    
    

## 9. Increasing degrees of freedom ##

races = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i in range(len(observed)):
    races.append(((expected[i] - observed[i]) ** 2) / expected[i])

race_chisq = sum(races)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]
chisquare_value, race_pvalue = chisquare(observed, expected)
