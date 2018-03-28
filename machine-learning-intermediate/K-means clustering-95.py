## 1. Clustering NBA Players ##

import pandas as pd
import numpy as np

nba = pd.read_csv("nba_2013.csv")
nba.head(3)

## 2. Point Guards ##

# Enter code here.
point_guards = nba[nba['pos'] == 'PG']
point_guards

## 3. Points Per Game ##

point_guards['ppg'] = point_guards['pts'] / point_guards['g']

# Sanity check, make sure ppg = pts/g
point_guards[['pts', 'g', 'ppg']].head(5)

## 4. Assist Turnover Ratio ##

point_guards = point_guards[point_guards['tov'] != 0]
point_guards['atr'] = point_guards['ast'] / point_guards['tov']

## 5. Visualizing the Point Guards ##

plt.scatter(point_guards['ppg'], point_guards['atr'], c='y')
plt.title("Point Guards")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.show()

## 8. Visualize Centroids ##

plt.scatter(point_guards['ppg'], point_guards['atr'], c='yellow')
plt.scatter(centroids['ppg'], centroids['atr'], c='red')
plt.title("Centroids")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.show()

## 9. Setup (continued) ##

def centroids_to_dict(centroids):
    dictionary = dict()
    # iterating counter we use to generate a cluster_id
    counter = 0

    # iterate a pandas data frame row-wise using .iterrows()
    for index, row in centroids.iterrows():
        coordinates = [row['ppg'], row['atr']]
        dictionary[counter] = coordinates
        counter += 1

    return dictionary

centroids_dict = centroids_to_dict(centroids)

## 11. Step 1 (Continued) ##

# Add the function, `assign_to_cluster`

def assign_to_cluster(player):
    
    player_values = [player['ppg'], player['atr']]
    dists = []
    
    for centroid, coords in centroids_dict.items():
        dist = calculate_distance(coords, player_values)
        dists.append((dist, centroid))
    
    return min(dists)[1]

# This creates the column, `cluster`, by applying assign_to_cluster row-by-row
# Uncomment when ready

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)

## 12. Visualizing Clusters ##

# Visualizing clusters
def visualize_clusters(df, num_clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1])
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)
    plt.show()

visualize_clusters(point_guards, 5)

## 13. Step 2 ##

def recalculate_centroids(df):
    new_centroids_dict = dict()
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        # Finish the logic
        cluster = df[df['cluster'] == cluster_id]
        ppg = cluster['ppg'].mean()
        atr = cluster['atr'].mean()
        new_centroids_dict[cluster_id] = [ppg, atr]
    return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)

## 14. Repeat Step 1 ##

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

## 15. Repeat Step 2 and Step 1 ##

centroids_dict = recalculate_centroids(point_guards)
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

## 16. Challenges of K-Means ##

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg', 'atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards, num_clusters)