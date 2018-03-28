## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])

most_bars_country = flags['name'][flags['bars'].idxmax()]
highest_population_country = flags['name'][flags['population'].idxmax()]

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = flags[flags['orange'] == 1].shape[0] / total_countries

stripe_probability = flags[flags['stripes'] > 1].shape[0] / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = 0.5 ** 10
hundred_heads = 0.5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.

red_flags = flags[flags['red'] == 1].shape[0]
total_flags = flags.shape[0]

three_red = (red_flags / total_flags) * ((red_flags - 1) / (total_flags - 1)) * ((red_flags - 2) / (total_flags - 2))

## 5. Disjunctive probability ##

start = 1
end = 18000

hundred_prob = (end / 100) / end

seventy_prob = (len(list(range(0, 18000, 70))) - 1)/ end

## 6. Disjunctive dependent probabilities ##

reds = flags[flags['red'] == 1].shape[0]
oranges = flags[flags['orange'] == 1].shape[0]
stripes = flags[flags['stripes'] >= 1].shape[0]
bars = flags[flags['bars'] >= 1].shape[0]
stripes_and_bars = flags[(flags['stripes'] >=1) & (flags['bars'] >= 1)].shape[0]
red_and_orange = flags[(flags['orange'] == 1) & (flags['red'] == 1)].shape[0]
total = flags.shape[0]

stripes_or_bars = (stripes / total) + (bars / total) - (stripes_and_bars / total)
red_or_orange = (reds / total) + (oranges / total) - (red_and_orange / total)



## 7. Disjunctive probabilities with multiple conditions ##

heads_or = 1 - (0.5 ** 3)