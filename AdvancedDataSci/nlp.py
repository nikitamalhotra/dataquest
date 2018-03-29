import pandas as pd
import string
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

submissions = pd.read_csv('stories.csv', names=['id', 'created_at',
                                                'created_at_i', 'author',
                                                'points', 'url_hostname',
                                                'num_comments', 'title'])

submissions.rename(columns={'created_at': 'submission_time',
                            'points': 'upvotes',
                            'url_hostname': 'url',
                            'title': 'headline'}, inplace=True)

submissions.drop(['id', 'created_at_i', 'author', 'num_comments'], axis=1, inplace=True)
submissions.dropna(inplace=True)
submissions = submissions.iloc[:6000]

headlines = submissions['headline'].tolist()
tokenized_headlines = [headline.split(" ") for headline in headlines]

exclude = set(string.punctuation)
clean_tokenized = [[''.join(ch for ch in word if ch not in exclude).lower() for word in headline] for headline in
                   tokenized_headlines]

single_tokens = []

for headline in clean_tokenized:
    single_tokens += headline
unique_tokens = list(set(single_tokens))

counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

for i, clean_list in enumerate(clean_tokenized):
    for token in clean_list:
        if token in unique_tokens:
            counts[token].iloc[i] += 1

word_counts = counts.sum()

cols = word_counts[(word_counts <= 100) & (word_counts >= 5)].index
counts = counts[cols]

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print('RMSE:', rmse)
