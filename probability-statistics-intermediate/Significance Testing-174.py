## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)
print(mean_group_a, mean_group_b)

plt.hist(weight_lost_a, alpha=0.7)
plt.hist(weight_lost_b, alpha=0.7)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)

mean_differences = []
for _ in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        if numpy.random.rand() >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
    mean_a = np.mean(group_a)
    mean_b = np.mean(group_b)
    iteration_mean_difference = mean_b - mean_a
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}
for diff in mean_differences:
    sampling_distribution[diff] = sampling_distribution.get(diff, 0) + 1


## 8. P value ##

frequencies = []
for key, value in sampling_distribution.items():
    if key >= 2.52:
        frequencies.append(value)
p_value = sum(frequencies) / 1000