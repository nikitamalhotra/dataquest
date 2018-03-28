## 3. Finding Similar Rows With Euclidean Distance ##

selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

def euclidean(row):
    squared_dist = (selected_player[distance_columns] - row) ** 2
    return squared_dist.sum() ** (1 / 2)

lebron_distance = nba[distance_columns].apply(euclidean, axis=1)


## 4. Normalizing Columns ##

nba_numeric = nba[distance_columns]
nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()

## 5. Finding the Nearest Neighbor ##

from scipy.spatial import distance

# Fill in the NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for Lebron James
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between Lebron James and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)

most_similar_to_lebron = nba['player'].iloc[euclidean_distances.nsmallest(2).idxmax()]
print(most_similar_to_lebron)

## 7. Using sklearn ##

# The columns that we'll be using to make predictions
x_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf']
# The column we want to predict
y_column = ["pts"]

from sklearn.neighbors import KNeighborsRegressor
# Create the kNN model
knn = KNeighborsRegressor(n_neighbors=5)
# Fit the model on the training data
knn.fit(train[x_columns], train[y_column])
# Make predictions on the test set using the fit model
predictions = knn.predict(test[x_columns])

## 8. Computing Error ##

actual = test[y_column]

mse = (((predictions - actual) ** 2).sum()) / len(predictions)