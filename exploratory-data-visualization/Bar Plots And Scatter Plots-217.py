## 2. Introduction to the data ##

import pandas as pd

reviews = pd.read_csv('fandango_scores.csv')
columns_to_keep = ['FILM', 
                   'RT_user_norm', 
                   'Metacritic_user_nom', 
                   'IMDB_norm',
                   'Fandango_Ratingvalue',
                   'Fandango_Stars']

norm_reviews = reviews[columns_to_keep]

## 4. Creating Bars ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, width=0.5)
plt.show()

## 5. Aligning Axis Ticks And Labels ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.bar(left=bar_positions, height=bar_heights, width=0.5)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=90)
plt.xlabel('Rating Source')
plt.ylabel('Average Rating')
plt.title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()

## 6. Horizontal Bar Plot ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.barh(bottom=bar_positions, width=bar_widths, height=0.5)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
plt.ylabel("Rating Source")
plt.xlabel("Average Rating")
plt.title("Average User Rating For Avengers: Age of Ultron (2015)")

plt.show()


## 7. Scatter plot ##

fig, ax = plt.subplots()
xvals = norm_reviews['Fandango_Ratingvalue']
yvals = norm_reviews['RT_user_norm']

ax.scatter(xvals, yvals)
plt.xlabel("Fandango")
plt.ylabel("Rotten Tomatoes")
plt.show()

## 8. Switching axes ##

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x1 = norm_reviews['Fandango_Ratingvalue']
y1 = norm_reviews['RT_user_norm']
x2 = norm_reviews['RT_user_norm']
y2 = norm_reviews['Fandango_Ratingvalue']

ax1.scatter(x1, y1)
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
ax2.scatter(x2, y2)
ax2.set_ylabel('Fandango')
ax2.set_xlabel('Rotten Tomatoes')

plt.show()

## 9. Benchmarking correlation ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(norm_reviews['Fandango_Ratingvalue'], 
            norm_reviews['RT_user_norm'])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)

ax2.scatter(norm_reviews['Fandango_Ratingvalue'],
            norm_reviews['Metacritic_user_nom'])
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)

ax3.scatter(norm_reviews['Fandango_Ratingvalue'], 
            norm_reviews['IMDB_norm'])
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)