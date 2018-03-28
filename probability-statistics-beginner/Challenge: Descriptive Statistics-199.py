## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

## 2. Mean ##

def calc_mean(series):
    return sum(series.values) / len(series.values)

cols = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']
user_reviews = movie_reviews[cols]

means = user_reviews.apply(calc_mean)
rt_mean = means['RT_user_norm']
mc_mean = means['Metacritic_user_nom']
fg_mean = means['Fandango_Ratingvalue']
id_mean = means['IMDB_norm']

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    return sum([(val - mean) ** 2 for val in series]) / len(series)

def std_dev(series):
    return calc_variance(series) ** (1/2)

rt_var, rt_stdev = calc_variance(movie_reviews['RT_user_norm']), std_dev(movie_reviews['RT_user_norm'])

mc_var, mc_stdev = calc_variance(movie_reviews['Metacritic_user_nom']), std_dev(movie_reviews['Metacritic_user_nom'])

fg_var, fg_stdev = calc_variance(movie_reviews['Fandango_Ratingvalue']), std_dev(movie_reviews['Fandango_Ratingvalue'])

id_var, id_stdev = calc_variance(movie_reviews['IMDB_norm']), std_dev(movie_reviews['IMDB_norm'])

## 4. Scatter plots ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 8))

ax1 = fig.add_subplot(3, 1, 1)
ax1.scatter(movie_reviews['RT_user_norm'], movie_reviews['Fandango_Ratingvalue'])
ax1.set_xlim(0, 5)

ax2 = fig.add_subplot(3, 1, 2)
ax2.scatter(movie_reviews['Metacritic_user_nom'], movie_reviews['Fandango_Ratingvalue'])
ax2.set_xlim(0, 5)

ax3 = fig.add_subplot(3, 1, 3)
ax3.scatter(movie_reviews['IMDB_norm'], movie_reviews['Fandango_Ratingvalue'])
ax3.set_xlim(0, 5)
    

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_covariance(series1, series2):
    mean1 = calc_mean(series1)
    mean2 = calc_mean(series2)
    return sum([(val1 - mean1) * (val2 - mean2) for i, val1 in enumerate(series1) for j, val2 in enumerate(series2) if i == j]) / len(series1)

rt_fg_covar = calc_covariance(movie_reviews['RT_user_norm'], movie_reviews['Fandango_Ratingvalue'])

mc_fg_covar = calc_covariance(movie_reviews['Metacritic_user_nom'], movie_reviews['Fandango_Ratingvalue'])

id_fg_covar = calc_covariance(movie_reviews['IMDB_norm'], movie_reviews['Fandango_Ratingvalue'])
                              

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(series_one, series_two):
    return calc_covariance(series_one, series_two) / (calc_variance(series_one) ** (1/2) * calc_variance(series_two) ** (1/2))

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])