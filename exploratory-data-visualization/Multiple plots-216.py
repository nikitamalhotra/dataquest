## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

plt.plot(unrate['DATE'].iloc[:12], unrate['VALUE'].iloc[:12])
plt.xticks(rotation='vertical')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x1 = unrate['DATE'].iloc[:12]
y1 = unrate['VALUE'].iloc[:12]
x2 = unrate['DATE'].iloc[12:24]
y2 = unrate['VALUE'].iloc[12:24]

ax1.plot(x1, y1)
ax2.plot(x2, y2)

plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##

fig = plt.figure(figsize=(12, 12))

for i in range(5):
    ax = fig.add_subplot(5, 1, i + 1)
    ax.plot(unrate['DATE'].iloc[i*12:(i+1)*12], unrate['VALUE'].iloc[i*12:(i+1)*12])

plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6, 3))
plt.plot(unrate['MONTH'].iloc[:12], unrate['VALUE'].iloc[:12], c='red')
plt.plot(unrate['MONTH'].iloc[12:24], unrate['VALUE'].iloc[12:24], c='blue')

plt.show()

## 9. Adding More Lines ##

fig = plt.figure(figsize=(10, 6))

plt.plot(unrate['MONTH'].iloc[:12], unrate['VALUE'].iloc[:12], c='red')
plt.plot(unrate['MONTH'].iloc[12:24], unrate['VALUE'].iloc[12:24], c='blue')
plt.plot(unrate['MONTH'].iloc[24:36], unrate['VALUE'].iloc[24:36], c='green')
plt.plot(unrate['MONTH'].iloc[36:48], unrate['VALUE'].iloc[36:48], c='orange')
plt.plot(unrate['MONTH'].iloc[48:60], unrate['VALUE'].iloc[48:60], c='black')

plt.show()

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=str(1948 + i))
plt.legend(loc='upper left')
plt.show()


## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')

plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month")
plt.xlabel("Unemployment Rate")
plt.show()